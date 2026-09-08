# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified transversal counts and orthogonal-mate witnesses for the group-based Latin squares of orders 7 and 8

## 1. Objects and notation

A **Latin square** of order `n` is an `n × n` array over symbols `{0,…,n−1}` with each
symbol once per row and column. A **transversal** is a set of `n` cells, one per row,
column, and symbol; `T(L)` is the number of transversals. `τ(L)` is the maximum size of
a partial transversal (distinct rows, columns, symbols). An **orthogonal mate** of `A`
is a Latin square `B` with all `n²` ordered pairs `(A[i][j],B[i][j])` distinct
(a Graeco–Latin pair). A mate exists iff the `n²` cells partition into `n` disjoint
transversals (the symbol classes of `B`), so `T(A) = 0` implies no mate.

For a finite group `G = {g_0,…,g_{n−1}}`, the **Cayley table** `L[i][j] = index(g_i·g_j)`
is a Latin square. Up to isomorphism there is 1 group of order 7 (`C7`) and 5 groups of
order 8: cyclic `C8`, `C4×C2`, elementary abelian `C2³` (XOR table), dihedral `D8`,
quaternion `Q8`. These give canonical, regeneration-from-definition (not copied)
benchmark squares at the two target orders, including the transversal-free cyclic
order-8 case and mates at both orders.

**Element orders used.**
`C7`: `0..6`, `a+b mod 7`.
`C8`: `0..7`, `a+b mod 8`.
`C4×C2`: elements `(a,b)`, `a∈Z4, b∈Z2`, listed `(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(3,1)` → labels `0..7`; product componentwise.
`C2³`: labels `0..7`, product XOR.
`D8`: `{(i,j): j∈{0,1}, i∈Z4}` listed `(0,0),(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(3,1)` → `0..7`;
  `(i,j)·(k,l) = (i+(−1)^j·k mod 4, j+l mod 2)`.
`Q8`: units `{1,i,j,k} = {0,1,2,3}` with signed products
  `1²=2²=3²=−1`, `1·2=3, 2·3=1, 3·1=2` (cyclic, positive), reversed products negative;
  elements `(sign,unit)`, `sign∈{0,1}`, listed `(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3)` → `0..7`.

## 2. Theorem (verified finite benchmark)

Let `L(G)` be the Cayley table above. Then:

| square | order | T (exact) | τ | orthogonal mate? |
|---|---|---|---|---|
| `L(C7)` | 7 | **133** | 7 | **yes** (formula mate below) |
| `L(C8)` | 8 | **0** | **7** | **no** (T=0 forbids partition into 8 transversals) |
| `L(C4×C2)` | 8 | **384** | 8 | **yes** (explicit mate) |
| `L(C2³)` | 8 | **384** | 8 | **yes** (GF(8) mate) |
| `L(D8)` | 8 | **384** | 8 | **yes** (explicit mate) |
| `L(Q8)` | 8 | **384** | 8 | **yes** (explicit mate) |

Moreover the mate `B7` of `L(C7)` itself satisfies `T(B7) = 133`.

All counts are by exhaustive `n!`-permutation scans (`7! = 5040`, `8! = 40320` per
square — trivially replayable); group axioms, Latin property, witnesses, and the
`τ(L(C8)) = 7` maximum (exact row-by-row backtracking search) are checked by the
accompanying stdlib-only script `artifacts/verify.py`, which prints 40 `PASS` lines
and writes `artifacts/results.json`.

## 3. Explicit squares

### 3.1 Order 7
`A7 = L(C7)`, `A7[i][j] = (i+j) mod 7`:
```
0 1 2 3 4 5 6
1 2 3 4 5 6 0
2 3 4 5 6 0 1
3 4 5 6 0 1 2
4 5 6 0 1 2 3
5 6 0 1 2 3 4
6 0 1 2 3 4 5
```
Orthogonal mate `B7[i][j] = (2i+j) mod 7`:
```
0 1 2 3 4 5 6
2 3 4 5 6 0 1
4 5 6 0 1 2 3
6 0 1 2 3 4 5
1 2 3 4 5 6 0
3 4 5 6 0 1 2
5 6 0 1 2 3 4
```
Transversal witness for `A7` (column per row): `[0,1,2,3,4,5,6]` (main diagonal;
symbols `2i mod 7`, a permutation since 2 is prime to 7).

