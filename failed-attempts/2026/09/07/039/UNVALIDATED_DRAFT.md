# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Explicit certified non-bipartite cubic Ramanujan 2-lift tower from the Petersen base

## Setup and conventions

Let $G_0$ be the Petersen graph on vertices $\{0,\dots,9\}$: outer $5$-cycle
$(0,1,2,3,4)$, spokes $(i,5+i)$, inner star $(5+i,5+(i+2 \bmod 5))$.
Fix the edge order

| idx | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| edge | (0,1) | (1,2) | (2,3) | (3,4) | (4,0) | (0,5) | (1,6) | (2,7) | (3,8) | (4,9) | (5,7) | (6,8) | (7,9) | (8,5) | (9,6) |

$G_0$ is $3$-regular with spectrum $\{3^1,1^5,-2^4\}$.
For a signing $s:E\to\{+1,-1\}$, the **2-lift** has vertices
$(v,\epsilon)$, $v\in V$, $\epsilon\in\{0,1\}$, and for each edge
$e=(u,v)$ with sign $+1$ the lifts $(u,0)-(v,0)$, $(u,1)-(v,1)$,
with sign $-1$ the crossed lifts $(u,0)-(v,1)$, $(u,1)-(v,0)$.
The lift is $3$-regular with $2|V|$ vertices; its spectrum is
$\mathrm{Spec}(A)\cup\mathrm{Spec}(A_s)$ where $A$ is the base adjacency
matrix and $A_s$ the signed adjacency matrix. A lift is Ramanujan if every
**new** eigenvalue (of $A_s$) and every nontrivial old one satisfies
$|\lambda|\le 2\sqrt{2}\approx 2.828$.

Switching: negating all signs incident to one vertex preserves the lift
isomorphism class. Fixing a spanning tree to $+1$ gives one representative
per switching class; exhaustive search over classes is exhaustive over lifts.

## Explicit signings

**Signing $s_1$** (on $G_0$, $+1$ except $-1$ on edges $7,8,14$):
$$s_1=(+1,+1,+1,+1,+1,+1,+1,-1,-1,+1,+1,+1,+1,+1,-1).$$
I.e. the three $-1$ edges are $(2,7)$, $(3,8)$, $(9,6)$.

**Graph $G_1$** is the 2-lift of $(G_0,s_1)$: $20$ vertices, $30$ edges,
enumerated in `artifacts/G1.json` (edge $k$ of $G_1$ listed in file order).

**Signing $s_2$** (on $G_1$, in the `G1.json` edge order; $-1$ exactly on
edges $3,7,9,22,23,24,25,27$):
$$s_2=(+1,+1,+1,-1,+1,+1,+1,-1,+1,-1,+1,+1,+1,+1,+1,+1,+1,+1,+1,+1,+1,+1,-1,-1,-1,-1,+1,-1,+1,+1).$$
In endpoint form: $-1$ on $(11,12)$, $(13,14)$, $(14,10)$, $(6,8)$,
$(16,18)$, $(7,9)$, $(17,19)$, $(18,15)$; $+1$ elsewhere.

**Graph $G_2$** is the 2-lift of $(G_1,s_2)$: $40$ vertices, $60$ edges,
enumerated in `artifacts/G2.json`.

## Theorem

1. The signed Petersen matrix $A_{s_1}$ has characteristic polynomial
   $x^4(x^2-5)^3$. Hence the new spectrum of the lift is
   $\{\sqrt5^3,0^4,-\sqrt5^3\}$ and $\rho(A_{s_1})=\sqrt5\approx 2.236$.
2. $G_1$ is connected, non-bipartite, $3$-regular on $20$ vertices with
   spectrum $\{3,\sqrt5^3,1^5,0^3,-2^4,-\sqrt5^3\}$; so
   $\lambda(G_1)=\sqrt5<2\sqrt2$ (Ramanujan), girth $5$, diameter $5$.
3. No signing of the Petersen graph gives new spectral radius below
   $\sqrt5$: exhaustive search over all $2^6=64$ switching classes attains
   minimum $\sqrt5$ (two complementary classes); the next-best class has
   $\rho\approx 2.5616$. So $s_1$ is switching-class optimal.
4. The signed $G_1$ matrix $A_{s_2}$ has characteristic polynomial
   $$x^{20}-30x^{18}+375x^{16}-2540x^{14}+10175x^{12}-24766x^{10}
     +36345x^8-31000x^6+14320x^4-3200x^2+256,$$
   factored as
   $$(x^2-2x-1)(x^2+2x-1)\,(x^8-12x^6+43x^4-52x^2+16)^2.$$
   Every root satisfies $|x|\le 13/5=2.60<2\sqrt2$ (certificate below).
   Hence all new eigenvalues of the $G_1\to G_2$ lift are $\le 2.60$ in
   absolute value.
