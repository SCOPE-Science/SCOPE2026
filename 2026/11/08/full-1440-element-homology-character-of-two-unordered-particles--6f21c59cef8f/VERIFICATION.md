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

# Reproducibility and verification

Run `python3 verify_configuration.py` beside `verification_output.txt` on Python 3 with no third-party dependencies. The program regenerates the finite graph from six labels, the complete cubical chain model, all signed boundaries, finite-field ranks modulo 2, 3 and 5, sixteen independent octagon homology generators, and exactly 1440 graph automorphisms. It checks signed cellular equivariance on every two-cell under every automorphism, computes all 1440 rational top-homology traces using the Hopf identity, and checks the exact irreducible decomposition for the canonical six-label permutation subgroup. Its successful recorded output begins `TUTTE_COXETER_TWO_POINT_CHARACTER_PASS` and reports the character-value counts 90:1, -6:75, 2:180, 0:1184.

The rational boundary-rank computation is justified by two inequalities: rank modulo 3 is 810, and 16 explicitly independent parked-octagon cycles give 16 independent images in first graph homology, hence rational boundary rank at most 810. This avoids incorrectly inferring rational rank from a single prime rank. The resulting free rank 90 of integral second homology uses freeness of the kernel of an integral homomorphism between free chain groups and the absence of cells above dimension two.

The signed Lefschetz character is for ordinary, not sign-twisted or Borel–Moore, homology. Integral first-homology torsion, the integral automorphism-module lattice, higher particle counts, and independent mathematical validation are not determined.
