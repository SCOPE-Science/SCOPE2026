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

Run `python verify.py` with Python 3.9 or newer in the same directory as the other research files. The checker uses only Python's standard library and performs exact-formula numerical bracketing of the optimal reset rate for multiple drift magnitudes and finite trap strengths, including the reactivity-neutral parameter. The recorded run passed 534 deterministic numerical consistency assertions and found \(u_c=1.294952188188740\ldots\), \(m_c=0.464240177926471\ldots\), and \(s_c=1.461382226893605\ldots\).

The script checks the stationarity equation, representative global-mean comparisons, strict optimizer orderings, and critical-value independence to floating-point tolerance. It is not a computer proof of the infinite-parameter theorem. The analytic uniqueness, sign continuity, root uniqueness and boundary arguments are in RESULT.md. An independent scientific audit has not been carried out.
