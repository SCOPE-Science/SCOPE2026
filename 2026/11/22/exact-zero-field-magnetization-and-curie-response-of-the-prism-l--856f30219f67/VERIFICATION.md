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

# Checks and limitations

`verify_transfer.py` uses SymPy for exact symbolic factorization of the displayed transfer matrix, the all-size characteristic-polynomial identity and the second-derivative radical. It also checks the first seven trace counts independently of the radical simplification.

`verify_enumeration.py` uses Python's standard library to construct the physical base graph and every Ising bond of its line graph, then evaluates all \(2^{3n}\) spin assignments for each \(n\in\{3,4,5,6\}\). It obtains minimum energies \(-2nJ\) and ground counts \(86,450,1942,9074\); the magnetization-resolved counts for the first three sizes are checked against separately supplied exact values. Exact integer energy arithmetic is used throughout.

The infinite-family theorem is analytic: every step rests on the local triangle lower bound, exhaustive local transfer construction, an exact degree-four determinant and Perron-root differentiation. The finite checks are not independently sufficient to prove the all-size or asymptotic claims. No independent scientific audit has been performed.
