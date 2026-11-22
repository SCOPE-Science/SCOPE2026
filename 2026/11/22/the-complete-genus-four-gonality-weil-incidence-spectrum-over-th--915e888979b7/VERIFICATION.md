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

The included standalone reproductions were executed from the packaged source versions:

- `python3 verify_gonality_census.py weil_gonality_certificate.hex` yielded `GENUS4_F2_GONALITY_WEIL_INCIDENCE_VERIFIED`, with 620 Weil classes, 1,044 curves and gonality counts 264/526/253/1.
- `python3 verify_explicit_witness.py` yielded `GENUS4_F2_THREE_GONALITIES_SAME_ZETA_VERIFIED`, with extension-count rows (1,1,1), (5,5,5), (10,10,10), (17,17,17).

The first program optionally accepts the originally published Magma source as its second argument, to compare all 620 compact records with the original text. This optional comparison is provided for reproducibility and was not separately executed from a local source copy; the source was directly read in its accessible repository representation for constructing the compact certificate. Completeness of the original curve census is cited, not independently reproduced. This is not an independent mathematical audit.
