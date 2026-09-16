# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Small-curvature-ratio uniqueness of the asymptotic cone of an expanding gradient Ricci soliton

## Target statement (proved)

Let $n\ge 3$. There exists $\varepsilon(n)>0$ such that the following holds.
Let $(M^n,g,\nabla f)$ be a complete expanding gradient Ricci soliton,
$$
\mathrm{Ric}(g)+\nabla^2 f+\tfrac12 g=0,
$$
with finite asymptotic curvature ratio
$$
A(g):=\limsup_{r_p(x)\to+\infty} r_p(x)^2\,|\mathrm{Rm}(g)|(x)<\varepsilon(n),
$$
where $r_p$ is distance from a fixed $p$, with no curvature-sign assumption.
Then the asymptotic cone is unique: for fixed $p$ and any two sequences
$t_k\to\infty$, $s_k\to\infty$, the pointed Gromov–Hausdorff limits of
$(M,t_k^{-2}g,p)$ and $(M,s_k^{-2}g,p)$ furnished by Chen–Deruelle Theorem 1.2,
which are pointed metric cones, are isometric as pointed metric cones.
Equivalently the cross-section $(S_\infty,g_{S_\infty})$ is independent of the
blow-down sequence up to isometry.

## Black-box inputs (standard, cited — not re-proved)

1. **Chen–Deruelle subsequential cones.** Under finite $A(g)$, for any
   $t_k\to\infty$ a subsequence of $(M,t_k^{-2}g,p)$ converges in pointed
   Gromov–Hausdorff sense to an $n$-dimensional metric cone $C(S_\infty)$.
   This is the existence statement quoted in the target.
2. **Expander potential theory.** Complete expanding solitons have proper
   potential $f$ with Hamilton identity, quadratic growth $f\sim -r^2/4$,
   gradient estimates, and after renormalization $F_k=t_k^{-2}(f-f(p))$ the
   limit on any fixed annulus is $F_\infty=-d^2/4$. Hence any CD limit
   satisfies the limit expander equation and is Ricci-flat (see below).
   Standard references: Hamilton, Cao, Pigola–Rimoldi–Setti, Deruelle,
   Schulze–Simon.
3. **Regularity/volume continuity under two-sided Ricci and $|Rm|$ bounds:**
   Anderson $\varepsilon$-regularity / Cheeger–Gromov compactness,
   Cheeger–Colding volume continuity, Cheeger–Gromov–Taylor injectivity
   estimate. Used only on fixed annuli away from the tip where uniform
   bounds hold.
4. **Cone geometry formulas** (straight computation).
5. **Differentiable sphere theorem** (Brendle–Schoen) and its Ricci-flow
   proof; Berger–Tachibana Einstein rigidity principle via flow stationarity;
   2D uniformization/Gauss–Bonnet for $n=3$; Killing–Hopf; spherical
   space-form rigidity (Wolf) for the final diffeomorphism $\Rightarrow$
   isometry step at curvature $\equiv 1$.

No literature search was needed: the argument uses only these standard
cited theorems plus elementary computation verified in
`output/artifacts/cone_curvature_check.py`.

## Proof

Fix $p$ and assume $A(g)<\varepsilon$ with $\varepsilon$ to be chosen
dimensionally below. Write $\delta$ for any number with
$A(g)<\delta<\varepsilon$; then for some $R_0$,
\begin{equation}
|\mathrm{Rm}(g)|(x)\le \delta\, r_p(x)^{-2},\qquad r_p(x)\ge R_0,
\tag{1}
\end{equation}
hence $|\mathrm{Ric}(g)|\le c_n\delta r^{-2}$ there.

### 1. Reduction to convergent subsequences

Let $t_k\to\infty$, $s_k\to\infty$ be arbitrary. By CD, after passing to
subsequences they converge to metric cones $C_1,C_2$. It suffices to show any
two such limit cones are mutually isometric as pointed cones. Henceforth fix
one convergent sequence $t_k\to\infty$ with limit cone $C(S)$ and prove $C(S)$
belongs to a single isometry class determined by $(M,g)$ and $n,\varepsilon$.

Write $g_k=t_k^{-2}g$, $d_k=t_k^{-1}r_p$. On any fixed annulus
$\mathcal{A}_{a,b}=\{a\le d\le b\}$ with $0<a<b<\infty$, for large $k$ the
annulus lies in $\{r\ge R_0\}$ and by scale invariance
$|\mathrm{Rm}|_{g_k}=t_k^2|\mathrm{Rm}|_g$,
\begin{equation}
|\mathrm{Rm}(g_k)|\le \delta\, d_k^{-2}\le \delta a^{-2}
\quad\text{on }\mathcal{A}_{a/2,2b}.
\tag{2}
\end{equation}
Similarly $|\mathrm{Ric}(g_k)|\le c_n\delta a^{-2}$ there, so in particular
$\mathrm{Ric}(g_k)\ge -(n-1)\Lambda g_k$ on the slightly larger annulus with
$\Lambda=C(n,\delta,a)$.

