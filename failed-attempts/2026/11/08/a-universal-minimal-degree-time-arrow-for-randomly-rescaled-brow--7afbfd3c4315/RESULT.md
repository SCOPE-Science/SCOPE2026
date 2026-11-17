# A universal minimal-degree time arrow for randomly rescaled Brownian resetting

## Finding

Consider a stationary Brownian particle that moves by ordinary diffusion between Poisson events and is multiplied at each event by an independent random contraction. Although its stationary one-time density is symmetric and its two-point covariance is a single exponential, **the first nonzero polynomial time-reversal asymmetry always occurs at total degree four**, with an exact strictly signed profile and a unique most-informative lag.

Let the Poisson rate be \(r>0\), the diffusivity \(D>0\), and the independent reset marks be real \(A\) satisfying \(|A|\le\rho<1\) almost surely. For \(k=1,2,3,4\), write

\[
\mu_k=\mathbb E[A^k],\qquad \lambda_k=r(1-\mu_k),\qquad
v=\frac{2D}{\lambda_2},\qquad w=\frac{12Dv}{\lambda_4},
\]

and define the strictly positive mark statistic

\[
G=\mathbb E[(1-A)^2(1-A^2)]>0.
\]

For every \(t>0\), the stationary antisymmetric fourth-order two-time moment is

\[
\boxed{\mathcal I(t):=\mathbb E[X_0^3X_t]-\mathbb E[X_0X_t^3]
=-\frac{rwG}{2}\,H(t)<0},
\]

where

\[
H(t)=\int_0^t e^{-\lambda_1(t-s)-\lambda_3s}\,ds
=\begin{cases}
\dfrac{e^{-\lambda_1t}-e^{-\lambda_3t}}{\lambda_3-\lambda_1},&\lambda_3\ne\lambda_1,\\[5pt]
t e^{-\lambda_1t},&\lambda_3=\lambda_1.
\end{cases}
\]

The magnitude \(-\mathcal I(t)\) increases strictly up to one and only one positive lag, then decreases strictly. That lag is

\[
\boxed{t_*=\begin{cases}
\dfrac{\log(\lambda_3/\lambda_1)}{\lambda_3-\lambda_1},&\lambda_3\ne\lambda_1,\\[5pt]
\dfrac1{\lambda_1},&\lambda_3=\lambda_1.
\end{cases}}
\]

In contrast, the stationary covariance is \(\mathbb E[X_0X_t]=v e^{-\lambda_1t}\). For **every** pair of nonnegative integers \(p,q\) with \(p+q<4\) and every \(t\ge0\),

\[
\mathbb E[X_0^pX_t^q]-\mathbb E[X_0^qX_t^p]=0.
\]

Thus total degree four is the minimal polynomial degree at which stationary two-time observations can detect the arrow of time in this entire model family.

## Assumptions and scope

The particle evolves continuously by \(dX_t=\sqrt{2D}\,dW_t\) away from Poisson events. At each event, \(X_t=A_jX_{t-}\), where the marks \(A_j\) are independent identically distributed copies of \(A\), independent of the Brownian noise and Poisson process. The contraction assumption \(|A|\le\rho<1\) is uniform; it includes deterministic resetting, randomly changing reset signs, and resetting to zero. Neither finite support nor a symmetric mark law is required. All assertions concern the unique two-sided stationary law, rather than an arbitrary transient initial condition.

The stationary solution has an \(L^2\)-convergent stochastic-integral representation

\[
X_t=\sqrt{2D}\int_{-\infty}^t
\left(\prod_{\tau_j\in(s,t]}A_j\right)dW_s.
\]

The independent marked Poisson product has exponentially decreasing second moment. Conditional Gaussianity and standard moment estimates then give every finite stationary polynomial moment; contracting coupling ensures uniqueness. The process is spatially sign-symmetric because the Brownian noise is symmetric and all reset multipliers are independent of it.

## Proof

**1. Generator and stationary moments.** On polynomial test functions the generator is

\[
\mathcal L f(x)=Df''(x)+r\bigl(\mathbb E[f(Ax)]-f(x)\bigr).
\]

Therefore, for positive integer \(k\),

\[
\mathcal L x^k=Dk(k-1)x^{k-2}-\lambda_kx^k.
\]

The stationary generator identities, together with spatial symmetry, give \(\mathbb E[X]=\mathbb E[X^3]=0\) and

\[
\mathbb E[X^2]=v=\frac{2D}{\lambda_2},\qquad
\mathbb E[X^4]=w=\frac{12Dv}{\lambda_4}.
\]

Each \(\lambda_k\) is positive: for odd powers use \(|\mathbb E[A^k]|\le\rho^k\), and for even powers use \(\mathbb E[A^k]\le\rho^k\).

**2. Polynomial semigroup.** The Markov semigroup maps \(x\) to \(e^{-\lambda_1t}x\). Solving the inhomogeneous two-dimensional moment system for \(x^3\) yields

\[
P_tx^3=e^{-\lambda_3t}x^3+6D H(t)x.
\]

Consequently,

\[
\mathbb E[X_0^3X_t]=w e^{-\lambda_1t},\qquad
\mathbb E[X_0X_t^3]=w e^{-\lambda_3t}+6Dv H(t).
\]

