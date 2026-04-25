# Cross-Site Scripting (XSS) Cheat Sheet for Testers
## Purpose
This cheat sheet helps perform basic XSS checks during testing.  
It focuses on simple, practical tests that can be applied without deep security knowledge.

## What is XSS?
Cross-Site Scripting (XSS) occurs when an application includes untrusted input in a web page without proper validation or encoding, allowing scripts to run in the browser.

Example:
```html
<div>Welcome, input</div>
````
If input is not sanitized, a script can be injected and executed.

## When to Test
Look for input fields such as:
* Forms (login, comments, search)
* URL parameters
* Input fields that are displayed back to the user
* API responses rendered in the UI
* Error messages

## Types of XSS (Quick Overview)
* Reflected: input is immediately returned in the response
* Stored: input is saved and shown to other users
* DOM-based: handled in the browser via JavaScript

## Basic Test Approach
1. Enter test payload
2. Observe behavior in browser
3. Look for:
    * Script execution
    * Broken HTML
    * Unexpected pop-ups or alerts

## Common Test Payloads
### 1. Basic Script Injection
```
<script>alert(1)</script>
```
Expected:
* Input is escaped or blocked

Risk:

* Alert is executed > XSS vulnerability

### 2. HTML Injection Check
```
<b>test</b>
```
Expected:
* Rendered as text

Risk:
* Rendered as HTML > possible XSS entry point

### 3. Attribute Injection
```
" onmouseover="alert(1)
```
Expected:
* Input safely encoded

Risk:
* JavaScript executes on hover

### 4. Image-based Payload
```
<img src=x onerror=alert(1)>
```
Expected:
* Blocked or sanitized

Risk:
* Script executes via error handler

### 5. Simple Event Injection
```
<svg onload=alert(1)>
```
Expected:
* Blocked or escaped

## Safe vs Risky Payloads
### Safe examples (recommended for testing):
```
<script>alert(1)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
```
### Avoid (harmful or disruptive):
```html
<script>while(true){}</script>
```
This creates an infinite loop in the browser.

**Result:** the page freezes or crashes, making the application unusable (Denial of Service).

```html
<script>document.location='malicious-site'</script>
```

This redirects the user to another website.

**Result:** users can be sent to phishing or malicious sites without their consent.

## What to Look For
* JavaScript execution (alerts, pop-ups)
* HTML rendered instead of escaped
* Input reflected directly in the page
* Different behavior between inputs

## High-Risk Areas
Be extra careful when testing:
* User-generated content (comments, profiles)
* Admin panels
* Input shown to other users
* Rich text editors

## API Example
Response:
```json
{
  "name": "<script>alert(1)</script>"
}
```
If this is rendered in the GUI without encoding > potential XSS

## Safe Testing Tips
* Use test environments only
* Avoid disruptive scripts
* Keep payloads simple
* Do not impact other users
* Document findings clearly

## Example Test Scenario
Comment field:
```
<script>alert(1)</script>
```
If alert appears when viewing the comment > potential stored XSS

## Reporting
When reporting, include:
* Payload used
* Location (field, URL, API)
* Where it executed (page, element)
* Observed behavior

Example:
"Entering `<script>alert(1)</script>` in the comment field resulted in script execution when viewing the page."

## Summary
Start simple:
* Test input reflection
* Check rendering behavior
* Look for script execution

Even basic XSS tests can reveal serious vulnerabilities early in the development process.