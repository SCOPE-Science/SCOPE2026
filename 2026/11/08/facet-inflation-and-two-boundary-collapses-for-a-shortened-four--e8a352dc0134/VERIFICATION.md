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

# Reproduction and limitations

Run `python verify_cycle_facets.py` from the directory containing this file. The standard-library checker enumerates all core-symbol configurations with exact `Fraction` arithmetic for `t=1/2,3/4,7/8`; it checks both tight-connected conditions, counts `A=26,38,38` and `B=15,27,27`, and evaluates the all-dimensional formula. It separately solves tight equations along all labeled spanning trees and both signs for `N=5,6` in the same three regimes, exhaustively checking all dual vertices. It also checks the equilateral endpoint.

The actual execution concluded `ALL_SHORT_CYCLE_FACET_CHECKS_PASSED`. Enumeration of small dimensions and discrete representative parameters is not a universal proof; the analytic symbol reduction and outside-point dichotomy support the theorem for all stated real parameters and dimensions. The program is intended for exact replication, not independent certification.
