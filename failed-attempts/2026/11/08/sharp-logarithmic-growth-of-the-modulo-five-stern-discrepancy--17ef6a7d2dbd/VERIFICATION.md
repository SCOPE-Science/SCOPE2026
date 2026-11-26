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

For the consecutive Stern pair the two children are the invertible maps L(a,b)=(a,a+b), R(a,b)=(a+b,b) modulo five. L fixes the initial pair (0,1), so leading zeroes preserve indexing. Lexicographic length-r words concatenate the L block and then the R block. A prefix completed in the second block has weight S_r(Lq) plus its internal prefix; this proves the three updates including empty and full prefixes. The independent finite recomputation confirms S_5=S_1, A_28=A_16−4 and B_28=B_16+4 at all 24 states. The S update propagates its period four, hence also period twelve. A constant translation of both arguments of either extremum passes unchanged through min/max, so the all-state extrema certificate propagates from r=16 by induction. The listed base pairs and witness discrepancies match. Consecutive dyadic bounds squeeze the running absolute maximum to (log_2 X)/3+O(1).

## originality

FAIL

A distinct earlier-dated Resultary record establishes the same residue-pair discrepancy on exactly the same inclusive prefix domain and the same shifts for every r≥8, covering the submitted r≥16 theorem. It explicitly supplies the same witness lengths and values, the same all-state 16-to-28 extremum certificate, and both signed dyadic asymptotics, which imply the submitted all-X estimate. This is demonstrated coverage, not a failure of retrieval or a defect in the mathematics.

## value

FAIL

The discrepancy problem is well motivated by Reznick, but as a contribution the frozen finding only repeats known exact extrema and witnesses and takes a routine consequence of their dyadic growth. Rechecking the known table and narrowing its valid range does not add a worthwhile new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
