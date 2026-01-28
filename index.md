# NIPH/FHI R Packages

A registry of R packages developed and maintained by the Norwegian Institute of Public Health (NIPH/FHI), with a focus on supporting surveillance and analysis of infectious diseases.

## Overview

R packages at NIPH are organized into two levels:

**Project-level packages**: Developed for specific projects or one-off analyses. May have lighter documentation and quality requirements initially.

**Area-level packages**: Shared infrastructure used across multiple teams and reports. Require full documentation, automated testing, and management commitment to succession planning.

## Package Registry

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

## Requirements by Level

### Project-level Packages

- GitHub repository in the `niphr` organization
- README with basic usage examples
- Automated checks via GitHub Actions (basic)

### Area-level Packages

- All project-level requirements
- Full documentation via pkgdown (auto-generated on GitHub Pages)
- Comprehensive GitHub Actions CI/CD (unit tests, R CMD check, code coverage targeting 80%+)
- Management sign-off confirming succession plan: at least one additional person trained on the package, or critical functions documented with worked examples
- Version policy documented (breaking changes, deprecation path)

## Governance

### Core Team

NIPH maintains a core team (4-5 people) responsible for:

- Developing and maintaining standardized coding practices and documentation guidelines
- Establishing and updating quality standards for R packages
- Coordinating new package development to avoid duplication
- Providing guidance and training to package developers
- Maintaining this registry

**The core team does not execute package development**—developers own their packages and coordinate with the core team.

### Decision Authority

The core team can:
- Provide technical review and guidance on package structure and quality
- Recommend whether packages meet standards for area-level promotion
- Flag dependencies or conflicts with existing packages

The core team cannot:
- Unilaterally block package development
- Require specific coding styles beyond documented guidelines
- Force someone to maintain a package

### Management Oversight

A steering group (typically area leadership) approves:
- Resource allocation for package development and maintenance
- Promotion of packages to area-level status
- Major policy or standard changes

## Technical Standards

### Project-level: Required

**Sensitive data**: Packages must not contain real patient data, surveillance records, or other sensitive information. Use only synthetic or publicly available example data.

**Licensing**: All packages should use the MIT license unless there is a specific reason to choose otherwise.

**GitHub Actions**: All packages use GitHub Actions for continuous integration. The standard workflow runs `R CMD check --as-cran` on pushes to `main` and `develop`, and on pull requests to `main`. See [csalert's workflow](https://github.com/niphr/csalert/blob/main/.github/workflows/check-and-pkgdown.yml) as a reference.

### Project-level: Desirable

**Code style**: Packages should follow the [tidyverse style guide](https://style.tidyverse.org). Code should be formatted using [air](https://positron.posit.co/guide-r-air.html) (see this [introduction to air](https://tidyverse.org/blog/2025/02/air/)).

**Testing**: Packages should use [testthat](https://testthat.r-lib.org) for unit testing. See the [R Packages testing chapter](https://r-pkgs.org/testing-basics.html) for guidance.

**Documentation**: Packages should use [roxygen2](https://roxygen2.r-lib.org) for function documentation and [pkgdown](https://pkgdown.r-lib.org) to generate documentation websites. Package websites are hosted on GitHub Pages at `niphr.github.io/<package-name>/`.

**CRAN submission** (if applicable):
- Must pass `R CMD check --as-cran` with no ERRORs or WARNINGs
- NOTEs should be minimized and justified
- Coordinate submission timing with the core team

### Area-level: Required

All project-level requirements and desirables become mandatory, plus:

**Testing coverage**: Unit tests targeting 80%+ code coverage.

**Version policy**:
- Use YYYY.MM.DD versioning for all releases
- Breaking changes documented clearly in release notes
- Deprecation warnings required for at least one release before removal

**Dependencies**: Minimize dependencies on other custom packages. If a package depends on another custom package, flag this during review. Cascade maintenance issues must be considered during approval.

**Maintenance**:
- Annual review cycle: core team checks whether packages are still actively used
- Packages not updated in 12+ months will be marked as "maintenance mode"
- Unmaintained packages remain available but receive no updates
- If maintainer leaves: successor must be identified within 1 month, or package moves to maintenance mode

## Getting Started

### Developing a New Package

1. Check this registry to see if a similar package already exists
2. Discuss your idea with your team lead and the core team (to coordinate with ongoing work)
3. **Request a repository from the core team**. The core team will create the repository with the standard structure (GitHub Actions, license, pkgdown configuration). Only the core team can create repos in the `niphr` GitHub organization.
4. Develop and test your code following the technical standards above
5. Submit for core team review when ready

### Moving from Project to Area-level

Your package must meet all area-level requirements (see above). Submit a brief form to the core team including:
- Description of the package and its use cases
- Current maintainer and succession plan (who else is trained?)
- Link to documentation and test coverage
- Expected user base

The core team will review and provide a recommendation. Final approval requires sign-off from the steering group (area leadership), which includes a commitment to provide sufficient resources to maintain the succession plan.

## Resources

- [R Packages (2e)](https://r-pkgs.org) — comprehensive guide to R package development
- [tidyverse style guide](https://style.tidyverse.org) — code style reference
- [air](https://positron.posit.co/guide-r-air.html) — code formatter for R

---

*Last updated: 2026-01-28*
*For questions, contact: RichardAubrey.White@fhi.no*
