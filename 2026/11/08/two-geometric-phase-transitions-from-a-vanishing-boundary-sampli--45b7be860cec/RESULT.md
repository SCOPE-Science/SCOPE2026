# Two geometric phase transitions from a vanishing boundary sampling density

## Finding
Let \(K\subset\mathbb R^2\) be a strictly convex compact body with \(C^3\) boundary, perimeter \(L\), and continuous strictly positive curvature \(\kappa(s)\). Choose an arclength origin \(s=0\) on its boundary. Sample \(n\) independent boundary points with a continuous probability density \(f\) with respect to arclength. Assume that \(f(s)>0\) for \(s\ne0\), and, for fixed \(c>0\), \(\alpha>0\),
\[
f(s)=c|s|^\alpha(1+o(1))\qquad(s\to0).
\]
Let \(P_n\) be the convex hull, \(H_n=d_H(K,P_n)\), and \(A_n=\operatorname{area}(K)-\operatorname{area}(P_n)\). Let \(\Pi\) be a Poisson point process on \(\mathbb R\) of intensity \(c|x|^\alpha\,dx\). Enumerate its consecutive points as \(\cdots<X_{-1}<X_0<X_1<\cdots\), and define \(M=\max_j(X_{j+1}-X_j)\), and, when \(\alpha>1/2\), \(S=\sum_j(X_{j+1}-X_j)^3\). Almost surely \(M\in(0,\infty)\), and \(S\in(0,\infty)\) if \(\alpha>1/2\).

For every \(\alpha>0\),
\[
n^{2/(\alpha+1)}H_n\ \Longrightarrow\ \frac{\kappa(0)}8 M^2.
\]
The area deficit exhibits a *different, sharp* transition at \(\alpha=1/2\):
\[
\begin{cases}
n^2 A_n\xrightarrow{\mathsf P}\displaystyle\frac12\int_0^L\frac{\kappa(s)}{f(s)^2}\,ds, &0<\alpha<1/2,\\[5pt]
\displaystyle\frac{n^2}{\log n}A_n\xrightarrow{\mathsf P}\displaystyle\frac{2\kappa(0)}{3c^2}, &\alpha=1/2,\\[8pt]
n^{3/(\alpha+1)}A_n\Longrightarrow\displaystyle\frac{\kappa(0)}{12} S,&\alpha>1/2.
\end{cases}
\]
In the last regime the displayed Hausdorff and area convergences hold *jointly*, with \(M,S\) formed from the same Poisson process. Thus exceptionally sparse sampling near one point controls the worst geometric error for every \(\alpha>0\), but controls total missing area only above a second exponent threshold.

## Assumptions and scope
All limits take \(n\to\infty\); the curve, \(\alpha\), \(c\), and \(f\) remain fixed. The zero is unique on the periodic arclength circle. The curve has strictly positive curvature, and \(f\) is a probability density, so the coefficient \(c\) has arclength units. Point-process indexing is arbitrary and only consecutive gaps are used. \(\Longrightarrow\) is weak convergence and \(\xrightarrow{\mathsf P}\) convergence in probability. The Poisson law is not claimed to possess a closed elementary CDF.

## Proof
**1. Geometric cap expansions.** Every sampled point is a vertex of the inscribed polygon, and its cyclically successive sample points bound disjoint omitted caps. For an arclength gap \([s,s+\delta]\) with \(\delta\to0\), uniformly in \(s\), the maximal Euclidean distance from its boundary arc to the inscribed polygon is \(\kappa(s)\delta^2/8+O(\delta^3)\), and the area of its omitted cap is \(\kappa(s)\delta^3/12+O(\delta^4)\). These follow by expressing the arc in tangent/normal coordinates, using \(y(x)=\kappa(s)x^2/2+O(x^3)\), calculating the chord, and integrating the chord-minus-arc height. At an arbitrary sample configuration with sufficiently small maximal gap, the Hausdorff distance is the maximum over these cap errors, while the area deficit is their sum.

