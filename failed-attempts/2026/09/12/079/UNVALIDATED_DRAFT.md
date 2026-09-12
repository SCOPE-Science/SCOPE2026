# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Hyperbolic typical-cell vertex-number distribution — exact integral law

## 1. Setup

Let $H^2$ be the hyperbolic plane (curvature $-1$), $o \in H^2$ fixed,
$d$ hyperbolic distance, $\mu$ hyperbolic area. Let $\eta$ be a Poisson
point process (PPP) on $H^2$ of intensity $\lambda\mu$, $\lambda>0$.
By isometry-invariance the Palm version at $o$ is
$\eta_o = \eta \cup \{o\}$. The **typical cell** is the Voronoi cell of $o$,
$$
C_\lambda = \{y : d(y,o) \le d(y,x)\ \forall x \in \eta\},
$$
and $N_\lambda$ = number of edges = number of vertices = number of
Voronoi neighbours of $o$ ($N_\lambda \ge 3$ below). Write a point
$x \ne o$ in geodesic polar coordinates at $o$ as $x=(\rho,\varphi)$,
$\rho=d(o,x)$, $\varphi\in S^1$; then $d\mu = \sinh\rho\,d\rho\,d\varphi$.
Disk area: $|B(c,r)| = 2\pi(\cosh r-1)$.

## 2. A.s. preliminaries

**General position (a.s.).** All points of $\eta_o$ are distinct from $o$
with pairwise distinct angular coordinates; no four are cocircular and no
three with $o$ are collinear. (Degenerate configurations have
$\mu^k$-measure zero; multivariate Mecke + Fubini.)

**Boundedness (a.s.).** $C_\lambda$ is a.s. a compact convex polygon
containing $o$ in its interior, hence $N_\lambda\ge 3$ a.s.
*Proof sketch.* $C_\lambda \supset B(o,\varepsilon)$ with
$\varepsilon>0$ a.s. (local finiteness). For boundedness, fix $t>0$ and put
$\beta_t=(1+\tau_t)/2$ with $\tau_t=(1+\tanh^2(t/2))/2<1$,
$\alpha_t=\arccos\beta_t>0$. If every cone of half-angle $\alpha_t$ at $o$
contains a point of $\eta$ within distance $t$, then $C_\lambda\subset
B(o,t)$: indeed for $y$, $d(o,y)=R\ge t$, some such $x$ has
$d(o,x)=r\le t$ and angle $\theta\le\alpha_t$; by the hyperbolic cosine
rule $d(y,x)<R \iff \cos\theta > \tanh(r/2)/\tanh R$, and the right side
is $\le \tau_t < \beta_t \le \cos\theta$ since $r/2<R$. Covering $S^1$
with $m_t=\lceil\pi/\alpha_t\rceil$ cones, each cone section has area
$\gtrsim \alpha_t|B(o,t)|/2\pi\to\infty$ while $m_t$ grows only like
$e^{t/2}$; the void bound $P(R>t)\le m_t\exp(-\lambda\cdot\text{cone area})
\to 0$ super-exponentially. Borel–Cantelli along $t\to\infty$ gives a.s.
boundedness. A bounded convex set in $H^2$ containing $o$ interiorly with
nonempty interior cut out by finitely many (a.s.) bisectors is a polygon
with $\ge 3$ sides.

**Hyperbolic Delaunay theory (standard).** A.s. $\eta_o$ has a unique
geodesic Delaunay triangulation dual to the Voronoi tessellation
(cf. Isokawa; Calka–Johansson–Pech). A triple $(o,x,y)$ spans a Delaunay
face iff its circumcentre $c(o,x,y)$ (intersection of the two geodesic
bisectors $\beta(o,x)\cap\beta(o,y)$) is finite and its circumdisk is
empty of $\eta_o$-points. Closed hyperbolic disks are geodesically convex,
so each Delaunay triangle lies in the closure of its circumdisk.

