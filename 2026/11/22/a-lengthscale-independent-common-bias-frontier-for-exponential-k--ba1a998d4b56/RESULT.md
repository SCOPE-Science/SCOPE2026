# A lengthscale-independent common-bias frontier for exponential-kernel quadrature

## Finding
Let a zero-mean unit-variance stationary Gaussian process on \([0,1]\) have covariance \(k_\lambda(s,t)=\exp(-\lambda|s-t|)\), where \(\lambda>0\). Observe it at all \(n\ge2\) equispaced nodes, including both endpoints, with a *single shared* independent centered Gaussian offset of variance \(\tau\ge0\) added to every observation. Use the exact Gaussian posterior mean to estimate the Lebesgue integral of the process.

Write
\[
 r=e^{-\lambda/(n-1)},\qquad u=\frac{1-r}{\lambda(1+r)},\qquad
 D=1+\tau\frac{2+(n-2)(1-r)}{1+r}.
\]
The unique posterior-mean quadrature weights are
\[
 w_1=w_n=\frac{u[1-(n-2)\tau]}D,\qquad
 w_i=\frac{2u(1+\tau)}D\quad(2\le i\le n-1).
\]
All weights are strictly positive for \(n=2\) and every finite \(\tau\ge0\). For \(n\ge3\), all weights are nonnegative **if and only if** \(\tau\le1/(n-2)\), with strict positivity if and only if the inequality is strict. Above this sharp boundary exactly the two endpoint weights are negative, independently of the correlation length \(1/\lambda\). The negative-weight mass, also the sharp magnitude of the most negative estimator output on sampled values in \([0,1]\), is
\[
 H_n=\frac{2u}{D}\max\{0,(n-2)\tau-1\}.
\]
For every fixed \(\lambda>0\) and \(\tau\ge0\), the associated signed nodal quadrature measures converge weakly, as \(n\to\infty\), to
\[
 \frac{(1+\tau)\,\mathrm dt-\frac\tau2(\delta_0+\delta_1)}{1+\tau(1+\lambda/2)}.
\]
Thus any fixed positive common-offset variance eventually causes negative endpoint weights whose total mass persists in the dense-grid limit. In contrast, replacing the single common offset by independent, equally distributed observation errors of **any** finite variance \(\eta\ge0\) retains strictly positive weights on the same grids.

## Assumptions and scope
The integration interval is exactly \([0,1]\) with Lebesgue probability measure. The covariance amplitude at zero separation is normalized to one. The sites are exactly \(x_i=(i-1)/(n-1)\), with one observation per site. The shared-error model is \(Y_i=X(x_i)+Z\), where \(Z\sim N(0,\tau)\) is a *single* variable common to all observations, independent of \(X\). There is no independent nugget in this model. The target is \(J=\int_0^1X(t)\,\mathrm dt\), and the estimator is \(\mathbb E[J\mid Y_1,\dots,Y_n]\). Only \(n\ge2\), \(\lambda>0\), \(\tau\ge0\) are claimed. The independent-error comparison uses separate \(N(0,\eta)\) noises, independent of each other and \(X\).

## Proof
Set \(K_{ij}=r^{|i-j|}\), \(\mathbf 1=(1,\ldots,1)^\mathsf T\), and \(m_i=\int_0^1 k_\lambda(x_i,t)\,\mathrm dt\). Gaussian conditioning gives the unique weight vector
\[
 w=(K+\tau\mathbf1\mathbf1^\mathsf T)^{-1}m.
\]
The matrix \(K\) is strictly positive definite because \(0<r<1\). Its precision \(Q=K^{-1}\) is tridiagonal, equal to \((1-r^2)^{-1}\) times the matrix with diagonal entries \(1\) at the endpoints and \(1+r^2\) internally, and adjacent off-diagonal entries \(-r\). This identity follows by multiplication with \(K\), including for \(n=2\).

Direct integration yields
\[
 m_i=\frac{2-r^{i-1}-r^{n-i}}\lambda.
\]
Multiplication by the tridiagonal precision, using cancellation of the two geometric sequences in every interior row, gives
\[
 v:=Qm=u(1,2,\ldots,2,1)^\mathsf T.
\]
Multiplication of \(Q\) by the all-ones vector likewise gives
\[
 b:=Q\mathbf1=\frac1{1+r}(1,1-r,\ldots,1-r,1)^\mathsf T.
\]
Consequently \(\mathbf1^\mathsf Tv=2(n-1)u\) and \(\mathbf1^\mathsf Tb=[2+(n-2)(1-r)]/(1+r)\). The rank-one inverse identity gives
\[
 w=v-\frac{\tau b\,\mathbf1^\mathsf Tv}{1+\tau\mathbf1^\mathsf Tb}.
\]
Substitution and simplification give the displayed endpoint and interior formulas. As \(u,D,1+\tau\) are strictly positive, only the factor \(1-(n-2)\tau\) controls the sign. For \(n=2\) this factor is one; for \(n\ge3\) its unique zero is \(1/(n-2)\). For sampled values in \([0,1]\), the smallest possible weighted sum is precisely the sum of its negative coefficients: set the samples to one at strictly negative weights and to zero at strictly positive weights, with arbitrary samples at weights equal to zero. This proves the formula for \(H_n\). Above the frontier this gives the two endpoint samples equal to one and all other samples zero. When all weights are nonnegative, the all-zero vector attains the minimum zero.

