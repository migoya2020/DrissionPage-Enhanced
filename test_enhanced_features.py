#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for enhanced DrissionPage features
"""

def test_proxy_auth():
    """Test proxy with authentication"""
    print("\n=== Testing Proxy Authentication ===")
    try:
        from DrissionPage import ChromiumPage, ChromiumOptions
        
        # Example proxy (replace with your actual proxy)
        proxy = 'username:password@proxy.example.com:8080'
        
        co = ChromiumOptions()
        co.set_proxy(proxy)
        
        page = ChromiumPage(co)
        
        # Enable proxy authentication
        success = page.set.proxy_auth(proxy)
        
        if success:
            print("✓ Proxy authentication enabled successfully")
            print(f"  Proxy: {proxy}")
        else:
            print("✗ Failed to enable proxy authentication")
        
        # Test with a simple request
        # page.get('https://httpbin.org/ip')
        # print(f"  Response: {page.json}")
        
        page.quit()
        print("✓ Proxy auth test completed")
        
    except Exception as e:
        print(f"✗ Proxy auth test failed: {e}")


def test_resource_blocking():
    """Test resource blocking"""
    print("\n=== Testing Resource Blocking ===")
    try:
        from DrissionPage import ChromiumPage
        
        page = ChromiumPage()
        
        # Test blocking images
        print("Testing image blocking...")
        page.set.block_resources(images=True)
        print("✓ Image blocking enabled")
        
        # Test blocking multiple resources
        print("Testing multiple resource blocking...")
        page.set.block_resources(images=True, css=True, fonts=True)
        print("✓ Multiple resource blocking enabled")
        
        # Test custom patterns
        print("Testing custom pattern blocking...")
        page.set.block_resources(patterns=['analytics', 'tracking'])
        print("✓ Custom pattern blocking enabled")
        
        # Test unblocking
        print("Testing unblock...")
        page.set.unblock_resources()
        print("✓ Resources unblocked")
        
        page.quit()
        print("✓ Resource blocking test completed")
        
    except Exception as e:
        print(f"✗ Resource blocking test failed: {e}")


def test_combined():
    """Test proxy auth + resource blocking together"""
    print("\n=== Testing Combined Features ===")
    try:
        from DrissionPage import ChromiumPage, ChromiumOptions
        
        # Setup (use your actual proxy)
        proxy = 'username:password@proxy.example.com:8080'
        
        co = ChromiumOptions()
        co.set_proxy(proxy)
        
        page = ChromiumPage(co)
        
        # Enable both features
        page.set.proxy_auth(proxy)
        print("✓ Proxy auth enabled")
        
        page.set.block_resources(images=True, css=True)
        print("✓ Resource blocking enabled")
        
        print("✓ Combined features test completed")
        
        page.quit()
        
    except Exception as e:
        print(f"✗ Combined test failed: {e}")


def test_proxy_parsing():
    """Test proxy URL parsing"""
    print("\n=== Testing Proxy URL Parsing ===")
    try:
        from DrissionPage._units.proxy_auth import ProxyAuth
        
        class MockOwner:
            pass
        
        pa = ProxyAuth(MockOwner())
        
        test_cases = [
            'user:pass@proxy.com:8080',
            'http://user:pass@proxy.com:8080',
            'https://user:pass@proxy.com:8080',
            'myuser:myp@ss@10.0.0.1:3128',
        ]
        
        for proxy in test_cases:
            result = pa._parse_proxy(proxy)
            if result:
                print(f"✓ Parsed: {proxy}")
                print(f"  Username: {result['username']}")
                print(f"  Password: {result['password']}")
                print(f"  Host: {result['host']}")
            else:
                print(f"✗ Failed to parse: {proxy}")
        
        print("✓ Proxy parsing test completed")
        
    except Exception as e:
        print(f"✗ Proxy parsing test failed: {e}")


def main():
    """Run all tests"""
    print("=" * 60)
    print("DrissionPage Enhanced Features Test Suite")
    print("=" * 60)
    
    test_proxy_parsing()
    test_resource_blocking()
    # test_proxy_auth()  # Uncomment when you have a real proxy
    # test_combined()    # Uncomment when you have a real proxy
    
    print("\n" + "=" * 60)
    print("Test suite completed!")
    print("=" * 60)


if __name__ == '__main__':
    main()
