---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a fixed zero-vector set, a nonzero vector has q+1 possible projective directions and q−1 lifts of its chosen direction. Zero determinants identify directions on surviving endpoints, and nonzero determinants separate them; this proves the contraction count, including the zero contribution of loops. Vertex scalings attain arbitrary edge ratios on a proper support (a forest). On full odd support the sole closure condition for scalings is a square class, removed by a simultaneous GL(2,k) map with chosen determinant; in characteristic two squaring is already bijective. Therefore the division by (q−1)^|S| is exact. With at least two active edges the no-deletion quotient is an edge or cycle and is 3-colorable; with one active edge delete a vertex outside its endpoints; empty support admits the zero assignment. Full support gives the cycle coloring count q^n−q, with q^(2n) free central choices. The group assertion follows for the edge cocycle f(a,b)_i=a_i b_(i+1): its commutator is f(a,b)−f(b,a), even in characteristic two, with no use of a half-bracket. Inspected the frozen checker and seven recorded outputs without executing the uploaded code. An independent transfer count (`python3 /workspace/independent_checks.py 5`) compared every target with the support formula on the seven frozen sizes and on (3,4) and (5,4) over F4, including all 1,024 targets at (5,4). Computation is bounded corroboration only.

## originality

FAIL

The all-target support-only fiber census is already a direct consequence of the earlier pointwise alternating-rank theorem for odd unicyclic graphs and additive-character orthogonality. A distinct same-day broader record also explicitly gives the exact fibers in matching-sum form on all graphs without even cycles, including all odd cycles and every characteristic. Its related-work passage calls the single-cycle result earlier, but neither the same date nor that unlinked phrase establishes priority; the independent November 2 implication is sufficient. The positive chromatic expression is a different derivation/presentation and the elementary surjectivity argument is useful, but they do not establish novelty of the advertised complete support-only classification and its full-support count.

## value

PASS

Prescribed commutator counts and surjectivity on a natural nonacyclic family give more information than a commuting probability or a count of conjugacy classes. The nonnegative chromatic expression gives a direct combinatorial account and witnesses positivity on this family, unlike an alternating matching sum in which positivity is not manifest. This scientific usefulness does not remove the exact coverage of the advertised census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
