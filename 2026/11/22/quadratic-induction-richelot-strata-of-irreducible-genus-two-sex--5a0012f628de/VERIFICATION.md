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

# Verification of the reported mathematical assertions

The general statement uses a symbolic six-cycle matching argument, a projective involution/pencil criterion, the two rational involution classes, and an explicit quadratic-character cancellation. It is not inferred from finite tests.

Three standalone Python 3 programs provide exact finite certificates, with no external dependencies: `check_richelot.py`, `check_trace.py`, and `check_weil_spectra.py`. Run them in the same directory. The first enumerates all degree-six monic polynomials over the fields with three and five elements and checks irreducibility and involution counts. The second verifies the predicted point counts over extensions of degrees one and three for every nonsplit member. The third calculates the complete degree-two point-count histograms and therefore all claimed Weil numerators in these two fields. Expected totals: 116 monic irreducibles and 12 nonsplit examples for size three; 2,580 irreducibles and 200 nonsplit examples for size five.

Scientific limits: the finite certificates do not prove the universal all-field assertions; the symbolic argument does. No other fields' complete Weil spectra are asserted. The quotient-versus-Jacobian distinction and the known invariant-polynomial counting theorem must be kept explicit. Independent validation is not part of these checks.
