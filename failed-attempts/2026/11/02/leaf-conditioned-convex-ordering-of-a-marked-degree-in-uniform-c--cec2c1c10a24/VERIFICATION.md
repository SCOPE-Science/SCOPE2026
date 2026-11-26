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

In the uniform Prüfer word of length m=n−2, L=k fixes q=n−k distinct labels, and J=D−1 is the marked multiplicity. There are binom(n,q) q! S(m,q) such words; fixing j>0 marked positions leaves S(m−j,q−1) possible fiber partitions before choosing and labeling the q−1 remaining symbols. This gives (1), including j=m and the star, and exchangeability yields the claimed atom at zero and constant mean. The Stirling recurrence gives B_{N+1}=z(B_N+B_N'). The logarithmic-derivative expression 1+B_N'/B_N decreases on each pole interval, with one crossing between successive poles and one to the left; at the right of the last pole it is positive. The poles are simple and B_N+B_N' does not vanish at them, so the induction gives real-rooted rows. Row log concavity, for A=S(N,t−1), B=S(N,t−2), C=S(N,t), gives BC≤A²<AC+A², the exact comparison needed for the strict Stirling ratio lemma. Therefore the adjacent positive-cell ratios increase on their common support, growing the right endpoint; these ratios multiply for non-star comparisons and the star is immediate from its positive count m. Because zero gains mass, some positive cell loses mass, while the larger right endpoint gains mass. Thus the positive-cell differences have one weak negative-to-positive transition. The tail differences H_t are negative at t=1, positive at t=k, and cannot return to negative: H_t first weakly increases while the cell differences are nonpositive and then decreases to zero through nonnegative values. Their sum is zero by the mean. The stop-loss gaps for r≥1 are nonnegative: either the prefix through r is nonpositive and contains H_1<0, or the suffix is nonnegative. For r≤ell−2, in the second case the suffix contains the strictly positive tail difference at ell−1. This gives strict convex order by the discrete hinge representation. Merging two Prüfer positions gives the stated factorial-moment and variance expressions; constant mean and increasing second moment imply the covariance claims. I inspected the finite verifier without using it as evidence for the unbounded n result. Both one-crossing formulations hold in the specified family; the word 'equivalently' should not be read as a converse for arbitrary mass functions.

## originality

FAIL

An earlier distinct Resultary record, 21ba647f27d9, explicitly states the strict adjacent convex order for the same model and every admissible adjacent pair, and gives the same conditional law and variance. Its size-biased likelihood-ratio result directly implies the added weak tail crossing. The date is not needed for the finding of equivalent coverage or a claim of historical priority.

## value

FAIL

The marked-degree ordering at fixed mean is a worthwhile structural theorem in its original setting, but is already obtained from a prior likelihood-ratio comparison of the same positive cells. Here the added weak tail description and generalized covariances are immediate reorganizations of those ratios, endpoints and moments, not an independently valuable surviving extension. No repair is justified by rephrasing the covered theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
