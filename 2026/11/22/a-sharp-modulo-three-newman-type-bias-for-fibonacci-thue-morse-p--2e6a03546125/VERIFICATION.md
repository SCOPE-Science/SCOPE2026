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

# Verification record

Exact reproducibility checks are contained in `verify.py`, executable by `python3 verify.py` with the Python standard library. The program constructs the ring \(\mathbb Z[\omega]\), where \(\omega^2+\omega+1=0\), and checks the eight-step matrix, its determinant and trace, and its quadratic matrix identity over integers. It also computes residue-class signed counts through an independent last-digit dynamic program and compares them with direct greedy Zeckendorf enumeration for all cutoffs through digit length 19.

Observed outcome: `PASS: 29575 integer assertions / comparisons; exact Z[omega] matrix [[(8, 1), (-1, -3)], [(3, 1), (0, -1)]] det (1, 0) trace (8, 0)`. The output includes the test vectors at digit lengths seven, fifteen, and twenty-three, respectively \((2,-1,-1)\), \((15,-8,-8)\), and \((121,-60,-60)\).

The checker also checks phase-seven formulas at all applicable lengths up to 91. Those finite checks cannot establish the infinite statements; the proof is the explicit recurrence and Cayley–Hamilton computation written in RESULT.md. The proof treats every nonnegative index and all nonnegative depth parameters without heuristic sampling or unverified finite exhaustion. No independent scientific audit has been performed.
