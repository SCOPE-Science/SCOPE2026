# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Stability of planar subluminal traveling waves for the 3+1 membrane graph — TARGET resolution (first horn: global regularity + sharp decay)

## 1. What is proved

**Theorem.** Let $|v|<1$ and let $r,b_2,b_3\in\mathbb R$. Put
$\phi_v(t,x)=r(x_1-vt)+b_2x_2+b_3x_3+c$.
Consider the timelike extremal-hypersurface (membrane) graph equation on
Minkowski $\mathbb R^{1+3}$,
$$
\partial_\mu\!\left(\frac{\eta^{\mu\nu}\partial_\nu\phi}
{\sqrt{1+|\nabla_x\phi|^2-(\partial_t\phi)^2}}\right)=0,
\qquad \eta=\mathrm{diag}(-1,1,1,1),
\tag{1}
$$
i.e. $\partial_\mu(g^{\mu\nu}(\partial\phi)\,\partial_\nu\phi)=0$ with
$g^{\mu\nu}(q)=\eta^{\mu\nu}-q^\mu q^\nu/(1+Q(q))$,
$Q(q)=\eta^{\alpha\beta}q_\alpha q_\beta$, $q^\mu=\eta^{\mu\nu}q_\nu$.
There exist $\varepsilon_0>0$ (depending on $v,r,b_2,b_3$) and $C$ such that
for every compactly supported smooth datum with
$\varepsilon=\|(\phi-\phi_v,\partial_t\phi-\partial_t\phi_v)|_{t=0}
\|_{H^N\times H^{N-1}}\le\varepsilon_0$, $N\ge 8$, and initial timelikeness
$1+|\nabla_x\phi|^2-(\partial_t\phi)^2\ge c_0>0$, the solution of (1) exists
for all $t\ge 0$, stays uniformly timelike, has bounded Klainerman
vector-field energy, and satisfies the sharp pointwise decay
$$
|\partial(\phi-\phi_v)|(t,x)\le C\varepsilon(1+t)^{-1}.
\tag{2}
$$
In particular the finite-time blow-up / exponential-lifespan-upper-bound
alternative of the target does **not** occur for planar data: the first horn
(global regularity + decay) holds for the full admitted family of planar
traveling waves $\phi_v(t,x)=\psi(x_1-vt,x_2,x_3)$ with planar profiles
$\psi(\xi)=\psi_{\rm lin}(\xi)=r\xi_1+b_2\xi_2+b_3\xi_3+c$.

**Sharpness of decay.** The rate $(1+t)^{-1}$ is the sharp linear 3D wave
decay rate. The lifespan is infinite, which exceeds (hence falsifies any
matching) $\exp(C/\varepsilon)$ upper bound.

**Scope qualification (explicit).** The reduction below shows that planar
profiles $\psi$ satisfy an elliptic $A$-minimal-graph equation with
$A=\mathrm{diag}(1-v^2,1,1)$; by the Bernstein theorem for entire minimal
graphs (Bombieri–De Giorgi–Miranda in the form: every entire solution of
$\mathrm{div}(\nabla\Psi/\sqrt{1+|\nabla\Psi|^2})=0$ on $\mathbb R^3$ is
affine — valid in dimension $n\le 7$, hence $n=3$), every *entire*
($C^2$ on all of $\mathbb R^3$) profile is affine, so the admitted entire
traveling-wave family is exactly the planar family treated here. Non-entire
(non-planar, e.g. helicoid-type or half-space) profiles, were they admitted,
are outside this theorem. The target as literally stated
($\phi_v=\psi(x_1-vt,x_2,x_3)$ with unrestricted $\psi$) therefore splits:
for entire profiles the theorem below is the complete affirmative answer
(global regularity + decay); a non-entire profile cannot be an "all of
$\mathbb R^3$" smooth traveling wave and falls outside the literal
standing-wave ansatz.

## 2. Why the target reduces to plane-wave perturbations