For all rates, including coincident rates, the exponential difference equals \((\lambda_3-\lambda_1)H(t)\). Since \(6Dv=\lambda_4 w/2\), subtraction gives

\[
\mathcal I(t)=w\left(\lambda_3-\lambda_1-\frac{\lambda_4}{2}\right)H(t).
\]

The crucial factor is an exact pointwise polynomial identity:

\[
(a-a^3)-\frac{1-a^4}{2}
=-\frac{(1-a)^2(1-a^2)}2.
\]

Averaging this identity under the mark distribution yields

\[
\lambda_3-\lambda_1-\frac{\lambda_4}{2}=-\frac r2 G.
\]

Because \(|A|<1\) almost surely, \(G>0\); because \(t>0\), the defining integral gives \(H(t)>0\). Thus the asserted sign is strict and has no exceptional contraction parameters, including \(\lambda_3=\lambda_1\).

**3. Unique optimum lag.** If \(\lambda_3\ne\lambda_1\), differentiating the divided exponential gives

\[
H'(t)=\frac{-\lambda_1e^{-\lambda_1t}+\lambda_3e^{-\lambda_3t}}{\lambda_3-\lambda_1}.
\]

There is exactly one positive zero, at the stated \(t_*\), because \(e^{-(\lambda_3-\lambda_1)t}\) is strictly monotone. Moreover \(H'(0)=1\), and \(H(t)\to0\) as \(t\to\infty\); the zero is a strict global maximum. At coincident rates, \(H(t)=te^{-\lambda_1t}\) peaks uniquely at \(1/\lambda_1\).

**4. Minimal polynomial degree.** Spatial sign symmetry makes every mixed moment of odd total degree zero. If one exponent is zero, the two orientations agree by stationarity. Equal exponents agree identically. Every nonnegative pair with total degree below four belongs to one of these cases; the displayed antisymmetric fourth-order moment is nonzero for every positive lag, completing the minimality proof.

## Verification

A standalone standard-Python checker, \(\texttt{proof_checker.py}\), runs exact-rational evaluations of the nonstandard factorization and stationary moment identities over deterministic and finitely supported signed-mark distributions. It independently computes both conditional-polynomial and factorized versions of the fourth-order lag difference, checks positive and negative marks, mixtures, the coincident-rate limit, and the unique maximum. It reports **1,896 passing assertions**. These finite tests corroborate the algebra but are not the proof for arbitrary mark distributions.

An exact illustrative law takes \(r=D=1\) and \(A=\pm\tfrac12\) with equal probabilities. In this case \(\lambda_1=\lambda_3=1\), \(v=8/3\), \(w=512/15\), \(G=15/16\), and the theorem reduces to

\[
\boxed{\mathcal I(t)=-16t e^{-t},\qquad t_*=1.}
\]

This is also a direct check of the otherwise easy-to-miss coincident-rate case.

## Relationship to prior work

Dahlenburg, Chechkin, Schumer and Metzler (2021) investigated stochastic resetting with random amplitudes, including partially resetting models, and analyzed displacement distributions and low-order moments in several regimes. Biroli, Feld, Hartmann, Majumdar and Schehr (2024) established the stationary spatial law and first-passage theory for Brownian position rescaling by a *fixed* positive or negative multiplier. Both prior model formulations are acknowledged. The present result isolates a different dynamical question: a minimal-order, strictly signed time-antisymmetric two-time observable, its exact universal marked-factor formula, and the unique lag of maximal magnitude.

Zanin and collaborators (2024) considered time-irreversibility diagnostics for *geometric* Brownian motion with resetting. That paper concerns a different diffusion and reset mechanism; it motivates the diagnostic question but does not supply the theorem here. More general polynomial-semigroup or stochastic-thermodynamic frameworks may imply pieces of the calculation. The specific simultaneous minimality, marked-factor strictness, and unique-lag assertion has not been located in the compared sources. Lack of identification is not a proof of absolute priority.

## Limitations

The theorem concerns stationary sampling, independent Brownian and Poisson noises, iid bounded contractive marks, and integer polynomial two-time moments. It does not establish an entropy-production formula, finite-sample statistical power, observational robustness, or universality when some reset factors have modulus at least one. The sign convention is the explicitly displayed \(\mathcal I(t)\); reversing the two time orientations reverses that sign. The exact proof is analytical, but literature priority remains subject to independent verification.

## References

1. M. Dahlenburg, A. V. Chechkin, R. Schumer and R. Metzler, *Stochastic resetting by a random amplitude*, arXiv:2104.14866, first public version 2021-04-30, https://arxiv.org/abs/2104.14866 .
2. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1, 2024-06-12, https://arxiv.org/html/2406.08387v1 .
3. M. Zanin and collaborators, *Evaluating Time Irreversibility Tests Using Geometric Brownian Motions with Stochastic Resetting*, *Symmetry* **16** (2024), 1445, https://doi.org/10.3390/sym16111445 .
4. D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, *Physical Review E* **98** (2018), 022129, https://doi.org/10.1103/PhysRevE.98.022129 .
