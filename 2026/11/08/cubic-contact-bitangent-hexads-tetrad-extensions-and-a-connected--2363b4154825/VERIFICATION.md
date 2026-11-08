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

Run `python3 artifacts/verify_hexads.py` on the extracted artifact. The program uses only the Python 3 standard library and exact arithmetic, and it prints `VERIFY_OK` after all full-domain assertions pass. It generates all \(64\) quadratic-space vectors, all \(376740\) candidate six-subsets of \(28\) odd vectors, all \(20475\) four-subsets, and the full \(6048\)-by-\(6048\) cross-intersection census. It also independently constructs the exchange graph and checks its full connectivity.

The finite algorithm proves the indicated incidence numbers once the identification of the odd theta characteristics, conic syzygies, and cubic contact conditions with the quadratic-space model is established. The proof of those identifications is in RESULT.md and classical references. Running the checker does not constitute independent scientific certification. No higher-dimensional or real-curve generalization is claimed.
