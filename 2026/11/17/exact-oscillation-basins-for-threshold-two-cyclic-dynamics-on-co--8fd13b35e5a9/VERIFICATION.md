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

# Reproducibility

Run `python3 finite_certificate.py` and `python3 full_state_check.py` using Python 3's standard library. Corresponding exact outputs are included as `finite_certificate.out` and `full_state_check.out`.

The first script exhaustively checks 729 capped initial population signatures, proves the four-update/global three-shift identity under the clipping lemma in `RESULT.md`, and verifies all 31 polynomial coefficients of the four-term generating function. The second script uses direct labelled vertex updates for 752,877 initial states across 45 graph sizes and independent exact rational coefficient extraction. It checks eventual least periods, entrance-time bounds, and attraction-basin counts.

Finite direct simulation alone would not prove a statement for arbitrary graph sizes; the symbolic clipping reduction is the essential infinite-family step. Neither verification uses an external proof assistant or claims independent certification.
