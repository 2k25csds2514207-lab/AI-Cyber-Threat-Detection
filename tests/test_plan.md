# Cyber Threat Detection - Testing Plan

## Threats to Test

1. DDoS
2. Botnet C2
3. DGA / DNS Tunnelling
4. Encrypted Malware
5. Port Scanning
6. Data Exfiltration

## Alert Validation

Every alert should contain:

- Timestamp
- Flow ID
- Threat Class
- Confidence Score
- Severity
- Supporting Evidence

## Basic Test Cases

| Threat | Expected Detection |
|---|---|
| DDoS | High traffic/packet rate |
| Botnet C2 | Repeated periodic communication |
| DGA/DNS Tunnelling | Suspicious DNS characteristics |
| Encrypted Malware | Suspicious TLS/QUIC metadata |
| Port Scanning | Many destination ports/hosts |
| Data Exfiltration | Unusual outbound data volume |
