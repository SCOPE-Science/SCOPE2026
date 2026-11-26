# Strict angular anisotropy calibration for a quarter-turn swimmer in a harmonic trap

## Finding
Consider the stationary, athermal, planar four-orientation run-and-tumble model with a harmonic restoring force and independent clockwise and anticlockwise quarter-turn clocks. Let \(\theta\) be the position's polar angle relative to a propulsion axis and write \(a=\gamma/\mu>0\), where \(\gamma\) is the rate of each permissible quarter-turn and \(\mu\) is the harmonic relaxation rate. The stationary fourth angular harmonic
\[
 Q(a)=\mathbb E[\cos(4\theta)]
\]
is **strictly decreasing and continuous** from \(1\) to \(0\) as \(a\) runs from zero to infinity. In particular,
\[
 0<Q(a)<1,\qquad Q(1)=\pi-3,\qquad
 Q(a)\sim\frac{1}{8a}\quad(a\to\infty).
\]
Thus every possible stationary angular measurement \(q\in(0,1)\) determines exactly one tumbling-to-trap ratio \(a\) by \(Q(a)=q\). This determination is independent of propulsion speed. The theorem asserts an identifiability property of the stationary *position angle*, not of the instantaneous heading.

## Assumptions and scope
Let \(\mu,v_0,\gamma>0\). A planar particle obeys \(\dot{\boldsymbol r}=-\mu\boldsymbol r+\sqrt2 v_0\boldsymbol\sigma(t)\). The orientation \(\boldsymbol\sigma\) lies in \(\{\pm\boldsymbol e_x,\pm\boldsymbol e_y\}\), and each of its two permissible quarter-turn transitions occurs at rate \(\gamma\). There is no added translational Brownian diffusion, interaction, resetting, or rotational-angle continuum. The invariant orientation law is uniform. The stationary position law is unique; its origin has zero probability, so the polar angle is defined almost surely.

Use the orthogonal coordinates \(u=(x+y)/\sqrt2\) and \(v=(x-y)/\sqrt2\), with \(L=v_0/\mu\). The normalized stationary coordinates \(U=u/L\), \(V=v/L\) are independent, with common density
\[
 f_a(z)=\frac{(1-z^2)^{a-1}}{B(1/2,a)}\boldsymbol1_{(-1,1)}(z).
\]
This decoupling and the density are established in Smith, Le Doussal, Majumdar and Schehr (2022) and are premises, not novelty claims. Set \(X=U^2\), \(Y=V^2\). They are independent \(\operatorname{Beta}(1/2,a)\) variables. The complete result concerns all positive real \(a\), not only values on either side of the planar-density mode transition at \(a=1\).

## Proof
**1. The angular response as a beta ratio.** Write \(\phi=\arg(U+iV)\). Because \((x,y)\) is the reflected forty-five-degree rotation of \((u,v)\), \(\theta=\pi/4-\phi\) modulo \(2\pi\). Hence, except at the null origin,
\[
 \cos(4\theta)=-\cos(4\phi)
 =-1+\frac{8U^2V^2}{(U^2+V^2)^2}.
\]
Introduce the even, strictly decreasing-on-positive-arguments function \(F(t)=\operatorname{sech}^2(t/2)\). Since \(F(\log(X/Y))=4XY/(X+Y)^2\),
\[
 Q(a)=2\mathbb E F(D_a)-1,\qquad
 D_a=\log X-\log Y,
 \quad X,Y\stackrel{\mathrm{iid}}\sim\operatorname{Beta}(1/2,a).
 \tag{1}
\]
The expectation exists, since the integrand lies in \([0,1]\). An equivalent fully explicit integral formula is
\[
 Q(a)=\frac{8}{B(1/2,a)^2}\int_0^1\!\int_0^1
 \frac{\sqrt{xy}(1-x)^{a-1}(1-y)^{a-1}}{(x+y)^2}\,dx\,dy-1.
 \tag{2}
\]

**2. Symmetric unimodality of the logarithmic beta ratio.** Put \(W_a=-\log X>0\). Its density is
\[
 h_a(w)=\frac{e^{-w/2}(1-e^{-w})^{a-1}}{B(1/2,a)}\boldsymbol1_{(0,\infty)}(w).
 \tag{3}
\]
For \(a>1\), this is strictly log-concave on its half-line support, because
\[
 \frac{d^2}{dw^2}\log h_a(w)
 =-\frac{(a-1)e^{-w}}{(1-e^{-w})^2}<0.
\]
The difference of two independent identically distributed log-concave real random variables has a symmetric log-concave density, and therefore a symmetric unimodal density. This standard convolution fact applies to \(D_a=W_a^{(2)}-W_a^{(1)}\).

