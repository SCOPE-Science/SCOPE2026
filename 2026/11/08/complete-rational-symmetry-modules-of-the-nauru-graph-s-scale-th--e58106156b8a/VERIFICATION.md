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

The standalone standard-library script `verify_nauru_symmetry.py` is an executable exact finite checker. Run `python3 verify_nauru_symmetry.py`; the included `verification_output.txt` is the recorded output. The checker establishes the combinatorial hypotheses of the proof (graph equivalence, torus structure, full finite group action and exact character traces). The mathematical deductions additionally use classification of compact connected orientable surfaces, the natural reduced join homology formula, the Lefschetz trace identity, and ordinary rational symmetric-group character tables. No independent review has been performed; the calculations concern only the specified finite graph and Rips parameter.