### 3.2 Order 8 — hosts
`L(C8)`: `L[i][j]=(i+j) mod 8` (cyclic; transversal-free, τ=7 — see §4).
`L(C4×C2)`:
```
0 1 2 3 4 5 6 7
1 0 3 2 5 4 7 6
2 3 4 5 6 7 0 1
3 2 5 4 7 6 1 0
4 5 6 7 0 1 2 3
5 4 7 6 1 0 3 2
6 7 0 1 2 3 4 5
7 6 1 0 3 2 5 4
```
`L(C2³)` (XOR): row `i` is `i^j`:
```
0 1 2 3 4 5 6 7
1 0 3 2 5 4 7 6
2 3 0 1 6 7 4 5
3 2 1 0 7 6 5 4
4 5 6 7 0 1 2 3
5 4 7 6 1 0 3 2
6 7 4 5 2 3 0 1
7 6 5 4 3 2 1 0
```
`L(D8)`:
```
0 1 2 3 4 5 6 7
1 2 3 0 5 6 7 4
2 3 0 1 6 7 4 5
3 0 1 2 7 4 5 6
4 7 6 5 0 3 2 1
5 4 7 6 1 0 3 2
6 5 4 7 2 1 0 3
7 6 5 4 3 2 1 0
```
`L(Q8)`:
```
0 1 2 3 4 5 6 7
1 4 3 6 5 0 7 2
2 7 4 1 6 3 0 5
3 2 5 4 7 6 1 0
4 5 6 7 0 1 2 3
5 0 7 2 1 4 3 6
6 3 0 5 2 7 4 1
7 6 1 0 3 2 5 4
```

### 3.3 Order 8 — orthogonal mates (each checked Latin with 64 distinct pairs)
`BV8` from the GF(8) construction (§5):
```
0 1 2 3 4 5 6 7
2 3 0 1 6 7 4 5
4 5 6 7 0 1 2 3
6 7 4 5 2 3 0 1
3 2 1 0 7 6 5 4
1 0 3 2 5 4 7 6
7 6 5 4 3 2 1 0
5 4 7 6 1 0 3 2
```
Mate of `L(C4×C2)`:
```
1 0 2 5 7 3 4 6
4 3 0 6 5 2 1 7
7 1 3 4 6 0 2 5
6 4 7 1 2 5 3 0
0 6 1 3 4 7 5 2
2 5 4 0 1 6 7 3
3 7 5 2 0 4 6 1
5 2 6 7 3 1 0 4
```
Mate of `L(D8)`:
```
1 0 2 5 3 4 7 6
5 1 0 2 7 6 3 4
6 7 4 3 5 0 1 2
4 3 6 7 2 5 0 1
0 5 3 1 6 2 4 7
3 2 1 0 4 7 6 5
2 6 7 4 0 1 5 3
7 4 5 6 1 3 2 0
```
Mate of `L(Q8)`:
```
1 0 2 4 3 6 7 5
5 2 0 1 4 7 6 3
6 1 5 7 0 3 4 2
7 4 1 6 2 5 3 0
0 7 4 3 6 2 5 1
3 5 7 0 1 4 2 6
2 6 3 5 7 0 1 4
4 3 6 2 5 1 0 7
```

Transversal witnesses (columns per row): `C4×C2`: `[0,2,3,4,5,7,6,1]`;
`C2³`: `[0,2,4,6,3,1,7,5]`; `D8`: `[0,1,4,5,3,2,7,6]`; `Q8`: `[0,1,3,2,6,7,5,4]`.

