# Exact period minimum and two-gate critical arrest of the Wilson algebraic cycle

## Finding

For the polynomial Wilson–Liénard family
\[
\dot x=y-(x^2-1)(x^3-bx),\qquad
\dot y=-x\bigl(1+y(x^3-bx)\bigr),
\]
let \(\Gamma\) be the unit circle and let \(T(b)\) be the **minimal period in the given physical time** of \(\Gamma\), whenever it is a periodic orbit. There is an exact interval \((b_-,b_+)\) on which this is so. On the whole interval the period is strictly convex, obeys \(T(b)=T(1-b)\), and has the unique exact minimum
\[
T(1/2)=\frac{16\pi}{\sqrt{63}}.
\]
At both ends it diverges with the **same explicit inverse-square-root coefficient**, although the transverse Floquet exponents diverge with different, opposite-sign coefficients. The normalized physical-time occupation measure on the fixed circle converges at each endpoint to two equal atoms; in each slowing gate its square-root-scaled angular fluctuation approaches the standard Cauchy law.

Here are exact definitions and constants. Let \(u\in(1/2,1)\) be the unique solution of
\[
2u-1=2[u(1-u)]^{3/2},
\]
and put
\[
r=u(1-u),\qquad b_-=u-r^{-1/2},\qquad b_+=1-b_-,
\qquad C=2\pi\sqrt{\frac{2\sqrt r}{3-8r}}.
\]
Numerically \(b_-=-1.4400956573053\ldots\), \(b_+=2.4400956573053\ldots\), and \(C=5.8932532999967\ldots\). Then \(\Gamma\) is a periodic orbit exactly when \(b_-<b<b_+\), and
\[
\lim_{\varepsilon\downarrow0}\sqrt\varepsilon\,T(b_-+\varepsilon)
=\lim_{\varepsilon\downarrow0}\sqrt\varepsilon\,T(b_+-\varepsilon)=C.
\]
Write \(\mathfrak m(b)>0\) for the nontrivial transverse multiplier of the periodic circle. Put
\[
q_-=-2u(u-b_-)<0,\qquad q_+=2(1-u)(u-b_-)>0.
\]
Then
\[
\lim_{\varepsilon\downarrow0}\sqrt\varepsilon\log\mathfrak m(b_-+\varepsilon)=Cq_-,
\qquad
\lim_{\varepsilon\downarrow0}\sqrt\varepsilon\log\mathfrak m(b_+-\varepsilon)=Cq_+.
\]
The circle is therefore attracting sufficiently close to the left endpoint, and repelling sufficiently close to the right endpoint. The signed transverse exponent per unit time tends to \(q_-\) and \(q_+\), respectively.

For the normalized physical-time measure \(\nu_b\) along \(\Gamma\), define
\[
p_-=(\sqrt{u},-\sqrt{1-u}),\qquad
p_+=(\sqrt{1-u},\sqrt u).
\]
As probability measures on the plane,
\[
\nu_{b_-+\varepsilon}\Rightarrow\frac12(\delta_{p_-}+\delta_{-p_-}),
\qquad
\nu_{b_+-\varepsilon}\Rightarrow\frac12(\delta_{p_+}+\delta_{-p_+}).
\]
More precisely, if \(\theta_g\) denotes either of the two critical angles and \(\theta-\theta_g\) is its signed local angle in a fixed small gate, then conditional on being in that gate, the variable
\[
Z_\varepsilon=\sqrt{\frac{\beta}{\alpha\varepsilon}}(\theta-\theta_g),
\quad \alpha=\sqrt r,\quad \beta=\frac{\sqrt r(3-8r)}{2u-1},
\]
converges in distribution to the density \(\bigl[\pi(1+z^2)\bigr]^{-1}\) on \(\mathbb R\), at either endpoint. All endpoint statements are one-sided from within the open periodicity interval.

## Assumptions and scope

The system is considered on \(\mathbb R^2\), with real parameter \(b\). The claimed periodic orbit is the **fixed geometrical unit circle only**, not other possible moving limit cycles. Its angular coordinate is \((x,y)=(\cos\theta,\sin\theta)\); \(T(b)\) is a full physical-time traversal. The transverse multiplier is for the original smooth planar flow, not for the reparameterized angular equation. The weak occupation measures and Cauchy fluctuations concern uniform sampling of physical time over one traversal, not uniform sampling of angle.

