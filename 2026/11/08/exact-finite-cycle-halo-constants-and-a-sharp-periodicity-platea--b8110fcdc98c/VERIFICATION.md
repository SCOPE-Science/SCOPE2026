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

The finite exact-rational checker in `verify.py` was run with Python 3. It independently enumerated every nonempty marked subset of each cycle of lengths 2 through 10; for each cycle it tested all strict rational threshold breakpoints with denominators at most the cycle length and all consecutive open-interval midpoints. It compared the direct halo sizes with the claimed cardinality upper bound and verified a contiguous-block extremizer for each cardinality. It checked the endpoint jump and large-cycle estimates. Output:

`VERIFY_OK all_critical_levels_and_midpoints_n=2..10 number_level_cases=259 sharp_cardinality_upper_bounds=True contiguous_block_extremizers=True n10_alpha3/5_C=8/5 finite_plateau_jump=True large_n_bounds=True`

The proof, rather than the finite enumeration, establishes all integers, all real thresholds, and permutation extensions. No independent audit has been carried out.
