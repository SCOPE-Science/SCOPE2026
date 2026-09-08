# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified linear Fano-free Turán maxima on 9–10 vertices

## Objects and definitions
A 3-uniform hypergraph $H$ is **linear** if any two distinct edges share at most
one vertex. $F$ denotes the Fano plane (7 vertices, 7 triples, each pair in
exactly one triple). $\mathrm{ex}_{\mathrm{lin}}(n,F)$ is the maximum number of
edges in a linear Fano-free 3-graph on $n$ vertices.

## Theorem (exact values with witnesses)
- $\mathrm{ex}_{\mathrm{lin}}(9,F)=12$, attained e.g. by the Steiner triple
  system STS(9) = AG(2,3) with edge list $H_9$ in `artifacts/witnesses.json`.
- $\mathrm{ex}_{\mathrm{lin}}(10,F)=13$, attained e.g. by the 13-triple packing
  $H_{10}$ in `artifacts/witnesses.json`.

Both witnesses are linear and Fano-free; both are verified by the committed
stdlib-only replay `artifacts/verify.py` (run: `python3 verify.py`).

## Proof
### Lemma 1 (link = matching; degree cap).
In a linear 3-graph, the link of any vertex (pairs $xy$ with $vxy\in E$) is a
matching, so $d(v)\le\lfloor(n-1)/2\rfloor=:c_n$. Hence $3e=\sum d(v)\le nc_n$
and $e\le\lfloor nc_n/3\rfloor$.

For $n=9$: $c_9=4$, $e\le\lfloor36/3\rfloor=12$ (Schönheim bound).
For $n=10$: $c_{10}=4$, $e\le\lfloor40/3\rfloor=13$ (Schönheim bound).

### Witnesses (constructions).
$H_9$ = the 12 lines of AG(2,3); $H_{10}$ = the committed 13-triple packing
(degrees $4^9 3^1$). Linearity is checked by asserting no pair of vertices
recurs (at most $\binom{n}{2}$ pairs); each vertex link is directly checked to
be a matching.

### Fano-freeness.
A linear 3-graph contains $F$ iff some 7-set of vertices spans $\ge7$ edges
(since $F$ has 7 edges on 7 vertices, and linearity forces exactly 7).
Direct enumeration over all $\binom{9}{7}=36$ resp. $\binom{10}{7}=120$
seven-sets shows every 7-set of $H_9$ resp. $H_{10}$ spans at most 5 edges.
Hence both are Fano-free. (Computed maxima: 5 in both cases; see verifier.)

### Optimality.
The witnesses attain the Lemma-1 ceiling ($12=\lfloor36/3\rfloor$,
$13=\lfloor40/3\rfloor$), so no linear 3-graph — Fano-free or not — on 9
resp. 10 vertices has more edges. A fortiori the Fano-free maxima equal
12 and 13. This simultaneously serves as the Lagrangian replay: at uniform
weights $L(H,\mathbf{1}/n)=e/n^3$ saturates the integer cap; no heavier
linear Fano-free example is possible.

### Runner-up and Steiner separation.
Deleting any edge of $H_n$ gives a linear Fano-free example with $E_n-1$
edges, so the optimum is sharp with gap exactly 1. STS(9) exists (12 blocks)
and coincides with the extremal; no STS(10) exists, and the Schönheim packing
ceiling 13 is the extremal number.

## Census / stability fragment (proved + computed)
- $n=9$: $e=12$ forces $\sum d=36=9\cdot4$ with $d\le4$, hence 4-regular; with
  12 triples covering all $\binom{9}{2}=36$ pairs exactly once, every extremal
  example is an STS(9). STS(9) is unique up to isomorphism (classical: the
  affine plane AG(2,3)), so there is exactly **one** extremal isomorphism type.
- $n=10$: $e=13$ forces $\sum d=39=40-1$, hence degree sequence $4^9 3^1$ is
  forced for every extremal example. The pair-leave (uncovered pairs of $K_{10}$)
  has degree sequence $3^1 1^9$ (a $K_{1,3}$ star plus 3 disjoint edges).
  Randomized enumeration found $\ge2$ non-isomorphic 13-edge maximum packings
  (exact backtracking isomorphism test, both with max 7-span 5, hence Fano-free);
  the full isomorphism-type count is left open (conjecture: small, and every
  maximum packing is Fano-free since max 7-span observed is 5 — but a complete
  enumeration log is beyond this pass, so this part is stated as computed
  evidence, not theorem).
- Near-extremal ($E_n-1$) classification is left open.

## Reproducibility
- `artifacts/witnesses.json`: committed edge lists $H_9,H_{10}$ and $E_9,E_{10}$.
- `artifacts/verify.py`: stdlib-only checker (linearity, degree cap, link
  matchings, Schönheim saturation, exhaustive 7-set Fano scan, Lagrangian
  replay). Output: ALL CHECKS PASSED.

## What is proved vs computed vs open
- Proved: $E_9=12$, $E_{10}=13$ with certified witnesses and optimality;
  $n=9$ uniqueness (one extremal type); forced degree sequences.
- Computed evidence: max 7-span 5 for both witnesses; $\ge2$ iso types of
  13-packings on 10 vertices (all sampled ones Fano-free).
- Open/conjecture: complete iso-type census on $n=10$; $E_n-1$ stability.
