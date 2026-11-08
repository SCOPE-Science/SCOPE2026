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

# Verification of exact binary-field automorphism maxima

The standalone `verify.py` works over the two-element field with bit-packed binary structure matrices. It enumerates every matrix of dimension one through four, tests nonsingularity by exact binary elimination, strong connectivity by forward and reverse reachability, and the entire graph-automorphism group by checking all permutations. For each dimension the exact maximum is compared to the theorem; for dimension four, this entails all \(65{,}536\) structure matrices, including singular and nonsimple ones.

Results: among simple matrices, the number of labeled matrices is \(1,3,80,11{,}658\), with exact maxima \(1,2,3,24\) at dimensions \(1,2,3,4\). The checker additionally tests all even loopless-complete constructions in dimensions \(2,4,6,8\), odd hub constructions in dimensions \(3,5,7\), and an exceptional directed three-cycle. It verifies directly that every full symmetric-invariant binary matrix in dimensions \(3,5,7,9\) fails either invertibility or strong connectivity. The final line is:

`VERIFY_OK exhaustive_n=1..4; witness_n=2,3,4,5,6,7,8; odd_obstructions=3,5,7,9`

The all-dimensional theorem is not deduced from finite enumeration. The critical proof step for odd \(n\ge5\) uses the standard classification of proper nontrivial normal subgroups of \(S_n\), which is established mathematical theory rather than a computational assertion. Replay with `python verify.py` must match `verification_output.txt` byte for byte. No independent audit or proof-assistant certification has been performed.
