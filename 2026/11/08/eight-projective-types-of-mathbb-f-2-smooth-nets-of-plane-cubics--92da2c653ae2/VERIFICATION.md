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

# Reproduction and limits

Execute `python verify_smooth_cubic_nets.py` with SymPy 1.12 or newer. The checker was executed against the standalone file and printed `SMOOTH_NET_CLASSIFICATION_PASS 336 5544 864 8` after asserting counts, complete orbit sizes, stabilizers, eight basis representatives and rational-point spectra. It also compared exact ideal tests to all derivatives on projective points over extensions of degrees 1 through 4. The latter finite-extension exercise is an independent cross-check only, not a general geometric-smoothness proof. The proof instead rests on exact Gröbner ideal dimensions in the algebraic closure.

Eight basis triples and coefficient-mask monomial order are displayed in `RESULT.md`. The classification does not assert new existence or sharpness of projective dimension (already established in Asgarli–Ghioca–Reichstein). It is restricted to binary ternary cubics and equivalence over the binary ground field. No independent audit was conducted.
