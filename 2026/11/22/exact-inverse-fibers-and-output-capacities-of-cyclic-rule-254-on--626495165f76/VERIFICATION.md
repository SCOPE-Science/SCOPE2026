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

# Reproducible checks and scope

Use `python3 verify.py` with Python 3 and the standard library. The script separately enumerates admissible inputs, constructs the observed output fiber dictionary, computes the proposed product formula and three forbidden-word test for **every** binary output, and derives the two rational-series coefficients via polynomial recurrences on all cyclic lengths 1 through 18. It prints `VERIFY_OK` only when every assertion passes. Tests succeeded on the supplied script.

The input restriction includes wraparound; with a one-site ring only the zero input is admitted. Run lengths in the product formula are maximal cyclic runs in nonconstant outputs. This check does not exhaust arbitrarily large rings and is not a substitute for the full run-chain and rooted-cycle proofs in `RESULT.md`.

The all-one preimage Perrin recurrence is classical; reproduction of that count is not a priority claim. Rational generating functions concern distinct **indexed cyclic outputs**, not output necklaces or number of inputs. The all-length asymptotics require the primitive renewal singularity argument, not numeric extrapolation. No external independent mathematical assessment is claimed.
