# Reentrant real-to-conjugate-to-real optimal coherent sites for a quadratic Bargmann–Fock state

## Finding
In the normalized analytic Bargmann–Fock space, let
\[
 f_a(z)=1+a z-a z^2,\qquad a>0.
\]
Approximate \(f_a\) by a freely scaled *single* normalized coherent kernel \(k_w(z)=\exp(z\overline w-|w|^2/2)\), with \(w\in\mathbb C\). Put
\[
 h(a)=a^3-2a^2-7a+4,
\]
and let \(a_-\) and \(a_+\) be its two positive roots, in \((1/2,1)\) and \((3,4)\), respectively. Numerically,
\[
 a_-=0.515138047128\ldots,\quad a_+=3.626198068527\ldots.
\]
The complete set of globally optimal coherent sites has the following **reentrant classification**:

1. If \(0<a<a_-\), there is exactly one optimum, at the unique real stationary site \(x_2(a)>0\) lying between the two real zeros of \(f_a\).
2. If \(a_-<a<a_+\), there are exactly two optima, the conjugate sites
   \[
   w_\pm(a)=\frac{1-a}{2}\pm i\sqrt{\frac{-h(a)}{4a}}.
   \]
3. If \(a>a_+\), there is exactly one optimum, at the unique real stationary site \(x_1(a)<0\) lying to the left of both zeros of \(f_a\).
4. At each boundary \(a=a_-\) or \(a=a_+\), the two sites merge into the *unique* real optimum \(w=(1-a)/2\).

