### 2025-07-22

### **Customer facing features: Now available\! 🚀**

* The login process has been updated to a multi-phase flow, first asking for an email and then showing the available authentication methods for that account, such as password or OIDC. [\#3586](https://github.com/ubicloud/ubicloud/pull/3586)  
* The PostgreSQL API and CLI now return the target VM and storage sizes in addition to the current sizes, making it easier to see pending changes. [\#3590](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3590)  
* You can now lock specific email domains to an OIDC provider, enforcing that all users from that domain authenticate via the designated provider. [\#3594](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3594)  
* The PostgreSQL metrics dashboard now displays `softirq` CPU usage, providing more detailed performance insights. [\#3595](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3595)  
* Billing rates have been added for the `Qwen2.5-VL-72B` AI model. [\#3601](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3601)  
* It is now possible to remove the last SPDK installation from a host, as long as another storage backend like Ubiblk is in use. [\#3643](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3643)

### **Customer facing features: Not yet released ⌛**

* Idempotency has been improved for AWS VPC and NIC operations, making them more reliable. [\#3591](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3591)  
* The `metrics-server` is now automatically installed on new Kubernetes clusters, a prerequisite for features like `kubectl top`. [\#3599](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3599)  
* Support has been added for CloudHypervisor 46.0 on Ubuntu 24 hosts, laying the groundwork for future VM runtime upgrades. [\#3602](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3602)  
* AWS subnets will now be created in a random availability zone (`a`, `b`, or `c`) to improve fault tolerance. [\#3605](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3605)  
* A small, configurable percentage of GitHub Action VMs will now run on CloudHypervisor 46.0 for gradual testing and rollout. [\#3606](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3606)  
* Listing of PostgreSQL backups from AWS S3 now supports pagination, ensuring all backups are retrieved even if there are a large number of them. [\#3607](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3607)  
* Support has been added for the `us-east-1` and `us-east-2` AWS regions. [\#3609](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3609)  
* A new process has been added to establish full mesh SSH connectivity between Kubernetes worker nodes. [\#3610](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3610)  
* CloudHypervisor 46.0 is now the default version for new VMs on Ubuntu 24.04 hosts. [\#3613](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3613)  
* The logic for `VmHostSlice` has been clarified to better handle its lifecycle and prevent unprepared slices from being orphaned. [\#3625](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3625)  
* The worker mesh synchronization process for Kubernetes clusters is now triggered automatically when a cluster is provisioned. [\#3634](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3634)

### **Bug fixes / maintenance 🔧**

* The `cloudify_server` demo script has been updated to be Hetzner-only to ensure reliability, and now requires Hetzner credentials in the `.env` file. [\#3534](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3534)  
* Validation for PostgreSQL configuration values with units (like `ms` or `GB`) has been relaxed to also allow raw integer values. [\#3553](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3553)  
* The OIDC authentication nonce is now generated with a time-based component to guarantee it does not repeat. [\#3587](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3587)  
* A capitalization issue with "GitHub" during the social login flow has been corrected. [\#3593](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3593)  
* Support for Ubiblk v0.1-7 has been added, fixing a startup race condition that could cause boot failures. [\#3597](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3597)  
* The system has been updated to use Alma Linux 9.6, as version 9.5 is no longer available for download. [\#3598](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3598)  
* Fixed an issue where destroying a VM before its storage was fully installed would cause the purge process to fail. [\#3604](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3604)  
* The `mistral-small-3` model has been delisted from OpenRouter as it is being deprecated. [\#3611](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3611)  
* The format for generated SSH private keys has been fixed to ensure compatibility with `openssh` and `libcrypto`. [\#3615](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3615)  
* SHA256 hashes for Alma Linux 9.6 have been added to prepare for the version switch. [\#3616](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3616)  
* The non-standard `shortcut icon` link has been removed from the layout to prevent duplicate favicon requests. [\#3624](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3624)  
* The Ruby version used by the project has been bumped to 3.4.5. [\#3627](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3627)  
* A fix has been implemented to correctly parse the persistent device ID for NVMe disks, which starts with `nvme-eui.` not `nvme-eui-`. [\#3628](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3628)  
* The `locked_domain.domain` database column is now case-insensitive to correctly handle all domain name variations. [\#3629](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3629)  
* Metrics are no longer exported for a resource after it has been marked as deleted. [\#3631](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3631)  
* A bug in the locked domains feature was fixed where the OIDC provider name was not being compared correctly. [\#3638](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3638)

### **Internal improvements 🌟**

* The `SemaphoreMethods` module has been converted to a more robust Sequel plugin for better code structure. [\#3441](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3441)  
* The JIT configuration for GitHub runners is now passed via a file instead of command-line arguments, preventing potential errors with large tokens. This is currently behind a feature flag. [\#3570](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3570)  
* A logical error in the E2E test script was fixed, which previously caused GitHub runner tests to execute unintentionally. [\#3578](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3578)  
* The output from the `setup_environment` script is now suppressed to reduce log noise and save bandwidth. [\#3589](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3589)  
* A new `encrypted_columns` argument was added to the `ResourceMethods` plugin to simplify setting up encrypted model attributes. [\#3592](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3592)  
* Logging for `respirate` sleep duration has been fixed to log the requested sleep time, allowing for more accurate fractional-second values. [\#3596](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3596)  
* VM host utilization logging has been enhanced to show how many runners of each size can fit into the available capacity, providing more actionable scaling data. [\#3600](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3600)  
* The daemon is now cleaned up properly after setting up the VhostBlockBackend, which improves the development workflow for re-installations. [\#3603](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3603)  
* E2E test monitoring has been improved by enabling synchronous output and using line-buffered `grep` to ensure logs appear in real-time. [\#3614](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3614)  
* Extra debugging logging has been removed from the PostgreSQL archive command. [\#3621](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3621)  
* A new test has been added to ensure that all encrypted database columns are properly included in the `redacted_columns` list for security. [\#3623](https://www.google.com/search?q=https://github.com/ubicloud/ubicloud/pull/3623)