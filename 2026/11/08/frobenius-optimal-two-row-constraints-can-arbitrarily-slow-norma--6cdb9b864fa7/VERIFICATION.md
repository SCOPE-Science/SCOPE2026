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

# Reproducibility checks

All six rows have squared Euclidean norm one. Direct multiplication gives \(A^\top A=\operatorname{diag}(2c^2,2,2,2s^2)\). Every two-row set belongs to one of the four cases in `RESULT.md`; no computational search is needed to establish coverage. The limiting regime \(s\downarrow0\) is taken through positive \(s\), so no rank deficiency is introduced at finite parameters.

`verify_unitrows.py` requires Python 3 and `sympy` declared in `requirements.txt`. Execute `python -m pip install -r requirements.txt`, then `python verify_unitrows.py` in the extracted directory. The observed output is `PASS: exact spectra, all 60 constrained pairs, and 96 exact moment identities`. All checked arithmetic is rational for four Pythagorean parameter pairs: \((s,c)=(3/5,4/5),(5/13,12/13),(8/17,15/17),(20/101,99/101)\).

The script enumerates all fifteen pairs for each parameter, computes projector pseudoinverses, Frobenius residuals, positive spectra and contraction optima. It then replays exact second-moment recursion of the independent-selection dynamics and a separate conditional branching recursion rejecting zero residuals, at time indices zero through five. It verifies the specified exact expectation formulas for both constraint choices.

Finite symbolic/rational runs do not establish all real parameters or infinite-time asymptotics; analytic proofs in `RESULT.md` do. No independent mathematical or computational audit has been performed.