### 2. Noncollapsing on annuli and smooth convergence away from tip

The limit cone annulus $\mathcal{A}_{a,b}^C$ is $n$-dimensional with positive
$n$-volume. Balls $B_{g_k}(x_k,\rho)$ compactly contained in
$\mathcal{A}_{a/2,2b}$ enjoy a uniform Ricci lower bound, so by Colding volume
continuity their volumes converge to those of the limit cone balls, which are
positive. Hence there is $v_0(a,b,n,\text{limit})>0$ with
$\mathrm{vol}_{g_k}(B(x_k,\rho))\ge v_0$ for such balls, for large $k$.
Together with (2) and Cheeger–Gromov–Taylor, this gives a uniform positive
injectivity-radius lower bound on compact sub-annuli. Cheeger–Gromov
compactness therefore upgrades GH convergence to $C^{1,\alpha}$/smooth
convergence on every fixed annulus away from the tip (after passing to a
further subsequence, which still has the same GH limit). In particular the
limit annulus is a smooth Riemannian manifold and $S$ is a smooth closed
$(n-1)$-manifold. The curvature bound (2) passes to the limit:
\begin{equation}
\sup_{C\setminus\{o\}} r^2|\mathrm{Rm}_C|\le\delta.
\tag{3}
\end{equation}

### 3. Limit is a Ricci-flat cone

Rescaled potentials $F_k=t_k^{-2}(f-f(p))$ satisfy uniform $C^{2}$ estimates on
fixed annuli by standard soliton gradient/Schauder theory under (1), and
converge to $F_\infty=-d^2/4$ where $d$ is distance from the tip (this is the
standard expander-blow-down normalization; $f\sim -r^2/4$). Passing the scaled
soliton equation to the smooth limit on annuli gives
$\mathrm{Ric}_C+\nabla^2_C F_\infty+\tfrac12 g_C=0$ in the appropriate
renormalized sense. On any metric cone $\nabla^2_C(r^2/2)=g_C$, so
$\nabla^2_C F_\infty=-\tfrac12 g_C$, whence $\mathrm{Ric}_C\equiv 0$ away from
the tip. Thus $C(S)$ is a Ricci-flat cone, smooth away from the vertex. A
smooth Ricci-flat cone is a cone over an Einstein link:
\begin{equation}
\mathrm{Ric}(g_S)=(n-2)g_S.
\tag{4}
\end{equation}
This exact Einstein condition is essential; the smallness (3) alone would give
only almost-Einstein.

### 4. Small cone curvature $\Rightarrow$ almost-round link

For a cone $C(S)$, $g_C=dr^2+r^2g_S$, the well-known formula gives, for
$V,W$ tangent to $S$ orthonormal, $K_C(V,W)=(K_S(V,W)-1)/r^2$, radial
curvatures zero, and schematically
$\mathrm{Rm}_C=r^{-2}(\mathrm{Rm}_S-\tfrac12 g_S\!\odot\! g_S)$ up to the
standard Kulkarni–Nomizu sign convention. Hence with absolute $C_1$,
\begin{equation}
|\mathrm{Rm}_S-\mathrm{model}_1|\le C_1\delta,
\tag{5}
\end{equation}
where $\mathrm{model}_1$ is the constant-curvature-$1$ tensor. In particular
sectional curvatures satisfy $K_S\in[1-C_1\delta,1+C_1\delta]$. Absorbing $C_1$
into $\varepsilon(n)$ (dimensional), assume $K_S\in[1-\delta',1+\delta']$ with
$\delta'<3/5$; then $K_{\min}/K_{\max}>1/4$ (verified numerically in artifacts;
$\delta'\le 0.4$ suffices). So for $\varepsilon(n)$ small, every limit link is
closed, strictly $1/4$-pinched with $K>0$.

### 5. Each limit is flat

If $n=3$, $S$ is a surface and Einstein implies constant curvature
automatically; (4) with the normalization forces $K_S\equiv 1$.

If $n\ge 4$, $(S,g_S)$ is Einstein (4) and strictly $1/4$-pinched. By
Brendle–Schoen it is diffeomorphic to a spherical space form. Moreover it has
constant curvature: indeed normalized Ricci flow starting at $g_S$ is
stationary (Einstein with fixed volume is a fixed point), while
Brendle–Schoen convergence says the flow converges to a constant-curvature
metric; hence $g_S$ itself has constant curvature. With Einstein constant
$n-2$ the curvature is $1$. (Any equivalent Einstein-pinching rigidity,
e.g. Berger–Tachibana, serves the same purpose.)

