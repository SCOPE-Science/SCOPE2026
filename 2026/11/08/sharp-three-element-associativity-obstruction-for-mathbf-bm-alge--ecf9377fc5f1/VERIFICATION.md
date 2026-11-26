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

An independent integer-only enumeration exhausted all 1, 16, and 19,683 operation tables on the carriers of sizes 1, 2, and 3. It tested M by equality of its left-translation row with the diagonal, and B by L_{(B·x)·y}=L_x∘L_y for every x,y, computing associativity by L_{x·y}=L_x∘L_y. It formed full marked permutation orbits and computed closure of the marks. The resulting tuples (labelled, marked classes, generated classes, nonassociative classes, generated nonassociative classes) were (1,1,1,0,0), (14,7,4,0,0), and (204,36,7,6,1). At order 3 the six specified nonassociative representatives have disjoint size-six marked orbits; the underlying types are distinct (they have one versus two nonzero products relative to the unique absorbing element). The fixed counts are 204,4,4,4,0,0. Only the marking B=0,M=2 of Type II generates its carrier, because 2·2=1. The explicit associativity failure follows by the two products displayed in the finding.

## originality

PASS

Credit only the exact lower cutoff, order-1–3 census and nonassociative classification, including uniqueness of the generated class. The cited Imamura paper already supplies the identical Type II table with both markings, including the generated marking. This gives the upper cutoff immediately, not the exclusion of order 2, the complete catalogue, or uniqueness. No matching distinct census or stronger theorem was established in the checked sources.

## value

PASS

The census locates the first failure of associativity after relaxing the identity-bearing BI setting and distinguishes arbitrary markings from generation by the named combinators. For a researcher looking for smallest BM witnesses, the six-class list establishes which alternatives exist, and the uniqueness result identifies the only generated obstruction at the cutoff. This is a natural finite classification, not merely a replay of the famous or already displayed example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