## 4. The transversal-free cyclic order-8 square

Exhaustive scan of all `8! = 40320` permutations finds **no** transversal of `L(C8)`,
so `T = 0`. Exact maximum-partial-transversal search (row-by-row backtracking with
remaining-rows pruning) returns maximum 7, with witness cells
`(1,0),(2,1),(3,2),(4,3),(5,5),(6,6),(7,7)`:
rows `{1..7}`, columns `{0,1,2,3,5,6,7}`, symbols (from `(i+j) mod 8`)
`{1,3,5,7,2,4,6}` — seven distinct rows, columns, symbols. Hence `τ(L(C8)) = 7`:
a near-transversal exists but no full transversal. Since an orthogonal mate is
equivalent to a partition of the 64 cells into 8 disjoint full transversals,
`L(C8)` has **no** orthogonal mate. (The other four order-8 group tables, with
`T = 384`, do — see §3.3; each mate was found by transversal-partition DFS and then
independently verified.)

## 5. Constructions used for the mates

*Order 7.* `A7[i][j] = i+j`, `B7[i][j] = 2i+j (mod 7)`. `B7` is Latin (each row/column
a permutation); the pairs `{(i+j, 2i+j)}` are distinct: if two cells gave the same
pair, subtracting gives `i = i'`, then `j = j'`. So 49 distinct pairs — orthogonal.

*Order 8, `C2³`.* Work in `GF(8) = GF(2)[t]/(t³+t+1)` with elements as 3-bit ints and
reduction `0b1011` on overflow. `c = t = 2` is primitive (`c⁷ = 1`, checked); the map
`i ↦ c·i` permutes nonzero elements and fixes 0, so `C = [0,2,4,6,3,1,7,5]` is a
permutation. `A[i][j] = i^j`, `B[i][j] = (c·i)^j` are both Latin (XOR with a fixed
permuted row index), and pairs are distinct: equal pairs give `i^j = i'^j'`,
`(c·i)^j = (c·i')^j'`, XOR-ing gives `i^i' = c·(i^i')`, forcing `i = i'` (since
`c ≠ 1`), then `j = j'`. 64 distinct pairs — orthogonal.

*Order 8, others.* Enumerate all 384 transversals per square, then DFS-partition the
64 cells into 8 disjoint transversals (succeeds in ≤ 36 nodes); the transversal index
at each cell defines the mate, verified Latin + orthogonal afterward.

## 6. Proof vs computation vs conjecture (separation)

*Proof (human-checkable):* orthogonality arguments for `B7` and `BV8` in §5;
`T = 0 ⇒ no mate` implication; group-law definitions.
*Computed evidence (machine-replayed):* group axioms; Latin property of all 11
arrays; exact counts `T ∈ {133, 0, 384}` by exhaustive permutation scans;
`τ(L(C8)) = 7` by exact backtracking; Latin + 64-pair checks for the 5 mates;
`T(B7) = 133`. All replay via `python3 artifacts/verify.py` (stdlib only, seconds).
*Conjecture / not claimed:* nothing about the remaining 141 main classes / 558+
isotopy classes of order 7; the full 564-class census of the topic statement is
explicitly **not** claimed here.

## 7. Limitations and scope

1. This is a **partial theorem**: the complete group-isomorphism-type stratum
   (1+5 canonical squares), not the full 147-main-class / 564-isotopy-class census.
2. Novelty is in the combined certified table + replayable witnesses, not in the
   well-known group classification or the known principle that cyclic even-order
   tables are transversal-free.
3. Counts are exact for these squares but say nothing about non-group-based
   order-7/8 classes; no general existence theorem is claimed.

## 8. Reproduction

```
python3 output/artifacts/verify.py   # 40 PASS lines, writes results.json, exit 0
```
Requires only Python 3 stdlib. Rerun time: seconds (6 × n! scans + backtracking).
Artifacts: `output/artifacts/verify.py`, `output/artifacts/results.json`,
`output/artifacts/verify.log`.
