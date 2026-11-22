# Sparse-Poisson rank-one calibration for exponential Stein–Chen goodness-of-fit discrepancies

## Finding
Let \(n\to\infty\), \(\lambda_n>0\), and \(\lambda_n\to0\). For each row, take independent \(X_{n,1},\ldots,X_{n,n}\sim\operatorname{Poisson}(\lambda_n)\). For every fixed \(0<z<1\), define the exponentially weighted, sample-mean-fitted Stein–Chen discrepancy
\[
D_n(z)=\frac1n\sum_{i=1}^n X_{n,i}z^{X_{n,i}}-
\left(\frac1n\sum_{i=1}^nX_{n,i}\right)
\left(\frac1n\sum_{i=1}^nz^{X_{n,i}+1}\right).
\]
This is the difference-form statistic \(\widehat T_3\) of Aleksandrov, Weiß and Jentsch (2021), with weight \(f(k)=z^k\). Define
\[
\sigma_\lambda^2(z)=\lambda z^2\left\{e^{\lambda(z^2-1)}[1+\lambda(1-z)^2]-e^{2\lambda(z-1)}\right\}>0,
\quad H_n(z)=\frac{\sqrt n D_n(z)}{\sigma_{\lambda_n}(z)}.
\]
For **any fixed finite selection** \(z_1,\ldots,z_m\in(0,1)\), the entire vector has one of the following three limits, according to \(\tau_n=n\lambda_n^2\):

1. If \(\tau_n\to\infty\), then \((H_n(z_1),\ldots,H_n(z_m))\Rightarrow(G,\ldots,G)\), where \(G\sim N(0,1)\).
2. If \(\tau_n\to\tau\in(0,\infty)\), then \((H_n(z_1),\ldots,H_n(z_m))\Rightarrow(H_\tau,\ldots,H_\tau)\), where \(H_\tau=(\tau-2P_{\tau/2})/\sqrt{2\tau}\) and \(P_{\tau/2}\sim\operatorname{Poisson}(\tau/2)\).
3. If \(\tau_n\to0\), then \((H_n(z_1),\ldots,H_n(z_m))\to(0,\ldots,0)\) in probability.

Consequently, along sequences with \(\lambda_n\to0\), the standard normal approximation for **any one fixed** \(0<z<1\) is valid if and only if \(n\lambda_n^2\to\infty\). Every set of separately standardized exponential weights collapses onto the **same single random coordinate**, even in the Gaussian regime. In particular, when \(n\lambda_n^2\to 0.3\), a two-sided normal critical value \(1.9599639845\ldots\) yields limiting null rejection probability \(1-e^{-0.15}=0.139292\ldots\), rather than \(0.05\). At this positive critical intensity, substituting the consistent sample mean for \(\lambda_n\) in \(\sigma\) does not change that limit.

An exact covariance identity behind the collapse, for all \(\lambda>0\) and \(0<z,w<1\), is
\[
\Sigma_\lambda(z,w)=\lambda zw\left\{e^{\lambda(zw-1)}[1+\lambda(1-z)(1-w)]-e^{\lambda(z+w-2)}\right\}
\sim 2\lambda^2zw(1-z)(1-w).
\]
Here \(\Sigma_\lambda\) is the covariance of the *linear influence functions*, not the uncorrected finite-sample covariance of \(D_n\). The actual statistic also has the finite-sample expectation
\[\mathbb E D_n(z)=\frac{\lambda_n z(1-z)e^{\lambda_n(z-1)}}{n}.\]

## Assumptions and scope
All samples are independent within rows, and are exactly Poisson with common mean \(\lambda_n\); no serial dependence, data-adaptive weights, or joint growth of the number of weights is asserted. Sample size grows without a fixed rate restriction, except the displayed conditions on \(n\lambda_n^2\). Weights are fixed strictly inside \((0,1)\), so no endpoint normalization is attempted. The unstudentized statistic is always defined, including all-zero samples. Normalization uses the known-null influence standard deviation; the stated substitution result requires the positive critical-intensity regime.

