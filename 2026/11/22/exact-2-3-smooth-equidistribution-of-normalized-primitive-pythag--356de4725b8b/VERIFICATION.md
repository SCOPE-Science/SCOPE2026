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

# Reproducibility and limits

Run `python3 check_area.py` with a standard Python 3 installation. The program independently exhausts dyadic, ternary and mixed modulus fibers; verifies the number of zero fibers over several odd primes; and checks finite hypotenuse-bounded triangle samples. An observed `CHECK_OK 41 test families` is an exact finite check, not a proof of the infinite theorem.

The unrestricted theorem follows from the local two-adic isometry, the ternary nonzero-gradient lifting property, the Chinese remainder theorem, the four projective zero lines at each prime at least five, and ordinary Möbius-inversion lattice-point counting in a circular sector. All definitions and error bounds occur in `RESULT.md`. No numerical certificate is assumed for the asymptotic formula. The literature check does not establish unconditional historical priority.