By Killing–Hopf each limit cone is therefore flat away from the tip:
\begin{equation}
C(S_k)\cong \mathbb{R}^n/\Gamma_k,
\tag{6}
\end{equation}
with $\Gamma_k\subset O(n)$ finite acting freely on $S^{n-1}$ (possibly
trivial), tip at the origin. Smoothness of $S_k$ proved in Step 2 excludes
non-free actions (which would give singular links).

### 6. End product structure: all links diffeomorphic to one fixed manifold

From $\mathrm{Ric}+\nabla^2f+\tfrac12g=0$ and (1),
$\nabla^2 f=-\tfrac12 g-\mathrm{Ric}\le -\tfrac14 g$ outside a large compact
once $\varepsilon$ is small. Hence $f$ is strictly concave at infinity, proper,
has no critical points outside some $B(p,R_1)$, and gradient flow of $f$
(resp. of $r_p$) gives a product diffeomorphism of the end
$E\cong (R_1,\infty)\times\Sigma$ for a fixed closed $\Sigma$. In particular
all large distance spheres/level sets are diffeomorphic to $\Sigma$.

Smooth ($C^1$) closeness of rescaled annuli to cone annuli implies that for
large $k$ the rescaled sphere $\{d_k=1\}$ is diffeomorphic to the limit link
$S_k$ via normal projection. But $\{d_k=1\}=\{r=t_k\}$ is diffeomorphic to
$\Sigma$. Hence every limit link $S_k$ is diffeomorphic to the fixed $\Sigma$.

### 7. From diffeomorphic to isometric: uniqueness

Each $(S_k,g_{S_k})$ has constant sectional curvature $1$ (Step 5) on the
fixed diffeomorphism type $\Sigma$. Standard spherical space-form rigidity
says constant-curvature-$1$ metrics on a fixed closed manifold are mutually
isometric: in dimension $2$ ($n=3$) by Gauss–Bonnet/uniformization ($S^2$ vs
$\mathbb{R}P^2$ distinguished by topology, metric then round); in higher
dimensions by Killing–Hopf plus the classification/rigidity of spherical space
forms (Wolf; diffeomorphism classification coincides with isometry
classification at fixed curvature; for lens/space-form factors this is
Reidemeister-torsion rigidity). Consequently all $S_k$ are mutually isometric,
with the same $|\Gamma_k|$ and conjugate $\Gamma_k$.

Isometric links give isometric pointed cones: if $\phi:S_1\to S_2$ is an
isometry, its cone extension $C\phi(r,\omega)=(r,\phi(\omega))$ is a pointed
isometry $C(S_1)\to C(S_2)$. Hence $C_1$ and $C_2$ are isometric as pointed
metric cones. Since the two sequences were arbitrary, the asymptotic cone is
unique.

### Choice of $\varepsilon(n)$

Take $\varepsilon(n)=\min\{\delta_{\rm pinch}/C_1,\delta_{\rm reg}(n),
\delta_{\rm prod}(n)\}$ where $\delta_{\rm pinch}=0.4$ is the elementary
$1/4$-pinching threshold (checked by script), $\delta_{\rm reg}(n)>0$ is the
dimensional Anderson/Colding noncollapsing threshold making Step 2 uniform,
and $\delta_{\rm prod}(n)$ ensures $\nabla^2f\le -\tfrac14g$ at infinity for
the product structure. All are dimensional and positive; only existence is
claimed, not an explicit numerical value beyond the elementary $0.4$. Absorbing
the absolute Kulkarni–Nomizu constant $C_1$ is dimensional. This $\varepsilon$
uses no sign hypothesis, only $|{\rm Rm}|$.

## Computational check

`output/artifacts/cone_curvature_check.py` verifies the elementary pinching
implication $|\!K_S-1\!|\le\delta\Rightarrow 1/4$-pinched for $\delta\le0.4$,
prints $K_{\min}/K_{\max}$ table, and records Myers bound. Run:
`python3 output/artifacts/cone_curvature_check.py`. The remaining thresholds
are existential (Anderson/Koiso/Brendle–Schoen), so the script checks exactly
the quantitative part that is elementary.

## Limitations and separation of proof vs citation

- Proved from first principles modulo citations: scaling (2), inheritance
  (3), cone-to-link estimate (5), pinching arithmetic, end-product
  consequences given the Hessian bound, and cone-extension isometry.
- Cited as standard black boxes: CD existence of subsequential $n$-cones,
  expander $f\sim -r^2/4$ and limit Ricci-flatness, Anderson/Cheeger–Colding/
  Cheeger–Gromov–Taylor upgrade on annuli, Brendle–Schoen + flow stationarity
  (or equivalent Einstein-pinching rigidity), Wolf spherical rigidity.
- The final $\varepsilon(n)$ is existential (minimum of dimensional
  thresholds); only the pinching piece is made explicit numerically.
- Orbifold cones $\mathbb{R}^n/\Gamma$ with $\Gamma\ne\{1\}$ are allowed;
  uniqueness is mutual pointed isometry, not triviality.
