# Universal single-crossing of habitat-quorum survival under synchronized mortality

## Finding

Let \(n\ge2\) habitat patches start occupied. Each patch has a fixed marginal extinction rate \(e>0\). A rate \(g\in[0,e]\) of the hazard is supplied by a single common fatal shock; its remaining rate \(e-g\) acts separately at each patch. Write \(T_{n,k}(g)\) for the first time fewer than \(k\) patches are occupied, where \(1\le k\le n\). All patch extinctions are permanent.

For every pair \(0\le g_1<g_2\le e\), the following complete classification holds for every \(t>0\):

* If \(k=1\), then \(\Pr(T_{n,1}(g_2)>t)<\Pr(T_{n,1}(g_1)>t)\).
* If \(k=n\), the strict inequality is reversed.
* If \(2\le k\le n-1\), there is **exactly one** \(t_*>0\) such that the higher-common-shock survival probability is smaller for \(0<t<t_*\), equal for \(t=t_*\), and larger for \(t>t_*\).

In the smallest intermediate-quorum case \((n,k)=(3,2)\), the exact mean viable time is
\[
\mathbb E T_{3,2}(g)=\frac{5e-4g}{(2e-g)(3e-2g)}.
\]
It has a unique maximum over \(g\in[0,e]\), attained at
\[
g_*=\frac{5-\sqrt3}{4}e,\qquad \max_g\mathbb E T_{3,2}(g)=\frac{8-4\sqrt3}{e}.
\]
Thus every intermediate-quorum survival-curve comparison has exactly one time crossing, yet mean viable time has an interior optimum. These are one combined result about the same fixed-marginal common-shock model.

## Assumptions and scope

The rates \(e>0\), \(0\le g\le e\) are measured in inverse time. Let \(Z\) be exponential with rate \(g\), and let \(X_1,\dots,X_n\) be independent exponential clocks of rate \(e-g\), independent of \(Z\). The convention at rate zero is that the clock is \(+\infty\) almost surely. The occupied life of patch \(i\) is \(L_i=\min(X_i,Z)\). Its marginal survival is \(\Pr(L_i>t)=e^{-et}\), independent of \(g\). All \(n\) patches start occupied. No recolonization, rescue, reproduction, immigration or post-extinction recovery occurs. The quorum \(k\) is an exact integer; time \(t\) is strictly positive. The common shock destroys all still-occupied patches simultaneously and can also occur when none remain.

Define the binomial tail
\[
B_{n,k}(u)=\sum_{j=k}^n\binom nj u^j(1-u)^{n-j},\qquad 0\le u\le1.
\]
Independence conditional on the absence of the common shock yields the exact survival function
\[
S_g(t):=\Pr(T_{n,k}(g)>t)=e^{-gt}B_{n,k}\big(e^{-(e-g)t}\big).
\]
In particular, no assumption of independent patch lifetimes is made when \(g>0\).

## Proof

