# Sharp cube-root bounds for resource-limited flowering windows

## Finding

For every effective floral-display budget \(B>0\) and phenological timing scale \(\sigma>0\), suppose a single pollinator opportunity occurs at time \(T\sim N(0,\sigma^2)\). A flowering schedule consists of one freely placed interval \([c-w,c+w]\) with half-width \(w>0\). Display intensity is uniform over this interval and has total budget \(B\), hence intensity \(B/(2w)\). Conditional on the opportunity falling inside the interval, the probability of successful contact is the saturating Poisson response \(1-\exp[-B/(2w)]\); outside it is zero. The expected-success score is

\[
S(c,w)=\left(1-e^{-B/(2w)}\right)\int_{c-w}^{c+w}\frac{e^{-t^2/(2\sigma^2)}}{\sqrt{2\pi}\sigma}\,dt.
\]

There is **exactly one globally optimal schedule**: its center is \(c_*=0\), and its positive half-width \(w_*\) is the unique solution, with \(y=w_*/\sigma\) and \(k=B/(2\sigma)\), of

\[
\frac{y e^{-y^2/2}}{\int_0^y e^{-u^2/2}\,du}
=\frac{k/y}{e^{k/y}-1}.
\]

Its half-width is strictly increasing with \(B\), and it obeys the **strict, sharp, global cube-root enclosure**

\[
\boxed{\left(\frac{3B\sigma^2}{4}\right)^{1/3}<w_*<(B\sigma^2)^{1/3}}.
\]

The constants are simultaneously best possible over positive budgets: \(w_*^3/(B\sigma^2)\to3/4\) as \(B/\sigma\to0\), and \(w_*^3/(B\sigma^2)\to1\) as \(B/\sigma\to\infty\). Thus the high- and low-budget optimal half-widths both obey cube-root scaling, with different sharp coefficients. The ratio of the upper to lower bound is only \((4/3)^{1/3}\).

## Assumptions and scope

The scheduling class is **one contiguous interval**, freely centered on the real-time axis, of arbitrary finite positive length. Display is uniform *within* that interval and fixed in total; only its center and length may be chosen. The effective contact probability is exactly the stated Poisson saturation function and does not itself depend on time inside the interval. The Gaussian opportunity time and total display budget are model inputs, not inferred quantities. Results quantify an idealized probabilistic service score, not measured seed production or an empirically calibrated flowering recommendation.

## Proof

**1. Optimal center.** At any fixed \(w>0\), the Gaussian mass in \([c-w,c+w]\) has derivative \(f_\sigma(c+w)-f_\sigma(c-w)\) in \(c\), where \(f_\sigma\) is even and strictly decreases as \(|t|\) increases. This derivative is strictly negative for \(c>0\), strictly positive for \(c<0\). The multiplicative saturation factor is positive and independent of \(c\), so \(c=0\) is the unique maximizing center.

**2. Unique optimal width.** Set \(y=w/\sigma\), \(k=B/(2\sigma)\), and \(I(y)=\int_0^y e^{-u^2/2}\,du\). Up to a positive constant the centered objective is \(F_k(y)=(1-e^{-k/y})I(y)\). Define

