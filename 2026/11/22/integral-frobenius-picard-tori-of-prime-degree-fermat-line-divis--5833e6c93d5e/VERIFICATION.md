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

Use the families A: x1=-ζ^a x0, x3=-ζ^b x2; B: x2=-ζ^c x0, x3=-ζ^e x1; C: x3=-ζ^f x0, x2=-ζ^g x1. Each family gives two ℓ-point strata at x0=0 or the other free coordinate zero, and ℓ branches at each point. Cross-family intersections have all coordinates nonzero; their sign patterns after setting x0=1 distinguish AB, AC and BC because μ_ℓ and −μ_ℓ are disjoint. For AB the condition is b+c=e+a, giving ℓ³ points; permutations of coordinates handle the other two pairs. Distinct incident projective lines give distinct tangent directions on the smooth surface. Thus the ordinary point and genus counts follow, and the incidence graph is connected. Prime ℓ implies every nonzero label tuple has period d; for d>1 the all-zero labels give a fixed hexagon with six fixed leaves. In the rooted orbit quotient, a tree edge going to a new free orbit lifts to d edges with d distinct new endpoints; inductively this gives an invariant tree. The oriented off-tree edge basis is therefore an integral permutation basis, with one fixed edge and R/d free orbits, not just a rational character calculation. For d=1 all labels are fixed. In the normalization units sequence the scalars give the graph torus and the conductor principal units give the unipotent kernel; distinct smooth branches give conductor exponent ℓ−1 at the multiple points (product of the other branch equations), and 1 at nodes. Since ℓ−1<p, finite logarithm on the conductor quotients turns principal units into a quotient of vector spaces, compatibly with descent. Its dimension is Σ(δ−m+1)=6ℓ binom(ℓ−1,2). The normalization has no abelian contribution; Lang plus the finite abelian p-primary decomposition gives the claimed point group. The δ formula gives the displayed genus and the degree-five checks agree. The source finite checks illustrate the construction; the proof covers all admissible degrees and Frobenius orders.

## originality

PASS

The exact integral character lattice of the odd-prime Fermat surface line divisor for all Frobenius orders is distinct from the inspected geometry, zeta, surface Picard, even-quartic and plane Ceva results. Credit the pre-existing incidence geometry and the analogous integral method; this pass is not a claim of global priority.

## value

PASS

A complete arithmetic isomorphism classification, not just a dimension or trace computation, for the natural singular boundary formed by the standard Fermat lines. It distinguishes actual tori via integral Frobenius and yields exact Picard rational-point groups at every possible order; the invariant-tree argument explains why the integral classification takes this form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
