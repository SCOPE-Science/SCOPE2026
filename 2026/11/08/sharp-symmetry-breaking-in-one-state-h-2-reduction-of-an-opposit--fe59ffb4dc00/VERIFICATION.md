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

The normalized delay-free factor and the physical transfer function have equal \(H_2\) approximation error because multiplication by \(z\) is norm-preserving on the unit circle. The claimed minimization uses every \(\lambda\) in the open complex unit disk, every \(c\in\mathbb C\), and every \(a>0\), \(0<p<1\).

Run `python3 verify.py` in a directory containing the extracted standalone checker. It performs exact rational arithmetic at six values of the squared pole modulus, verifies both branches of the captured-norm formula, checks the rational example \(p^2=3/4\), independently reconstructs six infinite-horizon errors from 300 impulse coefficients per model and compares them to the exact geometric sums, and tests the global angular/radial captured-norm bound at 58,500 seeded complex samples.

The proof is analytic and is not based on the finite sampling: orthogonal Hardy projection, reverse triangle inequality, strict radial derivative analysis, and a Taylor expansion cover the infinite quantifiers. The 300-term reconstructions approximate the infinite impulse norm and are not themselves convergence certificates. Exact-rational identities in the checker are supplementary to the hand-verifiable algebra. No external or independent mathematical audit is represented by these tests.
