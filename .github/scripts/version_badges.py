#!/usr/bin/env python3
"""Write shields.io endpoint badges comparing each niphr package's r-universe
(development) version against its CRAN version.

  green  = development version matches CRAN
  orange = development version differs from CRAN (a CRAN release is due)
  blue   = package is not on CRAN

The package list is discovered from the r-universe, so any new niphr package is
picked up automatically.
"""
import json
import os
import urllib.request

UNIVERSE = "https://niphr.r-universe.dev"
CRANDB = "https://crandb.r-pkg.org"
OUTDIR = "badges"


def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "niphr-version-badges"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except Exception:
        return None


def cran_version(pkg):
    data = fetch_json(f"{CRANDB}/{pkg}")
    if not isinstance(data, dict) or "error" in data:
        return None
    return data.get("Version")


def as_numbers(version):
    parts = []
    for part in version.replace("-", ".").split("."):
        parts.append(int(part) if part.isdigit() else 0)
    return tuple(parts)


def main():
    packages = fetch_json(f"{UNIVERSE}/api/packages") or []
    os.makedirs(OUTDIR, exist_ok=True)
    for entry in packages:
        pkg = entry.get("Package")
        dev = entry.get("Version")
        if not pkg or not dev:
            continue
        cran = cran_version(pkg)
        if cran is None:
            color = "blue"
        elif as_numbers(dev) == as_numbers(cran):
            color = "brightgreen"
        else:
            color = "orange"
        badge = {
            "schemaVersion": 1,
            "label": "r-universe",
            "message": dev,
            "color": color,
            "cacheSeconds": 3600,
        }
        with open(os.path.join(OUTDIR, f"{pkg}.json"), "w") as fh:
            json.dump(badge, fh)
        print(f"{pkg}: dev={dev} cran={cran} -> {color}")


if __name__ == "__main__":
    main()
