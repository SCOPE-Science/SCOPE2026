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

From the extracted package directory, install packages listed in `requirements.txt` and execute `python check_numeric.py`, `python check_exact.py`, and `python check_cutoff.py`. The first constructs the antisymmetric two-fermion Hamiltonian directly and numerically checks full dark projectors for 120 deterministic graph selections through eight vertices; it also checks independent positive loss strengths by non-Hermitian time evolution. The second constructs exact cycle and component bases, tests their eigenenergies and loss constraints, independently checks maximality by ranks of projected monitored-edge vectors, and compares all basis-state survival probabilities with rational electrical-resistance calculations for 93 graphs (including all graphs on three and four vertices). The third exhaustively checks full-capture threshold graphs of sizes two through six (up to 32,768 detector patterns at size six).

All three scripts completed successfully on the supplied contents before assembly. Finite checks are not proofs of the asserted all-size classification. The mathematical proof is in `RESULT.md`. No external independent validation is claimed, and no physical experimental test, finite-time error bound, or interacting-particle test is supplied.