For the weak limit, set \(h=1/(n-1)\). As \(n\to\infty\), \(u/h\to1/2\) and \(\mathbf1^\mathsf Tb\to1+\lambda/2\). Each endpoint weight therefore tends to \(-\tau/[2(1+\tau(1+\lambda/2))]\), while every interior weight divided by \(h\) tends to \((1+\tau)/[1+\tau(1+\lambda/2)]\). Evaluating against an arbitrary continuous test function and invoking convergence of the interior Riemann sum establishes precisely the signed weak limit, including \(\tau=0\).

For independent observation errors with covariance \(\eta I\), the weight vector solves \((I+\eta Q)w=v\). The tridiagonal matrix \(Q\) has strictly positive diagonal entries, strictly negative off-diagonals and strictly positive row sums. Therefore \(I+\eta Q\) is a strictly row-diagonally-dominant nonsingular \(M\)-matrix, with entrywise nonnegative inverse. Since \(v\) is strictly positive, the resulting \(w\) is strictly positive for every \(\eta\ge0\). This comparison does not assert positivity for arbitrary correlated-error covariances.

## Verification
The standalone script `verification/verify.py` reconstructs the kernel system from both sides, checks the displayed rank-one identities using exact rational surrogate correlations, and independently solves the physical exponential-covariance systems numerically. Executing `python verification/verify.py` with the packages in `verification/requirements.txt` returned `PASS 660 exact rational tests and 210 numerical kernel-system tests`. The exact tests cover \(2\le n\le34\), several rational \(0<r<1\) and \(\tau\ge0\), while the numerical tests include genuine exponential correlations and independent matrix solves. The proof above, not those finite tests, establishes the claims for all real allowed parameters and all integer node counts.

## Relationship to prior work
The posterior-mean formula and importance of positive Bayesian quadrature weights are standard; see Karvonen, Kanagawa and Särkkä (2018/2019), especially their formulation of quadrature weights and discussion of Matérn-kernel positivity. Their reviewed sufficient conditions concern noiseless kernel quadrature and do not imply a sign law for a rank-one *measurement-noise* covariance. Cai, Lam and Scarlett (2022/2023) investigate noisy kernel quadrature and average-case error rates with independently distributed Gaussian observation noise; they do not study the present shared-offset sign frontier. Both papers supply motivation and baseline techniques, not the specific threshold, exact weights or signed weak limit claimed here.

The independent-noise statement is a comparison, not a priority claim. The related exponential-kernel subprobability theorem [3] treats arbitrary ordered sites, nonnegative target measures, and nonnegative diagonal nuggets. In particular its strict-positivity conclusion applies here for \(\eta>0\), while the noiseless case follows directly from \(v=Qm\) above. Its diagonal-noise hypothesis excludes the shared offset.

## Limitations
These formulas require a stationary exponential covariance, exact equispacing including endpoints, a unit-amplitude kernel, and the indicated pure rank-one common offset. They are not a statement about a constant term *in the latent kernel*: the cross-covariance with the integral must remain \(m\), not \(m+\tau\mathbf1\). An independent nugget mixed with common noise, nonuniform grids, other integration densities, non-Gaussian errors or other kernels may change the frontier. Positive or negative posterior-mean weights do not by themselves determine quadrature accuracy or the posterior variance. The priority comparison is limited to inspected works; exhaustive historical priority is not asserted.

## References
1. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*. arXiv:1812.08509, first publicly posted 20 December 2018; *Statistics and Computing* 29 (2019), 1317–1333. https://arxiv.org/abs/1812.08509 ; https://doi.org/10.1007/s11222-019-09901-0
2. X. Cai, C. T. Lam and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*. arXiv:2202.10615, first publicly posted 22 February 2022; TMLR (2023). https://arxiv.org/abs/2202.10615
3. *Universal subprobability weights for exponential-kernel quadrature and a sharp smoothness obstruction*, Resultary finding (22 November 2026), https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-universal-subprobability-weights-for-exponential-kernel-quadratu--43f5dd97bf96/RESULT.md
