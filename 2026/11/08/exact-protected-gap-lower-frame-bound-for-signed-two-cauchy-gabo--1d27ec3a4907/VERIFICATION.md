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

Run `python3 check_two_cauchy.py`. The executed standard-library checker returned `TWO_CAUCHY_PROTECTED_GAP_CHECKS_PASS 154988 cases 139`. It verified exact symbolic identities by direct arithmetic, sampled 139 sets of pole ratios with a nonempty protected gap, tested five residue choices and a grid of Zak variables for each, checked both claimed endpoint fibers, checked the unique max-min coefficient, and compared three single-pole closed-form Zak values with truncated Fourier series. The finite grid cannot prove absence of exceptional interior minima; this is proved by the concave-quadratic lemma in RESULT.md.

A source overlap comparison examined the open-access original text of Belov–Kulikov–Lyubarskii's rational Cauchy frame study, including the explicit already-announced qualitative two-kernel classification, and the available abstract/introduction of their one-pole frame-operator study. The sharp signed two-pole lower bound is the claim reviewed here. No independent audit or external validation has been performed, and publication priority is not guaranteed.
