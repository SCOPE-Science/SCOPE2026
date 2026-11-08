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

# Verification and reproducibility

The mathematical claim is proved from the Lyndon proper-suffix criterion, a disjoint marker-count classification, a partition into six integer order chambers, and the uniform simplex limit for weak compositions. No external computational oracle is needed to prove it.

Run `python3 verify_lyndon.py` with Python 3. The program independently lists distinct substrings and checks the Lyndon suffix test for each three-one word through length 21; it separately expands the rational generating function as a product of geometric series, checks a gap sum through length 70, and recomputes the limiting mean and variance with exact rational arithmetic. Its expected final output is `VERIFY_OK`. The source code is included as a complete standalone file, and all checks apply to the formula and domain stated in `RESULT.md`.

Finite enumeration is not an exhaustive argument over all lengths. The all-length proof is the factor-by-factor characterization and six-chamber geometric-series derivation. The probability limit uses convergence of normalized uniform weak compositions and bounded moments. The literary-priority comparison is subject to possible uncatalogued sources; no external independent mathematical audit has been performed.
