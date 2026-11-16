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

# Verification scope

`verify_hodge.py` is standalone apart from NumPy. Run with `OPENBLAS_NUM_THREADS=1 python verify_hodge.py`.
It assembles the two incidence matrices from the stated cell boundaries, checks the boundary-of-boundary identity, computes the full edge-Hodge spectrum for every `n` from 3 through 60 and three positive weight pairs, and compares with the closed Fourier formulas. It tests the exact two divisibility resonance equivalences, optimal gap balance and six/seven switch.

The program passed 22,272 individual comparisons. This finite numerical evidence does **not** certify the all-integer analytic theorem: the all-size implications are proven by the symbolic Fourier and cosine calculations in RESULT.md. Numerically close eigenvalues are never accepted as an infinite proof.

Historical-priority assessment uses relevant directly inspected full texts from 2021; an associated 2023 article was accessible only by abstract. Independent mathematical audit is not performed.
