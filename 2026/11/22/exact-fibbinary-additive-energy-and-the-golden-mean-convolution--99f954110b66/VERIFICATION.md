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

The standard-library checker `CHECK.py` reconstructs the twelve reachable carry states directly from the four-digit rule and checks the exact integer polynomial identities 
\[
(M^5-2M^4-6M^3+M^2+4M-2I)v=0
\]
and
\[
\det(tI-M)=t^2(t-1)(t+1)^2(t^2-2)(t^5-2t^4-6t^3+t^2+4t-2).
\]
It also directly compares the recurrence with brute-force pair-sum histograms for every depth from zero through eleven and evaluates the parity of the first 257 proportional binomial coefficients. Run `python3 CHECK.py`. The observed result is `CHECK_OK 353 assertions; 12 reachable states; E_0..E_11 verified`.

These finite checks are not used to infer infinite claims. The all-depth energy follows from an explicitly specified finite-dimensional matrix annihilation. The positive Perron eigenvalue governs its growth because the reachable graph is strongly connected and aperiodic. Cylinder-weight comparability and a two-cell tail argument prove the continuous correlation exponent and the lack of a square-integrable density. No independent audit or general density-classification theorem is claimed.