## Proof
Put \(B_z(k)=z^{k+1}\), \(\phi_z=z e^{\lambda(z-1)}\), and
\[\psi_{\lambda,z}(k)=kz^k-\lambda z^{k+1}-\phi_z(k-\lambda).\]
The Poisson generating-function identity \(\mathbb E z^X=e^{\lambda(z-1)}\) shows \(\mathbb E\psi_{\lambda,z}(X)=0\). Exact multiplication and Poisson factorial moments give
\[
\operatorname{Cov}(\psi_{\lambda,z}(X),\psi_{\lambda,w}(X))
=\lambda zw\{e^{\lambda(zw-1)}[1+\lambda(1-z)(1-w)]-e^{\lambda(z+w-2)}\}.
\]
In particular, \(\sigma_\lambda^2(z)=2\lambda^2z^2(1-z)^2[1+O_z(\lambda)]\), with \(\sigma_\lambda(z)>0\) because the influence function is not almost surely constant for \(\lambda>0\). Also \(\operatorname{Cov}(X,z^{X+1})=-\lambda z(1-z)e^{\lambda(z-1)}\), giving the exact bias formula.

An exact decomposition, not just a first-order asymptotic expansion, is
\[
nD_n(z)=\sum_{i=1}^n\psi_{\lambda,z}(X_{n,i})
-n(\overline X-\lambda)(\overline{B}_z-\phi_z).
\]
Cauchy–Schwarz, \(\operatorname{Var}(X)=\lambda\), and \(\operatorname{Var}(B_z(X))=O_z(\lambda)\) imply that the final product has expected absolute value \(O_z(\lambda)\). After dividing by \(\sqrt n\sigma_\lambda(z)\asymp_z\sqrt n\lambda\), it tends to zero in \(L^1\) for every sequence \(n\to\infty,\lambda_n\to0\). This remainder estimate remains valid in all three regimes.

If \(n\lambda_n^2\to\infty\), partitioning the Poisson expectation over \(X=0\), \(X=1\), and \(X\ge2\) gives \(\mathbb E|\psi_{\lambda,z}(X)|^3=O_z(\lambda^2)\): on the first two events the influence function is respectively \(O_z(\lambda^2)\) and \(O_z(\lambda)\), and on the last it is bounded by \(C_z(1+X)\) while every polynomially weighted Poisson tail above one is \(O(\lambda^2)\). As \(\operatorname{Var}(\psi_{\lambda,z}(X))\asymp_z\lambda^2\), the Lyapunov ratio is \(O((\sqrt n\lambda_n)^{-1})\to0\). For any fixed linear combination of weights, the same third-moment bound holds and its variance divided by \(\lambda_n^2\) has a finite limit. Combinations with positive limiting variance obey Lyapunov, and those with zero limiting variance converge to zero by Chebyshev. The exact covariance identity then gives the common-normal vector by Cramér–Wold.

