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

# Reproducibility and limits

Run the three checks with Python 3.9 or later, standard library only, with the supplied optimal-codebook text files in the same directory:

```sh
python3 verify.py
python3 alternate.py
python3 witness.py
```

The `verify.py` output checks all exact source words, all radius-one received-word intersections, every finite graph edge, exact independent-set counts of the small graph components, the 42-disjoint-edge structure at lengths six and seven, 80 and 502 codewords in the supplied optimum lists, and the length-eight zero-conflict case. It terminates in `VERIFY_OK`.

The independently implemented `alternate.py` uses pairwise Kendall inversion counts instead of received-word intersections; it independently confirms each length-two-through-seven conflict count, the within-orientation lower bound for enumerated examples, and the matching property at six and seven. It terminates in `ALTERNATE_OK`.

The `witness.py` inequality-DAG construction checks the cross-orientation sharpness witnesses for every length two through one hundred and terminates in `WITNESS_OK`. The infinite family is established mathematically by an acyclic local-gadget gluing proof in `RESULT.md`; finitely many tests do not themselves establish infinitely many cases.

All counts and certificates are integer and exact, with no random sampling or solver-dependent numerical tolerances. No test purports to constitute independent external mathematical validation. The closed-form all-length part depends on the human-readable proof's general combinatorial arguments, and the finite counts depend on reproducible exhaustive enumeration.
