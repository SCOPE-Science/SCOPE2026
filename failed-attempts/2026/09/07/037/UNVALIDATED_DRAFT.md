# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact maximal Sidon subsets of Z_n for n = 31..55

## 1. Definitions and claim

Work in the cyclic group `Z_n = {0,...,n-1}` with addition mod `n`.

**Definition.** `A ⊆ Z_n`, `|A| = k`, is *Sidon* (modular Golomb / `B_2`) if the
`k(k-1)` ordered differences `a-b (a≠b)` are pairwise distinct mod `n`
(hence nonzero). Then `|A-A| = k(k-1)+1`.

Equivalently (Lemma 1 below) the `k(k+1)/2` sums `a+b (a≤b)` are pairwise
distinct mod `n`. All witnesses below satisfy **both**; the verifier checks both.

**Counting bound.** Distinct nonzero differences give `k(k-1)+1 ≤ n`, i.e.
`k ≤ (1+√(4n-3))/2`. Let `ub(n)` be the largest such `k`. For `n=31..42`,
`ub=6`; for `n=43..55`, `ub=7` (`k=8` needs `n≥57`).

**Theorem (certified census).** Let `S(n)` be the maximum Sidon size in `Z_n`.
Then, with witnesses in residues mod `n`:

| n | S(n) | witness | gap `(n-1)-S(S-1)` | how proved |
|---|------|---------|--------------------|------------|
| 31 | 6 | {0,1,3,8,12,18} | 0 (perfect) | counting bound |
| 32 | 5 | {0,1,3,7,12} | 11 | exhaustive: no 6-set |
| 33 | 5 | {0,1,3,7,12} | 12 | exhaustive: no 6-set |
| 34 | 5 | {0,1,3,7,12} | 13 | exhaustive: no 6-set |
| 35 | 6 | {0,1,3,7,12,20} | 4 | counting bound |
| 36 | 6 | {0,1,3,8,23,27} | 5 | counting bound |
| 37 | 6 | {0,1,3,7,16,26} | 6 | counting bound |
| 38 | 6 | {0,1,3,7,17,30} | 7 | counting bound |
| 39 | 6 | {0,1,3,7,12,22} | 8 | counting bound |
| 40 | 6 | {0,1,3,7,17,28} | 9 | counting bound |
| 41 | 6 | {0,1,3,7,12,20} | 10 | counting bound |
| 42 | 6 | {0,1,3,7,12,20} | 11 | counting bound |
| 43 | 6 | {0,1,3,7,12,20} | 12 | exhaustive: no 7-set |
| 44 | 6 | {0,1,3,7,12,20} | 13 | exhaustive: no 7-set |
| 45 | 6 | {0,1,3,7,12,20} | 14 | exhaustive: no 7-set |
| 46 | 6 | {0,1,3,7,12,20} | 15 | exhaustive: no 7-set |
| 47 | 6 | {0,1,3,7,12,20} | 16 | exhaustive: no 7-set |
| 48 | 7 | {0,1,3,15,20,38,42} | 5 | counting bound |
| 49 | 7 | {0,1,3,7,27,35,40} | 6 | counting bound |
| 50 | 7 | {0,1,3,8,14,18,30} | 7 | counting bound |
| 51 | 7 | {0,1,3,7,12,20,30} | 8 | counting bound |
| 52 | 7 | {0,1,3,7,12,22,35} | 9 | counting bound |
| 53 | 7 | {0,1,3,7,12,22,40} | 10 | counting bound |
| 54 | 7 | {0,1,3,7,16,26,37} | 11 | counting bound |
| 55 | 7 | {0,1,3,7,12,20,30} | 12 | counting bound |

"Counting bound" means `S(n)=ub(n)`: the witness shows `S≥ub`, the bound gives
`S≤ub`. "Exhaustive" means `S(n)=ub(n)-1`: the witness shows `S≥ub-1`, a complete
search proves no `ub`-set exists, and the bound rules out anything larger.
Full difference/sum lists are stored in `artifacts/sidon_table.json`.

Notable structure (computed evidence, not assumed):
- `n=31` is the Singer perfect case `(31,6,1)`: 30 differences cover all nonzero
  residues. Witness differences sorted are `1..30` exactly.
- `n=43` is the *would-be* perfect case `7·6+1=43` (projective plane of order 6).
  We prove computationally there is **no** Sidon 7-set in `Z_43` (hence no cyclic
  `(43,7,1)` difference set). This is consistent with the Bruck–Ryser
  nonexistence of a plane of order 6, but our proof is self-contained and covers
  only the cyclic case. The gap `n=43..47` with `S=6` is the expensive part of the
  band; `7`-sets resume at `n=48`.
- `n=32,33,34` collapse to `S=5`: no 6-set exists even though the counting bound
  allows it. `6`-sets resume at `n=35` (the Golomb-ruler threshold `2·17=34`).

## 2. Lemmas (proof, not computation)