The uniqueness statement for \(u\) refers only to \((1/2,1)\). At the excluded endpoint parameters the circle has two equilibria and is not a single periodic trajectory. At interior parameters there may also be off-circle limit cycles; their number and stability are not asserted here.

## Proof

**1. Exact angular reduction and circle domain.** Set \(B_b(x)=x^3-bx\) and \(R=x^2+y^2-1\). A direct product-rule calculation gives
\[
\dot R=-2xB_b(x)R.
\]
Hence \(\Gamma\) is invariant. On \(\Gamma\) the vector field factors as
\[
(\dot x,\dot y)=(y,-x)\bigl[1+xy(x^2-b)\bigr],
\]
so
\[
\dot\theta=-f_b(\theta),\qquad
f_b(\theta)=1+\cos\theta\sin\theta(\cos^2\theta-b).
\]
For \(s=xy>0\), \(f_b>0\) is equivalent to \(b<x^2+1/s\); for \(s<0\) it is equivalent to \(b>x^2+1/s\). Writing \(v=x^2\in(0,1)\), the sharp bounds are therefore
\[
b_- =\max_{0<v<1}\left(v-\frac1{\sqrt{v(1-v)}}\right),
\quad
b_+ =\min_{0<v<1}\left(v+\frac1{\sqrt{v(1-v)}}\right).
\]
The first maximizer satisfies \(2v-1=2[v(1-v)]^{3/2}\). The left side strictly increases on \((1/2,1)\) while the right side strictly decreases, so there is a unique solution \(u\). Reflecting \(v\mapsto1-v\) gives the second minimizer and \(b_+=1-b_-\). At equality the angular speed has exactly two zeros, at antipodal positions. Thus the fixed circle rotates strictly exactly for \(b\in(b_-,b_+)\), with
\[
T(b)=\int_0^{2\pi}\frac{d\theta}{f_b(\theta)}.
\]

**2. Exact symmetry, convexity and minimum.** The quarter-turn identity
\[
f_{1-b}(\theta+\pi/2)=f_b(\theta)
\]
proves \(T(1-b)=T(b)\). Differentiation under the integral on any compact subinterval of \((b_-,b_+)\) gives
\[
T''(b)=2\int_0^{2\pi}
\frac{(\cos\theta\sin\theta)^2}{f_b(\theta)^3}\,d\theta>0.
\]
Symmetry and strict convexity give the unique minimum at \(b=1/2\). There
\(f_{1/2}(\theta)=1+\frac18\sin(4\theta)\), so the elementary integral for \(1/(1+k\sin t)\), \(|k|<1\), yields \(T(1/2)=16\pi/\sqrt{63}\).

**3. The two identical quadratic gates.** At the left endpoint the two angular zeros occur at \(p_-\) and \(-p_-\); at the right endpoint they occur at \(p_+\) and \(-p_+\). Writing \(v=\cos^2\theta\), direct differentiation gives
\[
\partial_\theta f_b=(2v-1)(v-b)-2v(1-v),
\quad
\partial_{\theta\theta}f_b=-2xy(8v-3-2b).
\]
The defining equation for \(u\) implies
\[
8u-3-2b_- =\frac{3-8r}{2u-1}>0.
\]
At either endpoint and each of its two gates, the local expansion from **inside** the periodicity interval is
\[
f_{b_\pm\mp\varepsilon}(\theta_g+\phi)
=\alpha\varepsilon+\beta\phi^2
+O(\varepsilon|\phi|+|\phi|^3),
\quad \alpha=\sqrt r,\quad
\beta=\frac{\sqrt r(3-8r)}{2u-1}>0,
\]
where the notation means \(b_-+\varepsilon\) at the left and \(b_+-\varepsilon\) at the right. The expansion is uniform on a sufficiently small fixed gate. Away from the two gates the denominator has a uniform positive lower bound.

Consequently, for every continuous \(g\) on the circle,
\[
\sqrt\varepsilon\int_0^{2\pi}
\frac{g(\theta)}{f_{b_\pm\mp\varepsilon}(\theta)}\,d\theta
\longrightarrow\frac{\pi}{\sqrt{\alpha\beta}}
\bigl[g(\theta_g)+g(\theta_g+\pi)\bigr].
\]
To justify this, set \(\phi=\sqrt\varepsilon z\) in each gate. The positive quadratic lower bound allows dominated convergence after first restricting to a fixed scaled interval; the complement is bounded by a multiple of \(\int_{|z|>K}(1+z^2)^{-1}dz\), uniformly as \(K\to\infty\). Each gate contributes exactly \(\pi/\sqrt{\alpha\beta}\). Since \(2u-1=2r^{3/2}\), one has \(\alpha\beta=(3-8r)/(2\sqrt r)\), giving \(C=2\pi/\sqrt{\alpha\beta}\). Choosing \(g=1\) proves the two period limits; dividing by \(T\) proves the two-atom occupation limits. The same scaling with \(z=\sqrt{\beta/(\alpha\varepsilon)}\phi\) gives the claimed conditional standard Cauchy law.

