# A fixed-information, vanishing-rank-dependence law for normal-mode copulas

## Finding

Fix any real amplitude \(0<\theta<1\). For every pair of positive integers \(m,n\), define the normal-mode copula and its density by
\[
C_{m,n,\theta}(u,v)=uv+\frac{\theta}{mn\pi^2}\sin(m\pi u)\sin(n\pi v),\qquad
c_{m,n,\theta}(u,v)=1+\theta\cos(m\pi u)\cos(n\pi v).
\]
The density is strictly positive and all its density-value divergences from the independence copula are independent of the two mode numbers. In particular, writing \(P_{m,n,\theta}\) for the associated joint law and \(\Pi\) for independent uniform marginals,
\[
\begin{aligned}
\operatorname{TV}(P_{m,n,\theta},\Pi)&=\frac{2\theta}{\pi^2},\\
\chi^2(P_{m,n,\theta}\Vert\Pi)&=\frac{\theta^2}{4},\\
D_{\mathrm{KL}}(P_{m,n,\theta}\Vert\Pi)&=I(\theta)
=\sum_{j=1}^{\infty}\frac{\theta^{2j}}{(2j)(2j-1)}
\left(\frac{\binom{2j}{j}}{4^j}\right)^2>0.
\end{aligned}
\]
By contrast, the two population Chatterjee directional rank coefficients have the exact frequency laws
\[
\boxed{\xi(V\mid U)=\frac{3\theta^2}{2n^2\pi^2},\qquad
\xi(U\mid V)=\frac{3\theta^2}{2m^2\pi^2}.}
\]
Consequently, along \(m=n=2k\) as \(k\to\infty\), both directional rank coefficients tend to zero at the exact inverse-square rate, while total variation, chi-square divergence, and mutual information stay at fixed strictly positive values. Moreover, both Spearman's rho and Kendall's tau vanish **exactly** for every such copula, and
\[
\|C_{2k,2k,\theta}-\Pi\|_\infty=\frac{\theta}{4k^2\pi^2}\longrightarrow0.
\]
Thus no strictly positive lower bound for either directional population rank coefficient can depend on mutual information or total-variation distance alone, even among strictly positive smooth copula densities uniformly bounded above by \(1+\theta\) and below by \(1-\theta\).

## Assumptions and scope

All statements concern bivariate copulas on \([0,1]^2\) with uniform margins; \(m,n\in\mathbb{N}\) are positive integer frequencies and \(0<\theta<1\) is held fixed across comparisons. The independent reference law \(\Pi\) has density one. Total variation is half the \(L^1\) density discrepancy. The Pearson chi-square divergence is \(\int(c-1)^2\), and mutual information is \(\int c\log c\), with integrals over the unit square and natural logarithms.

For any continuous convex \(f\) with \(f(1)=0\), the corresponding forward \(f\)-divergence is \(\int f(c_{m,n,\theta})\). The claim of invariance extends to every measurable function of the density for which the integral exists, and therefore to all such finite \(f\)-divergences. The directional coefficient \(\xi(V\mid U)\) is the population measure of predictability of the response \(V\) from \(U\), not the finite-sample statistic.

## Proof

**1. Copula validity and a distributional identity.** The mixed derivative of the asserted formula is exactly \(c_{m,n,\theta}\). Since \(|\cos|\le1\) and \(0<\theta<1\),
\[
1-\theta\le c_{m,n,\theta}(u,v)\le1+\theta.
\]
Integrating the cosine perturbation over either coordinate gives zero, so both margins are uniform; the boundary conditions follow from the sine factors. Thus every displayed \(C_{m,n,\theta}\) is a strictly positive smooth copula.

For a uniform \(U\) on \([0,1]\), \(\cos(m\pi U)\) has the same arcsine distribution as \(\cos(\pi U)\), for every positive integer \(m\): each consecutive half-wave has the same pushforward distribution after reflection. Thus for independent uniform coordinates \(U,V\), and every integrable Borel \(h\),
\[
\int_0^1\!\int_0^1 h(c_{m,n,\theta}(u,v))\,du\,dv
=\frac1{\pi^2}\int_0^\pi\!\int_0^\pi
h(1+\theta\cos s\cos t)\,ds\,dt.
\]
This equality is independent of both mode numbers. Taking \(h=f\) proves the asserted full family of divergence invariances, without presuming any particular divergence formula.

**2. Exact information quantities.** Since \(\int_0^1|\cos(m\pi u)|\,du=2/\pi\), the total-variation identity follows. Since \(\int_0^1\cos^2(m\pi u)\,du=1/2\), the chi-square identity follows. To compute mutual information, put \(Z=\cos(m\pi U)\cos(n\pi V)\). Because \(|\theta Z|\le\theta<1\), the expansion
\[
(1+x)\log(1+x)=x+\sum_{r=2}^\infty\frac{(-1)^r x^r}{r(r-1)}
\]
converges absolutely and uniformly on the range of \(\theta Z\). Odd moments of each cosine vanish and, for every \(j\ge1\),
\[
\mathbb E\bigl[\cos^{2j}(m\pi U)\bigr]=\frac{\binom{2j}{j}}{4^j}.
\]
Integrating term by term gives the displayed nonnegative series for \(I(\theta)\). Its first term is strictly positive, so \(I(\theta)>0\).

