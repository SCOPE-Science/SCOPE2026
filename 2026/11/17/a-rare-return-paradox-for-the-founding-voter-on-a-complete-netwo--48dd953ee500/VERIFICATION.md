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

# Verification and boundaries

The analytic proof computes the complete-graph tagged-pair disagreement ODE exactly, integrates its two components, and uses the distinguished site's terminal-state balance to identify both flip-count expectations. A separate gambler's-ruin and quadratic-supermartingale calculation proves the all-future probability bound for any upward return, and hence the nonuniform-integrability conclusion. No computation replaces these steps.

`verification/check_founder.py` implements a labelled-state CTMC and a separate two-count aggregation. Run `python verification/check_founder.py` with Python, NumPy and SciPy. `verification/check_founder.out` contains the observed stdout. Labels are retained in the full-state check. The cases \(n=2\) through \(9\) validate the mean and the zero-flip control, and cases \(n=3\) through \(17\) validate the upward-return upper bound. These finite checks do not establish the all-\(n\) result. The exact zero-flip probability is a prior-work-covered comparison quantity, not a new claim.

The rate convention is one copying clock per vertex per unit time, not one global copying clock. Counts ignore ineffective copying updates. The theorem applies only to a singleton positive founder, not arbitrary initial proportions. The rare-event upper bound need not be sharp. No independent mathematical audit has been performed.
