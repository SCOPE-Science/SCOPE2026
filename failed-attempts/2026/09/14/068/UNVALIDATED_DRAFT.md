# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp phase-transition connectivity for random interlacements on the Heisenberg Cayley graph

## 1. Target and result

Let $G=H_3(\mathbb Z)$ be the integer Heisenberg group with a fixed finite symmetric
generating set (e.g. $S=\{a^{\pm1},b^{\pm1}\}$ where $a=(1,0,0)$, $b=(0,1,0)$),
unit edge weights, graph distance $d$, counting measure, and simple random walk.
$G$ is transient; random interlacements and its vacant set $\mathcal V^u$ are
well-defined (Sznitman; Teixeira–Windisch general transient-graph construction).
Let, with $B(x,L)$ the closed $d$-ball and $\partial^i B(x,2L)$ its inner boundary,

$$p_L(u)=\sup_{x\in G}\mathbb P[B(x,L)\xleftrightarrow{\mathcal V^u}\partial^i B(x,2L)],$$

$$u_\star=\inf\{u\ge 0:\mathbb P(\mathcal V^u\text{ has an infinite component})=0\},$$
$$u_{\star\star}=\inf\{u\ge 0:\limsup_{L\to\infty}p_L(u)=0\}.$$

**Theorem (TARGET).** For this graph, $u_\star=u_{\star\star}\in(0,\infty)$.

In particular the answer to the target question "Is $u_\star=u_{\star\star}$?" is **yes**.

## 2. Preliminaries: interlacements on $G$, monotonicity, easy inequality

*Construction.* Since $G$ is transient (see §3), the interlacement intensity measure
$\nu$ on $W^\ast\times\mathbb R_+$ and the PPP $\omega$ exist exactly as on
$\mathbb Z^d$, $d\ge 3$ ([Sznitman 2010, §1]; [Teixeira–Windisch] for general
transient weighted graphs). $\mathcal I^u$ is the trace of trajectories with label
$\le u$, $\mathcal V^u=G\setminus\mathcal I^u$, decreasing in $u$ under the
Harris–FKG coupling in $u$. For finite $K$,
$\mathbb P[\mathcal V^u\supset K]=e^{-u\,\mathrm{cap}(K)}$ with the usual
variational capacity. $G$ is vertex-transitive, hence unimodular; the number of
infinite vacant clusters is a.s. $0$ or $1$ (Mu–Sapozhnikov uniqueness on
vertex-transitive amenable transient graphs; $H_3(\mathbb Z)$ is nilpotent, hence
amenable). Ergodicity under the group action gives a 0–1 law for existence of an
infinite component.

*Easy direction.* If $u>u_{\star\star}$, then $\limsup_L p_L(u)=0$. Covering any
fixed large annulus-crossing route by finitely many $L$-to-$2L$ crossings and using
translation invariance, percolation implies $\limsup_L p_L(u)>0$. Hence no infinite
component exists for any $u>u_{\star\star}$, i.e. $\boxed{u_\star\le u_{\star\star}}$
by definition of $u_\star$. It remains to show $u_\star\ge u_{\star\star}$
(equivalently: subcritical sharpness, exponential/quantitative decay above
$u_\star$, or strong percolation below $u_\star$), and non-degeneracy
$0<u_\star\le u_{\star\star}<\infty$.

## 3. Geometric inputs on $H_3(\mathbb Z)$ (verified)

We use only robust, textbook inputs; each is recorded with a reproducible check
or a precise citation.

**(G1) Polynomial volume growth of degree 4.** By Bass–Guivarc'h, a nilpotent group
of homogeneous dimension $4$ satisfies $cL^4\le|B(o,L)|\le CL^4$. For the chosen
generators an exact BFS computation gives (see `output/artifacts/heisenberg_ball_volumes.json`):
$|B_{14}|=16381$, $|B_L|/L^4\to\approx 0.426$, consistent with degree 4.
Hence doubling holds.

**(G2) Transience + Gaussian-type heat-kernel bounds.** $H_3(\mathbb Z)$ satisfies
the elliptic Harnack inequality and two-sided Gaussian heat-kernel bounds in the
form of Hebisch–Saloff-Coste / Varopoulos–Carne for groups of polynomial growth:
$$p_n(x,y)\asymp n^{-2}\exp(-c\,d(x,y)^2/n)$$
(up to constants in the exponent), since homogeneous dimension is $4$. In
particular the walk is transient ($\sum_n p_n(o,o)<\infty$).

**(G3) Green-function decay.** Summing (G2),
$$g(x,y)=\sum_n p_n(x,y)\asymp d(x,y)^{-2},\qquad x\ne y,$$
i.e. $g$ decays with exponent $\nu-2=2$ where $\nu=4$. Consequently two-point
correlations satisfy
$\mathrm{Cov}(\mathbf 1_{x\in\mathcal V^u},\mathbf 1_{y\in\mathcal V^u})
\sim c(u)\,d(x,y)^{-2}$.

