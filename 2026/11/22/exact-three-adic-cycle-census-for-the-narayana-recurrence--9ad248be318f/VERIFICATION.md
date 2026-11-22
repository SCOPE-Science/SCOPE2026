---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification
The independent standard-library script `check.py` traverses the entire finite state space modulo \(3^k\) for \(k=1,2,3,4\). For each newly encountered state, it computes its actual least-period cycle by direct iteration and compares the complete cycle-length histogram with the theorem. This checks all 531,441 states for the largest modulus, and each smaller modulus exhaustively. It confirms the integer identity \(M^8-I=3B\), \(\det M=\det B=1\).

Expected and observed cycle counts are 5, 35, 299, and 2669. Observed longest cycle lengths are 8, 24, 72, and 216. Direct enumeration is finite evidence only; the written Hensel decomposition, three-adic lifting and fixed-point subtraction provide the all-level proof. There is no independent audit or computer-assisted formal certification.
