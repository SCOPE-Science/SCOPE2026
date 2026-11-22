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
# Reproducibility and scope

Run `python verify.py` with Python 3.9+ and SymPy to reproduce the symbolic algebra and 16,000 supplementary finite-support comparisons. The exact rational case has \(a=1\), \(b=\sqrt{99}\), \(h=1/25\), and mixing \(H=0\) and \(H=2/25\) equally gives mean-square factor \(7/9\), versus \(25/31\) at deterministic step \(h\). An algebraic positivity identity, not numerical sampling, proves the bound for all admissible distributions. The result does not address fixed-time trajectory error, step-cost savings or independent validation.
