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
# Verification

The exact mathematical proof is in `RESULT.md`. The first implementation `verify_dynamics.py` evolves the synchronous rule for three steps for every initial state with 2 through 6 matching pairs, and separately checks the local successor-neighbor predicate. It examined 597,861 labelled states and matched the formula in every instance. The second implementation `verify_transfer.py` uses a four-mask exact column transfer based on per-vertex successor requirements and independently reproduces the formula for all sizes 1 through 60. The two programs were executed from the included source files and produced the included `.out` files.

Run the tests with a standard Python 3 interpreter in the directory containing the scripts:

```
python3 verify_dynamics.py
python3 verify_transfer.py
```

These checks do not certify the theorem for infinitely many graph sizes: that assertion follows from the exhaustive support-type proof. No human or independent external audit has been performed.
