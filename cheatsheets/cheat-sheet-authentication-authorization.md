# Authentication and Authorization Cheat Sheet for Testers
## Purpose
This cheat sheet helps testers validate authentication and authorization controls in applications.  
It focuses on simple, practical checks that can be applied during regular testing.

## What is Authentication vs Authorization?
- Authentication = verifying who the user is (login)
- Authorization = verifying what the user is allowed to do (permissions)

Example:
- Login with username/password > authentication
- Access admin page > authorization

## When to Test
Focus on:
- Login and logout functionality
- Role-based access (user, admin, etc.)
- Sensitive actions (edit, delete, view data)
- API endpoints with user data

## Basic Test Approach
1. Log in as a normal user
2. Try to access restricted functionality
3. Modify requests or URLs
4. Observe system behavior

Look for:
- Access granted when it should not be
- Missing validation
- Different behavior between roles

## Common Test Scenarios
### 1. Role-Based Access Check
Try accessing admin functionality as a normal user:
```
/admin
/admin/users
```

Expected:
- Access denied

Risk:
- Access granted > authorization issue

### 2. Direct URL Access (Force Browsing)
Navigate directly to restricted pages without proper role:
```
/settings
/manage-users
```

Expected:
- Redirect or error

Risk:
- Page loads > missing access control

### 3. ID Manipulation (Basic IDOR)
Change identifiers:
```
/user/123 > /user/124
````

Expected:
- Access denied

Risk:
- Access to another user's data

### 4. API Authorization Check
Example request:
```json
GET /api/users/123
Authorization: Bearer <token>
````
Try:
* Accessing another user's data
* Removing or modifying token

Expected:
* Request blocked

Risk:
* Data returned > broken authorization

### 5. Missing Backend Validation
UI blocks action, but API allows it.

Steps:
1. Try action in UI (blocked)
2. Repeat via API (Postman)

Expected:
* API also blocks action

Risk:
* API allows action > security issue

## What to Look For
* Access without proper role
* Missing permission checks
* Data exposure between users
* UI restrictions without backend validation
* Different behavior between UI and API

## High-Risk Areas
* Admin panels
* User management
* Data belonging to other users
* API endpoints
* Actions like delete, update, export

## Safe Testing Tips
* Use test accounts with different roles
* Do not access real user data
* Test in controlled environments
* Document findings clearly

## Example Test Scenario
User role:
* Logged in as regular user

Test:
* Navigate to `/admin`

If access is granted > potential authorization vulnerability

## Reporting
When reporting, include:
* Role used (user/admin)
* Action performed
* Endpoint or page
* Observed behavior
* Expected behavior

Example:
"A regular user was able to access the /admin endpoint and view restricted data."

## Summary
Focus on:
* Who can access what
* What happens when roles change
* Whether backend enforces rules

Even simple checks can reveal critical authorization issues.