**Lemma 1 (sums ⇔ differences).** For any abelian group, ordered differences
`a-b (a≠b)` are all distinct iff sums `a+b (a≤b)` are all distinct (with the
`n/2` self-collision counted as failure on both sides).
*Proof.* If `a+b=c+d` with distinct multisets `{a,b}≠{c,d}`, then `a-c=d-b`
with `a≠c`, `d≠b`, and `(a,c)≠(d,b)` (otherwise the multisets coincide or force
`a=b`), so differences collide. Conversely if `a-b=c-d` with distinct ordered
pairs and `a≠b`, `c≠d`, then `a+d=c+b` with `{a,d}≠{c,b}` (equality would force
same pair or `a=b`), so sums collide. If `d=-d` (i.e. `2(x-y)=0` with `x≠y`),
then on the sums side `2x=2y` with `{x,x}≠{y,y}`, so both sides fail together. ∎

Hence the definitional choice does not affect the table; both properties are
verified for every witness.

**Lemma 2 (translation + multiplier reduction; completeness of pruning).**
Every `A⊆Z_n` has a translate containing `0`. Fix `0∈A`. Let
`a_1=min(A∖{0})` as an integer and `d=gcd(a_1,n)`. Then some `u∈Z_n^*` has
`u·a_1≡d (mod n)` (orbits of `Z_n^*` on `Z_n` are classified by `gcd(·,n)`; CRT
lifts the inverse of `a_1/d` mod `n/d` to a unit mod `n`). Consequently every
affine orbit `x↦u·x+t` contains a representative with `0∈A` and `a_1|n`, obtained
by minimizing `a_1` over the multiplicative orbit (if `a_1∤n` then
`d=gcd(a_1,n)<a_1` is attained and strictly smaller). Since the Sidon property is
affine-invariant, existence of a Sidon `k`-set is equivalent to existence with
`0∈A` and `a_1|n`. Searching only that restricted space is complete for the
decision problem. ∎

The census search uses Lemma 2 (divisor-restricted DFS). The independent verifier
uses **no** Lemma 2 (full sorted search from `0`, set-based), so the
nonexistence certificates do not share this proof dependency.

## 3. Method (difference-conflict backtracking)

Sorted DFS over sets containing `0`: candidates `x` in increasing order. Maintain
occupied differences. For new `x` and current `A`, the `2|A|` values
`x-a, a-x` must be nonzero, pairwise distinct, and disjoint from occupied
(bitmask in census; Python `set` in verifier — two independent code paths).
Lex order gives canonicity/determinism. Pruning is exactly difference conflict;
plus the trivial "not enough residues left" cut. Node counts and timings are
logged per `n` in `artifacts/search_log.json` (total census ≈0.24 s; verifier
≈1 s; both stdlib-only, deterministic, no randomness).

For `S(n)=ub(n)` cases optimality is pure arithmetic (no search tree needed).
For the 8 gap cases (`32,33,34` for `k=6`; `43–47` for `k=7`) both programs
independently exhaust the tree:
restricted (divisor) nodes: 1499/1738/1268 and 4387/11118/18779/9277/8469;
unrestricted verifier nodes: 3801/6873/5321 and 39934/34054/58510/45228/81376.
Agreement of the two implementations is the optimality certificate.

## 4. Replay

```
python3 artifacts/sidon_census.py   # regenerates sidon_table.json + search_log.json (~1 s)
python3 artifacts/verify_sidon.py   # rechecks all witnesses + independent exhaustive no-go (~1-2 s)
```

`verify_sidon.py` asserts: table covers `31..55`; each witness contains `0`,
is sorted, has `k(k-1)` distinct nonzero differences and `k(k+1)/2` distinct sums;
`ub` arithmetic correct; `S≤ub`; gap/perfect fields correct; and for each
`S=ub-1` case its own exhaustive search finds no `ub`-set.

## 5. Separation of proof / computed evidence / conjecture / uncertainty

- **Proof:** Counting bound; Lemma 1; Lemma 2; verifier's arithmetic checks.
- **Computed evidence (machine-checked, two implementations):** the `S(n)` values,
  witnesses, difference/sum lists, and the 8 nonexistence search trees.
- **Conjecture (not claimed):** full classification of extremal sets up to
  dihedral/multiplier equivalence; behavior outside `31..55`.
- **Uncertainty:** correctness rests on two short Python programs (no proof
  assistant). Mitigation: independent data structures (bitmask vs set),
  independent pruning (divisor vs none), naive double-loop recheck, and
  determinism. We supply exactly one extremal set per `n`, not a census of all.
- **Originality:** to our knowledge no prior source publishes this exact
  per-`n` certified table with witnesses and replayable optimality logs for
  `31..55`. We do not claim the bare numbers were never computed elsewhere;
  the contribution is the closed, machine-checked certificate package. The
  `n=31` Singer set is classical (included as a check); the `n=43` cyclic
  nonexistence is the `q=6` instance of a known theorem, reproved here
  computationally for the cyclic case only.

## 6. Limitations

- Definition fixed as above (ordered differences / sums with repetition; shown
  equivalent here, but other "weak" variants in the literature may differ).
- Only one witness per `n`; no enumeration of all extremal or inequivalent sets.
- Band limited to `31..55`; method scales further but runtimes grow
  (k=8 needs `n≥57`; not attempted).
- No formal-methods certificate (no DRAT/Lean); trust is in readable stdlib
  Python plus double implementation.