**4. Physical transverse multipliers.** The regular defining function \(R\) has normal linearization \(\dot{\delta R}=-2xB_b(x)\delta R\) on the circle. Because \(R\) is a defining coordinate and the orbit returns to its initial point, its nontrivial planar Floquet multiplier is exactly
\[
\mathfrak m(b)=\exp\left\{\int_0^{2\pi}
\frac{-2\cos^2\theta(\cos^2\theta-b)}{f_b(\theta)}\,d\theta\right\}.
\]
Apply the weighted gate limit proved above to the continuous numerator. At the left gate its value is \(q_-=-2u(u-b_-)\); at the right gate it is \(q_+=2(1-u)(u-b_-)\). Both antipodal gates have equal values. This gives both limits of \(\sqrt\varepsilon\log\mathfrak m\) and of \(T^{-1}\log\mathfrak m\). Since \(u-b_->0\), the strict signs are opposite. This proves all assertions.

## Verification

The accompanying standalone standard-library script `checker.py` recomputes the unique critical parameter numerically, checks the exact-center period and quarter-turn period symmetry, and compares rescaled direct physical-time quadratures with the analytical constants. It reports values approaching \(C\approx5.89325330\), \(Cq_-\approx-14.90253096\) and \(Cq_+\approx9.32202310\). Its execution ends with `WILSON_CIRCLE_DIAGNOSTICS_OK`. These are **numerical diagnostics only**; the universal claims are proved by the angular identities, strict convexity and localized integral limits above.

## Relationship to prior work

Gasull and Sabatini introduced and investigated this fixed algebraic circle and its moving companion limit cycles (2019). Chen and Chen analyzed the polynomial Wilson–Liénard family's global bifurcations (2020). Gasull and Giacomini's full publicly available 2021 paper, Section 3.1 and Corollary 3.2, supplies the explicit polynomial system, the circle's existence window, and its attraction/repulsion regimes. Those bifurcation and stability classifications are **not claimed as new**. The present exact convex physical-period profile, algebraic minimum, equal two-end slowing coefficient, two-gate occupation limit and opposite sharp Floquet laws are different quantitative statements; they are not consequences of the quoted existence and stability statements without additional analysis.

Related published work on singular physical-time slowing for other planar algebraic ovals concerns different vector fields and different critical loci; generic local saddle-node asymptotics alone do not provide these model-specific coefficients or the global period symmetry. The 2019 and 2020 studies were not accessible in full through the attempted lawful routes, so prior-publication priority remains a material uncertainty; the same-paper 2021 arXiv full text was inspected, not merely its abstract. Comparison against unindexed or subsequently published equivalent derivations is not exhaustive.

## Limitations

No claim is made about all off-circle cycles, their physical periods, or a global planar basin classification. At the two critical parameters the circle is not a periodic orbit, and the divergent period is an interior one-sided limit. The Cauchy law refers to a locally rescaled angular coordinate **conditional on a fixed gate**, not to the unscaled whole-circle distribution. The statement gives leading endpoint asymptotics but no uniform finite-parameter error constant or full higher-order expansion. No independent mathematical audit has been performed.

## References

1. A. Gasull and H. Giacomini, *Effectiveness of the Bendixson–Dulac theorem*, arXiv:2101.03874v1, first posted 2021-01-11, Section 3.1, Corollary 3.2. https://arxiv.org/html/2101.03874v1 ; DOI: 10.1016/j.jde.2021.10.011.
2. A. Gasull and M. Sabatini, *Fixed and moving limit cycles for Liénard equations*, Ann. Mat. Pura Appl. 198 (2019), 1985–2006, DOI: 10.1007/s10231-019-00850-z. Abstract and publication metadata consulted; full text not verified.
3. H. Chen and H. Chen, *Global dynamics of a Wilson polynomial Liénard equation*, Proc. Amer. Math. Soc. 148 (2020), 4769–4780, DOI: 10.1090/proc/15074. Author-hosted abstract consulted; full text not verified.
