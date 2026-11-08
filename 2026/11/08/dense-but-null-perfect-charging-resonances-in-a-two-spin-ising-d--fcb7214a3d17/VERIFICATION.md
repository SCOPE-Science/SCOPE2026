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

# Reproduction and limitations

Run `python verify.py` from the package directory using Python 3.9 or newer, standard library only.

The program checks 29 symbolic rational members of the explicit unbounded-DM triple family, several numerically exponentiated full Hermitian four-by-four Hamiltonians, the three characteristic coefficient identities, independently computed Jacobi eigenvalues at five test targets and increasingly accurate exact resonant couplings approximating those targets. It prints the number of deterministic assertions that passed and raises an assertion if any test fails.

The statement that the countably many exact resonances are dense in the *entire* positive coupling quadrant is analytic: all physical Jacobi eigenvalue triples are approximated by odd integers, and the reconstructed couplings vary continuously. Finite sampled couplings alone are not a proof of density. This verification reports no independent audit, and does not certify correctness for nonzero noise or other battery Hamiltonians.
