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

The measure is uniform on labeled acyclic edge subsets, not on spanning trees or rooted forests. A right-side vertex of degree at most one cannot be in a cycle and has four unmarked choices. Of the higher-degree vertices, the only possibilities are one double or triple, or two doubles with different hub pairs; repetitions or a triple with another high vertex give a four-cycle, and three distinct doubles give a six-cycle. This gives the stated normalization. For a single marked edge, the marked vertex can have degree one, one of two compatible double neighborhoods, or the triple. For same-right-endpoint pairs it has the forced double or the triple. For different right endpoints, two forced doubles have two distinct compatible choices when the hubs coincide and three when they differ. Counting with those multipliers gives all three joint probabilities in RESULT.md 70–75. Subtracting the squared marginal yields the three polynomial differences in lines 76–86, and their signs and leading terms give strictness and the stated limits for n≥3. As a bounded independent check, exhaustive depth-first cycle detection on all 2^(3n) masks for n=3,4 gave (total, single, three joint counts) of (328,134,48,48,52) and (1856,712,224,246,262).

## originality

FAIL

A distinct indexed finding on the same UTC date already displays the same U_n,V_n and all three exact covariance formulas in the identical unweighted forest model, on the larger domain n≥2. There is no distinct mathematical remainder in the frozen claim. This is verified overlap, not a finding about which record was first or about copying; relative priority is not established.

## value

PASS

As a mathematical result, an exact all-size classification for three natural pair orbits outside the series-parallel class is informative for the uniform-forest correlation question. In particular it distinguishes a nonvanishing negative dependence from two different inverse-square effects. This assessment of the theorem's substance does not award originality or incremental value to a duplicate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
