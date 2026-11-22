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

# Verification

The closed-form spectral gap is proved by an analytic rank-one operator comparison. The included `verify.py` checks the generator's every allowed edge for the selected finite instances, detailed balance against the conditioned Bernoulli product measure, and the proposed eigenfunctions with exact fractions. The exact checks cover 61,254 directed edge comparisons for integers \(2\le n\le9\) and the values \(\sqrt{1-q}\in\{1/2,2/3,3/4\}\).

Symmetric finite-generator diagonalization additionally tests the first positive eigenvalue at 21 pairs of parameters \(1\le n\le7\) and \(q\in\{1/8,1/2,7/8\}\), including the one-leaf exception. The finite calculations support, but do not replace, the proof for all real \(0<q<1\) and all integers \(n\ge2\).

Reproduce with `python3 verify.py`; the exact part needs Python alone, while the optional spectral check needs NumPy and SciPy. The standard chain is restricted to at least one vacancy. No check here constitutes an independent scientific audit or definitive assessment of historical priority.
