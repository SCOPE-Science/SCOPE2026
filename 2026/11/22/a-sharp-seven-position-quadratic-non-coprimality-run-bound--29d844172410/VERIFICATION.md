---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Only prime support matters. An odd prime with a root of −1 is 1 mod 4, so except for 5 it exceeds 7. For two hits at displacement d=1,…,7, subtraction gives 2(a+i)≡−d, hence p divides d²+4; factoring 5,8,13,20,29,40,53 leaves only separations 3,5,7 for p≠2,5. Such a prime hits at most one slot of a fixed parity and at most two slots in the whole block (p>7, and at most two roots). With 2 present, it covers four slots, and 5 covers at most two of the opposite parity while the third prime covers at most one. With 2 absent, eight hits require 5 covering exactly four and two disjoint admissible pairs. I enumerated a mod 5 independently: the five masks are {2,3,7}, {1,2,6,7}, {0,1,5,6}, {0,4,5}, {3,4}. In the complements of the two size-four masks the only admissible edges share vertex 0 or vertex 7, respectively; no matching. For sharpness, a≡7 mod 10 covers offsets 0,2,4,6 by 2 and 1,5 by 5; CRT with a+3 congruent to a root of −1 mod r covers the final offset for every specified r, with a nonnegative representative. The a=7 example has the missing value 101. The proof covers all prime powers and is not mediated by a finite prime cutoff. VERIFICATION.md and verify.py were read, not executed.

## originality

PASS

The supported distinct claim is the exact maximum seven for the translated argument of X²+1 with three distinct fixed modulus primes, with an infinite extremal family. The closest accessible polynomial and run results compare different modular conditions or scopes, not stronger results implying this sharp bound.

## value

PASS

This is the first kind of nontrivial covering obstruction one needs when studying a fixed quadratic with a small prime support: parity and possible pair distances rule out simultaneous coverage even though counting individual hit capacities can allow eight. The exact upper bound settles the entire three-prime class, including arbitrarily large primes and prime powers, with an infinite supply of extremizers. It is not a numerical check on one modulus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
