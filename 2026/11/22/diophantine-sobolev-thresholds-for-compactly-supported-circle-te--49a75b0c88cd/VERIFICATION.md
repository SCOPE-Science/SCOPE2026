---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

With probability Haar measure direct integration gives a_0=c²/(2π) and a_n=|1−e^{inc}|²/(2πn²) for n≠0. For p/q, the allowed nonconstant residue classes give uniform comparison with n⁻²; a missing Fourier coefficient is a continuous functional on C(T), and subtracting the atomic measures of two disjoint q-orbits annihilates all allowed modes. In the irrational case all frequencies are present, which gives uniform density by trigonometric polynomials and strict definiteness by uniqueness for finite measures. The O(n⁻²) upper bound and finite polynomials give continuous embedding in H¹ and density there; a sparse subsequence with summable n²a_n gives an H¹ member not in the RKHS by assigning coefficients √a_n. Testing single characters and then summing shows bounded inclusion iff inf (1+n²)^s a_n>0. The exponential difference is comparable to ||nα||, and the limsup formula for μ gives both strict regimes and the stated independent endpoint condition. Dividing in·f̂(n) by 1−e^{inc} gives the unique zero-mean transfer, and Parseval supplies exactly 2π and the separate constant term. The equation only sees the nonconstant part, so the claim is not restricted to mean-zero f. A single-character norm check and an exact q=3 orbit test were also verified. The frozen verify.py was inspected, not executed; its finite diagnostics do not certify Diophantine asymptotics, and the description of two continued-fraction regimes overstates the script, which samples one badly approximable example. No expert or formal certification is asserted.

## originality

PASS

Credit circle Pólya positivity, Fourier-diagonal RKHS theory, and small-divisor inversion as established ingredients. The supported distinct contribution is their exact identification for this particular compact-circle tent: the full arithmetic native-space inclusion frontier and the rotation-coboundary isometry alongside the rational support restriction. No inspected earlier statement supplies this package or the tent-specific isometric identification. This is a best-of-knowledge comparison, not a priority certificate.

## value

PASS

The same natural geodesic profile varies continuously with support length, while native-space containment can shift from excluded Fourier modes to dense proper containment with arbitrarily severe Sobolev loss. The complete exact arithmetic test, including the endpoint and a norm-preserving cohomological interpretation, answers when a regularity class is uniformly controlled by this kernel; plain positivity or general Parseval does not answer that question. No finite-site conditioning or universal cohomological inverse is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
