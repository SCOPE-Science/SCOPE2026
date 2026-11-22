# Centered two-sample design for stationary Ornstein–Uhlenbeck quadratic path energy

## Finding
Let \(X\) be the stationary, real, centered, unit-variance Ornstein–Uhlenbeck process with \(\mathbb E[X(u)X(v)]=e^{-\lambda|u-v|}\), where \(\lambda>0\). Estimate the *random quadratic path energy* \(Q_T=\int_0^T X(u)^2\,du\) using its conditional expectation given **two noiseless, distinct point observations**, at freely chosen locations in \([0,T]\), with \(T>0\). The loss is expected squared error.

**Exact location theorem.** Every globally Bayes-optimal pair is symmetric about the midpoint \(T/2\), and both sites are strictly inside the observation interval. Set \(L=\lambda T\). Its gap is \(d/\lambda\) for a global maximizer \(0<d<L\) of the following explicit one-variable function:
\[
\Phi_L(d)=\left(1+\frac{d}{e^d+1}-\frac{e^{d-L}}2(1+e^{-d})\right)^2
+\left(1-\frac{d}{e^d-1}-\frac{e^{d-L}}2(1-e^{-d})\right)^2.
\]
The exact optimal reduction in Bayes mean-square error is \(2\max_{0<d<L}\Phi_L(d)/\lambda^2\). No claim is made that the finite-\(L\) maximizing gap is unique.

**Long-horizon theorem.** Let \(d_L\) be *any* globally optimal dimensionless gap. As \(L\to\infty\), all optimal gaps converge to the same positive constant
\[
 d_L\longrightarrow d_*=2.554928950095267006479\ldots,
\]
where \(d_*\) is the **unique** global maximizer of
\[
\Phi_\infty(d)=2+\frac{2d}{e^{2d}-1}\left(d\coth d-2\right),\quad d>0.
\]
Consequently the total Bayes-risk reduction tends to \(2\Phi_\infty(d_*)/\lambda^2=4.036371112171323\ldots/\lambda^2\). The constant is not a universal physical-time separation: the physical gap tends to \(d_*/\lambda\). The unlimited-horizon *total* variance of \(Q_T\) diverges; the absolute information gain above stays finite.

## Assumptions and scope
The model has known covariance and unit marginal variance, continuous-time stationary Gaussian sample paths, exactly two **exact** point values, nonadaptive choice of locations, and unrestricted placement including possible endpoints. For distinct observations \(0\le s<t\le T\), define \(Z=(X(s),X(t))^\top\), the positive definite covariance \(K=\mathbb E[ZZ^\top]\), and the positive definite cross-covariance integral \(M=\int_0^T c(u)c(u)^\top\,du\) where \(c(u)=(e^{-\lambda|u-s|},e^{-\lambda|u-t|})^\top\). For the Gaussian conditional-mean estimator, the law of total variance and Wick's identity give the objective
\[
\operatorname{Var}(\mathbb E[Q_T\mid Z])=2\operatorname{tr}\left[(K^{-1}M)^2\right].
\]
This is equivalent to minimizing the Bayes squared error because \(\operatorname{Var}(Q_T)\) is design-independent. Coincident observations contain just one value and are included via their continuous zero-gap limit.

## Proof
**1. Exact two-site reduction.** Write dimensionless positions \(\xi=\lambda s\), \(\eta=\lambda t\), gap \(d=\eta-\xi\), left margin \(\ell=\xi\), right margin \(w=L-\eta\), and \(r=e^{-d}\), \(z=e^{-2\ell}\), \(v=e^{-2w}\). Put \(B=\lambda M\). Direct integration over the three subintervals determined by the observation sites gives
\[
K=\begin{pmatrix}1&r\\r&1\end{pmatrix},\qquad
B=\begin{pmatrix}
1-(z+r^2v)/2&r[d+1-(z+v)/2]\\
r[d+1-(z+v)/2]&1-(r^2z+v)/2
\end{pmatrix}.
\]
Thus the normalized information \(F=\operatorname{tr}[(K^{-1}B)^2]\) obeys the exact identity
\[
F=H(d,r)+\frac14(z+v)^2-(z+v)-\frac{1-r^2}{2}zv,
\]
where
\[
H(d,r)=\frac{2\{d^2(r^4+r^2)+2d(r^4-r^2)+(1-r^2)^2\}}{(1-r^2)^2}.
\]
In particular this identity follows from matrix multiplication alone and is checked symbolically by the verifier.

