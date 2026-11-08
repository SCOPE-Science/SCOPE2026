# Faster biased chirality reversals strictly amplify trapped orbital circulation

## Finding
Consider the stationary planar swimmer described below, with unequal positive chirality-flip rates and a possibly anisotropic harmonic trap. Its stationary orbital current has a fixed sign and **increases strictly in absolute magnitude when the switching clock is accelerated while the stationary chirality bias is held fixed**. The result holds at every trap anisotropy, every rotational diffusivity including zero, and every independent translational diffusivity. The spatial cross-covariance has a second sharp sign law.

Write the flip rates from clockwise and counterclockwise states as \(a,b>0\), the total rate as \(\lambda=a+b\), and the stationary chirality bias as \(\delta=(b-a)/(a+b)\in(-1,1)\). Let \(\omega>0\), \(v>0\), \(\kappa_x,\kappa_y>0\), \(D_R,D_t\ge0\). Set
\[
 A(s)=s(s+\lambda)+\omega^2,\qquad Q(s)=A(s)^2+\omega^2\lambda^2\delta^2,
 \qquad \mathcal I(s)=\frac{\omega\delta((s+\lambda)^2+\omega^2)}{Q(s)}\quad(s>0).
\]
For \(s_x=\kappa_x+D_R\) and \(s_y=\kappa_y+D_R\), the stationary cross-covariance \(C=\operatorname{Cov}(X,Y)\) and signed orbital current \(J\) are exactly
\[
 C=\frac{v^2}{2(\kappa_x+\kappa_y)}[\mathcal I(s_x)-\mathcal I(s_y)],\qquad
 J=\frac{v^2}{\kappa_x+\kappa_y}[\kappa_x\mathcal I(s_x)+\kappa_y\mathcal I(s_y)].
\]
In particular, for \(\delta\ne0\), \(\operatorname{sgn}J=\operatorname{sgn}\delta\) and \(\operatorname{sgn}C=\operatorname{sgn}(\delta(\kappa_y-\kappa_x))\) if \(\kappa_x\ne\kappa_y\). Equivalently, \(J=0\) exactly for equal flip rates, whereas \(C=0\) exactly for equal flip rates or equal trap strengths. At fixed \(0<|\delta|<1\), \(|J|\) is strictly increasing in \(\lambda\in(0,\infty)\), with sharp endpoints
\[
 J_{0+}=\frac{v^2\omega\delta}{\kappa_x+\kappa_y}
 \sum_{j\in\{x,y\}}\frac{\kappa_j}{(\kappa_j+D_R)^2+\omega^2},\qquad
 J_{\infty}=\frac{v^2\omega\delta}{\kappa_x+\kappa_y}
 \sum_{j\in\{x,y\}}\frac{\kappa_j}{(\kappa_j+D_R)^2+\omega^2\delta^2}.
\]
Thus \(0<|J_{0+}|<|J(\lambda)|<|J_\infty|\). The endpoints are limits, not additional admissible positive-rate models.

## Assumptions and scope
Let \(\sigma_t\in\{+1,-1\}\) be the stationary continuous-time Markov chain with transitions \(+1\to-1\) at rate \(a\) and \(-1\to+1\) at rate \(b\). Its stationary weights are \(\pi_+=b/(a+b)\), \(\pi_-=a/(a+b)\). Let \(W\), \(B_x\), \(B_y\) be independent two-sided standard Brownian motions, independent of \(\sigma\), and take \(\theta\) modulo \(2\pi\) with initially uniform angle independent of the stationary chain. Define
\[
 d\theta_t=\omega\sigma_t\,dt+\sqrt{2D_R}\,dW_t,\quad
 dX_t=(-\kappa_xX_t+v\cos\theta_t)\,dt+\sqrt{2D_t}\,dB_{x,t},\quad
 dY_t=(-\kappa_yY_t+v\sin\theta_t)\,dt+\sqrt{2D_t}\,dB_{y,t}.
\]
Use the stationary solutions obtained by integrating each stable linear positional equation from the infinite past. All expectations below refer to this law. Let
\[
 J=\mathbb E\bigl[X(-\kappa_yY+v\sin\theta)-Y(-\kappa_xX+v\cos\theta)\bigr].
\]
This equals the mean signed Stratonovich area rate \(\lim_{T\to\infty}T^{-1}\mathbb E\int_0^T(X_t\circ dY_t-Y_t\circ dX_t)\); the cross quadratic variation of the independent translational Brownian noises is zero. This is an orbital current, not the angular speed of \(\theta\) and not a probability-current density.

