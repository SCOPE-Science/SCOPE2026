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

The proof is an exact three-state transfer-matrix calculation for every dimension \(n\ge3\). Its critical identities are \(N^3=I_3\), \(P^3\equiv I_3\pmod2\), \(P^2N\mathbf1=\mathbf1\), and the parity-even coordinate marginals when \(n\equiv2\pmod3\). The three explicit periodic signing families attain the claimed multiplier gaps; they are not inferred from a finite scan.

Run `python3 checker.py` (Python 3 standard library). It independently generates the admissible binary words, computes full integer fast Walsh transforms for dimensions 3 through 17, compares them against state-based direct signed sums on all masks through dimension 10 and selected additional masks through 17, and checks arithmetic lemmas and the gap witnesses. The expected final marker is `FORBIDDEN_001_SHARP_WALSH_PASS`. The finite scans support but cannot prove the infinite statement.

The source comparison includes accessible full-text HTML versions of arXiv:1402.6377 and arXiv:1501.00378, and bounded comparison with related mathematical records; a comprehensive historical-priority certificate is not asserted. No independent validation is reported.
