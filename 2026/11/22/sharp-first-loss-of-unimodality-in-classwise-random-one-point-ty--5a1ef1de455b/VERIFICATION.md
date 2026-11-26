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

The Fraïssé extension property realizes exactly one new-class diagram and all adjacency subsets in each represented class. Homogeneity identifies equal diagrams with equal complete types, and nonalgebraic types exclude the named points. Consequently c0=k+1 and cj is the sum of binomial coefficients for j>=1. For n<=16, a rise from j to j+1 at j>=3 needs a class b>=2j+2. Its contribution to the preceding difference is at least 28, 90, or 297 at j=3,4,5, while all others can offset at most 28, 20, or 1. In the j=3 equality-bound case, splitting the other eight points strictly reduces the pair count, and leaving them together gives a positive contribution instead. For j>=6 the remainder is too small to offset anything. Rises therefore propagate back to the 2-to-3 step. Except in the all-singleton case, c0<=c1, so any failure requires c1>c2 and c3>c2. The second inequality forces a size-six or larger class and c2>=15; the first requires n>=16. At n=16 equality c2=15 exhausts all within-class pairs with just one size-six class, and the explicit valley persists with additional singletons. A separate enumeration of nonincreasing partitions using the binomial recurrence examined 914 profiles and returned only (6,1^10) with coefficients (12,16,15,20,15,6,1). Replay by generating partitions with each next part at most the previous one, summing each part's row starting from binom(a,0)=1 and adding 1 at grade zero, and detecting any positive adjacent difference after a negative one. Frozen VERIFY.py and its recorded output were inspected, not executed.

## originality

PASS

Best of the inspected evidence supports the sharp threshold, minimal-profile uniqueness and persistence as distinct. Neither the extension-count formula alone nor the existence of nonunimodal multipartite independence polynomials is credited as new.

## value

PASS

The first failure measures when aggregating unimodal within-class rank counts can create a valley. The result gives the full minimal obstruction rather than just an example, and the backward-rise lemma explains why only the first two nonconstant coefficient comparisons can cause failure at these orders. The equivalent multipartite graph statement also makes the cutoff relevant outside the type-count interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
