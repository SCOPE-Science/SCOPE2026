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

The defining adjacency matrices were independently generated from coordinate rules and checked against \(A^2=4I+2\mathbf1\mathbf1^{\mathsf T}\). All \(22{,}880\) nine-absorber instances were exhaustively evaluated in two standalone implementations included with this package.

`check_exact.cpp` uses exact integer fraction-free symmetric elimination on the two compressed spectral-projector matrices and asserts the five joint-rank classes for each graph. A successful local build and replay printed `EXACT_RANKS_OK`.

`check_krylov.cpp` independently uses the physical bright-subspace columns \(\{e_t,Ae_t,A^2e_t:t\in T\}\) and dual-prime modular ranks. A Hadamard bound, \(|\det M|<10^{16}\) for every square minor, and the product of the two primes exceeding \(10^{18}\), proves that the maximum modular rank is exactly the rational rank. A successful local build and replay printed `KRYLOV_OK cases=22880 primes=1000000007,1000000009`.

Both codes are self-contained C++17 and require an ordinary C++ compiler. The physical implications use the exact spectral projectors and strict positivity of every detector rate; the code does not attempt to certify any claim about finite-time decay constants, experimental errors, or independently established novelty.
