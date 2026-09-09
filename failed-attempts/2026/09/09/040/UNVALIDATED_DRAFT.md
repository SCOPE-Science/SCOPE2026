# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Explicit diffuse-regime certificate for two-marginal Coulomb transport on a cube
## (partial theorem toward an entropic-crystallization density regime; lane-377)

**Status.** This note proves a *one-sided, fully rigorous* partial result (fallback (a)+(b)
of the lane brief): an explicit correlation-energy lower bound for the uniform-density
cube cell, an explicit product-cost upper bound, and a certified **diffuse regime** in
which the symmetric entropic-regularized Coulomb minimizer cannot concentrate near any
deterministic (Monge / lattice-like) ansatz. The full two-sided crystallization threshold
`rs*` (lattice concentration at low density) is **not** proved here; it is stated as a
conjecture with the obstruction isolated. All constants are verified by rational
arithmetic a human can check; `output/artifacts/compute_bounds.py` replays them
deterministically. Monte-Carlo values are illustration only and are not used in any proof.

---

## 1. Setup

Let $L>0$, $Q_L=[0,L]^3$, $\rho_L = L^{-3}\mathbf 1_{Q_L}\,dx$ (uniform single-particle
density). Coulomb cost $c(x,y)=1/|x-y|$ ($+\infty$ on the diagonal, a null set).
Admissible plans $\Pi(\rho_L,\rho_L)$ with narrow topology (compact, metrizable).

Sharp problem and value:
$$C(\gamma)=\int_{Q_L^2} c\,d\gamma,\qquad
  V_0=\min_{\Pi(\rho_L,\rho_L)} C.$$

Entropic regularization (reference $\rho_L\otimes\rho_L$):
$$F_\varepsilon(\gamma)=C(\gamma)+\varepsilon\,S(\gamma),\qquad
  S(\gamma)=\mathrm{Ent}(\gamma\mid\rho_L\otimes\rho_L),$$
with $S(\gamma)=+\infty$ if $\gamma\not\ll\rho_L\otimes\rho_L$, else
$\int \log\frac{d\gamma}{d(\rho_L\otimes\rho_L)}\,d\gamma$.
Denote $V_\varepsilon=\inf_\Pi F_\varepsilon$ and minimizer $\gamma_\varepsilon$
(existence/uniqueness in Lemma 2).

Dimensionless regularization strength: $\eta=\varepsilon\,L$
($\varepsilon$ has units of energy $=1/$length; $\eta$ is dimensionless).
Wigner–Seitz radius $r_s$ is defined by $\tfrac43\pi r_s^3=L^3/N$
(volume per particle); §5 converts the threshold for $N=2$.

Two-point witness / Monge tube. For a Borel map $T:Q_L\to Q_L$ preserving $\rho_L$,
$\gamma_T=(\mathrm{id},T)_\#\rho_L$ is the deterministic (Monge) ansatz supported on
$\mathrm{graph}(T)$. Its $d$-tube is
$$U_{d,T}=\{(x,y)\in Q_L^2:\ |y-T(x)|<d\}.$$
$\gamma_T(U_{d,T})=1$ for every $d>0$. The corollary bounds $\gamma_\varepsilon(U_{d,T})$
uniformly in $T$.

## 2. Existence and elementary semicontinuity (proof)

**Lemma 1 (existence).** $V_0$ is attained. For every $\varepsilon>0$, $V_\varepsilon$ is
attained at a unique $\gamma_\varepsilon$.

*Proof.* $Q_L^2$ is compact so $\Pi(\rho_L,\rho_L)$ is narrowly compact (Prokhorov).
Truncated costs $c_M=\min(c,M)$ are continuous on $Q_L^2$ (capped continuously at the
diagonal with value $M$), so $\gamma\mapsto\int c_M\,d\gamma$ is continuous and
$C=\sup_M\int c_M$ is lower semicontinuous (l.s.c.) and bounded below by $0$; hence it
attains its minimum. $S(\cdot\mid\rho_L\otimes\rho_L)$ is l.s.c. with compact sublevels
and strictly convex where finite; $F_\varepsilon$ is thus l.s.c. with compact sublevels
(cost bounded below plus entropy coercivity), attains its minimum, and is strictly
convex, hence the minimizer is unique. ∎

