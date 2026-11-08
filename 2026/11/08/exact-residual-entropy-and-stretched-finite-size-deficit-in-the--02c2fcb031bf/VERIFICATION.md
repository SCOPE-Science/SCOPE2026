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

# Reproducibility and verification

The ground-state statement concerns the zero-field three-state antiferromagnetic Potts Hamiltonian and the deterministic triangular Apollonian network, with no varying edge weights or imposed boundary spins. The proof in `RESULT.md` establishes its exact count and entropy expansion for every integer generation at least two by boundary-state induction and convergent log recurrences.

Run `python3 verify.py` for a separate 27-state minimum-plus-count recurrence, exact finite brute force for generations zero through two, identities through generation nine, and checks of the two entropy constants. Run `c++ -O3 -std=c++17 exhaustive.cpp -o exhaustive && ./exhaustive` for an independently constructed graph and exhaustive spin evaluation through generation three, including all 43,046,721 configurations at the largest tested generation. During the present checks the programs returned `ALL_TRANSFER_CHECKS_PASS` and `ALL_EXHAUSTIVE_CHECKS_PASS` respectively.

All-generation assertions depend on the analytic recurrence proof, not on finite computation. Calculated digits are numerical evaluations of explicitly convergent series, not unconditional certified interval arithmetic. The literature comparison is provisional and independent audit has not yet been performed.
