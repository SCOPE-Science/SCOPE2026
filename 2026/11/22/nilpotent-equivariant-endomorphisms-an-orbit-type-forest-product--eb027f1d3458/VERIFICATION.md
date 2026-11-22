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

Run `python3 check_nilpotent.py` with Python 3. The checker uses only the standard library and constructs each finite group action from actual left cosets. It enumerates possible images of each orbit representative, extends the maps equivariantly, and directly iterates every entire point map rather than treating an orbit-forest formula as its oracle. The 16 main mixed actions include cyclic groups of orders 2, 3 and 4 and the nonabelian group \(S_3\). It also independently checks all two-type tests giving the \(S_3\) mark table, plus an equal-size-incomparable case for \(C_2\times C_2\). The sentinel is `POINTED_G_SET_NILPOTENCE_CHECKS_PASSED`.

The proof is combinatorial for **all finite groups**, using the orbit-map criterion, strict cardinality descent across nonisomorphic transitive orbits, and a weighted directed matrix-tree determinant. Computational checks cannot establish the infinite-parameter statement or priority over uninspected literature. No independent audit was performed.
