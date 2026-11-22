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

# Reproduction and mathematical scope

Run `python3 verify.py` with Python 3, NumPy and SciPy. The script asserts the exact two-branch Laplacian spectrum, finite matrix power traces, optimality comparisons and scalar derivative identities, including independent asymmetric conductance trials. It also tests representative numerical large-graph ratios across the subcritical, critical and supercritical regimes. On the tested environment it reported `PASS 1401 finite diagnostics`.

The full universal proof is in RESULT.md. In particular: strict convexity establishes unrestricted uniqueness for all \(m\ge3,p>0\), cycle Fourier modes give the positive root equation, and the uniform low-frequency Riemann approximation with \(m\sqrt t\to\infty\) yields the three rigorous limiting regimes. Numerical samples cannot establish these quantified statements, spectral-order novelty, or publication priority. Only the described equal-price cyclic-prism family is covered. Independent audit has not been performed.
