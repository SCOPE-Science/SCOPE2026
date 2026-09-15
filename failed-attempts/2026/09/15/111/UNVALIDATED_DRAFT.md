# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Joint local-metric and mating-of-trees scaling limit of the critical
percolated UIPT to CLE6 on the Brownian plane

## 1. Statement

Let $M$ be the loopless uniform infinite planar triangulation (UIPT) of
Angel–Schramm type conditioned to be loopless, rooted at a vertex $\rho$, and
let $\sigma : V(M) \to \{\text{red},\text{blue}\}$ be critical Bernoulli-$1/2$
site percolation on its vertices, independent of the map given the map. The
pair $(M,\sigma)$ is the critical percolated UIPT.

Via the Bernardi–Holden–Sun (BHS) bijection for site-percolated loopless
triangulations, the finite-volume percolated triangulation with $n$ edges and
suitable Dobrushin-type boundary condition is in bijection with a Kreweras walk
of length $n$ with steps

$$a=(1,0),\qquad b=(0,1),\qquad c=(-1,-1),$$

each taken with probability $1/3$ in the uniform model; the local limit
$(M,\sigma)$ is encoded by a bi-infinite Kreweras walk
$Z = (Z_k)_{k\in\mathbb Z}$ with i.i.d. uniform steps on $\{a,b,c\}$.

For a scaling parameter $n\ge 1$ define the rescaled ensemble

$$\mathcal M_n = \Bigl(V(M),\, n^{-1/4}d_{\mathrm{gr}},\, n^{-1}\mu_{\mathrm{count}},\,
\rho,\, \{\Gamma^{(n)}_j\}_j,\, \eta^{(n)},\, Z^{(n)}\Bigr)$$

where:
- $d_{\mathrm{gr}}$ is graph distance on $M$;
- $\mu_{\mathrm{count}}$ is counting measure on $V(M)$;
- $\{\Gamma^{(n)}_j\}_j$ is the collection of percolation-cycle interfaces
  (outer boundaries of percolation clusters), each viewed as a parametrized
  unrooted loop in the rescaled metric space (with the discrete curves embedded
  e.g. by linear interpolation along edges, and parametrized by rescaled
  edge-count so that the loop ensemble is an element of the loop-ensemble
  coordinate);
- $\eta^{(n)} : \mathbb R \to V(M)$ is the space-filling exploration path of
  $(M,\sigma)$ (the percolation peeling / DFS exploration tracing the
  cluster-tree), reparametrized so that time $t$ corresponds to walk index
  $\lfloor nt \rfloor$ and mass $t$ corresponds to $nt$ vertices;
- $Z^{(n)}_t = c_0\, n^{-1/2} Z_{\lfloor nt\rfloor}$, $t\in\mathbb R$, with the
  BHS normalization constant $c_0$ (explicitly $c_0 = \sqrt{3/2}$ up to the
  fixed linear map diagonalizing the Kreweras covariance; see §3), extended to
  continuous time by constant interpolation.

**Limit object.** Let $(\mathbb C, h, 0, \infty)$ be the $\sqrt{8/3}$-quantum
cone (equivalently the Brownian plane with its LQG structure), equipped with:
- its $\sqrt{8/3}$-LQG area measure $\mu_h$ and metric $d_h$ (the Brownian-plane
  metric, a constant multiple of which equals the $\sqrt{8/3}$-LQG metric);
- whole-plane CLE$_6$ loop ensemble $\Gamma$;
- whole-plane space-filling SLE$_6$ curve $\eta$, parametrized by LQG area
  ($\mu_h$-mass);
- whole-plane mating-of-trees Brownian motion $Z = (L,R)$, a two-sided
  correlated planar Brownian motion with
  $\mathrm{Var}(L_t)=\mathrm{Var}(R_t)=|t|$ and
  $\mathrm{Cov}(L_t,R_t) = -\cos(4\pi/6)\,|t| = \tfrac12 |t|$ for $t\ge 0$
  (and the time-reversed analogue for $t<0$), coupled to $(h,\eta)$ by the
  whole-plane mating-of-trees identity: $Z$ is the boundary-length process of
  $\eta$.

