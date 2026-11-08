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

Run `python3 verify.py` using Python 3's standard library. A successful run prints `VERIFY_OK 4699`. The program checks full rational Laplacian/projector identities, independent inverse-trace calculations, finite rational optimum comparisons, and the Karush–Kuhn–Tucker edgewise sign rules. No numerical tolerance is used for the exact-rational assertions. This is a finite verification suite and is **not** a replacement for the proof for all \(m,c,B\) in `RESULT.md`.

The general proof uses strict convexity of the inverse-trace objective, concavity of the spectral gap, group averaging, and an exact spectral decomposition. The displayed critical-window limits follow from algebra rather than checked finite sizes. No independent audit has been performed.
