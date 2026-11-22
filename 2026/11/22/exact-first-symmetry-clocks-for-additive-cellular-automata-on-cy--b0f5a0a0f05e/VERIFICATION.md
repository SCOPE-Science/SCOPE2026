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

The accompanying `check_symmetry.py` enumerates finite-ring initial states directly, applies subtraction in \(\mathbb F_{p^h}\) in its prime-field vector-space coordinates, detects first nontrivial cyclic translation symmetry, and stops on first repeated state when none occurs. It independently calculates Möbius counts and compares exact integer histograms. The tested dimensions are \(q=2\), lengths 2–12; \(q=3\), lengths 2–8; \(q=4\), lengths 2–6; and \(q=9\), lengths 2–4: 26 cases, 30,852 initial states. All checks passed from the embedded source.

These finite checks validate examples and guard against normalization and formula errors. All-length correctness rests on the kernel-gcd and inclusion–exclusion proof in `RESULT.md`. An expert independent audit is not performed. The proof does not cover nonunit multipliers or generalized nonlinear automata.
