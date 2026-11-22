---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The package contains two self-contained Python 3 programs using distinct graph implementations and orbit-classification algorithms. The scripts `direct_checker.py` and `functional_checker.py` were executed, producing identical JSON files with complete period/first-entry-time populations. The command `cmp direct_output.json functional_output.json` completed successfully.

Each enumerator processes all 16,384 initial binary states separately for both fourteen-vertex graphs, and the classification outputs sum to 16,384 per graph. The state-indexed SHA-256 digests are `a3f0f53509bb55025eeb957bdc84ad7cc290b5ef2c91c911aa8060e78cbabf10` for the first graph and `21340a7eb526c4436ba4799764212dc6fc55f52ba13e4237209bd66632865cb5` for the switched graph. The complete count table is in RESULT.md and the JSON output.

The labelled initial configuration represented by integer 3482 on the first graph has iterates, at times zero through eleven: `3482,13586,3474,13330,3472,13314,2448,9218,400,8194,384,8194`. The first periodic time is nine. The switched graph's initial integer 1245 has iterates `1245,4508,9309,5012,9293,5008,9229,912,8205,912` at times zero through nine, first periodic at seven. Bit position \(v\) is vertex \(v\). Both witnesses enter two-cycles, not fixed points.

Cospectrality follows analytically from a four-vertex orthogonal switching identity and nonisomorphism from a triangle-neighbor common-intersection invariant. Numeric spectral agreement was also observed, but the proof does not rely on floating-point eigensolvers. A symbolic characteristic polynomial factorization was compared independently during the analysis.

No assertion is made about unexamined infinite families or unindexed publications. Independent external auditing has not been performed.
