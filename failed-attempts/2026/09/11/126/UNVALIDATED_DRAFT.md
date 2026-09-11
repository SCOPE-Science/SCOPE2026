# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Three-edge dichotomy for a semilattice-quotient 4-element Taylor square algebra (lane-1022)

## 1. The algebra A3 (explicit tables)

Universe `A = {0,1,2,3}` with idempotent operations

- `s3(x,y) = max(x,y)` (chain semilattice for `0<1<2<3`);
- `m3(x,y,z) = median(x,y,z)` (chain median);
- cyclic Taylor term `c3 = m3`;
- candidate 3-edge term `e(x1,x2,x3,x4) = m3(x2,x3,x4)`.

`s3` table (rows x, cols y): entry `max(x,y)`:

|   | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 3 |
| 1 | 1 | 1 | 2 | 3 |
| 2 | 2 | 2 | 2 | 3 |
| 3 | 3 | 3 | 3 | 3 |

`m3` is the median (middle value after sorting); `e` is given by the formula
above on all 256 quadruples (full table in `artifacts/edge_table.json`).

Congruence `theta` has blocks `{0,1} | {2,3}`. Block map `b(v) = 0` for
`v in {0,1}`, `b(v) = 1` for `v in {2,3}`.

## 2. What is verified (machine-checked, stdlib only)

Replay: `python3 output/artifacts/verify_A3.py` prints `OVERALL: ALL_PASS`
(log: `output/artifacts/verify_A3.log`).

1. **Idempotence.** `s3(x,x)=x`, `m3(x,x,x)=x`, `e(x,x,x,x)=x` (all x).
2. **`s3` is a semilattice.** Commutative, associative, idempotent (64/64
   associativity triples).
3. **`m3` is a majority operation** (hence both blocks have majority
   behaviour): `m3(x,x,y)=m3(x,y,x)=m3(y,x,x)=x` for all x,y (16 cases each).
4. **`theta` is a congruence** for `s3` and `m3`:
   `b(max(a,b)) = max(b(a),b(b))` (16/16);
   `b(med(a,b,c)) = med(b(a),b(b),b(c))` (64/64). Holds because the blocks
   are intervals of the chain.
5. **Quotient.** `s3/theta` on `{B0,B1}` is the 2-element max semilattice
   (`B0+B0=B0`, all other sums `B1`); `m3/theta` is the 2-element majority
   operation. Semilattice laws verified on the quotient.
6. **Block closure.** `{0,1}` and `{2,3}` are closed under `s3`,`m3`, and
   `m3` restricts to a majority operation on each.
7. **Taylor.** `c3=m3` is symmetric, hence cyclic, and idempotent: an
   explicit cyclic (hence Taylor) term.
8. **Congruence distributivity (Jonsson).** With `d0(x,y,z)=x`,
   `d1(x,y,z)=m3(x,y,z)`, `d2(x,y,z)=z`:
   `d1(x,x,z)=x=d0(x,x,z)` (16/16), `d1(x,z,z)=z=d2(x,z,z)` (16/16),
   `d1(x,y,x)=x` (16/16). So `V(A3)` is congruence distributive.
9. **3-edge term (all formulations covered).** For `e(x1..x4)=m3(x2,x3,x4)`:
   `e(y,y,x,x)=x` (16/16), `e(y,x,y,x)=x` (16/16), `e(y,x,x,y)=x` (16/16),
   `e(x,x,y,x)=x` (16/16, Berman i=3), `e(x,x,x,y)=x` (16/16, Berman i=4).
   In particular the canonical Berman 3-edge triple holds. Full 256-row
   table exported with quotient projections.
10. **Quotient coherence.** `e` preserves `theta` (all 65536 pairs of
    quadruples), and the induced quotient operation is
    `E(B2,B3,B4) = maj(B2,B3,B4)` on all 256 quadruples (256/256).
11. **Two-generated subalgebras** (closure under `s3`,`m3`):
    `Sg(0,0)={0}`, `Sg(0,1)={0,1}`, `Sg(0,2)={0,2}`, `Sg(0,3)={0,3}`,
    `Sg(1,1)={1}`, `Sg(1,2)={1,2}`, `Sg(1,3)={1,3}`, `Sg(2,2)={2}`,
    `Sg(2,3)={2,3}`, `Sg(3,3)={3}`; singletons are subuniverses; no pair
    generates the whole algebra.
12. **No smooth loop-free obstruction.** Exhaustive census over all
    `2^12 = 4096` loop-free digraphs on `{0,1,2,3}`: a digraph is kept iff
    it is smooth (every vertex has an in- and an out-neighbour) and
    compatible with both `s3` and `m3` (closure of the edge relation under
    the operations coordinatewise). Count of survivors: **0**. Hence no
    quotient-compatible (indeed no) loop-free smooth obstruction digraph
    exists for this A3.

## 3. Decision

A3 satisfies every structural requirement in the problem statement
(idempotent, Taylor via an explicit cyclic term, genuine `{0,1}|{2,3}`
congruence, semilattice quotient, majority inside each block), and it
admits the quotient-coherent 4-ary idempotent 3-edge term
`e(x1,x2,x3,x4) = m3(x2,x3,x4)` verified on all 256 quadruples, so it
generates a congruence-distributive variety. The Hobby–McKenzie
dichotomy resolves **positively** for this square type. The corroborating
census (zero loop-free smooth compatible digraphs) is consistent with the
positive verdict.

## 4. Replay

```
python3 output/artifacts/verify_A3.py
```

reads no input, checks every identity above, writes
`output/artifacts/edge_table.json` (256 rows) and
`output/artifacts/verify_A3.log`, and exits 0 iff all checks pass.
