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

For labelled K_(n,n) with n>=2, expanding det(L+diag(z)) in the diagonal variables yields the prescribed-root principal minors, so substituting each Walsh sign gives the unnormalized multiplier with root-choice multiplicities intact. The positive signed diagonal entries n±1 make Schur complementation legitimate, and the all-ones cross blocks give exactly the product of reciprocal sums in the multiplier. For the zeros, Q=n^2-1, u=2p-(n-1), v=2q-(n-1) give (Q+u)(Q+v)=Q^2 with both factors positive. If u,v are on the same side of zero, monotonicity of the product forces both zero. If opposite in sign, |uv|<=Q, while a nonzero even u+v would give |Q(u+v)|>=2Q; setting u+v=0 then also forces uv=0. The stated class exists precisely for odd n>=3 and its Walsh multiplicity is the claimed squared binomial. Rank, degree n-1 and the Stirling limit follow. Every absolute multiplier is at most the positive coefficient sum, attained at the trivial character; the Laplacian spectrum gives the stated sum. Independently, exact signed determinants agreed for all 135 shore classes at 2<=n<=6. A separate direct combinatorial check enumerated, for each vertex, either no parent or a parent on the opposite shore, rejected directed cycles, tallied root masks and summed their Walsh signs. For n=1,2,3,4 it found trivial multipliers 3,45,1792,140625 and nullities 0,0,9,0, with only class (1,1) vanishing in that range. The excluded n=1 spectrum is 3,-1,-1,-1, so excluding it is necessary. Neither replay is an all-n proof; the submitted program was not executed.

## originality

FAIL

A distinct Resultary record, 7a0c1bc2e70a, states the identical balanced formula, unique zero pair, parity-dependent rank and nullity, and the same asymptotic nullity, within a stronger complete-bipartite result. This is demonstrable catalogue coverage, not an assertion of which same-day record was first. The first lost Walsh degree and maximal absolute coefficient are immediate consequences of the covered spectrum and positivity, and are not a surviving original central claim.

## value

FAIL

The exact Walsh loss for this naturally weighted root-set kernel is useful, but the frozen balanced-only result is fully covered by the stronger exact bipartite classification. Its low-degree survival and largest multiplier add only mechanical consequences; no distinct valuable claim remains to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
