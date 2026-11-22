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

# Computational and deductive verification

Run `python3 verify.py` with Python 3. The script independently lists all length-n binary words avoiding 001 and enumerates every coordinate-query support for n=1 through n=12, checking all 8,190 trace-shattering decisions. It separately checks the no-adjacent-triple support criterion, the complete face coefficients from the independence-polynomial decomposition, and the exact VC dimension. The largest examined instance n=12 has coefficients (1,12,66,165,210,126,28,1). The all-order proof comes from the absorbing-zero-suffix argument and the unique-terminal-pair partition in `RESULT.md`; finite tests alone cannot prove the general statement. Originality searches are not an independent priority certification.
