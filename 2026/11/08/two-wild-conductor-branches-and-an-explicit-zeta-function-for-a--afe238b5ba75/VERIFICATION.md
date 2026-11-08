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

# Reproducibility and limits

Run `python verify_scroll.py` with Python 3 and SymPy installed. No external files or network calls are required. The recorded output is embedded in `verification_output.txt`.

The script reduces the two incidence syzygies and the twisted cubic's Jacobian containment to exact characteristic-two polynomial identities. It verifies the quartic equation and conductor equation, the four-partial-derivative smoothness argument, the separable quadratic coefficient, a local power-series expansion through order four at a wild branch, and the exact nonzero determinant of the eight-by-eight matrix that forces balanced splitting. It also independently counts the elliptic conductor and quartic points over four binary fields using explicit modular polynomial arithmetic, obtaining \((\#E,\#S)=(4,8),(8,22),(4,86),(16,290)\).

The general claims use standard geometry in addition to the executable: the graph-of-minors blowup, finite birational normalization, openness of smoothness and vector-bundle splitting, conductor duality on a smooth normalization of a Gorenstein quartic, the wild Riemann–Hurwitz different, and the Weil polynomial of an elliptic curve. Finite-field enumeration alone is not a proof for all extensions. The witness is a nonempty-open certificate, not a universal check for every conic.
