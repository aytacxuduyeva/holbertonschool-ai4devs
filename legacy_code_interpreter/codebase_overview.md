# Codebase Overview - Legacy e-Commerce Engine

## Age
Initial release in 2011. The core architecture has remained largely unchanged since the last major release (v2.4) in late 2014.

## Size
Approximately **112,000 Lines of Code (LOC)**, distributed as follows:
- Java: ~88,000 LOC
- XML Configuration: ~14,000 LOC
- Legacy JSP Templates: ~10,000 LOC

## Dependencies
- **Spring Framework 3.2.x**: Legacy XML-based dependency injection.
- **Hibernate 4.1**: Outdated ORM version.
- **Apache Struts 2**: High security maintenance overhead.
- **Oracle JDBC 11g**: Tied to specific legacy database versions.

## Known Issues or Pain Points
- **God Objects**: The `OrderProcessor` class exceeds 5,000 lines, handling disparate tasks like tax, shipping, and billing.
- **Lack of Automation**: No CI/CD pipeline; deployments are manual and require significant downtime.
- **Technical Debt**: Unit test coverage is below 15%, making refactoring extremely risky.
- **Hard-coded Configurations**: Many environment-specific settings are hard-coded or buried in XML files.
- **Database Logic Leakage**: Significant business logic is stored in database procedures rather than the application layer.