For bounded \(n\lambda_n^2\), let \(N_{n,j}=\#\{i:X_{n,i}=j\}\). Uniformly for each fixed weight, the influence function evaluated at \(j=0,1,2\), after division by \(z(1-z)\), equals respectively
\[-\lambda^2+O_z(\lambda^3),\qquad 2\lambda+O_z(\lambda^2),\qquad -2+O_z(\lambda).\]
Since \(\Pr(X\ge3)=O(\lambda^3)\), the expected contribution from all \(X\ge3\) in the sum is \(O_z(n\lambda^3)=o(1)\). The error terms from \(j=0,1,2\) are also \(o_{\mathbb P}(1)\); hence
\[
\frac{nD_n(z)}{z(1-z)}=-n\lambda_n^2+2\lambda_n N_{n,1}-2N_{n,2}+o_{\mathbb P}(1).
\]
If \(n\lambda_n^2\to\tau>0\), then \(\lambda_n N_{n,1}\to\tau\) in probability (variance \(O(n\lambda_n^3)\to0\)), and binomial-to-Poisson convergence gives \(N_{n,2}\Rightarrow P_{\tau/2}\). The displayed second regime follows after \(\sqrt n\sigma_{\lambda_n}(z)\sim\sqrt{2n}\lambda_n z(1-z)\). For \(\tau=0\), a small additional argument handles the vanishing divisor: \(\Pr(N_{n,\ge2}>0)\le O(n\lambda_n^2)\to0\). On the complementary event, direct substitution gives \(D_n(z)=z(1-z)(N_{n,1}/n)^2\). Since \(\mathbb E[N_{n,1}^2]/(n\sqrt{n}\lambda_n)=O(\sqrt n\lambda_n+n^{-1/2})\to0\), Markov's inequality proves the third regime.

To prove the necessity of \(n\lambda_n^2\to\infty\) for Gaussian convergence, take any bounded subsequence of \(n\lambda_n^2\) and then a further subsequence with a limit \(\tau\ge0\). The second or third case gives a nonnormal limit, contradicting convergence to \(N(0,1)\). Finally, at \(\tau=0.3\) the critical two-sided event is exactly \(P_{0.15}\ge1\), since its zero value is within the normal cutoff and the first nonzero value is already outside; the Poisson upper tail is \(1-e^{-0.15}\). As \(n\lambda_n\to\infty\) whenever \(n\lambda_n^2\to0.3\), \(\overline X/\lambda_n\to1\) in probability, justifying plug-in normalization by Slutsky.

## Verification
Execute `python checker.py` with Python 3, NumPy and SciPy. It computes the closed influence covariance independently as an absolutely convergent Poisson sum; checks its leading sparse asymptotic and the exact finite-sample expectation identity; and uses multinomial count histograms to simulate critical, Gaussian and vanishing regimes. The completed run passed 164 assertions. At \(n=30000\), \(\lambda_n=\sqrt{0.3/30000}\), the check reported Monte Carlo rejection frequency \(0.134556\) against the exact asymptotic \(0.139292\). These finite simulations are corroboration, not the proof of any infinite statement. The checker truncates counts above seven only where the expected number of truncated observations is independently verified below \(10^{-8}\).

## Relationship to prior work
Aleksandrov, Weiß and Jentsch (first public version June 27, 2021) introduce the four Stein–Chen statistics, including difference-form \(\widehat T_3\), and derive fixed-mean normal approximations and joint statistics for multiple weight functions. The present result addresses a different **triangular null** with the Poisson mean shrinking to zero, where fixed-mean asymptotics are not uniform. Weiß, Puig and Aleksandrov (first published September 27, 2022) derive fixed-parameter power and optimize the same exponential-weight family against alternatives, but that theory does not establish the three low-intensity distributional regimes or the weight-independent critical Poisson law. General Poisson approximation for rare counts and triangular-array central limit theorems are classical ingredients, not claimed as new.

## Limitations
The trichotomy is not a statement about tests that invert a vanishing multivariate covariance matrix, which can amplify higher-order count events. It is not a finite-sample exact distribution, a uniform approximation over a growing weight set, or a result for time dependence or non-Poisson nulls. The zero-intensity regime's oracle-normalized statistic may not be computationally well-defined after plug-in if the sample mean is zero; no plug-in assertion is made there. Historical priority of the combined theorem remains subject to specialized literature outside the sources inspected. No independent validation is claimed.

## References
- Aleksandrov, B., Weiß, C. H., and Jentsch, C. *Goodness-of-fit tests for Poisson count time series based on the Stein–Chen identity.* Statistica Neerlandica 76 (2022), 35–64. First publicly published June 27, 2021. https://doi.org/10.1111/stan.12252 ; full open HTML https://onlinelibrary.wiley.com/doi/10.1111/stan.12252.
- Weiß, C. H., Puig, P., and Aleksandrov, B. *Optimal Stein-type goodness-of-fit tests for count data.* Biometrical Journal 65 (2023), 2200073. First publicly published September 27, 2022. https://doi.org/10.1002/bimj.202200073 ; full open HTML https://onlinelibrary.wiley.com/doi/full/10.1002/bimj.202200073.
- Meintanis, S. G. and Nikitin, Y. Y. *A class of count models and a new consistent test for the Poisson distribution.* Journal of Statistical Planning and Inference 138 (2008), 3722–3732. https://doi.org/10.1016/j.jspi.2007.12.011 (related empirical-pgf testing; complete text not inspected).
