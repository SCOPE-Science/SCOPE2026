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
# Verification and its limits

The proof is contained in RESULT.md; this document records checks of the original equations, not an independent proof. Run `python3 check.py` with Python 3. The script enumerates the complete derivation normal form in dimensions three and five, checks \(D^2=D\), tests the original Leibniz condition for every basis pair, determines ranks by row reduction, and compares the histogram against the symplectic and general-linear group-order formula. It does not assume the derived normal-form classification as an acceptance condition: it reconstructs candidate operators from all allowed coefficient matrices and verifies their defining equations directly. Preservation of the center by any derivation is independently proved in RESULT.md.

Recorded checked configurations: \((n,q)=(1,2),(1,3),(1,4),(1,5),(2,2)\). The output is `check_output.txt`, ending with `HEISENBERG_IDEMPOTENT_DERIVATION_ORIGINAL_LEIBNIZ_AND_RANK_OK`. The script explicitly implements extension-field arithmetic for \(\mathbb F_4\), and the field multiplication was separately tested for distributivity and associativity.

Only the reduced geometry is asserted. Finite enumeration is not an infinite proof. Historical priority is provisional, and independent review has not been performed.
