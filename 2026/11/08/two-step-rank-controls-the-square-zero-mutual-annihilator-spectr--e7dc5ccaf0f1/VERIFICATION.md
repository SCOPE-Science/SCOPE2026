---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Set U=im A, K=ker A, D=U∩K, with dimensions r,n-r,δ=r-rank(A²). The product restrictions are exactly L=im B⊂K and H=ker B⊃U+L, with B induced by any isomorphism E/H→L. For rank b and intersection t, choose L by [δ choose t]_q[k-δ choose b-t]_q q^((δ-t)(b-t)), choose codimension-b H containing U+L by [k-b+t choose b]_q, then multiply by GL_b(q). This bijection proves the entire formula for any characteristic and similarity class. Existence condition 2b≤k+t≤k+δ gives b≤floor((n-rank(A²))/2), and feasible t=max(0,2b-k,b-(k-δ)) realizes every lower rank. Independent exhaustive F2 n=4 calculations verified contrasting A rank 2 examples: diagonal(1,1,0,0) gives B rank counts (1,3,0), two J2 blocks give (1,9,6); correctness is proved by subspace counting, not extrapolation.

## originality

PASS

Prior published square-zero mutually annihilating pair counts impose A²=0; the Nov2 all-tuple double-flag theorem also assumes every operator square-zero. Huang’s count for arbitrary A concerns all AB=BA=0, without B²=0 and without rank/overlap strata. Neither directly supplies the arbitrary-A conditional (r,rank A²) rigidity and complete (b,t) Gaussian formula. Special A²=0 / unconditional totals remain known background.

## value

PASS

The complete fibre count of square-zero mutual annihilators of an arbitrary fixed finite-field operator is a natural invariant of matrix-pair representation theory. Its dependence only on rank A and rank A² and the exact sharp rank threshold expose a structural two-step rigidity, including examples separating matrices of the same rank; these are useful precise finite-field counts, not a routine recomputation of an unrelated table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
