# Exact 2-Selmer dimensions for the congruent-number twists n=51 and n=219: a certified +2 jump (2 -> 4)

## Context

Quadratic twists of the full-rational-2-torsion curve $E_0: y^2=x^3-x$ are the
standard laboratory for Birch–Swinnerton-Dyer rank predictions, Goldfeld-type
distribution questions, and Tate–Shafarevich visibility. Statistical theorems
describe Selmer distributions (Smith, Heath-Brown) and Heegner-point theorems
produce rank-1 subfamilies (Tian), but exact pointwise rank-versus-Selmer
certificates remain sparse. The admitted target claim was
$\dim_{\mathbf{F}_2}\mathrm{Sel}_2=3$ at $n=51$ and $5$ at $n=219$ with analytic
rank 0 and Sha visibility; the admitted preset fallback was $\dim=5$ at 219.
Recomputation refutes both absolute values and replaces them with the corrected
pair below. This record states the corrected emergent finding.

## Definitions

- $E_0: y^2=x^3-x$. For squarefree $n>0$, $E^{(n)}: n y^2=x^3-x$, isomorphic over
  $\mathbf{Q}$ to $E_n: y^2=x^3-n^2x$ (congruent-number curve).
- $\mathrm{Sel}_2(E^{(n)}/\mathbf{Q})$: 2-Selmer group. Write
  $\#\mathrm{Sel}_2 = 2^{s(n)+2}$; $s(n)$ is the 2-Selmer rank. Then
  $\dim_{\mathbf{F}_2}\mathrm{Sel}_2 = s(n)+2$ and
  $0 \le \mathrm{rank}\,E^{(n)}(\mathbf{Q}) \le s(n)$, with
  $\mathrm{rank} + \dim_{\mathbf{F}_2}\Sha[2] = s(n)$ where defined.
- Monsky normal form (odd squarefree $n$, $m$ odd prime factors; Das–Mondal
  Sec. 3 after Monsky): with $\phi((-1)^\epsilon)=\epsilon$,
  $D_l = \mathrm{diag}(\phi((l/p_i)))$, $l \in \{2,-2\}$,
  $E_{ij}=\phi((p_j/p_i))$ for $i\ne j$, $E_{ii}=\sum_{j\ne i}E_{ij}$ over
  $\mathbf{F}_2$, and
  $M_o = [[D_2, E+D_2],[E+D_{-2}, D_2]]$. Then $s(n) = 2m - \mathrm{rank}_{\mathbf{F}_2}(M_o)$.
- Odd-$n$ Tunnell data: $A(n)=\#\{2x^2+y^2+8z^2=n\}$,
  $B(n)=\#\{2x^2+y^2+32z^2=n\}$ (swap of $x,y$ immaterial). Tunnell: for odd
  squarefree $n$, if $A(n) \ne 2B(n)$ then $n$ is non-congruent (rank 0);
  if $A(n)=2B(n)$ the test is neutral. The alternative $2A=B$ is false
  (control $n=41$: $A=32,B=16$, known congruent, satisfies $A=2B$).

## Result

For $n_0 = 51 = 3\cdot 17$ and $n_1 = 219 = 3\cdot 73$ (stratum $p\equiv 3\bmod 8$,
$q\equiv 1\bmod 8$):

- $\dim_{\mathbf{F}_2}\mathrm{Sel}_2(E^{(51)}/\mathbf{Q}) = 2$ (Selmer rank $s=0$);
- $\dim_{\mathbf{F}_2}\mathrm{Sel}_2(E^{(219)}/\mathbf{Q}) = 4$ (Selmer rank $s=2$);
- hence a certified $+2$ jump $2 \to 4$, correcting the admitted $(3,5)$ by $-1$
  each; the preset fallback $\dim=5$ at 219 is refuted (value is 4).
- $n=51$ is non-congruent (rank 0) by Tunnell: $A=24$, $B=16$, $A-2B=-8\ne 0$,
  so $\mathrm{rank}+\dim\Sha[2]=0$ there.
