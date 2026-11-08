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

The standalone script `check_heisenberg.py` was executed successfully with Python 3. It directly constructs the finite-field Heisenberg group multiplication and the walk's full discrete distribution, then compares exact rational chi-square values with the closed formula and both total-variation bounds. It uses the irreducible polynomial \(T^2+T+1\) to implement the nonprime field \(\mathbb F_4\). Cases checked: prime-power field orders \(2,3,4,5\) at \(m=1\) for steps \(1\) through \(6\); \(q=7,m=1\) for steps \(1\) through \(5\); \(q=2,m=2\) for steps \(1\) through \(5\); \(q=3,m=2\) for steps \(1\) through \(3\); and \(q=2,m=3\) for steps \(1\) through \(4\).

Expected final output: `HEISENBERG_LAGRANGIAN_WALK_EXACT_CHECKS_PASS`.

These finite checks are corroboration, not a proof of any quantified infinite-family or asymptotic claim. The proof in `RESULT.md` supplies the representation-theoretic and probabilistic arguments. Independent audit and validation have not been performed.