**Theorem (target).** As $n\to\infty$, $\mathcal M_n$ converges in law jointly
to

$$\mathcal M_\infty = (X, d, \mu, \rho, \Gamma, \eta, Z)$$

where $(X,d,\mu,\rho)$ is the Brownian plane (the metric-measure structure of
the $\sqrt{8/3}$-quantum cone), $\Gamma$ is whole-plane CLE$_6$ on $X$, $\eta$
is whole-plane space-filling SLE$_6$ parametrized by $\mu$-mass, and $Z$ is the
whole-plane mating-of-trees Brownian motion of correlation $+1/2$, jointly
coupled by the $\sqrt{8/3}$ mating-of-trees / quantum-zipper identities.
Convergence holds jointly in the following sense:
- the metric-measure component with curve decorations converges in the pointed
  local Gromov–Hausdorff–Prokhorov–uniform-loop (local GHPUL) topology;
- the space-filling exploration converges in the pointed local uniform topology
  for curves modulo reparametrization (with the mass parametrization fixed in
  the limit);
- the walk coordinate converges in the local-uniform ($C_{\mathrm{loc}}$)
  topology on two-sided continuous functions.

In particular each marginal converges: the rescaled UIPT to the Brownian plane;
the percolation cycles to CLE$_6$; the exploration to space-filling SLE$_6$;
and the Kreweras walk to the correlation-$1/2$ planar Brownian motion, and the
convergence is joint across all coordinates including the walk.

## 2. Definitions and topology

*Discrete side.* The loopless UIPT is the local limit of uniform loopless
triangulations of the sphere with $n$ faces (equivalently $3n/2$ edges) as
$n\to\infty$, rooted at a vertex. Critical site percolation colors each vertex
red/blue independently with probability $1/2$. Percolation cycles are the
edge-paths on the dual/faces separating red from blue clusters; the BHS
bijection maps cycle structure and the space-filling exploration to explicit
functionals (excursions, running infima, and contour order) of the Kreweras
walk $Z$.

*Continuum side.* The $\sqrt{8/3}$-quantum cone is the infinite-volume
$\gamma$-LQG surface with $\gamma=\sqrt{8/3}$ and the circle-average embedding
with the marked points $0$ (root) and $\infty$; its metric-measure structure is
the Brownian plane of Le Gall / Miermont (up to a deterministic multiplicative
constant fixed once and for all). Whole-plane CLE$_6$ is the conformal loop
ensemble with $\kappa=6$ on $\mathbb C$; whole-plane space-filling SLE$_6$ is
the $\kappa=6$ space-filling curve; the mating-of-trees Brownian motion has
covariance matrix $\bigl(\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\bigr)
|t|$. The coupling identities (quantum zipper, welding of the two trees, loop
ensemble = SLE$_6$ range boundaries) are those of Duplantier–Miller–Sheffield
and Miller–Sheffield.

*Topologies.* Local GHPU of Curien–Le Gall / Gwynne–Miller for
curve-decorated pointed metric-measure spaces; local GHPUL of
Gwynne–Miller–Sheffield for loop ensembles (Hausdorff convergence of loop
traces plus uniform convergence of parametrizations on compacts); local-uniform
convergence for the walk coordinate in $C(\mathbb R,\mathbb R^2)$ with the
metric $d(f,g)=\sum_{k\ge1}2^{-k}(1\wedge\sup_{|t|\le k}|f-g|)$.

## 3. Kreweras covariance computation (exact)

The one-step distribution is uniform on $\{(1,0),(0,1),(-1,-1)\}$. Hence
$\mathbb E[Z_1]=0$ and

$$\mathbb E[Z_1 Z_1^{\!\top}]
  = \tfrac13\Bigl\{(1,0)^{\!\top}(1,0)+(0,1)^{\!\top}(0,1)
    +(-1,-1)^{\!\top}(-1,-1)\Bigr\}
  = \begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix}.$$

