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

# Reproducing the finite consistency checks

Run `python3 verify.py` with Python 3 standard library only. The script independently enumerates all positive elements of each conductor quotient, derives indecomposable generators by detecting decomposable nonzero sums, tests quotient sizes, and computes nilpotency classes directly. For a bounded subfamily it checks whether swapping the generators induces a bijective multiplication-preserving map. It also scans the strict monotonicity of the integer ceiling for admissible smaller generators at conductors through 2000. Expected output is saved verbatim in `verification_output.txt`.

## What the checks do not prove
The computations cover finite ranges only. The all-parameter classification follows from the inequalities and generator-normal-form argument in `RESULT.md`, not from the enumeration. Historical priority is not certified, and no independent audit has been performed. The theorem makes no claim about conductor quotients of numerical semigroups with three or more minimal generators.
