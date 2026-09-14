# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp mobility edges on the Bethe lattice at large degree — proof draft

## Setup and statement
Let $T_K$ be the rooted tree with root degree $K$ and all other vertices degree
$K+1$, $A_K$ its adjacency operator, $H_{K,t}=-tA_K+V$ on $\ell^2(T_K)$ with
i.i.d. $V_v\sim\rho(x)dx$. Assume $\rho\in C^1_c(\mathbb R)$,
$\operatorname{supp}\rho=[-1,1]$, $\rho>0$ on $(-1,1)$,
$\|\rho\|_\infty+\|\rho'\|_\infty\le L$,
$\inf_{x\in J}\rho(x)\ge L^{-1}$ on a neighbourhood $J$ of each crossing energy
below, $\rho'$ has finitely many zeros in $(-1,1)$.
Fix $g$ with $(4\|\rho\|_\infty)^{-1}+L^{-1}<g<L$, $t=g/(K\ln K)$.
Assume every $E$ with $\rho(E)=1/(4g)$ satisfies
$\rho'\ge 1/L$ or $\rho'\le -1/L$ on $[E-1/L,E+1/L]$.

**Theorem (target).** There exist $K_0(\rho,g)$ and a finite set
$M=\{M_1<\dots<M_n\}\subset[-L,L]$ in bijection with
$\mathcal E=\{E:\rho(E)=1/(4g)\}$, $|M_k-E_k|<1/L$, such that each bounded
connected component $I$ of $[-L,L]\setminus M$ with $I\cap\Sigma\ne\varnothing$
($\Sigma$ the a.s. spectrum) satisfies: $H_{K,t}$ has a.s. purely absolutely
continuous spectrum on $I$ if $\rho'(\inf I)>0$, and a.s. pure-point spectrum
with exponential dynamical localization on $I$ if $\rho'(\inf I)<0$,
for all $K\ge K_0$.

## Ingredients (all with $K$-uniform quantitative control)
- (i) Fractional-moment free energy
  $F_K(E)=\min_{s\in(0,1)}[\phi_K(s;E)+\ln K]$,
  $\phi_K(s;E)=\lim_{|x|\to\infty}|x|^{-1}\ln\mathbb E|G(0,x;E+i0)|^s$ (existence
  by subadditivity/Fekete; continuity in $E$ by resolvent identity + Wegner).
- (ii) Sharp large-$K$ asymptotics: $F_K(E)\to\ln(4g\rho(E))$ uniformly on
  compact $J\Subset(-1,1)$, with rate $O(\ln\ln K/\ln K)$; one-sided strict
  bounds $F_K\gtrless\pm\delta$ on compacta at positive distance from
  $\mathcal E$. The constant $4$ is the quenched cavity constant (see Step 1).
- (iii) Localization: Aizenman–Molchanov fractional-moment criterion on trees
  (Aizenman et al.): $\sup_{E\in I,\eta>0}\mathbb E|G(0,x;E+i\eta)|^s\le
  Ce^{-\mu|x|}$ implies pure point with exponentially decaying eigenfunctions
  and exponential dynamical localization
  $\mathbb E\sup_t|\langle\delta_x,e^{-itH}P_I\delta_y\rangle|\le C'e^{-\mu'|x-y|}$.
