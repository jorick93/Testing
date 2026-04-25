# SQL Injection Cheat Sheet for Testers

## Purpose
This cheat sheet helps perform basic SQL Injection (SQLi) checks during testing. It focuses on simple, practical tests that can be applied without deep security knowledge.

## What is SQL Injection?
SQL Injection occurs when user input is incorrectly handled and executed as part of a database query.

Example:
```sql
SELECT * FROM users WHERE username = 'input';
````

If input is not sanitized, an attacker can manipulate the query.

## When to Test
Look for input fields such as:

* Login forms
* Search fields
* URL parameters
* Filters or query inputs
* API request parameters

## Basic Test Approach
1. Enter unexpected input
2. Observe system behavior
3. Look for:
   * Errors
   * Unexpected data
   * Bypassed logic (e.g. login)

## Common Test Payloads
### 1. Basic Quote Test
Check if input breaks the query:
```
'
"
```
Expected:
* Proper validation or error handling

Risk:
* SQL error message shown

### 2. Authentication Bypass
Try bypassing login:
```
' OR '1'='1
' OR 1=1 --
```
Expected:
* Login should fail

Risk:
* Login succeeds without valid credentials

### 3. Comment Injection
Terminate the query:
```
' --
' #
```
Expected:
* Input should be rejected or sanitized

### 4. Boolean-Based Testing
Check true/false behavior:
```
' AND 1=1 --
' AND 1=2 --
```
Expected:
* Different responses for true vs false

Risk:
* System reacts differently > possible injection

### 5. UNION Injection (basic check)
Try combining queries:
```
' UNION SELECT NULL --
```
Expected:
* Rejected or handled safely

## What to Look For
* SQL error messages (e.g. "syntax error", "SQL")
* Different responses for similar inputs
* Unexpected data returned
* Login bypass or access to restricted data

## Safe Testing Tips
* Use test environments only
* Do not extract real data
* Keep payloads simple
* Document findings clearly

## Safety Warning
Avoid using destructive SQL commands such as:
```sql
DROP TABLE users;
DELETE FROM users;
```
These commands can permanently remove data and disrupt the system.
Always perform SQL Injection testing in a controlled test environment and stick to non-destructive payloads.

## Example Test Scenario
### Web example
Login form:
* Username: `' OR '1'='1`
* Password: anything
If login succeeds > potential SQL Injection vulnerability

### API Example

POST /login
```json
{
  "username": "' OR '1'='1",
  "password": "test"
}
```

## Reporting
When reporting, include:
* Input used
* Location (URL, field, API)
* Observed behavior
* Expected behavior

Example:
"Entering `' OR '1'='1` in the username field allowed login without valid credentials."

## Summary
Start simple:
* Try basic inputs
* Look for unusual behavior
* Focus on high-risk fields

SQL Injection testing can begin with just a few simple checks and can already reveal serious issues.