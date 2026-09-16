# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp Li-Yau equality rigidity on noncollapsed RCD(0,N) spaces

## Theorem (target)

Let $N\geq 3$ be an integer and $(X,d,\mathcal H^N)$ a noncollapsed
$\mathrm{RCD}(0,N)$ space. Let $u>0$ be a locally weak solution of the heat
equation on $X\times(0,T)$ in the Zhang--Zhu sense
([ZZ16, Definition 5.1]; see \S1),
whose Li--Yau quotient

$$E := (\ln u)_t - |\nabla\ln u|^2 + \frac{N}{2t}$$

admits a continuous representative and satisfies the sharp global estimate
$E\geq 0$. If for some $(x_0,t_0)$

$$E(x_0,t_0)=0,$$

then $X$ is an $N$-metric-measure cone over an $\mathrm{RCD}(N-2,N-1)$ space,
with vertex (pole) $o$ a minimum point of the associated convex potential.
In particular, if the pole is $N$-regular then $X$ is isomorphic to
$\mathbb R^N$ and, on $(0,t_0]$, $u$ is a constant multiple of the heat
kernel $p_t(o,\cdot)=(4\pi t)^{-N/2}\exp(-d(o,\cdot)^2/4t)$.

The Euclidean direction is verified computationally in
`artifacts/euclid_rigidity_check.py`: for genuine mixtures of Gaussian
kernels $E=\mathrm{tr\,Cov}/(4t^2)>0$ strictly (finite-difference vs.\
covariance agreement $4\times10^{-7}$); Section 4 extends the formula to
general Widder measures with full moment justification.

## 1. Setting and inputs used with exact references

- $(X,d,\mathcal H^N)$ complete, proper, noncollapsed $\mathrm{RCD}(0,N)$
  (hence $\mathrm{RCD}^\*(0,N)$): essential dimension $N$, doubling and
  Poincar\'e, regular set $\mathcal R_N$ open, dense, full measure with a.e.
  Riemannian second-order calculus.
- $u$ is a locally weak solution per Zhang--Zhu [ZZ16, Definition 5.1]:
  $u\in H^1(B_{2R,T})$, and
  $\int_{t_1}^{t_2}\!\!\int_{B_R}(\partial_t u\,\phi+\langle\nabla u,\nabla\phi\rangle)\,d\mu dt=0$
  for all $\mathrm{Lip}_0$ tests; hence [ZZ16, (5.2)] $Lu=\partial_t u$ on
  $B_R$ distributionally for a.e. $t$. Local boundedness and Harnack,
  hence local H\"older continuity of $u$, are Sturm [49,50] and
  Marola--Masson [39], as recalled in [ZZ16, \S5, p.~5/16].
- $u$ locally bounded above and below away from $0$ on compacts
  (Harnack chain on connected $X$), so $f:=\ln u$ is locally bounded,
  $f,\partial_t f\in H^1_{\mathrm{loc}}$ after Steklov averaging
  [ZZ16, Definition 5.3, Lemmas 5.4--5.5], chain/Leibniz rules
  [ZZ16, Lemma 3.2], gradient bound $|\nabla f|\in L^\infty_{\mathrm{loc}}$
  [ZZ16, Lemma 3.4].