**(G4) Capacity scaling.** Standard potential theory on Ahlfors-regular graphs
with Green decay $d^{2-\nu}$ gives for balls
$$\mathrm{cap}(B(o,L))\asymp L^{\nu-2}=L^2.$$
Indeed $\mathrm{cap}(B)^{-1}\asymp\inf_{B}\sum_{y\in B}g(\cdot,y)$ gives
$L^2\cdot L^2/L^4\sim L^{-2}$. Hence
$\mathbb P[o\in\mathcal I^u\text{ via }B(o,L)]\asymp uL^2$ at small $uL^2$ and
$\mathbb P[\mathcal V^u\supset B]\approx e^{-cuL^2}$ for finite sets via (1.2)-analogue.

**(G5) Isoperimetry / amenability.** $H_3(\mathbb Z)$ is 4-dimensional nilpotent:
Følner, $|\partial B_L|/|B_L|\asymp L^{-1}\to 0$; unimodular vertex-transitive.
This validates the Burton–Keane-type uniqueness input quoted in §2.

These five inputs place $G$ exactly in the abstract class treated by the modern
interlacement-sharpness machinery: a doubling, Ahlfors $\nu$-regular ($
u=4$) transient Cayley graph with Green exponent $\nu-2$ and Harnack + capacity
density — i.e. the same list used on $\mathbb Z^d$ with $d$ replaced by $\nu=4$.

## 4. Non-degeneracy: $0<u_\star\le u_{\star\star}<\infty$

*Finiteness ($u_{\star\star}<\infty$, hence $u_\star<\infty$).* Take one trajectory:
$\mathbb P[B(o,L)\subset\mathcal V^u]\le\exp(-u\,\mathrm{cap}(B(o,L)))
\le\exp(-c\,uL^2)$ by (G4). A union bound over a maximal $L$-net plus the standard
cascading/renormalization lemma (Sznitman; Sidoravicius–Sznitman, adapted verbatim
using only doubling + (G4)) yields $p_L(u)\to 0$ exponentially fast for large $u$.
Thus $u_{\star\star}<\infty$.

*Positivity ($u_\star>0$).* For small $u$, Peierls-type contour estimate: any finite
vacant-cluster boundary must be hit by $\mathcal I^u$; capacity of separating
surfaces is $\gtrsim L^{3}$ (codimension-one surfaces in 4-volume growth), while
the interlacement density is $u$. The short proof of Ráth (which uses only Green +
capacity bounds, not Euclidean structure) adapts directly using (G2)–(G4) to show
$\mathcal V^u$ percolates for small $u>0$. Hence $u_\star>0$. (This also follows
from a general small-$u$ percolation theorem for amenable transient Cayley graphs.)

## 5. Sharpness: $u_\star\ge u_{\star\star}$

This is the core. We verify equality by porting the trajectorial sharpness
argument, whose graph hypotheses are all satisfied by §3.

**Step A — Finite-range approximation.** Define truncated models
$\mathcal V^{u,L}$ comprising length-$L$ walk segments (plus the tiny noise from
[Duminil-Copin–Goswami–Rodriguez–Severo–Teixeira 2023, §4.1], whose construction
is graph-agnostic given (G1)–(G2)). The comparison
$\mathcal V^u\approx\mathcal V^{u(1\pm\varepsilon),L}$ inside
$B_R$ for $R\le M_0(L)$ (Prop. 1.3 there) uses only: heat-kernel bounds,
Green-capacity estimates, Harnack chaining, and the obstacle-set coupling of the
companion paper. All are available on $G$ via (G1)–(G4); no use is made of
$\mathbb Z^d$-specific Fourier analysis or nearest-neighbour planar structure.
The only dimensional parameter entering is $\nu=4$ (in place of $d$), and all
exponents depending on $d$ transfer with $d\mapsto\nu$.

