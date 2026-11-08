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

# Verification procedure

Run `python3 verify_nilclean.py` in a Python 3 standard-library environment. It lists all matrices \(A\), idempotents \(P\) and nilpotents \(N\) for \(q=2,3,4,5,7\), accumulates the actual decomposition count of each \(A=P+N\), and independently compares each count to the eigenline formula. It checks the number of idempotents and nilpotents, the total mass, the size of the nil-clean locus and the largest fiber. The extension field \(\mathbb F_4\) is represented by \(\mathbb F_2[T]/(T^2+T+1)\).

Expected standard output is stored as `verification_output.txt`. The exact enumerations are finite; the all-prime-power theorem is established by the mathematical argument in `RESULT.md`. No third-party code or data are required.