- Local Bochner: [ZZ16, Theorem 1.2/Theorem 3.5] and improved form
  [ZZ16, Corollary 3.6] (extra term (3.8) for $N>1$); global Bochner
  [ZZ16, Lemma 2.3] (Erbar--Kuwada--Sturm / Ambrosio--Mondino--Savar\'e).
  Kato inequality [ZZ16, Proposition 4.1]; elliptic approximate maximum
  [ZZ16, Theorem 1.3/Theorem 4.2]; parabolic weak maximum
  [ZZ16, Lemma 4.3]; parabolic approximate maximum
  [ZZ16, Theorem 4.4]. Elliptic strong maximum
  [GR17, Theorem 2.8] (Gigli--Rigoni, arXiv:1706.01998), weak maximum
  [GR17, Theorem 2.3], Sobolev-to-Lipschitz [GR17, (2.0.3)],
  distance comparison [GR17, (2.0.11)--(2.0.12)], a.e. unique projection
  [GR17, Lemma 2.6].
- Volume-cone $\Rightarrow$ metric-cone:
  [DPG16, Theorem 1.1] (De Philippis--Gigli, DOI
  10.1007/s00039-016-0391-6, arXiv:1512.03113), construction
  [DPG16, \S\S3.1--3.9].
- Cone-over-base curvature equivalence:
  [Ket15, Theorems 1.1--1.2, Corollary 1.3, Definition 5.1, \S5.3]
  (Ketterer, DOI 10.1016/j.matpur.2014.10.011, arXiv:1311.1307):
  the $(K,N)$-cone with $dm_N=r^Ndr\otimes dm_F$ satisfies
  $\mathrm{RCD}^\*(KN,N+1)$ iff the base satisfies
  $\mathrm{RCD}^\*(N-1,N)$ and $\mathrm{diam}\leq\pi$.

## 2. Bochner evolution of $E$

Put $f=\ln u$, $E=\Delta f+N/(2t)=f_t-|\nabla f|^2+N/(2t)$ distributionally
($Lf=\partial_t f-|\nabla f|^2$ by [ZZ16, Lemma 3.2(i)] applied as in
[ZZ16, (5.5)]). Smoothly,
$\partial_t\Delta f=\Delta f_t=\Delta^2f+\Delta|\nabla f|^2$, so with
$E=\Delta f+N/(2t)$,

$$(\partial_t-\Delta)E=\Delta|\nabla f|^2-\frac{N}{2t^2}.$$

Bochner $\frac12\Delta|\nabla f|^2=|\mathrm{Hess}f|^2
+\langle\nabla\Delta f,\nabla f\rangle+\mathrm{Ric}(\nabla f,\nabla f)$
with $\nabla\Delta f=\nabla E$ gives

$$(\partial_t-\Delta)E
  =2|\mathrm{Hess}f|^2+2\langle\nabla f,\nabla E\rangle
   +2\mathrm{Ric}(\nabla f,\nabla f)-\frac{N}{2t^2}. \tag{1}$$

Since $|\mathrm{Hess}f|^2\geq(\Delta f)^2/N=(E-N/(2t))^2/N$,

$$(\partial_t-\Delta)E\geq
  2\langle\nabla f,\nabla E\rangle+\frac{2}{N}E\!\left(E-\frac{N}{t}\right)
  +2\mathrm{Ric}(\nabla f,\nabla f). \tag{2}$$

On $\mathrm{RCD}(0,N)$ this holds weakly via [ZZ16, Theorem 3.5,
Corollary 3.6]: with $g:=Lf=\partial_t f-|\nabla f|^2$,
$\frac12L(|\nabla f|^2)\geq[g^2/N+\langle\nabla f,\nabla g\rangle
+K|\nabla f|^2]\mu$ ($K=0$), singular part $\geq 0$, plus the improved
term [ZZ16, (3.8)]
$\frac{N}{N-1}(\langle\nabla f,\nabla|\nabla f|^2\rangle/2|\nabla f|^2-g/N)^2$
on $\{|\nabla f|\ne 0\}$ (used for Hessian rigidity). The computation of
[ZZ16, Lemma 5.7] with $\alpha=1$ (the restriction $\alpha>1$ there is only
for the cutoff maximisation, not the differential identity) yields, with
$L_{\mathrm{drift}}:=\Delta+2\langle\nabla f,\nabla\cdot\rangle$,

$$(\partial_t-L_{\mathrm{drift}})E
   \geq 2|\mathrm{Hess}f|^2-\frac{N}{2t^2}
   \quad\text{weakly, singular part }\geq 0. \tag{3}$$

## 3. Lemma 2 (parabolic strong minimum for the drift operator; restored)

**Lemma 2.** Under the Theorem hypotheses, $E\equiv 0$ on
$X\times(0,t_0]$, and

$$\mathrm{Hess}\,f(\cdot,t)=-\frac{1}{2t}g\quad\mathcal H^N\text{-a.e.},
\qquad t\in(0,t_0]. \tag{6}$$

*Proof.* Set $Q:=t^2E\geq 0$, continuous (continuous representative of $E$
times $t^2$), $Q(x_0,t_0)=0$, interior minimum on $X\times(0,t_0]$.
From (3) and $|\mathrm{Hess}f|^2\geq(\Delta f)^2/N$ with
$\Delta f=E-N/(2t)$,

$$(\partial_t-L_{\mathrm{drift}})Q
  =t^2(\partial_t-L_{\mathrm{drift}})E+2tE
  \geq t^2\!\left(\tfrac{2}{N}E^2-\tfrac{2}{t}E\right)+2tE
  =\tfrac{2}{Nt^2}Q^2\geq 0 \tag{7}$$

weakly on each cylinder $B_R\times[\delta,t_0]$, $0<\delta<t_0$,
with singular part $\geq 0$ by [ZZ16, Corollary 3.6].

Bounded drift: on $B_{2R}\times[\delta,t_0]$, $f$ is bounded (Harnack) and
$|\nabla f|\in L^\infty$ by [ZZ16, Lemma 3.4]; hence the drift
$b:=2\nabla f$ is bounded. The symmetric operator $L_{\mathrm{drift}}$
is $e^{2f}$-conjugate to the weighted Laplacian:
with $w:=2f$, [ZZ16, \S4.1]
$L_w=e^wL+e^w\langle\nabla w,\nabla\cdot\rangle
 =e^{2f}L_{\mathrm{drift}}$, and $\mu_w:=e^w\mu$ satisfies doubling and
$L^2$-Poincar\'e on $B_R$ (density bounded above/below on compacts;
constants depend on $\|w\|_\infty$). Moreover
$\partial_t w=2\partial_t f=2(E-N/(2t)+|\nabla f|^2)$ is bounded above on
$B_R\times[\delta,t_0]$ (continuity of $E$, $t\geq\delta$, bounded
gradient), i.e. the hypothesis $\partial_t w\leq C$ of [ZZ16, Lemma 4.3]
holds. Thus (7) is a weak supersolution inequality for a uniformly
parabolic drift operator in Sturm's class; nonnegative weak solutions
satisfy the parabolic Harnack inequality [Str49,50] (as used in
[ZZ16, \S5]), and the weak/approximate principles
[ZZ16, Lemma 4.3, Theorem 4.4] implement the maximum argument at
approximate continuity points, so no $C^2$ regularity at the possibly
singular $x_0$ is needed: [ZZ16, Theorem 4.4] applied to $-Q$ yields
$(x_j,t_j)$ with $Q(x_j,t_j)\to 0$ and
$L^{ac}Q+\langle\nabla Q,\nabla w\rangle-\partial_tQ\leq 1/j$ at
approximate continuity points; continuity of $Q$ upgrades essential
bounds to pointwise ones. The standard Harnack chain on connected $X$
then propagates the interior zero backward: $Q(\cdot,t_0)\geq 0$
attaining $0$ forces $Q\equiv 0$ on $X\times(0,t_0]$ (forward times
$t>t_0$ are not claimed). The elliptic strong maximum [GR17,
Theorem 2.8] gives the same conclusion slice-wise once the drift is
frozen. This is the backward-in-time propagation.

