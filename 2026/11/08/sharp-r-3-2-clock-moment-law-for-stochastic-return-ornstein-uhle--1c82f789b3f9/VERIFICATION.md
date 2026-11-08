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

Analytical checks: differentiate \(K\) to verify \(K'(x)=1+k_2xK(x)\) and hence \(\mathcal L_2U=-1\); verify \(F''(0)=2\) for \(F(x)=xK(x)\). Stopped Dynkin's formula plus return hitting probabilities gives the exact identity \(M_r-M_2=(k_1-k_2)A_r/p_r\). The high-rate expansions are controlled by a Gaussian small-time estimate and the finite second moment of the independent positive clock variable. Bound the direct search-hit probability by a constant times the square of the clock duration.

Executable checks: run \(\texttt{python CHECKER.py}\) using Python 3, SciPy and NumPy. The script computes the exact absorbing Brownian heat-kernel/resolvent integrals for \(k_1=0,k_2=2\), verifies the independent renewal expression versus the potential identity at four clock rates, and tests the asymptotic moment-ratio constants for exponential, deterministic and two-point reset distributions. The numerical script was executed successfully with a PASS result. This constitutes finite-precision evidence, not a substitute for the arbitrary-clock proof.

Limits: no finite-rate universal ordering, no uniformity over stiffness or clock laws, and no infinite-dimensional extension are asserted. Independent audit has not been performed.
