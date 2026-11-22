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

The independent scientific-audit channel is not yet performed. This package contains an analytic proof and a standalone finite-state checker `verify.py`.

Actual local run: `python3 verify.py` returned `FK_BOOK_EXACT_CHECKS_PASSED 258`. It uses exact rational arithmetic for all edge states when there are three to five pages, checks four positive cluster weights and three rational activities, and performs six distinct large-size critical-window sign spot-checks. The infinite-size threshold follows analytically from strict monotonicity and a logarithmic limit; these finite tests do not certify all sizes. 

No claim is made for heterogeneous edges, for infinite q, or for independently certified historical priority.
