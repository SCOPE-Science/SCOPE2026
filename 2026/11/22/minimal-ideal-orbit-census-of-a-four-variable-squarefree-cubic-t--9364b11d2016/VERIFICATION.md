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

The six mixed monomials span the socle: a nonzero constant or linear term is detected by multiplication by a suitable generator. A minimal ideal is killed by the nilpotent maximal ideal, so precisely the socle lines qualify. Quadratic corrections to generator images act trivially on their products. In characteristic two every invertible linear substitution is allowed; the induced exterior square has the two nonzero alternating ranks 2 and 4, transitive within each rank even on projectivization. In odd characteristic the vanishing squares force monomial substitutions and exactly vertex-product scalings on edge weights. Forest weights can be normalized along rooted trees; on a triangle, the projective scalar absorbs the needed product quotient, and a pendant edge can then be normalized at its leaf. For a 4-cycle or K₄−e, the alternating product ratio is invariant and complete: normalize three cycle edges, then the ratio fixes the fourth. In K₄−e the residual scales on alternate vertices together with the projective scalar can normalize the diagonal by an arbitrary factor, not just a square: take scales x on one diagonal's two ends, y on the other shore, and scalar 1/(xy), giving diagonal multiplier x/y. The graph symmetries realize ratio inversion, with the two fixed values ±1. In full support the triple of opposite-edge products is complete: for ratios d_ij with d₁₂d₃₄=d₁₃d₂₄=d₁₄d₂₃, set t₁=1, s=d₁₂d₁₃/d₂₃, t_j=d₁j/s to solve d_ij=s t_i t_j. Permutations induce S₃ on this projective torus. The identity fixes (q−1)² triples, each transposition q−1, each 3-cycle gcd(3,q−1). Summing the resulting strata gives exactly the displayed total. Independent replay at q=3 normalized nonzero six-tuples by their first nonzero entry and built orbit components under all 24 permutations and 16 diagonal choices. All 364 lines were covered, giving 13 orbits with strata 1,2,3,3,2,2, including two full-support orbits.

## originality

PASS

The characteristic-two alternating-rank classification and general socle or automorphism tools are established. The supported distinction is the complete finite-field projective-socle orbit invariant for this fixed algebra, particularly the odd-field weighted support strata and the combined torus-symmetry quotient. Neither the inspected algebraic results nor the closest indexed weighted-graph or ideal-orbit analogues states or implies the complete count under this action.

## value

PASS

Minimal ideals are the simplest embedded nontrivial ideals of this natural small monomial algebra. The complete action quotient distinguishes finite fields with the same algebra presentation much more sharply than the ambient number of socle lines: two rank types in characteristic two versus quadratic growth in odd characteristic, with explicit invariants for testing equivalence. The useful part is a classification of all the odd-field strata, not a small-field census or the known alternating rank calculation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
