# Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature

## Finding

For a centered stationary Gaussian process on \([0,1]\) with covariance
\[
K(s,t)=\sigma^2\exp(-\lambda|s-t|),\qquad \sigma^2>0,\ \lambda>0,
\]
consider the Bayesian posterior variance \(V_n(T)\) of the integral \(I=\int_0^1 X(t)\,dt\), conditional on \(n\) noiseless point values at distinct, freely chosen times \(T=(t_1,\ldots,t_n)\). For every \(n\ge2\), the **unique** global minimizer has equally spaced interior points and equal nonzero terminal margins:
\[
t_j=a_n+(j-1)h_n,\quad
n h_n+\frac2\lambda\log\cosh\left(\frac{\lambda h_n}{2}\right)=1,\quad
a_n=\frac{h_n}{2}+\frac1\lambda\log\cosh\left(\frac{\lambda h_n}{2}\right),
\]
where the displayed scalar equation has a unique solution \(0<h_n<1/n\). For one point the unique optimum is \(t_1=1/2\). The exact optimal variance is given in the proof by a finite expression in \(a_n,h_n\).

For a separate randomized design, take independent \(U_i\sim\operatorname{Uniform}(0,1)\) and \(t_i=(i-1+U_i)/n\). Write \(V_n^{\rm jit}\) for its conditional integral variance. Then
\[
 n^2 V_n^{\rm opt}\longrightarrow\frac{\sigma^2\lambda}{6},\qquad
 n^2\mathbb E[V_n^{\rm jit}]\longrightarrow\frac{\sigma^2\lambda}{4},\qquad
 \frac{\mathbb E[V_n^{\rm jit}]}{V_n^{\rm opt}}\longrightarrow\frac32.
\]
More precisely, random observation placement exhibits Gaussian variance fluctuations:
\[
\sqrt n\left(n^2V_n^{\rm jit}-\frac{\sigma^2\lambda}{4}\right)
\ \xrightarrow{d}\ N\left(0,\frac{11\sigma^4\lambda^2}{864}\right).
\]
These statements concern posterior **integral** variance, not the spatially integrated point-prediction error.

## Assumptions and scope

Fix \(\sigma^2>0\), \(\lambda>0\). All designs use \(n\) distinct points in the closed unit interval and observe the Gaussian process exactly, without measurement noise. The mean is known to be zero, as are the covariance parameters. The weights of the Bayesian integral estimator are determined by Gaussian conditioning, not constrained to be equal. The randomized design uses one point independently uniformly in each regular interval, and expectation is over design randomness only. The process and observations need not be simulated to compute \(V_n\), which is a deterministic function of the locations. All limits hold with \(\lambda,\sigma^2\) fixed as \(n\to\infty\).

## Proof

**1. Exact additive decomposition.** Define the dimensionless functions, for \(x\ge0\),
\[
 b(x)=2x-3+4e^{-x}-e^{-2x},\qquad
 v(x)=2x-4\tanh(x/2).
\]
For sorted sampling times, let \(g_0=t_1\), \(g_i=t_{i+1}-t_i\) for \(1\le i<n\), and \(g_n=1-t_n\). The OU Gaussian Markov property makes disjoint open-gap conditional residuals independent given all observations. The unconditional integral variance on a gap of length \(\ell\) equals \(\sigma^2\lambda^{-2}2(\lambda\ell-1+e^{-\lambda\ell})\). Conditioning on its two endpoint observations removes \(2\sigma^2\lambda^{-2}(1-e^{-\lambda\ell})^2/(1+e^{-\lambda\ell})\), giving \(\sigma^2\lambda^{-2}v(\lambda\ell)\). On a terminal gap, conditioning on its single adjacent endpoint removes \(\sigma^2\lambda^{-2}(1-e^{-\lambda\ell})^2\), leaving \(\sigma^2\lambda^{-2}b(\lambda\ell)\). Thus, exactly,
\[
\boxed{\displaystyle
V_n(T)=\frac{\sigma^2}{\lambda^2}
\left[b(\lambda g_0)+\sum_{i=1}^{n-1}v(\lambda g_i)+b(\lambda g_n)\right].}
\]
No covariance across gap residuals remains, including at endpoints, by the Markov bridge decomposition. The identity also holds for \(n=1\) with the empty interior sum.

**2. Unique global optimal design.** Differentiate:
\[
b'(x)=2(1-e^{-x})^2,\quad v'(x)=2\tanh^2(x/2),\quad
b''(x)=4e^{-x}(1-e^{-x})>0,\quad
v''(x)=2\tanh(x/2)\operatorname{sech}^2(x/2)>0
\]
for \(x>0\). Both gap costs are strictly convex on \([0,\infty)\), with derivative zero at zero. Minimization over nonnegative gaps summing to one therefore has a unique minimizer, with every gap positive: a zero gap and a positive gap could be perturbed toward each other to decrease the cost, since positive gaps have strictly positive derivative. By strict convexity and symmetry all \(n-1\) interior gaps equal \(h_n\), and both terminal gaps equal \(a_n\). The common Lagrange multiplier gives \(b'(\lambda a_n)=v'(\lambda h_n)\). Taking nonnegative square roots yields \(1-e^{-\lambda a_n}=\tanh(\lambda h_n/2)\), equivalent to
\[
a_n=\frac{h_n}{2}+\lambda^{-1}\log\cosh(\lambda h_n/2).
\]
The sum-of-gaps constraint gives the displayed monotone scalar equation for \(h_n\), with left side strictly increasing from zero past one when \(h=1/n\), so there is one root in \((0,1/n)\). The exact optimal variance is
\[
 V_n^{\rm opt}=\frac{\sigma^2}{\lambda^2}
 \left[2b(\lambda a_n)+(n-1)v(\lambda h_n)\right].
\]
For \(n=1\), strict convexity of \(b(\lambda t)+b(\lambda(1-t))\) makes \(t=1/2\) uniquely optimal.

