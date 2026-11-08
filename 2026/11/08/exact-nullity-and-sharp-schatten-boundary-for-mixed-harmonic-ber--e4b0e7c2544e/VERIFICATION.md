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

# Reproduction and boundaries

The theorem follows from the exact monomial projection weights, strict gamma-moment log convexity, the reflected zero/positive tails, and a second-order asymptotic plus counting inversion. These analytical steps verify all infinite assertions without relying on computation.

Run `python3 CHECK.py` using the Python 3 standard library. The program checks a finite grid of degrees and radial weights, sign/zero interval, coefficient reflection, and approximate tail constants. It prints the number of assertions tested. It neither exhausts continuous weights nor establishes asymptotic assertions by itself. Independent mathematical audit has not been performed.