**Step 1 (binomial-tail elasticity).** For \(1\le k<n\), differentiating and telescoping the binomial tail gives
\[
u B'_{n,k}(u)=k\binom nk u^k(1-u)^{n-k}.
\]
For \(0<u<1\), put
\[
R_{n,k}(u)=\frac{u B'_{n,k}(u)}{B_{n,k}(u)}
=\frac{k}{1+\sum_{j=k+1}^n \frac{\binom nj}{\binom nk}\left(\frac{u}{1-u}\right)^{j-k}}.
\]
Every summand in the denominator increases strictly with \(u\), so \(R_{n,k}\) decreases strictly from \(k\) to \(0\) as \(u\) runs from \(0\) to \(1\). For \(k=n\), \(B_{n,n}(u)=u^n\) and \(R_{n,n}(u)=n\) identically.

**Step 2 (the log survival ratio).** Write \(a=e-g_1\) and \(b=e-g_2\), so \(a>b\ge0\). For fixed \(t>0\), the formula above yields
\[
S_g(t)=e^{-et}\frac{B_{n,k}(e^{-(e-g)t})}{e^{-(e-g)t}}.
\]
Differentiating the logarithm with respect to the local rate \(s=e-g\) and applying the fundamental theorem of calculus gives the exact identity
\[
F(t):=\frac1t\log\frac{S_{g_2}(t)}{S_{g_1}(t)}
=\int_b^a\big(R_{n,k}(e^{-st})-1\big)\,ds.
\]
The endpoint \(s=0\) is harmless: its value affects no integral, and the original survival formula is continuous at \(g=e\).

**Step 3 (strict classification).** If \(k=1\), then \(0<R_{n,1}(u)<1\) whenever \(0<u<1\), so \(F(t)<0\). If \(k=n\), then \(F(t)=(n-1)(a-b)>0\). Suppose \(2\le k<n\). For each \(s>0\), \(e^{-st}\) decreases strictly as \(t\) grows. Since \(R_{n,k}\) decreases strictly in its argument, \(t\mapsto F(t)\) increases strictly. By bounded convergence,
\[
\lim_{t\downarrow0}F(t)=-(a-b)<0,
\qquad
\lim_{t\to\infty}F(t)=(k-1)(a-b)>0.
\]
At the possible single endpoint \(s=0\), the limit differs but does not affect the integral. Continuity and strict monotonicity imply that exactly one zero exists, and multiplication by positive \(t\), followed by exponentiation, gives the asserted strict crossing signs. This proves the theorem for the entire real parameter ranges, including the boundary values \(g_1=0\) and \(g_2=e\).

**Step 4 (exact minimal-quorum mean).** For \((n,k)=(3,2)\), \(B_{3,2}(u)=3u^2-2u^3\), so
\[
S_g(t)=3e^{-(2e-g)t}-2e^{-(3e-2g)t}.
\]
Both exponential exponents are positive for \(0\le g\le e\); integrating from zero to infinity yields
\[
\mathbb E T_{3,2}(g)=\frac3{2e-g}-\frac2{3e-2g}
=\frac{5e-4g}{(2e-g)(3e-2g)}.
\]
Setting \(x=g/e\) gives
\[
\frac{d}{dx}\big(e\mathbb E T_{3,2}(ex)\big)
=\frac{8x^2-20x+11}{(2-x)^2(3-2x)^2}.
\]
The numerator has roots \((5-\sqrt3)/4\in(0,1)\) and \((5+\sqrt3)/4>1\), and changes from positive to negative at the first. The denominator is positive for \(0\le x\le1\). Hence the first root is the unique maximizer, with the stated maximum. At the two endpoints the means are \(5/(6e)\) and \(1/e\), respectively, both strictly smaller.

## Verification

A self-contained Python 3 standard-library file \(`verify.py`\) implements the displayed survival formula independently of a finite-state continuous-time Markov chain uniformization of the occupied-patch count. It checks 1,142 deterministic comparisons, including exact mean identities, numerical parameter grids for all three quorum classes, and samples of the crossing property. Run \(`python3 verify.py`\); the expected terminal line begins \(`PASS: 1142`\). The proof above is analytic: the numerical grid neither establishes the continuous parameter range nor the uniqueness claim by itself.

The critical identities required for an infinite-parameter proof are the binomial-tail derivative, strictly decreasing elasticity, the exact logarithmic ratio integral and its two strict endpoint limits. The mean-maximization assertion follows from a complete quadratic sign classification, not optimization software.

## Relationship to prior work

Johst and Drechsler (2003) motivate the question of how spatially correlated disturbance affects patch persistence, but their spatially explicit destruction/regeneration metapopulation includes recolonization and concerns extinction of the entire metapopulation. It does not imply a one-crossing theorem for a fixed-number-of-patches quorum with equal single-patch hazard.

The classical Marshall–Olkin common-shock construction (1967) already contains the dependence mechanism. Bayramoglu and Ozkut (2015) study the reliability and mean failure time of coherent systems under such shocks; their accessible abstract, not the complete article, establishes strong generic relevance, so no claim of historical priority relative to all of its results is made. Ozkut and Kan (2020), whose relevant general reliability formula was inspected, consider coherent systems under shock mechanisms; obtaining a particular survival function from those formulas is not the same as proving the strict single-crossing order for every \(n,k\) under compensating local hazards, or its sharp three-patch interior mean optimum. The new derivation explicitly fixes each marginal hazard as \(g\) changes; comparisons where a common-shock rate increases while local rates remain fixed address a different parameter family.

## Limitations

This theorem compares viability at a finite horizon under irreversible, exponential local extinction and a perfectly simultaneous common catastrophe. It makes no claim about recolonization, realistic landscape dynamics, arbitrary partially shared shocks, heterogeneous marginal risks, a random or changing quorum, alternative dependence families, or long-run persistence with reproduction. The source comparison is provisional: the complete 2015 article and its 2016 follow-up were not accessible for page-by-page inspection, so historical priority is not independently established. Numerical tests are supplementary, not a computer-assisted proof of all possible \(n,k,e,g,t\).

## References

1. A. W. Marshall and I. Olkin (1967), A multivariate exponential distribution, *Journal of the American Statistical Association* 62, 30–44.
2. K. Johst and M. Drechsler (2003), Are spatially correlated or uncorrelated disturbance regimes better for the survival of species?, *Oikos* 103, 449–456. First published 21 October 2003. https://doi.org/10.1034/j.1600-0706.2003.12770.x
3. I. Bayramoglu and C. M. Ozkut (2015), The Reliability of Coherent Systems Subjected to Marshall–Olkin Type Shocks, *IEEE Transactions on Reliability* 64, 435–443. https://doi.org/10.1109/TR.2014.2338252
4. I. Bayramoglu and C. M. Ozkut (2016), Mean residual life and inactivity time of a coherent system subjected to Marshall–Olkin type shocks, *Journal of Computational and Applied Mathematics* 298, 190–200. https://doi.org/10.1016/j.cam.2015.12.009
5. M. Ozkut and C. Kan (2020), On the coherent systems subject to Marshall–Olkin type shocks, *Mathematical Sciences and Applications E-Notes* 8, 2020. https://doi.org/10.36753/mathenot.621901