## Proof
**1. Angular spectral resolvent.** Put \(g_\pm(t)=\mathbb E[e^{i\omega\int_0^t\sigma_sds}\mid\sigma_0=\pm1]\). Their backward equations and initial conditions are
\[
 \frac d{dt}\binom{g_+}{g_-}=
 \begin{pmatrix}i\omega-a&a\\b&-i\omega-b\end{pmatrix}
 \binom{g_+}{g_-},\qquad g_+(0)=g_-(0)=1.
\]
Direct inversion of \(sI\) minus this matrix, followed by averaging with \((\pi_+,\pi_-)\), gives, for \(s>0\),
\[
 \int_0^\infty e^{-st}(\pi_+g_+(t)+\pi_-g_-(t))dt
 =\frac{s+\lambda+i\omega\delta}{s(s+\lambda)+\omega^2-i\omega\lambda\delta}.
\]
Taking imaginary parts gives the stated \(\mathcal I(s)\). Independent rotational Brownian increments multiply the angular correlation by \(e^{-D_Rt}\). In the stationary uniform-angle law, for \(t\ge0\),
\[
 \mathbb E[\cos\theta_0\sin\theta_t]=\tfrac12e^{-D_Rt}\operatorname{Im}(\pi_+g_+(t)+\pi_-g_-(t)),\quad
 \mathbb E[\sin\theta_0\cos\theta_t]=-\tfrac12e^{-D_Rt}\operatorname{Im}(\pi_+g_+(t)+\pi_-g_-(t)).
\]

**2. Stationary cross moments and current.** Stable linear filtering and the last identities give
\[
 \mathbb E[X\sin\theta]=\frac v2\mathcal I(s_x),\qquad
 \mathbb E[Y\cos\theta]=-\frac v2\mathcal I(s_y).
\]
Independence of the translational noises yields zero cross quadratic variation, so stationarity of \(XY\) gives
\[
 (\kappa_x+\kappa_y)\mathbb E[XY]
 =v\bigl(\mathbb E[X\sin\theta]+\mathbb E[Y\cos\theta]\bigr).
\]
The stationary means of \(X,Y\) vanish by uniformity of \(\theta\). Substitution proves the formula for \(C\). Expanding the definition of \(J\) as
\(J=(\kappa_x-\kappa_y)C+v(\mathbb E[X\sin\theta]-\mathbb E[Y\cos\theta])\)
and substituting again proves its formula. Independent translational noise therefore affects neither observable.

**3. Strict inequalities.** The denominator \(Q(s)\) is strictly positive. Direct differentiation at fixed \(\lambda,\delta,\omega\) yields
\[
 \partial_s\mathcal I(s)=-\frac{2\omega\delta P(s)}{Q(s)^2},
\]
where
\[
 \begin{aligned}
 P(s)={}&s^5+4\lambda s^4+(6\lambda^2+2\omega^2)s^3
 +(4\lambda^3+4\lambda\omega^2)s^2\\
 &+(\lambda^4+(3-\delta^2)\lambda^2\omega^2+\omega^4)s
 +(1-\delta^2)\lambda^3\omega^2.
 \end{aligned}
\]
Every displayed coefficient is nonnegative, and \(P(s)>0\) for \(s>0\). Therefore \(\mathcal I(s)\) has the strict sign of \(\delta\) and decreases strictly in \(s\) if \(\delta>0\) (increases strictly if \(\delta<0\)). The stated exact zero sets and signs of \(C,J\) follow.

