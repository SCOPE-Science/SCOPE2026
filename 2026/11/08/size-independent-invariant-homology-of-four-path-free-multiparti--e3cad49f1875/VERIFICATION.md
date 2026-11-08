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

# Executed checks and limitations

`verify_equiv_pf4.py` was executed directly using Python 3. The test enumerated every face by searching ordered four-vertex simple paths and independently computed the signed trace of each part-preserving permutation on the simplicial chain groups. There were 76 tested part-size tuples and 1,266 automorphisms. The trace equaled the theorem's formula on every case. Group averages agreed with the dimension \(\binom{m-1}{3}\) on every tuple. The largest enumerated complex had 102 nonempty faces. Execution completed with `ALL_VERIFY_OK`.

The code checks finite examples only; the uniform statement depends on the relative-chain and averaging proof in `RESULT.md`. No independent external mathematical audit has been performed.
