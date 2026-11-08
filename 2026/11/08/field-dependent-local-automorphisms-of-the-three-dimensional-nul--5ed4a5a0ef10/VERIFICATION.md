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

The arbitrary-field proof directly solves the interpolation equations for each possible first nonzero coefficient of an algebra element. The only nonstandard issue is that characteristic two eliminates the mixed product coefficient \(2uv\), coupling the square and cube parameters. A direct finite-field brute-force check in `verify.py` separately constructs elementwise automorphism orbits and tests every invertible lower-triangular linear map; no classification formulas are used to decide locality.

Checked by executing `python3 verify.py`: for \(q=2,3,4,5\), the local and global counts are respectively \((4,4),(108,18),(144,48),(4000,100)\), followed by `VERIFY_OK`. These tests include \(\mathbb F_4\), so the characteristic-two argument is tested beyond the prime field. Finite computations are not proofs for all fields. The novelty comparison is limited by accessible literature and does not assert independent mathematical certification.
