# Universal high-dropout spacing law for Brownian-bridge quadrature

## Finding
Let \(n\ge 2\) be fixed, let \(B\) be a standard zero-to-zero Brownian bridge on \([0,1]\), and let \(J=\int_0^1 B(t)\,dt\). Place \(n\) noiseless point sensors at deterministic ordered locations \(0\le x_1\le\cdots\le x_n\le1\). Each sensor independently returns its value with probability \(r=1-q\in(0,1)\), and its success/failure indicator is observed. Estimation uses the conditional mean of \(J\) from all returned values.

For every \(n\ge2\) and \(0<q<1\), the expected Bayes mean-square error has a **unique minimizer among ordered placements** \(x^*(q)\), which is reflection-symmetric. In the high-failure limit \(r\downarrow0\), its nodes obey the *universal, equally spaced microscopic law*
\[
\boxed{\displaystyle x_i^*(1-r)=\frac12+\frac{r}{8}(2i-n-1)+o(r),\qquad i=1,\ldots,n.}
\]
In particular, every node converges to the midpoint, but adjacent optimal nodes separate by \(r/4+o(r)\), not by a smaller order.

For \(n=2\) the unique optimal positions are exactly \(\tfrac12\mp d(q)\), where
\[
\boxed{\displaystyle d(q)=\frac{\sqrt{(1+q)^2+3(1-q)^2}-(1+q)}{6(1-q)},\qquad 0\le q<1.}
\]
Thus the two nodes remain strictly distinct at *every* positive survival probability; at \(q=0\) they are \(1/3,2/3\), while \(d(q)/(1-q)\to1/8\) as \(q\uparrow1\).

## Assumptions and scope
The Brownian bridge has covariance \(K(s,t)=\min(s,t)-st\), including known zero endpoint values. The sensor failures are mutually independent, independent of the bridge, and exchangeable. All successful observations are exact; the observer knows which measurements were lost. For each \(q\), the ordered positions may be selected in the closed simplex \(0\le x_1\le\cdots\le x_n\le1\), allowing coincident nodes. The claim is about expected *integral-estimation posterior variance*, not prediction of the entire path, mutual information, or worst-case geometric sensor coverage. The asymptotic holds with fixed finite \(n\), not in a simultaneous large-network limit.

## Proof
**1. Conditional bridge decomposition.** For a subset \(S=\{i_1<\cdots<i_k\}\) of surviving sensors, write \(t_0=0\), \(t_j=x_{i_j}\) for \(1\le j\le k\), and \(t_{k+1}=1\). Conditionally on the returned bridge values, the residual centered bridges on the disjoint gaps \([t_j,t_{j+1}]\) are independent. The integral of a Brownian bridge over a gap of length \(h\) has conditional variance \(h^3/12\), by covariance integration. The same formula holds by continuity when locations collide. Therefore the exact Bayes risk is
\[
R_q(x)=\frac1{12}\sum_{S\subseteq\{1,\ldots,n\}}(1-q)^{|S|}q^{n-|S|}\sum_{j=0}^{|S|}(t_{j+1}-t_j)^3.\tag{1}
\]
The empty-subset contribution is \(q^n/12\). This is an exact finite polynomial, not a Monte Carlo approximation.

**2. Existence, strict convexity, and symmetry.** Each gap length in (1) is a nonnegative affine function of an ordered \(x\). The function \(u\mapsto u^3\) is strictly convex on \([0,\infty)\). Consequently every subset's cost is convex. The all-surviving subset has positive weight \((1-q)^n\), and its \(n+1\) gap lengths uniquely determine the full ordered position vector. Its sum of cubes is strictly convex on the entire closed ordered simplex. Thus \(R_q\) is strictly convex and continuous, so it has exactly one ordered global minimizer. Reflection \(x_i\mapsto1-x_{n+1-i}\) preserves (1); uniqueness forces \(x_i^*=1-x_{n+1-i}^*\).

**3. Concentration at the midpoint with a linear scale.** Write \(r=1-q\), \(m=(1/2,\ldots,1/2)\), and \(\delta_i=x_i-1/2\). With exactly one surviving sensor at \(t\), direct conditioning gives
\[
V_1(t)=\frac1{12}-\frac{t(1-t)}4=\frac1{48}+\frac{(t-1/2)^2}{4}.
\]
For any fixed surviving subset, its cost in (1) is Lipschitz in each active location with one-sided derivative bounded in absolute value by \(1/4\) on the ordered simplex (the derivative is the difference of the squares of adjacent gaps, divided by \(4\)). Therefore, for any ordered \(x\), the contribution of subsets with at least two survivors to \(R_q(x)-R_q(m)\) is bounded below by
\[
-\frac{r(1-q^{n-1})}{4}\sum_i|\delta_i|\ge -\frac{(n-1)r^2}{4}\sum_i|\delta_i|.
\]
The singleton contributions are exactly \(rq^{n-1}\sum_i\delta_i^2/4\). Since \(R_q(x^*)\le R_q(m)\), Cauchy--Schwarz yields
\[
\bigl(\sum_i\delta_i^2\bigr)^{1/2}\le \frac{(n-1)\sqrt n\,r}{q^{n-1}}
\]
for the minimizer whenever \(0<r<1\). Hence \(x_i^*=1/2+O_n(r)\).