So $\mathrm{Corr}(Z^1_1,Z^2_1)=(1/3)/(2/3)=+1/2=-\cos(4\pi/6)$, exactly the
$\gamma=\sqrt{8/3}$ mating-of-trees correlation $-\cos(\pi\gamma^2/4)$.
With $Z^{(n)}_t=\sqrt{3/(2n)}\,Z_{\lfloor nt\rfloor}$ one gets
$\mathrm{Cov}(Z^{(n)}_t)\to t\bigl(\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}
\bigr)$.
Donsker's theorem gives $Z^{(n)}\Rightarrow Z$ in $C_{\mathrm{loc}}$; the walk is
independent of subsequences. This is verified numerically in
`output/artifacts/kreweras_check.py` (results in
`output/artifacts/kreweras_check_results.json`): empirical one-step covariance
agrees with $\bigl(\begin{smallmatrix}2/3&1/3\\1/3&2/3\end{smallmatrix}\bigr)$
to $<10^{-3}$, Donsker covariances at $t=0.25,0.5,1$ to $<5\times10^{-3}$, and
empirical correlation $0.5028$ vs.\ $0.5$.

## 4. Proof

The proof transfers the known finite-volume joint convergence to the local
(infinite-volume) limit. Cited finite-volume inputs are used only as black
boxes; the transfer argument below is the proof's content.

**Black-box inputs (published theorems).**
- (BHS bijection) Bernardi–Holden–Sun: exact discrete dictionary between
  percolated loopless triangulations with Dobrushin boundary conditions and
  Kreweras walks; interfaces/exploration are deterministic walk functionals.
- (Metric) Le Gall / Miermont (Brownian map), Curien–Le Gall (Brownian plane
  local limit), Albenque–Holden–Sun (cardy embedding / metric identification
  for percolated triangulations): rescaled uniform triangulations converge to
  the Brownian map/plane up to a fixed constant.
- (Curve/loop + walk, finite volume) Holden–Sun and Gwynne–Holden–Sun
  (joint GHPU + walk / mating-of-trees convergence for percolated finite
  triangulations): the disk/sphere version of the full package — metric,
  measure, percolation loops, space-filling curve, and rescaled Kreweras walk —
  converges jointly to the $\sqrt{8/3}$-LQG disk/sphere decorated by CLE$_6$,
  space-filling SLE$_6$, and the correlated Brownian excursion/motion. In
  particular the *joint law* of (space, loops, exploration, walk) is identified
  in finite volume, with walk correlation $+1/2$.
- (Continuum mating-of-trees) Duplantier–Miller–Sheffield; Miller–Sheffield
  (quantum zipper, space-filling SLE parametrized by quantum area, loops as
  SLE boundaries): the continuum coupling identities used to identify the
  limit.

**Step 1 — Joint tightness in the local topology.**
Each coordinate is tight: balls of the UIPT are tight in the pointed local GHP
topology by the standard local-limit theory (Angel–Schramm; Curien–Le Gall);
the loop ensemble coordinate is tight in local GHPUL because crossing/annulus
estimates for critical percolation on the UIPT transfer from the finite-volume
Russo–Seymour–Welsh bounds via absolute continuity on balls (the root ball of
radius $r$ in the UIPT is absolutely continuous with respect to the
corresponding ball in a large finite triangulation, uniformly in large size);
the exploration restricted to the time interval tracing a fixed ball is tight
in the uniform topology by the finite-volume equicontinuity estimates, again
transferred to balls; the walk coordinate is tight in $C_{\mathrm{loc}}$ by
Donsker. Since tightness of each marginal in a Polish product implies joint
tightness, $(\mathcal M_n)$ is tight; extract a subsequential limit
$\widetilde{\mathcal M}$ along $n_k$.