**2. Strict centering at every fixed positive gap.** At fixed \(d\), \(\ell+w=L-d\), hence \(zv=e^{-2(L-d)}\) is fixed. For \(0\le\ell,w\), the sum \(U=z+v\) satisfies \(0<U\le2\) and \(U\ge2\sqrt{zv}\), with equality if and only if \(\ell=w\). The only part of \(F\) that changes with \(U\) is \(U^2/4-U\), whose derivative is \(U/2-1<0\) except at the degenerate upper endpoint. Therefore centering strictly increases \(F\) unless \(\ell=w\). Every optimal distinct pair is exactly symmetric about \(L/2\).

**3. A centered spectral formula and strict interiority.** For centered sites set \(\epsilon=e^{-(L-d)}\). The two eigenvalues of the symmetric similar matrix \(K^{-1/2}BK^{-1/2}\) are
\[
\mu_+=1+\frac{d}{e^d+1}-\frac\epsilon2(1+e^{-d}),\qquad
\mu_-=1-\frac{d}{e^d-1}-\frac\epsilon2(1-e^{-d}).
\]
Both are positive for every \(0<d\le L\), because the integral Gram matrix \(B\) is positive definite. Consequently \(F=\Phi_L(d)=\mu_+^2+\mu_-^2\). At collision \(d\downarrow0\),
\[
\Phi_L(0+)=(1-e^{-L})^2,\qquad\Phi_L'(0+)=(1-e^{-L})^2>0.
\]
At the other boundary \(d=L\), the centered observations lie at the two interval endpoints and
\[
\mu_+'(L)=\frac{1-e^{2L}-2Le^L}{2(e^L+1)^2}<0,\qquad
\mu_-'(L)=\frac{1-e^{2L}+2Le^L}{2(e^L-1)^2}<0.
\]
The second inequality uses \(\sinh L>L\). Positivity of the eigenvalues gives \(\Phi_L'(L)<0\). Compactness of the continuous extension of \(\Phi_L\) to \([0,L]\) then yields at least one global maximizer, and the derivative signs put **all** maximizers in \((0,L)\). This also excludes the single-information collision design.

**4. Unique infinite-horizon gap.** For fixed \(d>0\), \(\epsilon\to0\), giving the stated \(\Phi_\infty\). Put \(h(d)=d\coth d-2\). Its derivative satisfies \(h'(d)=(\sinh d\cosh d-d)/\sinh^2d>0\), so \(h\) has a single positive zero \(d_0\). The excess \(G(d)=\Phi_\infty(d)-2=2d h(d)/(e^{2d}-1)\) is negative before \(d_0\), positive after it, and tends to zero from above at infinity.

For \(d>d_0\), \(G>0\) and its logarithm is strictly concave. Indeed,
\[
\frac{d^2}{dd^2}\log\frac{d}{e^{2d}-1}=-\frac1{d^2}+\frac1{\sinh^2d}<0.
\]
Also \((\log h)''<0\): multiplying \((h')^2-hh''\) by \(\sinh^4d\) gives
\[
D(d)=(\sinh d\cosh d-d)^2-2(d\cosh d-2\sinh d)(d\cosh d-\sinh d)
=\sum_{n=2}^\infty \frac{2^{2n-2}[2^{2n-1}-4n^2+10n-8]}{(2n)!}d^{2n}>0.
\]
The bracket is \(4\) at \(n=2\) and strictly increases for integer \(n\ge2\), because the consecutive difference is \(3\cdot2^{2n-1}-8n+6>0\). Therefore \(\log G\) is strictly concave on \((d_0,\infty)\) and tends to minus infinity at both endpoints. It has exactly one maximizer \(d_*\) there, which is also the unique global maximum of \(\Phi_\infty\).

**5. Convergence of every finite-horizon optimum.** Take arbitrary \(L_j\to\infty\) and corresponding optimal gaps \(d_j\). Testing the fixed competitor \(d_*\) gives \(\liminf\Phi_{L_j}(d_j)\ge\Phi_\infty(d_*)>2\). The sequence cannot converge toward zero: then \(\Phi_{L_j}(d_j)\to1\). It cannot escape to infinity: since \(0<e^{d_j-L_j}\le1\) and \(e^{-d_j}\to0\), both eigenvalues converge along every convergent subsequence of \(e^{d_j-L_j}\) to \(1-e^{d_j-L_j}/2\); hence \(\limsup\Phi_{L_j}(d_j)\le2\). Thus the gaps remain in a compact subinterval of \((0,\infty)\). Every subsequential limit maximizes \(\Phi_\infty\), so uniqueness forces convergence to \(d_*\). The asymptotic gain follows by continuity.

## Verification
Run `python verify.py` using the versions and packages listed in `requirements.txt`. The executable file derives the matrix identity by exact symbolic algebra, verifies the centered eigenvalue representation, collision and endpoint derivatives, and checks initial coefficients of the power-series positivity certificate. It also performs supplementary centered-versus-unrestricted comparisons at 7,958 sampled positions, numerical finite-horizon optimum checks, and high-precision root evaluation. The infinite-domain positivity and uniqueness claims follow from the displayed coefficient and concavity arguments, **not** from finite numerical tests. The decimal constant is numerical; uniqueness and convergence are analytical.

## Relationship to prior work
Sikolya–Baran (arXiv:1808.03444v1, 10 August 2018) study Gaussian process trajectory prediction with an integrated pointwise mean-square prediction error and an entropy criterion. Their criterion reduces an integrated posterior *pointwise covariance*, while the present functional is a single *quadratic path energy* and has a trace-square conditional-variance objective. Neither criterion implies the centered two-site theorem or the limiting nonzero gap by an algebraic or monotonicity substitution.

Ji–Müller study sparse functional-data trajectory recovery and **linear** functional regression, rather than conditional prediction of a nonlinear integrated square. Grebenkov optimizes quadratic-form *estimators of observed Gaussian trajectories* with controlled mean/cumulants, not observation locations for conditional prediction of an unobserved continuous quadratic functional. Published work on optimal nodes for the **linear** OU integral similarly targets a distinct first-chaos quantity; squared-energy information is a second-chaos trace-square. Related two-observation Brownian and Brownian-bridge quadratic-energy results have nonstationary covariance, different boundary geometry and do not establish the stationary exponential-kernel centering or universal separation.

## Limitations
Noiseless measurement, exactly two points, stationary Gaussianity, exponential covariance and known parameters are essential assumptions. The theorem does not establish a unique finite-horizon gap, uncertainty about estimated covariance parameters, adaptive design, noisy observations, other path functionals, or multi-site design. The physical optimal gap scales as the correlation length. This is a self-review and not independent validation. Publication priority beyond the inspected and indexed works remains open to independent checking.

## References
1. K. Sikolya and S. Baran, *On the optimal designs for the prediction of complex Ornstein–Uhlenbeck processes*, arXiv:1808.03444v1 (first public 2018-08-10), https://arxiv.org/abs/1808.03444.
2. H. Ji and H.-G. Müller, *Optimal Designs for Longitudinal and Functional Data*, arXiv:1604.05375v1 (2016-04-18), https://arxiv.org/abs/1604.05375.
3. D. S. Grebenkov, *Optimal and sub-optimal quadratic forms for non-centered Gaussian processes*, arXiv:1307.0185v1 (2013-06-30), https://arxiv.org/abs/1307.0185.
