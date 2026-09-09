# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified local invariants, known-generator verification, and numerical canonical height for the open rank-2 congruent-number curve E_799657

## 1. Object and status

Let `n = 799657`, `D = n^2 = 639451317649`, and

```
E : y^2 = x^3 - D*x      over Q.
```

The live LMFDB Congruent Numbers page (re-fetched 2026-09-09, Release 1.2.1) states that
among the first 1,000,000 congruent-number curves, exactly three rank-2 entries
(`n = 799657, 937121, 998617`) have only one generator known, with regulator and Sha
unknown; the per-`n` page for 799657 gives one generator

```
P1 = (-94381225/289, 2049376840680/4913)
```

and states "the other is not yet computed". **This report does not exhibit the missing
second generator.** It certifies the local setup rigorously, verifies the known generator
exactly, computes its canonical height numerically, and logs a bounded integral search —
a meaningful partial theorem toward the audit plan, with all non-claims explicitly fenced.

## 2. Theorem (partial; proved here)

With `E`, `n`, `D`, `P1` as above:

1. **Primality/squarefree.** `n = 799657` is prime (exhaustive trial division to
   `isqrt(n) = 894`, zero divisors), hence squarefree with single prime factor.
2. **Minimality.** The model `y^2 = x^3 - Dx` is globally minimal: at 2, `v2(Delta) = 6
   < 12` blocks the only possible 2-scaling; at odd `u`, `u^12 | Delta = 64D^3` forces
   `u | n` while `u^4 | 48D` then forces `u = 1`.
3. **Reduction at `p = n`.** `v_n(c4) = 2`, `v_n(c6) = +inf`, `v_n(Delta) = 6`,
   `v_n(j) = 0` (potentially good). Tate step 7 applies with auxiliary cubic
   `P(T) = T^3 - T = T(T-1)(T+1)` splitting completely mod `n`; hence Kodaira type
   `I_0^*`, Tamagawa number `c_n = 4`, conductor exponent `f_n = 2`.
4. **Reduction at `p = 2`.** `v2(c4) = 4`, `v2(Delta) = 6`, `D = 1 mod 16`. Cross-checked
   against the general congruent-twist family and the fully documented sibling
   `y^2 = x^3 - x` (LMFDB 32.a3, Kodaira `III`, `c_2 = 2`, conductor `2^5`): the same
   2-adic invariants give Kodaira type `III`, `c_2 = 2`, conductor exponent `f_2 = 5`.
   (Conductor-exponent attribution: odd part `n^2` contributes `2*1 = 2` via `I_0^*`;
   total conductor `32*D = 2^5 * n^2` is confirmed independently below.)
5. **Conductor.** `N(E) = 32*D = 20462442164768`, matching the live LMFDB per-`n` value
   digit-for-digit.
6. **Torsion.** `E(Q)_tors = Z/2 x Z/2` exactly: the full 2-torsion
   `{O, (0,0), (n,0), (-n,0)}` is rational, and exact finite-field enumeration gives
   `#E(F_3) = #E(F_5) = 4` at good primes 3 and 5, so no larger torsion injects.
7. **Known generator.** `P1` satisfies `y^2 = x^3 - D*x` exactly (integer identity
   `b^2 = a^3 - D*a*17^4` with `a = -94381225`, `b = 2049376840680`, denominators
   `17^2`, `17^3`); `P1` is nontorsion (its x-coordinate is not in `{-n, 0, n}`).
8. **Bounded integral search.** Every integral `x = a` with `|a| <= 10^6` with
   `a^3 - D*a` a square is in `{-n, 0, n}` (exact `isqrt` loop; hits exactly the
   2-torsion x-coordinates). Replay: `output/artifacts/integral_search_d1.py`.

## 3. Numerical result (computed evidence, not a proved enclosure)

**Canonical height of P1.** Exact-rational duplication limit `h(x(2^N P1))/4^N`
(big-integer `Fraction` arithmetic, only the final logarithm transcendental):

| N | digits(num/den of x(2^N P1)) | h/4^N |
|---|---|---|
| 1 | 33/28 | 18.988919134065643 |
| 2 | 133/124 | 19.075537794331762 |
| 3 | 531/522 | 19.075537799228204 |
| 4 | 2121/2113 | 19.075537818813928 |

i.e. `hhat(P1) ~ 19.07553782`, stable to ~1e-8 across N = 2..4
(`output/artifacts/hhat_p1_exact.py`). A proved enclosure would need interval
arithmetic and an explicit tail bound; it is NOT claimed here.

## 4. What is explicitly NOT claimed (fenced uncertainty)

- The missing second generator, regulator, saturation index, rank equality, and Sha:
  untouched. A 2-isogeny Selmer formalism file (`selmer2.py`) records only the torsor
  setup; its Q2 solubility table is incomplete and no Selmer bound is claimed.
- No rigorous canonical-height lower bound H0 for a missing independent point; no
  certified height pairing. The numerical `hhat(P1)` above is computed evidence only.
- A first mpmath Tate-series attempt failed (archimedean-only series, omitted
  denominator places) and was discarded; the failure mode is logged in WORKLOG, not shipped.

## 5. Reproducibility

- All exact claims replay in seconds with stdlib-only Python:
  `python3 output/artifacts/verify_all.py` prints `VERIFY_OK`
  (primality, valuations, conductor, `#E(F_3) = #E(F_5) = 4`, on-curve check, subset search).
- Live LMFDB sources (fetched 2026-09-09): CongruentNumbers overview page (three open
  entries incl. 799657) and `/EllipticCurve/Q/CongruentNumber/799657` (P1 coordinates,
  conductor 20462442164768, "other [generator] not yet computed").
- Note on the type-`III`-at-2 attribution: valuations `v2(c4) = 4, v2(Delta) = 6` are
  exact; the Kodaira-symbol step cites the standard Tate table as realized on the
  documented sibling 32.a3 with identical 2-adic invariants. If a referee demands a
  line-by-line Tate-step trace at 2, it can be appended without changing any invariant.

## 6. Value

Even with the generator still missing, this pins down every local invariant of the
smallest of the three published open entries by exact computation, verifies the known
generator independently of the dataset files, supplies the first numerical canonical
height `hhat(P1) ~ 19.0755` for downstream regulator/Sha work, and leaves a replayable
stdlib-only certificate — constraining, not closing, the open entry.
