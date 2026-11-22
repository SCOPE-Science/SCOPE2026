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

For two Gaussian densities of unit mass and strictly Loewner-comparable positive covariance forms A,B (d>=3), Gaussian Fourier evaluation yields I=2exp(-S)(cosh Q+cos H), S=(A+B)/2 quadratic, Q=(A-B)/2 positive definite quadratic, H linear center difference. The measured logarithmic jets obey L2=−S−H²/4 and L4=Q²/4−H⁴/96; hence M=S+H²/4 and T=4L4=Q²−R² where R=H²/sqrt(24) is PSD rank at most one. In d>=3, Q+R is positive definite and Q−R has ≥d−1>=2 positive directions (possibly one negative or one zero); both are irreducible real quadratics and distinct if R!=0. Polynomial unique factorization determines their factors up to reciprocal scale/exchange. A nonzero multiple of full-rank Q plus rank-one R has rank≥d−1>=2, so the rank≤1 constraint forces scale=1; exchanging factors would make R negative. R=0 is handled by unique positive definite square root of T. Then H², S and the unordered covariance pair recover uniquely, modulo center sign, common translation and component exchange. Complete derivative data through 4 determine L2,L4; nothing relies on full intensity. Independently expanded the proposed planar Q1,R1 and Q2,R2 with SymPy and verified exactly Q1²−R1²=Q2²−R2². Choosing S2 to align M gives distinct positive definite planar covariance pairs with identical quartic data; the n-dimensional order-two example keeps S,H fixed and varies Q. The general proof is algebraic; a finite SymPy identity is not a proof of uniqueness.

## originality

PASS

PASS for full anisotropic strictly Loewner-ordered Gaussian pairs in all d>=3 with finite PHASELESS fourth jet and sharp planar counterexample; lower-dimensional isotropic published theorem and ordinary mixture moments do not imply this higher-rank unique factorization claim.

## value

PASS

A global recovery theorem from a finite phaseless intensity jet for a motivated anisotropic two-Gaussian model is a substantial structural inverse result. The exact d3 factorization threshold and explicit sharp d2 ambiguity explain the role of covariance ordering, unlike a mere parameter fit, and demonstrate a mathematically meaningful boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
