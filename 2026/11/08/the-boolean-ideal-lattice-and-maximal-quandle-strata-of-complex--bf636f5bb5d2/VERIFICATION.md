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

# Computational and symbolic verification

The proof in RESULT.md is a universal symbolic argument. Its critical steps are (1) the exact Fourier multiplication identity, (2) reciprocal/square phase propagation, (3) the induced \(s^2/r\) law, (4) the right-translation surjectivity argument for maximal quandles, and (5) the square-root reachability argument for ideals. All hold for any finite abelian odd-order group over complex coefficients.

Execute `python verify_magma.py` under Python 3. The checker creates roots of unity in finite fields large enough for the tested groups, uses Fourier inversion to generate vectors, and multiplies them directly using the defining quandle basis structure constants. It checks idempotency, every predicted pair product for small cases, selected pair products for larger groups, and the support strata. For group orders one, three and five it enumerates *every nonempty subset* and independently tests the two-sided-ideal condition. The exact output is in `verify_magma_output.txt`; all tests passed.

Finite-field trials do not certify the complex theorem by themselves, and do not claim to exhaust arbitrary finite abelian groups. No independent mathematical audit has been performed.
