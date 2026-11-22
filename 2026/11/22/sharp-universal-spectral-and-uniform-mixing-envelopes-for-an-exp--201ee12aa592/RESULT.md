# Sharp universal spectral and uniform-mixing envelopes for an exponential-quadratic copula

## Finding

Consider the exponential-quadratic copula of Zachariah, Arshad and Pathak,
\[
C_{\alpha,\delta}(u,v)=uv+\delta\bigl(1-e^{\alpha u(1-u)}\bigr)\bigl(1-e^{\alpha v(1-v)}\bigr),\qquad 0\le u,v\le1.
\]
Give its associated stationary Markov chain uniform one-dimensional margins and use this copula for successive states. Define
\[
g_\alpha(u)=(1-2u)e^{\alpha u(1-u)},\quad
M_\alpha=\max_{0\le u\le1}|g_\alpha(u)|,\quad
J_\alpha=\int_0^1g_\alpha(u)^2\,du.
\]
For \(\alpha\ne0\), the complete admissible parameter domain is \(|\delta|\alpha^2M_\alpha^2\le1\); for \(\alpha=0\), every finite \(\delta\) gives independence. Put \(\lambda=\delta\alpha^2J_\alpha\), with \(\lambda=0\) at \(\alpha=0\).

**Theorem.** For every admissible parameter pair and every integer \(n\ge1\), the lag-\(n\) joint density and the Hirschfeld--Gebelein--Rényi maximal correlation obey
\[
p_n(u,v)=1+(\delta\alpha^2)^nJ_\alpha^{n-1}g_\alpha(u)g_\alpha(v),\qquad
\rho_{\mathrm{HGR}}(U_0,U_n)=|\lambda|^n.
\]
There is one universal constant \(\mathfrak m\) such that the **sharp, simultaneously attainable envelopes** over the entire copula parameter domain are
\[
\boxed{\sup_{\alpha,\delta}\rho_{\mathrm{HGR}}(U_0,U_n)=\mathfrak m^n,\qquad
\sup_{\alpha,\delta}\|p_n-1\|_{\infty}=\mathfrak m^{n-1}.}
\]
The second identity includes \(n=1\), when the right-hand side equals one. For each \(n\ge2\), equality in either envelope requires exactly
\[
\alpha=\alpha_*=2s_*^2=4.567563049978093\ldots,\qquad
|\delta|=\frac{e^{1-\alpha_*/2}}{2\alpha_*}=0.030321188550275\ldots.
\]
Here \(s_*=1.511218556327656\ldots\) is the unique root greater than one of
\[
\int_0^{s_*}t^2e^{-t^2}\,dt=s_*^3e^{-s_*^2},
\]
and
\[
\boxed{\mathfrak m=s_*^2e^{1-s_*^2}=0.632579805061989\ldots<1.}
\]
At the optimal parameters, the extremal absolute density discrepancy occurs at \(u,v\in\{(1-\sqrt{2/\alpha_*})/2,(1+\sqrt{2/\alpha_*})/2\}\). Thus even at the edge of admissibility every such chain mixes uniformly, with the optimal global exponential base specified exactly.

## Assumptions and scope

The real parameter \(\alpha\) and finite real parameter \(\delta\) vary over all values for which \(C_{\alpha,\delta}\) is a bivariate copula. A stationary time-homogeneous Markov chain \((U_j)_{j\ge0}\) on \([0,1]\) has marginal law uniform on \([0,1]\) and transition density \(p_1(u,v)=\partial_u\partial_vC_{\alpha,\delta}(u,v)\). Maximal correlation means the supremum of the absolute Pearson correlation over all pairs of nonconstant square-integrable measurable functions of the two indicated random variables. The essential supremum \(\|p_n-1\|_\infty\) is with respect to Lebesgue measure on the unit square. The special case \(\alpha=0\) is independent of \(\delta\).

## Proof

**1. Validity and maximal amplitude.** Differentiating the copula gives
\[
p_1(u,v)=1+\delta\alpha^2g_\alpha(u)g_\alpha(v),\qquad
\int_0^1g_\alpha(u)\,du=0.
\]
The function \(g_\alpha\) is antisymmetric around one half. Its range is exactly \([-M_\alpha,M_\alpha]\), so nonnegativity of the density for every pair is equivalent to \(|\delta|\alpha^2M_\alpha^2\le1\) for nonzero \(\alpha\). Differentiation gives
\[
g_\alpha'(u)=e^{\alpha u(1-u)}\{\alpha(1-2u)^2-2\}.
\]
Consequently
\[
M_\alpha=\begin{cases}1,&\alpha\le2,\\
\sqrt{2/\alpha}\,e^{\alpha/4-1/2},&\alpha>2.
\end{cases}
\]
The first branch uses the endpoint extrema; the second uses the two interior extrema. In particular, \(J_\alpha<M_\alpha^2\), strictly for every finite \(\alpha\), since \(g_\alpha\) is continuous and not almost everywhere of constant absolute value.

