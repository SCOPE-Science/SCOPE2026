# Exactly two arrival-fraction reversals between moment-matched Gamma and inverse-Gaussian residence clocks

## Finding
Let two positive transit-time laws have the same mean \(\mu>0\) and squared coefficient of variation \(v>0\). Model one by \(X\sim\mathrm{Gamma}(1/v,\mu v)\), with the second parameter a **scale**, and the other by \(Y\sim\mathrm{IG}(\mu,\mu/v)\), with the second parameter the usual inverse-Gaussian shape \(\lambda\). Write their cumulative distribution functions as \(F_\Gamma\) and \(F_{\mathrm{IG}}\).

There exist exactly two distinct times \(0<t_-(\mu,v)<t_+(\mu,v)<\infty\) at which \(F_\Gamma(t)=F_{\mathrm{IG}}(t)\). Both are genuine sign changes, with
\[
F_\Gamma(t)-F_{\mathrm{IG}}(t)\begin{cases}>0,&0<t<t_-,\\<0,&t_-<t<t_+,\\>0,&t>t_+.\end{cases}
\]
The **densities** cross exactly three times; each cumulative crossing is bracketed by successive density crossings. All thresholds scale linearly with \(\mu\). As \(v\downarrow0\), the cumulative crossing locations obey
\[
\frac{t_\pm(\mu,v)}{\mu}=1\pm\sqrt v+o(\sqrt v).
\]
Thus matching **both** the mean and variance does not make the modeled fraction of material arriving before a specified deadline comparable in a single direction: the preference changes exactly twice.

## Assumptions and scope
The laws are positive, continuous, unshifted, normalized probability distributions, with finite \(\mu>0\) and \(v>0\); they are an idealized comparison of parametric residence-time transfer kernels, not a transport-equation equivalence for arbitrary flow fields. The Gamma density is \(f_\Gamma(t)=t^{1/v-1}e^{-t/(\mu v)}/[\Gamma(1/v)(\mu v)^{1/v}]\). The inverse-Gaussian density is
\[
f_{\mathrm{IG}}(t)=\sqrt{\frac{\mu/v}{2\pi t^3}}\exp\left[-\frac{(\mu/v)(t-\mu)^2}{2\mu^2t}\right].
\]
Both have expectation \(\mu\) and variance \(\mu^2v\). For normalized time \(x=t/\mu\), define \(g_v\) and \(h_v\) as their corresponding mean-one densities and \(H_v(x)=\int_0^x(g_v(u)-h_v(u))\,du\). The roots of \(H_v\) claimed above are strictly positive, finite, and interior; the trivial limiting equalities at zero and infinity are not counted.

## Proof
**1. Normalize and count possible density crossings.** Scaling time by \(\mu\) reduces to the mean-one laws. Their logarithmic density ratio \(L_v(x)=\log[g_v(x)/h_v(x)]\) satisfies the exact identity
\[
L_v'(x)=\frac{-x^2+(2+v)x-1}{2vx^2}.
\]
Its numerator has two distinct positive roots
\[
a_v=\frac{2+v-\sqrt{v(v+4)}}2,\qquad b_v=\frac{2+v+\sqrt{v(v+4)}}2,
\]
with \(0<a_v<1<b_v\) and \(a_vb_v=1\). Therefore \(L_v\) decreases, then increases, then decreases, so \(g_v-h_v\) has at most three distinct sign changes (and at most three distinct roots) on \((0,\infty)\). Direct tail comparison gives \(L_v(x)\to+\infty\) as \(x\downarrow0\) and \(L_v(x)\to-\infty\) as \(x\to\infty\).

**2. Matching moments forces three density sign changes.** Since both densities have total mass one, mean one, and second raw moment \(1+v\),
\[
\int_0^\infty x^j[g_v(x)-h_v(x)]\,dx=0\quad(j=0,1,2).
\]
If the continuous nonzero difference had at most two sign changes, choose a polynomial \(P\) of degree at most two whose simple roots are exactly those sign-change positions, with overall sign chosen so that \(P(x)[g_v(x)-h_v(x)]\ge0\) everywhere. The product is strictly positive on an open set, so its integral is positive; but moment orthogonality says that integral is zero. Contradiction. Hence exactly three simple density crossings \(0<c_1<c_2<c_3\) occur with the signs \(+,-,+,-\) on the four intervals.