**3. Directional rank coefficients.** Differentiating the copula in its first coordinate yields the conditional distribution function of \(V\) given \(U=u\):
\[
F_{V\mid U=u}(v)=\partial_u C_{m,n,\theta}(u,v)
=v+\frac{\theta}{n\pi}\cos(m\pi u)\sin(n\pi v).
\]
For uniform response margins, the population Chatterjee coefficient has the normalized conditional-CDF representation
\[
\xi(V\mid U)=6\int_0^1\!\int_0^1
\bigl(F_{V\mid U=u}(v)-v\bigr)^2\,du\,dv.
\]
Insert the preceding formula and use the exact cosine-square and sine-square integrals (both \(1/2\)); this gives \(3\theta^2/(2n^2\pi^2)\). Exchanging the two coordinates proves \(\xi(U\mid V)=3\theta^2/(2m^2\pi^2)\).

**4. Sharp separation and vanishing concordance.** For \(m=n=2k\), the last two formulas give \(\xi(V\mid U)=\xi(U\mid V)=3\theta^2/(8k^2\pi^2)\). The mutual-information and total-variation values remain the strictly positive constants from Step 2. The exact supremum of the CDF correction is \(\theta/(mn\pi^2)\), because the two sine factors independently attain absolute value one in the square. Finally, Spearman's rho is \(12\int(C-uv)\), which vanishes if either sine mode has even frequency. Kendall's tau is \(4\int Cc-1\); the linear perturbation terms integrate to zero for even frequencies, and its quadratic term factors through \(\int_0^1\sin(m\pi u)\cos(m\pi u)\,du=0\). Hence both concordance coefficients are exactly zero along the even-even sequence. This completes the proof.

## Verification

An independently runnable Python script, `verify.py`, evaluates all five quantities by direct midpoint quadrature on six frequency pairs at \(\theta=1/2\), compares against the analytical formulas, and checks convergence of the information series. Running `python3 verify.py` in the same folder prints six rows and a final `PASS` line. The script uses the Python standard library only. The calculations corroborate the formulas but are **not** substituted for the all-frequency analytical arguments above.

For example, \(I(1/2)\approx0.03203926887\) nats and \(\operatorname{TV}=1/\pi^2\approx0.10132118364\), independent of mode frequencies. At \((m,n)=(2,4)\), the corresponding two rank coefficients are approximately \(0.00237471524\) and \(0.00949886097\), illustrating directional asymmetry at fixed information.

## Relationship to prior work

Chesneau (2021) discusses the trigonometric copula construction. Fukumoto (2023, with a corresponding 2024 journal article) develops normal-mode copulas, their nonmonotonic dependence, and classical rank associations. In particular, the zero Spearman/Kendall coefficients at even frequencies are **prior results**, not claimed here as new. Chatterjee (2021) gives the general directional rank-dependence functional. The contribution here is the joint exact frequency-invariance theorem for all density-value divergences, the two directional Chatterjee formulas, and their fixed-information vanishing-rank consequence in this same published model. General existence of dependent zero-concordance copulas does not establish the fixed-information separation.

Searches for normal-mode copulas, Sarmanov Fourier copulas, conditional-CDF rank dependence, information invariance, and related general dependence constraints revealed no directly covering calculation among accessible primary sources and indexed mathematical records. This is a best-knowledge priority assessment, not a claim of exhaustive literature coverage.

## Limitations

The proof fixes \(\theta\in(0,1)\) and positive integer frequencies, and concerns population coefficients only. It does not establish finite-sample power or sample-size rates for a rank test against rapidly oscillating alternatives. The densities are smooth individually and uniformly bounded, but their derivatives are not uniformly bounded in frequency. The limiting copulas converge uniformly to independence while their joint distributions do not converge in total variation. The exact formulas are established here analytically; independent mathematical audit and comprehensive historical-priority certification have not been performed.

## References

1. C. Chesneau, *On New Types of Multivariate Trigonometric Copulas*, AppliedMath **1** (2021), 3–17. https://doi.org/10.3390/appliedmath1010002 (public 14 December 2021).
2. K. Fukumoto, *Not Linearly Correlated, But Dependent: A Family of Normal Mode Copulas*, arXiv:2308.03541 (posted 7 August 2023). https://arxiv.org/abs/2308.03541.
3. K. Fukumoto, *Normal Mode Copulas for Nonmonotonic Dependence*, Political Analysis **32** (2024), 417–430. https://doi.org/10.1017/pan.2023.45.
4. S. Chatterjee, *A New Coefficient of Correlation*, J. Amer. Statist. Assoc. **116** (2021), 2009–2022. https://doi.org/10.1080/01621459.2020.1758115.
5. J. Ansari and M. Rockel, *The exact region and an inequality between Chatterjee's and Spearman's rank correlations*, J. Multivariate Analysis **214** (2026), article 105630. https://doi.org/10.1016/j.jmva.2026.105630.
