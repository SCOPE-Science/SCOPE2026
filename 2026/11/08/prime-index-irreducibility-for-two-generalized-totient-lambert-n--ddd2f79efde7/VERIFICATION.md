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

# Verification of prime-index numerator irreducibility

Run `python verify.py` using Python 3, with no third-party packages. The script reconstructs \(S_p\), \(P_p\), \(H_p\), and \(Q_p\) as lists of exact integer coefficients. It independently computes the original companion expression \(P_p(X)(1+X^p)^2-2XP_p(X^2)\) and the proposed factorization \((1+X^2)H_p(X^2)\), and checks equality coefficient by coefficient. It checks the full list of shifted coefficients of \(P_p\) and \(H_p\) for the Eisenstein divisibility conditions; it also checks \(H_p(-1)=1-p^2\) for primes congruent to \(3\pmod4\).

Observed output:

```
VERIFY_OK primes_2..47=15 p_congruence_three_mod_four=8 identities=PASS shifted_Eisenstein=PASS negative_root_sign=PASS
```

Additional symbolic irreducibility checks of \(P_p\), \(H_p\), and \(H_p(X^2)\) at \(p=3,5,7,11,13\) agreed with the mathematical statement, but were not used in its proof. For \(p\equiv1\pmod4\), the script does not assert an unrestricted irreducibility result for \(H_p(X^2)\). The proof for all eligible primes is symbolic: the finite checks alone cannot prove an infinite assertion. The published original derives the numerator identities; the argument here independently derives and verifies the specialized identities and all necessary hypotheses.
