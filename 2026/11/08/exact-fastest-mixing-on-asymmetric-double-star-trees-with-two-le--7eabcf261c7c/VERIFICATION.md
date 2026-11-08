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

# Reproduction and verification
Run `python VERIFY.py` in the directory holding the standalone files. It requires Python 3.9+ and no third-party libraries. The program carries out exact rational checks for \(n=6,7,\ldots,200,256,512,1000\). Each check separately verifies the stipulated weights and row capacities, the Rayleigh dual coefficient identity, the quadratic spectral interval, and agreement of a determinant computed by the Leibniz permutation formula with the asserted characteristic factorization at five rational evaluation points.

The proof for every integer \(n\ge6\) is in `RESULT.md` and does not infer universal truth from these finite tests. No external expert or independent audit has been performed. The independent audit status is explicitly unperformed.