**3. Sharp loss of independent stratified placement.** For the randomized design, the terminal gaps are \(U_1/n\) and \((1-U_n)/n\), and the interior gaps are \((1+U_{i+1}-U_i)/n\). Set \(Y_i=(1+U_{i+1}-U_i)^3\). The expansions (uniform for arguments in \([0,2\lambda/n]\)) are
\[
 b(x)=\frac23x^3+O(x^4),\qquad v(x)=\frac16x^3+O(x^5).
\]
They imply, deterministically and uniformly over all sampled locations,
\[
 n^2 V_n^{\rm jit}=\frac{\sigma^2\lambda}{6n}
 \sum_{i=1}^{n-1}Y_i+O(n^{-1}),
\]
with constants depending only on the fixed covariance parameters. The same expansions, together with \(h_n\sim1/n\) and \(a_n\sim1/(2n)\), give \(n^2V_n^{\rm opt}\to\sigma^2\lambda/6\). Since \(\mathbb E Y_i=3/2\), the expectation of the preceding uniform approximation gives \(n^2\mathbb E V_n^{\rm jit}\to\sigma^2\lambda/4\) and therefore the efficiency ratio \(3/2\).

**4. Fluctuations.** The bounded stationary sequence \((Y_i)\) is 1-dependent, hence satisfies the classical central limit theorem for sums of 1-dependent bounded variables. Exact polynomial integration over independent uniforms gives
\[
 \mathbb E Y_i=\frac32,\quad
 \operatorname{Var}(Y_i)=\frac{16}{7},\quad
 \operatorname{Cov}(Y_i,Y_{i+1})=-\frac{307}{336}.
\]
All covariances for indices at distance at least two vanish. Thus the sum has asymptotic variance \(16/7-2(307/336)=11/24\) per summand. The deterministic \(O(n^{-1})\) remainder above is negligible after multiplication by \(\sqrt n\), giving the claimed Gaussian variance \(\sigma^4\lambda^2(11/24)/36=11\sigma^4\lambda^2/864\). The centering is valid because the finite-sample mean differs from its limit by \(O(n^{-1})\).

## Verification

The standalone script `verify_ou_quadrature.py` evaluates the exact Schur complement for the posterior integral variance and compares it to the independent Markov-gap formula on optimized and randomized designs for multiple correlation lengths and sample counts. It also checks derivative identities, Taylor coefficients, and the three exact rational cubic-gap moments using symbolic polynomial integration. Run `python verify_ou_quadrature.py` with NumPy, SciPy and SymPy installed; 140 assertions pass. Numerical tests support the identities but do not replace the convexity argument or the 1-dependent central limit theorem.

## Relationship to prior work

Pronzato and Zhigljavsky (2018) develop the Bayesian quadrature / kernel-energy framework and discuss the exponential covariance kernel, but do not supply the specific all-\(n\) global integral-variance minimizer with its exact terminal spacing and randomized stratification fluctuation law. Mukherjee's work on stochastic-process sampling addresses optimally estimating entire sample paths using integrated *pointwise* mean-square prediction error; the available abstract of the dissertation also mentions integral estimation, so direct precedence for the integral-design portion cannot be excluded without reviewing that thesis. Sikolya and Baran study optimal prediction designs for a *complex* OU process under pathwise IMSPE and entropy criteria, distinct from the variance of one integrated functional. Existing general Gaussian-Markov conditioning and 1-dependent CLTs supply tools; the result is a direct specialization, not a new general theory of either method.

## Limitations

The claim assumes known stationary exponential covariance, known zero mean, Gaussianity, noiseless observations, one fixed spatial dimension, and fixed hyperparameters. No guarantee is made for estimating covariance parameters, designs with observation costs or repeated nodes, nonstationary Gauss–Markov processes, or pathwise IMSPE. Independent external verification and comprehensive publication-precedence review are outstanding, especially the unavailable integral-estimation section of Mukherjee's dissertation. The common leading jitter penalty and CLT can also be related to the local Brownian scaling of exponential kernels; the full finite-sample optimal spacing remains the main distinct formula.

## References

1. L. Pronzato and A. Zhigljavsky, *Bayesian quadrature and energy minimization for space-filling design*, arXiv:1808.10722v1 (public 2018-08-31), https://arxiv.org/abs/1808.10722.
2. K. Sikolya and S. Baran, *On the optimal designs for the prediction of complex Ornstein–Uhlenbeck processes*, arXiv:1808.03444 (2018), https://arxiv.org/abs/1808.03444.
3. B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Purdue University dissertation (2001), abstract at https://docs.lib.purdue.edu/dissertations/AAI3043760/.
4. B. Mukherjee, *A note on sampling designs for random processes with no quadratic mean derivative*, publicly available manuscript, https://websites.umich.edu/~bhramar/research/synote1.pdf.
