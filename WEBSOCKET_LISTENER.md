# WebSocket Listener - DrissionPage

## 🎯 Overview

The WebSocket listener allows you to monitor and capture WebSocket frames (both sent and received) from browser tabs in real-time.

---

## 🚀 Quick Start

### Basic Usage

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://example.com')  # Site with WebSocket

# Start listening to all WebSockets
page.ws_listen.start()

# Get frames
frame = page.ws_listen.get_frame(timeout=5)
print(f"Direction: {frame['_direction']}")  # 'sent' or 'received'
print(f"Payload: {frame['response']['payloadData']}")
```

---

## 📖 API Reference

### Starting the Listener

```python
# Listen to all WebSocket connections
page.ws_listen.start()

# Listen to specific WebSocket URL
page.ws_listen.start(targets='wss://example.com/socket')

# Listen to multiple URLs
page.ws_listen.start(targets=['socket1.com', 'socket2.com'])

# Use regex pattern
page.ws_listen.start(targets=r'wss://.*\.example\.com', is_regex=True)
```

### Getting Frames

```python
# Blocking get (waits for next frame)
frame = page.ws_listen.get_frame(timeout=10)

# Non-blocking get
try:
    frame = page.ws_listen.get_frame_nowait()
except Empty:
    print("No frames available")
```

### Frame Structure

```python
frame = {
    '_direction': 'received',  # or 'sent'
    'requestId': '...',
    'timestamp': 123456.789,
    'response': {
        'opcode': 1,  # 1=text, 2=binary
        'mask': False,
        'payloadData': '{"type":"message","data":"..."}'
    }
}
```

### Stopping the Listener

```python
# Stop listening
page.ws_listen.stop()

# Clear queued frames
page.ws_listen.clear_frames()
```

---

## 💡 Examples

### Example 1: Monitor All WebSocket Traffic

```python
from DrissionPage import ChromiumPage
from queue import Empty

page = ChromiumPage()
page.get('https://websocket-echo.com')

# Start listening
page.ws_listen.start()

# Monitor for 30 seconds
import time
end_time = time.time() + 30

while time.time() < end_time:
    try:
        frame = page.ws_listen.get_frame(timeout=1)
        direction = frame['_direction']
        payload = frame['response']['payloadData']
        print(f"[{direction.upper()}] {payload}")
    except Empty:
        continue

page.ws_listen.stop()
```

### Example 2: Filter Specific WebSocket

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://example.com')

# Only listen to specific WebSocket
page.ws_listen.start(targets='wss://api.example.com/live')

while True:
    frame = page.ws_listen.get_frame()
    data = frame['response']['payloadData']
    
    # Process data
    if 'important' in data:
        print(f"Important message: {data}")
        break

page.ws_listen.stop()
```

### Example 3: Binary Data Handling

```python
from DrissionPage import ChromiumPage
from base64 import b64decode

page = ChromiumPage()
page.get('https://binary-websocket-site.com')

page.ws_listen.start()

frame = page.ws_listen.get_frame()
opcode = frame['response']['opcode']

if opcode == 1:  # Text
    data = frame['response']['payloadData']
    print(f"Text: {data}")
elif opcode == 2:  # Binary
    binary_data = b64decode(frame['response']['payloadData'])
    print(f"Binary: {binary_data}")

page.ws_listen.stop()
```

### Example 4: Background Thread Consumer

```python
from DrissionPage import ChromiumPage
from queue import Empty
import threading

class WebSocketMonitor:
    def __init__(self, page, target_url):
        self.page = page
        self.running = False
        self.thread = None
        
        # Start listener
        page.ws_listen.start(targets=target_url)
    
    def _consumer(self):
        """Background thread to consume frames"""
        while self.running:
            try:
                frame = self.page.ws_listen.get_frame(timeout=1)
                self._process_frame(frame)
            except Empty:
                continue
    
    def _process_frame(self, frame):
        """Process received frame"""
        direction = frame['_direction']
        payload = frame['response']['payloadData']
        print(f"[{direction}] {payload}")
    
    def start(self):
        """Start background consumer"""
        self.running = True
        self.thread = threading.Thread(target=self._consumer, daemon=True)
        self.thread.start()
    
    def stop(self):
        """Stop consumer and listener"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)
        self.page.ws_listen.stop()

# Usage
page = ChromiumPage()
page.get('https://example.com')

monitor = WebSocketMonitor(page, 'wss://api.example.com')
monitor.start()

# Do other things while monitoring in background
import time
time.sleep(60)

monitor.stop()
```

### Example 5: Regex Pattern Matching

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('https://example.com')

# Listen to multiple domains using regex
pattern = r'wss://(api|ws|socket)\.example\.com'
page.ws_listen.start(targets=pattern, is_regex=True)

frame = page.ws_listen.get_frame()
print(frame['response']['payloadData'])

page.ws_listen.stop()
```

---

## 🔍 Advanced Usage

### Multiple Tabs

```python
from DrissionPage import ChromiumPage

