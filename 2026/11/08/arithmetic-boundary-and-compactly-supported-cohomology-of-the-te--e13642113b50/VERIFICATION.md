---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The Fermat branch quartic in char3 is Hermitian over F9: 28 isotropic points have 28 hyperflex tangents, each lifts to two (-1)-curves by tangent restriction to a square t^4; these exhaust 56. The 63 anisotropic base points are incident to exactly four tangents, and each has two preimages, giving 126 ordinary fourfold crossings; each of 28 ramification points is a two-branch tangency. The four F3-rational tangent lines have nonsquare split coefficient 2, exchanging their exceptional components under Frob, while other tangents are nonrational. All singular supports are F9-rational, so D(F3^m)=10 at odd m; F9 incidence inclusion-exclusion gives 56(q+1)-3*126-28=56q-350 when m is even. Known Picard rank8 with Frob involution of trace0 yields #X=q²+1 odd, q²+8q+1 even, hence #U=q²-9 odd and (q-9)(q-39) even. The normalization exact sequence gives H¹(D) dimension (28+3*126)-56+1=351, Frobenius trace -9 from #D(F3), giving weight-zero Hc² eigen 1^171,(-1)^180. The injection H²(X)->H²(D) follows from nondegenerate Picard pairing and exceptional span; quotient has Hc³ eigen 3^24,(-3)^24; Hc⁴ eigen 9. Cohomological determinant and adjunction give displayed zeta and p_a(D)=757. Independent exact F9 enumeration reproduced 91 plane points, 28 tangent base points, 63 four-tangent points and four rational branch tangents; finite checks do not prove all extensions.

## originality

PASS

Knecht–Reyes 2015 already establishes this same Fermat double plane over F9, all 28 hyperflexes, nine generalized Eckardt points per bitangent and fullness. A more decisive November 2 2026 published SCOPE theorem, *Four orthogonal Frobenius reflections on the characteristic-three Fermat double plane*, was read in full and ALREADY proves on the exact F3 surface that all exceptional curves form 28 transpositions, none descends individually, the Picard eigenvalues ±1 each four times, and #X over every extension. Those are expressly NOT novel. The assessed additional result is the complete *reduced boundary D and open U* Frobenius cohomology and zeta, including singular normalization, odd-degree stabilization, and precise Hc degree-by-degree weights, which neither earlier text states. Both known inputs make these consequences accessible via standard methods and priority risk is substantial: if a stronger theorem or ready table computes the full open complement, O would fail. On actual searched material, the full mixed-weight cohomology computation and boundary arithmetic are not presented, so best-of-knowledge PASS is limited to this exact surviving contribution rather than the original claims of novelty for component descent.

## value

PASS

The union of all exceptional curves is a distinguished canonical divisor on this rational surface; its complete open-complement Hasse–Weil zeta and compact-support Frobenius decomposition are natural exact arithmetic invariants, not an arbitrary one-off count. Although geometry and surface Frobenius are known, organizing the arithmetic branch-incidence and localization into all extension counts and mixed-weight open cohomology is a nontrivial, self-contained exact calculation of a natural object. Reusing prior component-descent and 28-hyperflex facts is explicitly credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
