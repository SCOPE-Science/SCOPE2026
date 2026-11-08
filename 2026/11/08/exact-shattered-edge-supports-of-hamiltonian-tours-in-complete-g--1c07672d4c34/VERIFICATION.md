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

# Verification record

Run `python3 verify_hamiltonian.py` from the directory containing the standalone script. It uses only Python's standard library. It enumerates Hamiltonian cycles by permutations with reversed tours identified, computes their edge-bitmask traces, and compares full trace sets with the structural classification. It tests every edge support through size \(n\) on \(K_n\) for \(3\le n\le7\), for 209,087 nonempty supports, and independently checks the complete coefficient counts. It then checks all 50 feasible path-component-length types on \(K_8\) and \(K_9\). The expected output ends with `HAMILTONIAN_EDGE_SHATTERING_CHECKS_PASS exhaustive_supports= 209087 representative_types= 50`.

The mathematical proof is not a consequence of these finite calculations. Its critical infinite-size step is the explicit five-block complement cycle together with Dirac's minimum-degree Hamiltonicity criterion for at least six blocks. The proof separately handles the two-, three-, and four-block cases. No theorem for incomplete host graphs or general cycle families is asserted.
