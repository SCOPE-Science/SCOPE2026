# Exact fourth-order dependence and a sharp exponential-moment cutoff in coordinate-sampled Langevin

## Finding
Consider the full-noise, randomly selected-coordinate Langevin iteration defined below, applied to an isotropic Gaussian target. A scalar reduction of its Gaussian innovation variance can exactly match the target covariance at every stable positive step size, but the invariant distribution remains non-Gaussian in a quantifiable and unavoidable way.

Write \(c=1-dah\). For every dimension \(d\ge 2\), precision \(a>0\), and step \(0<h<2/(da)\), let \(\pi_h\) be the unique invariant distribution of the calibrated iteration. Every coordinate \(i\) satisfies
\[
\mathbb E_{\pi_h} X_i=0,\qquad \mathbb E_{\pi_h}X_i^2=\frac1a,
\qquad \frac{\mathbb E_{\pi_h}X_i^4}{(\mathbb E_{\pi_h}X_i^2)^2}-3
=\frac{3(d-1)(1-c^2)}{d(1+c^2)}>0.
\]
For every distinct pair \(i\ne j\),
\[
\operatorname{Cov}_{\pi_h}(X_i^2,X_j^2)=-\frac{1-c^2}{2da^2}<0.
\]
Thus exact target covariance does not restore either Gaussian marginals or the independence of squared coordinates.

At the distinguished step \(h=1/(da)\), a selected coordinate is completely reset. Each stationary coordinate is the Gaussian scale mixture
\[
X_i\mid A_i=k\sim N\!\left(0,\frac{k+1}{da}\right),
\qquad \Pr(A_i=k)=\frac1d\left(1-\frac1d\right)^k,\quad k=0,1,2,\ldots.
\]
Its moment-generating function is exactly
\[
\mathbb E_{\pi_h}e^{tX_i}
=\frac{\exp(t^2/(2da))}{d-(d-1)\exp(t^2/(2da))}
\quad\text{if}\quad |t|<\sqrt{2da\log\!\left(\frac d{d-1}\right)},
\]
and is infinite outside this open interval, including its endpoints. Hence covariance-exact calibration does not yield sub-Gaussian stationary marginals, even for a Gaussian target.

## Assumptions and scope
Fix an integer \(d\ge2\), scalar \(a>0\), and positive step \(h\) with \(0<h<2/(da)\). The target is \(N(0,a^{-1}I_d)\). Let \(J_n\) be independent uniform choices from \(\{1,\ldots,d\}\), and let \(\xi_n\) be independent standard \(d\)-dimensional Gaussian random vectors, independent of all \(J_n\). Define \(E_j=e_je_j^{\mathsf T}\), and set
\[
\beta=1-\frac{dah}{2}>0,
\qquad X_{n+1}=(I_d-dahE_{J_n})X_n+\sqrt{2h\beta}\,\xi_n.
\]
This is a scalar-noise-calibrated version of the *full-noise*, one-coordinate-gradient overdamped Langevin update, not a sampler that updates only its selected coordinate. The scalar noise calibration is a second-moment identity already accessible by elementary covariance analysis; it is not itself the new claim. Assertions concern the unique invariant law, not a finite-time law and not a general non-isotropic potential.

## Proof
**Existence and moments.** Put \(p=1/d\), \(c=1-dah\in(-1,1)\), and \(v=2h\beta>0\). For fixed \(i\), the recurrence is
\[
X_{n+1,i}=A_{n,i}X_{n,i}+\eta_{n,i},\qquad
\Pr(A_{n,i}=c)=p,\quad \Pr(A_{n,i}=1)=1-p,
\]
where \(\eta_{n,i}\) are independent \(N(0,v)\), independent of the selecting variables and past. Coupling two copies using the same selections and innovations gives
\[
\mathbb E\|X_{n+1}-Y_{n+1}\|^2=u\,\mathbb E\|X_n-Y_n\|^2,
\quad u=1-p(1-c^2)<1.
\]
This produces a stationary law with finite second moment and proves uniqueness among such laws by quadratic Wasserstein contraction. In fact the same coupling contracts any finite initial difference coordinatewise almost surely: every coordinate is selected infinitely often, so \(c^{N_i(n)}(X_{0,i}-Y_{0,i})\to0\) almost surely, where \(N_i(n)\) counts its selections. Thus no second stationary probability law with arbitrary moment behavior can coexist. To justify fourth-moment manipulations, a two-sided stationary coordinate can be expressed as a convergent sum of Gaussian innovations multiplied by products of past \(A_{n,i}\). For \(w=\mathbb E A_{n,i}^4=1-p(1-c^4)<1\), the \(L^4\) norms of its terms are bounded by \(3^{1/4}\sqrt v\,w^{k/4}\), giving finite fourth moments by Minkowski; the corresponding joint mixed fourth moments are finite by Cauchy–Schwarz. Sign symmetry gives zero means.

**Covariance and marginal kurtosis.** The invariant coordinate variance \(V\) obeys \(V=uV+v\). Since \(1-u=p(1-c^2)\) and \(v=(1-c^2)/(da)\), it follows that \(V=1/a\). For different coordinates, \(\mathbb E[A_{n,i}A_{n,j}]=1-2p(1-c)\); independent innovations yield a zero stationary cross-covariance. Thus \(\operatorname{Cov}(X)=a^{-1}I_d\). The stationary fourth moment \(M_4\) satisfies the exact Gaussian-innovation recurrence
\[
M_4=wM_4+6uvV+3v^2,
\]
so
\[
M_4=\frac{3}{a^2}\frac{2-p(1-c^2)}{1+c^2}
=\frac3{a^2}\left(1+\frac{(d-1)(1-c^2)}{d(1+c^2)}\right).
\]
This proves the positive excess kurtosis formula for every interior admissible step.

