---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

PASS. For any subgroup H≤S_n of the natural label action on μ_ell(K_n), a geometric fixed point has barycentric weights constant on each H-orbit. The simplicial orbit model retains precisely independent vertex orbits (nonsingleton orbits are absent from top clique level). Its graph Q has complete consecutive-level joins except equal singleton labels, with the apex adjacent to level zero. When f≥1, each nonsingleton-orbit vertex at level j<ell is dominated in Ind(Q) by a fixed singleton label at that level: the latter has subset open neighborhood and is nonadjacent to it. Repeated valid strong collapses leave μ_ell(K_f). If f=0, all admissible same-level orbit vertices have equal open neighborhoods and collapse to one representative per level, yielding P_{ell+1}. The standard path-independence recurrence and published ordinary generalized-Mycielski wedge formulas produce the three ell mod 3 regimes, including f=1 contractibility via isolated vertex. Original verify.py computes 168 orbit partition/level models, 462 domination deletions, 110 mod-two homology checks, independent adjacency formulas and no extrapolation. These finite tests corroborate the subgroup-universal structural proof.

## originality

PASS

PASS, best of knowledge. Carnero Bravo's 2026 theorem and Goyal–Shukla–Singh's 2019 formulas classify ordinary nonequivariant Ind(μ_ell(K_n)) and are explicitly used for final sphere counts; they do not imply the geometric H-fixed model for all subgroups. The Resultary symmetric-group homology theorem computes rational character as tensor powers of the standard representation, which records homological traces but cannot classify homotopy of subgroup-fixed point spaces. This orbit strong-collapse theorem depends on the number of labels fixed by the entire subgroup, not the number fixed by individual permutations. Potential unindexed genuine equivariant classification remains a risk.

## value

PASS

PASS. Full subgroup-geometric-fixed homotopy types form a natural invariant for S_n-actions; they are finer than ordinary spaces and rational equivariant homology characters. The proof gives a robust all-ell and all-subgroup model reduction to a path when f=0 and to a smaller Mycielskian when f≥1, making a surprising fixed-label-only dependence explicit and potentially reusable for equivariant questions. Not merely substitution into ordinary wedge formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
