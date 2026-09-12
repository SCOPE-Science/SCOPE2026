# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact Olson data for C_4^2 and the column lower-bound theorem for (Z_N)^2

## 1. Smallest case: G = C_4^2 = (Z_4)^2 (machine-verified)

**Theorem A.** `Ol(C_4^2) = 6`. There are exactly 120 zero-sum-free subsets of
size 5 (the maximal ones). Under the linear group `GL(2,Z_4)` (order 96) they
form exactly **2 orbits**, of sizes **96** and **24** (point stabilizers of
orders 1 and 4). Representatives:

- main orbit (96): `{(0,1),(0,2),(1,0),(1,1),(1,2)}`;
- small orbit (24): `{(0,1),(1,0),(1,1),(1,2),(1,3)}`.

Translation is excluded because the action is partial on subsets of nonzero
elements: e.g. translating the main representative by `(0,3)` gives
`{(0,0),(0,1),(1,0),(1,1),(1,3)}`, which contains `(0,0)` and leaves the family.

*Proof.* Exhaustive check over all `2^15 = 32768` subsets of the 15 nonzero
elements, using reachable-sum DP: a set is zero-sum-free iff `(0,0)` is never
reached. Maximum free size is 5, attained by 120 sets. Orbit decomposition is
by direct union-find over the 96 matrices of `GL(2,Z_4)`. Reproduce with
`output/artifacts/c4_exact.py`, which prints
`maxk = 5 Ol(C4^2) = 6 count = 120`, `GL(2,Z4) size = 96`,
`GL orbits: 2 sizes: [96, 24]`.

## 2. Column lower-bound theorem (all N, hence all p)

**Theorem B.** Let `G = (Z_N)^2` with `N >= 2` and let `b >= 0` satisfy
`T_b = b(b+1)/2 < N`. Then

    S = {(1,j) : 1 <= j <= N-1} ∪ {(0,j) : 1 <= j <= b}

is zero-sum-free in `G`. Consequently `Ol(G) >= N + b`.

*Proof.* Let `T ⊆ S` be nonempty, with `r` elements from the `x = 1` column.
The `x`-coordinate of `σ(T)` is `r mod N` with `0 <= r <= N-1`. If `r >= 1`
it is nonzero mod `N`. If `r = 0`, then `T` lies in the `x = 0` column with
distinct `y`-coordinates in `{1,…,b}`, so its integer `y`-sum lies in
`[1, T_b]`, and `T_b < N` keeps it nonzero mod `N`. Either way
`σ(T) ≠ (0,0)`. ∎

For `N = p^2` this gives `Ol(C_{p^2}^2) >= p^2 + b` with
`b ~ √2·p`, i.e. a `Θ(p^2)` lower bound:

| N=p² | b | free set | Ol lower bound | Davenport upper bound 2N−1 |
|------|---|----------|----------------|----------------------------|
| 4    | 2 | 5        | 6              | 7                          |
| 9    | 3 | 11       | 12             | 17                         |
| 25   | 6 | 30       | 31             | 49                         |
| 49   | 9 | 57       | 58             | 97                         |
| 121  |15 | 135      | 136            | 241                        |

Instances with `N ≤ 9` are additionally brute-force verified by
`output/artifacts/column_theorem.py`. The bound is **tight at N = 4**: the
column 5-set `{(1,1),(1,2),(1,3),(0,1),(0,2)}` is GL-equivalent (not set-equal)
to the main-orbit representative of Theorem A, e.g. via M=(1,0,0,3),
and `Ol = 6`.

## 3. Relation to the target

The target asked for the exact `Ol(C_{p^2}^2)` for all large `p` plus full
extremal classification via an explicit Chevalley–Warning system. That goal
remains out of reach: CW degree counting only bites at `n = Ω(p^2)` with no
stability/classification content, while exhaustive search needs `2^{(p²−1)²}`
checks (infeasible already at `p = 3`). Theorems A and B are the strongest
fully proved, reproducible increments: the first exact value with orbit-level
classification (at `p = 2`) and a general `Θ(p^2)` extremal family that is
sharp in the only exactly solvable case. A first-quadrant "sum-triangle"
family conjectured mid-investigation turned out to be false (explicit
zero-sum witnesses found by DP, e.g. `(1,1)+(1,2)+(2,1) = (0,0)` mod 4);
it is recorded here only as negative evidence and plays no role in the proofs.
