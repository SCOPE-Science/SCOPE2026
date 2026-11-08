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
# Reproducibility and limits

The mathematical correctness argument differentiates the monic-coefficient parametrization and uses evaluation at the distinct Frobenius conjugate roots to prove exact tangent independence. Formal straightening and the normalization exact sequence identify the local algebra and the Picard group. These are general proofs for all prime powers and \(n\ge3\); the following exact computations only support specific small cases.

Execute `python3 checks/field_orbits.py`: this standalone standard-library program builds finite fields, explicitly enumerates Frobenius orbits and coefficient images, independently ranks tangent matrices over each field, and checks the arithmetic-genus and Picard point-order formulas for \((q,n)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,3),(5,3)\). Its expected output is `checks/field_orbits.txt`, ending with `ALL_INDEPENDENT_FINITE_CHECKS_PASSED`.

Execute `python3 checks/hilbert_functions.py`: this separately implemented exact mod-two homogeneous coordinate-ring calculation checks degree-by-degree Hilbert dimensions for \((q,n)=(2,2),(2,3),(2,4)\), at the printed degrees, against the predicted genus. Its expected output is `checks/hilbert_functions.txt`, ending with `ALL_HILBERT_REPLAYS_PASSED`. The \(n=2\) tests are controls only; the scientific finding is for \(n\ge3\).

Neither program enumerates all primes, exponents or \(n\); these finite calculations are not proofs of any all-parameter statement. The local gluing is proved mathematically, and no independent mathematical audit has been performed.