**Remark (what is not claimed).** Full $\Gamma$-convergence
$F_\varepsilon\xrightarrow{\Gamma} C$ with recovery at singular (infinite-entropy)
minimizers is **not** proved here: the constant sequence fails exactly on
graph-concentrated plans ($S=+\infty$), and marginal-preserving smoothing is not
constructed in this note. The main theorem avoids any recovery sequence: it uses only
the competitor $\rho_L\otimes\rho_L$ (finite cost, zero entropy) for an upper bound,
the universal lower bound for energy, and Pinsker's inequality. Convergence of
minimizers to a sharp minimizer is therefore not claimed.

## 3. One-cell correlation bounds with explicit constants (proof)

Work in units $L=1$ and scale at the end ($C$ scales as $1/L$).

**Lemma 2 (universal lower bound).** For every $\gamma\in\Pi(\rho_L,\rho_L)$,
$$C(\gamma)\ge \frac{1}{\sqrt3\,L} > \frac{0.577}{L}.$$

*Proof.* For $x,y\in Q_L$, $|x-y|\le\sqrt3\,L$ (space diagonal), so $c\ge 1/(\sqrt3\,L)$
except on the null diagonal. Integrate. Numerically,
$1.733^2=3.002689>3$ so $\sqrt3<1.733$, hence $1/\sqrt3>1/1.733$; and
$1.733\times 0.577 = 0.999941<1$, so $1/1.733>0.577$. ∎

**Lemma 3 (product-cost upper bound).** Let $I_L$ be the cost of
$\gamma_{\rm prod}=\rho_L\otimes\rho_L$. Then
$$I_L \le \frac{3.571}{L}.$$

*Proof.* By scaling $x=Lu$ it suffices to take $L=1$. Fix $a>0$ and split
$1/r\le r^{-1}\mathbf 1_{\{r<a\}}+1/a$. For fixed $x\in Q_1$,
$$\int_{Q_1}\frac{dy}{|x-y|}
  \le \int_{\{|z|<a\}}\frac{dz}{|z|}+\frac{1}{a}
  = 4\pi\int_0^a r\,dr+\frac1a = 2\pi a^2+\frac1a,$$
using $\{y\in Q_1:|x-y|<a\}\subseteq\{|z|<a\}$. Integrating over $x$ gives the double
integral $\le 2\pi a^2+1/a$. At $a=1/2$: $I_1\le \pi/2+2$. With the certified enclosure
$\pi<3.142$ (standard; e.g. $3.140<\pi<3.142$), $I_1<3.142/2+2=3.571$. Scaling gives
$I_L=I_1/L$. ∎

**Per-pair gap.** Define $G_1=L\times(I_L-1/(\sqrt3 L))<3.571-0.577=2.994<3.0$
(deterministic replay in artifacts: $G_1=2.99396\ldots$).

## 4. Main theorem: certified diffuse regime (proof)

**Theorem (explicit diffuse certificate, $N=2$).** Let $\tau=0.1$. If
$$\eta=\varepsilon L > \frac{G_1}{2\tau^2}\quad(\text{in particular if }\eta\ge 150),$$
then the unique entropic minimizer $\gamma_\varepsilon$ satisfies
$$\mathrm{TV}(\gamma_\varepsilon,\rho_L\otimes\rho_L)<0.1,$$
where $\mathrm{TV}$ is total variation. Consequently, for the tube ratio $d/L=0.1$,
uniformly over all measure-preserving $T$,
$$\gamma_\varepsilon(U_{d,T}) < 0.11,$$
so $\gamma_\varepsilon$ cannot assign mass $\ge 0.9$ (indeed $\ge 0.11$) to any single
Monge tube; it is certified diffuse in this regime. In Wigner–Seitz units ($N=2$),
$\varepsilon r_s>73.9$ suffices (see §5).

*Proof.* Competitor bound: $V_\varepsilon\le F_\varepsilon(\gamma_{\rm prod})=I_L+0\le
3.571/L$. Energy floor: $C(\gamma_\varepsilon)\ge 1/(\sqrt3\,L)>0.577/L$. Hence
$$S(\gamma_\varepsilon)\le\frac{I_L-C_{\min}}{\varepsilon}
  \le \frac{G_1}{\varepsilon L}=\frac{G_1}{\eta}.$$
With $G_1<2.994$ and $\eta\ge 150$: $S<2.994/150=0.01996$. Pinsker's inequality
$\mathrm{TV}^2\le S/2$ gives $\mathrm{TV}<\sqrt{0.00998}<0.0999<0.1$ (since
$0.1^2\times2=0.02>0.01996$). The general threshold $\eta>G_1/(2\tau^2)$ follows from
the same chain with $\tau$ in place of $0.1$; $G_1/(2\tau^2)<2.994/0.02=149.7<150$.

