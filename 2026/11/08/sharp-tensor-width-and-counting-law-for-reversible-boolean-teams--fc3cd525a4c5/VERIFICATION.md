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

# Finite verification

Run `python3 checker.py` with standard Python 3. The checker independently searches for the least number of reversible-dependence pieces by assigning every team element a piece label and testing all dependence atoms on each piece. In dimensions two and three it exhausts all Boolean teams, checks the antipodal-width formula, the joint size/width count, the two local bounds, and the iff extremizer criterion. It also verifies the even-parity sharpness construction in dimensions three through eight.

These checks test a finite portion of the hypotheses. The theorem for all dimensions follows from the argument in `RESULT.md`, not from program termination. Results about novelty and generalization to non-Boolean domains are not verified computationally. No independent audit has been performed.