- At $n=219$: $s=2$, i.e.
  $\mathrm{rank}(E^{(219)})+\dim_{\mathbf{F}_2}\Sha(E^{(219)})[2]=2$;
  Tunnell is neutral ($A=48$, $B=24$, $A=2B$), so the rank-0 / visible-Sha
  allocation at 219 is NOT proved and is stated open
  (rank 2 vs $(0,\Sha\dim 2)$ vs $(1,\Sha\dim 1)$).

## Proof / evidence

Prime data recomputed by Euler criterion:
$(2/3)=-1$, $(2/17)=+1$, $(2/73)=+1$; $(-2/3)=(-2/17)=(-2/73)=+1$;
$(17/3)=(3/17)=-1$; $(73/3)=(3/73)=+1$.
So the $(3/q)$ symbol split ($-1$ at 51, $+1$ at 219) holds.

Matrices from the normal form with primes $[3,17]$ and $[3,73]$:

- $M(51) = [[1,0,0,1],[0,0,1,1],[1,1,1,0],[1,1,0,0]]$.
  Elimination: pivot $(0,0)$, then $(2,1)$, then $(1,2)$, then $(3,3)$;
  RREF $= I_4$. Rank 4, $s = 4-4 = 0$, $\dim\mathrm{Sel} = 2$.
- $M(219) = [[1,0,1,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]$.
  Pivots $(0,0),(2,2)$; rows 1,3 zero. Rank 2, $s = 4-2 = 2$,
  $\dim\mathrm{Sel} = 4$. Nullspace basis $(0,1,0,0),(0,0,0,1)$.

Elimination log: `output/artifacts/elim_log.txt`.
Replay: `output/artifacts/verify_all.py` (stdlib only) rebuilds Legendre data,
matrices, F2 ranks, and Tunnell counts.

Tunnell brute force uses exact bounds
$|x|\le\sqrt{n/2}$, $|y|\le\sqrt{n}$, $|z|\le\sqrt{n/8}$ (resp. $\sqrt{n/32}$),
hence exhaustive: $n=51$: $A=24,B=16$; $n=219$: $A=48,B=24$.
Discriminating control $n=41$ ($A=32,B=16$, known congruent) confirms the
$A=2B$ form used in the headline.

## Limitations

- The Monsky formula $s=2m-\mathrm{rank}(M_o)$ is taken from the literature
  (Das–Mondal/Monsky), not reproved; inputs, matrix, and rank are recomputed
  from scratch.
- No per-place $(b_1,b_2,b_3)$ $\mathbf{Q}_p$ solubility logs are claimed
  (enumerator timed out); the fallback per-class $\mathbf{Q}_p$ criterion is NOT met.
- No proof that $\mathrm{rank}(E^{(219)})=0$ and no visibility diagram; the
  $(\mathrm{rank},\Sha)$ split of $s=2$ at 219 is open.
- Minimality of 219 as first $+1$ representative is not rechecked and not used.

## Reproducibility

Run `python3 output/artifacts/verify_all.py` (stdlib only). It prints
ranks, Selmer dimensions, Tunnell counts $A,B$, and the Legendre table, and
writes `tables.txt`. The elimination steps in `elim_log.txt` can be checked by
hand over $\mathbf{F}_2$.

## References

- A. Smith, 2^infty-Selmer groups, 2^infty-class groups, and Goldfeld's
  conjecture, arXiv:1702.02325. Statistical distribution; no per-twist dim.
- D. R. Heath-Brown, The size of Selmer groups for the congruent number
  problem, Invent. Math. 111 (1993). Average/moment theorems.
- Y. Tian, Congruent Numbers and Heegner Points, arXiv:1210.8231. Rank-1
  Heegner constructions; Monsky normal form as method.
- S. Das, S. Mondal, Monsky Matrix and 2-Selmer rank, arXiv:2604.26183.
  Normal form $s=2m-\mathrm{rank}(M_o)$, infinite $s=0$ families generalizing
  Lagrange; no dim at 51/219.
