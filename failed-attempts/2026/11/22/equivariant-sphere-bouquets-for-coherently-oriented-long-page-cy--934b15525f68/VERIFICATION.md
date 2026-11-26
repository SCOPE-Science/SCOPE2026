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

A face uses at most one arc of each branch type, and the only resulting directed cycles use both arcs of a single branch and the whole return path R. Thus the book complex X is the join K_(n,n)*Δ_R with precisely the n diagonal facets removed but their boundaries retained. The join is contractible and its pair with X has relative integral cells only in degree d=ℓ−1, one per removed facet. The connecting map gives the oriented missing-cell boundaries as an integral basis. Ordering every removed facet as (p_i,q_i,R) gives the unsigned permutation lattice. Attaching only d≥3 cells to X neither joins components nor changes π₁, so X is connected and simply connected; the map from the abstract wedge of boundaries based at one common return vertex induces a homology isomorphism, hence a homotopy equivalence. A setwise stabilizer cannot permute the vertices of a face nontrivially because there is at most one p and one q and all return arcs are fixed. The fixed-space calculation therefore restricts to the f_H fixed branches, or to a nonempty simplex for f_H=0. The wedge map restricts to the same homotopy equivalence there, so equivariant Whitehead applies. Its quotients are the asserted wedges indexed by branch orbits, and naturality of the relative generators under branch addition gives the primitive split inclusion. This checks the theorem, not merely the finite mod-two calculations.

## originality

FAIL

The principal theorem is a suspension corollary of the previously classified equivariant triangular book, not a mathematically independent family after reparameterizing the return path. The decisive evidence is an exact, natural equivariant PL reduction, not a shared date or a merely plausible literature match. If r is a return arc and D and L are its deletion and link, splitting r into two consecutive arcs r1,r2 gives (∂Δ¹*D) ∪ (Δ¹*L): if zero or one replacement arc is selected, the other original arcs may form any face of D, because neither endpoint competes with another arc in the relevant direction and one half cannot complete a directed cycle through the fresh vertex. Selecting both halves has exactly the old test for a face containing r. Stellar-subdividing the replacement edge at its midpoint r gives (∂Δ¹*D) ∪ (∂Δ¹*{r}*L) = ∂Δ¹*X_old, the suspension with both suspension vertices fixed. This identity is independent of any calculation for long books, commutes with all branch permutations and branch inclusions, and restricts facewise to the missing-cycle boundaries. Iteration transfers the earlier equivariant wedge and its fixed/quotient counts, with the cycle basis and coordinate inclusion transferred from the relative missing triangles. No separate earlier statement explicitly printing the ℓ≥4 formula is required for this implication.

## value

FAIL

The book construction is natural and the direct proof is correct, but within the stated scope lengthening the common directed arc only suspends a known equivariant example; it changes no branch action or incidence relevant to the claimed invariants. The fixed and quotient formulas and the inclusion are routine transfers under the same natural suspension. A proof of a substantially broader subdivision or book-classification theorem could be useful, but that is not the frozen result and is not submitted as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