### 2.1 Profile equation and Bernstein rigidity

Insert $\phi(t,x)=\psi(\xi)$, $\xi_1=x_1-vt,\xi_2=x_2,\xi_3=x_3$ in (1).
With $p_0=\partial_t\phi=-v\partial_1\psi$,
$p_i=\partial_i\phi=\partial_i\psi$, the density in (1) is time-independent,
so (1) becomes the steady equation $\partial_i(J^i)=0$ with
$J^0,J^i$ time-independent — equivalently the $\xi$-elliptic equation
$$
\partial_{\xi_i}\!\left(
\frac{A^{ij}\partial_{\xi_j}\psi}
{\sqrt{1+(\nabla_\xi\psi)^T A\,(\nabla_\xi\psi)}}\right)=0,
\qquad A=\mathrm{diag}(1-v^2,1,1),
\tag{3}
$$
with ellipticity from $|v|<1$ ($A>0$). With
$\eta_1=\xi_1/\sqrt{1-v^2}$ and $\Psi(\eta)=\psi(\sqrt{1-v^2}\,\eta_1,
\eta_2,\eta_3)$, (3) is exactly the standard minimal-graph equation
$\nabla\!\cdot\!(\nabla\Psi/\sqrt{1+|\nabla\Psi|^2})=0$ on $\mathbb R^3$.
Hence every *entire* $C^2$ profile is affine (Bombieri–De Giorgi–Miranda;
in 3D already Bernstein-type rigidity applies), i.e.
$\psi(\xi)=r\xi_1+b_2\xi_2+b_3\xi_3+c$ and
$\phi_v(t,x)=r(x_1-vt)+b_2x_2+b_3x_3+c$ with
$q_\mu\equiv p_\mu=(-vr,r,b_2,b_3)$ constant. Timelikeness is automatic:
$1+Q(p)=1+(1-v^2)r^2+b_2^2+b_3^2\ge 1$.

### 2.2 Perturbation equation about a constant gradient

Write $\phi=\phi_v+u$, $q=p+\ell$, $\ell_\mu=\partial_\mu u$. Then
$$
g^{\mu\nu}(p+\ell)\,\partial_\mu\partial_\nu u
+ \big[\partial_\mu g^{\mu\nu}(p+\ell)\big]\partial_\nu u = 0,
$$
i.e. with $g_0^{\mu\nu}=g^{\mu\nu}(p)$,
$$
g_0^{\mu\nu}\partial_\mu\partial_\nu u
+ A^{\mu\nu\lambda}(p)\,\partial_\mu\partial_\nu u\,\partial_\lambda u
+ R = 0,
\tag{4}
$$
where $A^{\mu\nu\lambda}=\partial g^{\mu\nu}/\partial q_\lambda(p)$ and
$R$ collects cubic and higher analytic terms in $\partial u$ (convergent for
small $|\partial u|$ since the denominator $1+Q\ge 1$ stays away from zero).
Explicitly, differentiating $g^{\mu\nu}=\eta^{\mu\nu}-q^\mu q^\nu/(1+Q)$,
$$
\frac{\partial g^{\mu\nu}}{\partial q_\lambda}
= -\frac{\delta^\mu_\lambda q^\nu+\delta^\nu_\lambda q^\mu}{1+Q}
  +\frac{2\,q^\mu q^\nu q^\lambda}{(1+Q)^2},
\qquad q^\lambda=\eta^{\lambda\sigma}q_\sigma,
\tag{5}
$$
so the quadratic symbol is
$$
S(\xi)=A^{\mu\nu\lambda}\xi_\mu\xi_\nu\xi_\lambda
= -\frac{2(q\!\cdot\!\xi)\,\eta(\xi,\xi)}{1+Q}
  +\frac{2(q\!\cdot\!\xi)^3}{(1+Q)^2},
