### **Customer facing features: Now available!** 🚀

- Kubernetes cluster management is now available in CLI with list and create commands [#3429](https://github.com/ubicloud/ubicloud/pull/3429)
- PostgreSQL configuration management is added with support for custom PostgreSQL and PgBouncer settings [#3474](https://github.com/ubicloud/ubicloud/pull/3474)
- OIDC authentication support is now available with dynamic client registration for enterprise login [#3543](https://github.com/ubicloud/ubicloud/pull/3543)
- New GitHub runner instances get a free 7-day premium upgrade with improved UI badges [#3523](https://github.com/ubicloud/ubicloud/pull/3523)
- CLI error messages are improved with better validation and help output [#3513](https://github.com/ubicloud/ubicloud/pull/3513)
- PostgreSQL failover functionality is enhanced with better planned and unplanned failover handling [#3575](https://github.com/ubicloud/ubicloud/pull/3575)
- Read replica creation is now restricted to databases with existing backups [#3581](https://github.com/ubicloud/ubicloud/pull/3581)

**Customer facing features: Not yet released** ⌛

- New AWS instance types (c6gd, m6gd, m8gd) are added for enhanced performance options [#3540](https://github.com/ubicloud/ubicloud/pull/3540)
- PostgreSQL configuration backend will allow advanced database tuning [#3474](https://github.com/ubicloud/ubicloud/pull/3474)

**Bug fixes / maintenance** 🔧

- PostgreSQL hugepage allocation is fixed to only occur during initial provisioning [#3536](https://github.com/ubicloud/ubicloud/pull/3536)
- WALG credentials bug is fixed for read replicas after promotion [#3542](https://github.com/ubicloud/ubicloud/pull/3542)
- GitHub runner JIT token corruption logging is improved for better debugging [#3549](https://github.com/ubicloud/ubicloud/pull/3549)
- PostgreSQL data disk device path detection is fixed on AWS [#3563](https://github.com/ubicloud/ubicloud/pull/3563)
- Primary server configuration is fixed after removing standby nodes [#3564](https://github.com/ubicloud/ubicloud/pull/3564)
- Maintenance window parameter handling is fixed to accept zero values [#3576](https://github.com/ubicloud/ubicloud/pull/3576)
- S3 endpoint errors are handled to prevent UI crashes [#3582](https://github.com/ubicloud/ubicloud/pull/3582)
- Database locking is improved to reduce unnecessary blocking [#3545](https://github.com/ubicloud/ubicloud/pull/3545)
- AWS API call safeguards are added to prevent operation failures [#3548](https://github.com/ubicloud/ubicloud/pull/3548)
- Error handling is improved for AWS entity deletion operations [#3559](https://github.com/ubicloud/ubicloud/pull/3559)
- Blob storage destruction error handling is enhanced [#3556](https://github.com/ubicloud/ubicloud/pull/3556)
- NIC destruction redundancy is removed to prevent double processing [#3561](https://github.com/ubicloud/ubicloud/pull/3561)
- WAL file replication is ensured during server transitions [#3580](https://github.com/ubicloud/ubicloud/pull/3580)

**Internal improvements** 🌟

- Clover workflow environment setup is unified with shared actions [#3399](https://github.com/ubicloud/ubicloud/pull/3399)
- Control plane tests now run in parallel for faster CI execution [#3555](https://github.com/ubicloud/ubicloud/pull/3555)
- E2E tests are enhanced with mail server and Stripe test configurations [#3571](https://github.com/ubicloud/ubicloud/pull/3571)
- E2E test performance is improved with dual respirate processes [#3572](https://github.com/ubicloud/ubicloud/pull/3572)
- GitHub runner script service descriptions are made explicit for security [#3551](https://github.com/ubicloud/ubicloud/pull/3551)
- JIT configuration is now passed via file for better reliability [#3570](https://github.com/ubicloud/ubicloud/pull/3570)
- PostgreSQL cron background workers are enabled by default [#3552](https://github.com/ubicloud/ubicloud/pull/3552)
- Golden file handling is improved for case-insensitive filesystems [#3547](https://github.com/ubicloud/ubicloud/pull/3547)
- Bootstrap rhizome waiting time is reduced from 120 to 5 seconds [#3565](https://github.com/ubicloud/ubicloud/pull/3565)
- Subnet and NIC operations are optimized for AWS locations [#3574](https://github.com/ubicloud/ubicloud/pull/3574)
- OIDC authentication is restricted to client-secret-basic for better compatibility [#3583](https://github.com/ubicloud/ubicloud/pull/3583)
- Tilt gem is updated to version 2.6.1 for parallel testing fixes [#3585](https://github.com/ubicloud/ubicloud/pull/3585)
- Representative server fencing is improved with immediate termination [#3562](https://github.com/ubicloud/ubicloud/pull/3562)
- Primary server handling is improved when destroyed during read replica creation [#3566](https://github.com/ubicloud/ubicloud/pull/3566)