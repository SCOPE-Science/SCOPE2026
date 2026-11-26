---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The determinant sum gives the unnormalized volume. Uniform conditioning leaves the sine pair kernel g(t)=sqrt(1-t^2)/2-pi/8 and a bounded canonical cubic kernel. Under the row tilt, a two-index overlap in the cubic sum inserts one tilt factor in each conditional projection, and a one-index overlap inserts two; the variance bound O(n^3+n^4 epsilon^2+n^5 epsilon^4) is valid. It is negligible at both stated scales. Independent checks of the normalized Funk–Hecke integral, addition theorem and Parseval give degree-2m eigenvalue -a_m with multiplicity 4m+1, trace sum pi/8 and quadratic sum 1/6-pi^2/64. The degree-two zonal coordinate has exact mean epsilon/sqrt(5), all other positive-degree means vanish, and for every finite set of coordinates the row covariance tends to the identity by uniform convergence of the density and harmonic orthonormality. The infinite spectral tail is canonical under every row since it excludes degrees zero and two, so its scaled L2 norm tends uniformly to zero with the cutoff. The blocks, including the noncentral one, are independent in the limit. Trace summability gives almost-sure and L1 convergence; a finite set of chi-squares can all be small independently of the small-expected nonnegative tail, yielding the exact upper support edge. The degree-two projection under the row law has coefficient -a_1 epsilon; after dividing by n^(5/2)|epsilon| the remaining bounded canonical terms vanish and the one-coordinate triangular CLT gives a_1^2/5=pi^2/20480. Both signs and the exact row centering are consistent. The verifier was inspected, not executed; numerical quadrature is not the proof. No finite-sample support, arbitrary-mode or rate claim is verified.

## originality

FAIL

The main critical-window law is a covered specialization. García-Portugués–Paindaveine–Verdebout's Theorem 4(ii) already gives the entire infinite weighted chi-square law with exactly its first active even sector noncentral. The prior isotropic zonotope record supplies the very same spectral weights and the order-three-to-order-two geometric reduction at the null. The reduction transfers at the critical scale by elementary likelihood-ratio contiguity and deterministic centering; it does not need the stronger moving-law remainder estimate to imply the headline limit. The standardized Gaussian for larger vanishing tilts is not stated by Theorem 4(iii), which gives consistency, but follows by the usual first-projection CLT with the already known degree-two eigenvalue. No mathematical error is inferred from the prior coverage.

## value

FAIL

The geometric interpretation and exact constants are informative, but the distinctive critical noncentral law, its scale and support change are obtainable from the prior Sobolev law and the known isotropic projection. The remaining supercritical calculation restores the standard first-order CLT and inserts the prior degree-two eigenvalue. Its overlap bounds justify the exposition but are routine consequences of bounded-kernel degeneracy, and the frozen record does not identify a further geometric obstruction or nontrivial quantitative conclusion that would merit a narrower validation. No repaired claim is supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
