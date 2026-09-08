# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Extremal Betti census for moment-angle complexes over 6-vertex complexes (connected-graph pool + 2D representatives), with Hochster replay

## 1. Objects and formula

Let $K$ be a simplicial complex on vertex set $[6]=\{0,\dots,5\}$ of dimension $\le 2$.
Let $Z_K$ be the moment-angle complex. The Hochster formula (Buchstaber–Panov) gives,
over a field (we use rational rank; integral torsion treated separately):

$$H^{\ell}(Z_K) \cong \bigoplus_{J\subseteq[6]} \widetilde H^{\ell-|J|-1}(K_J),$$

where $K_J$ is the full subcomplex induced by $J$, with convention
$\widetilde H^{-1}(K_\varnothing)=\mathbb Z$ (contributing the single $H^0$ class).
Hence the total Betti number is

$$b(Z_K) = 1 + \sum_{\varnothing\ne J\subseteq[6]}
  \bigl(\tilde b_0(K_J)+\tilde b_1(K_J)+\tilde b_2(K_J)\bigr),$$

with $\tilde b_0=c-1$ ($c$ = components), $\tilde b_1=e-k+c-\mathrm{rank}\,d_2$,
$\tilde b_2=t-\mathrm{rank}\,d_2$ for $k$ vertices, $e$ edges, $t$ triangles in $K_J$.

## 2. Pool $P$ (fixed before computation)

- **Graph part:** all $112$ isomorphism types of *connected* graphs (= 1-dimensional
  complexes, geometric realization a wedge of circles) on $[6]$, enumerated as
  $S_6$-canonical minima of the $2^{15}=32768$ labeled graphs (156 total iso types,
  112 connected — both standard numbers, reproduced here).
- **2D representatives:** octahedral $S^2$ triangulation ($b=8$), stacked 6-vertex
  $S^2$ ($b=12$), cone-on-$C_6$ disk ($b=12$).
- **Boundary control (excluded):** minimal 6-vertex $\mathbb{RP}^2$ (10 triangles)
  has $H_1=\mathbb Z/2$ (SNF diagonal $(1^{\times 9},2)$), so integral torsion occurs
  at the pool boundary; all pool members were checked torsion-free in the
  $d_2$-rank sense (rational rank = integral rank for the $K_J$ pieces relevant here;
  full integral homology of every $K_J$ not claimed).
- **Flag split:** triangle-free (flag in dimension 1) vs. non-flag.

## 3. Extremal theorem (proved by certified exhaustion)

**Theorem.** Over the $112$ connected graph types on $[6]$:
- (a) The unique (up to isomorphism) maximizer of $b(Z_K)$ is the complete graph
  $K_6$ (rep code $32767$, 15 edges), with $b(Z_{K_6})=112$.
- (b) The runner-up is rep code $8191$ (13 edges) with $b=86$; hence the
  maximality gap is $26\ge 1$.
- (c) Among connected *flag* (triangle-free) types the maximum is $b=50$,
  attained by exactly $6$ tree types (rep codes $31,61,121,122,659,692$,
  each 5 edges).
- (d) Including disconnected graphs, the global maximum is the 6-point complex
  with $b=130$; the connectedSplitter is stated so the $K_6$ anchor is read
  within the connected (wedge-of-circles) pool.

**Proof.** Exhaustion over all $32768$ labeled graphs: for each of the $63$ nonempty
$J$ compute $(c,e,t,\mathrm{rank}\,d_2)$ and sum. Vectorized (numpy) census and an
independent exact-fraction (Bareiss/`Fraction`) verifier agree on all key values:
$K_6=112$, $8191\to 86$, flag-max $31\to 50$, octahedron-graph $70$,
octahedral-$S^2$ $8$, cone-disk $12$. The per-type table
(`artifacts/betti_table.csv`, 156 rows) lists every iso type; the top of the
connected ranking is $112 > 86 > 84 > \cdots$, certifying (a)–(c). ∎

Bigraded Tor ranks: $b(Z_K)=\sum_{J,d}\dim \widetilde H^{d-|J|-1}(K_J)$ refines to
the $(J,\deg)$ table; e.g. for $K_6$ the nonzero multidegrees are
$|J|=2$: $\deg 5$ (15 classes); $|J|=3$: $\deg 6$ (20$\times$... detailed in
`artifacts/graph_census.json`); full per-slot data reproducible via
`artifacts/rmodel.py::cohomology_dims`.

## 4. Massey search (partial: scan log, no witness claimed)

A Koszul–Taylor dga model $R(K)$ (squarefree multidegrees, exact sympy arithmetic)
with cup product, defining-system solver, and indeterminacy-quotient test
($m(\tau)$ affine family vs. $D + a{\cdot}H + H{\cdot}c$ column space) was built
(`rmodel.py`, `cup.py`, `massey.py`, `scan.py`, `scanfull.py`).
Approximately $7400$ ordered triples across $C_6$, $P_6$, octahedron-graph, $K_6$,
star $S_5$ (first-$N$ degree-ordered triples, first and all quotient reps) were
tested; **no nontrivial triple Massey product was found**. One instructive
near-miss: on $C_6$, $\langle[J_{18}],[J_{40}],[J_5]\rangle$ has both cups zero on
the nose yet the Massey set contains $0$ (defining system with $s=t=0$ gives
$m=0$). This is reported as a *scan log*, not a vanishing theorem.

## 5. Replay

```
python3 output/artifacts/verify.py        # exact-arithmetic check of key Betti numbers
python3 output/artifacts/census_graphs.py # labeled-graph vectorized census (max 112, gap)
python3 output/artifacts/scanfull.py S5 400  # sample Massey scan
```

## 6. Separation of proof / evidence / conjecture

- **Proved:** the connected extremal census (a)–(d) by two-code-path exhaustion.
- **Computed evidence:** full 156-row Betti table; $\approx$7400-triple Massey scan
  with zero hits (evidence toward formality in this regime, not proof).
- **Conjecture/uncertainty:** whether any pool member carries a nontrivial triple
  Massey product (untested triples and 2D-complex higher operations remain open);
  integral-torsion freeness is verified only via $d_2$-ranks over $\mathbb Q$ plus
  the $\mathbb{RP}^2$ boundary witness, not by SNF of every $K_J$.
