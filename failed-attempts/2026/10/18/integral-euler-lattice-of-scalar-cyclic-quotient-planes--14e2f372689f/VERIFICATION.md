---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For scalar weights, the source Euler coefficients specialize to Q=sum a_j^2−2 sum a_j a_(j+1)+sum a_j a_(j+2). Polarization gives 2I−2(S+S^−1)+S^2+S^−2, keeping both contributions when powers coincide. Multiplying by the invertible S^2 identifies the cokernel with Z[t]/(t^n−1,(t−1)^2(t^2+1)), presented by C^n−I in the monic degree-four companion basis. The replay (python3 replays/1_euler.py; output replays/1_euler.txt) checks C^4−I=2vw^T, CB=B, B^2=0, and computes constants and slopes for the specified minors of C^r−I+mB. They are affine exactly, since B has rank one, not a finite extrapolation. For r=0 the presentation has rank one and its sole invariant is 2m. For r=1,2,3 the rank is three by the polynomial gcd over Q. The primitive right and left nullvectors v,w have only sign entries, so all maximal minors have the magnitude of the checked principal minor; the selected unit 2-minor forces both smaller Smith divisors to be units. This gives torsion orders n, 2n, n/2 and free ranks 1,1,3 in the proposed regimes. For real inertia the Fourier eigenvalue is −8 sin²(theta/2) cos(theta). Negative eigenvalues correspond to 0<k<n/4 or 3n/4<k<n; positives correspond to n/4<k<3n/4. The counts are 2(ceil(n/4)−1) and ceil(3n/4)−floor(n/4)−1, respectively, giving every row of the frozen table. In particular n=3 and n=4 are semidefinite even when shifts coincide, and n>=5 is indefinite. This concerns the stated polar normalization and neither the half-Hessian nor geometric torsion classes.

## originality

FAIL

The exact integral cokernel is a direct specialization of another indexed theorem. The accessible general abelian radical result also gives the signed Fourier factorization on the entire character lattice: its proof specializes to a sign test on one cosine, whose strict-quarter count is precisely the frozen all-order inertia table. Thus composite orders are not an uncovered substantive remainder merely because their inertia counts are not tabulated verbatim. An additional indexed result explicitly covers the odd-prime inertia. These are distinct same-date records; the overlap establishes coverage, not within-day priority or provenance.

## value

FAIL

The polar lattice is a natural invariant and the proof is correct. Against the checked coverage, however, the full Smith invariant is already a parameter substitution, and the only apparently untabulated component (composite-order scalar inertia) is a direct substitution and elementary interval count from the known signed spectrum. The frozen result does not derive any separate new invariant or application from this combination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
