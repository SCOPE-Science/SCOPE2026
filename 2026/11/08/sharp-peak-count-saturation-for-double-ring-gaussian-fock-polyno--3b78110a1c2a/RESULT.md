# Sharp peak-count saturation for double-ring Gaussian Fock polynomials

## Finding

For every integer \(n\ge3\) and every pair \(0<a<b\) of real numbers, define the Gaussian-weighted polynomial intensity
\[
H_{n,a,b}(z)=e^{-|z|^2}\left|(z^n-a)(z^n-b)\right|^2,\qquad z\in\mathbb C.
\]
It has **at most \(2n+1\) distinct local maxima**, including possibly degenerate ones. Every local maximum other than the origin lies on one of the \(n\) rays \(z^n\in(-\infty,0)\), and on any such ray there are at most two local maxima. Every nonzero stationary point away from the polynomial zeros lies on one of the \(2n\) rays \(z^n\in\mathbb R\).

The bound \(2n+1\) is **attainable, with every maximum nondegenerate, for every integer \(n\ge11\)**. For \(n=11\), the explicit integer parameters \(a=50000\) and \(b=4800000\) attain it, giving exactly \(23\) nondegenerate maxima. For every \(n\ge12\), an open set of positive parameter pairs attains \(2n+1\) maxima. For example, \(n=12\), \(a=1\), \(b=33800000\) gives exactly \(25\) nondegenerate maxima.

The theorem does **not** claim that degree \(n=11\) is the smallest order admitting the saturated bound; no assertion about sharpness for \(3\le n\le10\) is made. Nor does it identify the global maximum among the coexisting local maxima.

## Assumptions and scope

The integer \(n\) is at least \(3\), the real constants satisfy \(0<a<b\), and local maxima mean local maxima of the smooth function \(H_{n,a,b}:\mathbb C\to[0,\infty)\). A *nondegenerate* maximum has negative-definite real Hessian. The Gaussian factor is normalized exactly as \(e^{-|z|^2}\); a change of Fock scale changes the displayed coefficients and radii. The \(2n\) polynomial zeros are simple, hence nondegenerate minima of \(H\). The origin is always a nondegenerate maximum because \(n\ge3\).

## Proof