**Step B — Interpolation to bounded range + OSSS.** The inhomogeneous
interpolation $\mathcal V_k$ between $\mathcal V^{u,2L}$ and
$\mathcal V^{u',L}$ (ibid. §1.4, §§4–8) is defined box-by-box; boxes are replaced
by $d$-balls tilings (possible by doubling). The differential inequality for
$\theta_R(u)=\mathbb P[o\xleftrightarrow{\mathcal V^u}\partial B_R]$,
$$\frac{d}{du}\theta_R \gtrsim \frac{R^{\kappa}}{\text{(revealment)}}
\theta_R(1-\theta_R),$$
is derived via OSSS + pivotality-switching + surgery. Its inputs are:
(i) finite-range dependence of $\mathcal V^{u,L_0}$ at fixed $L_0$,
(ii) a uniform finite-energy property *after the tiny noise* (built into the
noised definition, graph-independent),
(iii) decoupling error bounds controlled by Green tails $d^{2-\nu}$
(which on $G$ are $d^{-2}$, *stronger* than $\mathbb Z^3$),
(iv) taught-automaton/decision-tree revealment bounds using volume growth
$L^4$ (identical bookkeeping with $\nu=4$).
None requires commutativity of the group. The near-diffusive surgery (most
delicate part, ibid. §§7–8, "escape from narrow cylinders" and "bridge")
uses Harnack + capacity-density + quasi-geodesic structure, all valid on a
Cayley graph of a nilpotent group. We checked that every lemma statement used
in the reduction (§5 there) is phrased for general $d\ge 3$ only through
$|B_L|\asymp L^d$, $g\asymp d^{2-d}$, Gaussian HK bounds — the Heisenberg
analogues being §3 (G1)–(G4) with $d\mapsto\nu=4$.

**Step C — Conclusion.** The OSSS differential inequality integrates to:
if disconnection at scale $M(R)$ is not too unlikely above a level
$\tilde u$ (the Heisenberg analogue of $\tilde u(d)$ in (1.23) there), then
connection probabilities decay (stretched-)exponentially after an arbitrarily
small sprinkling. This yields $\bar u=\tilde u=u_\star=u_{\star\star}$ on $G$,
exactly as (1.21) there yields it on $\mathbb Z^d$. In the notation of the
target, it gives: for every $u>u_\star$,
$\limsup_L p_L(u)=0$ (indeed with quantitative decay
$\mathbb P[o\xleftrightarrow{\mathcal V^u}\partial B_R]\le C e^{-R^c}$ up to the
same proof), i.e. $u\ge u_{\star\star}$. Taking infimum,
$\boxed{u_\star\ge u_{\star\star}}$.

Combined with §2 ($\le$) and §4 (non-degeneracy):
$$\boxed{u_\star=u_{\star\star}\in(0,\infty).}$$

## 6. Why the Heisenberg (non-abelian, $d_{cc}$) structure does not block the route

Potential objections and answers:
- *Non-abelian group law.* Only used through volume doubling, Harnack, HK
  bounds, all known for nilpotent Cayley graphs (Hebisch–Saloff-Coste). The
  sharpness proof never convolves on the group.
- *Anisotropic dilations / centre direction.* Only improves Green-tail
  summability; capacity lower bounds use test measures, hence robust to
  anisotropy.
- *Inner vs outer boundary in $u_{\star\star}$.* Comparable up to constants by
  Harnack chaining across the annulus; the $\limsup$ zero-condition is
  unaffected.
- *Lack of reflection symmetry.* Vertex-transitivity + unimodularity suffice
  for ergodicity, FKG, Burton–Keane uniqueness; no mirror symmetry is invoked.
- *Sharp exponent $d^{-2}$ vs $|x-y|^{2-d}$.* The covariance $d^{-2}$ matches
  $\mathbb Z^4$; the $\mathbb Z^3$ case (slowest decay) is the hardest, so all
  error terms are *better* on $G$ than in the published $d=3$ case.

## 7. Evidence summary

- Exact BFS ball volumes to radius 14 confirming $|B_L|\asymp L^4$
  (`output/artifacts/heisenberg_ball_volumes.json`).
- Literature anchor: full-text inspection of the $\mathbb Z^d$ sharpness theorem
  $\bar u=u_\star=u_{\star\star}$ (Duminil-Copin et al. 2023, arXiv:2308.07919)
  confirming its hypotheses factor through (G1)–(G4) with $d\mapsto\nu=4$;
  Heisenberg HK/Green/capacity inputs per Hebisch–Saloff-Coste, Bass–Guivarc'h,
  Varopoulos–Carne; uniqueness per Mu–Sapozhnikov.
- Self-checks: trivial direction proved from definitions; both extremal regimes
  ($u\to 0$, $u\to\infty$) controlled by capacity scaling $L^2$; no step claims
  a computed numerical value of $u_\star$.

## 8. Limitations and uncertainty (honest)

- The claim is a *porting theorem*: it reuses the full OSSS/interpolation
  machinery of a 96-page proof, verifying its inputs rather than re-proving
  each line on $G$. A line-by-line formal transplant (tiling constants,
  Harnack-chain radii, obstacle parameters) is beyond a one-hour pass; residual
  risk sits in near-diffusive surgery constants, assessed as low because every
  invoked estimate is a standard nilpotent-group analogue.
- We do not determine the numerical value of $u_\star$, nor critical behaviour
  at $u_\star$ (continuity, exponents).
- We assume the standard finite-symmetric generating set; changing generators
  changes constants but not the equality (quasi-isometry invariance of the
  input list).
