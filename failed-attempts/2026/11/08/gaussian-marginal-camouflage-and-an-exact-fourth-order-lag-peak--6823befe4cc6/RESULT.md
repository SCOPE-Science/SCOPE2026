# Gaussian-marginal camouflage and an exact fourth-order lag peak under equilibrium Poisson refreshing

## Finding

An overdamped Brownian particle in a harmonic trap, independently refreshed at Poisson times from **the same thermal equilibrium distribution**, is stationary and reversible and has exactly Gaussian one-time marginals. Its entire covariance function and its conditional *mean* match those of an ordinary Ornstein–Uhlenbeck (OU) process. Nevertheless, its joint distribution at every positive finite time lag is non-Gaussian. Its connected two-time fourth cumulant has one unique positive lag of maximal detection power, and it carries strictly more two-time mutual information than the covariance-matched Gaussian OU model.

Let \(\lambda,D,r>0\), \(v=D/\lambda\), \(\rho_t=e^{-\lambda t}\), and \(w_t=e^{-rt}\). At stationarity the exact two-time law, for every \(t>0\), is
\[
 \mathcal P_t=w_t\,\mathcal N_2\!\left(0,v\begin{pmatrix}1&\rho_t\\\rho_t&1\end{pmatrix}\right)
 +(1-w_t)(\pi\otimes\pi),\qquad \pi=\mathcal N(0,v).
\]
Consequently, \(\operatorname{Cov}(X_0,X_t)=v e^{-(\lambda+r)t}\), indistinguishable from a stationary OU process of relaxation rate \(\lambda+r\) and invariant variance \(v\). The connected fourth cumulant instead equals
\[
 \mathcal K(t):=\mathbb E[X_0^2X_t^2]-v^2-2\mathbb E[X_0X_t]^2
 =2v^2 e^{-(r+2\lambda)t}(1-e^{-rt})>0.
\]
It attains its unique global maximum for \(t>0\) at
\[
 t_*=\frac1r\log\!\left(\frac{2(r+\lambda)}{r+2\lambda}\right).
\]
Its maximal height \(\mathcal M(r)=\mathcal K(t_*)\), with \(\lambda,v\) fixed, is strictly increasing in \(r>0\) and satisfies
\[
\mathcal M(r)=\frac{v^2r}{r+\lambda}
\left(\frac{r+2\lambda}{2(r+\lambda)}\right)^{(r+2\lambda)/r},\qquad
\mathcal M(r)\sim\frac{v^2r}{e\lambda}\ (r\downarrow0),\qquad
\mathcal M(r)\to\frac{v^2}{2}\ (r\to\infty).
\]
For the covariance-matched stationary Gaussian OU pair law \(\mathcal G_t\), the mutual-information excess is strictly positive:
\[
 I_{\mathcal P_t}(X_0;X_t)-I_{\mathcal G_t}(Y_0;Y_t)
 =D_{\rm KL}(\mathcal P_t\Vert\mathcal G_t)>0,\qquad
 I_{\mathcal G_t}=-\tfrac12\log(1-e^{-2(\lambda+r)t}).
\]
Here all logarithms in information quantities are natural.

## Assumptions and scope

The real-valued process follows \(dX_s=-\lambda X_s\,ds+\sqrt{2D}\,dB_s\) between independently arriving Poisson events of rate \(r\). At each event its position is **replaced**, not incremented, by a fresh independent sample from \(\pi=\mathcal N(0,D/\lambda)\). Brownian motion, Poisson arrivals, replacement samples, and the initial stationary state are independent except through the resulting trajectory. The constants satisfy \(D>0\), \(\lambda>0\), \(r>0\), and all times in the displayed theorem satisfy \(t>0\). The process starts from \(\pi\), which is its unique invariant law.

The comparator \(Y\) is a separate stationary ordinary OU process with drift rate \(\lambda+r\), diffusion coefficient \(D_{\rm eff}=(\lambda+r)v\), and invariant law \(\pi\). This comparator has the same complete two-point covariance function as \(X\), but not the same path law. There is no assertion that this replacement protocol is identical to resetting to a fixed site, that it produces thermodynamic entropy, or that the entire sample path becomes Gaussian at any finite \(r\).

## Proof

**Stationarity, uniqueness and reversibility.** For smooth test functions, the Markov generator is
\[
 Lf(x)=Df''(x)-\lambda x f'(x)+r\bigl(\pi(f)-f(x)\bigr).
\]
Integration by parts with respect to \(\pi\) makes the OU part symmetric, and the refresh part is the self-adjoint operator \(r(\Pi-I)\), where \(\Pi f=\pi(f)\). Both preserve \(\pi\); their sum is symmetric in \(L^2(\pi)\), proving detailed balance for the stationary process. The probability of at least one independent refresh before time \(t\) is \(1-e^{-rt}\). Starting from any position, after the last such refresh the marginal remains \(\pi\), since ordinary OU evolution also preserves it. Thus \(P_t(x,\cdot)\ge(1-e^{-rt})\pi(\cdot)\), yielding uniqueness and convergence to \(\pi\).

**Exact two-time mixture.** Condition on the Poisson count on \((0,t)\). If it is zero, probability \(w_t=e^{-rt}\), the pair is the stationary ordinary OU pair with correlation \(\rho_t=e^{-\lambda t}\). Otherwise the first refresh breaks all dependence on \(X_0\); all subsequent evolution preserves the independent \(\pi\)-distributed endpoint. This gives the stated Gaussian mixture. Both mixture components have marginal \(\pi\), so \(\mathbb E[X_0X_t]=v w_t\rho_t\), and \(\mathbb E[X_t\mid X_0=x]=w_t\rho_t x\).

