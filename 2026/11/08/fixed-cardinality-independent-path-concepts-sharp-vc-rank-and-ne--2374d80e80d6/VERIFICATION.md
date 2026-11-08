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
# Verification details

Run `python verify.py` using Python 3.10 or later. The script has only standard-library dependencies.

The checker enumerates all fixed-cardinality independent sets and every coordinate support for each path length from one through fourteen, covering seventy \((n,k)\) parameter pairs. It separately verifies every label assignment of the constructive VC gadget for lengths through twenty-one, and applies an exhaustive, memoized Littlestone recursion to all parameter pairs through length thirteen. It checks the cardinality identity, the online lower and upper bounds, and the exact one-defect case. On the reviewed artifact, the terminal outputs were `VC_ALL_PARAMETERS_PASS 70`, `GADGET_ALL_ASSIGNMENTS_PASS 1662`, `LDIM_ALL_SMALL_PASS 62`, and `FIXED_SIZE_PATH_VC_ONLINE_PASS`.

The unbounded theorem does not follow from finite experiments: the defect-count parity argument, explicit completion gadgets, count-preserving coordinate shift, and disjoint threshold-product tree are the mathematical proofs. The checker does not assert an exact online dimension outside its finite recursion or historical originality.
