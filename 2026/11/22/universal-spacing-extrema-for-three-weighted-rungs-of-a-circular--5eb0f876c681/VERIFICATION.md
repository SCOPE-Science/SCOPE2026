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

# Reproduction

Run `python3 verify.py` with the Python 3 standard library; it prints `VERIFY_OK 14694 exact rational tests` on success. Run `python3 verify_symbolic.py` with SymPy installed; it prints `SYMBOLIC_VERIFY_OK` upon exact symbolic verification.

The main checker independently constructs the full two-layer weighted Laplacian, uses exact-rational Bareiss cofactors, independently inverts the reduced one-dimensional cyclic operator, compares their determinant ratios, checks all three-rung placements for the specified finite sizes and validates strict balancing where applicable. The polynomial checker verifies both algebraic identities underlying the all-size local rearrangement theorem. The proof establishes the positive parameter-domain bounds analytically; no finite computation is presented as a universal proof.

# Mathematical boundaries

The theorem concerns three identically reweighted rungs and unit rail conductances on \(C_n\square K_2\), \(n\ge5\), with positive real rung weight. For \(t=1\), all locations tie. Unequal defect weights and more than three defects are outside the claim. Independent scientific audit has not been performed.
