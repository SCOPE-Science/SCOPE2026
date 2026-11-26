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

The ordered state (Fₙ,Fₙ₊₁) evolves by A with rows (0,1),(1,1); direct multiplication gives A⁵ with rows (3,5),(5,8). The integral substitution on all d+1 monomials has B_d⁵≡3ᵈI=I mod 5 for 4|d, and Cayley–Hamilton gives a monic integral order-at-most-(d+1) recurrence shared by all translates and by their window sums. Hence the stated finite gcd reduction is valid. If Q≡I mod 5ᵗ, the binomial expansion of Q⁵ shows Q⁵≡I mod 5ᵗ⁺¹; no diagonalization or denominators are needed. For r≥2, write B_d^(5^(r−1))=I+5^(r−1)D. Its powers indexed by j=0,…,4 sum to 5I modulo 5ʳ: the linear coefficient is 10·5^(r−1) and terms of degree ≥2 are divisible by 5^(2r−2). Apply this to each of the 5^(r−1) initial offsets, proving S_r(n)≡5 S_(r−1)(n) mod 5ʳ for every start. Modulo five, Fₙ₊₅≡3Fₙ and the only zero residue among the first five occurs at index 0; the fourth-multiple power is therefore the five-periodic unit indicator with sum 4. Induction gives the stronger block congruence with the negative sign, and grouping u such blocks gives exact valuation r−1 in every window for k=5ʳu with u a unit. For a 5-coprime k the first two windows differ by the unit F_kᵈ modulo five, giving gcd valuation zero, even when an initial window is zero. The bundled evidence script was inspected, not executed. The independent bounded replay passed 175 modular block checks and 75 exact finite gcds, including d=60,100 and starts beyond the first block. Finite checks are corroborative only.

## originality

PASS

The distinct supported statement is the simultaneous fourth-multiple-exponent, all-start block congruence and resulting exact five-primary window-gcd law at the ramified prime. The special cases of other primes, odd/coprime lengths and different powers or recurrences are credited without generalizing their conclusions beyond their domains.

## value

PASS

This determines a missing exceptional prime in the natural higher-power window-gcd problem. The exact one-level loss and nonzero leading residue hold uniformly in start, block order and a full exponent class, supplying a stronger arithmetic benchmark than a gcd table. In particular it handles the ramified prime where the quartic order criterion has no stated coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
