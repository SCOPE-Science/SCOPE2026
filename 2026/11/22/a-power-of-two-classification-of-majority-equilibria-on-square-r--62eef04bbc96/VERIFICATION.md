---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

From degree 2n−2 and open-neighbor one-count r_i+c_j−2x_ij, tie retention gives one-cell r_i+c_j≥n+1 and zero-cell r_i+c_j≤n−1. A zero in a higher-degree row cannot share a column with a one in a lower-degree row, so rows nest, equal-degree rows agree, and the sorted row lengths determine the unique Ferrers representative. The rightmost one and first zero of a proper row give the two corner inequalities; a full row forces every column height at least one, and a zero row forces every column height at most n−1, so neither boundary row adds a condition. Increasing all positive widths by one and appending a zero preserves the corner inequalities. Conversely, a zero-bottom fixed shape cannot have a width-one row because that row would need a column of height n, so deletion and decrement are exact inverses. Complement followed by transpose is an involution on the orbit representatives and exchanges the zero-bottom and positive-bottom cases (the new last width counts old zero rows), proving the doubling with base two. A stabilizing row-and-column pair preserves row and column degrees individually; equal-degree supports coincide in Ferrers form. Thus the stabilizer is the product of multiplicity factorials, yielding the labelled count. Inspected the source verification materials, without executing uploads. An independent direct open-neighbor implementation exhausted all 66,064 boards for n=2,3,4 and found 6,32,302 labelled equilibria and 4,8,16 classes. Exhaustion of Ferrers partitions only (not all boards) through n=10 reproduced the recursive sets and every listed labelled total; replay: python3 /workspace/branches/d94764f3-f04d-4aa9-8bd2-75fd830f3797/ordinal5_independent.py. The universal result is proved by induction, not inferred from enumeration. No transpose quotient, two-cycle or basin result is certified.

## originality

PASS

Best-of-knowledge pass for the all-order square result, including the labelled orbit formula. A close all-rectangle statement does imply the square Ferrers theorem and 2^n count; its explicit attribution of that special case to the assigned result distinguishes it from independent earlier coverage.

## value

PASS

The symmetry class and labelled counts are natural invariants of a standard product graph under a specified local rule. The nested-support deduction and reversible doubling explain all equilibria, not just the known order-four census; the multiplicity formula then turns geometric shapes into exact labelled populations. The binary restriction, fixed states, and exclusion of transpose in the quotient are substantive and explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