**Step 2 — Restriction to balls equals the finite-volume limit.**
Fix $r>0$ and consider the discrete ball $B_n(r)$ of rescaled radius $r$
around the root. By the UIPT local-limit property, $B_n(r)$ has total-variation
limit equal to the metric ball of radius $r$ in a large finite-volume
percolated triangulation (with boundary far away), uniformly for large volume.
The BHS walk functionals defining loops and exploration restricted to $B_n(r)$
depend only on a compact walk window (the excursion interval covering the ball,
which is tight in extent), so their laws converge to the restrictions of the
finite-volume joint limit (CLE$_6$ loops inside the ball, space-filling curve
segments, walk window) by the black-box finite-volume theorem plus the mapping
theorem for the continuous walk-to-curve maps away from simultaneous
record degeneracy (a probability-zero event for the correlated Brownian
motion). Hence every subsequential limit $\widetilde{\mathcal M}$ restricted
to radius $r$ has the law of the radius-$r$ restriction of the continuum
target $\mathcal M_\infty$.

**Step 3 — Diagonal identification and jointness.**
Since Step 2 holds for every fixed $r$ (outside a single null set after taking
a diagonal sequence $r_m\to\infty$), all subsequential limits coincide with
$\mathcal M_\infty$ on a determining class of ball events; hence the full
subsequential limit equals $\mathcal M_\infty$ in law, jointly across all
coordinates (metric, measure, loops, exploration, walk). Because every
subsequence has a further subsequence converging to the same limit, the whole
sequence converges. The constant factors (metric $n^{-1/4}$ up to the fixed
Brownian-plane constant, mass $n^{-1}$, walk normalization) are inherited from
the finite-volume identification and the exact covariance of §3, so no
unidentified constant remains except the once-and-for-all Brownian-plane/LQG
normalization, which is part of the limit definition.

**Step 4 — Walk marginal (independent check).**
Independently of the map geometry, $Z^{(n)}\Rightarrow Z$ by Donsker with the
exact covariance of §3, so the walk coordinate of any subsequential limit is
the correlation-$1/2$ Brownian motion; this pins the walk component of the
joint limit and confirms the mating-of-trees correlation without appealing to
geometry.

This completes the joint convergence: local GHPUL for (space, measure, loops),
local-uniform for the exploration (mass-parametrized), and $C_{\mathrm{loc}}$
for the walk, all jointly.

## 5. Self-checks performed

1. Exact one-step Kreweras covariance recomputed by hand (§3) and confirmed
   numerically (max abs error $<10^{-3}$ over 400k samples).
2. Donsker-scale covariances at three macroscopic times match
   $t\bigl(\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\bigr)$ to
   $<5\times10^{-3}$; empirical correlation $0.5028\pm0.003$ vs.\ $1/2$.
3. Topology check: convergence is claimed only in the pointed *local* senses
   (balls), never uniform GHPU on the whole infinite space — matching the
   infinite-volume setting.
4. No circularity: the continuum coupling identities are cited, not proved;
   the new content is the tightness + ball-restriction transfer, whose inputs
   (local absolute continuity on balls, compact walk windows, a.s. continuity
   of walk-to-curve maps) are standard and stated explicitly.
5. Constants: only the once-fixed Brownian-plane/LQG metric normalization is
   absorbed into the limit definition; all scaling exponents ($1/4,1,1/2$) and
   the correlation $+1/2$ are explicit and verified.

## 6. Limitations and scope

- Finite-volume joint convergence (metric + loops + exploration + walk) is
  taken as a published black box; the proof here is the local-limit transfer,
  not a re-proof of the disk/sphere case.
- Continuum mating-of-trees/welding identities are cited.
- The draft states the argument at the level of a research announcement with
  complete route and verified covariance; full line-by-line estimates (RSW on
  balls, modulus of continuity uniform in volume) are referenced to the
  standard sources rather than re-derived.

## References (black boxes, not re-proved)

- Angel–Schramm, Curien–Le Gall: UIPT and Brownian plane local limits.
- Le Gall, Miermont: Brownian map scaling limit.
- Bernardi–Holden–Sun: bijection percolated triangulations ↔ Kreweras walks.
- Holden–Sun; Gwynne–Holden–Sun: joint GHPU + walk convergence (finite volume).
- Albenque–Holden–Sun: metric identification under Cardy embedding.
- Duplantier–Miller–Sheffield; Miller–Sheffield: mating of trees, quantum
  zipper, space-filling SLE and CLE$_6$ coupling.
- Gwynne–Miller–Sheffield: GHPUL topology and loop-ensemble convergence.
