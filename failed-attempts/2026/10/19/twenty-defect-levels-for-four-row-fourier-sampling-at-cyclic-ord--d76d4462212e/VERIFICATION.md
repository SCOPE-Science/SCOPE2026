---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The claim concerns all ordered pairs of independent four-element row and column sets, not principal minors. Row translation multiplies each column by a nonzero scalar and unit dilation permutes all column sets. An independent Burnside count gives fixed-subset totals 516, 156, 156 and 180 over the twelve translations for units 1, 5, 7 and 11 respectively, hence 1008/48 = 21 row orbits. The frozen cyclotomic test is exact: the determinant reduces to a polynomial of degree at most three modulo x^4−x^2+1, with each coefficient bounded by 24 from the 24 terms. Thus vanishing at all four distinct roots modulo 61 is equivalent to zero over the complex numbers. A separate subset-DP census in the cyclotomic ring, without using orbit reduction or executing the frozen code, checked all 245,025 pairs directly. It reproduced every row-orbit triple, all 20 defect multiplicities, 40,608 singular pairs, fraction 1504/9075, and the two stated defects. The identical sorted occupancy vectors for divisors 1, 2, 3, 4, 6 are respectively (4), (1,3), (1,1,2), (0,1,1,2), (0,0,1,1,1,1). This certifies singularity, not the subdivision of singular minors by rank or their conditioning.

## originality

FAIL

The distinct indexed record 2e8e14615690 contains the complete rank-refined table for exactly the same 21 affine orbits. Adding the rank-2 and rank-3 counts gives every defect entry and the aggregate, hence every conclusion of the census. Its two relevant entries also give the same equal-occupancy contrast by elementary residue counting. Coverage is demonstrated without treating this later-dated catalogue entry as antecedent or drawing any conclusion about independent priority. The inspected earlier results give only the defect-zero level and the near-consecutive orbit, not the full census.

## value

FAIL

Order twelve is the first cyclic order both nonsquarefree and not a prime power, and the number of failing four-frequency supports is a motivated refinement of full spark. However, every entry and the proposed contrast are mechanically determined by the existing stronger partner-rank table. The independent exact replay is valuable for validation but does not turn this projection of a known table into an independently needed unknown invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
