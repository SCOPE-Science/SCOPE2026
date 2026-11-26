---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

I reconstructed the all-prime and all-polynomial argument, not just the monomial tests. Euler exponents are (1/n)∑_{d|n} μ(n/d)P(U_d), so their integrality is equivalent to the stated prime-power congruences by Möbius inversion and factoring off each p-part. The ghost sequence tr((M²)^n) has integral Euler exponents by det(I−xM²)^−1; cancelling 8 against odd prime powers in 8U_n²=V_{2n}−2(−1)^n proves sufficiency at odd primes for every even weight. At 2, V_n≡2 mod 4 and doubling give v₂(U_{m2^r})=r for odd m, making r=1 exactly the parity obstruction. Conversely, infinitely many inert odd primes send U_{mp} to −U_m; for each fixed m, integrality forces P(−U_m)=P(U_m) over Z, hence evenness. The equivalent polynomial normal form follows by division by Y−1. For an even weight, clearing denominators in the Binet expansion and pairing conjugates gives the stated rational power. At the root associated with α^{2j₀}, the largest index attaining the maximal positive denominator deficit contributes an odd valuation after clearing; smaller indices cannot hit this root, and larger ones contribute even valuations. With D the stated power of two, extending that valuation gives v(E_P)=odd/D; the ramification index is divisible by D, forcing degree D even over Q(√2)(x), and any rationalizing exponent is divisible by D. Constants and H=0 give rational series. For a nonzero odd part the highest odd exponent contributes an uncancelled irrational log-derivative residue at x=α^{−d}; local Puiseux orders of algebraic functions are rational. The monomial product follows by conjugate pairing; its smallest multipliers follow from the parity test. Replay: RESULT.md §§1–7; checker.py was read, not run, and its finite coefficient and ghost tests do not prove the degree or universal claim.

## originality

PASS

Best-of-knowledge pass for the all-polynomial ordinary Pell criterion and exact degree, including the conjectured all-k monomial integrality families. Neither the general tools nor the close Fibonacci analogues inspected give the Pell dyadic criterion or its exact spectrum. The exact index self-hit does not establish prior coverage.

## value

PASS

The theorem settles three concretely stated Pell monomial conjecture families and determines exactly which arbitrary polynomial combinations survive the dyadic obstruction. The precise ramification/degree exponent remains useful when spectral factors from distinct degrees coincide; it determines whether an algebraic Pell exponential is rational and the exact rationalizing power. These are more than reproducing the first few coefficients or making the Fibonacci parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
