# Vanishing-weight collapse of inverse-Gaussian CDF–Stein statistics

## Finding

For the weighted inverse-Gaussian (IG) CDF–Stein goodness-of-fit statistics of Allison, Betsch, Ebner and Visagie, the moment (MO) and maximum-likelihood (ML) implementations have different zero-weight boundaries. For each fixed nonconstant positive sample, the MO discrepancy generically approaches a nonzero constant as the threshold tends to infinity, whereas the ML discrepancy is identically zero past the sample maximum. Consequently the unweighted MO squared discrepancy is generically infinite, while the unweighted ML squared discrepancy is finite.

More sharply, let \(X_1,\ldots,X_n\) be i.i.d. \(\operatorname{IG}(\mu,\lambda)\), with fixed \(\mu,\lambda>0\), and put \(\phi=\lambda/\mu\). For **every deterministic sequence** \(a_n>0\) satisfying \(a_n\to0\), the original four statistics (two estimators, two weights) obey

\[
 a_n T^{\mathrm{MO}}_{n,a_n}\ \Rightarrow\ \frac{3}{2\phi}\chi_1^2,
 \qquad
 \sqrt{a_n}\,\widetilde T^{\mathrm{MO}}_{n,a_n}\ \Rightarrow\ \frac{3\sqrt\pi}{4\phi}\chi_1^2,
\]
\[
 a_n T^{\mathrm{ML}}_{n,a_n}\ \xrightarrow{\mathbb P}\ 0,
 \qquad
 \sqrt{a_n}\,\widetilde T^{\mathrm{ML}}_{n,a_n}\ \xrightarrow{\mathbb P}\ 0.
\]

There is **no relation required** between the rate of \(a_n\downarrow0\) and the growth of \(n\). The nondegenerate MO limits follow from a one-dimensional moment-mismatch fluctuation, not from the fixed-positive-weight Gaussian process limit. The assertion is for the statistics themselves, not an assertion that a separately recalibrated bootstrap test has wrong significance level.

## Assumptions and scope

Define \(\bar X=n^{-1}\sum_iX_i\), \(Y_i=X_i/\bar X\), \(u=n^{-1}\sum_iY_i^{-1}\) and \(v=n^{-1}\sum_iY_i^2\). For \(n\ge2\) and a nonconstant sample, \(u,v>1\). Use exactly the source's two scale-invariant shape estimates

\[
\widehat\phi_{\rm ML}=(u-1)^{-1},\qquad
\widehat\phi_{\rm MO}=(v-1)^{-1}.
\]

For either choice \(\widehat\phi\), set

\[
G_n(t)=\frac1{2n}\sum_{i=1}^n
 \left(\widehat\phi+\frac3{Y_i}-\frac{\widehat\phi}{Y_i^2}\right)\min(Y_i,t)
 -\frac1n\sum_{i=1}^n\mathbf 1_{\{Y_i\le t\}},\quad t\ge0,
\]
\[
T_{n,a}=n\int_0^\infty G_n(t)^2e^{-at}\,dt,\qquad
\widetilde T_{n,a}=n\int_0^\infty G_n(t)^2e^{-at^2}\,dt.
\]

These formulae define all four statistics. There is no restriction on the fixed true shape \(\phi>0\). A singular sample with all observations identical is excluded from the finite-sample formulas; under the continuous null it has probability zero.

## Proof

**1. Exact plateau.** For every \(t\ge M=\max_iY_i\), the minimum equals \(Y_i\) and every indicator is one. Since \(\bar Y=1\),

\[
G_n(t)=C_n=\frac12\{1-\widehat\phi(u-1)\}.
\]

Therefore \(C_n^{\rm ML}=0\) exactly, while

\[
C_n^{\rm MO}=\frac{v-u}{2(v-1)}
=\frac{\overline{(Y-1)^3/Y}}{2\overline{(Y-1)^2}}.
\]

The cubic identity uses \(\bar Y=1\). As \(G_n-C_n\) vanishes for \(t\ge M\), dominated convergence gives, for any fixed nonconstant sample,

