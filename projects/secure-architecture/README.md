## 🔐 Secure AWS Architecture Project

Designed a secure cloud architecture using AWS concepts including VPC, public and private subnets, EC2, and S3.

### Key Security Features:

* Public-facing web server with restricted access (HTTP/HTTPS only)
* Private application server with no public IP
* Secure S3 bucket with encryption and no public access
* IAM roles with least privilege
* NAT Gateway for controlled outbound internet access
* Logging enabled (CloudTrail, VPC Flow Logs)

### Security Approach:

Implemented defense-in-depth by combining network isolation, identity control, and data encryption to reduce attack surface and limit impact of breaches.
