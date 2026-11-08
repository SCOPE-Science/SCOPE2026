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
The proof of the all-parameter assertion is analytic: four-point Fourier interpolation, a nonzero matrix determinant, the Hermitian low-rank criterion, explicit failure witnesses and the odd-determinant lower bound.

Reproduce the finite exact check with `python verify_two_square.py`. Expected message:

`TWO_SQUARES_PASS rank=8 nullspace=1 det_diagonal=-6 distinct_nodes=8 alias_counterexample=PASS same_circle=PASS`

The finite checks use symbolic Gaussian-integer arithmetic and verify one nondegenerate sample geometry, exact radial identities and untwisted failure. The checker does not certify the universal parameter theorem or establish originality. No independent mathematical audit has been performed.
