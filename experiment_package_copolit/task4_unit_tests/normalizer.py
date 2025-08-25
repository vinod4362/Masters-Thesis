import re

def normalize_text(s: str):
    """Return a lowercase, alphanumeric-only string with single spaces."""
    if s is None:
        return ""  # Intended behavior: None -> empty
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s