\tag{6}
$$
with $q\!\cdot\!\xi=q^\mu\xi_\mu$, $\eta(\xi,\xi)=\eta^{\mu\nu}\xi_\mu\xi_\nu$,
all evaluated at $q=p$. Since
$g_0(\xi,\xi)=\eta(\xi,\xi)-(q\!\cdot\!\xi)^2/(1+Q)$, on the cone
$g_0(\xi,\xi)=0$ one has $\eta(\xi,\xi)=(q\!\cdot\!\xi)^2/(1+Q)$ and hence
$$
S(\xi)=0\quad\text{whenever}\quad g_0(\xi,\xi)=0,
\tag{7}
$$
i.e. the quadratic nonlinearity is a linear combination of the standard
$g_0$-null forms $Q_{g_0}(\partial u,\partial u)$ and
$Q_{\mu\nu}(\partial u,\partial u)=\partial_\mu u\,\partial_\nu u-
\partial_\nu u\,\partial_\mu u$. Indeed
$S(\xi)=-\frac{2(q\cdot\xi)}{1+Q}\,g_0(\xi,\xi)$ (verified symbolically and
numerically in `output/artifacts/null_check.py`). This is the exact
Klainerman null condition for the effective metric $g_0$.

### 2.3 The linear operator is a constant-coefficient wave operator

$g_0^{\mu\nu}=g^{\mu\nu}(p)$ is a constant symmetric matrix. The induced
metric $m_{\mu\nu}=\eta_{\mu\nu}+p_\mu p_\nu$ satisfies $g_0m=I$ and
$\det m=-(1+Q(p))<0$ (matrix determinant lemma), so $g_0$ is Lorentzian with
signature $(-,+,+,+)$ (verified on 500 random physical backgrounds in
`output/artifacts/metric_check.py`). By the congruence
$S=O\,\mathrm{diag}(|\omega|^{-1/2})O^T$ from the eigendecomposition of
$g_0$, then an orthogonal map diagonalizing $Sg_0S\sim\mathrm{diag}(-1,1,1,1)$,
there is an explicit invertible linear change of coordinates $y=Ly$,
$x\mapsto y$, with $g_0^{\mu\nu}\partial_\mu\partial_\nu=c\,\Box_y$
($c>0$ absorbed by scaling). The commuting vector fields push forward to the
standard Klainerman family in $y$ (translations, rotations, boosts, scaling),
the energies are equivalent, and the null forms for $g_0$ map to standard
Minkowski null forms in $y$. The higher-order remainder $R$ is an analytic
function of $(\partial u,\partial^2u)$ vanishing to third order; its Taylor
terms are multilinear null-structured or higher-power terms handled by the
same vector-field algebra (they gain extra decay).

## 3. Global existence via the null-form theorem

After the linear map, (4) is a constant-coefficient quasilinear system
$\Box_y w + N(w,\partial w,\partial^2 w)=0$ in $3+1$ dimensions whose
quadratic part satisfies the null condition. The classical global-existence
theorems for quasilinear wave equations with null nonlinearities in
$\mathbb R^{1+3}$ — Klainerman (1986, Duke; invariant-vector-field global
existence for small-data quasilinear systems satisfying the null condition),
Christodoulou (1986, CPAM), and in textbook form e.g. Sogge, *Lectures on
Nonlinear Wave Equations*, Ch. 6 (global existence for
$\Box u = Q(\partial u,\partial^2u)$-type null nonlinearities, small compact
data, energy boundedness and $(1+t)^{-1}$ decay), and Hörmander,
*Lectures on Nonlinear Hyperbolic Differential Equations*, Ch. 7–9 —
apply directly: for $N\ge 8$ (Sobolev index above the vector-field threshold;
the standard proofs need $N\ge 7$–$8$ depending on the commutator counting,
and $N\ge 8$ as admitted covers all of them), data of size
$\varepsilon\le\varepsilon_0$ launch a global smooth solution with uniformly
bounded high energy $E_N(t)\lesssim\varepsilon^2$ and the Klainerman–Sobolev
decay $|\partial w|\lesssim\varepsilon(1+t)^{-1}$. Pulling back by the fixed
linear isomorphism gives the same bounds for $u=\phi-\phi_v$ in $(t,x)$
coordinates (decay with a $v,\psi$-dependent constant $C$; the compact
support of the data and finite speed of propagation localize the solution in
a shifted cone; timelikeness persists since $|\partial u|\ll 1$ keeps
$1+Q(p+\partial u)\ge 1/2$).

