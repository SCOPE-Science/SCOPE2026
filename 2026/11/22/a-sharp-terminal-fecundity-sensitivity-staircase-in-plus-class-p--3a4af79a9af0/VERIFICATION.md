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

# Verification details

The algebraic proof in RESULT.md is the correctness basis. The packaged `check.py` uses only Python standard libraries, a fixed random seed, bisection of the characteristic equation, analytic Perron-coordinate ratios and independent central finite differences. Replay command from the extracted package: `python3 check.py`.

The checker passed 10,685 numerical assertions, including randomized class sizes, the complete four-class fertility-crossing example, ratio identities and derivative comparisons. Floating-point tolerances are specified in code; these checks do not establish any infinite universal quantifier. Formal symbolic proof, uniqueness, equality and boundary cases are supplied in RESULT.md. Historical novelty is limited by the accessible works listed there. Independent audit has not been performed.
