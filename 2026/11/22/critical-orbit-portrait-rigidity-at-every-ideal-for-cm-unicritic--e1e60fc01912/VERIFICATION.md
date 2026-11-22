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
# Verification of the critical-orbit ideal classification

The exact proof is in `RESULT.md`. Execute `python3 check_portraits.py` in an ordinary Python 3 environment; no external packages, network, downloads, or external data are required. The accompanying script constructs the dynamical orbit directly and tests quotient equality using divisibility in \(\mathbb Z\) and \(\mathbb Z[i]\).

Completed checks: 1,078 prime-power integer/Gaussian orbit cases, 484 composite Gaussian ideal cases, and 9,438 characteristic-prime finite-field instances of all cyclotomic branches through degree 120. The program reports a PASS line if every equality and portrait assertion matches its separately computed expected form. The Gaussian ideal-divisibility tests use rational primes through 101 and exponents through seven. The field cases cover primes through 97; these finite bounds are experimental checks only.

The mathematically decisive infinite steps are the complete CM-PCF parameter classification [Sano 2026], algebraic-unit differences for every higher-degree orbit, the explicit Gaussian valuations of the three exceptional differences in the quadratic case, and the exact \((\max,\mathrm{lcm})\) product rule for critical-orbit types under the Chinese remainder theorem. No finite enumeration is claimed to prove an unbounded statement. No external independent validation is claimed.
