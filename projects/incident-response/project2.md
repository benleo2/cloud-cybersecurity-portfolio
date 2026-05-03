## Detection

Suspicious login is detected from an unknown ip at an unsusual time.

Cloud trail logs showed:
- Multiple API calls
- login from new location

## Containment

- Disabled compromised IAM credentials
- Rotated access keys
- Revoked active sessions

The goal is to stop the attacker access immediately.

## investigaion

Analysing CloudTrail logs for identifying:
- Attacker ip address
- Action performed by the attacker
- Accessed resources (EC2,S3)

Findings:
- S3 access attempt
- Resource enumeration activity

## Eradication
- Removed unauthorized access
- Verified IAM policies
- Ensured no malicous changes are created

## Restore
- Resored normal operations
- Ensured no suspicous activity is happening
- Enabled monitoring

## Lessons learned

- MFA should be enforced
- least privelage IAM policies minimize attacks
- Continous monitoring should be required
- credential leak is the major reason for attacks
