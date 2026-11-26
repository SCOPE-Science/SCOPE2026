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

A specified unordered consecutive-label triple contracts to one object with six internal orders, giving 6/[n(n-1)]. At label offsets 1 and 2 the triple windows overlap in two and one positions; allocating shared labels to the overlap gives 4 and 8 orders of their union, respectively. Disjoint triples contract separately with 36 internal choices. Summing the resulting intersections gives O(n^(-2)), so Bonferroni yields P(E_n)=6/n+O(n^(-2)) and asymptotic uniqueness. Given a specified triple, the block order is uniform and independent of the contracted permutation; its successive differences give exactly the four stated marks. At most two original consecutive-value edges cross the block boundary, each requiring an outside label to neighbor the contracted block and hence having probability O(1/n) uniformly. Each feasible assignment of ell fixed directed singleton edges contracts to directed runs of the value paths, with probability 1/(n-2)_ell; contradictory choices, including both signs of the same edge, have probability zero. Disjoint-label ordered selections give n^ell+O(n^(ell-1)) choices, all overlapping selections O(n^(ell-1)). Each mixed factorial moment tends to 1 uniformly in the triple. Tightness and moment identification (the product Poisson law has exponential moments) give the asserted external joint limit, independent of the internal mark. Replacing the union indicator by the sum of marked indicators costs at most the pair intersection sum on bounded tests, or O(1/n) after conditioning. Adding the components gives the claimed shifted Poisson(2) law and fixed-k probabilities. The exact signed means have internal contribution 2/3, one contribution 1/(n-2) per external singleton edge and 1/[3(n-2)] per boundary edge. Independent positional-window enumeration over all 46,230 permutations for n=3, through 8 verified single and pair counts, all internal marks and both signed conditional means; replay: python3 /workspace/branches/reproduce_records_1_to_4.py. Frozen verification, source code and same-model review were inspected, not treated as independent evidence. The enumeration is only a finite check of the analytic proof.

## originality

PASS

Best-of-knowledge pass for the rare-event conditional joint law, not for ordinary adjacency limits, overlap enumeration or Poisson factorial-moment technique. The retrieved marginal results neither state nor determine the mark. The closest common-interval primary passage could not be independently retrieved; this leaves a specific priority risk, not a result about the whole paper.

## value

PASS

Selecting comparisons by a shared three-marker block changes the null law nontrivially: a particular direction-correlated mark cannot be approximated by reusing the unconditional Poisson(2) model. The joint law quantifies this selection effect for the natural uniform-permutation null model, with no claim about evolutionary sampling or a finite-size rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
