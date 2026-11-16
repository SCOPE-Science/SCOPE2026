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

# Verification and reproducibility

Two standalone checks are included. Run `python verify_fft.py 7` for an exhaustive exact transform over all \(3^{2n-1}\) balanced frequency classes at each rung count \(1\le n\le7\). The program stores Eisenstein coefficients as ordered integer pairs, uses ternary Fourier butterflies, and asserts the closed rank formula. Run `python verify_direct.py` to enumerate every anchored proper colouring directly, count the three phase residues independently, and check **each individual Fourier-zero decision** against the endpoint criterion for \(1\le n\le5\). Both programs require Python 3 and NumPy and succeeded locally.

The proof's infinite-order conclusion depends on the displayed rank-one transfer identity, the \((1-\omega)\)-adic endpoint lemma and the modulo-prime nonvanishing of interior connectors; finite enumeration alone cannot certify it. External historical priority and an independent audit remain unperformed. The code makes no attempt to verify the literature beyond the documented comparisons.
