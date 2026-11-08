# Sign-reversed optimal momentum and the one-ninth antipersistent noise floor

## Finding

For a scalar strongly convex quadratic with a curvature-matched heavy-ball step and stationary AR(1) additive gradient noise, the sign of every stationary-variance-minimizing momentum coefficient is strictly **opposite** to the noise autocorrelation sign. This is a global statement over the whole Schur-stable momentum interval, not merely a derivative test at zero momentum. In the strongly anticorrelated limit, the optimally tuned stationary variance approaches exactly one ninth of the zero-momentum variance, and the optimal momentum approaches the stability boundary at a sharp square-root rate.

More precisely, with the definitions below, let \(V(\beta,q)\) be the limiting variance and \(R(\beta,q)=V(\beta,q)/V(0,q)\). For every \(-1<q<1\), the stable momentum range is \(-1/2<\beta<1\), and
\[
R(\beta,q)=\frac{1+\beta+\beta q-\beta q^2-\beta^2q-\beta^2q^2}{(1-\beta)(1+2\beta)(1+\beta q^2-\beta q)}.
\]
For \(q>0\), every global minimizer has \(\beta<0\), whereas every nonnegative \(\beta\ne0\) has \(R(\beta,q)>1\). For \(q<0\), every global minimizer has \(\beta>0\), whereas every negative \(\beta\) has \(R(\beta,q)>1\). When \(q=0\), the unique minimizer is \(\beta=0\). Global minimizers exist for every \(q\).

For \(-1<q<0\), put \(R_*(q)=\min_{-1/2<\beta<1}R(\beta,q)\). Then \(R_*(q)>1/9\) and, as \(q\downarrow-1\),
\[
R_*(q)=\frac19+\frac{8\sqrt3}{27}\sqrt{1+q}+o(\sqrt{1+q}),
\qquad
\frac{1-\beta_*(q)}{\sqrt{1+q}}\longrightarrow\sqrt3
\]
for **every** selection \(\beta_*(q)\) from the set of global minimizers. No uniqueness of the minimizer for an arbitrary fixed correlation is needed for these claims.

## Assumptions and scope

Let \(F(x)=\lambda x^2/2\), \(\lambda>0\), and use the curvature-matched fixed learning rate \(\eta=1/\lambda\). Let gradient evaluations be \(\lambda x_k+\zeta_k\), with the scaled additive noise \(\xi_k=\eta\zeta_k\) obeying
\[
\xi_k=q\xi_{k-1}+\varepsilon_k,\qquad -1<q<1.
\]
The innovations \(\varepsilon_k\) are independent and identically distributed with mean zero and variance \(\sigma^2\in(0,\infty)\), and independent of the deterministic initial iterate and its predecessor. The noise is initialized stationarily, or equivalently the limiting variance is taken after transients vanish. The standard heavy-ball recursion is
\[
x_{k+1}=x_k-\eta(\lambda x_k+\zeta_k)+\beta(x_k-x_{k-1})
=\beta(x_k-x_{k-1})-\xi_k.
\]
The objective minimizes at zero. All assertions concern the stationary variance of the *last iterate*, not Polyak averaging, nonlinear losses, time-varying step sizes, or actual without-replacement noise beyond the explicit AR(1) model.

## Proof

**1. Stable range and exact covariance.** The homogeneous iterate characteristic polynomial is \(z^2-\beta z+\beta\). The Schur–Jury inequalities give precisely \(-1/2<\beta<1\). Together with \(|q|<1\), this makes the augmented linear system stable. Define \(Y_k=(x_k,x_{k-1},\xi_{k-1})^{\mathsf T}\). It obeys
\[
Y_{k+1}=MY_k+B\varepsilon_k,\quad
M=\begin{pmatrix}\beta&-\beta&-q\\1&0&0\\0&0&q\end{pmatrix},\quad B=\begin{pmatrix}-1\\0\\1\end{pmatrix}.
\]
Because \(\rho(M)<1\), its unique stationary covariance \(\Sigma\) solves \(\Sigma=M\Sigma M^{\mathsf T}+\sigma^2BB^{\mathsf T}\), with the absolutely convergent series \(\Sigma=\sigma^2\sum_{j\ge0}M^jBB^{\mathsf T}(M^{\mathsf T})^j\). Solving the six independent linear equations in its symmetric entries gives
\[
V(\beta,q)=\Sigma_{11}=\frac{\sigma^2(1+\beta+\beta q-\beta q^2-\beta^2q-\beta^2q^2)}{(1-q^2)(1-\beta)(1+2\beta)(1+\beta q^2-\beta q)}.
\]
In particular \(V(0,q)=\sigma^2/(1-q^2)\). The stationary covariance and rational formula can be independently checked by direct substitution in the Lyapunov equation; `verify.py` performs exact symbolic elimination rather than Monte Carlo inference. All denominators are positive on the stated domain.

**2. Global sign classification.** Subtracting one from the variance ratio and factoring gives
\[
R(\beta,q)-1=
\frac{-2\beta(1-q)[q\beta(\beta-1)-\beta-q]}{(1-\beta)(1+2\beta)(1+\beta q^2-\beta q)}.
\]
For \(0<q<1\) and \(0<\beta<1\), the bracket is negative, so the difference is positive. For \(-1<q<0\) and \(-1/2<\beta<0\), the bracket equals \((-q)(1+\beta-\beta^2)-\beta>0\); the difference is again positive. At \(q=0\), the same factorization reduces to a strictly positive multiple of \(\beta^2\) for every \(\beta\ne0\). On the other hand,
\[
\left.\frac{\partial R}{\partial\beta}\right|_{\beta=0}=2q(1-q).
\]
Consequently there is an improving momentum of opposite sign to every nonzero \(q\), but none of the same sign can improve on no momentum. The ratio diverges at both stable endpoints for every fixed \(|q|<1\), by the positive numerator limits, so a global minimum is attained in the interior. This proves the claimed sign of **every** minimizer.

