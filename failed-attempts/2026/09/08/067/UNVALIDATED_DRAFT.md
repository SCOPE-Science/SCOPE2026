# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Finiteness census with replayable coset tables over short 2-generator 2-relator presentations

## Claim (fallback scope; full dichotomy NOT claimed)

Let S be the 343 canonical representatives of presentations
`<a,b | w1, w2>` with `|w1|+|w2| <= 8` (cyclically reduced words over
`{a,b,a^-1,b^-1}`, up to generator renaming/inversion, cyclic rotation,
relator inversion, and relator swap), enumerated by
`artifacts/enumerate_presentations.py` and listed in
`artifacts/presentations.csv`. Then:

1. **235 presentations are finite with exact certified orders** (range 1..27;
   distribution `{1:36, 2:52, 3:31, 4:38, 5:16, 6:31, 7:5, 8:9, 9:4, 10:3,
   12:2, 16:5, 21:1, 24:1, 27:1}`). Each carries a closed,
   inverse-consistent, connected Todd–Coxeter coset table over the trivial
   subgroup in which both relators act trivially at every point
   (`artifacts/coset_tables/<id>.json`, `artifacts/results.csv`
   status `finite_closed_table`).
2. **85 presentations are certified infinite**: 76 by abelianization (exponent-sum
   matrix determinant 0, hence the group maps onto Z) and 9 as free products
   `Z_m * Z_n` with `m,n >= 2` (pure-power relators in distinct generators),
   which contain a nonabelian free subgroup or are infinite dihedral and have
   the standard alternating normal form.
3. **23 presentations are explicitly UNRESOLVED** (bounded enumerator exceeded
   200 cosets / 1.5 s budget), listed with status `unresolved_overflow` and no
   order claimed.
4. **Three infinite candidates have certified word-metric growth balls** to
   radius 12 with explicit exponential lower bounds, recomputed exactly:
   - `<a,b|a^2,b^3>` = Z2\*Z3: balls
     `1,4,8,14,22,34,50,74,106,154,218,314,442`,
     `|B_n| >= floor((3/2)^n)+1`;
   - `<a,b|a^2,b^4>` = Z2\*Z4: balls
     `1,4,9,17,30,51,85,140,229,373,606,983,1593`,
     `|B_n| >= floor(phi^n)+1`, `phi=(1+sqrt5)/2`;
   - `<a,b|a^3,b^3>` = Z3\*Z3: balls
     `1,5,13,29,...,16381`, `|B_n| >= 2^n+1` for `n>=2` (`|B_1|=5`).

All finite tables and all growth balls pass the independent second-script
replay `artifacts/replay.py` (relator triviality, closedness/coherence,
connectivity, abelianization divisibility, ball recomputation): ALL PASS.

## Method (bounded, reproducible)

1. **Canonical enumeration.** All cyclically reduced words of length 1..7 over
   `{a,b,A,B}`; all pairs with total length `<= 8`; quotient by the 8 signed
   generator renamings, rotation, inversion, and relator swap. Result: 343
   representatives (lengths 2..8).
2. **Abelianization.** Exponent-sum 2x2 matrix; `det = 0` certifies a surjection
   onto Z, hence infiniteness (76 cases).
3. **Free-product normal forms.** Relators pure powers in distinct generators
   with both exponents `>= 2` give `Z_m * Z_n`, certified infinite by the
   alternating normal-form argument (9 cases, including `<a^2,b^2>` =
   infinite dihedral).
4. **Bounded Todd–Coxeter.** HLT-style scan with definition/coincidence
   processing, cap 200 cosets, 1.5 s per presentation, from the trivial
   subgroup. Closed tables only are claimed (235); open/overflow runs are
   marked unresolved, never claimed.
5. **Growth balls.** Exact BFS over alternating normal forms in generators
   `{a,A,b,B}` for Z2\*Z3, Z2\*Z4, Z3\*Z3 (these presentations *equal* the free
   products, so the balls are exact group word-metric balls), radius 12, with
   fitted-and-verified exponential lower bounds.
6. **Independent replay.** `replay.py` re-parses every logged table and ball
   from scratch and rechecks all certificate properties.

## Evidence summary

- `artifacts/presentations.csv`: 343 canonical representatives
   (id, w1, w2, lengths).
- `artifacts/results.csv`: per-case verdict (`finite_closed_table` /
   `infinite_abelianization` / `infinite_free_product` / `unresolved_overflow`),
   exact order where finite, abelianization determinant/order, detail string.
- `artifacts/coset_tables/<id>.json` (235 files): closed permutation tables
   `{coset: [a-image, A-image, b-image, B-image]}`, order, definition count.
- `artifacts/growth_{g1,g2,g3}.json`: sphere/ball counts to radius 12, lower
   bound values, method note.
- Replay: 235/235 tables verified (closed, inverse-consistent, connected,
   relators trivial, `|G_ab|` divides `|G|`); 3/3 ball logs recomputed
   byte-equal with bounds holding.

## Conjectures and uncertainty (NOT claimed)

- The 23 `unresolved_overflow` cases (all with nonzero abelianization
  determinant, e.g. `<AA,AABB>`, `<AA,ABAB>`, `<AAA,ABAB>`, `<AABB,AAbb>`)
  are mostly small finite cyclic groups whose enumerator exceeded the
  fixed cap; their true orders are NOT claimed here.
- Knuth–Bendix confluence logs from the audit plan were not produced; the
  fallback claim rests on coset tables + abelianization/free-product
   certificates + growth balls instead. No KB claim is made.
- Canonical reduction is under renaming/rotation/inversion/swap only (not full
  Nielsen equivalence), so "representative scope" means orbit representatives
  under this explicit finite group action, stated exactly.

## Selected finite orders >= 8 (sample; full table in `results.csv`)

`<AA,ABBBB>` 8; `<AAA,ABBB>` 9; `<AAAA,ABB>` 8; `<AA,ABABBB>` 16;
`<AA,ABAbbb>` 16; `<AA,ABBBBB>` 10; `<AA,ABBBaB>` 16; `<AA,ABBBab>` 16;
`<AAA,AABBB>` 9; `<AAA,ABABB>` 9; `<AAA,ABAABBB>`-type `<AAA,ABAbb>` 24;
`<AAA,ABBBB>` 12; `<AAA,ABBaB>` 27; `<AAA,ABBab>` 21; `<AAAA,ABBB>` 12;
`<AAAAA,ABB>` 10; `<AAAAB,Abb>` 9; `<AAAB,AAbb>` 8; `<AAAB,ABBB>` 8;
`<AAAB,AbAb>` 8; `<AAAB,Abbb>` 10; `<AAABB,Abb>` 8; `<AAB,AbAbb>` 8;
`<AABB,ABAb>` 8; `<AABB,AbAb>` 16; `<ABAb,ABaB>` 8.

## Reproduction

```
python3 artifacts/enumerate_presentations.py  # -> presentations.csv (343 reps)
python3 artifacts/analyze.py                  # -> results.csv + coset_tables/
python3 artifacts/growth.py                   # -> growth_{g1,g2,g3}.json
python3 artifacts/replay.py                   # expect ALL PASS
```

Runs in under ~2 minutes total (enumeration ~1 min, analysis ~30 s,
growth + replay seconds) with only the Python standard library.
