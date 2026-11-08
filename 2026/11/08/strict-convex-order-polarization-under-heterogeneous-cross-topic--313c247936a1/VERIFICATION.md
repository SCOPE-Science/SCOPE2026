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
# Verification

The analytic proof uses the geometric inverse expansion, the irreducibility-implied positivity of the comparison kernel, the preservation of its invariant left weight, and strict Jensen equality conditions. The asymptotic coefficient is derived on the invariant mean-zero subspace. These steps, rather than finite tests, establish the theorem for all sizes.

To reproduce the finite tests, run `python verify.py` with Python 3 and `sympy` available. The script uses exact rational matrix operations and deterministic sampling. It checked 48 directed positive stochastic matrices of sizes 2–5, their exact inverse identity and stationary distributions, three convex hinge functionals per matrix, and strict weighted variance inequalities. It also checked an exact two-person disagreement instance and an exact three-person failure of the analogous unweighted variance ordering, while verifying the strict opposite \(\pi\)-weighted comparison. All checks passed.

The finite sampling does not exhaust all directed graphs or establish originality. Independent scientific audit has not been performed.
