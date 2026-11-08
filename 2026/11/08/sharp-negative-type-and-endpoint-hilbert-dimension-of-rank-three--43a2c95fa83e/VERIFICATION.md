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

The full mathematical argument is in `RESULT.md`. Run `python3 verify.py` with Python 3 (standard library only). Its successful marker is `BILINEAR_THREE_NEGATIVE_TYPE_PASS`.

The checker enumerates every matrix over \(\mathbb F_2\) for \(m=3,4\), every matrix over \(\mathbb F_3\) for \(m=3\), and every matrix over \(\mathbb F_4\) for \(m=3\). It checks the rank-by-rank additive Fourier coefficients against the closed formulas and separately verifies all frequency multiplicity identities. The \(\mathbb F_3\) check verifies exact conjugate character cancellation, while \(\mathbb F_4\) uses explicit polynomial-basis multiplication and trace characters. Additional cases validate root locations and integer identities. Those checks are finite only. The infinite family follows from the subspace transform and sign inequalities in the proof; no machine proof or independent validation is asserted.
