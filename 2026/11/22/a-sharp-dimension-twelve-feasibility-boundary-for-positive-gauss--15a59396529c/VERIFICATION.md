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

# Reproducible checks

From the same directory as the included source, execute `python3 verify_cube_pade.py`. Python 3 and the open-source SymPy symbolic algebra library are required. The program uses only exact integer and rational arithmetic for the certificates and reports:

`VERIFY_OK exact_checks=116; Q12_positive_at_1/3; Q13_all_h_obstructed`

It checks thirteen rational shells and their positive common-denominator integers for the twelve-cube; the full polynomial identities and Sturm variations for distances seven, thirteen and one in the thirteen-cube; and the exact coefficient of the order-seven small-step obstruction. Several lower-dimensional rational tests are supplementary.

To independently reconstruct the whole infinite-dimensional theorem, use the Walsh shell identity and the exact Sturm-sign checks in `RESULT.md`. Marginalization proves the reduction from all dimensions to the twelve-cube witness and thirteen-cube obstruction. A positive finite sample does not establish an infinite-step assertion: it is the Sturm root exclusion, not sampling, that controls the whole positive real axis.

The certificates do not test internal Runge–Kutta stages, finite-precision error, nonuniform conductances, or other integration schemes. Independent mathematical audit: not performed.
