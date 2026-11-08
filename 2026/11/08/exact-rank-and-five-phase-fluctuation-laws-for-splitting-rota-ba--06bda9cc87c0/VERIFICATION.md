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

Run `python verify.py` with Python 3.9 or newer; no third-party dependencies are required.

The program independently enumerates all finite-field subspaces in canonical reduced row-echelon representation and verifies which are Lie subalgebras, then counts complementary pairs and rank multiplicities. For the three-dimensional boundary, it also enumerates all linear endomorphism matrices and directly tests idempotency and the weight-\(-1\) Lie Rota–Baxter identity. For five larger binary-field dimensions it checks numerical proximity to the five discrete-Gaussian profiles, using the exact finite rank counts.

The checks passed for subalgebra pairs at \((n,q)=(1,2),(1,3),(2,2)\) with rank distributions \((1,12,12,1)\), \((1,36,36,1)\), and \((1,240,960,960,240,1)\). Full matrix enumeration passed for the first two of these; all five asymptotic profile comparisons passed at \(n=60,61,62,63,64\), \(q=2\). Expected terminal line: `VERIFY_OK`.

These finite checks are not proofs of the universal assertions. The general proof uses the center, symplectic Grassmannian counting, a uniform finite-field product bound, and dominated convergence. No separate external review has been performed.
