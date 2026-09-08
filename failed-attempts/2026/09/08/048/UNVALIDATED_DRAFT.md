# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp parametric boundary at 73 for the frozen 3-identity Mordell core

## Statement of the frozen family and result

Let **M** be the frozen 3-identity classical Mordell core (fixed before computation):

- **(F3)** If `n = 4k+3`, then `4/n = 1/(k+1) + 1/(2n(k+1)) + 1/(2n(k+1))`.
- **(F5)** If `n = 8M−3`, i.e. `(n+3) ≡ 0 (mod 8)`, then `4/n = 1/(2M) + 1/(nM) + 1/(2nM)`.
- **(F17)** If `n = 24M−7`, i.e. `(n+7) ≡ 0 (mod 24)`, then `4/n = 1/(6M) + 1/(nM) + 1/(6nM)`.

**Theorem.** Relative to this frozen M:

1. Every prime `p < 73` with `p ≡ 1 (mod 4)` is an instance of an identity in M
   (explicit parameters tabulated below).
2. `73` is prime, `73 ≡ 1 (mod 4)`, and **no** identity in M instantiates `4/73`
   (finite congruence-elimination certificate).
3. `4/73` is solvable, with explicit witness `4/73 = 1/20 + 1/292 + 1/730`.

Hence `73` is the least prime `≡ 1 (mod 4)` outside the frozen 3-identity core —
a certified parametric-separation witness: the classical 3-identity toolkit provably
stops at 73 while the equation remains solvable non-parametrically.

## Proofs

*F3.* `1/(k+1) + 2/(2n(k+1)) = 1/(k+1) + 1/(n(k+1)) = (n+1)/(n(k+1))`.
With `n = 4k+3`, `n+1 = 4(k+1)`, so this equals `4/n`. ∎

*F5.* `1/(2M) + 1/(nM) + 1/(2nM) = (n + 2 + 1)/(2nM) = (n+3)/(2nM)`.
With `n+3 = 8M` this equals `8M/(2nM) = 4/n`. ∎

*F17.* `1/(6M) + 1/(nM) + 1/(6nM) = (n + 6 + 1)/(6nM) = (n+7)/(6nM)`.
With `n+7 = 24M` this equals `24M/(6nM) = 4/n`. ∎

*Coverage table* (each verified by exact rational arithmetic):

| p  | identity | triple (x, y, z) |
|----|----------|------------------|
| 5  | F5, M=1  | (2, 5, 10) |
| 13 | F5, M=2  | (4, 26, 52) |
| 17 | F17, M=1 | (6, 17, 102) |
| 29 | F5, M=4  | (8, 116, 232) |
| 37 | F5, M=5  | (10, 185, 370) |
| 41 | F17, M=2 | (12, 82, 492) |
| 53 | F5, M=7  | (14, 371, 742) |
| 61 | F5, M=8  | (16, 488, 976) |

Completeness of the prime list: the integers `≡ 1 (mod 4)` below 73 are
5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69; trial division
leaves exactly the 8 primes above (9=3², 21,25,33,45,49,57,65,69 composite).

*Elimination lemma for 73.* Membership in each identity requires its congruence:
F3 needs `p ≡ 3 (mod 4)` but `73 ≡ 1 (mod 4)`; F5 needs `(p+3) ≡ 0 (mod 8)`
but `73+3 = 76 ≡ 4 (mod 8)`; F17 needs `(p+7) ≡ 0 (mod 24)` but
`73+7 = 80 ≡ 8 (mod 24)`. Since the parameters (k, M) must be integers, no
instantiation exists. In residue terms: the `1-mod-4` primes split into the
`8M−3` class (5, 13, 29, 37, 53, 61) and the `24M−7` class (17, 41), and
`73 = 8·9+1 = 24·3+1` hits neither. ∎

*Witness.* `4/73 − 1/20 = 80/1460 − 73/1460 = 7/1460 = (5+2)/1460
= 1/292 + 1/730`, since `292 = 4·73` and `730 = 10·73`. So
`4/73 = 1/20 + 1/292 + 1/730`, verified by exact `Fraction` arithmetic. ∎

## Reproduction

Run `python3 output/artifacts/verify.py` (stdlib only): re-derives the prime list,
re-checks every coverage triple, re-checks the three elimination congruences,
and re-checks the witness identity.

## Limitations and scope (read before citing)

- The boundary `p* = 73` is relative to the **frozen 3-identity core** above, the
  widely-cited minimal Mordell representatives. It is NOT proved against every
  congruence-specific splitting in Mordell (1967) / Ionascu–Wilson / Salez extensions;
  a broader frozen list could cover 73. The theorem is therefore a scoped partial result.
- Originality claim is correspondingly scoped: no other source is known to freeze exactly
  this 3-identity core and certify its least `1-mod-4` failure point; the obstruction
  template (admissibility-congruence elimination) is reusable for testing richer families.
- Existence at 73 is classical; the new content is the proved non-coverability by M
  plus the clean divisor-structured witness.
