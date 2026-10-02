# Complete Betti-table census for Artinian monomial ideals in 4 variables with Hilbert function (1,4,10,5)

## Context

General Boij–Söderberg theory describes the rational cone spanned by Betti
diagrams but does not decide which integral tables occur at a fixed Hilbert
function. Pardue / Bigatti–Hulett give only the maximal (lex) table for a
Hilbert function, and Eliahou–Kervaire formulas cover only the Borel-fixed
(stable) subfamily. Peeva–Stillman list the Hilbert-function vs. Betti-table
realizability gap as an open problem. This record closes one concrete
colength-20 instance in a machine-checkable form.

## Definitions

Let `R = k[x,y,z,w]`, `k` any field (certificates cover characteristic 0 and
large primes; small characteristics unchecked).
`H(R/I) = (1,4,10,5)` means `dim_k (R/I)_0 = 1`, `dim_1 = 4`, `dim_2 = 10`,
`dim_3 = 5`, `dim_{\ge 4} = 0`; colength `1+4+10+5 = 20`.
`beta_{i,j}(R/I) = dim_k Tor_i(R/I,k)_j` are the graded Betti numbers.
There are `C(3+4-1,3) = 20` cubic monomials, of which 4 are pure powers
`x^3,y^3,z^3,w^3` and 16 are not. Canonical order of the 16 non-pure cubics:

| idx | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mon | zww | zzw | yww | yzw | yzz | yyw | yyz | xww | xzw | xzz | xyw | xyz | xyy | xxw | xxz | xxy |

For an ideal with `H = (1,4,10,5)`, `T(I)` denotes the 5 cubic standard
monomials (survivors) and `C(I)` the 15 complementary cubic generators.
`h_4` is the number of quartic monomials not divisible by the cubic
generators. `S_4` acts by permuting variables (graded automorphism preserving
Betti numbers). "Type" in the assignment meant `h_3 = 5`; true socle dimension
is reported separately.

## Result

**Lemma 1 (pure-power forcing, cubic-generated case).**
If `I` is generated in degree 3 with `(R/I)_4 = 0`, then
`x^3,y^3,z^3,w^3 in I`, since `x^4` is divisible among cubics only by `x^3`
(and likewise for `y,z,w`).

**Theorem 1 (enumeration).**
Exactly 1752 monomial ideals in `R` are generated in degree 3 and have
`H = (1,4,10,5)`. They are in bijection with the 5-subsets `S` of the 16
non-pure cubics for which every quartic is divisible by one of the 15
complementary cubics plus the 4 pure powers. Over the `C(16,5) = 4368`
candidates, `h_4` distributes as `{0:1752, 1:2124, 2:468, 3:24}`.

**Theorem 2 (Betti census of the 1752).**
The 1752 ideals realize exactly 10 distinct graded Betti tables. In every
table `beta_00 = 1`, `beta_13 = 15` (the 15 cubic generators; no other first
syzygies), `beta_24 = 25`, `beta_47 = 5`; all other entries vanish except
`(beta_25, beta_35, beta_36, beta_46)`:

| freq | witness survivors T | b25 | b35 | b36 | b46 |
|------|---------------------|-----|-----|-----|-----|
| 684 | zww,yww,yzz,xzw,xyw | 7 | 13 | 12 | 2 |
| 348 | zww,yww,yzz,xzw,xyy | 6 | 12 | 11 | 1 |
| 336 | zww,yww,yzz,xzw,xyz | 6 | 12 | 12 | 2 |
| 120 | zww,yzw,yzz,xyw,xxz | 5 | 11 | 11 | 1 |
| 108 | zww,yww,yzz,xzw,xzz | 8 | 14 | 13 | 3 |
| 60 | zww,yww,yzz,xww,xyz | 8 | 14 | 12 | 2 |
| 36 | zww,yzw,xzz,xyw,xyz | 5 | 11 | 12 | 2 |
| 24 | zww,yww,yzz,xww,xzz | 9 | 15 | 13 | 3 |
| 24 | zww,yzw,xzz,xyy,xxw | 5 | 11 | 10 | 0 |
| 12 | zww,yww,xzw,xyw,xyz | 7 | 13 | 13 | 3 |

Frequencies sum to 1752. The freq-24 table on
`T = {zww,yww,yzz,xww,xzz}` with `(9,15,13,3)` is the unique
componentwise-maximal (hence lex-largest) table. Full `(i,j)` matrices,
witness index sets, and frequencies are in
`artifacts/betti_census.json`. Euler identity
`sum_i (-1)^i beta_{i,j} = coeff_j((1+4t+10t^2+5t^3)(1-t)^4)`
` = [1,0,0,-15,25,-6,-10,5]` holds for every table.

**Proposition 3 (symmetry and stable subfamily).**
The 1752 ideals fall into 80 `S_4`-orbits (66 of size 24, 14 of size 12);
Betti tables are constant on orbits. No member is Borel-fixed (strongly
stable) under any of the 24 variable orders (exhaustive scan 0/1752).
Hence Eliahou–Kervaire-type formulas cover none of this subfamily.

