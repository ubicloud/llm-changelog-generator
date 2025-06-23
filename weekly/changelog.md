### **Customer facing features: Now available\!** 🚀

- Ubuntu 2004 runner images are removed \#3414  
- Inference Model Cards UI is improved \#3417

**Customer facing features: Not yet released** ⌛

- Postgres free tier  
- Inference Router / Deepseek R1/2  
- Kubernetes Persistent Storage  
- UbiBlk

**Bug fixes / maintenance** 🔧

- Metrics reconfiguration on destination update is fixed \#3410  
- Don't try to update dns when cert order doesn't exist at \#3412  
- Internal stripe\_data helper is fixed \#3415

**Internal improvements** 🌟

- Models are refactored \#3360  
- gen\_timestamp\_ubid\_uuid function \#3388  
- Content visibility toggle code is replaced with CSS (less JS\!) \#3409  
- DB lock is removed from GH runner quota\_available? for less contention \#3422  
- Limit for customer concurrency limit is bumped from 70% to 75% \#3421  
- Timeout of 10s for retrieving DockerHub quota limits \#3425  
- Image sizes are logged in E2E logs \#3368