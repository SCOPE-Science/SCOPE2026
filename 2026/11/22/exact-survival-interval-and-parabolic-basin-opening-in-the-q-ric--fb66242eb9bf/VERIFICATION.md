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

# Reproducibility and scientific limits

Run `python3 verify.py` with Python 3 standard-library modules only. The script checks normalized map identities and fixed-point/preimage relations for a legitimate parameter slice \(k=3/2\), plus qualitative basin samples, the asymptotic fold time constant and the first basin-width correction. A successful run prints `PASS` together with the numerical threshold and equilibria. These are finite diagnostic tests, not a machine proof of the full theorem.

The infinite-orbit statements follow from the elementary analytic derivations in `RESULT.md`: global trapping, strict increase on the trapping interval, the single maximum of \(G(t)/t\), monotone convergence to fixed points, Taylor expansion at the neutral fixed point, and an implicit inverse-branch expansion. The all-parameter proof is written independently of the finite diagnostics.

Scientific source inspection comprises the published original article's abstract and dated metadata, the full publicly available Chapter 2 of the originating authors' thesis, and the abstract of the earlier Allee-type Ricker paper. No independent specialist audit or formal verification has been performed, and the unavailable complete original journal text remains a priority limitation.
