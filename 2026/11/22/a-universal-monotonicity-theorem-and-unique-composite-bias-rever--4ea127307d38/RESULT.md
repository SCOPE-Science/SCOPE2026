# A universal monotonicity theorem and unique composite-bias reversal for spatially heterogeneous curve numbers

## Finding

**Theorem.** Let \(0<\lambda<1\) and \(S_0>0\) be fixed. Let the dimensionless local curve number \(C\) have an arbitrary non-point-mass probability law with compact support in \((0,1)\); the law represents area fractions of hydrologically distinct subcatchments. Put \(S=S_0(C^{-1}-1)\), \(s_- = \min\operatorname{supp}S\), and \(s_+=\max\operatorname{supp}S\). For storm rainfall depth \(P>0\), set

\[
q(P,s)=\begin{cases}0,&P\le\lambda s,\\[2pt](P-\lambda s)^2/(P+(1-\lambda)s),&P>\lambda s,\end{cases}
\qquad \bar q(P)=\mathbb E[q(P,S)].
\]

For every \(P>\lambda s_-\) there is exactly one active equivalent retention \(s_{\mathrm{eff}}(P)>0\) satisfying \(q(P,s_{\mathrm{eff}}(P))=\bar q(P)\). It lies in \([s_-,s_+]\), is continuously differentiable, and satisfies

\[
\frac{d}{dP}s_{\mathrm{eff}}(P)>0,\qquad
\lim_{P\downarrow\lambda s_-}s_{\mathrm{eff}}(P)=s_-,\qquad
\lim_{P\to\infty}s_{\mathrm{eff}}(P)=\mathbb E S.
\]

Thus the effective curve number \(C_{\mathrm{eff}}(P)=[1+s_{\mathrm{eff}}(P)/S_0]^{-1}\) is **strictly decreasing** in storm size. The standard area-averaged composite curve number is \(\bar C=\mathbb EC\), with retention \(s_c=S_0[(\mathbb EC)^{-1}-1]\). There is **exactly one** \(P_*>\lambda s_-\) at which distributed and composite runoff estimates agree, and necessarily \(P_*>\lambda s_c\):

\[
\bar q(P)-q(P,s_c)\begin{cases}>0,&\lambda s_-<P<P_*,\\=0,&P=P_*,\\<0,&P>P_* .\end{cases}
\]

For \(0<P\le\lambda s_-\), both runoff estimates equal zero (not additional positive-runoff crossovers). Moreover

\[
\lim_{P\to\infty}[\bar q(P)-q(P,s_c)]
=-(1+\lambda)(\mathbb ES-s_c)<0.
\]

## Assumptions and scope

This is the unmodified, event-based SCS/NRCS curve-number runoff equation with a fixed initial-abstraction ratio \(\lambda\). It assumes uniform event rainfall depth across spatial subareas, non-interacting area-weighted runoff, fixed soil/cover categories, and no extra routing, infiltration dynamics, or rainfall-intensity dependence. The arbitrary area-weight law may be continuous, discrete, singular, or a mixture, but must be nondegenerate and compactly supported strictly within \((0,1)\). In standard SI curve-number notation \(S_0=254\) mm and the conventional tabulated CN equals \(100C\). The theorem remains true for any positive \(S_0\) and any \(0<\lambda<1\).

## Proof

**1. Existence and differentiability.** For fixed \(P>0\), \(q(P,s)\) is continuous and nonincreasing in \(s\), and strictly decreasing when it is positive. For \(P>\lambda s_-\), the distribution has strictly positive mean runoff; since its nonconstant local retention spans \([s_-,s_+]\), the intermediate-value theorem gives exactly one \(s_{\mathrm{eff}}\in[s_-,s_+]\) on the active branch. The local runoff derivative \(q_P\) is continuous at the runoff threshold, where it equals zero on both sides. Compact support justifies differentiation under the expectation. Since \(q_s(P,s_{\mathrm{eff}})<0\), implicit differentiation gives a continuously differentiable \(s_{\mathrm{eff}}\).

**2. A universal strictly concave response-speed function.** Fix \(P>0\) and put \(a=1-\lambda\). For an active local runoff response define \(z=(P-\lambda s)/(P+a s)\); inactive responses are assigned \(z=0\). Then \(0\le z<1\), and elementary algebra gives

\[
q(P,s)=H_P(z):=\frac{Pz^2}{\lambda+a z},
\qquad q_P(P,s)=2z-z^2,
\qquad H_P''(z)=\frac{2P\lambda^2}{(\lambda+a z)^3}>0.
\]

The displayed identity for \(q_P\) also holds at inactive sites, since both sides are zero. The function \(H_P\) is strictly increasing and strictly convex on \([0,1]\). Its inverse \(Z_P:[0,P]\to[0,1]\) is strictly concave and increasing. Because \(z\mapsto 2z-z^2\) is increasing and concave on \([0,1]\), the composite

\[
\Phi_P(u)=2Z_P(u)-Z_P(u)^2
\]

is strictly concave on \([0,P]\), and every local response obeys \(q_P(P,s)=\Phi_P(q(P,s))\).

**3. Strict monotonicity by Jensen.** For any \(P>\lambda s_-\), the random variable \(q(P,S)\) is not almost surely constant. Strict Jensen applied to \(\Phi_P\) gives

\[
\bar q'(P)=\mathbb E\Phi_P(q(P,S))
<\Phi_P(\bar q(P))=q_P(P,s_{\mathrm{eff}}(P)).
\]

Differentiating the equivalent-retention identity yields