Tube exclusion: under the product measure, for each $x$,
$\rho_L(\{y:|y-T(x)|<d\})\le \frac43\pi d^3/L^3$ (ball volume; intersection with the
cube only smaller). Integrating over $x$:
$(\rho_L\otimes\rho_L)(U_{d,T})\le\frac43\pi(d/L)^3$, uniformly in $T$. At $d/L=0.1$
with $\pi<3.142$: $\le \frac43(3.142)(10^{-3)}<0.0042$. By the coupling characterization
of TV, $\gamma_\varepsilon(U)\le(\rho_L\otimes\rho_L)(U)+\mathrm{TV}$, giving
$<0.0042+0.1=0.1042<0.11$. Since $\gamma_T(U_{d,T})=1$, any Monge plan is at TV-distance
$\ge 0.89$ from $\gamma_\varepsilon$. ∎

## 5. Wigner–Seitz conversion ($N=2$)

$L^3/N=\frac43\pi r_s^3$ gives $L=f_N r_s$ with $f_2=(8\pi/3)^{1/3}$. Enclosure:
$2.03^3=8.365427<8\pi/3$ and $8\pi/3<8(3.142)/3=8.3787<2.033^3=8.402443$ (using
$3.140<\pi<3.142$), so $f_2\in[2.03,2.033]$ (replayed in artifacts). Since
$\varepsilon L=\varepsilon f_2 r_s$ and $f_2\ge 2.03$,
$$\varepsilon r_s>73.9 \implies \varepsilon L>73.9\times2.03=150.017>150,$$
so the theorem applies. (Artifacts record the unrounded value
$\mathrm{thr}/2.03=73.74\ldots<74$.)

## 6. Deterministic replay and Monte-Carlo illustration

`output/artifacts/compute_bounds.py` (numpy only, seeded) checks every rational
enclosure above ($\sqrt3$ squaring, $\pi$-based caps, gap, Pinsker threshold, tube mass,
$r_s$ factor) with `assert`, writing `output/artifacts/results.json`. All assertions pass.
Seeded ($M=4\times10^5$) Monte-Carlo of the product cost gives mean $1.883\pm0.0023$
(3$\sigma$ interval $[1.877,1.890]\subset[0.577,3.571]$) and short-range mass
$0.0267$ at $\alpha=0.2$ versus the analytic cap $\frac43\pi(0.2)^3<0.0336$ — consistent
with, but not used in, the proofs.

## 7. Delimitation: conjecture, not claim

*Crystallization side (open).* Whether for $\eta\ll1$ (equivalently large $r_s$ at fixed
physical $\varepsilon$) every cluster point of $\gamma_\varepsilon$ concentrates near a
BCC-like lattice support with a two-point witness above threshold is left as an explicit
conjecture; the obstruction is the missing marginal-preserving recovery/smoothing at
singular plans (§2 remark) plus a lattice-ansatz upper bound. No $r_s^*$ lower
(crystallization) threshold is claimed.

*General $N$.* The pair-cost decomposition for exchange-symmetric $N$-plans is not
proved here; the theorem is stated for $N=2$ only, where symmetrization is vacuous.
Extension via the averaged two-marginal and entropy monotonicity is future work.

## 8. Originality boundary

Foundations (SCE as Coulomb multi-marginal OT: Friesecke–Gerolin–Gori-Giorgi review,
arXiv:2202.09760), the HK$\to$SCE semiclassical limit via plan smoothing
(Cotar–Friesecke–Kl\"uppelberg, arXiv:1706.05676), radial co-motion non-optimality with
the deterministic/crystallization question left open (Seidl et al., arXiv:1702.05022),
entropic SCE for kinetic correlations rather than a density threshold
(Gerolin–Grossi–Gori-Giorgi, arXiv:1911.05818), and the Lieb–Oxford constant improvement
1.58 (Lewin–Lieb–Seiringer, arXiv:2203.12473) provide tools and context but none states
or implies the explicit one-cell diffuse certificate above ($\eta\ge150$, i.e.
$\varepsilon r_s>73.9$ for $N=2$, with TV$<0.1$ and uniform Monge-tube exclusion). The
combination — elementary product competitor + universal diagonal bound + Pinsker — is a
new quantitative boundary lemma, not a repackaging of numerics.
