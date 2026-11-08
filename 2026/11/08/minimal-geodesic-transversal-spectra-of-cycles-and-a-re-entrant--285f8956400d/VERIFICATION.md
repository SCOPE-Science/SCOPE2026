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

# Reproducible verification
Run `python3 verify.py` with Python 3.8 or newer. Only the Python standard library is used.

The verifier independently constructs the cycle's shortest simple paths, keeps only maximal geodesics, enumerates each vertex subset for every cycle order \(3\le n\le18\), and checks the original path-hitting and inclusion-minimality definitions directly. It then compares each minimal set with the proved cyclic-gap criterion and its cardinality with the exact coefficient formula. The observed output is:

```text
VERIFY_OK cycle_orders=3..18 all_subsets=524280 minimal_sets=497 independent_shortest_paths=PASS gap_characterization=PASS exact_count_polynomial=PASS reentrant_purity=PASS
```

The verification exhausts only the indicated finite range; the unrestricted result rests on the proof in RESULT.md. Neither the program nor this report supplies independent peer review or publication-priority certification.
