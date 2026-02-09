## Overview

We organize packages into two levels:

**Project-level packages**: Built for specific projects or one-off analyses. Documentation and testing requirements are lighter.

**Area-level packages**: Shared infrastructure used across multiple teams. These need full documentation, automated testing, and a succession plan.

## Package registry

| Package | Level | Maintainer | Status |
|---------|-------|-----------|--------|
| [cs9](https://niphr.github.io/cs9/) | Project | Richard Aubrey White | [![CRAN status](https://www.r-pkg.org/badges/version/cs9)](https://cran.r-project.org/package=cs9) |
| [csalert](https://niphr.github.io/csalert/) | Project | Richard Aubrey White | [![CRAN status](https://www.r-pkg.org/badges/version/csalert)](https://cran.r-project.org/package=csalert) |
| [csdata](https://niphr.github.io/csdata/) | Project | Richard Aubrey White | [![CRAN status](https://www.r-pkg.org/badges/version/csdata)](https://cran.r-project.org/package=csdata) |
| [csdb](https://niphr.github.io/csdb/) | Project | Richard Aubrey White | [![CRAN status](https://www.r-pkg.org/badges/version/csdb)](https://cran.r-project.org/package=csdb) |
| [csmaps](https://niphr.github.io/csmaps/) | Project | Richard Aubrey White | [![CRAN status](https://www.r-pkg.org/badges/version/csmaps)](https://cran.r-project.org/package=csmaps) |
| [csstyle](https://niphr.github.io/csstyle/) | Project | Richard Aubrey White | [![CRAN status](https://www.r-pkg.org/badges/version/csstyle)](https://cran.r-project.org/package=csstyle) |
| [cstidy](https://niphr.github.io/csdata/) | Project | Richard Aubrey White | [![CRAN status](https://www.r-pkg.org/badges/version/cstidy)](https://cran.r-project.org/package=cstidy) |
| [csutil](https://niphr.github.io/csdata/) | Project | Richard Aubrey White | [![CRAN status](https://www.r-pkg.org/badges/version/csutil)](https://cran.r-project.org/package=csutil) |

## Requirements by level

### Project-level packages

- GitHub repository in the `niphr` organization
- README with basic usage examples
- GitHub Actions running basic checks

### Area-level packages

- Everything required for project-level, plus:
- pkgdown documentation site on GitHub Pages
- GitHub Actions CI/CD with unit tests, R CMD check, and 80%+ code coverage
- Management sign-off on succession plan: someone else trained on the package, or critical functions documented with worked examples
- Version policy documented (how you handle breaking changes and deprecation)

## Governance

### Core team

A core team of 4-5 people handles:

- Coding practices and documentation guidelines
- Quality standards for R packages
- Coordinating new packages to avoid duplication
- Training and guidance for developers
- This registry

The core team doesn't build packages. Developers own their packages and coordinate with the core team as needed.

### What the core team can and can't do

The core team can:
- Review packages and give technical guidance
- Recommend whether a package is ready for area-level
- Flag dependency issues or conflicts with existing packages

The core team can't:
- Block package development unilaterally
- Require coding styles beyond what's documented here
- Force anyone to maintain a package

### Management oversight

A steering group (usually area leadership) approves:
- Resources for package development and maintenance
- Promotion to area-level
- Major policy changes

## Technical standards

### Project-level: required

**Sensitive data**: No real patient data, surveillance records, or other sensitive information. Use synthetic or publicly available example data only.

**Licensing**: Use MIT unless you have a reason not to.

**GitHub Actions**: All packages run `R CMD check --as-cran` on pushes to `main` and `develop`, and on pull requests to `main`. See [csalert's workflow](https://github.com/niphr/csalert/blob/main/.github/workflows/check-and-pkgdown.yml) for reference.

### Project-level: desirable

**Code style**: Follow the [tidyverse style guide](https://style.tidyverse.org). Format code with [air](https://positron.posit.co/guide-r-air.html) (see this [introduction to air](https://tidyverse.org/blog/2025/02/air/)).

**Testing**: Use [testthat](https://testthat.r-lib.org). See the [R Packages testing chapter](https://r-pkgs.org/testing-basics.html).

**Documentation**: Use [roxygen2](https://roxygen2.r-lib.org) for function docs and [pkgdown](https://pkgdown.r-lib.org) for the website. Package sites live at `niphr.github.io/<package-name>/`.

**CRAN submission** (if applicable):
- Pass `R CMD check --as-cran` with no ERRORs or WARNINGs
- Minimize NOTEs and justify any that remain
- Coordinate timing with the core team

### Area-level: required

Everything above becomes mandatory, plus:

**Testing coverage**: 80%+ code coverage.

**Version policy**:
- Use YYYY.MM.DD versioning
- Document breaking changes in release notes
- Deprecation warnings for at least one release before removing anything

**Dependencies**: Keep dependencies on other custom packages to a minimum. Flag any such dependencies during review so we can think through maintenance implications.

**Maintenance**:
- Annual review: core team checks that the maintainer is still at NIPH and still wants to maintain the package
- If the maintainer has left or no longer wants to maintain it: find a successor within 1 month, or the package moves to maintenance mode
- Maintenance mode means the package stays available but won't receive updates

## Getting started

### Developing a new package

1. Check this registry for similar packages
2. Talk to your team lead and the core team to coordinate
3. **Request a repository from the core team**. They'll create it with standard setup (GitHub Actions, license, pkgdown config). Only the core team can create repos in `niphr`.
4. Build and test following the standards above
5. Submit for core team review when ready

### Moving from project to area-level

Your package needs to meet all area-level requirements. Submit a brief form to the core team with:
- What the package does and who uses it
- Current maintainer and succession plan (who else knows it?)
- Link to documentation and test coverage
- Expected user base

The core team reviews and makes a recommendation. Final approval comes from the steering group, meaning they also commit to funding the succession plan.

## Resources

- [R Packages (2e)](https://r-pkgs.org) - the book on R package development
- [tidyverse style guide](https://style.tidyverse.org) - code style reference
- [air](https://positron.posit.co/guide-r-air.html) - code formatter for R

---

*Last updated: 2026-01-28*
*Questions? Contact RichardAubrey.White@fhi.no*
