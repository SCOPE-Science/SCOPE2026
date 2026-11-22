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

# Reproducible verification

Run `python verify_cyclic_quintic_hasse.py` under Python 3 with SymPy 1.14 (or compatible). No network access, seed, external certificate, or unbundled data file is required.

The verifier reconstructs all coefficients of the three \(1\)-, \(2\)-, and \(3\)-dimensional unrooted Cartier blocks from the polynomial \(x(x-1)(x^2-sx+t)\), then checks their full determinant factorization over \(\mathbb F_{11}[s,t]\). It proves the reducedness of the Hasse support by polynomial gcd, and checks a unit Gröbner basis for the saturation of the ideal of vanishing entries of the middle block by the smooth-discriminant factor. These are exact polynomial identities, not experiments at a finite selection of parameters.

Separately, the verifier constructs \(\mathbb F_{121}\) as \(\mathbb F_{11}[i]/(i^2+1)\), exhaustively tests all \(14,042\) ordered admissible pairs, reconstructs the relevant Cartier blocks, tests semilinear stable rank, and computes the projective branch relabeling orbits using determinant cross-ratios. A second arithmetic implementation using \(\mathbb F_{11}[u]/(u^2-2)\) independently confirms \(210\) Hasse zeros. The script asserts all stated counts and finishes with `CYCLIC_QUINTIC_F11_HASSE_VERIFIED`.

The conclusion about nonordinary geometric support follows from symbolic identities on the full parameter ring. Quadratic-field enumeration proves only the explicitly listed quadratic-field counts; it is not used as a substitute for an infinite-field proof. No independent audit was performed.
