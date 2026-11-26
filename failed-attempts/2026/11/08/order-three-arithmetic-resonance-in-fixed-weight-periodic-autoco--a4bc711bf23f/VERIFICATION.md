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

The shift graph is a union of simple cycles of length N/gcd(N,d); its triangle count T is N/3 exactly at the allowed shift d=N/3 and zero otherwise. Independently, orient the edges by +d and count 0→1 transitions X, so A_d=k-X even on monochromatic components. No two adjacent directed edges can both be starts. For j=1,2,3 the j-th falling moment of X is the number of ordered j-edge matchings times a_j=(k)_j(N-k)_j/(N)_{2j}, which is the probability of the specified j occupied and j empty sites. The matching counts are N, N(N-3), and N(N-4)(N-5)-6T: the last follows by inclusion-exclusion on the three adjacencies in a triple, with a triangle counted by the all-three intersection. Substitution into the centered moments gives the displayed mean, variance, baseline and +6Ta_3 correction (the third moment changes sign under A_d=k-X). The endpoint weights give a vanishing correction exactly as stated, and substitution at k=N/2 yields the opposite-sign formulas and the N=6 values. A fresh transfer-polynomial enumeration corroborates the formulas independent of the frozen edge-census code.

## originality

FAIL

Chen and Zhang's 2014 arXiv v3 / 2015 publication contains the exact general fixed-graph permutation-null third moment of the cut count (Lemma 3.8). A fixed split is exactly uniform sampling of a k-subset. On the simple 2-regular shift graph the cut count equals 2k-2A_d, and specialization of their local counts gives the full formula including the triangle correction. The prior paper does not state the periodic interpretation; the arithmetic classification and balanced sign comparison follow directly on substituting the cycle length and half weight. This is verified implication, not a verdict based on missing literature.

## value

FAIL

The fixed-weight cyclic statistic and its skewness contrast are natural, but the exact invariant is a degree-two specialization of the prior general formula, and the only remaining cyclic interpretation uses the elementary order of one shift. The balanced sign contrast is then a substitution. These may be useful expository consequences, but no independent worthwhile mathematical gap remains in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
