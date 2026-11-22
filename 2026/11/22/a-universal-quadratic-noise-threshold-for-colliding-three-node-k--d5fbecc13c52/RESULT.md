# A universal quadratic noise threshold for colliding three-node kernel quadrature

## Finding

Consider the unmodified Bayesian kernel quadrature estimator with three distinct symmetric nodes \((-d,0,d)\), a symmetric non-point integration probability measure \(\mu\), and independent equal-variance Gaussian observation noise \(\eta\ge0\). Let the normalized covariance kernel be a Gaussian scale mixture
\[
k(x,y)=\mathbb E[\exp\{-Q(x-y)^2\}],
\qquad Q\ge0,\quad \mathbb P(Q>0)>0,\quad
0<q_1=\mathbb E Q<\infty,\quad q_2=\mathbb E Q^2<\infty.
\]
For every spacing \(d>0\), both outer posterior-mean quadrature weights are strictly positive. The middle weight is nonnegative **if and only if** the noise variance meets the exact, possibly negative, threshold
\[
\boxed{\eta\ge\eta_c(d):=
\frac{2k(d)m(d)}{m(0)}-1-k(2d)},
\qquad
m(z)=\int k(z,x)\,\mu(dx),\quad k(r)=\mathbb E e^{-Qr^2}.
\]
Equality gives a zero middle weight; strict inequality gives a positive middle weight. If \(\eta_c(d)<0\), every admissible nonnegative noise variance already gives strictly positive weights.

Define
\[
A=2q_1+\frac{m''(0)}{m(0)}>0,
\qquad H=3q_2-q_1^2>0.
\]
The exact colliding-node limits are
\[
\boxed{\eta_c(d)=A d^2+o(d^2)},
\qquad
\boxed{w_0(\eta=0,d)\sim -\frac{m(0)A}{2H d^2}},
\qquad
\boxed{w_\pm(\eta=0,d)\sim\frac{m(0)A}{4H d^2}}.
\]
Moreover, for any fixed \(c>0\), if \(\eta(d)=c d^2+o(d^2)\), then
\[
\boxed{w_0\longrightarrow\frac{m(0)(c-A)}{3c},
\qquad w_\pm\longrightarrow\frac{m(0)(2c+A)}{6c}}.
\]
Thus the sharp noise regularization scale for positivity is quadratic in the physical node spacing. The theorem concerns *signs of unmodified posterior weights*, not optimal approximation error or a constrained positive-weight algorithm.

## Assumptions and scope

The probability measure \(\mu\) on \(\mathbb R\) is symmetric about zero and satisfies \(\mu(\mathbb R\setminus\{0\})>0\). Its support may be bounded or unbounded; the integral defining \(m\) exists because \(0<k\le1\). The three distinct observation sites are \(-d,0,d\) with \(d>0\); for an integration domain with restricted sites, choose \(d\) within that domain. The mixing variable \(Q\) is independent of the integration variable. The fixed covariance is normalized to \(k(0)=1\). Errors at the three observations are independent centered Gaussian variables with common known variance \(\eta\), independent of the Gaussian-process prior. The weights below are its exact linear-Gaussian conditional-mean weights.

The unconstrained weight vector is
\[
w=(K_d+\eta I_3)^{-1}(m(d),m(0),m(d))^{\mathsf T},
\quad
K_d=\begin{pmatrix}1&k(d)&k(2d)\\k(d)&1&k(d)\\k(2d)&k(d)&1\end{pmatrix}.
\]
The estimator is not explicitly normalized to integrate constants exactly. The second mixing moment condition is essential for the stated fourth-order Gram determinant and quadratic weight blowup; no corresponding power law is asserted for rougher kernels with infinite \(\mathbb E Q^2\).

## Proof

**1. Strict positive definiteness and exact weights.** Each kernel \(\exp\{-q(x-y)^2\}\) with \(q>0\) is strictly positive definite on distinct real sites; since \(\mathbb P(Q>0)>0\), so is the mixture. Thus \(K_d+\eta I_3\) is positive definite for every \(d>0,\eta\ge0\). Symmetry forces \(w=(u,v,u)\). With
\[
c_d=k(d),\quad e_d=k(2d),\quad m_0=m(0),\quad m_d=m(d),
\quad\Delta_d=(1+\eta)(1+\eta+e_d)-2c_d^2>0,
\]
the two independent Gram equations give the exact Cramer formulas
\[
\boxed{u=\frac{(1+\eta)m_d-c_dm_0}{\Delta_d}},
\qquad
\boxed{v=\frac{(1+\eta+e_d)m_0-2c_dm_d}{\Delta_d}}
=\frac{m_0(\eta-\eta_c(d))}{\Delta_d}.
\]
This immediately gives the middle-weight sign classification once \(u>0\) is proved.

