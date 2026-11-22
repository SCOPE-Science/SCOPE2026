---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

A tau-invariant collision-free unordered configuration is a disjoint union of an occupied subset T of m fixed midpoints and b free 2-orbits, each uniquely represented by one particle on the A-side open m-star, with a+2b=k. Midpoint occupancy is locally constant in the invariant collision-free locus, giving an actual clopen disjoint-union homeomorphism rather than just equality of Euler characteristics. Strictly increasing branchwise deformation identifies half-open and closed-star configuration homotopy types. Farley–Sabalka radial-tree Morse result bounds UConf_b(star) by a graph with free fundamental group. Standard subdivision and matching-polynomial Euler calculations yield chi_b=C(b+m-1,m-1)-(m-1)C(b+m-2,m-1); hence R_m(b)=1-chi_b. Binomial choices of T and b=(k-a)/2 give integral torsion-free Betti sums and generating functions. Separate arithmetic tested R_m(b)>=0 and R_m(b)>0 iff b>=2 for 3<=m<=8, 0<=b<=11. The first fixed-space nonzero H1 is therefore k=4, for all m>=3. No finite test replaces exact orbit-sector homeomorphism.

## originality

PASS

Farley–Sabalka already determine ordinary radial-tree/star graph-braid ranks, so that factor is prior. Published two-point theta pole-swap studies determine automorphism characters on ambient H1, not the pointwise-fixed subspace of UConf_k for all k. A published all-particle fixed-space theorem for arm-permutation subgroups of a STAR has different underlying graph and symmetry; it does not cover reversal of a two-pole THETA. The audited all-k canonical midpoint-sector homeomorphism plus integral homology generating functions is a new combined fixed-point classification in inspected sources; elementary orbit bookkeeping is acknowledged.

## value

PASS

Geometric fixed loci under graph involutions are natural equivariant topological objects and can differ drastically from invariant homology of the ambient configuration space. The complete classification for every particle number and every arm count, including exact connected components, all integral Betti ranks, and first-loop threshold at k=4, is independently useful in graph braids and symmetric collision-free motion planning. No new ordinary-star rank is claimed; the value is the exact fixed-locus identification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