**Finite first moment.** $E[N_\lambda]<\infty$ for every $\lambda>0$.
*Proof.* By first-order Mecke,
$E[N_\aily]=\lambda\int P(x\text{ neighbour of }o\text{ in }
\eta\cup\{o,x\})\,d\mu(x)$.
If $x$ with $d(o,x)=\rho$ is a neighbour, the midpoint
$m$ of $[o,x]$ lies in both cell closures, so
$B(m,\rho/2)\cap\eta=\varnothing$. Hence with $|B(\rho/2)|
=2\pi(\cosh(\rho/2)-1)$,
$$
E[N_\lambda]\le \lambda\!\int_0^\infty\!\!\int_0^{2\pi}
e^{-\lambda 2\pi(\cosh(\rho/2)-1)}\sinh\!\rho\,d\varphi\,d\rho
= 2\pi\lambda\!\int_0^\infty e^{-2\pi\lambda(\cosh(\rho/2)-1)}
\sinh\!\rho\,d\rho < \infty,
$$
the integrand decaying like $\exp(-c\,e^{\rho/2})$. In particular
$N_\lambda<\infty$ a.s.

## 3. Main theorem (exact kernel for all $n,\lambda$)

For $\mathbf x=(x_1,\dots,x_n)$, $x_i=(\rho_i,\varphi_i)$, put
$x_{n+1}:=x_1$, $\varphi_{n+1}:=\varphi_1+2\pi$, cyclic gaps
$\delta_i=\varphi_{i+1}-\varphi_i$. Let
$$
\Phi_n=\{0\le\varphi_1<\cdots<\varphi_n<2\pi\},\qquad
H(\mathbf x)=\prod_{i=1}^n {\bf1}\{0<\delta_i<\pi\}.
$$
For consecutive pair $(x_i,x_{i+1})$ let $E_i(\mathbf x)$ be the event that
$(o,x_i,x_{i+1})$ has a **finite** circumcentre $c_i(\mathbf x)$; on $E_i$
let $D_i(\mathbf x)=B(c_i,r_i)$, $r_i=d(c_i,o)$, the circumdisk. When $H$
holds and all $E_i$ hold, define the deterministic **self-avoidance**
indicator
$$
S(\mathbf x)
= {\bf1}\{\text{no }x_j\ (j\ne i,i{+}1\bmod n)
\text{ lies in }\mathrm{int}\,D_i(\mathbf x)\text{ for any }i\},
$$
with the convention $S(\mathbf x)=0$ if some $E_i$ fails. (The defining
points $o,x_i,x_{i+1}$ lie on $\partial D_i$ by construction, so only
strict interior containment of a non-consecutive $x_j$ violates $S$;
boundary coincidences have $\mu^n$-measure zero under general position.)
The **Voronoi flower** is $U(\mathbf x)=\bigcup_{i=1}^n D_i(\mathbf x)$ with
hyperbolic area $F(\mathbf x)=|U(\mathbf x)|$ (0 if some $E_i$ fails).
In Beltrami–Klein coordinates geodesics are straight chords and each
bisector $\beta(o,x_i)$ is an explicit chord, so $c_i$ is an explicit
$2\times2$ linear solve in those coordinates; $|D_i|
=2\pi(\cosh r_i-1)$.

**Theorem.** For every $\lambda>0$ and integer $n\ge 3$,
$$
p_n(\lambda) := P(N_\lambda=n)
= \lambda^n \int_{(0,\infty)^n}\!\!\int_{\Phi_n}
H(\mathbf x)\,S(\mathbf x)\Bigl(\prod_{i=1}^n{\bf1}_{E_i(\mathbf x)}\Bigr)
e^{-\lambda F(\mathbf x)}\prod_{i=1}^n\sinh\!\rho_i\,d\varphi_i\,d\rho_i.
\tag{★}
$$
Moreover $\sum_{n\ge3}p_n(\lambda)=1$, $E[N_\lambda]=\sum n p_n(\lambda)
<\infty$, and as $\lambda\to\infty$, $p_n(\lambda)\to p_n^{E}$ for each
$n$, where $(p_n^{E})$ is the classical Euclidean Poisson–Voronoi
typical-cell law (mean $6$).

