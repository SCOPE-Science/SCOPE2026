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

The accompanying `verify_edges.py` uses only Python's standard library. Execute `python3 verify_edges.py`.

The checker constructs exact integer-numerator images of every source interval, treats the critical-point-spanning source cell separately, and performs strict integer comparisons against target intervals. For all integers \(2\le m\le512\) it independently counts the directed positive-overlap pairs and checks the prime-factor expression; it also checks 100 exact square-family instances. Observed output includes `VERIFY_OK exact_integer_adjacency_resolutions= 511 sharp_square_family_cases=100`.

The checks are finite computational corroboration only. The all-resolution count, sharp extremal bound, and almost-sure trajectory statement are proved analytically in `RESULT.md`. No numerical sampling is used to infer an infinite statement. Independent scientific audit has not been performed.