**Negative squared-coordinate covariance.** Since exactly one coordinate is selected per iteration, for distinct \(i,j\),
\[
T=\mathbb E[A_{n,i}^2A_{n,j}^2]=1-2p(1-c^2).
\]
Writing \(M_{22}=\mathbb E X_i^2X_j^2\), independence and centering of the Gaussian innovations imply
\[
M_{22}=TM_{22}+2uvV+v^2.
\]
Solving gives \(M_{22}=a^{-2}(1-(1-c^2)/(2d))\). Subtracting \(V^2\) proves the strictly negative squared-coordinate covariance.

**Exact reset-step mixture and its moment-generating boundary.** If \(h=1/(da)\), then \(c=0\), \(\beta=1/2\), and \(v=1/(da)\). Every selection of coordinate \(i\) erases its previous value; in each intervening unselected iteration, an independent \(N(0,v)\) increment accumulates. At a stationary time the number \(A_i\) of consecutive unselected steps since the last selection has the geometric law \(p(1-p)^k\), so conditional on \(A_i=k\), the coordinate is the sum of exactly \(k+1\) independent \(N(0,v)\) increments. This proves the stated mixture. The moment-generating function is the geometric series
\[
\sum_{k=0}^\infty p(1-p)^k \exp\!\left(\frac{(k+1)t^2}{2da}\right).
\]
Its ratio is \((1-p)\exp(t^2/(2da))\); summation is valid exactly when the ratio is strictly less than one. When the ratio is at least one, the nonnegative series diverges. This yields the claimed sharp exponential-moment threshold.

## Verification
Run `python3 check.py` using the Python standard library. Its exact-rational assertions reconstruct the invariant second-, fourth-, and cross-fourth-moment recurrences for several dimensions, precisions, and strictly stable rational steps; at the reset step they independently check the geometric-age specialization. The accompanying `check_output.txt` records actual execution. The infinite-series boundary and universal dimension/step claims are proved algebraically above, not inferred from finite test cases.

For \(d=2\), \(a=1\), \(h=1/2\), both stationary marginal variances equal one, but \(\mathbb E X_i^4=9/2\), \(\operatorname{Cov}(X_1^2,X_2^2)=-1/4\), and the marginal moment-generating function is finite exactly when \(|t|<2\sqrt{\log 2}\).

## Relationship to prior work
Ding and Li (2020) define and analyze full-noise random-coordinate overdamped Langevin sampling, establishing general Wasserstein convergence estimates rather than exact stationary fourth-order diagnostics. Ding, Li, Lu, and Wright (2020) analyze a distinct coordinate-only-noise and coordinate-only-state-update method; it cannot be substituted for the iteration here. The earlier stationary covariance calculation for this full-noise model is acknowledged and not presented as new: covariance matching alone does not imply fourth moments, squared-coordinate dependence, or an exponential-moment boundary. Another previously reported Gaussian-covariance-matched random-projection model has a nonzero excess-kurtosis formula; its fourth-order directional-design condition fails for the discrete set of coordinate-axis projectors. It therefore does not imply the all-dimensional cross-square law or the geometric reset-time mixture derived here.

Vollmer, Zygalakis, and Teh (2016) compute moments up to degree four for a different fixed-step stochastic-gradient Langevin toy model with a deterministic autoregressive coefficient and random additive data-driven forcing. Their Appendix 10 moment recurrences do not imply the multiplicative coordinate-selection formulas or the simultaneous squared-coordinate law here. Altschuler and Talwar (2022) obtain stationary concentration results under hypotheses including a uniform conditional sub-Gaussian gradient-noise control. In the present model the random-coordinate gradient error grows proportionally with the unbounded state, so that hypothesis is not applicable. These distinctions support a candidate-specific novelty assessment, not a proof that no earlier specialist result exists.

## Limitations
The analysis is for isotropic quadratic targets and independent full-dimensional Gaussian innovations. It does not claim that the uncalibrated published algorithm has unbiased covariance, nor that this scalar calibration is suitable for all target potentials. The exact marginal Gaussian scale mixture and bounded moment-generating domain are asserted only at the reset step, while the fourth-order laws cover the full stated stable interval. No total-variation rate, algorithmic efficiency improvement, or finite-sample confidence guarantee is established. Exact-rational checks are corroboration, not proof of universal assertions. Independent verification and a complete specialist publication search remain outstanding.

## References
- Zhiyan Ding and Qin Li, *Langevin Monte Carlo: Random Coordinate Descent and Variance Reduction*, arXiv:2007.14209, first posted 2020-07-26. https://arxiv.org/abs/2007.14209
- Zhiyan Ding, Qin Li, Jianfeng Lu, and Stephen J. Wright, *Random Coordinate Langevin Monte Carlo*, arXiv:2010.01405, first posted 2020-10-03. https://arxiv.org/abs/2010.01405
- Sebastian J. Vollmer, Konstantinos C. Zygalakis, and Yee Whye Teh, *Exploration of the (Non-)Asymptotic Bias and Variance of Stochastic Gradient Langevin Dynamics*, JMLR 17(159), 2016, Section 2 and Appendix 10. https://jmlr.csail.mit.edu/papers/v17/15-494.html
- Jason Altschuler and Kunal Talwar, *Concentration of the Langevin Algorithm's Stationary Distribution*, arXiv:2212.12629, 2022. https://arxiv.org/abs/2212.12629
