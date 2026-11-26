---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks and limitations

The supplied `check.py` uses Python 3 and its standard library. Its expected output is `PASS 1896 numerical assertions`. This is a reproducible finite diagnostic, not an exhaustive proof for all odd integers.

The numerical tests cover \(N\in\{3,5,7,9,11,17,31\}\) and nine noncolliding displacement parameters (including \(\delta=1/2\)), evaluate Fourier moments for every mode in the band, check all quadrature weight signs and the two-dimensional Gram reduction, and compare the exact bounded-sample amplification. The collision-layer tests use \(N\in\{51,101,501,1001\}\) and three fixed positive scales. The all-integer proof in `RESULT.md` uses cardinal interpolation, circular-distance sine comparisons, the Gram decomposition and small-angle limits.

At the excluded endpoint \(\delta=1\), the Dirichlet kernel vanishes at every sample location but has normalized integral one, so no exact quadrature rule using these samples exists. The joint limit has fixed positive \(t\) and odd \(N\to\infty\). The comparison with Chen, Lin and Zhang in `RESULT.md` uses the accessible v4; publication priority remains unconfirmed.