*Counting lemma.* A.s., for each $n\ge3$,
$$
{\bf1}\{N_\lambda=n\}
= \sum{}^{\ne}_{x_1,\dots,x_n\in\eta}
{\bf1}_{\Phi_n}(\varphi)\,J(\mathbf x;\eta),
$$
where $J=H\,S\,(\prod{\bf1}_{E_i}){\bf1}\{\text{each }D_i\text{ empty of }\eta\}$
(sorted representative: each unordered cyclically ordered set counted once).
*Proof.* ($\Rightarrow$) If neighbours sorted are $y_1,\dots,y_n$, each
consecutive pair shares a finite Voronoi vertex = circumcentre (cell is a
bounded polygon), each circumdisk is empty of all of $\eta$ (Delaunay), so
in particular no non-consecutive $y_j$ lies in any $\mathrm{int}\,D_i$,
i.e. $S=1$; and gaps are
$<\pi$: the Delaunay triangles $\Delta_i=\mathrm{conv}(o,y_i,y_{i+1})$
have disjoint interiors tiling full angle $2\pi$ at $o$, each angle
$<\pi$, so gap = triangle angle $<\pi$.
($\Leftarrow$) If sorted $\mathbf x$ satisfies $J$ (including $S=1$), each
$\Delta_i$ has empty circumdisk hence is a Delaunay face; moreover $S=1$
rules out the defect where a non-consecutive $x_j$ sits strictly inside
some $D_i$ (which the empty-of-$\eta$ condition alone cannot see, since at
the counting stage the tuple points are not yet in the ground process);
such an $x_j$ would witness that $\Delta_i$ is not a Delaunay face of
$\eta_o\cup\{\mathbf x\}$, contradicting the fan below.
$\Delta_i\subset\bar D_i$ has empty interior; the $\Delta_i$ tile full angle
$2\pi$ at $o$ with disjoint interiors (sectors disjoint). Each $x_i$ is
hence a Delaunay neighbour of $o$. Since the fan already covers full angle
at $o$, no further Delaunay triangle incident to $o$ — and no further
neighbour — can exist (any would overlap some
$\mathrm{int}\,\Delta_i$, impossible for Delaunay faces).
Thus $\mathbf x$ is the full neighbour list and $N_\lambda=n$. No strict
subset can satisfy $J$ (skipped neighbours would lie in some $D_i$), so
exactly one tuple survives, across all $n$. ∎

