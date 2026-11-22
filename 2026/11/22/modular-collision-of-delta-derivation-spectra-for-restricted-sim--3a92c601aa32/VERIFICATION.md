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

The accompanying `verify_delta.py` implements Gaussian elimination over the prime field directly on the full coefficient matrix obtained from \([e,f]=h\), \([h,e]=2e\), and \([h,f]=-2f\). It does not use the block decomposition in the proof. Run `python3 verify_delta.py`; the observed exact output is `MODULAR_SL2_DELTA_SPECTRUM_OK 1023`.

For every \(p\in\{3,5,7,11,13,17,19\}\), it checks every \(0\le m\le p-1\) and all \(\delta\in\mathbb F_p\). This is a finite cross-check only, not a proof for other characteristics or field extensions. The theorem for all odd-characteristic fields follows from the exact determinant and rank calculations printed in `RESULT.md`.

The code and formulas do not claim external certification or independent mathematical validation. Historical novelty is provisional, with the earlier characteristic-zero and ordinary positive-characteristic results explicitly credited.
