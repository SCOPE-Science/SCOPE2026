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

# Reproduction and limits

Execute `python3 square_root_partition_checker.py` with Python 3.8 or later. It uses only the standard library, including `itertools` and `math.comb`. The provided script independently builds every total function on small labeled sets, computes composition, verifies block preservation and the entire induced map, then compares its per-map counts to the stated finite sum. The matching outputs are in `square_root_partition_verification.txt`, with terminal line `ALL PRESCRIBED-BLOCK-FIBER TESTS PASSED`.

The proof covers all finite partitions and all induced block maps. Exhaustive enumerations end with a six-point ground set and cannot certify an infinite theorem by themselves; the counting bijection in RESULT.md supplies that proof. The structural assumption that every block is nonempty is used to make the induced block map unique. No independent audit has been performed.
