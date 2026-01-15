### 2025-07-08

**Customer facing features: Now available\! 🚀**

* **OIDC authentication** support is now available with dynamic client registration for enterprise login, starting with Moonpay with Okta  [\#3543](https://github.com/ubicloud/ubicloud/pull/3543)  
* **Kubernetes CLI support (v0.1)** is now available with list and create commands [\#3429](https://github.com/ubicloud/ubicloud/pull/3429)  
* New GitHub runner instances get a **free 7-day premium** upgrade with improved UI badges [\#3523](https://github.com/ubicloud/ubicloud/pull/3523)  
* CLI error messages are improved with better validation and help output [\#3513](https://github.com/ubicloud/ubicloud/pull/3513)  
* PostgreSQL failover functionality is enhanced with better planned and unplanned failover handling [\#3575](https://github.com/ubicloud/ubicloud/pull/3575)  
* PostgreSQL cron background workers are enabled by default [\#3552](https://github.com/ubicloud/ubicloud/pull/3552)  
* Read replica creation is now restricted to databases with existing backups [\#3581](https://github.com/ubicloud/ubicloud/pull/3581)

**Customer facing features: Not yet released** ⌛

* New AWS instance types (c6gd, m6gd, m8gd) are added for enhanced performance options [\#3540](https://github.com/ubicloud/ubicloud/pull/3540)  
* PostgreSQL configuration backend will allow advanced database tuning [\#3474](https://github.com/ubicloud/ubicloud/pull/3474)  
* Kubernetes CSI  
* OCR  
* UbiBLK

**Bug fixes / maintenance** 🔧

* \[PG\] PostgreSQL hugepage allocation is fixed to only occur during initial provisioning [\#3536](https://github.com/ubicloud/ubicloud/pull/3536)  
* \[PG\] Primary server configuration is fixed after removing standby nodes [\#3564](https://github.com/ubicloud/ubicloud/pull/3564)  
* \[PG\] Primary server handling is improved when destroyed during read replica creation [\#3566](https://github.com/ubicloud/ubicloud/pull/3566)  
* \[PG\] Representative server fencing is improved with immediate termination [\#3562](https://github.com/ubicloud/ubicloud/pull/3562)  
* \[PG\] Maintenance window parameter handling is fixed to accept zero values [\#3576](https://github.com/ubicloud/ubicloud/pull/3576)  
* \[PG\] S3 endpoint errors are handled to prevent UI crashes [\#3582](https://github.com/ubicloud/ubicloud/pull/3582)  
* \[PG\] WAL file replication is ensured during server transitions [\#3580](https://github.com/ubicloud/ubicloud/pull/3580)  
* \[PG\] WALG credentials bug is fixed for read replicas after promotion [\#3542](https://github.com/ubicloud/ubicloud/pull/3542)  
* \[AWS\] AWS API call safeguards are added to prevent operation failures [\#3548](https://github.com/ubicloud/ubicloud/pull/3548)  
* \[AWS\] PostgreSQL data disk device path detection is fixed on AWS [\#3563](https://github.com/ubicloud/ubicloud/pull/3563)  
* \[AWS\] Error handling is improved for AWS entity deletion operations [\#3559](https://github.com/ubicloud/ubicloud/pull/3559)  
* \[AWS\] Lots of Ubi on AWS related fixes [\#3560](https://github.com/ubicloud/ubicloud/pull/3560)  
* \[GHA\] GitHub runner JIT token corruption logging is improved for better debugging [\#3549](https://github.com/ubicloud/ubicloud/pull/3549)  
* \[GHA\] Blob storage destruction error handling is enhanced [\#3556](https://github.com/ubicloud/ubicloud/pull/3556)  
* \[Networking\] NIC destruction redundancy is removed to prevent double processing [\#3561](https://github.com/ubicloud/ubicloud/pull/3561)  
* \[Bump\] Tilt gem is updated to version 2.6.1 for parallel testing fixes [\#3585](https://github.com/ubicloud/ubicloud/pull/3585)

**Internal improvements** 🌟

* \[Clover\] Database locking is improved to reduce unnecessary blocking [\#3545](https://github.com/ubicloud/ubicloud/pull/3545)	  
* \[CI\] Clover workflow environment setup is unified with shared actions [\#3399](https://github.com/ubicloud/ubicloud/pull/3399)  
* \[CI\] Control plane tests now run in parallel for faster CI execution [\#3555](https://github.com/ubicloud/ubicloud/pull/3555)  
* \[CI\] E2E tests are enhanced with mail server and Stripe test configurations [\#3571](https://github.com/ubicloud/ubicloud/pull/3571)  
* \[CI\] E2E test performance is improved with dual respirate processes [\#3572](https://github.com/ubicloud/ubicloud/pull/3572)  
* \[GHA\] GitHub runner script service descriptions are made explicit for security [\#3551](https://github.com/ubicloud/ubicloud/pull/3551)  
* \[GHA\] JIT configuration is now passed via file for better reliability [\#3570](https://github.com/ubicloud/ubicloud/pull/3570)  
* \[CLI\] Golden file handling is improved for case-insensitive filesystems [\#3547](https://github.com/ubicloud/ubicloud/pull/3547)  
* \[PG\] Bootstrap rhizome waiting time is reduced from 120 to 5 seconds [\#3565](https://github.com/ubicloud/ubicloud/pull/3565)  
* \[AWS\] Subnet and NIC operations are optimized for AWS locations [\#3574](https://github.com/ubicloud/ubicloud/pull/3574)