**2. Transition and spectral identities.** The transition operator on the centered subspace of \(L^2([0,1])\) is
\[
(Th)(u)=\delta\alpha^2g_\alpha(u)\int_0^1g_\alpha(v)h(v)\,dv.
\]
This rank-one self-adjoint operator has its only possible nonzero eigenvalue \(\lambda=\delta\alpha^2J_\alpha\), with normalized eigenfunction \(g_\alpha/\sqrt{J_\alpha}\). Inductively multiplying kernels and using the zero integral of \(g_\alpha\) yields the formula for \(p_n\). The sharp Cauchy--Schwarz bound on correlations, with equality for the eigenfunction, gives \(\rho_{\mathrm{HGR}}(U_0,U_n)=|\lambda|^n\). Moreover,
\[
\|p_n-1\|_\infty=\bigl(|\delta|\alpha^2M_\alpha^2\bigr)\bigl(|\delta|\alpha^2J_\alpha\bigr)^{n-1}.
\]
For any fixed \(\alpha\ne0\), both quantities are maximized by either admissible endpoint \(|\delta|=1/(\alpha^2M_\alpha^2)\). Write \(B(\alpha)=J_\alpha/M_\alpha^2\).

**3. Unique global shape optimizer.** Substitute \(x=|1-2u|\). On \(\alpha\le2\),
\[
B(\alpha)=\int_0^1x^2e^{\alpha(1-x^2)/2}\,dx,
\]
whose derivative is strictly positive. On \(\alpha>2\), put \(s=\sqrt{\alpha/2}>1\). Then
\[
B(\alpha)=\frac e s\int_0^s t^2e^{-t^2}\,dt,
\qquad
\frac{dB}{ds}=\frac e{s^2}D(s),\quad
D(s)=s^3e^{-s^2}-\int_0^st^2e^{-t^2}\,dt.
\]
A direct derivative gives \(D'(s)=2s^2e^{-s^2}(1-s^2)<0\) on \(s>1\). Also
\[
D(1)>e^{-1}-1/3>0,
\qquad
\lim_{s\to\infty}D(s)=-\sqrt\pi/4<0.
\]
Thus \(D\) has exactly one root \(s_*>1\); \(B\) strictly increases to it and strictly decreases afterward. Because the \(\alpha\le2\) branch increases strictly, this is the unique global shape maximizer. At the root, substitution into \(B\) gives \(\mathfrak m=s_*^2e^{1-s_*^2}\). The equality cases follow from strictness in the shape optimization and the endpoint condition for \(\delta\). For \(n=1\) the density envelope of one is attained at *every* nonindependent admissible endpoint, whereas the maximal-correlation envelope still has the unique optimal shape. This proves the theorem.

## Verification

The standalone \`CHECKER.py\` uses only the Python standard library. Execute \`python3 CHECKER.py\` beside this document. It independently brackets the unique root, computes \(\alpha_*\), \(\mathfrak m\) and the endpoint parameter, compares direct quadrature with the transformed analytic integral at multiple positive and negative shapes, tests admissibility at boundary densities, and replays the two-step Chapman--Kolmogorov identity numerically. The decisive monotonicity and uniqueness arguments are the analytic differentiations in the proof, not a finite grid or numerical optimizer.

## Relationship to prior work

Zachariah, Arshad and Pathak's publicly available 2023 preprint (later published in 2024) defines this exact family, its admissibility ranges and its rank-concordance statistics, including the approximate maximum Spearman correlation near shape \(\alpha=3.8\). Those facts are prior work and are not claimed here. Their preprint discusses quadrant dependence, density total positivity and tail independence but not global maximal correlation or the sharp uniform Markov transition-density envelope.

Longla's 2024 work develops general spectral and mixing theory for square-integrable symmetric copulas; the rank-one operator/lag identity used here is compatible with, and in part follows from, that broader framework. The contribution here is the exact **shape-constrained global optimization** and the resulting same sharp constant for every lag in both maximal correlation and uniform density error. Longla's 2026 paper addresses nilpotent, finite-dependent constructions rather than this nontrivial reversible rank-one kernel. The originating author's 2025 dissertation reproduces the family and rank-concordance analysis but does not derive the displayed sharp mixing envelope.

## Limitations

This is a within-family, stationary copula-based result; it is not a best-possible mixing bound for all copulas or all Markov chains. For \(\alpha=0\) the model is independence for every finite \(\delta\), so the formula \(B(0)=1/3\) is only a continuous shape ratio, not a nonzero eigenvalue of that degenerate parameterization. The numerical decimals are approximations; the exact constant is defined by the unique integral root. Finite numerical checks do not replace the global proof. Priority beyond the examined sources remains open to independent literature verification.

## References

1. S. G. Zachariah, M. Arshad and A. K. Pathak, *A new class of copulas having dependence range larger than FGM-type copulas*, public preprint 5 April 2023, arXiv:2304.02231; *Statistics & Probability Letters* **206** (2024), 109988, https://doi.org/10.1016/j.spl.2023.109988, https://arxiv.org/abs/2304.02231.
2. M. Longla, *New copula families and mixing properties*, *Statistical Papers* **65** (2024), 4331–4363, https://doi.org/10.1007/s00362-024-01559-9.
3. M. Longla, *Copulas, m-dependence, and Markov chains*, *TEST* **35** (2026), 406–439, https://doi.org/10.1007/s11749-026-01003-0.
4. S. G. Zachariah, *Dependence and Uncertainty: A Copula-Based Framework*, Ph.D. dissertation, IIT Indore (2025), Chapter 2, https://dspace.iiti.ac.in/bitstream/123456789/16598/1/TH_745_Swaroop_Georgy_Zachariah_2001241009.pdf.
