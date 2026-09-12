# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the falsifiable radial revealment ledger for the Voronoi annulus circuit

## 1. Target restated

Intensity-1 Poisson–Voronoi coloring of the plane: Poisson points of intensity 1,
each colored red independently with probability $p$ (blue otherwise); the Voronoi
cell of each point inherits its color. On the annulus $A(n,2n)=\{n\le |z|\le 2n\}$,
$n\ge 16$, let $\mathrm{Circ}_n$ be the event that a red circuit separates the inner
from the outer boundary. The target claims a *named inward radial exploration*
determining $\mathrm{Circ}_n$ — the radial analogue of Algorithm 1 of
Ahlberg–Baldasso (arXiv:1708.03054), reconstructed in §2 — satisfies

$$\sup_{p\in[0.3,0.7]}\max_i \mathbf P_p[\text{query }i]\ \le\ 0.30\,n^{-1/3}
\tag{$\star$}$$

for every $n\ge 16$ (and hence a $0.3$-to-$0.7$ window of width $\le 0.70\,n^{-1/3}$).

**Theorem (disproof).** $(\star)$ is false. In fact, at the single parameter
$p=0.7$, some fixed macroscopic cell is queried with probability bounded below by
a positive constant independent of $n$, while the claimed cap tends to zero.

## 2. The radial exploration (faithful reconstruction)

Freeze the audit geometry: intensity 1, annulus $A(n,2n)$. Discretize as in
Ahlberg–Baldasso §3–§4 (two-stage construction with dense point set $\eta_k$ and
mesoscopic boxes of side $m$, $n^{-1/2}\ll m\ll 1$). The inward radial exploration is:

1. Choose a seed angle $\theta_0$ uniformly in $[0,2\pi)$.
2. Query all discretization cells meeting the seed ray
   $\{\arg z=\theta_0\}\cap A(n,2n)$ (plus neighbors, to resolve the local tiling —
   exactly as AB Step 4; correctness Lemma 4.1 requires this).
3. Iteratively query every cell red-connected (through revealed red cells) to the
   seed-ray cluster, until the full red components meeting the seed ray are
   determined; output whether a red circuit separates the boundaries.

Correctness *requires* exhaustive exploration of the attached red components:
as in AB Lemma 4.1, stopping early leaves tiling/connection ambiguity that an
adversary can flip. Hence, by construction, for every cell $i$,

$$R_i(p) := \mathbf P_p[\text{query }i]\ \ge\
\mathbf P_p[i\text{ is red-connected to the seed-ray cluster}]. \tag{1}$$

The revealment is $\max_i R_i(p)$ over deterministic discretization cells/points
(AB Proposition 4.4 uses exactly this normalization).

## 3. Constant lower bound at $p=0.7$

Fix a deterministic unit box $B$ centered at $(3n/2,0)$ and a deterministic unit
box $S(\theta_0)$ at radius $2n-\sqrt n$ adjacent to the seed ray (any fixed
relative position; both macroscopic). Let $C_\infty^{\mathrm{red}}$ be the red
infinite cluster and $\theta(0.7)=\mathbf P_{0.7}[x\in C_\infty^{\mathrm{red}}]$
(any $x$, by translation invariance).

- **Positivity.** Voronoi critical probability is $1/2$ (Bollobás–Riordan 2006),
  so $p=0.7$ is supercritical and $\theta(0.7)>0$ (this is the definition of
  $p_c$ as $\inf\{p:\mathbf P_p[0\leftrightarrow\infty]>0\}$).
- **Uniqueness.** The supercritical infinite red cluster is a.s. unique
  (Burton–Keane; the model is translation-invariant, ergodic, with finite energy
  — sprinkling red Poisson points in any bounded box has positive probability).
- **FKG.** $\{B\text{ meets }C_\infty^{\mathrm{red}}\}$ and
  $\{S(\theta_0)\text{ meets }C_\infty^{\mathrm{red}}\}$ are increasing events in
  the underlying independent (points, colors) product structure (the red set grows
  monotonically when a point is flipped blue$\to$red or a red point is added), so
  by the Poisson FKG inequality (e.g. Last–Penrose),
  $$\mathbf P_{0.7}[B\leftrightarrow C_\infty,\ S(\theta_0)\leftrightarrow C_\infty]
  \ \ge\ \mathbf P_{0.7}[B\leftrightarrow C_\infty]\,
  \mathbf P_{0.7}[S(\theta_0)\leftrightarrow C_\infty]
  \ \ge\ \theta(0.7)^2 =: c_0 > 0, \tag{2}$$
  since each factor is at least $\theta(0.7)$ (a box meets $C_\infty$ whenever its
  center lies in $C_\infty$). Conditional on both meeting the *unique* infinite
  cluster, $B$ is red-connected to $S(\theta_0)$, hence to the seed-ray cluster,
  so by (1), for *every* seed angle and *every* $n$,
  $$R_B(0.7)\ \ge\ c_0\ =\ \theta(0.7)^2\ >\ 0. \tag{3}$$