**1. Real-ray localization.** Write \(F(z)=(z^n-a)(z^n-b)\). At a nonzero point with \(F(z)\ne0\), the stationary equation is \(F'(z)=\overline z F(z)\). Set \(w=z^n\) and \(t=|z|^2>0\); after multiplication by \(z\) it becomes
\[
(t-2n)w^2+(n-t)(a+b)w+tab=0.
\]
Its discriminant equals
\[
\Delta(t)=(a-b)^2t(t-2n)+n^2(a+b)^2.
\]
When \(0\le t\le2n\), the bound \(t(t-2n)\ge -n^2\) gives \(\Delta(t)\ge4n^2ab>0\). For \(t>2n\), both displayed contributions are nonnegative except neither can remove the positive second one. Thus every possible \(w\) is real, even at the linear degeneration \(t=2n\). All nonzero nonzero-intensity critical points are therefore on the asserted rays.

**2. Only the negative rays can carry noncentral maxima.** Write \(z=re^{i\theta}\), \(R=r^n\). On a positive ray \(e^{in\theta}=1\), away from zeros, the second angular derivative of \(\log H\) is
\[
2n^2R\left(\frac{a}{(R-a)^2}+\frac{b}{(R-b)^2}\right)>0.
\]
So no such point can be a local maximum. On a negative ray \(e^{in\theta}=-1\), the same derivative is
\[
-2n^2R\left(\frac{a}{(R+a)^2}+\frac{b}{(R+b)^2}\right)<0.
\]
The radial–angular mixed derivative vanishes on either ray. On a negative ray put \(t=r^2\); its log intensity is \(L(t)=-t+2\log(t^{n/2}+a)+2\log(t^{n/2}+b)\), with
\[
L'(t)=\frac{Q_{n,a,b}(t)}{t},\quad
Q_{n,a,b}(t)=n\left(\frac{t^{n/2}}{t^{n/2}+a}+\frac{t^{n/2}}{t^{n/2}+b}\right)-t.
\]
As \(t\downarrow0\), \(Q(t)<0\) since \(n>2\); as \(t\to\infty\), \(Q(t)<0\). Distinct radial maxima correspond to positive roots where \(Q\) changes sign from positive to negative.

**3. Universal four-root and two-peak bound.** Put \(u=\sqrt t\). For \(u>0\), the equation \(Q(u^2)=0\) is exactly the polynomial equation
\[
P_{n,a,b}(u)=u^{2n}-2n u^{2n-2}+(a+b)u^n-n(a+b)u^{n-2}+ab=0.
\]
Indeed \(u^2P(u)=-(u^n+a)(u^n+b)Q(u^2)\). Since \(n\ge3\), the five displayed monomials have distinct strictly descending degrees and alternating coefficient signs \(+,-,+,-,+\). Descartes' rule of signs (counting multiplicities) bounds positive roots by four. A continuous radial profile with at most four positive stationary points can have at most two interior local maxima when its derivative is negative near both endpoints; the same conclusion including degenerate maxima follows from alternating derivative-sign transitions. The \(n\) negative rays thus contribute at most \(2n\) local maxima. The origin contributes one: the expansion \(H(z)=a^2b^2(1-|z|^2+O(|z|^3))\) gives real Hessian \(-2a^2b^2I\). The only other critical points are the polynomial zeros, which are minima. This proves the universal \(2n+1\) bound.

**4. The exact order-eleven witness.** Take \(n=11\), \(a=50000\), \(b=4800000\). For the five positive rational radii
\[
u\in\left\{3,\frac72,\frac{37}{10},\frac{79}{20},\frac{81}{20}\right\},
\]
the signs of \(Q(u^2)\), computed by exact rational arithmetic, are respectively \(-,+,-,+,-\). There are four distinct positive zeros, one in each of the four successive intervals. Descartes' bound shows these are all the positive zeros and all are simple. The two positive-to-negative crossings are radially strict maxima; the negative angular Hessian makes them nondegenerate planar maxima on each of \(11\) negative rays. Together with the origin there are exactly \(23\).

**5. Every order at least twelve admits saturation.** For fixed \(n\ge12\), formally set \(a=0\) in the radial equation away from \(t=0\). Then \(Q_{n,0,b}(t)=n+n t^{n/2}/(t^{n/2}+b)-t\). Its zeros with \(n<t<2n\) are equivalent to
\[
b=B_n(t):=t^{n/2}\frac{2n-t}{t-n}.
\]
With \(x=t/n\), the sign of \(B'_n(t)\) is the sign of
\[
\frac{n}{2x}-\frac1{2-x}-\frac1{x-1}.
\]
The two critical values in \(1<x<2\) solve \(n(x-1)(2-x)=2x\), with discriminant \(n^2-12n+4>0\) for every integer \(n\ge12\). The first is a strict local minimum of \(B_n\), the second a strict local maximum. Choose \(b\) strictly between their values. Then \(Q_{n,0,b}\) has three distinct simple zeros in \((n,2n)\) (the three monotonic branches of \(B_n\)). For sufficiently small \(a>0\), these three simple roots persist by continuity; moreover \(Q_{n,a,b}(t)<0\) for all sufficiently small \(t>0\), but \(Q_{n,a,b}(n)>0\) for sufficiently small \(a\). Consequently there is a fourth positive zero in \((0,n)\). Descartes' bound makes these all simple, yielding two nondegenerate radial maxima on each negative ray. Strict inequalities and simple roots persist under small parameter perturbations, giving an open set of saturating \((a,b)\) for every \(n\ge12\). For the integer instance \(n=12\), \(a=1\), \(b=33800000\), the signs of \(P_{12,1,33800000}(\sqrt t)\) at \(t=0,1,15,16,18,19\) are \(+,-,-,+,-,+\), displaying all four positive roots without numerical approximation.

## Verification

The standalone script `two_ring_check.py`, requiring only Python 3 standard-library `fractions`, verifies the five exact rational signs for order eleven; all six exact integer signs for the order-twelve example; the discriminant identity and strict positivity on selected exact parameters; and the order-twelve values \(B_{12}(16)=33554432\), \(B_{12}(18)=34012224\). Running `python3 two_ring_check.py` prints `TWO_RING_MAXIMA_CERTIFICATE_PASS`. The all-order statements are proved analytically by the real-ray discriminant, Descartes' rule, the one-variable Hessian argument, and the construction for every \(n\ge12\), not by finite sampling.

## Relationship to prior work

Abreu (arXiv:2210.06721v1, 2022) introduces the Chern-stationarity equation \(F'-\overline zF=0\) and derives average critical-point and peak densities for random Gaussian entire functions. Chabaud, Markham, and Grosshans (arXiv:1907.11009v1, 2019) describe stellar polynomials through their Husimi-zero constellations. These establish the natural phase-space setting but their studied statements do not classify the deterministic two-concentric-polygon polynomial or provide the four-radius saturation construction. Single-ring regular-polygon intensities have only one noncentral maximum shell, whereas the two-factor model can have two simultaneously. This is a distinct exact peak-count problem, not a claim about the random-point intensities or the general stellar hierarchy.

## Limitations

The family requires two aligned, distinct regular \(n\)-gon zero rings and positive radial factors. No classification is claimed for rotated rings, three or more rings, general coefficients, or the optimal maxima count for \(3\le n\le10\). The upper bound is a family-specific bound, not a universal bound for arbitrary degree-\(2n\) polynomials. The result counts local maxima rather than computing their heights or global dominance. The originality assessment is a documented literature comparison, not a proof of absolute historical priority.

## References

1. L. D. Abreu, *Local maxima of white noise spectrograms and Gaussian Entire Functions*, arXiv:2210.06721v1 (public 2022-10-13), https://arxiv.org/html/2210.06721v1 .
2. U. Chabaud, D. Markham, F. Grosshans, *Stellar representation of non-Gaussian quantum states*, arXiv:1907.11009v1 (public 2019-07-25), https://arxiv.org/abs/1907.11009 .
3. Descartes' rule of signs, in its standard polynomial form (applied to \(P_{n,a,b}\)).
