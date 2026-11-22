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

# Reproducible checks and limitations

Run `python check.py` with Python 3 and its standard library. It prints `PASS 1896 numerical assertions` when all checks pass. This is a reproducible finite diagnostic, not an exhaustive proof for all odd integers.

The numerical tests cover \(N\in\{3,5,7,9,11,17,31\}\) and nine noncolliding displacement parameters (including \(\delta=1/2\)), evaluate Fourier moments for every mode in the band, check all quadrature weight signs, check the two-point Gram spectral identity, and compare the exact optimal bounded-sample amplification. The collision-layer tests use \(N\in\{51,101,501,1001\}\) and three fixed positive scales. The proof in `RESULT.md` supplies infinite-domain validity by cardinal interpolation, circular-distance sine comparisons, a two-dimensional Gram decomposition, and small-angle limits. Neither the numerical checks nor this review constitute independent validation.

The singular collision \(\delta=1\) is excluded. The joint limit has fixed positive \(t\) and odd \(N\to\infty\). The complete manuscript of one closely relevant 2026 source was not available, so priority remains unconfirmed.
