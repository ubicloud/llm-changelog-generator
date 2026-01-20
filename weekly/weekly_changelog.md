## 2026-01-13

**Customer facing features: Now available\! 🚀**

* Included the `created_at` field in the PostgreSQL list API to support sorting and improve general observability [\#4496](https://github.com/ubicloud/ubicloud/pull/4496)  
* Added `pg_config` & `pgbouncer_config` to endpoints for creating read replicas [\#4527](https://github.com/ubicloud/ubicloud/pull/4527)  
* Added a "deleting" state for private subnets to clearly indicate when a resource is in the process of being destroyed [\#4532](https://github.com/ubicloud/ubicloud/pull/4532)

**External Communication** 📣

* Dec 2025 Changelog

**Customer facing features: Not yet released ⌛**

* Dist Inference  
* Clickhouse  
* UbiBLK  
  * Configured `ubiblk` as the default storage backend for all newly provisioned hosts [\#4534](https://github.com/ubicloud/ubicloud/pull/4534)

**Bug fixes / maintenance / internals 🔧**

* **PostgreSQL**  
  * Implemented monitoring for PostgreSQL archival backlogs to trigger alerts when WAL files exceed thresholds [\#4487](https://github.com/ubicloud/ubicloud/pull/4487)  
  * Updated the `paradedb` image to include the `wal-g` service file [\#4506](https://github.com/ubicloud/ubicloud/pull/4506)  
  * Updated `PostgresResourceNexus.assemble` to accept tags [\#4495](https://github.com/ubicloud/ubicloud/pull/4495)  
  * Fixed a bug in `wal-g` where stale credentials were used when switching to a new PostgreSQL timeline [\#4520](https://github.com/ubicloud/ubicloud/pull/4520)  
  * Resolved a `NoMethodError` on the PostgreSQL creation page when selecting unsupported flavors [\#4521](https://github.com/ubicloud/ubicloud/pull/4521)  
  * Handled cases where `lsn_monitor` is nil during PostgreSQL failover target selection [\#4524](https://github.com/ubicloud/ubicloud/pull/4524)  
  * Corrected the sha256 checksum for the `postgres_paradedb` image [\#4510](https://github.com/ubicloud/ubicloud/pull/4510)  
* **Networking**  
  * Improved random IP selection by switching from infinite recursion to bounded iteration [\#4371](https://github.com/ubicloud/ubicloud/pull/4371)  
  * Added retry logic and safety deadlines for AWS network interface and security group deletion to handle transient "in use" errors [\#4493](https://github.com/ubicloud/ubicloud/pull/4493)  
  * Introduced a configuration option to limit SSH access to specific IP ranges, enhancing security for private environments [\#4509](https://github.com/ubicloud/ubicloud/pull/4509)  
* **Framework**  
  * Refactored state machine logic to use a centralized `destroying` semaphore for label checks [\#4317](https://github.com/ubicloud/ubicloud/pull/4317), [\#4480](https://github.com/ubicloud/ubicloud/pull/4480)  
  * Optimized `Clog.emit` to accept metadata as an argument instead of a block to improve performance [\#4523](https://github.com/ubicloud/ubicloud/pull/4523), [\#4525](https://github.com/ubicloud/ubicloud/pull/4525)  
  * Removed unnecessary Sequel association options [\#4488](https://github.com/ubicloud/ubicloud/pull/4488) [\#4366](https://github.com/ubicloud/ubicloud/pull/4366) [\#4539](https://github.com/ubicloud/ubicloud/pull/4539)  
  * Added a `before_destroy` callback to the base progress class to handle one-time cleanup logic [\#4485](https://github.com/ubicloud/ubicloud/pull/4485)  
  * Corrected the `display_state` method to properly handle the destroying semaphore across multiple models [\#4474](https://github.com/ubicloud/ubicloud/pull/4474)  
  * Updated KMS key handling to avoid unnecessary base64 decoding [\#4515](https://github.com/ubicloud/ubicloud/pull/4515)  
  * Added a database constraint to prevent negative hugepage deallocation [\#4529](https://github.com/ubicloud/ubicloud/pull/4529)  
  * Optimized `Util.exception_to_hash` to reduce hash allocations and support nested exception causes [\#4465](https://github.com/ubicloud/ubicloud/pull/4465)  
  * Fixed double-nested exception logging [\#4511](https://github.com/ubicloud/ubicloud/pull/4511)  
  * Fixed an issue where `PageNexus.assemble` would ignore updates to existing active pages [\#4449](https://github.com/ubicloud/ubicloud/pull/4449)  
  * Updated `openssl` to version 4.0.0 and simplified exception handling for public keys [\#4499](https://github.com/ubicloud/ubicloud/pull/4499)  
  * Added `Sshable#write_file` to standardize file writing operations over SSH [\#4516](https://github.com/ubicloud/ubicloud/pull/4516)  
  * Added UUID type validation to configuration for earlier error detection [\#4498](https://github.com/ubicloud/ubicloud/pull/4498)  
  * Remove LocationCredential project association [\#4500](https://github.com/ubicloud/ubicloud/pull/4500)  
* **Admin**  
  * Added a new admin page to search for VMs by IPv4 address, covering both active and recently archived instances [\#4505](https://github.com/ubicloud/ubicloud/pull/4505)  
  * Enhanced the admin panel by adding billing and payment method tables and converting raw Stripe JSON data into a readable format [\#4517](https://github.com/ubicloud/ubicloud/pull/4517)  
* **Dev**  
  * Updated PostgreSQL dependency instructions for Debian/Ubuntu to include `pkg-config` [\#4315](https://github.com/ubicloud/ubicloud/pull/4315)  
  * Slack messages to remind PRs waiting for reviews\!  
* **Fleet**  
  * Added a `VmHost` health check to verify the clock source is set to `tsc` or `arch_sys_counter`, preventing monotonic time errors [\#4419](https://github.com/ubicloud/ubicloud/pull/4419)  
* **Tests**  
  * Backported FDR demock changes [\#4476](https://github.com/ubicloud/ubicloud/pull/4476)  
  * Replaced heavy mocks with real objects in `postgres_server_nexus_spec` [\#4503](https://github.com/ubicloud/ubicloud/pull/4503)  
  * Fixed flaky tests related to `Clog` emissions in `vpc_nexus_spec.rb` [\#4508](https://github.com/ubicloud/ubicloud/pull/4508)  
* **Version bumps**  
  * Upgraded Ruby development dependencies, including `concurrent-ruby`, `herb`, `prism`, and `unicode-emoji` [\#4477](https://github.com/ubicloud/ubicloud/pull/4477)  
  * Upgraded JavaScript dependencies including `@redocly/cli`, `openapi-format`, and `undici` [\#4491](https://github.com/ubicloud/ubicloud/pull/4491)