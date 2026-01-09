# 🚀 Quick Publishing Reference

## One-Command Publishing

### GitHub
```bash
git init && git add . && git commit -m "v4.2.0" && \
git remote add origin https://github.com/YOURUSERNAME/DrissionPage-Enhanced.git && \
git push -u origin main && \
git tag v4.2.0 && git push origin v4.2.0
```

### PyPI
```bash
rm -rf build dist *.egg-info && \
python setup.py sdist bdist_wheel && \
twine upload dist/*
```

---

## 📝 Before Publishing

1. **Update version**: Already done → `4.2.0`
2. **Update setup.py**: Already done → `DrissionPage-Enhanced`
3. **Test locally**: `python test_standalone.py` ✅
4. **Update README**: Use `README_ENHANCED.md`

---

## 🔑 What You Need

### GitHub
- GitHub account
- Repository name: `DrissionPage-Enhanced`
- Git installed

### PyPI
- PyPI account (create at https://pypi.org/account/register/)
- API token (get at https://pypi.org/manage/account/token/)

---

## 📦 Package Info

- **Name**: `DrissionPage-Enhanced`
- **Version**: `4.2.0`
- **Install**: `pip install DrissionPage-Enhanced`
- **Import**: `from DrissionPage import ChromiumPage` (same as original!)

---

## ✅ Quick Test After Publishing

```bash
# Create test environment
python -m venv test_env
source test_env/bin/activate  # Linux/Mac
# test_env\Scripts\activate  # Windows

# Install
pip install DrissionPage-Enhanced

# Test
python -c "
from DrissionPage import ChromiumPage, ChromiumOptions
co = ChromiumOptions()
print('✅ Import successful!')
print('✅ Version:', co.__class__.__module__)
"
```

---

## 🎯 URLs to Update

After publishing, update these in `README_ENHANCED.md`:

```markdown
Replace:
https://github.com/yourusername/DrissionPage-Enhanced

With:
https://github.com/YOURUSERNAME/DrissionPage-Enhanced
```

---

## 📊 Post-Publishing

1. **GitHub**: Create release with changelog
2. **PyPI**: Verify package page looks good
3. **Test**: Install and test in clean environment
4. **Announce**: Share on social media, forums

---

## 🆘 Quick Fixes

### Wrong package name?
```bash
# Edit setup.py, change name, rebuild
python setup.py sdist bdist_wheel
twine upload dist/*
```

### Forgot to include files?
```bash
# Update MANIFEST.in
# Increment version to 4.2.1
# Rebuild and upload
```

### Need to delete release?
- PyPI: Can't delete, must upload new version
- GitHub: Can delete release and tag

---

**Ready? Follow [PUBLISHING_GUIDE.md](PUBLISHING_GUIDE.md) for detailed steps!**