## 4. Contradiction

(3) gives $\sup_{p\in[0.3,0.7]}\max_i R_i(p)\ge c_0>0$ for all $n$, while
$(\star)$ demands it be $\le 0.30\,n^{-1/3}\to 0$. For every
$n>(0.30/c_0)^3$ the cap is violated (e.g. with any $c_0$, however small, such
$n$ exists). Hence $(\star)$ is false as a universal claim over $n\ge 16$. ∎

## 5. The window half falls with the revealment

The claimed $0.70\,n^{-1/3}$ window was to be *derived* from $(\star)$ via the
OSSS/Russo–Margulis differential inequality
$\frac{d}{dp}\mathbf P_p[\mathrm{Circ}_n]\ge 4\mathrm{Var}/\delta$ with
$\delta=0.30\,n^{-1/3}$. With $\delta\ge c_0$ the integration yields only a
constant window — no contradiction with the $0.4$ maximum width — so the window
bound is unproved (and the polynomial shape false at the claimed exponent).

## 6. Why the canonical proof route cannot be repaired (exact audit-patch check)

Replay `output/artifacts/radial_proxy.py`. At $n=16$ with the AB mesh
$m=1/\lceil 16^{1/4}\rceil=1/2$, the dyadic annulus family between $m$ and
$\sqrt m$ has $|J|=1$, and the AB one-arm bound reads
$\mathbf P[\mathrm{Arm}\mid\eta_k]\le 1/16+((1-q)+3/16)^{1/2}$ with
$q=c_1^4/32\le 1/32$; the base $(1-q)+3/16\ge 1.156>1$, so the bound is vacuous
($\min(1,\cdot)=1$), let alone $\le 0.119$. Even with perfect RSW input ($q=1$)
the floor is $1/16+(3/16)^{1/2}\approx 0.496\gg 0.119$, and a sweep over all
admissible meshes $m=16^{-a}$, $a\in[0.25,0.49]$, gives $|J|=1$ throughout.
Asymptotically the route yields exponent at most $q/(32\ln 2)\le 0.00141$
($236\times$ below $1/3$); with realistic RSW $c_1\approx 0.1$ it activates only
for $n\gtrsim 10^6$.

## 7. Supporting seeded proxy computations (heuristic, triangular lattice $p_c=1/2$)

- One-arm scaling $8\to 32$: log–log slope $-0.098\approx -5/48$ (rigorous
  exponent on the triangular lattice), $3.4\times$ flatter than $-1/3$;
  $\mathbf P[\text{arm to }32]=0.378$ vs $0.30\cdot 32^{-1/3}=0.094$ ($4\times$).
- Radial-query proxy on $A(16,32)$: at $p=0.7$, query probability $\approx 0.70$
  (95% CI lower edge $\ge 0.63$) at every radius $17$–$31$, vs cap $0.119$ —
  the predicted constant-vs-decaying separation is visible already at $n=16$.
- Supercritical density proxy: $\mathbf P_{0.7}[\text{origin cluster reaches }
  r=23]\approx 0.72$, so $\theta(0.7)^2\approx 0.52\gg 0.119$ in the proxy,
  illustrating the (3)-type lower bound shape.

These proxies use the triangular lattice (different model) and support, but do
not substitute, the rigorous §§3–4 argument, which uses only
Bollobás–Riordan ($p_c=1/2$), Burton–Keane (uniqueness), and Poisson FKG —
all standard citable results — plus the exhaustiveness property (§2) forced by
AB-style correctness.

## 8. What remains true / limitations

- The qualitative OSSS program (some polynomial window for the circuit event)
  is *not* refuted: AB's method should extend radially with a tiny unspecified
  exponent $\gamma>0$. Only the explicit $1/3$ exponent with constants
  $0.30/0.70$ is disproved.
- The disproof is asymptotic (some large $n$); it does not exhibit a violated
  scale with an explicit constant, since $\theta_{\mathrm{Voronoi}}(0.7)$ has no
  proved explicit lower bound. The universal ($\forall n\ge 16$) claim is
  nevertheless rigorously falsified.
- The argument targets every correct *exhaustive* frontier exploration (the only
  kind AB-style correctness permits); a non-exhaustive early-stopping variant
  would be a different algorithm from the named one and would need its own
  correctness proof.
- Proxy computations are triangular-lattice illustrations, not Voronoi evidence;
  the proof itself is analytic and self-contained modulo the three cited theorems.