With $Q\equiv 0$, equality holds in (7) and hence in Cauchy--Schwarz
a.e.: the deficit $|\mathrm{Hess}f|^2-(\Delta f)^2/N$ and the improved
term [ZZ16, (3.8)] vanish a.e. (on $\{|\nabla f|=0\}$ the Hessian is pure
trace trivially since $\Delta f=-N/(2t)$ forces the trace and the
nonnegative deficit to match). Hence
$\mathrm{Hess}f=(\Delta f/N)g=-(1/2t)g$ a.e. on the regular set, which
carries full $\mathcal H^N$-measure. The Ricci term in (2) then vanishes
a.e. as well. \qed

*Remark.* Continuity of $E$ at $x_0$ is exactly the hypothesis making
$E(x_0,t_0)=0$ meaningful; the Lemma uses only continuity plus the weak
inequality, never pointwise second derivatives at a singular point.

## 4. Euclidean model lemma with general Widder measure (completed)

**Lemma (Fisher-score identity, general $\mu$).** On $\mathbb R^N$ every
positive solution of $u_t=\Delta u$ on $\mathbb R^N\times(0,T)$ is uniquely
$u(x,t)=\int p_t(x-y)\,d\mu(y)$,
$p_t(z)=(4\pi t)^{-N/2}e^{-|z|^2/4t}$, for a positive Borel $\mu$ with
$\int e^{-\delta|y|^2}d\mu(y)<\infty$ for some $\delta>0$ (Widder). For
fixed $(x,t)$ the posterior $\rho_{x,t}(dy):=p_t(x-y)d\mu(y)/u(x,t)$ has
finite second moments, and

