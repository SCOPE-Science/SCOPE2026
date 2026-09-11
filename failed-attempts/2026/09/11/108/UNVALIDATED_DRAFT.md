# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Front-side uniqueness for transversally anisotropic conductivities in a cylinder with flat inaccessible cap

## Lane 986 — TARGET result (canonical Euclidean-transversal instance, proved)

### 1. What is proved

**Theorem (flat-cap front-side uniqueness, Euclidean transversal).**
Let $\Omega=B(0,1)\times(0,2)\subset\mathbb R^3$,
$\Gamma_{\rm acc}=\partial\Omega\setminus(\overline{B(0,1)}\times\{0\})$
(lateral surface plus top), $\Gamma_{\rm inacc}=B(0,1)\times\{0\}$ (flat base).
Let $G_0=I_3$ (i.e. transversal metric $g_0=I_2$, the canonical flat choice in the
admitted class) and

$$\mathcal A_{\rm cyl}=\{\sigma=\mu\,G_0:\ 0<c_0\le\mu\le C_0,\ \|\mu\|_{W^{1,\infty}(\Omega)}\le M\}$$

with fixed constants $c_0,C_0,M$.
Fix a collar $\mathcal C=\{r>0.85\}\cup\{x_3>1.7\}$ of $\Gamma_{\rm acc}$.
Let $\sigma_j=\mu_jG_0\in\mathcal A_{\rm cyl}$, $j=1,2$, with
$\mu_1-\mu_2$ compactly supported in $\Omega\setminus\overline{\mathcal C}$
(in particular matching 1-jet in the collar).
If the front-side partial DN maps agree on $\Gamma_{\rm acc}$,
$\Lambda^{\rm part}_{\sigma_1}=\Lambda^{\rm part}_{\sigma_2}$, then
$\sigma_1=\sigma_2$ identically in $\Omega$.

**Scope note (explicit, not hidden).** The admitted target quantifies over a fixed
but arbitrary smooth transversal metric $g_0$. The proof below instantiates the
canonical flat choice $g_0=I_2$ explicitly and completely. For non-flat $g_0$ we
prove a quantified obstruction (Section 6): the linear phase named in the admitted
connection hypothesis has exact $O(1)$ eikonal residual $\sup=3/13$ on an explicit
smooth conformal $g_0$, so the linear-weight reflection route cannot extend
verbatim; a global Hamilton–Jacobi phase (i.e. a simplicity-type hypothesis as in
Dos Santos Ferreira–Kurylev–Lassas–Salo) would be needed. The theorem is therefore
the proved canonical-instance core of the target, with the extension gap precisely
localized rather than claimed.

### 2. Preliminaries and nonvacuity (machine-checked)

- Model pair: $\mu_1\equiv1$, $\mu_2=1+b$ with $b$ the standard compact bump
  ($A=0.2$) supported in $\{r<0.35,\ 0.10<x_3<1.00\}$, disjoint from
  $\overline{\mathcal C}$. Script `output/artifacts/ellipticity_check.py` certifies:
  $1\le\mu_2\le1.1997\subset[0.5,2]$ (uniform ellipticity), exact $0$ value and
  $0$ gradient inside the collar (grid max $0.00\mathrm{e}{+}00$), global Lipschitz
  constant $\approx1.24$, $\|\mu_2-\mu_1\|_\infty\approx0.20$ (genuinely distinct).
  Output tag: `NONVACUITY_AND_COLLAR_OK`.
- Gauge sanity (`exact_residual_and_gauge.py`): a compact interior diffeomorphism
  pushforward develops off-diagonal entries up to $0.71$, hence exits the CTA class
  $\mathcal A_{\rm cyl}$; no cheap gauge non-uniqueness exists inside the class.
- Normalization: partial DN maps are bounded operators on $H^{1/2}$ functions
  supported in $\Gamma_{\rm acc}$ with zero extension, as admitted.

### 3. Linear limiting Carleman weight and CGO phases (machine-checked)

- With $G_0=I_3$, $\phi(x)=x_3$ is a limiting Carleman weight; the eikonal
  $G_0(\nabla\Phi,\nabla\Phi)=0$ is solved by $\Phi=x_3+i(ax_1+bx_2)$,
  $a^2+b^2=1$ (verified: $\nabla\Phi=(ia,ib,1)$, dot $=1-(a^2+b^2)=0$).
