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

A singleton square forces f(0)=0 even without named constants. The equality of sum and product of two distinct source singletons forces disjointness when both images are nonzero. The proposed extension is unique since the singletons generate; a support meeting an inactive letter maps to 0, and otherwise its image is the union of its chosen blocks. This preserves union and preserves a product precisely via the disjointness/collision rule, including all 0 cases. Assigning each target letter to its source box or to the unused box gives (k+1)^m; using inclusion–exclusion on s occupied boxes gives the stated rank coefficients. The surviving 2^s-1 nonempty unions are distinct, so only the inactive supports collapse to the 0 congruence class. Every active set of size s is attainable for 0<=s<=min(k,m); surjectivity requires m singleton blocks and gives a falling factorial. For an idempotent, each nonzero block must lie entirely in the active set, so the disjoint nonempty blocks form a singleton permutation of that set, which idempotence forces to be identity. Intersections give composition, and the full-rank permutations give all automorphisms. Independent operation-table enumeration (`python3 /tmp/opencode/frozen_checks.py hom`) exhausted all functions in the four displayed small-rank pairs; totals, image-size histograms and numbers of distinct kernel relations all matched. The finite check does not substitute for the all-rank argument. Frozen verify.py and its recorded claims were inspected but not executed.

## originality

PASS

The concrete semiring family and useful relations on it are prior. Neither inspected construction nor the strongest matching corpus results give the complete labelled cross-rank homomorphism, image and kernel census or the resulting Boolean semilattice of idempotents for these operations.

## value

PASS

For an established semiring family, the result resolves which maps and quotient ranks occur across all source/target sizes, not just how many endomorphisms there are. The kernel and retract classifications give concrete structure for composing or ruling out morphisms in this family. The numerical inclusion–exclusion is elementary; the value lies in the complete uniform classification and its structural consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
