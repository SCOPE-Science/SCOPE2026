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

The real Walsh basis diagonalizes unnormalized XOR convolution with signs (−1)^|S∩E|. Expanding one factor 1−2·1_{π(i)>i} per selected row groups constraints by a nonattacking partial assignment, with (n−j)! completions for j assigned rows. On processing selected rows in descending order, each previously used column is also allowed in the new row, leaving exactly n−i−(j−1) choices when inserting its j-th rook. This proves the integer algorithm. The frozen second method uses the classical excedance-word recurrence and boundary deletions (checked against the cited original), then an unnormalized Walsh transform. An independent exact replay of the rook formula exhausts all 524287 order/mask pairs and matches direct permutation enumeration at n≤8. It reproduces the full nullity table, including zero nullity at 3,7,11,15. Every one of the 24 zero masks at 19 matches the certificate; bit reversal gives 12 two-element orbits. The inertia is (131048,131072,24) and the smallest nonzero magnitude is 3403284480. By the triangle bound, attained at the empty mask, the largest magnitude is 19!, so the quotient is exactly 41247931725/1154. The dimension used in the calculation is 2^(n−1); the uploaded program's printed dimension label uses n−1, the bit length, but its loop bounds, rank expression and the stated theorem use the correct dimension.

## originality

PASS

The supported distinct claim is the first failed order in the specified residue class, with complete blind-space and conditioning data at that order. The underlying excedance counts, recurrences, complement-reversal duality and classical rook/inclusion–exclusion enumeration are not originality claims.

## value

PASS

An invertible multiplicity-weighted pattern convolution permits recovery of every input on the cube. Odd orders avoid the elementary forced reversal-fixed odd-frequency zero present at even orders, and the initial successful residue-class orders are not enough to guarantee subsequent recovery. The first exact failure at 19 and its complete blind modes tell precisely which signals are unrecoverable there, and the nonzero gap quantifies worst-case stability on the remaining modes. This is a motivated cutoff, not a single arbitrary order or frequency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