\[
\lim_{a\downarrow0}aT_{n,a}=nC_n^2,\qquad
\lim_{a\downarrow0}\sqrt a\,\widetilde T_{n,a}
=\frac{\sqrt\pi}{2}nC_n^2.
\]

In addition, \(T_{n,a}^{\rm ML}\to n\int_0^M G_n(t)^2dt<\infty\) for either weight, while if \(C_n^{\rm MO}\ne0\), the unweighted MO integral diverges. The real-analytic function \(v-u\) is not identically zero on the positive normalized sample simplex: take two unequal coordinates symmetric about one and all remaining coordinates one. Thus under the absolutely continuous IG null, \(C_n^{\rm MO}\ne0\) almost surely for every \(n\ge2\).

**2. Joint-limit tail control without a tuning-rate restriction.** By scale invariance take \(\mu=1\). Write \(\widehat\mu=\bar X\), \(\theta=\widehat\phi\), \(R_n(t)=G_n(t)-C_n\), and \(s=\widehat\mu t\). A direct rearrangement gives the exact identity

\[
R_n(s/\widehat\mu)=P_n f_0(s)
 -\frac{\theta}{2\widehat\mu}P_n f_1(s)
 -\frac32P_n f_2(s)
 +\frac{\theta\widehat\mu}{2}P_n f_3(s),
\]

where \(P_nf_j(s)=n^{-1}\sum_{i=1}^n f_j(X_i,s)\) and

\[
\begin{aligned}
f_0(x,s)&=\mathbf1_{\{x>s\}},\\
f_1(x,s)&=(x-s)\mathbf1_{\{x>s\}},\\
f_2(x,s)&=(1-s/x)\mathbf1_{\{x>s\}},\\
f_3(x,s)&=(x^{-1}-s x^{-2})\mathbf1_{\{x>s\}}.
\end{aligned}
\]

All four random functions belong to the unweighted Hilbert space \(H=L^2((0,\infty),ds)\), since their squared norms are, respectively, \(x\), \(x^3/3\), \(x/3\) and \(1/(3x)\). The IG law has finite positive and inverse moments of all orders. Thus \(\sqrt n\|P_nf_j-Pf_j\|_H=O_{\mathbb P}(1)\) by the Hilbert-space second-moment identity (no empirical-process tightness theorem is needed).

At the population parameter \((\widehat\mu,\theta)=(1,\phi)\), the linear combination of \(Pf_j\) above is identically zero, by the original CDF–Stein identity and \(\mathbb E[X^{-1}]=1+\phi^{-1}\). The two estimators satisfy \(\widehat\mu-1=O_{\mathbb P}(n^{-1/2})\) and \(\theta-\phi=O_{\mathbb P}(n^{-1/2})\). Combining these facts with the exact finite four-function representation and changing variables \(dt=ds/\widehat\mu\) proves

\[
 n\int_0^\infty R_n(t)^2dt=O_{\mathbb P}(1)
\]

for either estimator. This is the critical unweighted residual bound; it holds even though the complete MO discrepancy itself is not in unweighted \(L^2\).

**3. Reduce the vanishing-weight statistics to the plateau.** For any \(a_n\downarrow0\), the residual contribution to the exponentially weighted statistic satisfies

\[
n a_n\int_0^\infty R_n(t)^2e^{-a_nt}dt
\le a_n n\int_0^\infty R_n(t)^2dt=o_{\mathbb P}(1).
\]

Similarly \(n\sqrt{a_n}\int R_n(t)^2e^{-a_nt^2}dt=o_{\mathbb P}(1)\). The mixed terms between \(C_n\) and \(R_n\) are also \(o_{\mathbb P}(1)\) after scaling, by weighted Cauchy–Schwarz and \(nC_n^2=O_{\mathbb P}(1)\). Because \(a\int_0^\infty e^{-at}dt=1\) and \(\sqrt a\int_0^\infty e^{-at^2}dt=\sqrt\pi/2\), it follows that

\[
a_nT_{n,a_n}=nC_n^2+o_{\mathbb P}(1),\qquad
\sqrt{a_n}\widetilde T_{n,a_n}=\frac{\sqrt\pi}{2}nC_n^2+o_{\mathbb P}(1).
\]

