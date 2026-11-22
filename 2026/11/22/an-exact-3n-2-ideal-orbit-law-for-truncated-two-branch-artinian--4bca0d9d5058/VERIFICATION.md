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

The proof uses the radical as a direct sum of one trivial and one uniserial module for multiplication by \(y\), and the explicit triangular automorphism action. All finite checks below use the full invariant-subspace condition, not a sample or interpolation. The attached `verify_orbit.py` enumerates every RREF radical subspace for the indicated small prime fields and calculates the complete orbits from algebra automorphism generators. It compares the exact number of proper ideals \((N-1)q+N+1\) and the number of proper-ideal orbits \(3N-3\); the whole ring gives one additional singleton ideal and orbit. Execution output is included in `verify_output.txt`.

The test covers \(N=3,4,5,6\) over \(\mathbb F_2\) and \(N=3,4,5\) over \(\mathbb F_3\). Every field and all larger \(N\) follow from the symbolic proof, not from these finite experiments. The automorphism-group scheme, absolute publication priority, and the all-length numerical brute-force census have not been independently certified.