**2. Local Poisson process.** Set \(h=n^{-1/(\alpha+1)}\) and rescale sampled arclength coordinates near zero by \(s\mapsto s/h\). For any bounded Borel sets whose boundaries have zero Lebesgue measure, the expected sample counts converge to \(\int c|x|^\alpha dx\), since \(nh^{\alpha+1}=1\); disjoint counts converge jointly to independent Poisson counts by the multinomial-to-Poisson limit. Consequently the point configurations, their consecutive gaps within a fixed bounded window, and the corresponding scaled cap errors converge jointly to the functionals of \(\Pi\).

**3. Locality of the largest gap.** Given a fixed target length \(t>0\), partition the rescaled coordinate rays beyond \(R\) into consecutive intervals of length \(t/2\). If any sample gap of length exceeding \(t h\) is present there, one such subinterval is empty. For \(R\) large enough, its empty probability is bounded by \(\exp(-C t^{\alpha+1}j^\alpha)\) at index \(j\), uniformly in \(n\) until a fixed small arclength cutoff; beyond that cutoff the sampling density has a positive minimum and the empty probability decays exponentially in \(nh\). The sum of these bounds tends to zero as \(R\to\infty\). Thus the largest rescaled sample gap localizes near the unique zero and converges to \(M\). Because the curvature is continuous, the cap expansions give the stated Hausdorff limit. The same bounds prove that all gaps of \(\Pi\) tend to zero at both infinities, so \(M\) is finite and attained almost surely.

**4. Area tails and the supercritical joint law.** For a Poissonized sample of intensity \(nf(s)\,ds\), the Campbell--Mecke formula for consecutive points gives the exact expected weighted cubic-gap functional in terms of
\[
\int_0^L nf(s)\int_s^{s+L}nf(t)\,(t-s)^3
\exp\!\left(-n\int_s^t f(u)\,du\right)\,dt\,ds,
\]
with periodic interpretation and the full-circle wrap interval. Its dominant contribution where the local spacing is small is \(6n^{-2}\int f(s)^{-2}ds\). Near the zero, a direct rescaling and elementary exponential bounds yield, for \(\alpha>1/2\),
\[
\limsup_{n\to\infty} h^{-3}\,
\mathbb E\!\left[\sum_{\text{gaps outside }[-Rh,Rh]}\!\delta_j^3\right]
\le C R^{1-2\alpha},
\]
where gaps meeting the window boundary may be assigned to the near side. The same estimates on the limiting Poisson process show \(\mathbb E\sum_{\text{outside }[-R,R]}(X_{j+1}-X_j)^3\le C R^{1-2\alpha}\). Thus \(S\) is finite and the finite-window convergence extends to the whole cubic-gap sum. The sum of the \(O(\delta^4)\) cap remainders is negligible on the \(h^3\) scale (locally by convergence, outside by the corresponding fourth-gap bound). Joint convergence with the largest-gap functional follows. Conditioning a Poisson process of intensity \(n(1\pm n^{-1/4})f\) to bracket a fixed sample size and using monotonicity of \(H_n,A_n\) de-Poissonizes the results without altering the limits.

**5. Subcritical area law.** On any closed subarc away from the zero, exponential-spacing approximation and the cap expansion give
\[
n^2 A_n(\text{subarc})\xrightarrow{\mathsf P}
\frac12\int_{\text{subarc}}\frac{\kappa}{f^2}\,ds.
\]
The local mean arises from \(\mathbb E\delta^3=6/(nf)^3\), multiplied by the local mean number \(nf\,ds\) of gaps and the geometric coefficient \(\kappa/12\). The corresponding variance tends to zero after multiplication by \(n^4\), by disjoint Poisson increment blocking and the fifth inverse-intensity moment estimate. The exact consecutive-point integral above bounds the expected contribution from \(|s|\le\varepsilon\) by
\[
Cn^{-2}\int_{h}^{\varepsilon}s^{-2\alpha}ds+Ch^3.
\]
For \(0<\alpha<1/2\), after multiplying by \(n^2\) this tends to at most \(C\varepsilon^{1-2\alpha}\), while \(n^2h^3\to0\). Send \(\varepsilon\downarrow0\) to obtain the asserted integral law.

