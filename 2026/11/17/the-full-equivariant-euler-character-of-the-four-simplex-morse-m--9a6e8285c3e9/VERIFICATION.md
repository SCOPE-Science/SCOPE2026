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

The four-simplex Δ^4 has 31 nonempty Hasse nodes and 75 primitive cover edges. For g in S5 an invariant matching is exactly a union of primitive-edge orbits. For o selected orbits the signed augmented reduced trace contribution is (-1)^(o-1), including -1 for the empty union, giving chi_E(g)=-P_g(-1). A legal face has no repeated Hasse nodes and no directed closed Forman V-path. I independently implemented an exhaustive C++ DFS over all orbit subsets with exact incidence, overlap and directed-cycle pruning. Its six nonidentity class counts, including empty, were 449440,10480,1029,1,32,3, and signed reduced Lefschetz traces -16,0,-1,-1,0,1 in the stated cycle-type order. Scoville §5.2 provides the exact full f-vector and identity reduced Euler characteristic 212456. S5 character arithmetic gives seven integral virtual Specht coefficients 1769,7079,8851,10623,8854,7084,1772 and 1769 full quotient reduced Euler characteristic. These are *virtual alternating* homology coefficients, not actual degreewise Betti numbers; the unknown graded homology is not inferred.

## originality

PASS

PASS best-of-knowledge: Scoville computed ordinary f-vector/identity Euler characteristic, explicitly not full homology or S5 signed traces; Lin–Scoville computed action/automorphism existence but not its virtual character. Published tetrahedral four-label S4 character and four-simplex optimal-facet stabilizer census do not supply all-face five-label signed Lefschetz sums. The exact nonidentity character remains distinct in inspected literature.

## value

PASS

PASS: the full S5 equivariant virtual Euler character of a natural but prohibitively large full discrete-Morse matching complex is a meaningful exact finite classification; its 1769 quotient reduced Euler characteristic and 7 Specht multiplicities capture symmetry information absent from raw face counts. This exact invariant is useful even while graded integral homology remains unknown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
