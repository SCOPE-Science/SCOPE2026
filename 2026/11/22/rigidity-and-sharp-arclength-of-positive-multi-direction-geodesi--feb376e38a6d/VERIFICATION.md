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

# Verification scope
The exact Parseval proof is self-contained in `RESULT.md`: Fourier integration along a primitive geodesic, the uniqueness of perpendicular rational directions, Toeplitz moment factorization, and integer length/equality classification. The only computational artifact is `CHECKER.py`.

Run `python CHECKER.py` with Python 3 standard library. On the construction used here, the checker returned 51 complete numerical Gram examples with maximum deviation \(3.7595789382577486\times10^{-16}\) and exhaustive bounded integer-length/equality comparisons for \(N=1,\ldots,49\). The numerical matrix checks corroborate the theorem but do not prove its infinite quantifiers. Inaccessible specialist full texts remain an originality-priority limitation; no external independent audit was performed.
