---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For the two nonaligned corners, incidence degree sums count the crossed landmarks twice even though each contributes zero; subtracting twice their indicators yields the exact separation. Positive degrees and no single-edge component suffice, since two occupied cross corners are disjoint edges whose endpoint sums are each at least three. At s=ceil(2N/3)≤2n−3, an empty row or column would require at least 2n−2 landmarks. A K₂ component forces all other components to have order ≥4 by applying the nonaligned test with its edge and any other edge. This gives ≥(3N−2)/4>s for N≥16. Hence N−c≤|S| and c≤q, so equality |S|=N−q forces exactly q spanning tree components with total excess r over order three. The star and larger-tree constructions have the needed part sizes and realize the bound. The component coefficients follow from counting bipartite trees on the fixed color classes (e.g., for (2,3), choose the shared column and attach each other column to one row, giving 12), and division by factorials accounts for unordered components of equal size. A fresh check verified direct distance sums for the constructions across all 72 admissible pairs with 8≤n≤16 and reproduced all three displayed exact counts, 31,046,400; 1,079,038,800; and 47,628,000.

## originality

PASS

Credit the scalar optimum, the distance identities and the component lower-bound method to prior work. The supported contribution is the equality-case classification of all spanning labelled incidence forests throughout the stated range, together with their enumeration. The prior rectangular construction produces particular forests and its degree-charging lower bound does not characterize all equality cases; the older square component argument anticipates the rigidity method.

## value

PASS

The scalar optimum cannot describe or count individual optimal landmark configurations. The spanning-forest theorem reduces all of them to a short list of component profiles, and the enumerator distinguishes the full labelled families without checking landmark subsets one by one. The strict near-square conditions arise from excluding empty rows and columns, not from an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
