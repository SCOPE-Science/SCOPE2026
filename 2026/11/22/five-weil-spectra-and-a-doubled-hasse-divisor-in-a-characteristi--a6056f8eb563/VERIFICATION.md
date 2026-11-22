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

The standalone file `verification/check_dihedral11.py` uses only the Python standard library and terminates successfully with `DIHEDRAL11_WEIL_AND_CARTIER_VERIFIED`. It performs exact finite-field sums in two irreducible quadratic models of \(\mathbb F_{121}\), independently counts \(C_a\) and its genus-two quotient, recomputes Weil polynomials, validates the Cartier coefficient formulas and the quartic's irreducibility, and confirms the elliptic exceptional isogeny type. Exhaustive finite enumeration establishes the nine-member marked census but is not presented as a proof of general assertions over algebraically closed fields. The character decomposition, group action, smoothness and semilinear Cartier-rank argument are written in RESULT.md. No independent audit has been performed.
