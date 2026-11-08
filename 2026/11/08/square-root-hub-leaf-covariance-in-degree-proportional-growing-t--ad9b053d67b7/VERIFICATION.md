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

# Verification

The theorem is proved by conditional expectations, exact summation, and asymptotics in `RESULT.md`. The accompanying `verify.py` is a standard-library-only checker, replayed successfully from the present artifact set.

Run `python3 verify.py` in the directory containing this file and `RESULT.md`. The program checks all attachment histories through nine vertices by exact rational probabilities, compares four moments at every size, replays the closed recurrences through 90 vertices, and evaluates long-size asymptotics through 100,001 vertices. Its output was `PASS 132 assertions` with diagnostics (size 100001): covariance divided by square-root size about `0.37344546`, root-degree variance divided by size about `0.72318816`, leaf variance divided by size about `0.11111001`, and square-root-size-scaled correlation about `1.31742210`. The corresponding proven limiting values are \(2/(3\sqrt\pi)\), \(2-4/\pi\), \(1/9\) and \(\sqrt{2/(\pi-2)}\).

The finite verifier is not an exhaustive proof for arbitrary \(n\). It does not establish publication priority or independently certify the result.
