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

# Reproducibility and verification

Invoke `python verify.py` in the extracted directory; this requires only the Python standard library. It reports 93 finite deterministic diagnostic assertions. The test independently enumerates complete-run paths and compares a correlation-series calculation across multiple turn angles and independent renewal distributions, tests large-run second-moment slopes, verifies the exact symmetric two-point jitter identity and its \(\sigma\downarrow0\) scaling, tests resonant ballistic and nonresonant bounded deterministic cases, and recovers the exponential-run expression.

The theorem is proved by a bounded martingale coboundary, optional stopped quadratic variation and the elementary renewal theorem, followed by an exact phase-lattice geometric sum. The computational tests do not prove these asymptotic steps. In particular, finite path enumeration cannot by itself certify long-time ballisticity or diffusivity, and no process-level central limit theorem is asserted.

Review of mathematical reasoning and these computations was conducted for this package only. Independent audit has not been performed.