5. $G_2$ is connected, non-bipartite, $3$-regular on $40$ vertices with
   $\lambda(G_2)\approx 2.58163\le 2.60<2\sqrt2$ (Ramanujan), girth $5$,
   diameter $6$.

Items 1–3 are exact (integer characteristic polynomial plus finite
enumeration); item 4 uses exact factoring plus a rigorous rational Sturm /
calculus certificate with no floating-point trust; item 5 combines 1–4 with
machine-checkable BFS facts (connectivity, bipartiteness, girth, diameter).

## Proof of the stage-2 bound (rigorous, no numerics trusted)

Write the degree-8 factor as $q(x)=r(x^2)$ with
$r(y)=y^4-12y^3+43y^2-52y+16$.
Claim: all roots $y$ of $r$ satisfy $|y|\le 169/25$, so all roots $x$ of $q$
satisfy $|x|\le 13/5=2.60$.

Indeed $r$ has Sturm sequence of length $5$ (computed exactly over
$\mathbb{Q}$); sign variations give $4$ distinct real roots total and
$0$ roots in $(169/25,\infty)$ and $0$ in $(-\infty,-169/25)$.
Equivalently, by hand-checkable rationals: with $B=169/25$,
- $r(B)=4202396/390625>0$, $r'(B)=1873586/15625>0$,
  $r''(y)=12y^2-72y+86=12(y-3)^2-22\ge 12(94/25)^2-22=92282/625>0$
  for $y\ge B$, so $r$ is strictly increasing from a positive value on
  $[B,\infty)$: no root there;
- $r(-B)=3174912796/390625>0$, $r'(-B)=-54908386/15625<0$,
  and $r''(y)>0$ for $y\le -B$ a fortiori (since $(y-3)^2\ge 9$), so $r$
  is strictly decreasing on $(-\infty,-B]$ from $+\infty$ down to a
  positive value: no root there.

The quadratic factors give $x=\pm 1\pm\sqrt2$; since $2<64/25=(8/5)^2$,
$|x|\le 1+8/5=13/5$. All four numbers $\pm1\pm\sqrt2$ are $<13/5$ in absolute
value (the largest is $1+\sqrt2<2.6$). The squared degree-8 factor only
doubles multiplicities. This proves item 4 with $\lambda\le 2.60$.
Numerically the largest new magnitude is $\approx 2.58163$ (a root of $q$),
consistent with the bound.

## Replay instructions

Requires only `numpy` and `sympy` (versions used: numpy 1.26.4, sympy 1.12):

1. `python3 output/artifacts/s1_search.py` — 64-class switching search; min $\sqrt5$.
2. `python3 output/artifacts/s1_exact.py` — exact charpoly $x^4(x^2-5)^3$.
3. `python3 output/artifacts/G1_props.py` — $G_1$ spectrum/connectivity/girth/diameter.
4. `python3 output/artifacts/s2_search.py` — 2048-class switching search; min $\approx 2.58163$.
5. `python3 output/artifacts/s2_exact.py` — exact charpoly + factorization.
6. `python3 output/artifacts/cert_r.py` — Sturm counts + exact rational checks.
7. `python3 output/artifacts/G2_props.py` — $G_2$ spectrum/connectivity/girth/diameter.

Total runtime under $5$ minutes on one core.

## Originality and limitations

- To our knowledge no prior work publishes these Petersen$\to 20\to 40$
  signing bitstrings with a $\lambda=\sqrt5$ stage-1 exact certificate and a
  $\le 2.60$ stage-2 Sturm certificate; MSS is nonconstructive/bipartite,
  Bilu–Linial gives only $O(\sqrt{d\log^3 d})$, derandomized near-Ramanujan
  results are asymptotic with $\epsilon$-slack at large sizes.
- Honest limits: (i) stage-2 optimality over switching classes was searched
  (minimum over all 2048 classes: yes, exhaustive) but we claim only that
  $s_2$ attains the class minimum $\approx 2.58163$, not a structural
  optimality theorem; (ii) the certified stage-2 bound is $2.60$, slightly
  above the true value $\approx 2.58163$ — the slack is the cost of a
  hand-checkable rational certificate; (iii) the $40$-vertex graph as an
  unlabelled cubic graph may coexist in enumerations of small cubic graphs —
  the new content is the explicit lift tower with certificates, not the bare
  isomorphism type; (iv) connectivity/non-bipartiteness/girth/diameter are
  machine-checked (BFS) facts replayable from the archived edge lists, not
  hand proofs.
