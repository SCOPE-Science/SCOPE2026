# One disk-coverage crossover for moment-matched exponential and Gaussian dispersal in dimensions at least three

## Finding
For every integer \(d\ge 3\) and scale \(\ell>0\), compare the isotropic exponential dispersal density \(k_E\) and the isotropic Gaussian density \(k_G\) defined below. Both have the same mean squared displacement. There is exactly one finite, strictly positive radius \(R_d\) such that the two laws assign the same probability to the source-centered closed ball of radius \(R_d\). The exponential kernel assigns strictly *more* probability to every smaller nontrivial ball; the Gaussian assigns strictly more to every larger finite ball.

Writing \(R_d=\ell\rho_d\), the crossover is characterized uniquely by
\[
P(d,\rho_d)=P\!\left(\frac d2,\frac{\rho_d^2}{2(d+1)}\right),
\]
where \(P(a,z)=\Gamma(a)^{-1}\int_0^z t^{a-1}e^{-t}\,dt\) is the regularized lower incomplete gamma function. The dimension dependence obeys the sharp additive limit
\[
\boxed{\lim_{d\to\infty}(\rho_d-d)=\frac{4+3\sqrt2}{6}=1.373773447853\ldots.}
\]
This is a statement about ball-landing probabilities under *equal mean squared displacement*, not an empirical claim that either kernel is correct for any species.

## Assumptions and scope
Fix integer \(d\ge3\), positive length \(\ell\), and Euclidean norm \(\|x\|\) on \(\mathbb R^d\). Define probability density functions with respect to \(d\)-dimensional volume by
\[
k_E(x)=\frac{\Gamma(d/2)}{2\pi^{d/2}\Gamma(d)\ell^d}e^{-\|x\|/\ell},\qquad
k_G(x)=\frac{1}{[2\pi(d+1)\ell^2]^{d/2}}e^{-\|x\|^2/[2(d+1)\ell^2]}.
\]
Their radial distributions are respectively \(\|X_E\|/\ell\sim\operatorname{Gamma}(d,1)\) (shape, scale) and \(\|X_G\|^2/[(d+1)\ell^2]\sim\chi^2_d\). Thus \(\mathbb E\|X_E\|^2=\mathbb E\|X_G\|^2=d(d+1)\ell^2\). The ball probabilities are \(F_E(R)=P(d,R/\ell)\) and \(F_G(R)=P(d/2,R^2/[2(d+1)\ell^2])\). Only source-centered balls and ideal, normalized isotropic densities are asserted; the statement does not address shifted patches, survival after arrival, empirical kernel fitting, or dimensions one and two.

## Proof
**Step 1 (exact radial-density crossing census).** Rescale \(\ell=1\). The ratio of radial densities (equivalently, spatial densities at the same radius) is
\[
\frac{f_G(r)}{f_E(r)}=C_d\exp\!\left(r-\frac{r^2}{2(d+1)}\right),\quad
C_d=\frac{2\Gamma(d)}{\Gamma(d/2)[2(d+1)]^{d/2}}.
\]
Its logarithm is a strictly concave quadratic, tends to \(-\infty\) at infinity, and has its maximum at \(r=d+1\). The two radial distributions have equal total probability and equal second moment. If \(\log C_d\ge0\), the ratio would be at least one near the origin and would switch sign relative to one at most once, from above to below. Since \(\int_0^\infty(f_G-f_E)\,dr=0\), multiplying the difference by \(r^2-r_0^2\), where \(r_0\) is its only crossing, would imply \(\int_0^\infty r^2(f_G-f_E)\,dr<0\), contradicting equality of the second moments. The case of no crossing contradicts probability normalization. Thus \(\log C_d<0\). If the quadratic's maximum were nonpositive, then \(f_G\le f_E\) everywhere with strict inequality on a set of positive measure, again contradicting normalization. Therefore its maximum is strictly positive and there are precisely two positive density crossings:
\[
a_d=(d+1)-\sqrt{(d+1)^2+2(d+1)\log C_d},\qquad
b_d=(d+1)+\sqrt{(d+1)^2+2(d+1)\log C_d}.
\]
The sign of \(f_E-f_G\) is positive on \((0,a_d)\), negative on \((a_d,b_d)\), and positive on \((b_d,\infty)\).