**4. The limiting convex energy and its unique optimizer.** Put \(x_i=1/2+r y_i\), where \(y_1\le\cdots\le y_n\) are bounded. Expanding (1) by the number of surviving sensors gives, uniformly for bounded ordered \(y\),
\[
R_{1-r}(m+ry)-R_{1-r}(m)
=r^3\left[\frac14\sum_{i=1}^n y_i^2-\frac1{16}\sum_{i<j}(y_j-y_i)\right]+O_{n,\|y\|_\infty}(r^4).\tag{2}
\]
Indeed one surviving sensor produces the positive quadratic term; for a given pair \(i<j\), the gap-cube formula gives \(V_{\{i,j\}}(m+ry)=1/48-r(y_j-y_i)/16+O(r^2)\), producing the attractive-to-spread term. Events with at least three survivors have probability \(O_n(r^3)\) and alter the co-located variance by \(O_n(r)\), so affect only the remainder.

The bracketed function \(G_n(y)\) in (2) is strictly convex. Using \(\sum_{i<j}(y_j-y_i)=\sum_i(2i-n-1)y_i\), its unique unconstrained minimizer is
\[
y_i^0=\frac{2i-n-1}{8},\qquad y_{i+1}^0-y_i^0=\frac14>0.
\]
Thus it is admissible in the ordered cone. The scale bound in step 3 makes the rescaled optimizers bounded. Every convergent subsequence must minimize \(G_n\) by the uniform expansion and comparison with arbitrary fixed ordered \(y\). Uniqueness gives \((x_i^*-1/2)/r\to y_i^0\) for each \(i\). This proves the universal asymptotic and strictly separated nodes for all sufficiently small \(r>0\).

**5. Exact two-sensor formula.** For \(n=2\), reflection forces the unique optimizer to be \(x_1=1/2-d\), \(x_2=1/2+d\), \(0\le d\le1/2\). The risk is
\[
R_q(d)=\frac{q^2}{12}+q(1-q)\left(\frac1{24}+\frac{d^2}{2}\right)+(1-q)^2\left(\frac1{48}-\frac d8+\frac{d^2}{4}+\frac{d^3}{2}\right).
\]
Its derivative vanishes precisely when \(12(1-q)d^2+4(1+q)d-(1-q)=0\). The polynomial is strictly increasing on nonnegative \(d\), negative at zero and positive at \(d=1/2\), so exactly one minimizer occurs in \((0,1/2)\). The positive quadratic root is the stated \(d(q)\). The limits follow by substitution and rationalization.

## Verification
A standalone script `verify_dropout.py` recomputes all conditional-variance identities, exact two-node stationarity equations, the fixed-size high-dropout expansions, and numerical minimizers for several small values of \(n\) and \(r\). Its finite tests are auxiliary reproducibility checks, not substitutes for the convexity and asymptotic proof above. The direct covariance-based variance calculation uses \(\operatorname{Var}(J)=1/12\), \(\operatorname{Cov}(J,B_t)=t(1-t)/2\), and \(\operatorname{Cov}(B_s,B_t)=\min(s,t)-st\).

## Relationship to prior work
Friedrich--Gallon--Pumir--Grauer [1] develop multipoint Brownian/fractional-Brownian interpolation for prescribed, nonuniform known samples, without a random-loss design theorem. Pronzato--Zhigljavsky [2] develop Bayesian quadrature and kernel-energy design in general, but do not give a failure-aware Brownian-bridge high-dropout spacing law. Santin [3] establishes equal spacing for a no-failure Brownian-bridge interpolation power-function criterion, distinct from the expected integral variance here. Krause--Singh--Guestrin [4] study robust mutual-information sensor selection under node failure, not this continuous-node Bayes integral risk. Frasca--Garin--Gerencsér--Hendrickx [5] study the same independent-failure mechanism with a *maximum-distance coverage loss*: their optimal sensors co-locate at the midpoint for all sufficiently high failure rates. The present integral-risk objective instead has an explicit nonzero \((1-q)/4\) asymptotic adjacent spacing, and a completely explicit two-node solution. These objective differences prevent implication from the cited theorems. Publication-priority assessment is provisional.

## Limitations
No result is claimed for noisy surviving values, failures depending on the bridge, other kernels or path functionals, adaptive location choice, or a joint \(n\to\infty\), \(q\to1\) limit. For general fixed \(n\), the exact optimal positions at intermediate failure probabilities are characterized uniquely by a finite strictly convex objective but not given in closed form. Finite numerical experiments do not establish the asymptotics. The literature comparison may miss older or unpublished exact specializations; no independent validation has been performed.

## References
[1] J. Friedrich, S. Gallon, A. Pumir, R. Grauer, *Stochastic interpolation of sparsely sampled time series via multi-point fractional Brownian bridges*, arXiv:2005.07591, initially public 2020-05-15. https://arxiv.org/abs/2005.07591

[2] L. Pronzato, A. Zhigljavsky, *Bayesian quadrature and energy minimization for space-filling design*, arXiv:1808.10722 (2018); later SIAM/ASA Journal on Uncertainty Quantification (2020). https://arxiv.org/abs/1808.10722

[3] G. Santin, *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, arXiv:2210.15959 (2022). https://arxiv.org/abs/2210.15959

[4] A. Krause, A. Singh, C. Guestrin, *Near-optimal sensor placements in Gaussian processes: theory, efficient algorithms and empirical studies*, JMLR 9 (2008), §6. https://jmlr.org/papers/v9/krause08a.html

[5] P. Frasca, F. Garin, B. Gerencsér, J. M. Hendrickx, *Optimal one-dimensional coverage by unreliable sensors*, arXiv:1404.7711, §5 (2014). https://arxiv.org/abs/1404.7711