\[
q_s(P,s_{\mathrm{eff}}(P))s_{\mathrm{eff}}'(P)
=\bar q'(P)-q_P(P,s_{\mathrm{eff}}(P))<0.
\]

As \(q_s<0\) on the active branch, \(s_{\mathrm{eff}}'(P)>0\) strictly at every positive-runoff storm depth.

**4. Endpoints and exact one-crossing.** For a storm just above \(\lambda s_-\), the active inferred retention is squeezed by \(s_-\le s_{\mathrm{eff}}(P)<P/\lambda\), hence its lower endpoint is \(s_-\). Uniformly for \(s\in[s_-,s_+]\), as \(P\to\infty\),

\[
q(P,s)=P-(1+\lambda)s+\frac{s^2}{P+(1-\lambda)s}
=P-(1+\lambda)s+O(P^{-1}).
\]

Since \(s_{\mathrm{eff}}\) stays bounded, comparing this identity for \(s=s_{\mathrm{eff}}\) and the spatial expectation proves \(s_{\mathrm{eff}}(P)\to\mathbb ES\) and the asserted tail discrepancy. Strict convexity of \(c\mapsto S_0(c^{-1}-1)\) and nondegeneracy give

\[
s_-< s_c = S_0[(\mathbb EC)^{-1}-1]<\mathbb ES.
\]

The strict continuity and monotonicity in Step 3 therefore give a unique \(P_*\) with \(s_{\mathrm{eff}}(P_*)=s_c\). Because the runoff function strictly decreases with active retention, the signs in the theorem follow. At the crossing \(q(P_*,s_c)>0\), so \(P_*>\lambda s_c\).

## Verification

A standalone straightforward implementation of the local SCS-CN formula and bisection inversion appears in `check.py`, along with randomized multigroup stress tests, the exact two-soil benchmark, and numerical checks of the response-speed algebra and the strictly decreasing effective curve number. Run using Python 3: `python check.py`. These finite tests are supplementary diagnostics only; the proof above establishes the universal quantified result.

For a 40%/60% mixture of local curve numbers 50 and 90, \(\lambda=0.2\) and \(S_0=254\) mm, the ordinary composite curve number is 74; the unique crossover is \(P_*=228.09380830096\ldots\) mm. At 50 mm the distributed minus composite estimate is \(+7.74932556\ldots\) mm; at 350 mm it is \(-6.11611651\ldots\) mm. All numbers are rounded from the model, not field observations.

## Relationship to prior work

Soulis and Valiantzas (2012; public discussion 2011) explicitly model two-CN heterogeneous watersheds, derive the mixture law, establish its large-storm effective retention, and illustrate the familiar decrease in inferred CN with increasing rainfall. Grove, Harbor and Engel (1998) examine composite versus distributed curve numbers by simulations. Her, Seong and Jeong (2016) propose exact and quadratic averaging procedures and discuss event-specific representative curve numbers. Therefore none of the two-class response equation, practical aggregation error, qualitative two-class trend, or existence of a rain-dependent effective CN is claimed as new. The present claim is restricted to the **strict all-storm monotonicity for every compactly supported nondegenerate spatial CN law**, together with the **unique and inevitable sign reversal relative to the *arithmetic* composite CN**, established via the strictly concave common response-speed function. The accessible 2016 averaging abstract does not establish these universal quantified statements, but its unavailable complete mathematical treatment remains a material priority risk. Bartlett et al. (2016) study a more general, different mechanism for stochastic spatial runoff upscaling; their framework is not a theorem of this fixed-abstraction classical equation.

## Limitations

The result is a theorem about the stipulated empirical law, not an assertion of field predictive accuracy. Allowing storm-varying initial abstraction, correlated spatial rainfall, routing, water redistribution, or soil-state evolution invalidates the simple mixture reduction and may invalidate the theorem. A prior full-text averaging analysis or classical interpolation inequality may establish part of the same claim; historical originality is therefore provisional, and independent external validation has not occurred. The theorem does not provide an explicit closed form for the universal crossover depth for arbitrary CN distributions, only existence, uniqueness and a reproducible bisection procedure.

## References

1. Soulis, K. X., and Valiantzas, J. D. (2012). *SCS-CN parameter determination using rainfall-runoff data in heterogeneous watersheds – the two-CN system approach.* Hydrology and Earth System Sciences **16**, 1001–1015. Public discussion opened 5 October 2011. DOI: https://doi.org/10.5194/hess-16-1001-2012 ; open full text: https://hess.copernicus.org/articles/16/1001/2012/hess-16-1001-2012.pdf
2. Grove, M., Harbor, J., and Engel, B. (1998). *Composite vs. Distributed Curve Numbers: Effects on Estimates of Storm Runoff Depths.* Journal of the American Water Resources Association **34**, 1015–1023. DOI: https://doi.org/10.1111/j.1752-1688.1998.tb04150.x
3. Her, Y., Seong, C., and Jeong, J. (2016). *Alternative CN Averaging Methods for Determining the Representative CN of a Watershed.* Journal of Irrigation and Drainage Engineering **142**, 06016004. Published online 15 March 2016. DOI: https://doi.org/10.1061/(ASCE)IR.1943-4774.0001021
4. Bartlett, M. S., Parolari, A. J., McDonnell, J. J., and Porporato, A. (2016). *Beyond the SCS-CN method: A theoretical framework for spatially lumped rainfall-runoff response.* Water Resources Research **52**, 4608–4627. DOI: https://doi.org/10.1002/2015WR018439
