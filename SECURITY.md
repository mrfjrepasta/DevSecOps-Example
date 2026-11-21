# Security Policy 
Created 11-21-2026

## Supported Versions
This repo is unsupported and is 'as-is'. There is no license for reproduction or use. This may or may not change, with or without notice, at the sole discretion of the repository owner.

## Reporting a Vulnerability

If a security issue (Bug, CVE, or CWE, or NIST Framework Violation for GRC purposes) is found, please reach out on LinkedIn. 
Please include the specific dependencies, their versions, and lines of code that created the security-related issue, if available.

If not available for some reason, please describe the issue as best as possible and include any logs, screenshots of observations, and the STDOUT (response of the request that incurred the finding) as evidence.

**Additionally, REDACT ALL SENSITIVE INFORMATION.**

You are only authorized to test main.py, test_main.py, and .gitignore for security-related issues, bugs, and findings.

Expect a response within 30 days. If accepted, rejected, or 'pending - need more info', you will receive notification. You are not permitted to disclose publicly until a confirmed resolve of the issue is observed. You must receive explicit permission first - this will usually be contained in the notification.

### What is sensitive information for the purpose of reporting?
- Keys & Session Tokens (only use the last 4 chars of the total charset)
- Data (If PII, HPI, HIPPA, and so forth.)
- Data from files found in .gitignore (.gitignore is for ignoring specific files and folders upon commits/pushes which might exist within the repository.)
- The API endpoints containing the security issue, bug, vuln, or framework violation(s).
### What is NOT sensitive information for the purpose of reporting?
- The URL + URI within the HTTP request header. (NOT Including the API endpoints.)
- Timestamp(s).
- HTTP Status Code as the result of the client request.

This Security.md file is not all inclusive. Receive approval, always
