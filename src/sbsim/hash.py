import hashlib


def sha256_file(path: str) -> str:
    """
    Compute SHA-256 of a file using streaming (memory-safe).
    """
    h = hashlib.sha256()

    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)

    return h.hexdigest()
