# A sharp three-query Gaussian Hutch++ crossover on spiked matrices

## Finding
Let \(A\) be a real symmetric positive-definite matrix with eigenvalues \((\kappa,1,\ldots,1)\), where \(\kappa\geq1\) and the dimension \(d\geq2\). Compare two unbiased trace estimators under exactly three multiplication queries with \(A\): (i) the Gaussian one-column/one-residual-probe Hutch++ estimator \(H_{++}\), and (ii) the average \(H_3\) of three independent Gaussian quadratic probes.

For every fixed dimension \(d\), the unusually large-spike limit of the first estimator has the sharp variance law
\[
\operatorname{Var}(H_{++})=\sqrt\pi\,\frac{\Gamma(d/2)}{\Gamma((d-1)/2)}\,\kappa+O_d(1),\qquad \kappa\to\infty.
\]
By contrast, \(\operatorname{Var}(H_3)=2(\kappa^2+d-1)/3\). Thus the deflated estimator's variance grows linearly, not quadratically, even though rare sketches that nearly miss the spike prevent bounded variance.

In the minimal dimension \(d=4\) in which three generic matrix-vector queries are fewer than the matrix dimension, the variances are exactly
\[
\operatorname{Var}(H_{++})=\frac{2(\kappa^4+8\kappa^3+7\kappa^2+6\kappa+2)}{(\kappa+1)^3},\qquad
\operatorname{Var}(H_3)=\frac{2(\kappa^2+3)}3.
\]
There is exactly one positive root \(\kappa_*\) of
\[
\kappa^5-18\kappa^3-11\kappa^2-9\kappa-3=0,
\qquad \kappa_*=4.56842704056585228676\ldots.
\]
For \(1\leq\kappa<\kappa_*\), \(H_3\) has strictly smaller variance; at \(\kappa_*\) they tie; for \(\kappa>\kappa_*\), \(H_{++}\) has strictly smaller variance. These are exact comparisons for the specified Gaussian implementations, not general algorithmic optimality claims.

## Assumptions and scope
Use an exact real-arithmetic matrix-vector oracle. Random vectors are independent standard real Gaussian vectors. Let \(s,g,z_1,z_2,z_3\sim N(0,I_d)\) be independent. Define \(q=As/\|As\|_2\), \(P=I_d-qq^{\mathsf T}\), and
\[
H_{++}=q^{\mathsf T}Aq+g^{\mathsf T}PAPg,
\qquad H_3=\frac13\sum_{j=1}^3z_j^{\mathsf T}Az_j.
\]
The first requires the three products \(As\), \(Aq\), and \(A(Pg)\). The second uses \(Az_1,Az_2,Az_3\). Scaling all eigenvalues by \(b>0\) scales both variances by \(b^2\); hence unit small eigenvalues are a normalization, not a limitation. Orthogonal similarity does not change either distribution. The result is for one rank-one Gaussian sketch and one Gaussian residual probe; alternative probe distributions, adaptive budgets, Rademacher probes, and other Hutch++ variants are not covered.

## Proof
**Conditional variance.** Orthogonally diagonalize \(A=I_d+\delta vv^{\mathsf T}\) with \(\delta=\kappa-1\), \(\|v\|_2=1\). For any fixed sketch direction \(q\), cyclicity gives
\[
q^{\mathsf T}Aq+\operatorname{tr}(PAP)=\operatorname{tr}(A).
\]
Thus \(\mathbb E(H_{++}\mid q)=\operatorname{tr}(A)\) and both estimators are unbiased. The Gaussian quadratic-form identity \(\operatorname{Var}(g^{\mathsf T}Bg)=2\operatorname{tr}(B^2)\) for symmetric \(B\), together with conditional total variance, yields
\[
\operatorname{Var}(H_{++})=2\mathbb E\operatorname{tr}((PAP)^2).
\]
Putting \(w=Pv\) and \(t=\|w\|_2^2=1-(q^{\mathsf T}v)^2\), one has \(PAP=P+\delta ww^{\mathsf T}\) and \(Pw=w\), so
\[
\operatorname{tr}((PAP)^2)=(d-1)+2\delta t+\delta^2t^2.\tag{1}
\]
With \(X\sim N(0,1)\), \(S\sim\chi^2_{d-1}\) independent, rotational invariance gives the exact distributional identity
\[
t\ \stackrel{\mathrm d}=\ \frac{S}{\kappa^2X^2+S}.\tag{2}
\]
The standard Gaussian fourth-moment identity also yields \(\operatorname{Var}(H_3)=2\|A\|_{\mathrm F}^2/3=2(\kappa^2+d-1)/3\).

