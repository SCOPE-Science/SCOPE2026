---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For a full-dimensional integral lattice polygon P with I interior and B≥3 boundary lattice points, Pick gives L_P(n)=(I+B/2−1)n²+(B/2)n+1. For Q=P×[0,m], m≥1, L_Q(n)=(mn+1)L_P(n); conversion to the four-dimensional Ehrhart-series denominator yields coefficients [1,(m+1)(I+B−3)+3m−1,(2m−1)(I+B−3)+(2m+1)I,(m−1)I]. The planar numerator 1+(I+B−3)t+It² has nonreal roots only if B=3,I=1,2,3. For the remaining real-rooted planar bases, the cited Wagner Hadamard/product theorem handles multiplication with [0,m]. For the three exceptional inputs, direct symbolic cubic discriminant expansions in q=m−1 were independently reproduced as [0,288,549,288,0], [256,2304,4180,2832,600], and [2304,10560,16317,10800,2592] (ascending coefficients). All are nonnegative on q≥0 and positive for cubic degree q>0; the q=0 quadratic discriminants are 4(I−1)². Positive nonconstant coefficients exclude nonnegative roots, establishing strict negativity of all roots including multiplicity. This is an infinite argument, not an inference from a finite grid.

## originality

FAIL

The full earlier 2026-10-25 Resultary theorem states precisely that every integral polygon prism P×[0,m], m≥1, has exclusively strictly negative real Ehrhart-numerator zeros, with the same four symbolic coefficient formulas; it additionally determines simplicity and the unique double root. Thus the November 8 final claim and unit-segment consequence are wholly covered by a strictly stronger, earlier published theorem.

## value

PASS

Real-rootedness for all three-dimensional lattice prisms over arbitrary planar polygons is a motivated exact classification; it covers the three exceptional non-real-rooted base types and gives a concrete restoration phenomenon. This would be useful as a self-contained result, though the actual statement was previously proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
