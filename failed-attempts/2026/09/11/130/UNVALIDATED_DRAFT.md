# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Quasirandom single-step book density increment with logarithmic gain — proof

## 1. Statement (target claim, exact)

Let `n ≥ 2^20`, `d = 1/2`, `ε = 10⁻⁴`. Let `G` be a simple `n`-vertex graph with

- (H1) density: `|e(G)/C(n,2) − d| ≤ ε`;
- (H2) codegree discrepancy: for `codeg(u,v) = |N(u) ∩ N(v)|`,
  `|codeg(u,v) − d²n| ≤ εn` for all but at most `εn²` unordered pairs `{u,v}`.

**Claim.** Either `G` contains a book `B₂(m)` (m distinct triangles sharing one
spine edge) with `m ≥ n/(200 ln n)`, or some `S ⊆ V(G)` with `|S| ≥ n/8`
satisfies `e(G[S]) ≥ (d + 1/(50 ln n)) · C(|S|,2)`.

Proof and explicit verified violator both count as complete resolution.
This draft proves the claim by showing the **first** disjunct always holds.

## 2. Conventions

`codeg(u,v)` counts common neighbours; the book pages on an edge `uv ∈ E(G)`
equal `codeg(u,v)`, so the maximal page count is the maximal codegree over
spine edges. Density means `e(G)/C(n,2)`.

## 3. Proof

Let `B` be the set of unordered pairs with `|codeg − d²n| > εn`; by (H2),
`|B| ≤ εn²`.

**Step 1 — a good edge exists.** By (H1),
`|E(G)| ≥ (d − ε)·C(n,2)`. Hence the number of edges outside `B` satisfies

```
|E \ B| ≥ (d − ε)·C(n,2) − εn².
```

At `n = 2^20`, `(0.4999)·C(n,2) − 10⁻⁴n² ≈ 2.747 × 10¹¹ > 0`
(machine replay in `output/artifacts/verify.py`; the same bound is positive for
every `n ≥ 2`). Fix any edge `uv ∈ E \ B`. Then

```
codeg(u,v) ≥ d²n − εn = (d² − ε)n.
```

With `d = 1/2`, `d² − ε = 0.2499`, so this edge already carries a book with at
least `0.2499n` pages.

**Step 2 — the threshold is far below.** The page threshold is
`T(n) = n/(200 ln n)`. We need `(d² − ε)n ≥ T(n)`, i.e.

```
ln n ≥ 1 / (200·(d² − ε)) ≈ 0.02001.
```

Since `n ≥ 2^20`, `ln n ≥ 20 ln 2 ≈ 13.86`, which exceeds the requirement by a
factor of about 690 (replayed numerically with 1% safety margin in
`verify.py`). Therefore

```
codeg(u,v) ≥ 0.2499n ≫ n/(200 ln n) ≈ 378 at n = 2^20.
```

So `G` contains `B₂(m)` with `m ≥ n/(200 ln n)`. The second disjunct is not
needed. ∎

## 4. Nonvacuity (the hypothesis is satisfiable)

The implication is nonvacuously true. For any prime `q ≡ 1 (mod 4)`, the Paley
graph on `q` vertices is `(q−1)/2`-regular (density exactly `1/2`), with adjacent
codegree `(q−5)/4` and non-adjacent codegree `(q−1)/4`; deviations from `d²q`
are at most `5/4`. With `ε = 10⁻⁴`, the discrepancy bound `εq` dominates `5/4`
as soon as `q ≥ 12500`, so for such Paley orders the bad set `B` is empty and
(H1)–(H2) hold, while the book on any edge has `(q−5)/4` pages — far above
`q/(200 ln q)`. An explicit large witness order is `q = 1048589` (verified
prime, `≡ 1 mod 4` in `verify.py`): density exactly `1/2`, `B = ∅`, book
`(q−1)/4 = 262147` pages versus threshold `≈ 378.2`.

Remark: raw random graphs `G(n,1/2)` do *not* satisfy (H2) at `n = 2^20`,
because codegree fluctuations there are of order `√n ≈ 1024 ≫ εn ≈ 105`.
The hypothesis is a genuinely strong discrepancy condition — satisfied by
algebraic quasirandom graphs such as Paley graphs — which is exactly why the
first disjunct follows so directly.

## 5. What is proved, and what is not

- **Proved:** under (H1)–(H2) with the stated constants, the book arm always
  holds; the claimed dichotomy is true. No density-gain extraction is needed.
- **Not claimed:** any improvement of the constants, any statement about
  `R(4,t)` itself, or any result under weaker discrepancy hypotheses.
  Constants `200` and `50` are far from sharp here (the proof gives book
  `0.2499n`, roughly 700× the threshold at `n = 2^20`).

## 6. Reproducibility

`output/artifacts/verify.py` (stdlib only) replays: (i) positivity of the
good-edge count lower bound at `n = 2^20`; (ii) the codegree-vs-threshold
inequality with a 1% safety margin plus the symbolic `ln n` margin;
(iii) exact structural facts for Paley(13); (iv) primality, congruence,
discrepancy fit, exact density, and book-vs-threshold for Paley(1048589).
Run: `python3 output/artifacts/verify.py` → `VERIFY_OK`.