**Sharp all-dimension asymptotic.** For \(j=1,2\), conditional on \(S\), set \(X=\sqrt S\,y/\kappa\) in the Gaussian integral. Denoting \(\phi(0)=1/\sqrt{2\pi}\),
\[
\mathbb E(t^j)=\frac{\phi(0)}\kappa\,\mathbb E\left[\sqrt S\int_{\mathbb R}\frac{\exp(-Sy^2/(2\kappa^2))}{(1+y^2)^j}\,dy\right].\tag{3}
\]
The integral for \(j=1\) is bounded by \(\pi\), hence \(\mathbb Et=O_d(\kappa^{-1})\). For \(j=2\), use \(0\leq1-e^{-a}\leq a\), \(\mathbb ES^{3/2}<\infty\), and the integrability of \(y^2/(1+y^2)^2\) to obtain
\[
\mathbb Et^2=\frac{\phi(0)\pi}{2\kappa}\mathbb E\sqrt S+O_d(\kappa^{-3})
=\frac{\sqrt\pi}{2\kappa}\frac{\Gamma(d/2)}{\Gamma((d-1)/2)}+O_d(\kappa^{-3}).
\]
Insert into (1), with \(\delta=\kappa-1\), to obtain the announced linear variance asymptotic, including its exact coefficient.

**Exact four-dimensional crossover.** For \(d=4\), the random variable \(u=X^2/(X^2+S)\) has distribution \(\operatorname{Beta}(1/2,3/2)\). Set \(y=\sqrt{u/(1-u)}\geq0\). Its density is \(4/[\pi(1+y^2)^2]\), and (2) becomes \(t=1/(1+\kappa^2y^2)\). Partial fractions and the elementary integrals
\[
\int_0^\infty\frac{dy}{y^2+a^2}=\frac\pi{2a},\qquad
\int_0^\infty\frac{dy}{(y^2+a^2)^2}=\frac\pi{4a^3}
\]
give, including \(\kappa=1\) by continuity,
\[
\mathbb Et=\frac{2\kappa+1}{(\kappa+1)^2},\qquad
\mathbb Et^2=\frac{\kappa^2+3\kappa+1}{(\kappa+1)^3}.\tag{4}
\]
Substitution into (1) gives the stated \(\operatorname{Var}(H_{++})\). Direct algebra factors their difference as
\[
\operatorname{Var}(H_3)-\operatorname{Var}(H_{++})
=\frac{2\big(\kappa^5-18\kappa^3-11\kappa^2-9\kappa-3\big)}{3(\kappa+1)^3}.\tag{5}
\]
The numerator has exactly one sign change in its descending nonzero coefficients and therefore at most one positive root by Descartes' rule of signs. It is negative at \(\kappa=1\) and positive at \(\kappa=5\), so it has exactly one positive root, lying in \((1,5)\); its sign determines the complete crossover statement.

## Verification
The standalone file `verify_trace.py` checks (1), (4), (5), the threshold signs and uniqueness, high-precision one-dimensional quadrature independently of the symbolic formulas, direct matrix identities for 180 Gaussian directions, and simulated variance of the actual Gaussian Hutch++ estimator. Run `python verify_trace.py` with Python, SymPy, mpmath and NumPy. The captured output is `verification_output.txt`. Finite numeric checks support arithmetic and implementation only; they are not substitutes for the all-parameter proof above.

## Relationship to prior work
Meyer, Musco, Musco and Woodruff (2020), arXiv:2010.09649, introduce Hutch++ and prove general query-complexity guarantees; their Algorithm 1 allows standard Gaussian sketches and probes. Persson, Cortinovis and Kressner (2021), arXiv:2109.10659, compare query allocation and introduce adaptive Hutch++ and Nyström++ variants. They explicitly discuss the contrast between flat and decaying spectra. Their general Gaussian variance formula, conditional residual-Frobenius framework and adaptive complexity results do not state the four-dimensional exact variance integral, its unique three-query crossover, or the sharp fixed-dimensional rare-sketch leading coefficient computed here. These are quantitative special-model results, not improvements to the published general complexity order. The published conditional variance identity itself is not claimed as new.

## Limitations
The all-dimension asymptotic holds for each fixed \(d\) as \(\kappa\to\infty\); it is not uniform over growing dimensions. The exact crossover is proved only for \(d=4\), and applies only to standard Gaussian sketch and residual sampling with exactly three multiplication queries. It does not compare against Rademacher estimators, deterministic special-matrix algorithms, adaptive allocation, Nyström++, or optimally chosen trace estimators. A matrix whose eigenvalues are known has a trivial known trace; the family here is a spectral test class for generic black-box algorithms, not a promise exploited by the implementations. Specialist unindexed precedence cannot be ruled out.

## References
1. R. A. Meyer, C. Musco, C. Musco and D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, arXiv:2010.09649 (first public version October 19, 2020), https://arxiv.org/abs/2010.09649; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC8553228/.
2. D. Persson, A. Cortinovis and D. Kressner, *Improved variants of the Hutch++ algorithm for trace estimation*, arXiv:2109.10659 (first public version September 22, 2021), https://arxiv.org/abs/2109.10659; HTML https://ar5iv.labs.arxiv.org/html/2109.10659.
