# API Security Testing Cheat Sheet for Testers
## Purpose
This cheat sheet helps testers perform basic security checks on APIs.  
It focuses on simple, practical tests that can be applied using tools like Postman.

## Why API Security Matters
Modern applications rely heavily on APIs.  
APIs often:
- Expose sensitive data
- Have less visible protection than UI
- Are easier to test and manipulate

Many security issues (OWASP API Top 10) occur at API level:
- Broken authentication
- Broken authorization
- Excessive data exposure

## When to Test
Focus on:
- Login and authentication endpoints
- User data endpoints
- CRUD operations (create, read, update, delete)
- Endpoints with IDs or parameters

## Basic Test Approach
1. Send a valid request
2. Modify the request
3. Observe the response

Change:
- IDs
- Tokens
- Parameters
- Request body

Look for:
- Unauthorized access
- Unexpected data
- Missing validation

## Common Test Scenarios
### 1. Missing Authentication
Request without token:
```script
GET /api/users
````

Expected:
* 401 Unauthorized

Risk:
* Data returned > authentication missing

### 2. Broken Authorization (Access Other Users)
When performing next request:
```script
GET /api/users/123
```

For example try another user:
```script
GET /api/users/124
```

Expected:
* Access denied

Risk:
* Data returned > broken authorization (IDOR)

### 3. Parameter Tampering
Modify request data:
```json
{
  "userId": 123,
  "role": "admin"
}
```

Expected:
* Server ignores or rejects changes

Risk:
* Role is accepted > privilege escalation

### 4. Excessive Data Exposure
Check response:
```json
{
  "id": 123,
  "name": "John",
  "email": "john@test.com",
  "password": "hashed"
}
```

Expected:
* Only necessary fields returned

Risk:
* Sensitive data exposed

### 5. Method Manipulation
Try different HTTP methods:
```script
GET /api/users/123
POST /api/users/123
DELETE /api/users/123
```

Expected:
* Only allowed methods work

Risk:
* Unauthorized actions allowed

### 6. Missing Input Validation
Send invalid input:
```json
{
  "email": "invalid-email"
}
```

Expected:
* Validation error

Risk:
* Accepted input > weak validation

## What to Look For
* Missing authentication checks
* Access to other users data
* Unexpected fields in responses
* Changes accepted without validation
* Inconsistent behavior between endpoints

## High-Risk Areas
* Authentication endpoints (/login, /auth)
* User data (/users, /profile)
* Admin endpoints
* File uploads
* Financial or sensitive data APIs

## Tools (Basic)
* Postman
* Browser DevTools (Network tab)
* Python Requests
* Robotframework requests library

## Safe Testing Tips
* Use test accounts
* Avoid modifying real user data
* Do not perform destructive actions
* Keep tests simple and controlled

## Example Test Scenario
1. Login and get token
2. Call:
```script
GET /api/users/123
```

3. Change to:
```script
GET /api/users/124
```

If data is returned > potential authorization issue

## Reporting
Include:
* Endpoint
* Method (GET, POST, etc.)
* Payload used
* Observed response
* Expected behavior

Example:
"Accessing /api/users/124 with a valid token for user 123 returned another user's data."

## Summary
Start simple:
* Modify requests
* Change IDs and parameters
* Check responses carefully

Even basic API tests can reveal critical security issues early.