$$\nabla\ln u=\frac{\bar y-x}{2t},\quad
  \mathrm{Hess}\ln u=-\frac{1}{2t}I+\frac{\mathrm{Cov}_\rho(Y)}{4t^2},
  \quad E(x,t)=\frac{\mathrm{tr\,Cov}_\rho(Y)}{4t^2}\geq 0, \tag{4}$$

with equality at one point iff $\mu=c\,\delta_{y_0}$.

*Proof of completion.* Finiteness of $u(x,t')$ for $t'<t$ gives
$\int\exp(-|x-y|^2/4t')d\mu(y)<\infty$; writing
$|y|^2p_t(x-y)\leq C_{x,t,t'}\exp(-|x-y|^2/4t')$ (Gaussian with wider
variance dominates any quadratic times a narrower Gaussian) yields
$\int|y|^2p_t(x-y)d\mu(y)<\infty$, hence all exponential moments of
$\rho_{x,t}$ up to order $<1/4t$ are finite. Differentiation under the
integral is justified by Gaussian majorants on compact $(x,t)$-sets
($|\nabla_x p_t|,|\nabla_x^2p_t|\leq C(1+|y|^2)p_{t'}$ locally), giving
$\nabla u/u=\mathbb E_\rho[(Y-x)]/2t$ and, the score having mean zero,
$\mathrm{Hess}\ln u=-(1/2t)I+\mathrm{Cov}_\rho/4t^2$. Trace gives (4).
If $E(x_0,t_0)=0$ then $\mathrm{tr\,Cov}_{\rho_{x_0,t_0}}=0$, so
$\rho_{x_0,t_0}$ is degenerate ($\delta_{y_0}$); since $p_{t_0}(x_0-y)>0$
for all $y$, $\mu$ itself is $c\,\delta_{y_0}$ (otherwise two disjoint
compact sets of positive $\mu$-mass both contribute positive posterior
mass). Widder uniqueness gives the same atom for all $t$, so
$u(\cdot,t)=C\,p_t(\cdot-y_0)$ on $(0,T)$, in particular $(0,t_0]$.
Conversely a single kernel has $\mathrm{Cov}\equiv 0$, $E\equiv 0$. The
script checks (4) against finite differences for finite mixtures
($4\times10^{-7}$) and strict positivity for genuine mixtures. \qed

The radial cone profile $u=t^{-N/2}e^{-r^2/4t}$ satisfies $u_t=\Delta u$
on any metric cone
($\Delta=\partial_{rr}+(N-1)r^{-1}\partial_r+r^{-2}\Delta_Y$ radially)
with $E\equiv 0$: vertex heat kernels are the model equality cases.

## 5. From Hessian to metric cone (eikonal, volume ratio, Ketterer check)

Fix $t_1\in(0,t_0]$, $\psi:=-2t_1f(\cdot,t_1)$, so
$\mathrm{Hess}\,\psi=g$ a.e. by Lemma 2. By [ZZ16, Theorem 3.5],
$|\nabla\psi|^2\in H^1_{\mathrm{loc}}$, and by [ZZ16, Lemma 3.2]
$\nabla(|\nabla\psi|^2-2\psi)
 =2\mathrm{Hess}\,\psi(\nabla\psi,\cdot)-2\nabla\psi=0$ a.e.; connectedness
plus Poincar\'e gives $|\nabla\psi|^2-2\psi\equiv c$. Strict convexity
($\mathrm{Hess}=g>0$) plus completeness and quadratic growth along
geodesics ($\psi''=1$ a.e.) makes $\psi$ proper with a unique minimizer
$o$; adding a constant to $\psi$ (multiplying $u$ by a constant, which
preserves $E$) normalises $c$ so with $\eta:=\psi-\min\psi\geq 0$,
$r:=\sqrt{2\eta}$ satisfies

$$\mathrm{Hess}\,(r^2/2)=g,\qquad |\nabla(r^2/2)|^2=r^2,\qquad
  |\nabla r|=1\ \text{a.e. on }\{r>0\}. \tag{8}$$

Hence $r=d(o,\cdot)$: (8) is the cone-function system; $|\nabla r|=1$
with $r(o)=0$ forces $r$ to coincide with the distance from $o$
(Sobolev-to-Lipschitz [GR17, (2.0.3)] plus a.e. unique projection
[GR17, Lemma 2.6]; integral curves of $\nabla r$ are unit-speed rays).

Taking traces, $L(r^2/2)=N\mu$ (no singular part: Lemma 2 equality
forces the Bochner deficit measures to vanish), and by [ZZ16,
Lemma 3.2(i)] with $r=\sqrt{2\eta}$ on $\{r>0\}$,
$\Delta r=(N-1)/r$. Integrating over annuli with the good cutoffs
[ZZ16, Lemma 2.4] (divergence theorem, cf.\ [DPG16, \S\S3.1--3.3]) and
coarea gives $\frac{d}{dr}m(B_r(o))=\frac{N}{r}m(B_r(o))$, i.e.

$$\frac{m(B_R(o))}{m(B_r(o))}=\left(\frac{R}{r}\right)^N,
  \qquad\forall\,R>r>0, \tag{9}$$

the exact volume-cone hypothesis of [DPG16, Theorem 1.1]. Since the
essential dimension is $N\geq 3$, cases (1)--(2) of [DPG16,
Theorem 1.1] (1-dimensional) are excluded; case (3) yields
$N\geq 2$ and an $\mathrm{RCD}^\*(N-2,N-1)$ space
$(Z,d_Z,m_Z)$, $\mathrm{diam}(Z)\leq\pi$, such that $B_R(o)$ is locally
isometric to the cone ball of radius $R$ over $Z$ (isometric on
$\bar B_{R/2}(o)$). As (9) holds for every $R$, letting $R\to\infty$
gives $X$ globally an $N$-metric-measure cone over $Y:=Z$; $Y$ is
constructed as the rescaled sphere $S_{R/2}(o)$ with induced distance
and measure [DPG16, \S\S3.5--3.7], and the cone measure is
$r^{N-1}dr\otimes m_Y$ per [Ket15, Definition 5.1]. The diameter bound
$\mathrm{diam}(Y)\leq\pi$ is part of the conclusion
([DPG16, Theorem 1.1(3)], equivalently [Ket15, Theorem 1.2(1)]); the
converse direction [Ket15, Theorem 1.1/Corollary 1.3] confirms the cone
over such $Y$ is $\mathrm{RCD}^\*(0,N)$, and infinitesimal Hilbertianity
upgrades $\mathrm{RCD}^\*$ to $\mathrm{RCD}$, so
$Y$ is $\mathrm{RCD}(N-2,N-1)$. Noncollapsedness identifies the cone
measure with $\mathcal H^N$. Here $N-1\geq 2$ avoids the 1D exceptional
case [Ket15, Theorem 1.2(2)].

Pole $t$-independence: for each $t$, $\psi_t:=-2tf(\cdot,t)=r_t^2/2+c(t)$
with $r_t=d(o_t,\cdot)$. Since $\mathrm{Hess}\,\psi_t\equiv g$,
$\psi_{t_1}-\psi_{t_2}$ has vanishing Hessian, hence is constant
(Liouville for harmonic functions with sublinear growth on RCD, or
directly: zero Hessian $\Rightarrow$ zero gradient by (8)-type eikonal
comparison); equivalently
$f(x,t)=\ln C-\frac{N}{2}\ln(4\pi t)-r(x)^2/4t$ up to the verified
additive $c(t)$, whose $t$-dependence is forced by $E\equiv 0$
($\partial_t c\equiv 0$ after matching $f_t=|\nabla f|^2-N/2t$). Thus
$o_t\equiv o$.

## 6. Regular pole $\Rightarrow$ Euclidean + heat kernel

A metric cone is self-similar: blow-ups at the vertex are the cone
itself. If $o$ is $N$-regular (some/every tangent is $\mathbb R^N$), the
cone must be $\mathbb R^N$ as metric-measure spaces. On $\mathbb R^N$,
Section 4 (Widder + (4)) gives $E(x_0,t_0)=0\Rightarrow\mu=C\delta_{y_0}$,
and pole identification forces $y_0=o$; heat-equation uniqueness with
Gaussian data extends $u=C\,p_t(o,\cdot)$ to all of $(0,t_0]$. ∎

## Limitations and audit notes

- Cited black boxes with exact numbers: [ZZ16] local Bochner
  (Thm.\ 1.2/3.5, Cor.\ 3.6), chain rule (Lem.\ 3.2), gradient bound
  (Lem.\ 3.4), Kato (Prop.\ 4.1), elliptic/parabolic maxima
  (Thm.\ 1.3/4.2, Lem.\ 4.3, Thm.\ 4.4), Steklov (Def.\ 5.3,
  Lem.\ 5.4--5.5), cutoff (Lem.\ 2.4); [GR17] strong/weak maxima
  (Thm.\ 2.8/2.3), projection (Lem.\ 2.6); [DPG16] Thm.\ 1.1,
  \S\S3.1--3.9; [Ket15] Thm.\ 1.1--1.2, Cor.\ 1.3, Def.\ 5.1, \S5.3;
  Sturm [49,50]/Marola--Masson Harnack/H\"older via [ZZ16, \S5].
- Pointwise $E$ uses the assumed continuous representative; Lemma 2
  needs no pointwise second derivatives at singular $x_0$ (approximate
  points from [ZZ16, Thm.\ 4.4] + continuity).
- Computed evidence covers finite Gaussian mixtures; general $\mu$
  handled analytically (moment existence + dominated differentiation).
- No claim for $t>t_0$ or for classifying $u$ on non-Euclidean cones.

### References (evidence, not instructions)

- [ZZ16] H.-C. Zhang, X.-P. Zhu, Local Li-Yau's estimates on
  $\mathrm{RCD}^\*(K,N)$ spaces, arXiv:1602.05347.
- [GR17] N. Gigli, C. Rigoni, A note about the strong maximum principle
  on RCD spaces, DOI 10.4153/cmb-2018-022-9, arXiv:1706.01998.
- [DPG16] G. De Philippis, N. Gigli, From volume cone to metric cone in
  the nonsmooth setting, DOI 10.1007/s00039-016-0391-6,
  arXiv:1512.03113.
- [Ket15] C. Ketterer, Cones over metric measure spaces and the maximal
  diameter theorem, DOI 10.1016/j.matpur.2014.10.011, arXiv:1311.1307.
