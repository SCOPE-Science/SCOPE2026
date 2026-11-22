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

# Reproducible mathematical checks

Run `python3 verify_bipartite.py` in the directory containing these files. Python standard library only; the script reports 313 passed checks covering two exact-rational balanced cases, positive-equilibrium residuals, fold identities, determinant signs on both sides of the saddle-node for \(m,n\) samples and real \(d>1\), and large-star leading-constant approximations.

The analytic argument in RESULT.md establishes the classification for **every** integer \(m,n\ge1\) and real \(d>1\). The finite numerical checks do not establish that universal assertion; in particular, root bisection and floating-point comparisons are tests rather than proof certificates.

The principal external scientific inputs are the published node-level model equation and its stated domain. Assertions about originality are restricted to the cited and materially inspected documents. No independent audit or independent mathematical validation is claimed.
