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

The pullback of the j-th block monomial has external character u^B v^(i+C) w^C, so distinct triples are orthogonal even with the multiplier weight |a|². Factoring (z−1)^i(z+1)^δ z^m leaves powers t^(m−j), where t=(2+z+z^(−1))/4; the normalized circular measure pushes to the arcsine density. This gives the stated beta weight and compressed multiplication by 1−t. Its characteristic polynomial is the degree-(m+1) orthogonal polynomial after the linear change of variable ζ=1−2t, which gives the stated Jacobi parameters and accounts for the whole multiset. On the larger space of all circle polynomials of degree at most N the squared multiplier form is the (N+1)-path tridiagonal with diagonal 1/2 and off-diagonal −1/4, giving the lower bound and a unique sine-coefficient minimizer. That polynomial has degree N, is nonzero at +1, and has order zero at −1 for even N and order one for odd N, from its finite sine-sum generating identity. Its reciprocity then places it in exactly the one even or two odd blocks claimed, since a degree-N component forces i+B+C=N. This also covers N=0 and guards against missing multiplicities. A separately rebuilt beta Gram/generalized-eigenvalue calculation through N=8 matched the block spectra (maximum discrepancy 1.39e−12), the minima, and the parity counts.

## originality

PASS

The distinct contribution is the sharp global cutoff minimum and exact equality multiplicity, not the Haar space, the path spectrum, or independent originality for the per-block Jacobi spectrum. Explicit prior Wold-block Gram data make the latter a classical compression consequence. Neither those data nor the standard path bound already identify which of the actual hexablock blocks contain a global equality vector; the cutoff and reciprocity/order classification are essential.

## value

PASS

The natural homogeneous cutoff comes from the space, not from choosing ad hoc examples. Its exact least singular value quantifies how finite-degree inversion on the image loses conditioning with N, and the parity law identifies exactly the independent modes causing that loss. This provides a finite-dimensional stability invariant not supplied by an abstract shift decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
