---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For distinct three sites, the Fourier spectral positivity and Vandermonde argument establish positive-definite covariance. Inverting its 3x3 Toeplitz Gram matrix gives Q13=(H_t(a)^2-H_t(0)H_t(2a))/det. For q=e^{-t} and r=q^(2j-1), each theta-product factor obeys B_r(c)^2-A_r C_r(c)=4r(1-c)(c(1+r+r²)+r); at c=0 all are positive, at c=-1/3 all negative. The log derivative 4r/B_r-8rc/C_r is strictly positive for c in [-1/3,0], and geometric decay permits termwise differentiation. For c outside this interval the factor signs preclude another zero. The periodic Gaussian Poisson formula yields 4t log R -> -2a²+4(pi-a)², root pi(2-sqrt 2), and the first product factor yields c_t=-exp(-t)+O(exp(-2t)). Independently evaluated theta matrices at t=.03,.3,1,4,10 and checked factor identity and sign/root; that is only corroboration.

## originality

PASS

The specific Schur-complement zero-crossing, strict global uniqueness and heat-scale limit are not statements of covariance-kernel construction or of equispaced precision sign theorems. Best-of-knowledge originality PASS under explicitly qualified classical theta-inequality priority risk.

## value

PASS

The smallest nontrivial Gaussian graphical-model conditional-independence geometry is a natural three-site configuration. A complete universal transition between positive and negative partial dependences and sharp heat-time endpoint positions gives a nontrivial, reusable precision-sign classification rather than merely a formula for the covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