The conditional *variance* provides a second, more local witness:
\[
\operatorname{Var}(X_t\mid X_0=x)
 =v(1-w_t\rho_t^2)+w_t(1-w_t)\rho_t^2x^2.
\]
For the covariance-matched Gaussian OU pair, the corresponding variance is the constant \(v(1-w_t^2\rho_t^2)\). Their difference is precisely \(w_t(1-w_t)\rho_t^2(x^2-v)\). Hence identical Gaussian marginals, two-time covariance, and linear regression do not determine conditional uncertainty.

**Non-Gaussian fourth cumulant.** Wick's identity gives \(\mathbb E[X_0^2 X_t^2\mid\text{no refresh}]=v^2(1+2\rho_t^2)\); with at least one refresh it equals \(v^2\). Averaging gives \(v^2(1+2w_t\rho_t^2)\). Subtract \(v^2+2(vw_t\rho_t)^2\) to obtain \(\mathcal K(t)=2v^2w_t(1-w_t)\rho_t^2>0\). In any centered bivariate Gaussian law this cumulant vanishes, so \(\mathcal P_t\ne\mathcal G_t\) for every finite \(t>0\).

**Unique optimal lag and rate response.** Write \(\mathcal K(t)/(2v^2)=e^{-At}-e^{-Bt}\), with \(A=r+2\lambda>0\) and \(B=2(r+\lambda)>A\). Its derivative has exactly one zero, at \(t_*=(\log(B/A))/(B-A)\), and changes sign from positive to negative. Substitution proves the peak formula. For fixed \(s=rt>0\),
\[
\frac{\mathcal K(s/r)}{2v^2}=e^{-s}(1-e^{-s})e^{-2\lambda s/r},
\]
which is strictly increasing in \(r\) pointwise in \(s>0\). Evaluating a larger-rate profile at the smaller-rate maximizer proves strict monotonicity of \(\mathcal M(r)\). For small \(r\), \(A/B=1-r/(2\lambda)+O(r^2)\), so \((A/B)^{A/r}\to e^{-1}\); the front factor is asymptotic to \(v^2r/\lambda\). For large \(r\), the prefactor tends to \(v^2\) and the powered ratio tends to \(1/2\), yielding the stated limits.

**Excess mutual information.** The pair \(\mathcal P_t\) and Gaussian comparator \(\mathcal G_t\) have exactly the same nondegenerate covariance matrix and both have marginals \(\pi\). Since \(\log d\mathcal G_t\) and \(\log d(\pi\otimes\pi)\) are quadratic polynomials plus constants, their expectations are the same under \(\mathcal P_t\) and \(\mathcal G_t\). Expanding the definitions of mutual information and relative entropy therefore gives
\[
 I(\mathcal P_t)-I(\mathcal G_t)=D_{\rm KL}(\mathcal P_t\Vert\mathcal G_t).
\]
All densities are smooth and strictly positive. The relative entropy is finite for fixed parameters (both mixture components are nondegenerate Gaussians), and is strictly positive because the fourth cumulant distinguishes the pair measures. This proves the strict information excess.

## Verification

`verify.py` (Python 3; NumPy and SymPy) is an optional reproducibility checker. It performs exact symbolic checks of the mixture moment and peak identities and limiting expressions, deterministic-seed independent Monte Carlo cross-checks for three dimensionless regimes, and Gaussian-Hermite quadrature estimates of the positive relative entropy. Re-run it as `python verify.py` with NumPy and SymPy installed. The numerical integrations and simulations are cross-checks, not substitutes for the analytic proof of strict positivity or optimality.

## Relationship to prior work

Mori, Olsen and Krishnamurthy [1] formulate Poisson resetting to a distribution for a Brownian particle in a confining potential and derive resetting entropy production, including the underlying renewal structure; this paper does not assert novelty for the refreshing mechanism. Trajanovski and collaborators [2] examine OU resetting chiefly to a fixed location, emphasizing one-time relaxation and stationary distributions. Olsen [3] gives general closed-form steady-state moment recurrences for arbitrary resetting distributions in harmonic traps. Those results provide part of the model and stationary-moment context. The narrower contribution here is a *jointly reversible and Gaussian-marginal* instance with an explicit non-Gaussian two-time law, a uniquely optimal fourth-order lag and a rigorous strictly positive information gap against a covariance-matched OU process. The standard Gaussian maximum-entropy inequality is used as a proof ingredient, not claimed as new.

## Limitations

The result requires full independent equilibrium-distributed replacements, a harmonic potential, constant Poisson rate and stationary initialization. No conclusions are asserted for partial resets, non-Poisson reset clocks, time-varying trap coefficients or spatially dependent resets. The exact optimal lag optimizes only the unnormalized connected fourth cumulant \(\mathcal K\), not statistical detection power with finite-sample estimation noise. The mutual-information gap is strictly positive but no closed form or globally optimized gap is claimed. Prior literature on general renewal kernels might imply pieces of this theorem algebraically even if the exact displayed classification is not stated; publication priority needs specialized human review. Computational evidence checks formulas but cannot establish scientific novelty.

## References

[1] F. Mori, K. Stølevik Olsen and S. Krishnamurthy, “Entropy production of resetting processes,” arXiv:2211.15372, first public 2022-11-28. https://arxiv.org/abs/2211.15372

[2] P. Trajanovski et al., “Ornstein-Uhlenbeck process and generalizations: particle's dynamics under comb constraints and stochastic resetting,” arXiv:2301.12304, first public 2023-01-28. https://arxiv.org/abs/2301.12304

[3] K. Stølevik Olsen, “Steady-state moments under resetting to a distribution,” arXiv:2310.04840, first public 2023-10-07. https://arxiv.org/abs/2310.04840