**3. Sharp anticorrelation limit.** For \(-1<q<0\) and \(0<\beta<1\), another exact factorization is
\[
R(\beta,q)=\frac{1}{(1+2\beta)^2}
+\frac{2\beta(1+q)[2+\beta-q(\beta^2+\beta+1)]}{(1-\beta)(1+2\beta)^2(1+\beta q^2-\beta q)}.
\]
The last summand is strictly positive. The sign classification covers \(\beta\le0\), for which \(R\ge1\). Thus for every stable \(\beta\) and every \(-1<q<0\), \(R(\beta,q)>1/9\). Let \(t=\sqrt{1+q}\). For any fixed \(c>0\) and \(\beta=1-ct\), direct rational expansion gives, uniformly for \(c\) in compact positive intervals,
\[
R(1-ct,-1+t^2)=\frac19+t\left(\frac{4c}{27}+\frac{4}{9c}\right)+O(t^2).
\]
The coefficient is uniquely minimized at \(c=\sqrt3\), where it equals \(8\sqrt3/27\). This choice gives an upper bound \(R_*(q)\le1/9+O(t)\), and the global lower bound just proved gives the matching limit.

For completeness, this expansion also controls *all* minimizers: if \(\beta_t\) minimizes, the first summand \((1+2\beta_t)^{-2}\) forces \(\beta_t\to1\) and \(1-\beta_t=O(t)\). With \(q\to-1\), \(\beta_t\to1\), the positive second summand is bounded below by a positive constant times \(t^2/(1-\beta_t)\), forcing \(1-\beta_t\ge c_0t\) for some \(c_0>0\). Therefore \(c_t=(1-\beta_t)/t\) stays inside a compact subinterval of \((0,\infty)\). The uniform expansion and uniqueness of the coefficient's minimizer force every accumulation point of \(c_t\) to equal \(\sqrt3\); hence \(c_t\to\sqrt3\), and the stated sharp expansion for \(R_*\) follows.

## Verification

Running `python verify.py` (Python 3.9+ with SymPy 1.10+) symbolically solves the six-dimensional symmetric Lyapunov system, verifies the exact rational variance and both factorizations, differentiates at zero momentum, checks the singular-limit expansion, and verifies three rational examples. Exact arithmetic gives \(V(-1/4,1/2)=328\sigma^2/255\) and \(V(1/4,-1/2)=184\sigma^2/171\); both beat \(V(0,\pm1/2)=4\sigma^2/3\). The script checks the normalized unit-innovation formulas, and scaling by \(\sigma^2\) is immediate. The proof of the global and asymptotic assertions is analytic, not dependent on finite numerical tests.

## Relationship to prior work

Kühn and Rosenow (2023), arXiv:2306.05300, establish temporally anticorrelated gradient noise under without-replacement sampling and derive stationary quadratic heavy-ball variance relations, focusing on finite-epoch covariance and nonnegative momentum. Their Theorem 4.3, Appendix C, and hyperparameter Appendix J are close prior work; the present result instead uses a genuine AR(1) noise law and permits negative momentum, deriving a global sign-optimality classification and a sharp antipersistence limit. The AR(1) model is not asserted to coincide with without-replacement noise.

Dang, Babanezhad, and Vaswani (2024), arXiv:2401.06738, study noise-adaptive heavy ball and minibatch acceleration; Pan, Liu, Wang, and Zhang (2023), arXiv:2312.14567, establish rates under independent gradient noise. Xie et al. (2021), arXiv:2103.17182, use a two-buffer positive-negative momentum construction that is algorithmically distinct from allowing a negative coefficient in classical heavy ball. These results do not state the correlated-noise sign theorem or the one-ninth optimal limit in the inspected passages. General linear-filter and discrete Lyapunov theory supplies the standard covariance machinery; an unlocated equivalent optimization result in that older literature remains a publication-precedence risk.

## Limitations

The scalar, curvature-matched step \(\eta\lambda=1\) is essential to the simple global sign theorem; no extension to other step sizes or multidimensional/noncommuting curvature is claimed. The theorem concerns additive, state-independent AR(1) noise with finite innovation variance and last-iterate stationary mean-square risk; it is neither a characterization of exact epoch sampling nor an almost-sure convergence guarantee. The optimization minimizes noise floor, not convergence time or finite-horizon loss. Uniqueness of the finite-correlation minimizer is not claimed. Independent publication-precedence validation remains outstanding.

## References

1. Marcel Kühn and Bernd Rosenow, *Correlated Noise in Epoch-Based Stochastic Gradient Descent: Implications for Weight Variances* (first posted 2023-06-08), https://arxiv.org/abs/2306.05300.
2. Anh Dang, Reza Babanezhad, and Sharan Vaswani, *(Accelerated) Noise-adaptive Stochastic Heavy-Ball Momentum* (first posted 2024-01-12), https://arxiv.org/abs/2401.06738.
3. Rui Pan, Yuxing Liu, Xiaoyu Wang, and Tong Zhang, *Accelerated Convergence of Stochastic Heavy Ball Method under Anisotropic Gradient Noise* (first posted 2023-12-22), https://arxiv.org/abs/2312.14567.
4. Zeke Xie, Li Yuan, Zhanxing Zhu, and Masashi Sugiyama, *Positive-Negative Momentum: Manipulating Stochastic Gradient Noise to Improve Generalization* (first posted 2021-03-31), https://arxiv.org/abs/2103.17182.
