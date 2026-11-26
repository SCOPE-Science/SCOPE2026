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

A trigger of K precludes triggers at each of its three guard sites; hence every old trigger persists after the simultaneous toggle. A new trigger would have a toggled guard site where an old, still present trigger precludes it. This proves involutivity even with repeated cyclic indices. Expansion gives DσK, with even-parity image and each fiber parameterized by u and its complement. Uniform u weights each fiber twice. Its distance indicators are w, whose zeros are exactly a=c≠b. For n≥7 the six directed differences of the three input offsets are distinct residues, so distinct windows share at most one bit; the probability of zero is 1/4 for either value of that bit. Three consecutive zero events would require the shared bits u_(i+1), u_(i+2), u_(i+3) to be pairwise unequal. Inclusion–exclusion therefore gives 1−3/4+3/16=7/16 for all ones. Means and variances follow. Closed walks with a specified initial step are in bijection with indexed cyclic words, for all n including n<3. An independent exact sparse-polynomial determinant expansion (/workspace/branches/6f5f3a6d-c8ab-4eac-ab99-1c807d3e5abd/charpoly_check.py) agrees coefficientwise with both quartics multiplied together. Direct fiber enumeration with /workspace/review_replay.py checks n=1–7 (n=7: 64 fibers, 28 triple successes). The CLT follows by independent length-floor(n^(1/3)) blocks separated by three indices: discarded variance is O(n^(2/3)), and at most three boundary summands change in passing to the ring. The frozen verifier evaluates the histogram/trace comparison at four z values, not coefficientwise as its verification prose might suggest; the all-length PGF identity is proved by the closed-walk argument, not those evaluations.

## originality

PASS

Pass for the explicitly reduced eight-state distribution calculation and the exact dependence and fluctuation laws, not for discovery of the CA or two-point fibers, and not for existence of an implicit complete distance enumerator. The strongest identified predecessor actually implies a 64-state PGF on the same ring ensemble. It does not give the reduced formula or the joint indicator and limit laws. The best-of-knowledge judgment does not settle absolute priority.

## value

PASS

The distance observable is natural for the already studied fibers. The result replaces a minimum-distance answer by a tractable reduced exact law and identifies a concrete mechanism making all pairs behave independently while triples do not. The exact linear variance and scaled limiting law distinguish typical pairs from the extremizers; the contribution is not merely a small enumeration or a fresh execution of the old collision graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
