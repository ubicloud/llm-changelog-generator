**Customer facing features: Now available!** 🚀

- Kubernetes cluster management added to CLI with list and create commands #[3429](https://github.com/ubicloud/ubicloud/pull/3429)
- PostgreSQL configuration management API for customizing database settings #[3474](https://github.com/ubicloud/ubicloud/pull/3474)
- New 7-day free premium runner trial for new GitHub installations #[3523](https://github.com/ubicloud/ubicloud/pull/3523)
- Improved CLI error messages with better help output for invalid options #[3513](https://github.com/ubicloud/ubicloud/pull/3513)
- OIDC authentication support for single sign-on integration #[3543](https://github.com/ubicloud/ubicloud/pull/3543)
- PostgreSQL read replica creation now requires existing backups for data safety #[3581](https://github.com/ubicloud/ubicloud/pull/3581)

**Customer facing features: Not yet released** ⌛

- New AWS instance types (c6gd, m6gd, m8gd) for improved performance options #[3540](https://github.com/ubicloud/ubicloud/pull/3540)
- Enhanced PostgreSQL on AWS with better disk handling and instance management #[3560](https://github.com/ubicloud/ubicloud/pull/3560)

**Bug fixes / maintenance** 🔧

- Fixed PostgreSQL maintenance window scheduling to properly accept midnight (00:00) times #[3576](https://github.com/ubicloud/ubicloud/pull/3576)
- Fixed read replica credential refresh after promotion #[3542](https://github.com/ubicloud/ubicloud/pull/3542)
- Fixed PostgreSQL primary server hanging when removing standby nodes #[3564](https://github.com/ubicloud/ubicloud/pull/3564)
- Fixed S3 endpoint errors causing UI crashes on fresh PostgreSQL deployments #[3582](https://github.com/ubicloud/ubicloud/pull/3582)
- Fixed PostgreSQL data disk identification on AWS instances #[3563](https://github.com/ubicloud/ubicloud/pull/3563)
- Improved GitHub runner error handling for corrupted JIT tokens #[3549](https://github.com/ubicloud/ubicloud/pull/3549)
- Fixed GitHub runner service descriptions to prevent token exposure #[3551](https://github.com/ubicloud/ubicloud/pull/3551)

**Internal improvements** 🌟

- Control plane tests now run in parallel, reducing CI time by 2-3x #[3555](https://github.com/ubicloud/ubicloud/pull/3555)
- Unified workflow environment setup across CI/CD pipelines #[3399](https://github.com/ubicloud/ubicloud/pull/3399)
- Enhanced PostgreSQL failover with separate planned and unplanned modes #[3575](https://github.com/ubicloud/ubicloud/pull/3575)
- Improved AWS API error handling to prevent unnecessary failures #[3548](https://github.com/ubicloud/ubicloud/pull/3548)
- Database lock optimizations using FOR NO KEY UPDATE for better concurrency #[3545](https://github.com/ubicloud/ubicloud/pull/3545)
- E2E test environment enhanced with mail server and Stripe test configuration #[3571](https://github.com/ubicloud/ubicloud/pull/3571)