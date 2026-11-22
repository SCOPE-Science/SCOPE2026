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

# Reproducibility and scope

The bundled `verify_area_spectrum.py` is a Python 3 standard-library-only checker. Running `python verify_area_spectrum.py` reconstructs all vertex coordinates, enumerates the known facial triples, computes integer \(4\operatorname{Area}^2\) values, checks the entire expected multiset for each order \(3\le n\le12\), confirms the established total two-face count, and verifies area-four square diagonals. Expected output: `COSMO_CYCLE_FACE_AREA_EXACT_PASS n=3..12`.

The analytic proof of the all-order result is in `RESULT.md`, with the published face criterion as an explicit premise. The finite checks do not provide an infinite certificate. The coordinate embedding is fixed, and any affine change not preserving its Euclidean metric may change the areas. Historical priority is provisional. Independent audit has not been performed.