The real stationary sites in (1) and (3) are specified uniquely by
\[
 a(1-2x)-x(1+ax-ax^2)=0
\]
in the indicated intervals. The transitions are continuous but square-root sharp: approaching \(a_-\) from above or \(a_+\) from below, respectively,
\[
 |\operatorname{Im}w_\pm|\sim
 \sqrt{\frac{-h'(a_-)}{4a_-}}\sqrt{a-a_-},
 \qquad
 |\operatorname{Im}w_\pm|\sim
 \sqrt{\frac{h'(a_+)}{4a_+}}\sqrt{a_+-a}.
\]
Throughout the closed conjugate-site regime \([a_-,a_+]\), the *exact* maximal captured squared norm is
\[
 M(a)=4a^2\left(1+\frac a4\right)e^{-2+1/a}.
\]
Outside that interval it is \(M(a)=e^{-x_j(a)^2}(1+a x_j(a)-a x_j(a)^2)^2\), with \(j=2\) on the low side and \(j=1\) on the high side. The optimal squared approximation error is \(1+3a^2-M(a)\).

## Assumptions and scope
The Hilbert space is the entire-function space with norm
\[
 \|f\|^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z),
\]
so \(\|z^n\|^2=n!\) and \(\|k_w\|=1\). The target is exactly \(f_a\) with one positive real coefficient \(a\), not arbitrary quadratic coefficients. The scalar multiplying \(k_w\) is unrestricted complex. The objective is squared Hilbert-space distance (equivalently maximal coherent-state overlap), not pointwise distance or a mixture of coherent states. All claimed optimizers are global over \(w\in\mathbb C\).

## Proof
**Reduction and exact angular identity.** By the reproducing property, optimization over a scalar at fixed \(w\) captures \(|\langle f_a,k_w\rangle|^2=e^{-|w|^2}|f_a(w)|^2\). Thus maximize \(Q_a(w)=e^{-|w|^2}|f_a(w)|^2\); a maximizer exists because this tends to zero at infinity and \(Q_a(0)=1\). Write \(w=x+iy\), \(u=x^2+y^2\). Direct expansion and completion of the square yield the identity
\[
 |f_a(w)|^2=\left(1+\frac a4\right)(1+au)^2
 -4a\left(x-\frac{1-au}{4}\right)^2. \tag{1}
\]
In particular, the upper bound in (1) is saturated exactly when \(x=(1-au)/4\). For \(a>1/2\), the function \(e^{-u}(1+au)^2\) has its unique global maximum over \(u\ge0\) at \(u_*=2-1/a\).

**All nonreal critical points and the middle regime.** At a nonzero value of \(f_a\), differentiation of \(\log Q_a\) gives the stationary equation \(\overline w f_a(w)=f_a'(w)\). Its imaginary and real parts are, respectively,
\[
 -y(au-2a+1)=0,\qquad
 x(1+2a-au)+a(u-1)=0. \tag{2}
\]
For \(y\ne0\), equations (2) force \(u=u_*\) and \(x=(1-a)/2\), hence
\[
 y^2=2-\frac1a-\frac{(1-a)^2}{4}=-\frac{h(a)}{4a}. \tag{3}
\]
The cubic \(h\) has exactly two positive simple roots: its derivative has only one positive critical point (a strict minimum), while \(h(0)>0\), \(h(1)<0\), and \(h(4)>0\). Consequently (3) is strictly positive exactly when \(a_-<a<a_+\). In this regime (1) is saturated at precisely the two sites (3), with \(u=u_*\). They attain the universal upper bound, making them the only global maximizers. At either endpoint the upper bound is saturated at only one real site, which is therefore the unique optimum. The displayed square-root expansions follow by Taylor expansion of the simple roots of \(h\).

**Excluding every other global site.** A global maximizer cannot be a zero of \(f_a\), and must satisfy the stationary equations. Outside \([a_-,a_+]\) there is no nonreal stationary point. On the real axis, the two simple zeros are \(\zeta_\pm=(1\pm\sqrt{1+4/a})/2\), with \(\zeta_-<0<\zeta_+\). On each of the three real intervals cut out by these zeros, \(\log Q_a(x)=2\log|f_a(x)|-x^2\) has strictly negative second derivative
\[
 -2-\frac{2}{(x-\zeta_-)^2}-\frac{2}{(x-\zeta_+)^2}<0.
\]
It tends to \(-\infty\) at the endpoints of each interval, so there is exactly one real stationary maximum in each: \(x_1<\zeta_-\), \(x_2\in(0,\zeta_+)\), and \(x_3>\zeta_+>1\). They obey the cubic stationary equation displayed in the Finding.

A real candidate also must maximize over its fixed-radius circle. By (1), this necessary condition is
\[
 D(x,a):=1-ax^2-4x\ge0\quad(x>0),
 \qquad D(x,a)\le0\quad(x<0). \tag{4}
\]
The candidate \(x_3>1\) never meets (4). For the other branches, polynomial elimination of the real stationary equation and \(D=0\) gives
\[
 \operatorname{Res}_x\big(a(1-2x)-x(1+ax-ax^2),\,1-ax^2-4x\big)
 =-a(a+4)h(a). \tag{5}
\]
At either positive root of \(h\), the simultaneous solution is \(x=(1-a)/2\), positive at \(a_-\) and negative at \(a_+\); uniqueness of the branch stationary point places these crossings on \(x_2\) and \(x_1\), respectively. For sufficiently small \(a>0\), \(x_2\sim a\) and \(x_1\sim-1/\sqrt a\), whence \(D(x_2,a)>0\) and \(D(x_1,a)>0\). Continuity, (5), and the absence of other positive crossing values show that \(x_2\) satisfies (4) exactly for \(a\le a_-\), whereas \(x_1\) satisfies (4) exactly for \(a\ge a_+\). Thus in the low regime only \(x_2\) and in the high regime only \(x_1\) can be a global maximizer. Since a global maximizer exists, those candidates are necessarily unique global maximizers. This completes the classification.

Finally, orthogonality of \(1,z,z^2\) gives \(\|f_a\|^2=1+a^2+2a^2=1+3a^2\); subtracting \(M(a)\) yields the best squared error.

## Verification
The independent-of-optimization identity (1) and resultant (5) were checked symbolically by polynomial expansion and elimination. The included `check.py` is a standalone Python standard-library numerical diagnostic: it reconstructs both positive critical roots by bisection, reconstructs all three real stationary sites, compares predicted optima against polar grids over a spread of coefficients, and evaluates the square-completion identity at off-axis sites. A passing finite grid is consistency evidence, not a proof of the global or universal assertions; those follow from (1)–(5), strict real-axis log concavity, and existence of maximizers. Run `python3 check.py` in the directory containing this report.

## Relationship to prior work
Alpay, Colombo, Diki, Sabadini and Struppa (arXiv:2304.11551, first version 23 April 2023) express superoscillatory Bargmann transforms as coherent-state superpositions and supply the normalized Fock kernel; their analyzed transform and approximation constructions do not give the best single coherent site for this three-mode polynomial. Escudero, Haimi and Romero (2021) give density criteria for Fock multi-jet sampling rather than site optimization for a fixed target. Zhang, Zhou and Yu (2021 online) investigate approximation by convex mixtures of a *given* set of quantum states, not free one-kernel Hilbert projection. Related Gaussian intensity classifications for \(\cosh(az)\), \(z^n-a\), and \((z^n-a)(z^n-b)\) have different target families or declared degree ranges and do not imply the present constrained quadratic's two sharp global-site transitions. A separate analytic Bergman-disk binomial approximation theorem concerns a different reproducing kernel and target; Gaussian Fock normalization and the frustrated three-mode interaction are essential here.

## Limitations
The classification is restricted to the balanced coefficient path \(1+a z-a z^2\), and does not classify every complex quadratic or multimode coherent mixture. It does not analyze all nonglobal stationary points or arbitrary metrics on quantum states. Originality is assessed against the specified inspected and indexed sources, not established by a proof of historical uniqueness. Independent mathematical review has not been performed.

## References
- D. Alpay, F. Colombo, K. Diki, I. Sabadini, D. C. Struppa, *Superoscillations and Fock spaces*, arXiv:2304.11551, first posted 2023-04-23; *Journal of Mathematical Physics* 64 (2023), 093505, https://arxiv.org/abs/2304.11551 .
- L. A. Escudero, A. Haimi, J. L. Romero, *Multiple Sampling and Interpolation in Weighted Fock Spaces of Entire Functions*, *Complex Analysis and Operator Theory* 15 (2021), 35, https://doi.org/10.1007/s11785-020-01065-4 .
- L.-q. Zhang, N.-n. Zhou, C.-s. Yu, *The Best Approximation of an Objective State With a Given Set of Quantum States*, *Annalen der Physik* (online 2021-12-30), https://doi.org/10.1002/andp.202100407 .
- AMS, *MSC2020*: 30H20, Bergman spaces and Fock spaces, https://mathscinet.ams.org/msc/msc2020.html?t=30H25 .