page = ChromiumPage()

# Tab 1
tab1 = page.new_tab('https://site1.com')
tab1.ws_listen.start(targets='wss://site1.com/socket')

# Tab 2
tab2 = page.new_tab('https://site2.com')
tab2.ws_listen.start(targets='wss://site2.com/socket')

# Listen to both
frame1 = tab1.ws_listen.get_frame(timeout=5)
frame2 = tab2.ws_listen.get_frame(timeout=5)

tab1.ws_listen.stop()
tab2.ws_listen.stop()
```

### JSON Data Parsing

```python
from DrissionPage import ChromiumPage
import json

page = ChromiumPage()
page.get('https://example.com')

page.ws_listen.start()

frame = page.ws_listen.get_frame()
payload = frame['response']['payloadData']

# Parse JSON
try:
    data = json.loads(payload)
    print(f"Type: {data.get('type')}")
    print(f"Message: {data.get('message')}")
except json.JSONDecodeError:
    print(f"Not JSON: {payload}")

page.ws_listen.stop()
```

---

## 📊 Frame Opcodes

| Opcode | Type | Description |
|--------|------|-------------|
| 0 | Continuation | Continuation frame |
| 1 | Text | Text message (UTF-8) |
| 2 | Binary | Binary data |
| 8 | Close | Connection close |
| 9 | Ping | Ping frame |
| 10 | Pong | Pong frame |

---

## ⚠️ Important Notes

1. **Start before navigation**: Start the listener before the WebSocket connection is established
   ```python
   page.ws_listen.start()
   page.get('https://example.com')  # WebSocket connects here
   ```

2. **Memory management**: Clear frames periodically if not consuming
   ```python
   page.ws_listen.clear_frames()
   ```

3. **Stop when done**: Always stop the listener to free resources
   ```python
   page.ws_listen.stop()
   ```

4. **Timeout handling**: Use timeouts to avoid blocking forever
   ```python
   frame = page.ws_listen.get_frame(timeout=10)
   ```

---

## 🆚 Comparison with HTTP Listener

| Feature | HTTP Listener (`listen`) | WebSocket Listener (`ws_listen`) |
|---------|-------------------------|----------------------------------|
| Protocol | HTTP/HTTPS | WebSocket (ws/wss) |
| Data | Request/Response | Frames (bidirectional) |
| Direction | Request → Response | Sent ↔ Received |
| Use Case | API calls, page loads | Real-time data, live updates |

---

## 🐛 Troubleshooting

### No Frames Received

**Problem**: `get_frame()` times out

**Solutions**:
```python
# 1. Start listener before WebSocket connects
page.ws_listen.start()
page.get('https://example.com')

# 2. Check target URL is correct
page.ws_listen.start(targets='correct-websocket-url')

# 3. Use regex if URL is dynamic
page.ws_listen.start(targets=r'wss://.*\.example\.com', is_regex=True)
```

### Memory Issues

**Problem**: Too many frames queued

**Solution**:
```python
# Clear frames periodically
page.ws_listen.clear_frames()

# Or consume frames in background thread
```

---

## 📝 Complete Example

```python
from DrissionPage import ChromiumPage
from queue import Empty
import json

def monitor_websocket(url, ws_target, duration=60):
    """Monitor WebSocket traffic for specified duration"""
    page = ChromiumPage()
    
    # Start listener before loading page
    page.ws_listen.start(targets=ws_target)
    
    # Load page (WebSocket will connect)
    page.get(url)
    
    import time
    end_time = time.time() + duration
    
    print(f"Monitoring WebSocket: {ws_target}")
    print("=" * 60)
    
    while time.time() < end_time:
        try:
            frame = page.ws_listen.get_frame(timeout=1)
            
            direction = frame['_direction']
            opcode = frame['response']['opcode']
            payload = frame['response']['payloadData']
            
            # Parse based on opcode
            if opcode == 1:  # Text
                try:
                    data = json.loads(payload)
                    print(f"[{direction.upper()}] JSON: {data}")
                except:
                    print(f"[{direction.upper()}] Text: {payload}")
            elif opcode == 2:  # Binary
                print(f"[{direction.upper()}] Binary: {len(payload)} bytes")
            else:
                print(f"[{direction.upper()}] Opcode {opcode}")
            
        except Empty:
            continue
    
    page.ws_listen.stop()
    page.quit()
    print("=" * 60)
    print("Monitoring complete")

# Usage
monitor_websocket(
    url='https://example.com',
    ws_target='wss://api.example.com/live',
    duration=30
)
```

---

## ✨ Summary

The WebSocket listener provides:
- ✅ Real-time WebSocket frame monitoring
- ✅ Bidirectional traffic capture (sent & received)
- ✅ URL filtering (exact match or regex)
- ✅ Text and binary data support
- ✅ Simple, intuitive API
- ✅ Thread-safe operation

**Perfect for**: Live data monitoring, debugging WebSocket applications, capturing real-time events, testing WebSocket implementations.