**6. Critical area law.** At \(\alpha=1/2\), discard the innermost \(|s|\le h n^\eta\) for arbitrary small fixed \(\eta>0\). The preceding expectation estimate makes its contribution at most \(C\eta\log n/n^2+O(n^{-2})\). On the remaining region the gap length divided by \(|s|\) tends uniformly to zero, so the local exponential-spacing calculation applies and has variance \(o(n^{-4}\log^2 n)\); for example the leading local variance bound is \(O(n^{-5}\int_{|s|>hn^\eta} f(s)^{-5}ds)=O(n^{-4-3\eta/2})\). Since
\[
\frac1{2n^2}\int_{hn^\eta<|s|<\varepsilon}\frac{\kappa(s)}{f(s)^2}ds
=\left(\frac{2\kappa(0)}{3c^2}-\frac{\kappa(0)\eta}{c^2}+o(1)\right)\frac{\log n}{n^2},
\]
first send \(n\to\infty\), then \(\eta\downarrow0\). Contributions outside any fixed neighborhood are \(O_{\mathsf P}(n^{-2})\). This establishes the critical coefficient.

## Verification
The standalone `CHECK.py` reproduces exact circle cap identities, checks quadratic/cubic coefficients, generates the inhomogeneous two-sided Poisson process directly by integrated-intensity inversion, and compares its joint geometric functionals with large random polygons. It also checks the finite-sample area mean in the \(\alpha<1/2\) phase and the critical constant. Run `python CHECK.py` with NumPy. Actual checker output in `VERIFICATION.md` records the tested values. The proof, not the finite simulations, establishes the limit laws.

## Relationship to prior work
Schneider (1988) studied random inscribed polygons under an everywhere positive continuous sampling density, which explicitly excludes the isolated power-law zero used here. Hüsler (1988) studied nonuniform maximum spacings with a zero density and therefore supplies close probabilistic context for the first (Hausdorff) component; the coupled missing-area law and its distinct critical exponent require the cubic-gap functional, not merely the largest spacing. Brunel (arXiv:1503.01504, first posted 2015-03-05) studied general Hausdorff deviation bounds and assumes a positive lower bound for his boundary-density example (Proposition 4). The present result instead gives an exact joint limiting law and a separate area transition for a sampling density vanishing at one boundary point.

## Limitations
This statement is limited to smooth strictly positively curved planar bodies with a single exact power-law zero. Multiple zeros, flat curvature points, rapidly varying nonpower-law densities, polygonal boundaries, and higher dimensions are not covered. The Poisson functional is characterized intrinsically rather than by an elementary density. The comparison with Hüsler's potentially relevant full text remains incomplete because a lawful full text was unavailable; this residual priority risk is not an independent originality certification.

## References
1. R. Schneider, *Random approximation of convex sets*, Journal of Microscopy 151 (1988), 211–227, DOI: 10.1111/j.1365-2818.1988.tb04682.x.
2. J. Hüsler, *Maximal, non-uniform spacings and the coverage problem*, Journal of Applied Probability 25 (1988), 519–528, DOI: 10.2307/3213981.
3. V.-E. Brunel, *Uniform Behaviors of Random Polytopes under the Hausdorff Metric*, arXiv:1503.01504, first publicly posted 2015-03-05; especially Section 3.3, Proposition 4.
4. M. Sonnleitner, *A limit theorem for Hausdorff approximation by random inscribed polytopes*, arXiv:2508.16442 (2025), positive-density optimal-sampling setting.
