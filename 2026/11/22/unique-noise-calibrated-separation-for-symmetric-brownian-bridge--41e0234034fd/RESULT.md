# Unique noise-calibrated separation for symmetric Brownian-bridge path reconstruction

## Finding
Let \(B\) be a standard centered Brownian bridge on \([0,1]\), with covariance \(K(s,t)=\min(s,t)-st\). Fix any observation-noise variance \(\eta>0\). Among **reflection-symmetric** designs consisting of two independent noisy observations at \(x=(1-a)/2\) and \(y=(1+a)/2\), where \(0\le a\le1\), the integrated posterior path variance
\[
\mathcal E_\eta(a)=\int_0^1\operatorname{Var}\bigl(B(t)\mid B(x)+\varepsilon_1,B(y)+\varepsilon_2\bigr)\,dt
\]
has exactly one minimizer \(a=a_\eta\), which satisfies \(0<a_\eta<1/3\). The two noises are independent centered Gaussians, each of variance \(\eta\), and independent of \(B\).

Set \(z=a/(1-a)\). Define the sextic
\[
\begin{aligned}
P_\eta(z)={}&32\eta^3z^6+(144\eta^3+40\eta^2)z^5\\
&+(256\eta^3+112\eta^2+16\eta)z^4\\
&+(224\eta^3+98\eta^2+18\eta+2)z^3\\
&+(96\eta^3+18\eta^2-2\eta-1)z^2\\
&+(16\eta^3-10\eta^2-4\eta)z-2\eta^2.
\end{aligned}
\]
For each \(\eta>0\), this polynomial has **exactly one positive real root** \(z_\eta\), and this root lies in \((0,1/2)\). The unique optimal separation is \(a_\eta=z_\eta/(1+z_\eta)\).

The exact risk is \(\mathcal E_\eta(a_\eta)=1/6-G_\eta(a_\eta)\), where
\[
G_\eta(a)=\frac{(1-a)^2\left[2\eta(1+a)^2+a(1-a)(1+3a)\right]}{12(1-a+2\eta)\left[a(1-a)+2\eta\right]}.
\]
The optimal separation satisfies \(a_\eta=1/3-(2/3)\eta+O(\eta^2)\) as \(\eta\downarrow0\) and \(a_\eta\sim1/(8\eta)\) as \(\eta\to\infty\). In particular it is **positive at every finite positive noise variance**. It strictly beats every design that observes the same location twice, even when that location is allowed to vary freely over \([0,1]\).

## Assumptions and scope
The target is integrated mean-square **path reconstruction**, not estimation of the random integral \(\int_0^1 B(t)dt\). The two observations have equal finite independent noise and unrestricted real-valued posterior linear estimation; their positions are required to be reflections about \(1/2\). Coincident sites \(a=0\) and endpoint sites \(a=1\) are included in the admissible symmetric class. The theorem does **not** assert that the same pair is globally optimal among all asymmetric two-site configurations, or under unequal/correlated noises or alternate loss weights.

## Proof
Let \(X=(x,y)\). Gaussian conditioning gives the posterior covariance \(K(t,u)-k_X(t)^\mathsf{T}(K_X+\eta I)^{-1}k_X(u)\), where \(K_X=(K(x_i,x_j))_{i,j=1}^2\) and \(k_X(t)=(K(t,x),K(t,y))^\mathsf{T}\). Because \(\eta>0\), the inverse exists even for repeated sites. Integrating the diagonal, \(\int_0^1K(t,t)dt=1/6\), and the reduction is \(\operatorname{tr}[(K_X+\eta I)^{-1}C_X]\), with \(C_X(i,j)=\int_0^1K(t,x_i)K(t,x_j)dt\).

For arbitrary \(0\le x\le y\le1\), direct integration on the three subintervals yields
\[
C_X(1,1)=\frac{x^2(1-x)^2}{3},\quad C_X(2,2)=\frac{y^2(1-y)^2}{3},\quad C_X(1,2)=\frac{x(1-y)(2y-x^2-y^2)}6.
\]
Also \(K_X(1,1)=x(1-x)\), \(K_X(2,2)=y(1-y)\), and \(K_X(1,2)=x(1-y)\). Substituting \(x=(1-a)/2\) and \(y=(1+a)/2\) into the explicit two-by-two inverse establishes the displayed rational formula for \(G_\eta(a)\) for every \(a\in[0,1]\).

