# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Extremal regularity and projective dimension of edge ideals on 7–8 vertices:
certified witnesses, exact maxima in part, and exact Betti tables

## 1. Setup and conventions

Let $S=\mathbb{Q}[x_1,\dots,x_n]$ and $I(G)$ the edge ideal of a simple graph $G$.
All invariants are for the quotient $M=S/I(G)$:
$$\mathrm{reg}(M)=\max\{j-i : \beta_{i,j}(M)\ne 0\},\qquad
\mathrm{pd}(M)=\max\{i : \beta_{i,j}(M)\ne 0\}.$$
Put
$$R_n=\max\{\mathrm{reg}(S/I(G)) : G\text{ connected},\,|V|=n\},\qquad
P_n=\max\{\mathrm{pd}(S/I(G)) : G\text{ connected},\,|V|=n\}.$$
Write $\mathrm{im}(G)$ for the induced matching number, $\nu(G)$ for the
matching number, and $\mathrm{min\text{-}match}(G)$ for the minimum size of a
maximal matching.

## 2. Cited tools (not claimed as new)

- (K) Katzman: $\mathrm{im}(G)\le \mathrm{reg}(S/I(G))$.
- (W) Woodroofe / H\`a–Van Tuyl: $\mathrm{reg}(S/I(G))\le \mathrm{min\text{-}match}(G)\le \nu(G)$.
- (AB) Auslander–Buchsbaum: $\mathrm{pd}(S/I(G))+\mathrm{depth}(S/I(G))=n$.
- (H) Hochster's formula for squarefree monomial ideals: with
  $\Delta(G)$ the independence complex,
  $$\beta_{i,j}(S/I(G))=\sum_{|W|=j}\dim_\mathbb{Q}\tilde H_{j-i-1}(\Delta(G)|_W;\mathbb{Q}).$$
- (MY) Matsuda–Yoshida, arXiv:2112.15297: classification of realizable
  $(\mathrm{reg},\mathrm{min\text{-}match},\nu,n)$ tuples for connected graphs.
  Per the admission review, (MY) implies $R_8\le 3$. This is used only for the
  conditional sharpening in Theorem 1(c); everything else is proved or computed here.

## 3. Results

### Theorem 1 (proved here, modulo the labelled citation).
(a) $R_7=3$. (b) $P_7=6$ and $P_8=7$.
(c) $R_8\in\{3,4\}$ unconditionally; $R_8=3$ assuming (MY).

### Theorem 2 (computed exact Betti tables, doubly verified).
The four graphs below (edge lists in §4) have the stated graded Betti numbers
$\beta_{i,j}(S/I(G))$ over $\mathbb{Q}$, each verified by two independent
exact homology pipelines over all $2^n$ subsets plus a per-subset Euler
identity replay with zero mismatches (logs in `output/artifacts/betticensus.json`):

- $K_7$: reg $1$, pd $6$; $K_8$: reg $1$, pd $7$ (both also match the closed form
  $\beta_{i,i+1}=\binom{n}{i+1}\cdot i$ for $1\le i\le n-1$).
- $G_{7}^{\mathrm{reg}}$: reg $3$, pd $4$; $G_{8}^{\mathrm{reg}}$: reg $3$, pd $5$.

### Proofs.

**Lemma (depth $\ge 1$).** Let $G$ have $\ge 2$ vertices and $\ge 1$ edge.
Then $\mathrm{depth}(S/I(G))\ge 1$, hence $\mathrm{pd}(S/I(G))\le n-1$.
*Proof.* $I(G)$ is squarefree monomial, so associated primes are exactly the
minimal vertex covers. The full set $\{1,\dots,n\}$ is a vertex cover but never
minimal for $n\ge 2$: deleting any single vertex leaves a vertex cover, since
every edge incident to the deleted vertex is still covered by its other endpoint
(no loops). Hence the maximal ideal is not associated, i.e. it contains a
non-zerodivisor. By (AB), $\mathrm{pd}\le n-1$. ∎

**Part (b).** The Lemma gives $P_7\le 6$, $P_8\le 7$. The complete graphs attain
them: the certified Betti tables of $K_7,K_8$ show $\mathrm{pd}=6,7$
(top Betti entries $(6,7)$ and $(7,8)$ nonzero). Hence $P_7=6$, $P_8=7$ exactly.

**Part (a).** For any 7-vertex graph, (W) gives
$\mathrm{reg}\le\mathrm{min\text{-}match}\le\nu\le\lfloor 7/2\rfloor=3$, so
$R_7\le 3$. The connected witness $G_{7}^{\mathrm{reg}}$ below has the exhibited
induced matching of size $3$, so (K) gives $\mathrm{reg}\ge 3$; indeed its
independent sandwich $\mathrm{im}=\mathrm{min\text{-}match}=3$ forces
$\mathrm{reg}=3$ by (K)+(W) alone. Hence $R_7=3$.

**Part (c).** For $n=8$, (W) gives $\mathrm{reg}\le\nu\le 4$, so $R_8\le 4$.
$G_{8}^{\mathrm{reg}}$ has $\mathrm{im}=\mathrm{min\text{-}match}=3$, forcing
$\mathrm{reg}=3$, so $R_8\ge 3$; i.e. $R_8\in\{3,4\}$ unconditionally.
Assuming (MY) which implies $R_8\le 3$, $R_8=3$.

## 4. Witness graphs (0-based labels)

- $G_{7}^{\mathrm{reg}}$: $n=7$, edges
  `{(0,1),(2,3),(4,5),(6,1),(6,3),(6,5)}` (three disjoint edges tied by hub 6).
  Connected. Induced matching: `{(0,1),(2,3),(4,5)}` (size 3; no other edge
  inside $\{0,\dots,5\}$). Minimal maximal matching: the same triple (size 3;
  the hub edges are all hit; exhaustive search over $2^6$ matchings confirms no
  maximal matching is smaller). Hence $\mathrm{im}=\mathrm{min\text{-}match}
  =\nu=3$, forcing reg $3$.
- $G_{8}^{\mathrm{reg}}$: $n=8$, edges
  `{(0,1),(2,3),(4,5),(6,1),(6,3),(6,5),(7,0)}` ($G_7$ plus pendant 7 at 0).
  Connected. Induced matching `{(0,1),(2,3),(4,5)}` size 3 (vertex 7 unused).
  Minimal maximal matching: same triple, size 3 (edge $(7,0)$ hit by 0;
  exhaustive search over $2^7$ matchings confirms minimality). Maximum matching
  `{(2,3),(4,5),(6,1),(7,0)}` size 4. Hence $\mathrm{im}=\mathrm{min\text{-}match}
  =3<\nu=4$, forcing reg $3$.

## 5. Exact Betti tables (Hochster, $\beta_{i,j}$ listed as $(i,j,\beta)$)

- $K_7$ (reg 1, pd 6):
  `(0,0,1),(1,2,21),(2,3,70),(3,4,105),(4,5,84),(5,6,35),(6,7,6)`.
- $K_8$ (reg 1, pd 7):
  `(0,0,1),(1,2,28),(2,3,112),(3,4,210),(4,5,224),(5,6,140),(6,7,48),(7,8,7)`.
- $G_{7}^{\mathrm{reg}}$ (reg 3, pd 4):
  `(0,0,1),(1,2,6),(2,3,6),(2,4,3),(3,4,1),(3,5,3),(3,6,1),(4,7,1)`.
- $G_{8}^{\mathrm{reg}}$ (reg 3, pd 5):
  `(0,0,1),(1,2,7),(2,3,7),(2,4,7),(3,4,1),(3,5,10),(3,6,2),(4,6,3),(4,7,3),(5,8,1)`.

## 6. Verification performed (and what was NOT done)

- Betti numbers computed from (H) by enumerating all $2^7=128$ / $2^8=256$
  subsets; each subset's reduced homology over $\mathbb{Q}$ computed by exact
  integer boundary matrices with **two independent rank routines**:
  stdlib `Fraction` Gauss–Jordan and `sympy.Matrix.rank`. The two pipelines
  agree on every Betti number of all four graphs.
- Independent Euler replay: for every nonempty $W$,
  $\sum_{\emptyset\ne F\in\Delta|_W}(-1)^{|F|-1}=\sum_k(-1)^k\dim\tilde H_k+1$
  checked from face enumeration vs. computed homology: 0 mismatches
  (127/127 subsets for $n=7$, 255/255 for $n=8$, all four graphs).
- $K_n$ tables additionally match the closed form
  $\beta_{i,i+1}=\binom{n}{i+1}i$ exactly.
- Matching certificates by exhaustive search over all $2^m$ edge subsets
  ($m\le 28$): largest induced matching, largest matching, smallest maximal
  matching, each with exhibited witness stored in the log.
- NOT done (stated honestly): no complete census over the 853+11117 types
  (infeasible in this environment: no nauty/geng, no CAS); no Taylor-to-minimal
  differential matrices; characteristic-dependence not studied (all homology
  over $\mathbb{Q}$); minimality of pd witnesses is by the Lemma upper bound,
  minimality of $R_8$ upper bound $3$ rests on cited (MY), not proved here.

## 7. How to reproduce

Run `python3 output/artifacts/compute.py` (needs only stdlib + sympy; sympy
present as 1.12 here). It regenerates `output/artifacts/betticensus.json`
with edges, connectivity, all matching witnesses, both-pipeline Betti tables,
agreement flags, and Euler counters. Expected runtime: seconds.

## 8. Status of the original target

The full 7–8-vertex Betti census with record-vs-runner-up separation remains
open. The fallback interval-table direction is partially advanced: this report
delivers exact proved maxima $R_7,P_7,P_8$, the interval $R_8\in\{3,4\}$
($=3$ under (MY)), four fully certified Betti tables, and a reusable exact
Hochster audit script — a citable extremal fragment, not the complete census.
