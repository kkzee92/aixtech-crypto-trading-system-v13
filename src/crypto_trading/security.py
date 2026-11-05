"""Enhanced zero-trust security helpers: encryption, audit, anomaly, expanded redaction, DLP (v13)."""
import hashlib
import json
import re
from datetime import datetime, timezone
from typing import Dict, Any, List
from cryptography.fernet import Fernet
import os

def get_fernet() -> Fernet:
    key = os.environ.get("ENCRYPTION_KEY")
    if not key:
        # Generate ephemeral for demo only - never persist
        key = Fernet.generate_key().decode()
    return Fernet(key.encode() if isinstance(key, str) else key)

def encrypt_data(data: str) -> str:
    return get_fernet().encrypt(data.encode()).decode()

def decrypt_data(token: str) -> str:
    return get_fernet().decrypt(token.encode()).decode()

class AuditLog:
    def __init__(self):
        self.chain: List[str] = []

    def log(self, event: Dict[str, Any]) -> str:
        event = event.copy()
        event["timestamp"] = datetime.now(timezone.utc).isoformat()
        event["severity"] = event.get("severity", "info")
        payload = json.dumps(event, sort_keys=True)
        prev = self.chain[-1] if self.chain else "genesis"
        digest = hashlib.sha256(f"{prev}:{payload}".encode()).hexdigest()
        self.chain.append(digest)
        return digest

def detect_anomaly(values: List[float], threshold: float = 3.0) -> bool:
    if len(values) < 5:
        return False
    mean = sum(values) / len(values)
    std = (sum((x - mean)**2 for x in values) / len(values))**0.5
    return abs(values[-1] - mean) > threshold * std if std > 0 else False

def redact_secrets(text: str) -> str:
    """Expanded redaction for common secret patterns including JWT and more."""
    patterns = [
        (r'(api[_-]?key|secret|private[_-]?key|token|password)\s*[:=]\s*\S+', r'\1=***REDACTED***'),
        (r'\b[0-9a-fA-F]{64}\b', '***PRIVATE_KEY_REDACTED***'),  # hex private keys
        (r'\b([a-z]+\s+){11,23}[a-z]+\b', '***MNEMONIC_REDACTED***'),  # simple mnemonic pattern
        (r'AKIA[0-9A-Z]{16}', '***AWS_KEY_REDACTED***'),
        (r'ghp_[0-9a-zA-Z]{36}', '***GITHUB_PAT_REDACTED***'),
        (r'eyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+', '***JWT_REDACTED***'),
    ]
    for pat, repl in patterns:
        text = re.sub(pat, repl, text, flags=re.I)
    return text

def dlp_check(text: str) -> bool:
    """Simple DLP: return True if potential sensitive pattern detected."""
    sensitive = [
        r'\b[0-9a-fA-F]{64}\b',
        r'AKIA[0-9A-Z]{16}',
        r'ghp_[0-9a-zA-Z]{36}',
    ]
    for pat in sensitive:
        if re.search(pat, text):
            return True
    return False
