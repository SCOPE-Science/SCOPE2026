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

# Computations and logical scope

The binary whole-wheel matrix is constructed independently of the polynomial proof in `verify/check_wheel_matrix.py`. It verifies the dimension of the kernel of every power through beyond the predicted nilpotency index for the 98 consecutive rim sizes 3 through 100, together with circumferences 120, 128, 160, 192 and 256: **673 exact power/nullity comparisons**. For circumferences 3 through 16 it constructs the full functional graph, removes noncyclic vertices by indegree elimination, and counts exact distances from the periodic set: **262128 binary states**, with complete agreement with the formula. The cases of circumference 3 and 4 are robustness checks outside the claimed range.

A second standalone implementation in `verify/check_local_module.py` uses truncated polynomial multiplication on \(\mathbb F_2[t]/t^h\) to implement the hub–rim local operator and compares the predicted nilpotent kernels and the cubic power identity for \(h=2,4,8,16,32,64,128\): **536 exact checks**. Both results were run on the actual standalone program files and their verbatim outputs are embedded beside the programs. Only exact integer/bit arithmetic is used; neither proof nor classification is inferred from finite enumeration.

The general proof checks the critical module splitting, explicit local operator, all local ranks (including the two exceptional small even scales), the Fitting decomposition, and the distinction between cumulative kernel counts and exact first-entry counts. These checks do not establish uniqueness among all published work or an independently audited result.
