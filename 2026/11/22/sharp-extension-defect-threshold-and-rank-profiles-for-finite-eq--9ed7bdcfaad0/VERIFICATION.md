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

A partial isomorphism pairs nonempty selected intersections of original blocks of equal selected size, and extends exactly when each pair also agrees in original capacity: then complete the partial bijections and match unused blocks by capacity. An unequal-capacity pair needs at least δ omissions on its larger side. At n−δ equality forces the larger block of size t=s+δ to be cut to s, with no other omissions on that side. The other side has the same selected profile and hence an excess block of size s; creating it from a larger block also costs at least δ, forcing a single truncation from t to s on that side too. Distinct nearest pairs give disjoint profiles. For each pair the ordered domain/image choices number m_t² binom(t,δ)², and for each such choice there are g(m_s+1)s!/(m_t t!) isomorphisms. Exactly 1/(m_s+1) match the two truncated blocks and extend, giving the frozen count when summed over pairs. For A_E, D_α counts subsets of each selected-size profile; each ordered pair of such subsets contributes ∏_j a_j!(j!)^{a_j}. For R_E repeat independently within each original capacity s; each subset count is m_s!∏_{j≥1}binom(s,j)^{a_j}/∏_{j≥0}a_j!, and pairing only nonempty intersections cancels one factor a_j! for j≥1, leaving (a_0!)² as in the formula. This includes the empty map and all equal-capacity hosts. The example (1,3) gives 9 bad maps at rank 2, the largest bad rank, not the first in ascending order. Independent enumeration through n=7 compared both polynomials against direct partial injections and distinct restrictions of actual full automorphisms for 45 partition types, including the empty host.

## originality

PASS

Both the homogeneous case and the complete profile and cutoff for two unequal classes have exact counterparts in indexed results. The supported distinct claim is for arbitrary mixed capacities and multiplicities, especially the exact first defective stratum summing over all nearest capacity pairs with the omission rigidity needed to count it. Generic profile counting and the equal-capacity factors are not assigned novelty in isolation.

## value

PASS

The nearest gap identifies the exact robustness of host-level extension under omission, and the coefficient distinguishes how often extension first fails among nearly complete partial symmetries. Knowing only homogeneous behavior, two-class examples or that some low-rank map fails does not give that near-total census when the host has multiple capacities and repeated closest gaps. The coupled profiles give an exact way to compare all partial symmetries to the restrictions of global ones.

The dated certificate retains the supplied scientific assessment, sources and limitations.
