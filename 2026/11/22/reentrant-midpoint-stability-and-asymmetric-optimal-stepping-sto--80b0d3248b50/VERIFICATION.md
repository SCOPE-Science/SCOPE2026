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

## Reproduction

Run `python3 CHECK.py` with Python 3 using only its standard library. It verifies exact polynomial evaluations, the rational strict comparison, the stationary-polynomial identity on supplementary rational inputs, and numerical root brackets. Expected terminal line begins `ASSERTIONS_PASSED 1169` and the two global maximizers are approximately \(0.626292211822\) and \(13.373707788178\).

## What is proved and what is checked

The universal one-scale optimizer classification and the three critical midpoint-stability changes follow by calculus and cubic root isolation in `RESULT.md`. The complete five-stationary-point classification at total length \(14\) follows from the sign pattern of a cubic, positivity of its denominators and an exact rational inequality. These analytical steps, not the finite checks, establish continuous-range assertions. The Python file tests the formulas independently over representative rational inputs and reports numerical roots for readability.

## Limits

No empirical movement-kernel fitting, ecological effectiveness assessment, or independent scientific validation has been performed. The numerical checks do not certify arbitrary continuum claims by enumeration. The theoretical assertions do not include a full classification of global optimal placements at every corridor length.