**2. Every outer weight is positive.** For a fixed scale \(q\), put \(M_q=\int e^{-qx^2}\,\mu(dx)\). Symmetry yields
\[
\int e^{-q(x-d)^2}\,\mu(dx)
=e^{-qd^2}\int e^{-qx^2}\cosh(2qxd)\,\mu(dx).
\]
The last integral is strictly greater than \(M_q\) for every \(q,d>0\), because \(\mu\) has positive mass away from zero. Meanwhile, both \(e^{-qd^2}\) and \(M_q\) decrease with \(q\), so the Chebyshev covariance identity gives
\[
\mathbb E[e^{-Qd^2}M_Q]\ge
\mathbb E[e^{-Qd^2}]\,\mathbb E[M_Q]=c_dm_0.
\]
Averaging the previous strict inequality over the positive-probability event \(Q>0\), one obtains \(m_d>c_dm_0\). Therefore
\((1+\eta)m_d-c_dm_0>0\) for all allowed parameters, proving \(u>0\) independently of the middle weight.

**3. The strictly positive collision coefficient.** Since \(q_2<\infty\), differentiation and Taylor expansion under the expectations are justified; symmetry implies \(m'(0)=0\), and
\[
m''(0)=\mathbb E_{Q,X}\left[(4Q^2X^2-2Q)e^{-QX^2}\right],
\qquad X\sim\mu.
\]
The positive quantity \(m_d-c_dm_0\) satisfies
\[
\lim_{d\downarrow0}\frac{m_d-c_dm_0}{d^2}
=\frac{m_0A}{2}.
\]
This coefficient is strictly positive, not merely nonnegative. Indeed the fixed-scale cosh contribution, divided by \(d^2\), tends to
\(2\mathbb E[Q^2X^2e^{-QX^2}]>0\), by dominated convergence. Its companion covariance term is nonnegative for each \(d\), so cannot cancel this positive contribution. The strict inequality uses both \(\mathbb P(Q>0)>0\) and \(\mu(|X|>0)>0\). Thus \(A>0\). More explicitly, write
\[
c_d=1-q_1d^2+\tfrac12q_2d^4+o(d^4),
\quad e_d=1-4q_1d^2+8q_2d^4+o(d^4),
\quad m_d=m_0+\tfrac12m''(0)d^2+o(d^2).
\]
Substitution in the exact \(\eta_c\) formula establishes \(\eta_c(d)=Ad^2+o(d^2)\).

**4. Exact weight growth and critical regularization.** For \(\eta=0\), the determinant factor satisfies
\[
\Delta_d=1+e_d-2c_d^2=2(3q_2-q_1^2)d^4+o(d^4)=2Hd^4+o(d^4).
\]
Here \(H>0\) follows from \(q_2\ge q_1^2>0\). The middle numerator is \(-m_0\eta_c(d)=-m_0Ad^2+o(d^2)\), and the outer numerator is \(m_d-c_dm_0=m_0Ad^2/2+o(d^2)\). Dividing proves both divergent-weight limits. With \(\eta(d)=cd^2+o(d^2)\), the same exact determinant instead satisfies \(\Delta_d=3cd^2+o(d^2)\), yielding the stated three finite weight limits. Consequently any fixed positive coefficient below \(A\) produces an eventually negative middle weight, while any coefficient above \(A\) produces an eventually positive one; the exact threshold, rather than this leading approximation, decides equality at finite spacing.

**5. A closed Matérn-\(5/2\) instance.** On \([0,1]\) with uniform probability measure, take the kernel
\[
k_\lambda(x,y)=\left(1+\lambda|x-y|+\frac{\lambda^2(x-y)^2}{3}\right)e^{-\lambda|x-y|},\qquad\lambda>0,
\]
and sites \((\tfrac12-d,\tfrac12,\tfrac12+d)\), \(0<d\le\tfrac12\). It has the Gaussian scale-mixture representation \(\mathbb E e^{-\lambda^2r^2/(4S)}\), with \(S\) gamma-distributed with shape \(5/2\) and unit rate. Put \(L=\lambda/2\), \(r=\lambda d\),
\[
\kappa(t)=(1+t+t^2/3)e^{-t},\quad
J(t)=\frac{8-(t^2+5t+8)e^{-t}}3,
\quad m_0=\frac{2J(L)}\lambda,\quad
m_d=\frac{J(L-r)+J(L+r)}\lambda.
\]
The exact threshold becomes
\[
\boxed{\eta_c(d,\lambda)
=\kappa(r)\frac{J(L-r)+J(L+r)}{J(L)}-1-\kappa(2r)},
\]
while the sharp collision expansion is
\[
\boxed{\eta_c(d,\lambda)
=\frac{(\lambda d)^2}{3}\left(1-\frac{L(1+L)e^{-L}}{J(L)}\right)
+O((\lambda d)^4)}
\]
for fixed \(\lambda>0\). The coefficient is strictly positive because \(J(0)=0\) and
\[\frac{d}{dL}\big[J(L)-L(1+L)e^{-L}\big]=\frac43L^2e^{-L}>0.\]
For \(\lambda=1,d=1/10\), the exact formula gives \(\eta_c=0.00021656365998818\ldots\) and noiseless central weight \(-5.52826600287479\ldots\), illustrating that a very small nonnegative noise variance can be the exact sign-restoring threshold for a badly clustered noiseless rule.

## Verification

The standalone \(\texttt{verify.py}\) checks the symmetric Gram-system identities and Taylor coefficients symbolically. Using arbitrary precision, it also compares the formulas with independent direct three-by-three linear solves for a two-scale Gaussian mixture and a discrete symmetric target, and for Matérn-\(5/2\) kernels with four inverse lengthscales and multiple spacings and noise levels. It checks the sign boundary, finite-nugget and zero-nugget asymptotic behavior, and the displayed numerical instance. The completed run returned 112 finite parameter groups and successful symbolic identities. Run \(\texttt{python verify.py}\) with the libraries listed in \(\texttt{requirements.txt}\); the analytical arguments, not the finite checks, prove the universal claims.

## Relationship to prior work

Karvonen, Kanagawa and Särkkä [1] investigate positivity and magnitude bounds for Bayesian quadrature weights, including implications of total positivity and node optimality and numerical experiments with Matérn kernels. Those statements do not give a universal noisy symmetric three-node sign law or a sharp finite-mixing-moment collision scale. Hayakawa, Oberhauser and Lyons [2] construct explicitly positive kernel quadrature rules, whereas the present theorem classifies **unmodified**, potentially signed posterior weights and the noise required to change their signs. Glaubitz and Reeger [3] investigate stability of RBF integration and remedies based on shape parameters and least squares; their general stability results do not imply the exact covariance-mixture coefficient \(A\) or the \(d^{-2}\) divergence. Related existing exact analyses for a Gaussian kernel under zero noise and for a Matérn-\(3/2\) kernel on a fixed interval cover narrower kernels or distinct smoothness regimes, but neither supplies the all-mixture, arbitrary symmetric-target theorem with finite-second-mixing-moment asymptotics here. The two-center and three-center settings, and formula equivalences, were compared at the level of hypotheses and implications, not merely titles.

## Limitations

The result is for exactly three symmetric nodes, symmetric non-point target measures, independent equal-variance noise, a normalized nondegenerate Gaussian scale-mixture kernel, and exact arithmetic. It does not prove monotonicity of the threshold as the node spacing changes, classify arbitrary asymmetric sites, optimize sites or kernels, or establish improved quadrature accuracy. In particular the noise threshold ensures **nonnegative weights**, not unbiasedness for constants or optimal mean-squared error; adding noise is not advocated when measurement precision is freely controllable. If the second mixing moment diverges, neither the \(d^{-2}\) law nor its coefficient is asserted. Published priority may be affected by specialized kernel interpolation and quadrature results not located in the inspected sources.

## References

[1] T. Karvonen, M. Kanagawa, S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, first public 2018-12-20, arXiv:1812.08509; *Statistics and Computing* 29 (2019), 1317–1333. https://arxiv.org/abs/1812.08509 ; https://doi.org/10.1007/s11222-019-09901-0

[2] S. Hayakawa, H. Oberhauser, T. Lyons, *Positively Weighted Kernel Quadrature via Subsampling*, first public 2021-07-20, arXiv:2107.09597. https://arxiv.org/abs/2107.09597

[3] J. Glaubitz, J. A. Reeger, *Towards stability results for global radial basis function based quadrature formulas*, first public 2023-01-30, arXiv:2301.12998. https://arxiv.org/html/2301.12998v1

[4] T. Karvonen, S. Särkkä, *Gaussian kernel quadrature at scaled Gauss–Hermite nodes*, first public 2018-03-26, arXiv:1803.09532. https://arxiv.org/html/1803.09532v4
