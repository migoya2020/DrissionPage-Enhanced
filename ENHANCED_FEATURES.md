# Enhanced DrissionPage Features - Examples

## 1. Proxy with Authentication

### Basic Usage

```python
from DrissionPage import ChromiumPage, ChromiumOptions

# Method 1: Set proxy with auth in options (recommended)
co = ChromiumOptions()
co.set_proxy('username:password@proxy.example.com:8080')
page = ChromiumPage(co)

# Enable proxy authentication handler
page.set.proxy_auth('username:password@proxy.example.com:8080')

page.get('https://httpbin.org/ip')
print(page.html)
```

### With HTTP/HTTPS prefix

```python
co = ChromiumOptions()
co.set_proxy('http://username:password@proxy.example.com:8080')
page = ChromiumPage(co)
page.set.proxy_auth('http://username:password@proxy.example.com:8080')
```

### Different proxy formats supported

```python
# Format 1: username:password@host:port
'myuser:mypass@proxy.com:8080'

# Format 2: http://username:password@host:port
'http://myuser:mypass@proxy.com:8080'

# Format 3: https://username:password@host:port
'https://myuser:mypass@proxy.com:8080'
```

## 2. Advanced Resource Blocking

### Block Images Only

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()

# Block images using advanced CDP interception
page.set.block_resources(images=True)

page.get('https://example.com')
# Images will be blocked, page loads faster
```

### Block Multiple Resource Types

```python
page = ChromiumPage()

# Block images, CSS, and fonts
page.set.block_resources(images=True, css=True, fonts=True)

page.get('https://example.com')
```

### Block with Custom Patterns

```python
page = ChromiumPage()

# Block specific domains or patterns
page.set.block_resources(
    images=True,
    patterns=['google-analytics.com', 'facebook.com', 'doubleclick.net']
)

page.get('https://example.com')
```

### Disable Resource Blocking

```python
# Re-enable all resources
page.set.unblock_resources()
```

## 3. Combined Usage - Proxy + Resource Blocking

```python
from DrissionPage import ChromiumPage, ChromiumOptions

# Setup with proxy authentication
co = ChromiumOptions()
co.set_proxy('username:password@proxy.example.com:8080')

page = ChromiumPage(co)

# Enable proxy auth
page.set.proxy_auth('username:password@proxy.example.com:8080')

# Block unnecessary resources for faster loading
page.set.block_resources(images=True, css=True, fonts=True)

# Navigate
page.get('https://example.com')
```

## 4. Comparison with Old Method

### Old Method (Limited)

```python
# Old way - only blocks via blink settings (easily detected)
co = ChromiumOptions()
co.no_imgs(True)  # Uses --blink-settings=imagesEnabled=false
page = ChromiumPage(co)
```

### New Method (Better)

```python
# New way - uses CDP Fetch domain (harder to detect)
page = ChromiumPage()
page.set.block_resources(images=True)
# More stealthy, better control
```

## 5. Advanced Scenarios

### Rotating Proxies with Auth

```python
from DrissionPage import ChromiumPage, ChromiumOptions

proxies = [
    'user1:pass1@proxy1.com:8080',
    'user2:pass2@proxy2.com:8080',
    'user3:pass3@proxy3.com:8080'
]

for proxy in proxies:
    co = ChromiumOptions()
    co.set_proxy(proxy)
    
    page = ChromiumPage(co)
    page.set.proxy_auth(proxy)
    page.set.block_resources(images=True, css=True)
    
    page.get('https://httpbin.org/ip')
    print(f"Using proxy: {proxy}")
    print(page.json)
    
    page.quit()
```

### Block Tracking Scripts

```python
page = ChromiumPage()

# Block common tracking and analytics
tracking_patterns = [
    'google-analytics.com',
    'googletagmanager.com',
    'facebook.com/tr',
    'doubleclick.net',
    'hotjar.com',
    'mixpanel.com',
    'segment.com'
]

page.set.block_resources(patterns=tracking_patterns)
page.get('https://example.com')
```

## 6. Performance Comparison

```python
import time
from DrissionPage import ChromiumPage

# Without blocking
page1 = ChromiumPage()
start = time.time()
page1.get('https://heavy-website.com')
time1 = time.time() - start
print(f"Without blocking: {time1:.2f}s")
page1.quit()

# With blocking
page2 = ChromiumPage()
page2.set.block_resources(images=True, css=True, fonts=True, media=True)
start = time.time()
page2.get('https://heavy-website.com')
time2 = time.time() - start
print(f"With blocking: {time2:.2f}s")
print(f"Speed improvement: {((time1-time2)/time1*100):.1f}%")
page2.quit()
```

## Key Improvements

### Proxy Authentication
- ✅ Now supports `username:password@host:port` format
- ✅ Uses CDP Fetch domain for authentication
- ✅ Handles auth challenges automatically
- ✅ Works with HTTP/HTTPS proxies

### Resource Blocking
- ✅ Uses CDP Fetch domain instead of blink settings
- ✅ Harder for websites to detect
- ✅ More granular control (images, CSS, fonts, media)
- ✅ Support for custom URL patterns
- ✅ Can be enabled/disabled dynamically
- ✅ Better performance and stealth

### Detection Evasion
- Old `--blink-settings=imagesEnabled=false` is easily detected
- New CDP Fetch interception appears as normal network behavior
- Requests fail with `BlockedByClient` error (looks like network issue)
- No browser flags or settings modified