**Theorem 4 (full generator-degree-<=4 stratum).**
Allowing minimal generators in degree 4, the `H = (1,4,10,5)` monomial
stratum has exactly `C(20,5) = 15504` ideals, realizing exactly 48 distinct
Betti tables (`beta_13 = 15` always; `beta_14 in {0,...,5}` counts minimal
quartic generators). The 1752/10 census is the `h_4 = 0` cubic-generated
slice. The 48 frequency multiset (sorted) is
`[1968,1608,1548,1224,1092,968,912,684,552,516,348,336,336,324,312,300,264,224,216,204,192,156,156,120,108,108,84,72,72,60,48,48,36,36,36,28,24,24,24,24,24,24,12,12,12,12,12,4]`
summing to 15504 (see `artifacts/full_census_summary.json`).

**Remark (socle type).** True socle dimensions on the 1752 distribute as
`{5:24, 6:468, 7:1116, 8:144}` (only 24 have socle type 5); on the full
15504 they range 5–11 as `{5:52, 6:1128, 7:4932, 8:5720, 9:2868, 10:768,
11:36}`.

## Proof / evidence

- Exact exhaustion of `C(16,5) = 4368` survivor sets reproduces
  `h_4 = {0:1752, 1:2124, 2:468, 3:24}`; each `h_4 = 0` set yields an ideal
  with `H = (1,4,10,5)` (degrees 0–2 full, no generators below degree 3) and
  `S` is recovered as degree-3 standards, so ideals are distinct; every
  degree-`>= 5` generator is redundant (divisible by a quartic in `I`).
- Graded Betti numbers computed as `Tor` via the Koszul complex
  `C_{i,j} = Lambda^i(k^4) tensor A_{j-i}` (`A = R/I`, monomial basis
  `|B| = 20`), differentials `d(e_S tensor m) = sum ±e_{S\\k} tensor x_k·m`
  (0 if in `I`); matrices `<= 60x60` over `{0,±1}`; ranks mod 32003 and mod
  1000003 agree on all 1752 (same 10 tables, same frequencies); exact
  rational arithmetic agrees on all 80 `S_4`-orbit representatives, lifting
  to all 1752 by graded-automorphism invariance. Independent auditor
  reimplementation over `QQ` for a witness and Euler checks on all ideals
  pass.
- `S_4`-orbit decomposition (80 orbits) and Borel-fixed scan over all 24
  orders, plus full `C(20,5) = 15504` census by the same Koszul computation,
  all re-derived in one stdlib-only script.

## Limitations

1. No Macaulay2/Singular cross-check (unavailable in the research
   environment); verification is dual-prime + exact-rational + Euler +
   `S_4`-consistency of the mathematically equivalent Koszul–Tor
   computation.
2. Certificates cover characteristic 0 / large primes; small-characteristic
   Betti numbers unchecked (monomial Betti numbers can depend on char).
3. Full-stratum extension archived as frequency multiset plus count (48
   tables over 15504 ideals); per-table matrices/witnesses archived only for
   the primary 1752/10 slice.
4. Originality rests on assignment triage searches, not a fresh exhaustive
   sweep; grey-literature (thesis/code) overlap cannot be fully excluded;
   novelty framed as triage, not a priority claim.
5. The Boij–Söderberg virtual-vs-realized gap list from the fallback plan
   was not produced; replaced by the full-stratum extension.

## Reproducibility

Run `python3 artifacts/audit_betti.py` (stdlib only, ~14 s): asserts the
candidate count, `h_4` distribution, 10-table / 48-table censuses, second-prime
agreement, Euler identities, rational agreement on orbit reps, orbit sizes,
and Borel-fixed scan. Machine-readable census in
`artifacts/betti_census.json` and `artifacts/full_census_summary.json`.

## References

- K. Pardue, Deformation classes of graded modules and maximal Betti
  numbers, Illinois J. Math. 40(4), 1996.
  https://doi.org/10.1215/ijm/1255985937 — maximal table only; lex ideal not
  in this terminating stratum.
- I. Peeva, M. Stillman, Open Problems on Syzygies and Hilbert Functions,
  J. Commut. Algebra 1(1), 2008. https://doi.org/10.1216/jca-2009-1-1-159 —
  realizability gap as open.
- G. Fløystad, Boij–Söderberg Theory: Introduction and Survey, 2012.
  https://doi.org/10.1515/9783110250404.1 — rational/cone level.
- R. Okazaki, K. Yanagawa, On CW complexes supporting Eliahou–Kervaire type
  resolutions of Borel fixed ideals, 2014.
  https://doi.org/10.1007/s13348-014-0104-0 — stable subfamily (empty here).
- Sadykov et al., Artinian Gorenstein algebras of embedding dimension four,
  J. Pure Appl. Algebra, 2005.
  https://doi.org/10.1016/j.jpaa.2004.12.015 — Gorenstein locus, disjoint
  (socle type 1 vs. mostly 6–8 here).