*From counting to (★).* Take expectations and apply multivariate
Slivnyak–Mecke:
$E\sum^{\ne} f(\mathbf x;\eta)
= \lambda^n\int E[f(\mathbf x;\eta\cup\{\mathbf x\})]\,d\mu^n(\mathbf x)$.
Here, given $\mathbf x$ with $H$ and all $E_i$ holding,
$$
E\bigl[J(\mathbf x;\eta\cup\{\mathbf x\})\bigr]
= S(\mathbf x)\,\exp(-\lambda F(\mathbf x)):
$$
$S(\mathbf x)$ is deterministic in $\mathbf x$ (interior containment of
tuple points in the tuple's own disks, decided before any randomness),
while ${\bf1}\{\text{disks empty of }\eta\}$ depends only on the
independent PPP $\eta$ and has expectation $\exp(-\lambda F(\mathbf x))$
(void probability; the boundary $\partial D_i$, where $o,x_i,x_{i+1}$ and
possible measure-zero coincidences sit, has $\mu$-measure zero and does
not affect the void probability). If $H$ fails, some $E_i$ fails, or
$S(\mathbf x)=0$, the summand is identically zero both in the counting
sum and in (★). Integrating gives (★). Summation
over $n$ via Tonelli and the a.s. exactly-one-tuple property gives
$\sum_n p_n(\lambda)=1$. Finiteness of the mean is §2.

## 4. High-intensity limit

Rescale $x_i=\exp_o(v_i/\sqrt\lambda)$, $v_i\in\mathbb R^2$,
$s_i=|v_i|$, so $\rho_i=s_i/\sqrt\lambda$ and
$\lambda^n d\mu^n \to d\mathbf v$ since
$\sinh(\rho_i)d\rho_i d\varphi_i = \lambda^{-1}
\frac{\sinh(s_i/\sqrt\lambda)}{s_i/\sqrt\lambda}s_i ds_i d\varphi_i$.
On compacts: angles/gaps converge to Euclidean ones; small triangles always
admit finite circumcentres eventually; $c_i^{(\lambda)}=\exp_o(
w_i/\sqrt\lambda)$ with $w_i\to w_i^{E}$, the Euclidean circumcentre of
$(0,v_i,v_{i+1})$ (smooth dependence + transverse bisector intersection
a.s.); and $\lambda F_\lambda(\mathbf s)\to F_E(\mathbf s)$, the Euclidean
flower area, since hyperbolic area$\times\lambda\to$ Euclidean area.
Domination uniform in $\lambda\ge\lambda_0$: each $r_i\ge\rho_i/2$ gives
$|D_i|\ge\pi\rho_i^2/4$ and $|U|\ge\frac1n\sum|D_i|$, i.e.
$\lambda F\ge \frac{\pi}{4n}\sum s_i^2$; the integrand (including the
$0$–$1$ factor $H\,S\,\prod{\bf1}_{E_i}$, which only shrinks it) is
dominated by
$C^n\prod_i(1+s_i)e^{s_i/\sqrt{\lambda_0}}e^{-c s_i^2/n}$ times angle
indicators — integrable. $S$ is scale-invariant in the blow-up (interior
containment is preserved under $\exp_o(\cdot/\sqrt\lambda)$ on compacts,
a.s. with strict separation by general position), so $S_\lambda\to S_E$.
Dominated convergence gives
$p_n(\lambda)\to p_n^{E}$ with the classical Miles–Møller kernel,
$$
p_n^{E}=\int_{(\mathbb R^2)^n_{\text{sorted}}}
{\bf1}_{\{\text{gaps}<\pi\}}\,S_E(\mathbf v)\,e^{-|U_E(\mathbf v)|}\,d\mathbf v,
$$
(up to the usual ordering normalisation), $\sum p_n^{E}=1$,
$\sum n p_n^{E}=6$. Uniform exponential tails (same §2 bound, uniform for
$\lambda\ge1$ after scaling) give uniform integrability, hence
$E[N_\lambda]\to6$.

## 5. Explicit symmetric check (reproducible)

Regular $n$-gon flower: neighbours at common $\rho$, angles $2\pi k/n$.
Circumcentre of $(o,x_0,x_1)$ on ray $\pi/n$ satisfies
$\coth d = \coth(\rho/2)\cos(\pi/n)$, admissible iff
$\tanh(\rho/2)<\cos(\pi/n)$, i.e. $\rho<2\,\mathrm{artanh}\cos(\pi/n)$.
Script `output/artifacts/symmetric_flower.py` (pure numpy) verifies:
admissibility thresholds, $A(d)=2\pi(\cosh d-1)$, empty-disk probabilities
$e^{-\lambda A(d)}$, inadmissibility for large $\rho$ (e.g. $n=3$,
$\rho=3$: $\coth(\rho/2)\cos(\pi/3)=0.552<1$), and scaling
$\lambda A(d_\lambda)\to\pi s^2/(4\cos^2(\pi/n))$ (for $n=6,s=1$:
$1.0560,1.0481,1.0473,1.0472\to1.0472$ at
$\lambda=10,10^2,10^3,10^4$), and self-avoidance $S=1$ for every tabulated
symmetric flower (verified in the Poincaré disk model with strictly
positive margin, e.g. $0.118$–$3.95$ for $n=3$ and $0.24$–$15.2$ for
$n=6$), so these examples lie in the support of the repaired kernel.

## 6. Limitations / honesty

The kernel is explicit modulo the elementary bisector-intersection map
(linear in Klein coordinates) and the union-area functional; no further
closed form exists for general asymmetric $n$-gons. Delaunay
existence/uniqueness and transverse convergence are invoked from standard
hyperbolic stochastic-geometry theory (Isokawa; Calka et al.); the
boundedness sector estimate and DCT majorant above make the new parts
self-contained. Numerics cover only the symmetric sub-family as a kernel
sanity check, not the full $n$-fold integral.
