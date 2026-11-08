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

# Reproducibility and verification

Run `python verify_triangle.py` with a standard Python 3 interpreter. The source uses only `itertools` and `fractions`, and every asserted comparison uses exact rational or integer arithmetic, not floating-point approximations.

The verifier creates all \(15\) distinct labeled committees of size \(4\) from \(6\) candidates, computes harmonic satisfaction by voter-approval set intersections, and enumerates **every** greedy tie branch. Independently, it computes aggregated four-seat compositions in three capacity-two candidate classes using harmonic values scaled by \(12\). For every positive integer triple sorted by triangle-label symmetry with total electorate size at most \(17\), the two methods must produce identical sets of greedy and optimizing composition outcomes and identical scores. Exactly \(123\) triples have total size below \(17\), and \(24\) triples have size \(17\); their exact cutoff is checked.

A separate test evaluates \(2684\) positive rational weight ratios including all ratio-boundary points and verifies the complete seven-row analytical phase table. It also confirms exactly the optimal and greedy PAV scores in the \((5,5,7)\) witness.

The finite enumeration proves the **finite** minimal-electorate assertion because it exhausts the entire specified positive-integer domain below and at the witness size. It does not prove the infinite weight-ratio phase theorem; that theorem is proved algebraically in `RESULT.md`. The code, calculations, and review do not constitute an independent external audit.
