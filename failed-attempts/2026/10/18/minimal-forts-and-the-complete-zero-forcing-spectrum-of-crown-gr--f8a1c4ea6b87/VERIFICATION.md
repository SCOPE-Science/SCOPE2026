---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a fort with index sets X,Y, outside A_i sees |Y|−1_{i∈Y} and outside B_j sees |X|−1_{j∈X}. Every pure triple is a fort, so a minimal fort with at least three from a shore is such a triple. With at most two from each shore, |Y|=2 forces Y⊆X, and the symmetric statement forces equality of both two-element index sets; these aligned four-sets are forts. With at most one per shore and nonempty support, a vertex on the opposite shore with index outside both sets sees one neighbor, because n≥3. This proves the list and minimality. An untouched fort prevents complete forcing; a process that stalls with a nonempty white set leaves a fort. Thus only complements with at most two omissions per shore and no identical pair of pairs are allowed. Counting those complements and subtracting the identical-pair cases gives all five coefficients and the minimum multiplicity. Inclusion-minimal forts correspond to maximal failed sets by complement, yielding both counts. Uniform 1/3 is feasible and summing all triple inequalities gives n/3 per shore as a lower bound. At equality all triple inequalities are tight, and any two distinct weights on a shore enter triples with a shared pair of other vertices when n≥4; subtraction gives uniqueness. The size upper bound on packing is attained by disjoint pure triples on each shore and, when n leaves two indices modulo three, a matched four-set. This gives the packing formula and the stated integral/fractional ratio. The frozen script and recorded output were inspected, not executed; they provide finite forcing, fort and packing checks but not independent fractional optimization.

## originality

FAIL

The distinct 2026/10/13 Resultary Finding gives exactly the all-sets forcing criterion and its complete polynomial on n≥3. Inclusion-minimal forbidden white sets are the pure triples and aligned four-sets; the established fort-transversal correspondence therefore already determines the entire stated minimal-fort hypergraph and maximal failed sets. The prior scalar is also explicit in Benson et al.'s product theorem. The remaining fractional value and its uniqueness reduce to summing and subtracting the covered pure-triple constraints; the packing value reduces to the minimum-size bound and grouping three indices at a time, with the covered aligned four-set for the two-index remainder. A later exact catalogue match explicitly states both scalar optima as well. It is not needed to infer priority, and it does not state uniqueness. No nonmechanical, independently valuable residual claim is established by these routine deductions.

## value

PASS

The full obstruction family and all-cardinality zero-forcing polynomial for a canonical bipartite family are useful for understanding forcing feasibility beyond the minimum cardinality. The packing and fractional calculations illustrate their optimization consequences. As a proposed repair after coverage of the structural result, those elementary scalar and equality calculations alone do not establish a distinct valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