The ML assertions already follow from \(C_n^{\rm ML}=0\).

**4. Exact one-dimensional null variance.** For \(X\sim\operatorname{IG}(1,\phi)\), let \(A=1+\phi^{-1}\). Since \(v-u\) has the influence function

\[
H(X)=X^2-X^{-1}-3A(X-1),
\]

the multivariate central limit theorem and delta method give \(\sqrt n(v-u)=n^{-1/2}\sum_iH(X_i)+o_{\mathbb P}(1)\). The required moments are

\[
\begin{aligned}
\mathbb EX^2&=\mathbb EX^{-1}=1+\phi^{-1},\\
\mathbb EX^3&=1+3\phi^{-1}+3\phi^{-2},\\
\mathbb EX^4&=1+6\phi^{-1}+15\phi^{-2}+15\phi^{-3},\\
\mathbb EX^{-2}&=1+3\phi^{-1}+3\phi^{-2}.
\end{aligned}
\]

They yield \(\mathbb EH(X)=0\) and \(\mathbb EH(X)^2=6\phi^{-3}\). Since \(v-1\to\phi^{-1}\),

\[
\sqrt n C_n^{\rm MO}\Rightarrow N(0,3/(2\phi)),
\qquad n(C_n^{\rm MO})^2\Rightarrow \frac3{2\phi}\chi_1^2.
\]

Substituting into Step 3 proves both nondegenerate limits.

## Verification

The standalone \(\texttt{check.py}\) reconstructs the four-function decomposition from raw observations, checks the exact rational sample \((1,2,3)\), and verifies \(C^{\rm ML}=0\) and \(C^{\rm MO}=-1/6\). It symbolically derives \(\mathbb EH(X)^2=6\phi^{-3}\), checks numerical quadrature for both weights at four small tuning values, and compares a 7,000-replicate \(n=1200\) IG simulation with the predicted one-dimensional Gaussian/chi-square null. All 50 assertions passed. These finite computations supplement, but do not replace, Steps 1–4.

## Relationship to prior work

Allison, Betsch, Ebner and Visagie introduced both CDF–Stein weighted tests, both estimation procedures, and their fixed-positive-weight asymptotic theory in a public 2019 preprint, later published in 2022. Their formulas and null-estimator expansions are used and credited here. This result is not the published fixed-\(a\) Gaussian-process limit: it derives an exact infinite-threshold distinction and a new joint limit when the weighting parameter tends to zero at an arbitrary rate. The preprint's comparison tables use \(\(a=0.1,1,10\)\), not this boundary. Nik and Weiß (2024) unify IG ML/MO estimators within a family of Stein moment estimators but do not analyze the CDF–Stein goodness-of-fit test's vanishing-weight law. A separate known large-\(a\) CDF–Stein boundary concerns the opposite small-threshold endpoint and does not imply this small-\(a\) theorem.

## Limitations

The theorem assumes i.i.d. fixed-parameter IG observations with \(\mu,\lambda>0\). It does not treat alternatives, drifting IG shape parameters, random data-dependent tuning, the joint conditional parametric bootstrap, or significance of a bootstrap-calibrated test. The complete MO statistic is infinite at exactly \(a=0\) for generic samples; limits are taken only through strictly positive \(a\). Statistical priority outside the inspected primary literature and searched research records is not independently certified.

## References

1. J. S. Allison, S. Betsch, B. Ebner, I. J. H. Visagie, *New weighted \(L^2\)-type tests for the inverse Gaussian distribution*, arXiv:1910.14119, first publicly submitted 30 October 2019. https://arxiv.org/abs/1910.14119
2. J. S. Allison, S. Betsch, B. Ebner, J. Visagie, *On Testing the Adequacy of the Inverse Gaussian Distribution*, Mathematics **10** (2022), 350, published 24 January 2022. https://doi.org/10.3390/math10030350
3. S. Nik, C. H. Weiß, *Generalized Moment Estimators Based on Stein Identities*, Journal of Statistical Theory and Applications **23** (2024), 240–274. https://doi.org/10.1007/s44199-024-00081-z
