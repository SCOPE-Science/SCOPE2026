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

## Exact reproduction

Run `python3 verify.py` with the files in this directory. The program uses only Python 3 standard library and a fixed deterministic seed. Successful output begins with `VERIFIED` and reports the number of checked laminar-support tuples and committee-count comparisons.

## Checked quantities

The verifier independently evaluates the claimed coefficient of the product of binomial polynomials and the count from direct enumeration of all size-\(k\) committees, testing their JR condition voter by voter. It also checks an eight-voter feasible election and the nonlaminar counterexample.

The exact-count computation is integer-valued: it uses Python integers and bit operations, not floating-point approximations. The universal proof relies on laminarity, residual JR and combinatorial counting, not on exhaustive finite testing. The asymptotic probability uses the classical central binomial coefficient asymptotic; the finite verifier does not constitute an infinite-limit proof.

## Boundaries

The code verifies only the enumerated finite ranges. Any claim about all election sizes rests on the analytic argument in RESULT.md. Source-priority comparisons and an independent scientific audit are outside the program's scope.
