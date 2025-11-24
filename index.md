# NIPH/FHI R Packages

A registry of R packages developed and maintained by the Norwegian Institute of Public Health (NIPH/FHI), with a focus on supporting surveillance and analysis of infectious diseases.

## Overview

R packages at NIPH are organized into two levels:

**Project-level packages**: Developed for specific projects or one-off analyses. May have lighter documentation and quality requirements initially.

**Area-level packages**: Shared infrastructure used across multiple teams and reports. Require full documentation, automated testing, and management commitment to succession planning.

## Package Registry

| Package | Level | Maintainer | Status | Documentation |
|---------|-------|-----------|--------|---|
| csdata | Project | Richard Aubrey White | [![CRAN status](https://www.r-pkg.org/badges/version/csdata)](https://cran.r-project.org/package=csdata) | [Link](https://www.csids.no/csdata/) |

## Requirements by Level

### Project-level Packages

- GitHub repository in the `niphr` organization
- README with basic usage examples
- Automated checks via GitHub Actions (basic)

### Area-level Packages

- All project-level requirements
- Full documentation via pkgdown (auto-generated on GitHub Pages)
- Comprehensive GitHub Actions CI/CD (unit tests, R CMD check, code coverage)
- Management sign-off confirming succession plan: at least one additional person trained on the package, or critical functions documented with worked examples
- Version policy documented (breaking changes, deprecation path)

## Governance

### Core Team

FHI maintains a core team (4-5 people) responsible for:

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

### Code Style

All packages must follow the [tidyverse style guide](https://style.tidyverse.org). GitHub Actions can enforce this with the `styler` package.

### Version Policy

- Use YYYY.MM.DD versioning for all releases
- Breaking changes should be documented clearly in release notes
- Deprecation warnings required for at least one release before removal
- All previous versions remain available on GitHub

### Dependencies

- Minimize dependencies on other custom packages when possible
- If a package depends on another custom package, flag this during review
- Cascade maintenance issues must be considered during area-level approval

### Maintenance

- Annual review cycle: core team checks whether packages are still actively used
- Packages not updated in 12+ months will be marked as "maintenance mode"
- Unmaintained packages remain available but receive no updates
- If maintainer leaves: successor must be identified within 1 month, or package moves to maintenance mode

## Getting Started

### Developing a New Package

1. Check this registry to see if a similar package already exists
2. Discuss your idea with your team lead and the core team (to coordinate with ongoing work)
3. Request a repository from the core team—only the core team can create repos in the `niphr` GitHub organization
4. Develop and test your code
5. Submit for core team review when ready

### Moving from Project to Area-level

Your package must meet all area-level requirements (see above). Submit a brief form to the core team including:
- Description of the package and its use cases
- Current maintainer and succession plan (who else is trained?)
- Link to documentation and test coverage
- Expected user base

## For Package Users

All packages are documented on their individual pkgdown sites, linked from the registry above. 

**Questions or issues?** Contact the core team or the individual package maintainer.

---

*Last updated: [DATE]*
*For questions, contact: [CORE TEAM CONTACT]*
