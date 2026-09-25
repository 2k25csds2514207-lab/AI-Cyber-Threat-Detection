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
### Test Case Details

#### Test Case 1: Normal Traffic
- Input: Normal network traffic
- Expected Output: No threat detected
- Expected Severity: Low

#### Test Case 2: DDoS
- Input: High-volume repeated requests
- Expected Output: DDoS threat detected
- Expected Severity: High

#### Test Case 3: Port Scanning
- Input: Multiple connection attempts to different ports
- Expected Output: Port scanning detected
- Expected Severity: Medium

#### Test Case 4: DGA / DNS Tunnelling
- Input: Suspicious DNS request patterns
- Expected Output: DNS tunnelling detected
- Expected Severity: High

#### Test Case 5: Data Exfiltration
- Input: Unusual outbound data transfer
- Expected Output: Data exfiltration detected
- Expected Severity: High
- ## Expected Outputs

### DDoS
- Alert should be generated for unusually high traffic volume.
- Threat class should be identified as DDoS.
- Confidence score should be present.

### Botnet C2
- Alert should be generated for suspicious periodic communication.
- Threat class should be identified as Botnet C2.
- Supporting evidence should be present.

### DGA / DNS Tunnelling
- Alert should be generated for suspicious DNS activity.
- Threat class should be identified correctly.
- Confidence score should be present.

### Encrypted Malware
- Alert should be generated for suspicious encrypted traffic.
- Threat class should be identified as Encrypted Malware.
- Supporting evidence should be present.

### Port Scanning
- Alert should be generated for multiple port connection attempts.
- Threat class should be identified as Port Scanning.
- Severity should be present.

### Data Exfiltration
- Alert should be generated for unusual outbound data transfer.
- Threat class should be identified as Data Exfiltration.
- Supporting evidence should be present.
