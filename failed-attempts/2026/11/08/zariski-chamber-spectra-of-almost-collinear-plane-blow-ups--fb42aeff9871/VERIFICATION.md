---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Bézout against the common and joining lines bounds the collinear multiplicities by d-m_* individually and d in sum. This gives C²≥m_*(d-m_*)≥0 for every unlisted nonexceptional irreducible curve. The incidence matrix forbids intersecting (-1)-pairs, and its Schur complement with R is -(n-1)+k, so k≤n-2 exactly. The four choices for the inclusion of R and E_* give the stated polynomial and its top coefficient. Any negative-definite support is realized: solve (-M)a=(A·C_i) for an ample A. The signs of the off-diagonals of -M and positive definiteness imply a≥0 (pair with the negative part of a). Then P=A+Σa_i C_i is big and nef, orthogonal to the support, and P+ΣC_i has precisely that negative part. An independent exact lattice-class enumeration by integral congruence elimination reproduced all reported profiles for n=3,4,5 and gave n=6 profile (1,14,79,241,435,467,271,58), total 1566. These finite tests are not the all-n argument.

## originality

FAIL

The distinct indexed two-transverse-block record supplies the exact formula mechanically, not just the standard chamber algorithm. Its stated range is n,m≥3, so m=1 is not literally covered by its theorem statement. However, add two new points on a line through the off-line center, with intersection with the original line unblown. In the resulting (n,3) blow-up, the strict transform of any original negative curve stays negative, so Step 1 of the two-block result exhausts its possibilities. The added block-line and cross-lines using the two new labels have square zero after descent, and the new exceptional curves contract. All remaining negative-curve classes and pairings are unchanged when pushed down. In the indexed two-block formula delete its B terms (v=0) and keep just the one retained column for its cross-stars and one retained F label: this is exactly its footprint expression with m=1. The empty cross-family contributes (1+t)^{n+1}+t(1+t)B_{n,n-2}(t); selection of r≥1 surviving cross-lines contributes binom(n,r)t^r[(1+t)^{n-r}+t B_{n-r,n-2}(t)]. Summing gives the frozen polynomial by the binomial theorem. The explicit total and top coefficient of the two-block record also specialize algebraically to the claimed values at m=1. This is demonstrable content coverage by reduction and specialization of the indexed enumeration, not a claim about which same-date record was first.

## value

FAIL

The rank-refined counts are natural and the all-n proof is sound. Under the exact-invariant standard the frozen contribution does not add a surviving unknown invariant once the explicit indexed two-block footprint formula is specialized to the retained column. A different proof of the same resulting coefficients and more finite checks do not remove that mechanical implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