Direct differentiation and rational clearing, with \(z=a/(1-a)\), gives for \(0\le a<1\)
\[
G'_\eta(a)=-\frac{(1-a)^7P_\eta(a/(1-a))}{6(1-a+2\eta)^2\left[a(1-a)+2\eta\right]^2}.
\]
All denominator factors are strictly positive. In ascending order, the coefficients of \(P_\eta\) are
\[
-2\eta^2,\quad 2\eta(8\eta^2-5\eta-2),\quad 96\eta^3+18\eta^2-2\eta-1,
\]
followed by four strictly positive coefficients. If the linear coefficient is positive, then \(\eta>(5+\sqrt{89})/16>1/2\), which forces the quadratic coefficient to be positive as well. Thus the nonzero coefficients have precisely one sign change, for **every** \(\eta>0\). Descartes' rule of signs gives at most one positive root, counted with multiplicity. Since \(P_\eta(0)=-2\eta^2<0\) and the leading coefficient is positive, continuity gives a positive root, which is necessarily unique and simple. The derivative identity therefore proves strict increase of \(G_\eta\) before this root and strict decrease afterward, establishing the unique global minimum of \(\mathcal E_\eta\) within the symmetric class. Moreover \(P_\eta(1/2)=3\eta(6\eta+1)(18\eta+1)/4>0\), so \(z_\eta<1/2\), giving \(a_\eta<1/3\).

At zero noise the positive-root branch tends to \(z=1/2\). It is simple there: implicit differentiation at \(a=1/3,\eta=0\) yields \(da/d\eta=-2/3\), proving the small-noise expansion. For large noise, put \(z=c/\eta\) in \(P_\eta(z)=0\). After division by \(\eta^2\), the leading balance is \(16c-2=0\), giving \(z_\eta\sim1/(8\eta)\) and the same asymptotic for \(a_\eta\). To make the last statement rigorous, note that the unique root lies in \((0,1/2)\) and its defining polynomial has positive leading powers for every fixed positive \(z\), which forces \(z_\eta\to0\); the nonnegative terms then bound \(\eta z_\eta\) above and below away from zero and infinity, allowing the stated balance.

Finally, two independent observations at one arbitrary location \(x\) have reduction \(2v^2/[3(\eta+2v)]\), with \(v=x(1-x)\in[0,1/4]\). This is strictly increasing in \(v>0\), so the best repeated site is \(x=1/2\), with gain \(G_\eta(0)=1/[12(1+2\eta)]\). But \(G'_\eta(0)=1/[12(1+2\eta)^2]>0\). Hence the uniquely optimal symmetric separated pair strictly improves upon **every** coincident pair without assuming reflection symmetry for the repeated location.

## Verification
The standalone `verify.py` recomputes the piecewise kernel-product integral, the exact two-point gain, the derivative-to-sextic identity, the polynomial value at \(1/2\), the collocation comparison, and 70 exact rational design checks using SymPy. It also prints illustrative numerical root locations. Execute with `python verify.py` in an environment with SymPy; expected results are in `VERIFIER_OUTPUT.txt`. The root uniqueness, all-noise sign classification, and endpoint asymptotics follow from the proof rather than finite tests.

For example, when \(\eta=1/10\), the unique symmetric optimum has separation \(a_\eta\approx0.274203082773\), nodes approximately \(0.362898458614\) and \(0.637101541386\). The corresponding integrated posterior variance is about \(0.08497416\), compared with \(0.09722222\) for the best repeated-midpoint design.

## Relationship to prior work
Gaussian conditional moments and noisy Gauss–Markov path reconstruction are treated by Davies (2024); the cited preprint gives prediction formulas but no finite-noise optimal reflection-symmetric two-location equation in the examined main text. Brownian-bridge IMSE designs without measurement noise and Brownian-bridge designs with an additional unknown straight-line regression component appear in the earlier works of Mukherjee (2001/2003) and in the 2023 Metrika article. The latter explicitly distinguishes its zero-noise equidistant result from its noisy regression/misspecification model. The present theorem treats **known-zero-mean bridge, finite independent measurement noise, and the full integrated posterior covariance**, rather than a noiseless bridge or a noisy parametric regression objective. It is not a claim of novelty for the Gaussian-conditioning formula or the noiseless equispaced limit.

## Limitations
Only reflection-symmetric two-site designs are classified globally. Full unrestricted two-site optimality, more observations, unequal variances, correlated noise, and alternative spatial risk weights remain unproved. Independent publication-priority review has not been performed. The historical Mukherjee dissertation was accessible only via abstract during comparison, so previously unexamined details could potentially affect originality; historical equivalence in Gaussian optimal design remains a residual risk. Computational checks are illustrative and do not certify the continuum argument independently.

## References
1. B. Davies, *Estimating sample paths of Gauss-Markov processes from noisy data*, arXiv:2404.00784, first posted 2024-03-31. https://arxiv.org/abs/2404.00784
2. *Robust optimal designs using a model misspecification term*, Metrika **86** (2023), 781–804, published online 2023-02-08. https://doi.org/10.1007/s00184-023-00893-6
3. B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Purdue University dissertation (2001), abstract available at https://docs.lib.purdue.edu/dissertations/AAI3043760/
4. J. Foster, T. Lyons, H. Oberhauser, *An Optimal Polynomial Approximation of Brownian Motion*, arXiv:1904.06998, first posted 2019-04-15. https://arxiv.org/abs/1904.06998