For fixed \(\delta\), differentiation with respect to the *total* flip rate gives the exact identity
\[
 \partial_\lambda\mathcal I(s)
 =\frac{2\lambda\omega^3\delta(1-\delta^2)
 (\lambda s+s^2+\omega^2)}{Q(s)^2}.
\]
Since \(\lambda>0\), \(0<|\delta|<1\), and \(s>0\), this derivative has the strict sign of \(\delta\). Both weights \(\kappa_x,\kappa_y\) in \(J\) are positive, proving strict growth of \(|J|\) with \(\lambda\). Finally, substituting \(\lambda\downarrow0\) and \(\lambda\to\infty\) into \(\mathcal I\) gives respectively \(\omega\delta/(s^2+\omega^2)\) and \(\omega\delta/(s^2+\omega^2\delta^2)\), proving the endpoint formulas and their strict ordering.

## Verification
The accompanying `checks.py` is a standalone standard-library Python program. Running `python checks.py` checks the matrix resolvent against the rational formula, both derivative identities and strict signs over nontrivial grids, integrates the original two-state angular backward equations with an independent Runge–Kutta/Simpson computation, checks the stationary cross-moment/current identities, and checks both rate endpoints. It passed 1,082 deterministic assertions in the prepared package. These finite checks are not substituted for the coefficient-positivity and resolvent proofs above.

## Relationship to prior work
Das and Basu (2023, arXiv:2301.11194) formulate and study *symmetric* chirality switching in free space. Their Section 5 explicitly identifies confinement as a further problem, and their Appendix A supplies a symmetric telegraph Fourier propagator. Caprini, Löwen and Marini Bettolo Marconi (2023, arXiv:2306.11133) study *constant* chirality in circular and elliptic traps, including anisotropy-induced cross-correlation and angular currents. Santra, Basu and Sabhapandit (2021, arXiv:2107.12640) study *propulsion-direction* reversals in a harmonic potential, rather than switching the sign of angular velocity; only their abstract was accessible in the present comparison. The elementary linear-filter response underlying our covariance is not new. The result here differs by treating two unequal positive chirality-switch rates jointly with anisotropic confinement, proving an exact zero/sign classification, and establishing strict switching-speed enhancement at fixed chirality bias, independent of trap shape and added positional thermal diffusion. The fixed-bias condition is essential: changing one rate alone also changes \(\delta\), and is not covered by the monotonicity assertion.

## Limitations
This is an exactly specified noninteracting, fixed-speed, angular-telegraph model in a harmonic trap. No claim is made for nonlinear confinement, state-dependent tumbling, non-Markovian chirality clocks, many-particle interactions, or the full stationary density. The signed orbital current is a second-order stationary observable and does not by itself determine entropy production or the whole probability current. The limit \(\lambda\downarrow0\) is a limit of stationary positive-rate models, not a claim of ergodicity for zero rate. The positivity proof is analytic; finite checks do not establish infinite-parameter uniqueness or priority over unindexed literature.

## References
1. S. Das and U. Basu, *Chirality Reversing Active Brownian Motion in Two Dimensions*, arXiv:2301.11194, first posted 2023-01-26, https://arxiv.org/abs/2301.11194 (Sections 2, 3, 5 and Appendix A).
2. L. Caprini, H. Löwen and U. Marini Bettolo Marconi, *Chiral active matter in external potentials*, arXiv:2306.11133, first posted 2023-06-19, https://arxiv.org/abs/2306.11133 (Sections II, IV and Appendix B); *Soft Matter* 19 (2023), 6234–6246.
3. I. Santra, U. Basu and S. Sabhapandit, *Direction reversing active Brownian particle in a harmonic potential*, arXiv:2107.12640, first posted 2021-07-27, https://arxiv.org/abs/2107.12640; *Soft Matter* 17 (2021), 10108–10119. Abstract-level comparison only.
