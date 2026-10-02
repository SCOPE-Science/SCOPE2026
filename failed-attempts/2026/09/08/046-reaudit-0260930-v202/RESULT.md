# Root-number-1 non-cube-sum witnesses for six of the ten least n = 3l (l prime 7 mod 9) above 2000

## Context

An integer n is a rational cube sum if n = x^3 + y^3 for some x, y in Q.
For cube-free n > 2 this holds iff the Mordell curve
E_{-432n^2}: Y^2 = X^3 - 432 n^2 has positive Mordell-Weil rank over Q.
The subfamily with global root number w(n) = +1 is the recognized hard case
because parity gives no information. Das-Jha (arXiv:2508.05361, J. Pure Appl.
Algebra 2025) proved: for prime l = 7 mod 9, if 3l is a cube sum then the
3-rank h_3(12l) of Cl(Q(cuberoot(12l))) equals 2 (Theorem A), and the class
group contains Z/6Z x Z/3Z (Corollary B). Moreover h_3(12l) = 2 iff the cubic
residue symbol (3/l)_3 = 1 (Lemma 2.5, via Gerth's formula).

## Definitions

- l in {2113, 2131, 2203, 2221, 2239, 2293, 2311, 2347, 2383, 2437}: the ten
  least primes congruent to 7 mod 9 exceeding 2000 (next such prime 2473).
- n = 3l; E_n: Y^2 = X^3 - 432 n^2.
- w(n): global root number of E_n over Q (Birch-Stephens formula).
- h_3(12l): 3-rank dim_{F_3} Cl(Q(cuberoot(12l)))[3].
- (3/l)_3 = 1 iff 3^((l-1)/3) = 1 mod l (Euler criterion, l = 1 mod 3 prime).

## Result (partial census)

(i) Every n above has global root number w(n) = +1.
(ii) h_3(12l) = 2 for l in {2131, 2203, 2221, 2383} and h_3(12l) = 1
otherwise.
(iii) For l in {2113, 2239, 2293, 2311, 2347, 2437}, i.e.
n in {6339, 6717, 6879, 6933, 7041, 7311}, n is NOT a sum of two rational
cubes, by the contrapositive of Das-Jha Theorem A.
For the remaining four l the Das-Jha 3-rank obstruction is silent and no
verdict is returned (explicitly open).

Computed table:

| l | n=3l | 3^((l-1)/3) mod l | (3/l)_3=1? | h_3(12l) | verdict |
|---|------|-------------------|------------|----------|---------|
| 2113 | 6339 | 438 | No | 1 | proved non-cube-sum |
| 2131 | 6393 | 1 | Yes | 2 | OPEN |
| 2203 | 6609 | 1 | Yes | 2 | OPEN |
| 2221 | 6663 | 1 | Yes | 2 | OPEN |
| 2239 | 6717 | 295 | No | 1 | proved non-cube-sum |
| 2293 | 6879 | 1303 | No | 1 | proved non-cube-sum |
| 2311 | 6933 | 1428 | No | 1 | proved non-cube-sum |
| 2347 | 7041 | 1284 | No | 1 | proved non-cube-sum |
| 2383 | 7149 | 1 | Yes | 2 | OPEN |
| 2437 | 7311 | 2351 | No | 1 | proved non-cube-sum |

## Proof / evidence

All literature ingredients are prior work; no originality is claimed for
them. Cube-sum equivalence, Birch-Stephens root-number formula, Gerth 3-rank
formula, Das-Jha Lemma 2.5 and Theorem A (whose proof uses the 3-isogeny
Selmer bound Prop 2.7 plus the 3-parity theorem of Nekovar-Kim-
Dokchitser-Dokchitser and Lemma 2.1) are cited.

Fresh computation is exact integer arithmetic in stdlib-only
`output/artifacts/verify_census.py`:
consecutiveness sieve over [2001,2500); cube-freeness of each n = 3l;
Birch-Stephens evaluation (n = 3 mod 9 gives w_3 = -1; l = 1 mod 3 gives
w_l = +1; hence w = +1); cubic symbol by Euler's criterion computed twice
(builtin `pow` and explicit multiply loop) with r^3 = 1 mod l sanity check
in every row; h_3 assignment by Lemma 2.5; verdict by Theorem A
contrapositive. Re-running gives `ALL CHECKS PASSED` and the six witnesses
above. The auditor re-executed the script and independently recomputed all
ten residues.

## Limitations

- Partial census only: 6/10 decided; l in {2131, 2203, 2221, 2383} with
  h_3 = 2 are explicitly OPEN.
- Only Theorem A's 3-rank contrapositive is used. No 2-part of
  Cl(Q(cuberoot(12l))) is computed, so Corollary B's Z/6Z x Z/3Z subgroup
  form is not invoked.
- No fresh phi-Selmer computation or Selmer logs; the Selmer bound is
  encapsulated in cited Theorem A.
- No rank-0, analytic-rank, cube-sum representation, or verdict claimed for
  the four open cases. Original 10/10 complete-census target with full
  class-group plus Selmer logs is not met; the certified headline is the
  six witnesses.

## Reproducibility

`python3 output/artifacts/verify_census.py` re-derives the window, every
root number, every cubic symbol (two implementations), every 3-rank, and
every verdict from the stated integers alone. No PARI/Sage required.

## References

- Das, Jha, On certain root number 1 cases of the cube sum problem,
  arXiv:2508.05361v2 (J. Pure Appl. Algebra 2025). Theorem A, Corollary B,
  Lemma 2.5, Prop 2.7, Sec 3 examples.
- Jha, Majumdar, Shingavekar, phi-Selmer group, ideal class groups and cube
  sum problem, arXiv:2207.12487 (general phi-Selmer bounds).
- De, Majumdar, Mondal, Relative p-class groups and p-Selmer groups,
  arXiv:2412.13022 (structural relation; downstream value).
- Gerth, On 3-class groups of pure cubic fields, J. Reine Angew. Math.
  278/279 (1975) (3-rank formula, Lemma 1.2 in Das-Jha).