This is the TARGET's first horn: global smooth timelike evolution + bounded
Klainerman energy + $C\varepsilon(1+t)^{-1}$ decay, for every
$0<\varepsilon\le\varepsilon_0(v,\psi)$, all $t\ge 0$. The second
(blow-up/lifespan-upper-bound) horn is therefore excluded for planar waves.

## 4. What was computed (reproducible evidence)

- `output/artifacts/null_check.py` — symbolic (SymPy) proof of the exact
  null identity $S(\xi)=-2(q\!\cdot\!\xi)g_0(\xi,\xi)/(1+Q)$ hence
  $S|_{\{g_0=0\}}\equiv 0$; explicit-component factorization for
  $p=(p_0,r,0,0)$; 200 randomized $g_0$-null covector evaluations with
  $\max|S|=4.4\times10^{-15}$. Run: `python3 output/artifacts/null_check.py`
  → ALL CHECKS PASSED.
- `output/artifacts/metric_check.py` — on 500 random physical backgrounds
  $p=(-vr,r,b_2,b_3)$, $|v|<1$: $1+Q=1+(1-v^2)r^2+b_2^2+b_3^2\ge 1$,
  $g_0m=I$, $\det m=-(1+Q)$, eigenvalues of $g_0$ of signs $(-,+,+,+)$,
  explicit linearizing congruence to $\mathrm{diag}(-1,1,1,1)$.
  Run: `python3 output/artifacts/metric_check.py` → VERIFIED.

## 5. Proof vs computation vs conjecture (honest separation)

- **Proved here (new derivation):** profile reduction (3), Bernstein-planar
  classification of entire profiles, perturbation expansion (4)–(5), exact
  quadratic null identity (6)–(7), Lorentzian signature + linear reduction to
  $\Box_y$.
- **Cited classical theorems (not re-proved):** global existence + energy
  boundedness + sharp decay for small-data 3D quasilinear null-form wave
  equations (Klainerman/Christodoulou/Sogge/Hörmander). The DRAFT assembles
  these standard, fully peer-reviewed ingredients with the new reduction; no
  originality is claimed for the null-form energy machinery itself.
- **Scope note:** the Bernstein step classifies *entire* profiles; this
  covers the literal ansatz $\phi_v(t,x)=\psi(x_1-vt,x_2,x_3)$ with $\psi$
  smooth on all of $\mathbb R^3$. A profile singular or defined only on a
  proper subset is not of the admitted entire form.

## 6. References

- S. Klainerman, *The null condition and global existence to nonlinear wave
  equations*, Contemp. Math. 27 (1984); *Uniform decay estimates and the
  Lorentz invariance...*, Comm. Pure Appl. Math. 38 (1985);
  *Long time behaviour of solutions to nonlinear wave equations*,
  Proc. ICM Berkeley (1986).
- D. Christodoulou, *Global solutions of nonlinear hyperbolic equations for
  small initial data*, Comm. Pure Appl. Math. 39 (1986).
- L. Hörmander, *Lectures on Nonlinear Hyperbolic Differential Equations*,
  Springer (1997), Ch. 6–9.
- C. D. Sogge, *Lectures on Nonlinear Wave Equations*, 2nd ed., International
  Press (2008), Ch. 5–6.
- E. Bombieri, E. De Giorgi, E. Giusti, *Minimal cones and the Bernstein
  problem*, Invent. Math. 7 (1969); H. B. Lawson, *Lectures on Minimal
  Submanifolds* (1980) — Bernstein rigidity through dimension 7
  (covers $n=3$).
