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

# Verification record

Run `python3 verify_tours.py` using the Python standard library. It exhaustively lists all 12 ternary cycles using a distinguished first edge, validates all their length-four windows, and performs exact Bareiss tree-count calculations for alphabet sizes 3, 4, 5. Expected terminal marker: `TOUR_AND_BAREISS_VERIFY_OK`.

Run `python3 verify_spectrum.py` with Python 3 and the SymPy package available. It computes the outgoing Laplacian and compares its full exact characteristic polynomial, root arborescence determinant, and cycle count with the theorem for alphabet sizes 3, 4, 5, 6. Expected terminal marker: `SPECTRUM_VERIFY_OK`.

These programs were executed and passed from the actual supplied source text. The infinite-family theorem additionally requires the structural proof and cannot be inferred solely from the finite computations. Publication priority and all other possible shorter-window or longer-window variants are not certified.
