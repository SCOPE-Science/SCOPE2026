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

# Verification

The `verify_howe31.py` program constructs the genus-three Cartier coefficient polynomials twice, by binomial convolution and by polynomial products, and compares them before computing their exact monic gcds in characteristic 7, 23 and 31. The roots are obtained from the polynomial factorizations over the algebraic closures, not from a census of rational parameters.

The `verify_maximal.py` program performs a complete exact scan of \(\mathbb F_{31^2}\) for each of the 29 admissible prime-field coefficients, computes the four fiberwise square-root multiplicities including the four points above infinity, tests the Weil bound, and independently recovers the quotient curve point-count identity.

The `verify_branch.py` program independently builds the eight branch points in \(\mathbb F_{31^2}\), enumerates all ordered triples defining candidate projectivities and verifies all image sets. The reported automorphism counts 16 and 8 and lack of a projectivity between the two specified branch sets are complete over the algebraic closure because three rational branch points determine the map.

Run these three files with Python 3 in the same directory. They use only the Python standard library. The expected final success markers are `HOWE31_GCD_CERTIFICATE_PASS`, `HOWE31_MAXIMAL_CERTIFICATE_PASS` and `HOWE31_BRANCH_CERTIFICATE_PASS`. Outputs are computations supporting the exact statements; none provides independent human review. The broader historical-priority comparison is incomplete because a directly relevant 2024 poster was not accessible.
