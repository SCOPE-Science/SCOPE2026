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

Run `python3 checks/matrix_certificate.py` and `python3 checks/labelled_evolution.py` from the directory containing this document. Both programs are standalone and use only the Python standard library; recorded outputs are in `checks/verification_output.txt`. These programs were executed against the delivered source content, not unrelated scripts.

The matrix program checks a separately implemented finite-field polynomial determinant for the characteristic-polynomial identity at fan lengths 2–14, verifies every nilpotent rank drop and its stabilization at lengths 2–96, and checks fixed-eigenspace dimensions for resonant lengths 3, 7, 15, 31 and 63. The labelled simulator builds the graph update independently and checks all 8,184 binary initial configurations at lengths 2–11, including the periodic orbit census at length 7.

These finite checks are not a proof of the infinite family. The proof uses exact path-matching factorization, an explicit kernel/image separation and the Fitting decomposition; it applies to all finite characteristic-two fields. The priority status is qualified and not externally audited.
