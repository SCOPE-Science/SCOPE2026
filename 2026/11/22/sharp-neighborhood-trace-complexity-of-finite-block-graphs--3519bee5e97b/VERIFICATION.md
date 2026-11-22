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

# Mathematical reproducibility

Run `python3 verify.py` with standard Python 3. The script constructs every labelled simple graph on at most six vertices, independently checks that every biconnected block is complete, computes distinct open-neighborhood traces for every parameter subset, and tests the claimed envelope. It also checks explicit witnesses for marker counts 1 through 18 and seeded random larger block graphs. The exact output and counts are recorded below following execution from the complete extracted package.

The mathematical proof is the incidence-forest counting argument and the explicit path-of-triangles witness in `RESULT.md`, not a claim of exhaustive verification beyond finite sizes. The marked set may be empty; the graph must be finite and nonempty. Some potentially relevant literature may not be indexed or accessible; no independent audit has been performed.

A run of the checker from its included standalone source reported:

`VERIFY_OK all_simple_graphs 33867 block_graphs 8367 parameter_sets 505867 sharp_witness_orders 18 random_cases 18432`

The exact same included checker is rerun after extracting it from the completed JSONL package. No exhaustive statement for larger ambient graph sizes is inferred from these tests.