\[
R(y)=\frac{yI'(y)}{I(y)},\qquad h(z)=\frac{z}{e^z-1}.
\]

Direct differentiation gives

\[
\frac{d}{dy}\log F_k(y)=\frac{R(y)-h(k/y)}{y}.
\]

With \(a=y^2/2\), substitution in the Gaussian integral yields

\[
R(y)^{-1}=\int_0^1 e^{a(1-u^2)}\,du,
\qquad h(z)^{-1}=\int_0^1 e^{zu}\,du.
\]

The first integral strictly increases with \(y\); the second strictly increases with \(z\). Consequently \(R(y)\) strictly decreases from \(1\) to \(0\) as \(y\) runs from \(0\) to \(\infty\), whereas \(h(k/y)\) strictly increases from \(0\) to \(1\). There is exactly one crossing, and the derivative is positive before and negative after it. This crossing is the unique global maximum since \(F_k(y)\to0\) at both ends. Increasing \(k\) strictly lowers \(h(k/y)\) at fixed \(y\), hence strictly increases the unique maximizing \(y\).

**3. Sharp universal enclosure.** Let \(U\) be uniform on \([0,1]\) and set \(X=1-U^2\). The first-order equation is

\[
\mathbb E[e^{aX}]=\mathbb E[e^{zU}],\qquad a=y^2/2,\quad z=k/y.
\]

The quantile functions of \(X\) and \(U\) are \(Q_X(s)=2s-s^2\) and \(Q_U(s)=s\), respectively. As \(Q_X(s)>Q_U(s)\) for every \(0<s<1\), strict stochastic dominance gives \(\mathbb E[e^{aX}]>\mathbb E[e^{aU}]\) for \(a>0\). Since the latter expectation strictly increases in its exponent, equality forces \(z>a\).

For the reverse bound define \(Y=4U/3\). Both \(X\) and \(Y\) have mean \(2/3\), and their lower quantiles satisfy, for every \(0<s<1\),

\[
\int_0^s[Q_X(u)-Q_Y(u)]\,du=\frac{s^2(1-s)}3>0.
\]

This implies \(X\) is **strictly smaller than \(Y\) in convex order**. For completeness, the quantile integral condition implies all upper-tail quantile integrals for \(X\) are smaller than those for \(Y\); maximizing \(\int_s^1 Q(u)\,du-(1-s)t\) over \(s\) gives \(\mathbb E[(X-t)_+]\le\mathbb E[(Y-t)_+]\) for every \(t\). Equal means and the integral representation of convex functions by affine functions and positive-part hinges establish the convex-order inequality. Strictness for the exponential follows because the distributions differ and its second derivative is strictly positive. Therefore \(\mathbb E[e^{aX}]<\mathbb E[e^{aY}]=\mathbb E[e^{(4a/3)U}]\), so equality forces \(z<4a/3\).

Together \(a<z<4a/3\) is \(y^3/2<k<2y^3/3\), equivalently

\[
(3k/2)^{1/3}<y<(2k)^{1/3}.
\]

Substituting \(k=B/(2\sigma)\) and \(y=w/\sigma\) proves the asserted physical bounds.

**4. Optimality of both constants.** When \(k\to0\), the enclosure forces \(y\to0\) and hence \(a,z\to0\). Taylor expansion of the equality of exponential moments gives \((2/3)a+O(a^2)=(1/2)z+O(z^2)\), and the enclosure keeps \(z/a\) bounded, so \(z/a\to4/3\). It follows that \(y^3/k\to3/2\). When \(k\to\infty\), the enclosure forces \(y,a,z\to\infty\). For any random variable supported on \([0,1]\) with essential supremum \(1\), \(\lim_{t\to\infty}t^{-1}\log\mathbb E[e^{tX}]=1\); applying this to both \(X\) and \(U\) in the moment equality and using \(1<z/a<4/3\) gives \(z/a\to1\), hence \(y^3/k\to2\). Converting back gives the sharp ratios \(3/4\) and \(1\).

## Verification

The analytic proof covers every \(B>0\), \(\sigma>0\), all real centers and all positive half-widths in the specified uniform-display class. Run `python3 check.py` with Python 3 and no third-party dependencies. The verifier compares the signed optimality equation, strict cube-root brackets, monotonicity, off-optimum scores, Gaussian center rearrangement and the exact quantile-integral identity over a parameter grid. It reports 6,232 supplementary checks; these finite computations do **not** establish the universal theorem. High-precision independent calculations at dimensionless budgets \(k\in\{10^{-12},10^{-6},1,10^6,10^{12}\}\) yield normalized ratios \(y^3/k\) approaching \(3/2\) and \(2\), consistent with the exact limit proofs. At \(k=1\), \(y_*=1.15529880799\ldots\) and \(S(0,w_*)=0.435570340282\ldots\).

## Relationship to prior work

Austin et al. (2024) document extension of species-level flowering durations and altered community co-flowering, using historical flowering records and quantile regressions; they do not optimize a resource-limited interval. Blasi et al. (2022) use saturating exponential functions for pollination potential in a spatially explicit bee-population simulation; their stated equation, dynamical inputs and objective are different. Ishii and Sakai (2001) discuss how floral longevity and blooming schedule jointly determine display size, but do not provide this Gaussian-window theorem. Lindh et al. (2016) optimize a switch from vegetative to reproductive growth in annual plants rather than a finite-length uniform-display window. Glaum et al. (2021) model network-level specialization via phenological resource overlap and adaptive foraging; the displayed model description uses time-modulated mutualism dynamics, not this one-event Gaussian optimization. The convex-order and Gaussian rearrangement tools are standard mathematics; the claim is their exact combination for the stated ecological benchmark, with best-possible universal coefficients. This comparison does not establish worldwide priority.

## Limitations

The theorem does not establish optimality among disjoint/multiple flowering periods, arbitrary time-varying display, non-Gaussian opportunity distributions, finite calendar boundaries, dependence between opportunity time and display response, or coupled population dynamics. The single-opportunity Gaussian and saturating conditional-contact models are idealizations. Source coverage and mathematical priority are necessarily provisional; no independent external mathematical audit has been performed.

## References

1. Austin, M. W., et al. (2024). *Climate change increases flowering duration, driving phenological reassembly and elevated co-flowering richness.* New Phytologist. First published 2024-07-24. https://doi.org/10.1111/nph.19994
2. Blasi, M., et al. (2022). *A model of wild bee populations accounting for spatial heterogeneity and climate-induced temporal variability of food resources at the landscape level.* Ecology and Evolution. https://doi.org/10.1002/ece3.9014
3. Ishii, H. S., and Sakai, S. (2001). *Effects of display size and position on individual floral longevity in racemes of Narthecium asiaticum (Liliaceae).* Functional Ecology. https://doi.org/10.1046/j.1365-2435.2001.00536.x
4. Lindh, M., et al. (2016). *Constrained growth flips the direction of optimal phenological responses among annual plants.* New Phytologist. https://doi.org/10.1111/nph.13706
5. Glaum, P., et al. (2021). *Phenology and flowering overlap drive specialisation in plant–pollinator networks.* Ecology Letters. https://doi.org/10.1111/ele.13884
