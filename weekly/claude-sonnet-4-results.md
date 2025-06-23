### **Customer facing features: Now available!** 🚀

- PostgreSQL UI split into multiple pages for better navigation and user experience with dedicated sections for overview, connections, backups, networking, and settings #3446
- Virtual machine creation now offers separate GPU and non-GPU options for easier instance selection when feature flag is enabled #3467
- Kubernetes cluster Service URLs are now copyable for easier access #3480
- CA certificate download functionality fixed for PostgreSQL connections #3500

**Customer facing features: Not yet released** ⌛

- Enhanced cache storage with 100GB free cache storage for premium GitHub runners #3473
- Ubiblk storage backend integration for improved volume allocation performance #3449

**Bug fixes / maintenance** 🔧

- Fixed S3 service unavailable errors during multipart uploads by properly handling them as 503 errors instead of 400 errors #3375
- Resolved session handling issues by checking active sessions before root route processing to prevent errors with closed accounts #3470
- Fixed GitHub runner recycling to properly handle deleted runners during recycle condition checks #3469
- Enhanced GitHub Actions xargs command to use NUL delimiter for robust handling of encoded configurations #3465
- Improved cache entry cleanup during repository destruction to ensure proper blob storage deletion #3463
- PostgreSQL connection strings updated to use proper SSL mode configuration instead of channel binding #3446
- Corrected IPv4 address table population to exclude host sshable IP addresses #3483, #3484
- Made SPDK setup process fully idempotent across Ubuntu 22.04 and 24.04 versions #3490

**Internal improvements** 🌟

- Optimized route handling across multiple endpoints for better performance and code organization #3389
- Added comprehensive monitoring for VmHost node_exporter metrics with VictoriaMetrics integration #3407, #3416
- Improved dispatcher logic with additional performance metrics including total delay and old strand percentage tracking #3459
- Simplified PostgreSQL option handling and validation system by centralizing business logic #3462
- Enhanced strand lease management by clearing cached instance state for better object shape handling #3479
- Increased CI timeout from 15 to 25 minutes to accommodate longer ARM build processes #3460
- Removed sampling strands for metrics as new respirate provides more accurate measurements #3468
- Added deadline management for GitHub runner recycling and wait states to detect stuck processes #3469
- Improved repository destruction workflow by moving cache cleanup logic from model to program #3463
- Updated strand donation logic to use fresh dataset queries instead of cached children for accuracy #3477
- Added new rake task for debugging cache files by converting marshalled data to text format #3476