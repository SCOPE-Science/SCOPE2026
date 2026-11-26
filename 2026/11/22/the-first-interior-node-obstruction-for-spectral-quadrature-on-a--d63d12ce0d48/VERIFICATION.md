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

For fixed sites, duality of the operator and nuclear norms makes the optimal linear error the distance of G to the span of the evaluation matrices. The same distance is a lower bound for adaptive nonlinear procedures by following the zero-input path and using opposite inputs in their common information kernel. This also works for the quotient class of functions because integral and evaluations are well defined linear functionals of the represented function. For a symmetric approximant Q, testing G−Q against the orthogonal projector onto ran(Q)⊥ bounds the nuclear error below by the spectral tail. Equality forces Q to have rank n (all eigenvalues of G are positive in the stated range), its range to maximize captured spectral trace, and G−Q to be positive and supported on that range's complement. For n=r+1≤d+1, the range is the vacuum plus an r-plane in the first-excitation shell. A representation of this positive rank-(r+1) matrix by at most r+1 atoms forces all coefficients positive by inertia. Each product evaluation vector then lies in the vacuum-plus-shell range, so at most one angle is nonzero; two nonzero angles would create a double excitation, since all cosines on the cube are positive. The active axes span that r-plane and each axis needs two opposite signs to cancel its vacuum cross entry. Thus 2r atoms are necessary, exceeding r+1 for r≥2. A sequence approaching equality would have a bounded subsequence of matrices converging to such an equality matrix. Its positive rank forces all r+1 coefficients eventually positive, and since each atom has trace one their sum is bounded. Compactness of the sites and bounded coefficients then yields the forbidden representation. For the specified H, the vacuum cost per excitation is at least cot²(1/4). Independent alternating-series bounds give 47≤q/p≤3761/79<50 and 15<cot²(1/4)<31/2, so the feasibility ratio is strictly between 3 and 4. For r≤3, equal-weight symmetric pairs at angles ±arctan√(rp/q) cancel the cross terms and attain both diagonals; the angle bound places both nodes inside the cube. Zero evaluations give error tr G=1, the central node attains the one-evaluation tail, and one symmetric pair attains the two-evaluation tail, including exact integration at d=1,n=2.

## originality

PASS

The supported distinct claims are the exact onset of nonattainment of a spectral-tail bound on this specified matrix-ball class, including strict loss even for adaptive nonlinear algorithms, and the positive cube-atomic feasibility and minimum-size result for its first-shell compression. The closely related verified trigonometric tensor-product RKHS result is a lower bound in a different norm and does not decide attainment or the atom cone for this subball. The nearest distinct indexed hit solves a different finite Fourier reweighting problem. This is not priority certification for the underlying spectral lower bound or the trigonometric quadrature framework.

## value

PASS

This separates a natural rank relaxation of deterministic quadrature from actual sampling, and locates the exact first failure while allowing signed weights, adaptivity and nonlinear output. The positive-atom threshold independently quantifies what the cube forbids even with unrestricted positive node count. The positive-rank compactness argument supplies a useful way to distinguish strict loss from unattained infima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
