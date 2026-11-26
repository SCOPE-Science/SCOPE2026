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

For a singleton or pair of zeros the stated union criterion is exactly the existence of distinct adjacent defenders (Hall's conditions for sets of size at most two). With the center labeled 2 the only failure is two zeros with no petal defender, so at most one no-defender petal may contain a zero and it must have exactly one; this gives the A product and B correction. With center 1 or 0 the petal predicate is: every zero has a local defender and each petal with at least two zeros has at least two local defenders. Distinct petals have disjoint local resources. This gives C by subtracting the one-2 states with at least two zeros from A. With center 0 its own singleton attack and its pair with any peripheral zero further exclude exactly the all-ones periphery and the states with one 2 and one 0 in the same petal, all at weight M. This verifies every coefficient and, at z=1, the stated total count. The leading C terms for sizes 2 and 3 are 3z² and 7z³, respectively; for s>=4 its minimum possible degree is four. Comparing center regimes yields the stated minimum counts and their label patterns. At (q,s)=(2,3) exactly 36 center-zero permutations of (0,1,2) in both petals tie the 27 center-two minima. An independent small-graph check by enumerating disjoint zero and defender sets and explicit injective defenses produced minima (weight,count)=(4,4), (7,88), (6,63), and (6,16) for petal sizes (2,2), (2,3,2), (3,3), and (4,4).

## originality

PASS

The prior general two-attack extremal theorem already covers computation of the scalar minimum through a path-packing invariant and construction of a minimum labeling; the invariant or existence of an optimum is not credited as new. The distinguishable claim is the entire feasible weight distribution in heterogeneous bouquets and, in particular, the exact homogeneous census and exhaustive pattern classification, not merely the minimum value. The inspected prior Roman census and windmill polynomials count different feasible sets or only minimal labelings under another predicate.

## value

PASS

Clique bouquets are a natural cut-vertex family in which local defense choices interact through a single common resource. The heterogeneous polynomial quantifies that interaction for every weight, showing exactly how one undefended petal zero can be paid for at center label 2 or how a center attack imposes a global exclusion at label 0. The explicit optimizer multiplicities and the exceptional 36-way contribution under a different center regime are not supplied by a scalar minimum computation or an ordinary Roman count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
