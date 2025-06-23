https://claude.ai/public/artifacts/63356ea9-6feb-4591-bb40-724e53e847fb

### **Customer facing features: Now available!** 🚀

- PostgreSQL UI redesigned with dedicated pages for better navigation and feature discovery #3446
- Virtual Machine creation page split into separate GPU/non-GPU flows for easier instance selection #3467 #3478
- Service URLs for Kubernetes clusters now have one-click copy functionality #3480
- CA certificate download button fixed for PostgreSQL connections #3500

**Customer facing features: Not yet released** ⌛

- Grafana installation and monitoring setup prepared for infrastructure monitoring #3407 #3416
- Enhanced cache storage limits (100GB) for GitHub installations with premium runners #3473

**Bug fixes / maintenance** 🔧

- Fixed AWS S3 service unavailability errors during multipart uploads now properly return 503 status #3375
- Resolved session validation issues for closed accounts to prevent errors on login #3470
- Fixed timeout issues for ARM CI jobs by increasing timeout from 15 to 25 minutes #3460
- Fixed GitHub runner recycling when runners are deleted or encounter API errors #3469
- Improved GitHub Actions xargs handling for special characters in configurations #3465
- Fixed SPDK setup idempotency issues on Ubuntu 24.04 #3490

**Internal improvements** 🌟

- Route handling restructured across multiple endpoints for better code organization #3389
- PostgreSQL options configuration centralized and simplified #3462
- GitHub repository destruction now explicitly handles cache cleanup #3463
- Dispatcher performance metrics enhanced with total delay and partition tracking #3459
- VmHost IPv4 address allocation optimized with new database table #3438 #3483 #3484
- Node exporter metrics collection added for VmHost monitoring #3407
- Ubiblk volume backend support added alongside existing SPDK #3449
- Strand caching improvements for better performance #3477 #3479
- Sampling strands removed in favor of more accurate respirate metrics #3468
- IPv4 address table population fixed to exclude host's sshable IP #3483
- Cache file debugging improved with new dump_sequel_caches rake task #3476
- VmHost ipv4_address table usage temporarily reverted then restored with fixes #3481 #3484