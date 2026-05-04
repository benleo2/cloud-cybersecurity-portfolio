## Identified risks

- IAM user has full admin access
- No MFA enforced
- Long term credential
- Over permissive policies ("*:*")
- No monitoring and restrictions

## Least privileage implentation

- Removed full admin access
- Created role based access with limited permissions
- Given required actions per role

## MFA enforcement

- Enabled MFA for all IAM users
- Ensured admin accounts require MFA

## IAM roles

- Replaced long term credentials with IAM roles
- Created temporary credentials for services

## Permission boudaries

- Applied boundaries to restrict maximum permissions
- Prevented privilege escalation

## Monitoring

- Enabled CloudTrail logging
- Monitoring IAM activity for suspicious actions

## Secuirty improvements

- Reduced attack surface by limiting permissions
- Prevented credential abuse by using MFA
- Improved visibility using logging
- Implemented zero trust priciples 