For \(0<a\le1\), expand the positive binomial series in (3):
\[
 h_a(w)=\frac1{B(1/2,a)}\sum_{n=0}^\infty
 \frac{(1-a)_n}{n!}e^{-(n+1/2)w},\qquad w>0.
\]
All coefficients are nonnegative. Writing the density of a difference of two copies for \(d\ge0\) and applying Tonelli yields
\[
 g_a(d)=\frac1{B(1/2,a)^2}\sum_{m,n\ge0}
 \frac{(1-a)_m(1-a)_n}{m!n!(m+n+1)}
 e^{-(n+1/2)d}.
 \tag{4}
\]
Thus \(g_a\) is strictly decreasing on positive arguments; symmetry gives \(g_a(-d)=g_a(d)\). This covers the remaining parameters, including \(a=1\). Consequently, for **every** \(a>0\), \(D_a\) admits a symmetric unimodal density. No continuity or boundedness at zero is needed: for \(a\leq 1/2\), the autocorrelation integral at zero diverges because \(h_a(w)^2\) is proportional to \(w^{2a-2}(1+o(1))\) as \(w\downarrow0\). This is a density singularity, not an atom.

**3. A strict smoothing inequality.** If \(D\) has a symmetric unimodal density \(g\), possibly unbounded at zero, then
\[
 H(s)=\mathbb E F(D+s)
\]
is even and strictly decreasing on \([0,\infty)\). Apply layer cake to \(g\), whose positive superlevel sets are centered intervals up to null endpoints. For a positive level the radius \(r\) of such an interval is finite by integrability; a set of levels of positive measure has \(r>0\) since \(\int g=1\). The contribution of this interval to \(H(s)\) is \(J_r(s)=\int_{s-r}^{s+r}F(v)\,dv\). For each \(r>0\) and \(s>0\), \(J_r'(s)=F(s+r)-F(s-r)<0\), since \(|s+r|>|s-r|\). Tonelli's theorem now gives the strict comparison of \(H\) at any two nonnegative shifts. Therefore, if \(E\) is independent of \(D\) with \(\Pr(E\ne0)>0\),
\[
 \mathbb E F(D+E)<\mathbb E F(D).
 \tag{5}
\]
This last statement does not require \(E\) itself to be symmetric or unimodal.

**4. Beta multiplication forces strict monotonicity.** Fix \(a,b>0\). The elementary gamma-addition/Dirichlet identity gives
\[
 X_{a+b}\ \stackrel d=\ X_a Z,\qquad
 X_a\sim\operatorname{Beta}(1/2,a),\quad
 Z\sim\operatorname{Beta}(a+1/2,b),
 \tag{6}
\]
with \(X_a\) and \(Z\) independent. Indeed, use three independent gamma variables of shapes \(1/2,a,b\); the ratio of the first to the sum of the first two is independent of the sum, and the latter sum divided by the three-variable total has the stated law. Apply (6) to two independent copies. Their logarithmic ratio obeys
\[
 D_{a+b}\stackrel d=D_a+E_{a,b},\qquad
 E_{a,b}=\log Z_1-\log Z_2,
\]
with the two summands independent and \(E_{a,b}\) nondegenerate. Combining (1) with (5) proves \(Q(a+b)<Q(a)\) for every \(a,b>0\).

**5. Endpoints, continuity, and exact anchor.** The beta integral or gamma representation shows \(X_a\to1\) in probability as \(a\downarrow0\). Therefore \(D_a\to0\) and (1), by bounded convergence, gives \(Q(a)\to1\). As \(a\to\infty\), the scaled variable \(aX_a\) converges in distribution to \(\operatorname{Gamma}(1/2,1)\). The ratio \(X/(X+Y)\) consequently converges to \(\operatorname{Beta}(1/2,1/2)\). As \(F(D_a)=4W(1-W)\) for \(W=X/(X+Y)\), its expectation tends to \(1/2\), and so \(Q(a)\to0\). Continuity follows from dominated convergence in the beta-density representation locally uniformly in \(a>0\). Strict monotonicity and these endpoints establish a bijection of \((0,\infty)\) onto \((0,1)\).

At \(a=1\), the rotated coordinates are uniform on a square. Its angular density in the rotated angle \(\phi\) is \(M(\phi)^2/8\), with \(M=\min(1/|\cos\phi|,1/|\sin\phi|)\). By eightfold symmetry,
\[
 \mathbb E\cos(4\phi)=\int_0^{\pi/4}\!\frac{\cos(4\phi)}{\cos^2\phi}\,d\phi=3-\pi,
\]
and hence \(Q(1)=\pi-3\).

Finally put \(Z=\sqrt a\,U\). Its density has the normalized Gaussian expansion
\[
 \frac{e^{-z^2}}{\sqrt\pi}\left[1+\frac{z^2-z^4/2-1/8}{a}+O(a^{-2})\right]
\]
under integrable polynomial-weighted errors (split at \(|z|=a^{1/8}\), where Taylor expansion is uniform, and use Gaussian-dominated tails outside). For the two independent coordinates, polar integration gives angular density
\[
 \frac1{2\pi}\left[1-\frac{\cos(4\phi)}{4a}+O(a^{-2})\right],
\]
with uniform angular remainder. Thus the physical-angle response satisfies \(Q(a)=1/(8a)+O(a^{-2})\), proving the asserted high-rate law.

## Verification
The reproducible `CHECK.py` numerically evaluates (2) by tensor Gauss--Jacobi quadrature, independently evaluates (1) with scrambled Sobol points transformed through exact beta inverse distribution functions, verifies strict parameter ordering on several nontrivial test points, compares the independent representations, checks the exact anchor \(Q(1)=\pi-3\), and tests the large-\(a\) coefficient. Its recorded output is `PASS: 38 analytic-anchor, positivity, monotonicity, quadrature, and asymptotic checks`. Dependencies: Python 3.10 or later, NumPy, SciPy. These are finite consistency checks, not exhaustive validation of the infinite real-parameter theorem, which rests on steps 1--5 above.

## Relationship to prior work
Smith, Le Doussal, Majumdar and Schehr derive the exact rotated-coordinate beta product law, angular marginal, and qualitative weakening of anisotropy as the flip-to-trap ratio grows. In particular, their source already contains the \(a=1\) angular distribution. Those formulas and observations are credited rather than claimed. The present claim adds the globally *strict* fourth-angular-harmonic ordering for all positive ratios, its full attainable range and one-observable inverse identification, proved through a beta multiplicative coupling and a nontrivial unimodality argument. A related mathematical result on radial concentration shells for the same square-supported process concerns the distribution of **radius**, not the fourth harmonic of **position angle**. A result on fourth radial moments for isotropic general-turn processes concerns a different orientation law and observable, not this comparison. These are distinctions of statements and implication, rather than title distinctions. An unindexed implication from a stronger angular-distribution ordering remains a priority risk.

## Limitations
The theorem concerns one angular harmonic of the **stationary position angle** in the exact quarter-turn, athermal harmonic model; it does not assert monotone ordering of the whole angular density, higher angular harmonics, noisy-angle estimators, or statistical confidence intervals from finite samples. It identifies \(\gamma/\mu\), not the two rates separately without calibrating one of them. Thermal translational noise and alternative turning rules are not covered. The small- and large-parameter endpoints are limits and are not attained by finite positive parameter values. Independently established publication priority and independent scientific audit are not provided.

## References
1. N. R. Smith, P. Le Doussal, S. N. Majumdar, and G. Schehr, “Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions,” arXiv:2207.10445v1 (first public 2022-07-21), *Physical Review E* 106, 054133 (2022). https://arxiv.org/abs/2207.10445 ; public full text https://arxiv.org/html/2207.10445.
2. B. Loewe and T. N. Shendruk, “Anisotropic run-and-tumble-turn dynamics,” arXiv:2305.03663v1 (2023-05-05), https://arxiv.org/abs/2305.03663v1. This preprint studies anisotropic turning kinetics, not the harmonic-trap angular inverse result.
3. “A two-shell radial concentration transition for a square-supported run-and-tumble particle,” https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-a-two-shell-radial-concentration-transition-for-a-square-support--d357046fa9e1 (radial, not angular, comparison).
4. “Sharp fourth-moment envelope for correlated-turn swimmers in a harmonic trap,” https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-sharp-fourth-moment-envelope-for-correlated-turn-swimmers-in-a-h--965a51cb75a3 (radial moments of a different turning model).
