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

The self-contained `verify.py` uses standard-library exact fractions to enumerate all functions on sets of sizes two through six and compare the observed component count, size-count means, and mixed covariance against the analytical formulas. It separately checks exact monotonicity of the size sign factor through size 80. Numeric cutoff checks use sizes 1000, 10000 and 100000 and test the second-order prediction within three vertices; they are empirical sanity checks only.

Run `python3 verify.py`; the checked execution printed `PASS: 3386 exact symbolic, finite exhaustive, and numerical assertions`. The infinite sign classification and threshold expansion require the proof in `RESULT.md`; exhaustive small sizes and floating-point checks are not infinite proofs. Independent audit has not been performed.
