---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the specified relative one-point game, an abstract move either extends a represented class or creates a new class. At depth t the first kind requires at least t unused points in each represented class independently; the second must use an untouched class of size at least t and leave the depth-(t−1) staircase among the other untouched classes. Conversely, if the depth-t capacities and staircase hold, using a point in the requested represented class or starting a largest untouched class leaves the depth-(t−1) conditions. This proves the exact local equivalence by induction including t=0 and F empty. Summing the row lower bounds forces t(t+1)/2; equality leaves exactly the staircase with distinct sizes, giving the stated multinomial. Enlarging the largest block (for t>0) fills every allowed larger order without increasing the rank beyond t, since only t classes exist. Replayed an independently written profile-game recursion for all partitions of orders 0–12 and all 71,820 choices of occupied sizes in those profiles; it agreed with the formula and the maximum rank at each order.

## originality

FAIL

A distinct published component-rank staircase theorem already provides mathematical coverage: with pure sets inside the equivalence components, it gives the full frozen local assertion, not just the case of the empty base or the same numerical threshold. The elementary extremal counting consequence does not give a materially distinct remainder. This establishes coverage in the published corpus; it does not establish which of the two same-day versions appeared first or whether either was independently discovered.

## value

FAIL

The rank of this non-free-amalgamation age is a natural example and the staircase theorem is informative. But as a standalone increment over the verified broader theorem, the local and global laws are exact substitutions. The extremal size and unique type follow by row summation and equality; the only extra presentation, a multinomial for that same type and the inverse triangular bound, does not leave an independently valuable new finding to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