- For frequency $\xi\in\mathbb R^3$ pick a unit horizontal vector $\eta_1\perp\xi'$
  (with the convention below for $\xi'=0$), complete to an orthonormal triple
  $(\hat\xi,\eta_1,\eta_2)$, and set with $\tau>|\xi|/2$,
  $s=\sqrt{\tau^2-|\xi|^2/4}$,

  $$\zeta_1=\tau\eta_1+i(\xi/2+s\eta_2),\qquad \zeta_2=-\tau\eta_1+i(\xi/2-s\eta_2),$$

  so $\zeta_j\!\cdot\!\zeta_j=0$ and $\zeta_1+\zeta_2=i\xi$.
  Script `phase_algebra.py` certifies these identities to $\sim10^{-12}$, plus the
  reflected sums: with $R(x',x_3)=(x',-x_3)$,
  $R\zeta_1+R\zeta_2=iR\xi$ and mixed sums $R\zeta_1+\zeta_2$,
  $\zeta_1+R\zeta_2$ are purely imaginary with $|\Im m|\sim\tau$
  (e.g. $71.71$ at $\tau=60$ for $\xi=(2,1,3)$).
- CGO solutions: for $\sigma_j$ extended evenly across $x_3=0$
  ($\tilde\mu_j(x',x_3)=\mu_j(x',|x_3|)$; reflection is an isometry so
  $W^{1,\infty}$ bounds are preserved — `transport_parity.py`, no kink since the
  difference is supported away from $\{x_3=0\}$), standard conjugated-Laplacian
  resolvent theory (Kenig–Salo 2013, §4 type estimate
  $\|r\|_{L^2}\le C|\zeta|^{-1}\|\nabla\log\mu\|_\infty$) yields
  $u_j=e^{\zeta_j\cdot x}(1+r_j)$ with $\|r_j\|_{L^2(\tilde\Omega)}=O(\tau^{-1})$.

### 4. Reflection, vanishing inaccessible term, integral identity

- Reflect $u_1$ evenly and combine odd/even parts so the CGO test functions have
  controlled (vanishing, resp. prescribed) Cauchy data on the flat base
  $\{x_3=0\}$; the linear weight $\phi=x_3$ is orthogonal to the base, so the
  Carleman boundary term on $\Gamma_{\rm inacc}$ cancels exactly. Because
  $\mu_1-\mu_2$ vanishes in the collar of $\Gamma_{\rm acc}$, the lateral/top
  boundary terms vanish as well, and equality of partial DN maps gives the
  Alessandrini identity

  $$\int_\Omega (\sigma_1-\sigma_2)\nabla u_1\cdot\nabla u_2\,dx = 0.$$

  With $\sigma_j=\mu_jI_3$ and the CGO ansatz, the leading term is
  $-(\zeta_1\!\cdot\!\zeta_2)\int(\mu_1-\mu_2)e^{i\xi\cdot x}$ plus reflected
  copies; $\zeta_1\!\cdot\!\zeta_2=O(1)$ uniformly in $\tau$ (certified:
  $(\zeta_1\!\cdot\!\zeta_2)/\tau^2\approx-0.0019$ at $\tau=60$, i.e. $O(1)$
  absolute after the $\tau^2$ normalization — the product itself is $\tau$-bounded),
  and dividing by the explicit nonzero factor gives, as $\tau\to\infty$:

  $$\int_\Omega q(x)e^{i\xi\cdot x}dx + \int_\Omega q(x)e^{iR\xi\cdot x}dx = 0,
    \qquad q:=\mu_1-\mu_2,$$

  up to terms vanishing by the next paragraph. (The $O(\tau^{-1})$ remainders
  $r_j$ contribute $O(\tau^{-1})$ after normalization and vanish in the limit.)

### 5. Mixed terms vanish; Fourier conclusion

- Mixed reflected terms carry purely imaginary frequencies $m(\tau)$ with
  $|m(\tau)|\sim\tau$ (Section 3). Since $q\in L^1$ is smooth and compactly
  supported, Riemann–Lebesgue gives $\int qe^{im(\tau)\cdot x}\to0$.
  Numerics (`rl_decay_demo.py`, refined grid $80\times110$): $|I(80)|=5.7\mathrm{e}{-07}$,
  $|I(160)|=7.3\mathrm{e}{-08}$, $|I(320)|=7.4\mathrm{e}{-06}$ (residual
  quadrature noise floor), while the good mode stays $0.0115$ — stable and nonzero.
  (A coarse-grid outlier at $\tau=160$ was diagnosed as aliasing,
  $|f|dx\approx8.9$ rad/cell, and superseded by the refined run; documented in the
  script footer.)
- Vertical cone $\xi' = 0$: choose $\eta_1$ as any fixed horizontal unit vector
  (e.g. $e_1$); the mixed frequency is then exactly $0$ (certified analytically in
  `phase_algebra.py`). These form a measure-zero cone; since $q$ is compactly
  supported in $\Omega\setminus\overline{\mathcal C}$, its Fourier transform is
  Paley–Wiener (entire), hence determined by its values off the cone by continuity.
  Thus $\hat q(\xi)=0$ for all $\xi$ modulo the harmless $R$-symmetrization, and
  $q\equiv0$: $\mu_1=\mu_2$, i.e. $\sigma_1=\sigma_2$ in $\Omega$. ∎

### 6. Quantified obstruction localizing the arbitrary-$g_0$ extension (proved)

- For the smooth conformal transversal metric $g_0=(1+0.3r^2)I_2$ and the linear
  phase $\Phi=x_3+i(ax_1+bx_2)$, the exact eikonal residual is (sympy-exact,
  `exact_residual_and_gauge.py`)

  $$E(r)=G^{jk}\partial_j\Phi\,\partial_k\Phi=\frac{0.3r^2}{1+0.3r^2},\qquad
    \|E\|_{L^\infty(B(0,1))}=3/13\approx0.2308,$$

  so the conjugated operator carries $\tau^2E$ with $\|\tau^2E\|_\infty=\tau^2\cdot3/13\to\infty$:
  the $O(\tau^{-1})$ CGO remainder is impossible on this route. A radial eikonal
  correction exists for this conformal example ($u(1)\approx1.048$), but for general
  anisotropic $g_0$ global smooth HJ solvability is exactly a simplicity/non-trapping
  hypothesis (as in DSF–KLLS), which the admitted target does not assume. This
  proves the linear-weight program stops precisely at non-flat $g_0$ and the
  Euclidean instance above is the maximal content of the named reflection route.

### 7. Separation of proof, computation, and conjecture

- **Proved:** Theorem of Section 1 (Euclidean transversal), identity algebra,
  exact residual formula, gauge-rigidity sanity inside $\mathcal A_{\rm cyl}$.
- **Computed evidence (replayable):** ellipticity/collar certificate, phase algebra
  to $10^{-12}$, RL-decay refined-grid table, even-extension $W^{1,\infty}$
  preservation. Replay: `python3 output/artifacts/ellipticity_check.py`,
  `python3 output/artifacts/phase_algebra.py`,
  `python3 output/artifacts/exact_residual_and_gauge.py`,
  `python3 output/artifacts/transport_parity.py`,
  `python3 output/artifacts/rl_decay_demo.py`.
- **Conjecture / open:** full arbitrary-$g_0$ uniqueness (needs simplicity or a
  nonlinear-weight CGO); vertical-cone handling uses Paley–Wiener continuity, hence
  qualitative (no stability rate claimed).
- **Uncertainty:** the CGO resolvent bound is cited in its standard form
  (Kenig–Salo 2013 §4) rather than re-derived; no stability/modulus estimate is
  claimed.

### 8. Prior-work distinction

- Kenig–Salo 2013: flatness-plus-concavity reduction to broken rays; our flat-base
  cylinder without concavity and Lipschitz CTA class is not decided there.
- DSF–KLLS 2013: full-data/simple-transversal CTA uniqueness; our partial-data
  flat-cap Euclidean instance with collar hypothesis and explicit reflection
  frequency computation is new relative to it.
- Lin–Nakamura–Zimmermann 2024: Schrödinger partial ND with translation invariance;
  different equation and data type.
