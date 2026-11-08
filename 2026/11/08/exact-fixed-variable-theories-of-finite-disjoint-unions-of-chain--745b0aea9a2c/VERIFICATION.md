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

# Verification instructions and limitations

Run the two bundled programs with ordinary Python 3 from the root of the extracted package:

```
python verification/fo_k_poset_refinement.py
python verification/partition_spectrum.py
```

Compare the exact standard output against `verification/fo_k_refinement_output.txt` and `verification/partition_spectrum_output.txt`, respectively. The first program enumerates every nonempty disjoint-union-of-chains isomorphism class with at most eight, seven or six elements at widths two, three or four. It refines full ordered \(k\)-tuple types using existential successor *sets* (not counts), then compares all pairs to the conjectured capped-multiplicity classification. It does not assume the expected classification when computing colors. The independent second program enumerates all integer partitions of orders through thirteen and compares capped multiplicities, a bounded-product recurrence, and the no-multiple-of-\(k+1\) description. Both outputs should end with `VERIFY_OK` or `PARTITION_VERIFY_OK`.

The proofs of length recognition, the permanent pebble invariant and the formal-series identity appear in `RESULT.md`. The finite experiments neither prove infinite quantifier-depth equivalence nor exclude an undiscovered earlier characterization. No independent mathematical audit has been performed.
