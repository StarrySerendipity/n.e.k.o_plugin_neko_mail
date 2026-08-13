import json
import urllib.request

SESSION = "neko-plugin-upload"
BASE = "http://127.0.0.1:10086/command"

def send(action, args=None):
    payload = json.dumps({"action": action, "args": args or {}, "session": SESSION}).encode("utf-8")
    req = urllib.request.Request(BASE, data=payload, headers={"Content-Type": "application/json; charset=utf-8"})
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read().decode("utf-8"))

# 填写仓库 URL
repo_url = "https://github.com/StarrySerendipity/n.e.k.o_plugin_neko_mail"
js_set_url = f"""
(() => {{
    const input = document.querySelector('input[placeholder*="仓库"]') ||
                  document.querySelector('input[name*="url"]') ||
                  document.querySelector('input[type="url"]');
    if (input) {{
        const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
            window.HTMLInputElement.prototype, 'value').set;
        nativeInputValueSetter.call(input, {json.dumps(repo_url)});
        input.dispatchEvent(new Event('input', {{ bubbles: true }}));
        input.dispatchEvent(new Event('change', {{ bubbles: true }}));
        return 'URL set: ' + input.value;
    }}
    // 如果找不到，尝试所有 input
    const inputs = document.querySelectorAll('input');
    for (let i = 0; i < inputs.length; i++) {{
        if (inputs[i].type === 'text' || inputs[i].type === 'url' || !inputs[i].type) {{
            const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                window.HTMLInputElement.prototype, 'value').set;
            nativeInputValueSetter.call(inputs[i], {json.dumps(repo_url)});
            inputs[i].dispatchEvent(new Event('input', {{ bubbles: true }}));
            inputs[i].dispatchEvent(new Event('change', {{ bubbles: true }}));
            return 'URL set (fallback): ' + inputs[i].value;
        }}
    }}
    return 'input not found';
}})()
"""
result = send("evaluate", {"code": js_set_url})
print(f"URL: {result}")
