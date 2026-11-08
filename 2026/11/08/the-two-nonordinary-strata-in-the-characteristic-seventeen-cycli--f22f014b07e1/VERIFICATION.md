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

# Reproducibility

Run `python3 verify.py`. The supplied pure-Python script expands the defining powers using the binomial formula over the polynomial ring with coefficients modulo 17, reconstructs the full three Cartier coefficient blocks, and proves the coefficient and determinant identities by exact polynomial equality. It checks that the quadratic factor has no roots in the prime field and that its exceptional roots are distinct from the forbidden parameters.

Output observed: `CERTIFICATE_OK: characteristic 17, two exceptional inversion orbits; (p-rank,a)=(4,2),(2,4)`.

The stable Cartier rank is justified in the mathematical proof by an invariant direct-sum decomposition into an everywhere invertible two-dimensional summand and four one-dimensional summands that are individually either zero or invertible. The script does not verify every theorem of Cartier theory or independently validate historical priority. No independent audit has been performed.
