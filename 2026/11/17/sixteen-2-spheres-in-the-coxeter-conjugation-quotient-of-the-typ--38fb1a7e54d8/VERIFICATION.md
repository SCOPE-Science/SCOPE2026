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

# Reproduction

Run `python verify_h4.py` using a Python 3 environment with SymPy installed as in `requirements.txt`. The script uses only exact integer pairs representing \(\mathbb Z[\varphi]\) and exact rational matrix rank for the quotient boundaries.

The observed execution reached `ALL_EXACT_CHECKS_PASS`, with \(14400\) group elements, \(280\) noncrossing elements, \(20,93,90\) quotient cells and quotient boundary ranks \(19,74\). It verified the two orbit sizes responsible for the trivial fundamental group, \(c^{15}=-I\), the Burnside Euler identity and the rank filtration. The exact transcript of scientific counts is in `execution_record.txt`.

The finite-field screening only avoids costly exact minor tests and has the provable no-false-negative property stated in RESULT.md; all candidate interval elements are checked exactly. The historical literature comparisons are source-inspection judgments rather than a proof of global novelty. No external validation is represented as completed.
