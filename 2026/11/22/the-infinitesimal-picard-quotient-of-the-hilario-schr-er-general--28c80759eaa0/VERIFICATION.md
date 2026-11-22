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

# Reproducibility and scope

Running `python3 verify_ghost.py` requires only the Python 3 standard library. It returns one success line for each of the primes \(3,5,7,11,13\). The program independently computes the semigroup gap indices, the logarithmic-derivative coefficients from ordinary polynomial cocycles, the finite-order \(\alpha_p\)-coaction coefficients, Frobenius ghost identities, and the fixed-ideal generator pattern. It uses exact integer arithmetic reduced modulo each prime.

The general proof depends on the formal logarithmic derivative, invertible gap degrees, universal binomial identities, the height-one \(\alpha_p\) action, and the surface Picard splitting cited in RESULT.md. Checking finitely many primes does not establish universal validity, nor does it replace checking whether the cited primary results apply to the stated action.

The asserted group is the infinitesimal quotient of the connected Picard scheme, not the entire Picard group. The geometric base field is algebraically closed of prime characteristic at least three.
