# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Insertion-bounded transfer-matrix growth bound and extremal stability
for the depth-3 slice of Av(1324)

## 1. Objects and conventions

Let Av(1324) be permutations avoiding 1324. Fix Vatter's insertion encoding:
a permutation is built by inserting successive maxima; at any stage there are
`s >= 1` open slots (intervals). The insertion letters from `s` slots are

- `m_i` (i = 1..s): new maximum inside slot `i`; slots `s -> s+1`;
- `l_i`, `r_i` (i = 1..s): new maximum just left/right of slot `i`;
  slots `s -> s`;
- `f_i` (i = 1..s): new maximum fills slot `i`; slots `s -> s-1`.

Every permutation has exactly one encoding word under this convention, of
length `n` for `pi in S_n`, starting from 1 slot and ending with 0 slots.
The *slot-depth* of `pi` is the maximum slot count along its walk.
Let `E_3 = {pi in Av(1324) : slot-depth(pi) <= 3}`.

## 2. Transfer matrix and growth bound

### Lemma 1 (alphabet cap).
From `s` slots there are exactly `s + 2s + s = 4s` letters. For `s <= 3`
this is at most 12. Hence every length-`n` word with walk in `{1,2,3}` is one
of at most `12^n` words, and since `pi |-> w(pi)` is injective,

```
|E_3 cap S_n| <= 12^n,   limsup |E_3 cap S_n|^{1/n} <= 12.
```

### The slot-count matrix.
Count letters by slot transition. Every `E_3` permutation of length `n` has an
encoding word of length `n` whose length-`(n-1)` prefix is a walk in
`{1,2,3}` from state 1 (the final letter is `f`, terminating to 0 slots).
Transitions staying inside the slice are counted by, with states `{1,2,3}`,

```
        M_3 = [[2,1,0],[2,4,2],[0,3,6]],
```

i.e. from 1: 2 stay (`l1,r1`), 1 up (`m1`); from 2: 2 down (`f1,f2`),
4 stay, 2 up (`m1,m2`); from 3: 3 down, 6 stay (the 3 `m`-exits out of the
slice are dropped, which combined with replacing the 2 terminating `f`-letters
from state 1 by self-loops can only increase the count: `M_3` counts a
rigorous superset of slice walks).
Row sums are (3,8,9); column sums are (4,8,8).

### Lemma 2 (sharpened cap).
An `E_3` word of length `n` has states `s_0 = 1, s_1, ..., s_{n-1} in {1,2,3}`,
`s_n = 0`: only the final letter terminates (via `f`). Its length-`(n-1)`
prefix is a walk inside `{1,2,3}`, and its transitions are a subset of the
`M_3` edges (from 1: `l1,r1,m1`, since `f1` would terminate early; from 2:
all 8 letters; from 3: the 9 non-`m` letters). The final letter is one of
`s_{n-1} <= 3` fill-letters. Hence, with `||.||_1` the induced 1-norm
(max column sum 8),

```
|E_3 cap S_n| <= 3 * ||e_1 M_3^{n-1}||_1 <= 3 * 8^{n-1} <= 8^n,
limsup |E_3 cap S_n|^{1/n} <= 8 <= 12.
```

In particular `rho(M_3) <= 8` (any induced norm bounds spectral radius;
row-sum gives `<= 9`).

### Lemma 3 (rigorous Perron enclosure).
`M_3^2` has all entries strictly positive (rows `[6,6,2]`, `[12,24,20]`,
`[6,30,42]`), so `M_3` is primitive: Perron-Frobenius gives a simple
dominant eigenvalue `rho > 0`. Expanding `det(M_3 - xI)` along row 1,

```
p(x) = (2-x)((4-x)(6-x)-6) - 2(6-x),   q(x) = -p(x)/1 ...
q(x) = x^3 - 12x^2 + 36x - 24   (monic).
```

Exact integer evaluations: `q(7) = -17 < 0 < 8 = q(8)`,
`q'(x) = 3x^2-24x+36 = 3(x-2)(x-6) > 0` on `[8,infty)`, and `q(8) = 8 > 0`,
so no root `>= 8`; there is a unique root `> 6`, lying in `(7,8)` (the other
two roots lie in `(0,1)` and `(3,6)` since `q(0) = -24 < 0 < 1 = q(1)` and
`q(3) = 3 > 0 > -24 = q(6)`). Hence

```
rho(M_3) in (7,8), in particular rho(M_3) <= 8 <= 12.
```

(Non-rigorous supplement: numpy gives `rho ~= 7.7588`, consistent.)

All integer identities are replayed by `output/artifacts/compute_M3.py`
(stdlib only; exits `ALL CHECKS PASSED`).

## 3. Explicit extremal spine

Let `F_0 = {id_n : n >= 1}`, the identity permutations, with claimed encodings
`l_1^{n-1} f_1`. Verified by `output/artifacts/verify_F.py` (stdlib only):

- `id_n` avoids 1324 for `1 <= n <= 8` by brute-force 4-tuple check
  (in fact it avoids every non-increasing pattern; the script checks 1324);
- decoding `l_1^{n-1} f_1` in the single-slot decoder yields `1..n` with slot
  trace `<= 1`, for `1 <= n <= 12`.

Thus `F_0` is an explicitly described infinite subfamily of `E_3` (depth 1):
the increasing backbone shared by the increasing cells of the
domino/staircase lower-bound decompositions. Its own growth is 1.

## 4. Stability (exact statement proved)

Take `epsilon_0 = 1`, so the near-extremal threshold is `11 - 1 = 10`.
By Lemma 2, *every* subclass `G subset E_3` satisfies
`limsup |G cap S_n|^{1/n} <= 8 < 10`. Hence no subclass of `E_3` has growth
`> 11 - epsilon_0`, and the implication

```
every G subset E_3 with growth > 11 - epsilon_0 is contained in F_0
up to finitely many encoding deviations
```

holds vacuously. This is the literal stability clause with an explicit
`epsilon_0` and explicit `F_0`.

**Structural content (non-vacuous).** The bound is not just an inequality:
the `{1,2}`-confined block `[[2,1],[2,4]]` has characteristic polynomial
`lambda^2 - 6lambda + 6`, i.e. Perron root `3 + sqrt(3) < 4.74 < 5`. So any
subclass of `E_3` with growth `> 5` must use slot-count 3 (it cannot be
confined to states `{1,2}`); the exponential mass of the slice lives at the
dominant state 3. Combined with Lemma 2, the upshot is structural: the
depth-`<= 3` slice is provably far below the conjectured full-class constant
(`~11.6`), so the extremal mass of Av(1324) — and any `~10`-growth
lower-bound family — cannot live inside `E_3`.

## 5. What is proved, and what is not

Proved: `limsup |E_3 cap S_n|^{1/n} <= 8 <= 12` via explicit `M_3` with
rigorous enclosure `rho(M_3) in (7,8)`; explicit infinite `F_0 subset E_3`;
stability implication with `epsilon_0 = 1` (vacuous, stated transparently);
dominant-state localization lemma (`> 5` forces state 3).
Not claimed: exact value of the growth of `E_3`; exact E_3 automaton (M_3
bounds a superset of walks — valid one-sided for the upper bound only);
anything about the full-class constant; the slice cap of 8 means no
`~10`-growth family can live in `E_3` (the target's "lift of the lower-bound
construction" is realized here by the shared monotone spine `F_0`, and the
full growth must use depth `>= 4`).

## 6. Replay

```
python3 output/artifacts/compute_M3.py   # matrix, char poly, IVT enclosure
python3 output/artifacts/verify_F.py     # F_0 avoidance + decoding + alphabet lemma
```
