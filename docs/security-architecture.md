# Zero-Trust Cyber and Data Security Architecture (v13)

## Principles
- Never trust inputs: all feature data is validated and sanitized with expanded range checks.
- Least privilege: no live trading keys or withdrawal capabilities.
- Defense in depth: redaction + audit + anomaly detection + encryption helpers + DLP patterns.
- Auditability: hash-chained logs with timestamps and event typing for integrity verification.
- Data minimization: synthetic data preferred; no PII or real secrets. Explicit data classification.
- Threat modeling: expanded to cover data exfiltration, model poisoning proxies, and audit tampering.

## Components
- **Redaction**: Expanded regex patterns for API keys, private keys (hex), mnemonics, AWS keys, GitHub PATs, JWT tokens, etc.
- **AuditLog**: Hash-chained events with ISO timestamps and severity levels.
- **Anomaly Detection**: Statistical (z-score) on numeric features; can veto signals. Enhanced with multi-feature checks.
- **Encryption**: Fernet helpers for demo encryption of sensitive demo payloads (ephemeral keys).
- **Input Validation**: Type, range, and schema checks in strategies and data layer.
- **DLP**: Pattern-based detection for potential sensitive data in outputs and logs.

## Threat Model (Research Scope)
Focus on accidental secret leakage in logs, malformed data causing crashes, unauthorized modification of audit trails, data exfiltration via logs, and proxy model poisoning via bad inputs. Not intended as production trading infrastructure. Aligns with zero-trust principles for research systems.