**3. Count cumulative crossings.** The derivative \(H_v'=g_v-h_v\) has signs \(+,-,+,-\). Thus \(H_v\) is positive on \((0,c_1]\). Since \(H_v(\infty)=0\) and it decreases toward zero on \((c_3,\infty)\), it is also strictly positive on \([c_3,\infty)\). Equality of means gives the integral identity
\[
\int_0^\infty H_v(x)\,dx=\mathbb E[Y/\mu]-\mathbb E[X/\mu]=0.
\]
It follows that \(H_v\) is negative somewhere (otherwise its strictly positive tails make this integral positive). Its unique minimum over \([c_1,c_3]\) is attained at \(c_2\). The strict monotonic decrease on \((c_1,c_2)\) and increase on \((c_2,c_3)\) therefore give exactly one root on each interval. This proves the signs, strictness, root count, and density-root bracketing, for every real \(v>0\).

**4. Concentrated-law cutoff positions.** Put \(s=\sqrt v\), \(x=1+sz\), and let \(\phi,\Phi\) be the standard-normal density and CDF. Direct Taylor expansion of the two normalized densities, using Stirling's formula for \(\Gamma(s^{-2})\), gives for bounded \(z\)
\[
\begin{aligned}
s g_{s^2}(1+sz)&=\phi(z)\left[1+\frac{s}{3}(z^3-3z)\right]+O(s^2),\\
s h_{s^2}(1+sz)&=\phi(z)\left[1+\frac{s}{2}(z^3-3z)\right]+O(s^2).
\end{aligned}
\]
To justify integrating these expansions, first restrict to \(|z|\le s^{-1/12}\), where the Taylor remainder is bounded by an integrable Gaussian times \(Cs^2(1+|z|^6)\); outside that interval, Chernoff bounds for the two moment-generating functions give probabilities \(o(s^2)\). Integrating \((z^3-3z)\phi(z)\), whose antiderivative is \((1-z^2)\phi(z)\), yields uniformly on compact \(z\)-sets
\[
H_{s^2}(1+sz)=\frac{s}{6}(z^2-1)\phi(z)+O(s^2).
\]
For every fixed \(\epsilon\in(0,1)\), the leading term has opposite strict signs at \(-1-\epsilon\) and \(-1+\epsilon\), and likewise at \(1-\epsilon\) and \(1+\epsilon\). By the already proved existence of exactly two cumulative roots, those roots must lie in the indicated respective brackets for all sufficiently small \(s\). Thus their standardized positions converge to \(-1\) and \(+1\).

## Verification
A standalone diagnostic program, `check_gamma_ig.py`, computes density crossings from the logarithmic-ratio derivative brackets and cumulative crossings from the density-crossing brackets. Running `python check_gamma_ig.py` with Python 3, NumPy, and SciPy passed 128 explicit assertions for 15 values of squared coefficient of variation between \(0.005\) and \(40\), and four additional small-variance asymptotic checks. (The reported total 128 includes all assertions from both sets.) For \(\mu=1,v=1\), the two numerical cumulative cutoffs are approximately \(0.6247192703\) and \(3.3572949772\). These numerical checks are *diagnostic*, not a proof of the universal claims; Steps 1–4 above supply that proof.

## Relationship to prior work
McGuire et al. (2005) discuss Gamma and advective-dispersion residence-time models as alternative transfer functions. Starn and Belitz (2018) fit Gamma and inverse-Gaussian parametric residence-time distributions to modeled groundwater particle residence times; they do not provide the above moment-matched, all-variance CDF crossing classification in the examined methodological and discussion sections. Colonius's published probability-chapter excerpt displays Gamma and inverse-Gaussian densities with the same mean and standard deviation; its figure provides a strong prior visual comparison, **not** a verified uniqueness theorem for exactly two cumulative intersections for every squared coefficient of variation. Giner and Smyth (2016) provide stable inverse-Gaussian probability calculations, rather than this comparison theorem. Classical density-crossing and moment orthogonality ideas are used, not claimed as new. General stochastic-order literature may contain stronger results that imply this statement; historical priority remains provisional.

## Limitations
The result is for one common mean and variance, without shifts, multimodal mixtures, recharge weighting, time-varying hydraulic conditions, adsorption, or measurement noise. No empirical superiority of either residence model is asserted. The first two moments alone do not identify the correct physical residence law. The three density crossings and two cumulative crossings are proved exactly; the supplied floating-point values and the checker cannot certify every parameter numerically. The small-variance expansion is asymptotic for fixed standardized thresholds, not a uniform bound over all times. An independent literature and proof audit has not been performed.

## References
- K. J. McGuire et al., “The role of topography on catchment-scale water residence time,” *Water Resources Research* 41 (2005), doi:10.1029/2004WR003657. First published 2005-05-03. https://doi.org/10.1029/2004WR003657
- J. J. Starn and K. Belitz, “Regionalization of groundwater residence time using metamodeling,” *Water Resources Research* 54 (2018), doi:10.1029/2017WR021531. https://doi.org/10.1029/2017WR021531
- H. Colonius, “Selected concepts from probability,” in *New Handbook of Mathematical Psychology*, Cambridge University Press, publisher excerpt, Fig. 1.2. https://assets.cambridge.org/97811070/29088/excerpt/9781107029088_excerpt.pdf
- G. Giner and G. K. Smyth, “statmod: Probability calculations for the inverse Gaussian distribution,” *The R Journal* 8(1) (2016). https://journal.r-project.org/articles/RJ-2016-024/
