def handler(event):
    name = event["input"].get("name", "World")
    return {
        "message": f"Hello, {name}!"
    }