**Step 2 (one ball crossover, with strict inequalities).** Put \(H_d(r)=F_E(r)-F_G(r)\). Then \(H_d(0)=0\), \(H_d'=f_E-f_G\), and \(H_d(r)\to0\) as \(r\to\infty\). Therefore \(H_d(a_d)>0\). Also \(H_d(b_d)=-\int_{b_d}^{\infty}(f_E-f_G)\,dr<0\). As \(H_d\) strictly decreases on \((a_d,b_d)\), it has precisely one zero \(\rho_d\) in that interval. It is strictly positive for \(0<r<\rho_d\) and strictly negative for every finite \(r>\rho_d\). Scale restoration proves existence and uniqueness for every \(\ell>0\).

**Step 3 (high-dimensional additive constant).** We use the central Gamma expansion, valid uniformly for any fixed bounded real \(u\):
\[
P(n,n+u)=\frac12+\frac{1}{\sqrt{2\pi n}}\left(u+\frac13\right)+O(n^{-1})\quad(n\to\infty).
\]
This follows by setting \(t=n+z\sqrt n\) in the Gamma density, applying Stirling's formula and expanding the normalized density as \(\phi(z)[1+(z^3-3z)/(3\sqrt n)]+O(n^{-1})\) in the central region. Integration gives the displayed coefficient, since \(\int_{-\infty}^0(z^3-3z)\phi(z)\,dz=\phi(0)\); standard Gamma Chernoff bounds control the discarded outer tails and make the remainder uniform for bounded \(u\). The calculation holds for integer or half-integer \(n\).

For every fixed bounded \(c\), evaluate the two CDFs at \(r=d+c\). The expansion with shape \(d\) gives
\[
F_E(d+c)=\frac12+\frac{\phi(0)}{\sqrt d}\left(c+\frac13\right)+O(d^{-1}).
\]
The Gaussian ball CDF equals \(P(d/2,(d+c)^2/[2(d+1)])\), and its Gamma argument equals \(d/2+(2c-1)/2+O(d^{-1})\), giving
\[
F_G(d+c)=\frac12+\frac{\phi(0)}{\sqrt d}\sqrt2\left(c-\frac16\right)+O(d^{-1}).
\]
Consequently,
\[
\sqrt d\,H_d(d+c)=\phi(0)\left[(1-\sqrt2)c+\frac13+\frac{\sqrt2}{6}\right]+O(d^{-1/2}).
\]
The bracket has one simple zero at \(c_*=(4+3\sqrt2)/6\), positive below and negative above. For each fixed \(\varepsilon>0\), the uniqueness and sign from Step 2 place \(\rho_d\) between \(d+c_*-\varepsilon\) and \(d+c_*+\varepsilon\) for all sufficiently large \(d\). Thus \(\rho_d-d\to c_*\), as claimed. This asymptotic needs no claim of monotonicity in dimension.

## Verification
`checker.py` computes Gamma and chi-square CDFs independently using SciPy, evaluates both density crossing points and the unique CDF crossing for dimensions \(3\le d\le500\), checks strict signs at multiple interior/exterior radii, and tests the asymptotic offset at six increasing dimensions. The diagnostic run reported 10,963 passed assertions. In particular, the observed dimension-three crossover is \(\rho_3\approx4.376639497882\); the dimension-100 crossover is \(\rho_{100}\approx101.373956103046\). These are numerical tests only; Steps 1–3 above establish the infinite theorem. Reproduce with `python checker.py` after installing SciPy (version 1.9 or later).

## Relationship to prior work
Skelsey, With, and Garrett (2012, online publication 27 September 2012) directly compare exponential and Gaussian *spatial dispersal kernels* and investigate their landscape-scale effects. Their chosen plotted scale parameters do not enforce the particular equal-mean-squared-displacement normalization here; their analysis does not establish one CDF crossing in every dimension \(d\ge3\), nor an additive high-dimensional correction. Winskill et al. (2015, online publication 10 November 2015) distinguish the spatial kernel from its radial-distance density and use cumulative displacement fractions for mosquitoes; they do not derive the present matched-moment comparison.

The lower-dimensional one-crossing phenomenon must not be counted as new here: an existing planar Brownian-retention, Gaussian-scale-mixture result already covers the planar case, and a separate standardized-exponential/Gaussian central-mass comparison addresses a different probability event. The present scientific claim is strictly the higher-dimensional \(d\ge3\) theorem together with its explicit dimension-dependent location and additive limit. Existing kernel definitions alone are not a theorem of unique ball-probability ordering; all required implications are proved above.

## Limitations
No application-specific dispersal scale is estimated. The comparison concerns centered balls, not shifted or heterogeneous habitats, and the high-dimensional asymptotic is a structural mathematical result rather than a biologically realizable spatial dimension. Empirical kernels may be neither Gaussian nor radial exponential. The assertion of originality is limited to inspected evidence and available comparisons; historical-priority verification is not independent and other higher-dimensional stochastic-order literature may contain an equivalent result. The diagnostic program checks finitely many dimensions and cannot certify the analytical claims.

## References
1. Skelsey, P., With, K. A., and Garrett, K. A. (2012). *Why dispersal should be maximized at intermediate scales of heterogeneity*. Theoretical Ecology. First published online 27 September 2012. https://doi.org/10.1007/s12080-012-0171-3
2. Winskill, P., et al. (2015). *Dispersal of Engineered Male Aedes aegypti Mosquitoes*. PLOS Neglected Tropical Diseases. Published 10 November 2015. https://doi.org/10.1371/journal.pntd.0004156