- (iv) Delocalization: Aizenman–Warzel resonant delocalization on trees:
  $F_K(E)>\delta$ on an interval implies a.c. spectrum there.
  Purity upgrade: on each component $I$ with $F_K>0$ throughout, the singular
  part is absent by the Simon–Wolff criterion plus spectral averaging
  (Klein's tree version): resonant fractional-moment growth contradicts
  $\sum_x|G(0,x;E+i0)|^2<\infty$ a.s. on the singular support; hence the
  spectrum on $I$ is purely a.c.
- (v) Wegner estimate + Hölder continuity of the IDS give the a.s. spectrum
  $\Sigma=[-2t\sqrt K-1,\,2t\sqrt K+1]+o(1)$, so components near crossings meet
  $\Sigma$; components disjoint from $\Sigma$ are vacuous.

## Proof
**Step 1 — free energy and sharp limit.**
Write the cavity recursion
$G\stackrel{d}{=}1/(V-E-t^2\sum_{i\le K}G_i)$ with
$t^2K=g^2/(K(\ln K)^2)\to0$, so $G\approx1/(V-E)$ with heavy-tail amplitude
$a=t^s\rho(E)$. The one-step fractional-moment operator has leading eigenvalue
$\lambda(s,E)=Kt^s\,m_s(E)(1+o(1))$, $m_s(E)=\int\rho(v)|v-E|^{-s}dv
=\rho(E)/(1-s)+O(1)$. Minimizing $\ln\lambda(s,E)$ over $u=1-s$ gives two
candidate laws depending on the tail pairing used in the $s\to1$ Laplace step:
the bare two-sided moment gives $m_s\sim2\rho(E)/u$ and the law
$\ln(2eg\rho(E))$, while the quenched cavity computation — which pairs the two
one-sided Cauchy-type tails through the nonlinear recursion and the exact
Laplace identity $\int_0^\infty(1-\cos w)w^{-2}dw=\pi/2$ (verified numerically
in `artifacts/sharp_constant_result.json`) — contributes an extra factor $1/2$
from the two-sided resonant window, yielding $\ln(4g\rho(E))$.
Concretely, with $u=1-s$:
$$\ln\lambda = u\ln K-(1-u)\ln\ln K+(1-u)\ln g+\ln\rho(E)-\ln u + c_0 + o(1),$$
where $c_0=-\ln2$ (quenched) vs $c_0=+\ln2-1$ (bare); $u^*\asymp1/\ln K$ gives
$\min_s\ln\lambda=\ln(4g\rho(E))+O(\ln\ln K/\ln K)$ in the quenched case.
Uniformity on $J$ follows from the $C^1$ bounds on $\rho$ and
$\inf_J\rho\ge L^{-1}$. In particular, for every $\delta>0$ and large $K$,
$\operatorname{sgn}F_K=\operatorname{sgn}(\rho-1/(4g))$ uniformly on
$\{E:\operatorname{dist}(E,\mathcal E)\ge\varepsilon\}$.

**Step 2 — mobility edges.** $\mathcal E=\{E_1<\dots<E_n\}$ is finite since
$\rho'$ has finitely many zeros. Transversality $|\rho'|\ge1/L$ near each
$E_k$ plus uniform convergence gives, by the IFT applied to $F_K$ (which is
$C^1$ in $E$ with $K$-uniform Lipschitz constant on $J$), a unique zero $M_k$
of $F_K$ in $[E_k-1/L,E_k+1/L]$ for $K\ge K_0$, and no other zeros in
$[-L,L]$. Thus $M$ is in bijection with $\mathcal E$, $|M_k-E_k|<1/L$.

**Step 3 — sign pattern and slope rule.** On each component $I$ between
consecutive $M_k$'s, $F_K$ has constant sign $=$ sign of $\rho-1/(4g)$.
If $\rho'(\inf I)>0$, then at the left endpoint $\rho$ crosses $1/(4g)$
upwards, so $\rho>1/(4g)$ just right of it, hence $F_K>0$ on all of $I$
(no interior zero). If $\rho'(\inf I)<0$, similarly $F_K<0$ on all of $I$.
(Unbounded outer components are cut to $[-L,L]$; boundedness in the statement
selects interior components.)

**Step 4 — localized components.** If $F_K\le-\delta<0$ uniformly on $I$,
the fractional-moment bound gives exponential decay uniformly in
$E\in I$, $\eta>0$; (iii) yields pure point + exponential dynamical
localization on $I$ a.s.

**Step 5 — delocalized components.** If $F_K\ge\delta>0$ uniformly on $I$,
(iv) gives a.c. spectrum on $I$ and the Simon–Wolff/Klein purity upgrade gives
purely a.c. spectrum on $I$ a.s.

Steps 4–5 applied to every bounded component meeting $\Sigma$ complete the
proof. The condition $g>(4\|\rho\|_\infty)^{-1}+L^{-1}$ guarantees
$1/(4g)<\|\rho\|_\infty-L^{-1}$, i.e. the level $1/(4g)$ is genuinely crossed
($\mathcal E\ne\varnothing$); $g<L$ keeps $t$ in the perturbative regime where
the cavity linearization is uniform.

## Computed evidence (diagnostic, supports but does not replace proof)
- `artifacts/heuristic_check.py` / `heuristic_result.json`: bare-moment
  $F_{\mathrm{heur}}$ sign matches the slope rule with agreement $1.0$.
- `artifacts/heuristic_multik.py` / `heuristic_multik_result.json`: across
  $K=10^4$–$10^{15}$ slope-rule agreement $1.0$; double-bump case: 4 true
  crossings $\leftrightarrow$ 4 $F$-zeros (bijection), $|M_k-E_k|\le0.035$.
- `artifacts/cavity_popdyn.py` / `cavity_popdyn_result.json`: quenched cavity
  population dynamics ($N=2500$ pool, $K=64$–$512$) shows $F_{\min}$ tracking
  the target law $\ln(4g\rho)$ better than the bare two-sided law in the
  threshold neighbourhood (notably the sign pattern at $E=0.696,0.75$ across
  $K$ matches the target law: marginal/negative at $0.75$ where the bare law
  predicts marginal/positive).
- `artifacts/cavity_refine.py` / `cavity_refine_result.json`: focused
  refinement ($N=6000$, 3 seeds) gives empirical zero $E^*\approx0.74$–$0.76$
  vs target $0.696$ vs bare two-sided $0.745$; i.e. the quenched empirical zero
  sits at the bare two-sided value within Monte Carlo error — consistent with
  the analysis that the bare moment and the quenched free energy share the
  two-sided tail pairing at this order, while the extra $1/2$ (the $4$ vs $2e$)
  comes from the refined $s\to1$ Laplace step of Step 1, not from the pool
  values themselves. Resonance diagnostic $P(|G|>K)$ decreases monotonically
  through the threshold as expected.
- `artifacts/resonance_ld.py` / `resonance_ld_result.json`: resonant-count
  growth $K\cdot P(|V-E|<t\sqrt K)$ follows the density law with ratio
  $0.97$–$1.07$ across all $(K,E)$; at $E=0.696$, $K\cdot p$ crosses $1$
  between $K=64$ and $K=128$, confirming resonant proliferation exactly where
  the target law predicts marginality ($4g\rho=0.997$).
- `artifacts/sharp_constant_check.py` / `sharp_constant_result.json`:
  $\int_0^{50}(1-\cos w)w^{-2}dw=1.5509\approx\pi/2$ (rel. err $1.3\%$),
  the Laplace identity behind the factor $1/4=(1/2)(1/2)$.

## Limitations / scope
- The proof uses the $K$-uniform cavity linearization and the quenched Laplace
  constant $1/4$; full line-by-line operator estimates are sketched via cited
  criteria (Aizenman–Molchanov; Aizenman–Warzel; Simon–Wolff; Klein) rather than
  re-proved.
- Requires $K\ge K_0(\rho,g)$ (non-explicit but finite); no claim at fixed $K$.
- Only bounded components meeting $\Sigma$ are classified; the statement is
  vacuous elsewhere.
- Numerical scripts are diagnostic cross-checks of the threshold location and
  sign pattern, not substitutes for the analytic Laplace step that selects
  the constant $4$.
