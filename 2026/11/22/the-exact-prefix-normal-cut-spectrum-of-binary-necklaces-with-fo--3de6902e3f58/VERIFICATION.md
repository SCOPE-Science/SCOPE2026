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

Execute `python3 verify.py` from the directory containing the file. The script uses only the Python 3 standard library. It exactly enumerates all 75 surjective weak rank orders of four gap lengths and constructs integer-polynomial common-denominator certificates for each cut-count generating function. It then enumerates every four-one binary necklace at each length 4 through 20. For every necklace and every cut beginning at a one, it independently evaluates all lengths against every contiguous nonwrapping factor, compares to the gap inequality, and checks the resulting frequency against the rational generating function by exact coefficients. No experiments substitute for the unbounded weak-order/Burnside proof in RESULT.md.

Expected closing line: `VERIFY_OK: 75 exhaustive weak orders, exact polynomial identity, and every four-one necklace length 4..20 checked by literal factor inequalities`.

Checks do not address historical priority, weights other than four, or infinite periodic variants. The separately claimed limiting fractions follow from rational pole orders, not a finite simulation.
