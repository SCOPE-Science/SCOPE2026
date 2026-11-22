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

# Exact verification and limits

Run `python3 verify.py` with Python 3 and its standard library. The code uses rational-number first-order dual arithmetic to rederive the equilibrium, reaction and flux Jacobians from the nonlinear formulas, then verifies the exact dispersion polynomial and handling-diffusivity threshold.

The mathematical certificate for all higher modes is the symbolic inequality \(90000P'_w(q)\ge49600w+1307>0\) for every \(w>0\) and \(q\ge1\), together with \(P_w(1)=(9850w+803)/45000>0\). Finite tests in the checker are supplementary, not the basis for the infinite-mode statement. The witness with equal effective diagonal diffusion entries is checked by exact fractions.

No nonlinear bifurcation calculation, global dynamics, empirical validation or rigorous mesoscopic-to-PDE convergence is claimed. The 2019 closely related full text was not accessible for a complete priority comparison; related general results and the source paper's explicit distinction in the demographic terms were used for the stated literature-bounded originality assessment. Independent scientific audit has not been performed.
