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

# Reproducibility

The accompanying `verify.py` is a standalone Python 3 script using only the standard library. Execute `python3 verify.py` in the directory containing that file. Expected final certificate lines include `VERIFY_OK`, exact finite bounds \(C<227/1000\) and \(S_{\le1000}<9/2000\), and the rational margin \(47/17200\). It also tests \(70\) direct congruences and \(299\) finite obstruction decompositions.

The script checks the finite claims in the proof with exact rational arithmetic and deterministic trial division. The tail comparisons and limiting density argument are proved symbolically in `RESULT.md`, not established by the script. Independent audit has not been performed.
