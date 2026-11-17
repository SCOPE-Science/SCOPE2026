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

# Verification and reproducibility

`check.py` is a standalone Python 3 program using only the standard library. Execute `python check.py` to reproduce sampled quotient fixed-point counts at odd periods 1, 3, and 5, a rational-coefficient quadratic example with two positive fixed points, and derivative checks on analytic realization families for three selected values of \(k\). All-period validity comes from the analytical crossing and primitive-cycle arguments, not these samples.

The numerical fixed-point finder uses a dense grid and bisection on the continuous quotient. It is not a certified root-isolation method and is not claimed to exhaust every periodic orbit outside the displayed examples. The analytic construction is proved for all sufficiently large \(K\) separately, rather than inferred from sample derivatives.

Scientific checks: the sign reversal is applied on regular orbits; no cut orbit is included; odd/even parity is handled separately; nonneutrality and nonperiodicity exclude crossing degeneracies; and the zeta relation is interpreted coefficient-wise.

Independent mathematical audit has not been performed.
