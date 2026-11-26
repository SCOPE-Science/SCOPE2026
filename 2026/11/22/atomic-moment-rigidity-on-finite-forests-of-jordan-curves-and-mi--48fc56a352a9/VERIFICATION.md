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

For distinct sites, the absolutely summable family gives a finite complex atomic measure. Disjoint Jordan boundaries make their filled disks either disjoint or strictly nested; the finite union of maximal filled disks has connected complement. Mergelyan therefore isolates a component by piecewise constants, and multiplying by z^k preserves the restriction's zero moments. For one disk, interior harmonic measures are pushforwards of Poisson measures under a Carathéodory homeomorphism, hence absolutely continuous to one fixed nonatomic harmonic measure. Their weighted sum converges in total variation by the ℓ¹ hypothesis, with exactly the interior polynomial moments. The modified boundary measure annihilates all polynomials; Mergelyan applied to powers of the inverse conformal map transfers its annihilation to the circle, where F. and M. Riesz gives absolute continuity. The original atomic boundary part is thus zero; the inner measure still annihilates polynomials. Finite descent removes every layer. A separate direct check of the crucial elimination uses a peak function g=(1+conjugate(alpha) phi^{-1})/2, where alpha maps to the chosen atom: g=1 at that atom and |g|<1 everywhere else in the disk. Each g^n integrates to zero by Mergelyan, and dominated convergence gives zero mass at the atom, even for dense sites. Finally distinct diagonal entries force every commuting off-diagonal matrix entry to vanish. Every ℓ¹ test sequence factors as x_n conjugate(y_n) for ℓ² vectors, so WOT on diagonals is precisely the pairing with ℓ¹; its zero preannihilator yields the claimed WOT closure. No computation is required.

## originality

PASS

The abstract moment equivalence, single-boundary result, convergent interior-sequence case, and even countably many concentric circles are already covered. The supported distinction is an arbitrary finite forest of pairwise disjoint Jordan boundaries, in particular deeply nested nonconcentric loops with unrestricted dense sites. There is no common conformal flattening or norm separation in the identified criteria; the geometric step that makes the known elimination principle recur on arbitrary branches supplies this distinct case.

## value

PASS

The theorem gives a concrete, unrestricted spectral-geometry condition for infinitely many distinct eigenvalues. Finite nesting is the important regime: usual uniform polynomial isolation fails across full nested curves, yet atomic ℓ¹ rigidity still holds after removing their outer layers. This supplies a reusable criterion for nonconcentric, nonsmooth and densely occupied families, rather than just another example on a circle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
