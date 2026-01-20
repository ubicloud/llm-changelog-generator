## 2026-01-20

**Customer facing features: Now available! 🚀**

* Extended AWS PostgreSQL instance sizes with new `i8ge`, `i7i`, and `i7ie` families, providing more options for high-performance workloads [#4307](https://github.com/ubicloud/ubicloud/pull/4307)

* Added the ability to specify a private subnet name when creating a PostgreSQL database via API/CLI, simplifying scripting workflows by allowing firewall rules to be added directly without parsing creation output [#4482](https://github.com/ubicloud/ubicloud/pull/4482)

* Added DNS AAAA records for non-AWS PostgreSQL databases, enabling IPv6 connectivity [#4502](https://github.com/ubicloud/ubicloud/pull/4502)

* Added `pg_config`, `pgbouncer_config`, and `tags` support to PostgreSQL read replica creation endpoints [#4527](https://github.com/ubicloud/ubicloud/pull/4527)

* Added `default_pg_config` to the PostgreSQL config API endpoint, showing computed configuration values alongside explicit user overrides [#4553](https://github.com/ubicloud/ubicloud/pull/4553)

* Added "deleting" display state to private subnets, making it clear when a resource is being destroyed rather than showing "available" until completion [#4532](https://github.com/ubicloud/ubicloud/pull/4532)

* Added "restarting" display state to PostgreSQL resources when the representative server's strand is in the `restart` label [#4571](https://github.com/ubicloud/ubicloud/pull/4571)

**Customer facing features: Not yet released ⌛**

* **Distributed Inference**
  * Added monitoring for inference router endpoints using the new `stats` endpoint to collect health status and trigger alerts [#4356](https://github.com/ubicloud/ubicloud/pull/4356)

* **Kubernetes**
  * Introduced etcd backups with a new `KubernetesEtcdBackup` strand that performs hourly snapshots and uploads them to MinIO, including automatic cleanup of old backups [#4548](https://github.com/ubicloud/ubicloud/pull/4548)

* **UbiBLK**
  * Made UbiBLK the default storage backend for new hosts after successful production testing [#4534](https://github.com/ubicloud/ubicloud/pull/4534)

**Bug fixes / maintenance / internals 🔧**

* **PostgreSQL**
  * Added paging alerts on PostgreSQL promotion failures, with automatic retries and page resolution on success [#4399](https://github.com/ubicloud/ubicloud/pull/4399)
  * Reduced failover-related deadlines and moved deadline registration before hops to ensure deadlines are registered even if the label raises an exception [#4601](https://github.com/ubicloud/ubicloud/pull/4601)
  * Hardened `PostgresServer#run_query` to reject non-frozen strings, replacing an insecure interpolation pattern with `Sequel::Dataset` placeholder support [#4544](https://github.com/ubicloud/ubicloud/pull/4544)

* **Networking**
  * Fixed `NoMethodError` in AWS NicNexus when no addresses are available for EIP attachment [#4473](https://github.com/ubicloud/ubicloud/pull/4473)
  * Fixed ACME DNS challenge records to use `authorization.domain`, creating exactly one record per authorization instead of a cross-product across all domains [#4562](https://github.com/ubicloud/ubicloud/pull/4562)

* **Framework**
  * Switched web routes from PATCH/DELETE to POST methods, eliminating JavaScript dependencies for form submissions [#4354](https://github.com/ubicloud/ubicloud/pull/4354), [#4358](https://github.com/ubicloud/ubicloud/pull/4358)
  * Removed unused Sequel association methods to reduce memory usage and improve garbage collection, with CI enforcement [#4366](https://github.com/ubicloud/ubicloud/pull/4366)
  * Added `before_destroy` callback to `Prog::Base` for cleanup logic that only needs to run once before destruction [#4485](https://github.com/ubicloud/ubicloud/pull/4485)
  * Improved strand destruction handling: auto-pop when destroy semaphore is set but no destroy label exists [#4489](https://github.com/ubicloud/ubicloud/pull/4489), pop extra stack frames before switching to destroy label [#4490](https://github.com/ubicloud/ubicloud/pull/4490)
  * Split AI playground CSP header to scope it only to that route [#4494](https://github.com/ubicloud/ubicloud/pull/4494)
  * Fixed broken `LocationCredential` project association that caused `NoMethodError` in production [#4500](https://github.com/ubicloud/ubicloud/pull/4500)
  * Added database constraint ensuring `used_hugepages_1g >= 0` to catch over-deallocation bugs at write time [#4529](https://github.com/ubicloud/ubicloud/pull/4529)
  * Added `Sshable#json` helper method for parsing SSH command output [#4554](https://github.com/ubicloud/ubicloud/pull/4554)
  * Fixed incorrect `one_to_one` associations that should be `many_to_one` [#4559](https://github.com/ubicloud/ubicloud/pull/4559)
  * Capped ext4 root reservation to 50GiB to avoid unnecessarily restricting customer disk usage [#4564](https://github.com/ubicloud/ubicloud/pull/4564)
  * Fixed `VmHostSliceNexus` wait state to rescue all SSH connection errors including `Net::SSH::ConnectionTimeout` [#4578](https://github.com/ubicloud/ubicloud/pull/4578)
  * Optimized billing record updates to skip finalization when records are unchanged [#4589](https://github.com/ubicloud/ubicloud/pull/4589)

* **Fleet**
  * Added VM host health check to verify clock source is `tsc` (or `arch_sys_counter` on arm64), alerting when hosts fall back to `hpet` which can cause monotonic time errors [#4419](https://github.com/ubicloud/ubicloud/pull/4419)

* **Admin**
  * Added admin page to search for archived records by ID, model name, and date range [#4550](https://github.com/ubicloud/ubicloud/pull/4550)
  * Reduced archived record search day limits to prevent Heroku router timeouts [#4556](https://github.com/ubicloud/ubicloud/pull/4556)
  * Fixed `UBID.parse` error handling in archived record search [#4568](https://github.com/ubicloud/ubicloud/pull/4568)
  * Added structured `workflow_job` display for runners, presenting JSON data in a readable table [#4572](https://github.com/ubicloud/ubicloud/pull/4572)

* **GitHub Actions**
  * Fixed blob storage bucket lifecycle to only create buckets when adding cache entries, preventing unnecessary deletions for users who only request entries without adding new ones [#3762](https://github.com/ubicloud/ubicloud/pull/3762)

* **Tests**
  * Democked test specs to use real persisted model instances instead of `instance_double` mocks: `vm_spec.rb` [#4377](https://github.com/ubicloud/ubicloud/pull/4377), `converge_postgres_resource_spec.rb` [#4389](https://github.com/ubicloud/ubicloud/pull/4389), `update_firewall_rules_spec` [#4504](https://github.com/ubicloud/ubicloud/pull/4504), `CertNexus` spec [#4546](https://github.com/ubicloud/ubicloud/pull/4546), `postgres_resource_spec` [#4547](https://github.com/ubicloud/ubicloud/pull/4547), `postgres_resource_nexus_spec` [#4563](https://github.com/ubicloud/ubicloud/pull/4563), `VmHost` model specs [#4585](https://github.com/ubicloud/ubicloud/pull/4585)
  * Added database dump step to E2E tests for debugging, uploading a subset of safe tables as artifacts [#4543](https://github.com/ubicloud/ubicloud/pull/4543)
  * Fixed E2E summary markdown table layout by stripping newlines from exception messages [#4577](https://github.com/ubicloud/ubicloud/pull/4577)

* **Dev**
  * Clarified Hetzner user credentials and SSH key usage in documentation [#3764](https://github.com/ubicloud/ubicloud/pull/3764)
  * Standardized `e.g.` usage in CLI help text [#4533](https://github.com/ubicloud/ubicloud/pull/4533)
  * Fixed trailing whitespace in `inference_router_replica_nexus.rb` [#4552](https://github.com/ubicloud/ubicloud/pull/4552)
  * Fixed typo in `cloudify_server` demo [#4565](https://github.com/ubicloud/ubicloud/pull/4565)
  * Simplified `location_id` passing using Ruby 3.1+ keyword shorthand [#4576](https://github.com/ubicloud/ubicloud/pull/4576)
  * Fixed missing argument in migration convert script [#4581](https://github.com/ubicloud/ubicloud/pull/4581)

* **Version bumps**
  * Bumped development dependencies: brakeman 7.1.1→7.1.2, pdf-reader 2.15.0→2.15.1, rubocop-ast 1.48.0→1.49.0 [#4535](https://github.com/ubicloud/ubicloud/pull/4535)
  * Bumped JS dependencies [#4537](https://github.com/ubicloud/ubicloud/pull/4537)
  * Bumped rubocop from 1.81.7 to 1.82.1 [#4551](https://github.com/ubicloud/ubicloud/pull/4551)