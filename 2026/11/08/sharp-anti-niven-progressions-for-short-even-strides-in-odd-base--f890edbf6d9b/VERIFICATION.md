---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For every prime q|b-1, the p-1 forbidden residues for c modulo q do not exhaust q, because either q|d leaves one forbidden class or q≥p. CRT yields 0≤c≤b-2 with gcd(b-1,1+c+jd)=1. The short-width bound gives x_j=c+jd<2b, hence s_b(x_j)=x_j-(b-1)e_j for e_j∈{0,1}; simultaneous m≡1 mod q-1 makes b^m≡b modulo all digit-sum prime factors. A hypothetical common factor divides (b-1)(1+e_j), supported only on primes of b-1 since b odd, contradicting CRT. The known p-divisibility obstruction gives sharpness; independent full-integer checks for b=11 and 21 d=4 plus modular witnesses at further bases corroborate.

## originality

PASS

The established p-1 obstruction and difference-2 existence are credited. The other same-day fixed-d construction requires larger base and gcd restrictions absent here; it does not imply the b=11,d=4 four-term extremum or the all-eligible-base short-stride family. The new CRT argument genuinely extends a natural open even-step question.

## value

PASS

The exact length of arithmetic progressions avoiding shared digit-sum factors is a natural Niven-theory invariant. The theorem proves sharp attainment for an infinite structured range of base and prescribed even-step parameters, including the previously untreated concrete d=4,p=5 boundary; it answers a motivated partial case of the explicit published conjecture rather than recomputing a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
