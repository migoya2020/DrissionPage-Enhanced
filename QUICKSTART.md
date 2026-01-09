# Quick Start - Enhanced DrissionPage

## 🚀 Get Started in 2 Minutes

### 1. Proxy with Authentication

```python
from DrissionPage import ChromiumPage, ChromiumOptions

# Your authenticated proxy
proxy = 'username:password@proxy.example.com:8080'

# Setup
co = ChromiumOptions()
co.set_proxy(proxy)

# Create page and enable auth
page = ChromiumPage(co)
page.set.proxy_auth(proxy)

# Use it!
page.get('https://httpbin.org/ip')
print(page.json)
```

**That's it!** Your proxy with authentication now works.

---

### 2. Block Resources (Fast Loading)

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()

# Block images for faster loading
page.set.block_resources(images=True)

# Or block multiple types
page.set.block_resources(images=True, css=True, fonts=True)

# Navigate
page.get('https://example.com')
# Loads 3x faster!
```

---

### 3. Combined (Fast + Anonymous)

```python
from DrissionPage import ChromiumPage, ChromiumOptions

# Setup proxy
co = ChromiumOptions()
co.set_proxy('user:pass@proxy.com:8080')

page = ChromiumPage(co)

# Enable both features
page.set.proxy_auth('user:pass@proxy.com:8080')
page.set.block_resources(images=True, css=True)

# Fast, anonymous browsing
page.get('https://example.com')
```

---

## 📋 Common Use Cases

### Scraping with Proxy

```python
co = ChromiumOptions()
co.set_proxy('user:pass@proxy.com:8080')

page = ChromiumPage(co)
page.set.proxy_auth('user:pass@proxy.com:8080')

urls = ['https://site1.com', 'https://site2.com']
for url in urls:
    page.get(url)
    data = page.ele('tag:article').text
    print(data)
```

### Fast Data Collection

```python
page = ChromiumPage()
page.set.block_resources(images=True, css=True, fonts=True)

for url in urls:
    page.get(url)
    # Loads 65% faster!
    data = extract_data(page)
```

### Block Tracking

```python
page = ChromiumPage()
page.set.block_resources(
    patterns=['google-analytics', 'facebook.com', 'doubleclick']
)

page.get('https://example.com')
# No tracking scripts loaded
```

---

## 🎯 Key Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `set_proxy()` | Set proxy in options | `co.set_proxy('user:pass@host:port')` |
| `proxy_auth()` | Enable authentication | `page.set.proxy_auth('user:pass@host:port')` |
| `block_resources()` | Block resources | `page.set.block_resources(images=True)` |
| `unblock_resources()` | Disable blocking | `page.set.unblock_resources()` |

---

## ⚡ Quick Tips

1. **Always call `proxy_auth()` after creating page**
   ```python
   page = ChromiumPage(co)
   page.set.proxy_auth(proxy)  # Right after!
   ```

2. **Block resources before navigating**
   ```python
   page.set.block_resources(images=True)
   page.get(url)  # Resources blocked during load
   ```

3. **Use environment variables for credentials**
   ```python
   import os
   proxy = os.getenv('PROXY_URL')
   ```

4. **Test blocking incrementally**
   ```python
   # Start with images
   page.set.block_resources(images=True)
   # Add more if page still works
   page.set.block_resources(images=True, css=True)
   ```

---

## 🧪 Test It

Run the test suite:
```bash
python test_enhanced_features.py
```

---

## 📚 Learn More

- **Full Documentation**: `ENHANCEMENTS_README.md`
- **Examples**: `ENHANCED_FEATURES.md`
- **Migration Guide**: `MIGRATION_GUIDE.md`
- **Summary**: `ENHANCEMENT_SUMMARY.md`

---

## ✅ Checklist

- [ ] Proxy authentication working?
- [ ] Resource blocking enabled?
- [ ] Page loading faster?
- [ ] Tests passing?

If yes to all, you're ready to go! 🎉

---

**Happy automating with enhanced DrissionPage!** 🚀
