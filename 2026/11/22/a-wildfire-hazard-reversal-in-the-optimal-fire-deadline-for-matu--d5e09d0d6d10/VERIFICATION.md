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

# Verification of the fire-deadline result

The proof is analytical: the exact expected numerator and denominator give the derivative equation, its unique root, strict derivative signs and all degenerate boundaries. `RESULT.md` contains all hypotheses, definitions, quantifiers and proof steps. `check.py` is a standalone standard-library Python 3 script requiring no data files or packages.

The packaged script was run as `python check.py`; it reported **PASS: 91091 deterministic checks** and the illustrative root and rates. This run covers a deterministic 2,500-parameter randomized grid, first-fire integration cross-checks, comparisons to a spread of neighboring deadlines, monotonicity checks under variations of wildfire hazard, viability loss and maturity, and degenerate no-maturity/no-loss boundaries. Its seed is hard coded, and finite numerical tests do **not** establish continuous-domain uniqueness or global originality.

The exact example uses \(\mu=1/4\), \(\delta=1\), \(m=r=1\), giving \(T_*=2.251203073190526\ldots\), \(J(T_*)=0.286160317878394\ldots\), and \(J(\infty)=0.155760156614281\ldots\). Nonstandard lemmas (one crossing of the critical-point equation; monotonicity of the auxiliary function; zero-loss and zero-maturity limits) are derived explicitly in the proof. No empirical calibration, population-growth result or independent audit is asserted.
