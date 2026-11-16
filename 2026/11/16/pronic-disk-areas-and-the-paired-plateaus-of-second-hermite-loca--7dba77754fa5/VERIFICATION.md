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
# Reproducibility and checks

The attached `verify_pronic.py` requires Python 3 and SymPy and uses exact symbolic/rational arithmetic. It independently reconstructs the incomplete-gamma antiderivatives for 44 normalized Hermite-index spectrogram densities and verifies 43 exact adjacent-gap expressions; it symbolically checks the polynomial identity with index treated as a variable, then tests five pronic disks and 15 nonpronic thresholds.

Expected output:

`H2_PRONIC_ORDER_PASS universal_polynomial_identity=1 exact_integral_levels=44 exact_neighbor_gaps=43 pronic_areas=5 nonpronic_radii=15 double_triplet_area=2`

The verifier is finite except for a universal algebraic polynomial identity. The statement for all indices and radii additionally uses the analytic sign, interval and integer-root arguments written out in RESULT.md. No third-party article or specialized certification software is bundled or asserted as independent proof.
