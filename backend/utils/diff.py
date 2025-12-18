import difflib

def generate_diff(original: str, updated: str) -> str:
    diff = difflib.unified_diff(
        original.splitlines(),
        updated.splitlines(),
        lineterm=""
    )
    return "\n".join(diff)
