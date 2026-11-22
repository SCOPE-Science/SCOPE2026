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

Run `python3 verify.py` from the package directory. The checker independently calculates prime-index defects by fast doubling, prime-power local congruences, and complete divisibility and positivity of the Möbius orbit transforms for bounded coefficient ranges. The expected output reports PASS for 27,540 prime-index identities, 25,920 local prime-power congruences, 7,680 positive integral orbit counts, and exact fifth-prime minimality for 96 sampled coefficient pairs.

The infinite proof requires Frobenius in the quadratic field, matrix binomial lifting, the Fibonacci–Lucas identity, and Dirichlet's theorem, none of which is established by the finite loop. The sharp multiplier depends on one explicit modulo-five identity. No external or independent mathematical audit has been carried out.
