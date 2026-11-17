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

The operator-valued positive-Herglotz criterion was applied to an exactly nilpotent three-by-three matrix. Direct expansion gave \(\det H=\rho^3-\rho(a^2+b^2)/t^2+(2-\rho)a^2b^2/t^4\). The principal minors were verified nonnegative at the claimed threshold using \(L\ge a^2,b^2,\rho ab\). The first-zero argument and strict product monotonicity establish all equality cases. These analytical steps establish the theorem for all admissible real and complex weights and all \(\rho>0\).

`CHECK.py` is a standalone Python standard-library diagnostic covering finite grids of \(\rho\) and weights. This check does not substitute for the analytic argument. Literature priority remains qualified, particularly because the 2003 truncated-shift paper's full text was inaccessible. Independent validation has not been performed.
