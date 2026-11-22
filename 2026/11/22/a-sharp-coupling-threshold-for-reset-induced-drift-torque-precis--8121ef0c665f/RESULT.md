# A sharp coupling threshold for reset-induced drift-torque precision in a Brownian gyrator

## Finding

A harmonically confined two-temperature Brownian gyrator is completely reset to the origin at independent Poisson rate \(r>0\). Let \(T_x,T_y>0\) be unequal and let \(0<|u|<1\) be the coupling magnitude. Define the *finite, noise-conditional drift torque* \(\tau=u(Y^2-X^2)\), distinct from the white-noise-inclusive instantaneous angular momentum. Set
\[
S=\frac{T_x+T_y}{2},\qquad H=\frac{T_x-T_y}{2},\qquad k=\frac{S^2}{H^2}>1,\qquad w=u^2\in(0,1).
\]
The stationary squared coefficient of variation \(\mathcal C(r)=\operatorname{Var}(\tau)/(\mathbb E\tau)^2\) is
\[
\boxed{\mathcal C(r)=\frac{2k(r+2)^3}{(r+4)((r+2)^2-4w)}+\frac{3r+4}{r+4}.}
\]
Define the sharp coupling threshold
\[
\boxed{w_c(k)=\frac{5k+4-\sqrt{k(25k+32)}}{4}\in(1/5,1).}
\]
If \(0<w\le w_c(k)\), \(\mathcal C(r)\) is strictly increasing on \(r>0\). If \(w_c(k)<w<1\), it has **exactly one positive critical point**, a strict global minimum \(r_*(k,w)\). This is the unique positive zero of the explicit quartic \(B_{k,w}\) in the proof below. At the boundary \(w=w_c(k)\), the zero derivative occurs only in the excluded no-reset limit \(r=0\).

Furthermore, for every lag \(t\ge0\),
\[
\operatorname{Cov}(\tau(t),\tau(0))=e^{-(r+2)t}\operatorname{Var}(\tau),
\]
so the drift-torque autocovariance has a single exponential relaxation rate, although its stationary one-time law is generally non-Gaussian. At fixed \(k>1\), as \(|u|\uparrow1\), \(\mathcal C(0^+)\to\infty\) while the finite-reset minimum stays bounded above; thus the relative snapshot-precision gain can approach \(100\%\).

## Assumptions and scope

Between resetting events, the planar Itô process obeys
\[
dX_t=(-X_t-uY_t)dt+\sqrt{2T_x}\,dW_t^x,\qquad
dY_t=(-Y_t-uX_t)dt+\sqrt{2T_y}\,dW_t^y,
\]
with independent standard Wiener processes. The resetting clock is independent of both Wiener noises. Every reset instantaneously replaces **both** coordinates with zero. Parameters obey \(T_x,T_y>0\), \(T_x\ne T_y\), \(0<|u|<1\), and \(r>0\). Expectations refer to the unique stationary law. The observable \(\tau=u(Y^2-X^2)\) is the conditional mean of the continuous-path angular momentum rate, not the white-noise-inclusive angular momentum and not reset-chord work or total entropy production. The no-reset value means the limit \(r\downarrow0\), which exists in the stable regime.

## Proof

Diagonalize the linear force by \(U=(X+Y)/\sqrt2\), \(V=(X-Y)/\sqrt2\). Their drift rates are \(a=1+u\), \(b=1-u\), so \(a+b=2\). Their diffusion covariance is \(2\bigl(\begin{smallmatrix}S&H\\H&S\end{smallmatrix}\bigr)dt\). Put \(Q=UV\), so \(\tau=-2uQ\). The generator including origin-reset jumps is
\[
\mathcal Lf=-aU\partial_U f-bV\partial_V f+S(\partial_U^2+\partial_V^2)f+2H\partial_U\partial_V f+r[f(0,0)-f(U,V)].
\]
Applying the stationary generator identity to \(U^2,V^2,UV\), gives
\[
\mathbb E U^2=\frac{2S}{r+2a},\quad
\mathbb E V^2=\frac{2S}{r+2b},\quad
\mathbb E Q=\frac{2H}{r+2}.
\]
In particular \(\mathbb E\tau=-4uH/(r+2)\ne0\). Applying it to \(U^2V^2\) yields the exact fourth-moment equation
\[
(r+4)\mathbb E(U^2V^2)=2S(\mathbb E U^2+\mathbb E V^2)+8H\mathbb E(UV).
\]
Substitution and subtraction of \((\mathbb EQ)^2\) gives
\[
\operatorname{Var}(Q)=\frac{8S^2(r+2)}{(r+4)((r+2)^2-4u^2)}+\frac{4H^2(3r+4)}{(r+2)^2(r+4)}.
\]
Dividing by \((\mathbb E Q)^2=4H^2/(r+2)^2\) proves the claimed \(\mathcal C\) formula.

Write \(w=u^2\). Direct differentiation gives
\[
\mathcal C'(r)=\frac{4B_{k,w}(r)}{(r+4)^2((r+2)^2-4w)^2},
\]
where
\[
\begin{aligned}
B_{k,w}(r)={}&(k+2)r^4+(8k+16-4kw)r^3\\
&+(24k+48-36kw-16w)r^2\\
&+(32k+64-96kw-64w)r\\
&+16[k(1-5w)+2(1-w)^2].
\end{aligned}
\]
The denominator is strictly positive for \(r\ge0\), \(0<w<1\). The constant coefficient has the sign of \(g_k(w)=k(1-5w)+2(1-w)^2\). This function is strictly decreasing on \([0,1]\), is positive at zero, and negative at one. Its unique zero there is \(w_c(k)\) above. It exceeds \(1/5\), because \(g_k(1/5)>0\).

The linear coefficient is positive when \(w<w_L=(k+2)/(3k+2)\), and the quadratic coefficient is positive when \(w<w_Q=6(k+2)/(9k+4)\). For \(k>1\), \(w_L<w_Q\). Also \(g_k(w_L)=-2k(k+2)(3k+4)/(3k+2)^2<0\), hence \(w_c<w_L<w_Q\). The cubic and quartic coefficients are positive throughout \(0<w<1\).

If \(w\le w_c\), every nonconstant coefficient is strictly positive and the constant one is nonnegative; thus \(B(r)>0\) for every \(r>0\). If \(w>w_c\), the constant coefficient is negative, while potential negative linear and quadratic coefficients arise *in that order* as \(w\) grows through \(w_L,w_Q\). Consequently, the ordered nonzero coefficient list (from degree four to zero) has **exactly one sign change**. Descartes' rule of signs gives at most one positive root counting multiplicity. As \(B(0)<0\) and \(B(r)\to+\infty\), a positive root exists and the derivative changes from negative to positive there. This proves its uniqueness, simplicity, and strict global minimality.

Finally, \(\mathcal LQ=-(r+2)Q+2H\), so \(Q-\mathbb EQ\) is an exact generator eigenfunction. The stationary Markov semigroup therefore gives \(\mathbb E[Q(t)-\mathbb EQ\mid Q(0)]=e^{-(r+2)t}(Q(0)-\mathbb EQ)\). Multiplying by the centered initial value gives the claimed autocovariance. Also \(\mathcal C(0^+)=1+k/(1-w)\to\infty\) for fixed \(k\) as \(w\uparrow1\), while \(\mathcal C(1)\) remains bounded, proving the limiting precision gain.

## Verification

The standalone file `verify.py` checks the exact second-/fourth-moment identities, the rational derivative and quartic coefficients by symbolic algebra. It independently integrates the conditional-Gaussian fourth moment over exponential reset age for five nontrivial parameter choices, comparing it to the generator result. A further numerical test checks one positive quartic root and its global-minimum consistency. The program completed with all assertions satisfied. The proof of the all-parameter root count is the analytic sign/Descartes argument above, not finite sampling.

As an illustrative unequal-temperature case, \(T_x=3,T_y=1\) gives \(k=4\), so \(\sqrt{w_c}\approx0.505408106\). At \(u=0.8\), the unique optimal rate is \(r_*\approx1.57059239449\); the squared coefficient of variation improves from \(12.1111111111\) (no resetting) to \(7.98000479132\) (optimal resetting).

## Relationship to prior work

Majumdar, Schehr, Viot and Oshanin (arXiv:2611.06322, first submitted 2026-11-04) study the same Brownian-gyrator generator under fixed-point and circular Poisson resets, obtain stationary position moments, local currents, and angular-momentum/velocity statistics. Their Appendix A identifies the deterministic conditional angular-momentum term \(u(Y^2-X^2)\). This paper supplies the established model and first/second-moment context; the present result isolates its finite drift torque, obtains its fourth-moment precision, and proves a global coupling-versus-reset-rate transition not stated in the inspected full text.

Viot et al. (arXiv:2307.05248; 2024 journal publication) calculate the white-noise-inclusive finite-time-step angular-momentum distribution of the **unreset** gyrator and show its divergent variance as time resolution increases. Their observable and resetting assumptions differ from this finite conditional-drift-torque result. Related results on non-Markovian gyrator torque generating functions, inertial-gyrator precision optimization, and coordinate-selective resetting do not directly imply this complete-origin-reset threshold. The general stationary moment method is not claimed as new.

## Limitations

This result concerns the stationary conditional drift torque and its *single-snapshot squared coefficient of variation*, not physical motor efficiency, measured total angular momentum with white noise, reset-chord circulation, integrated full-path stochastic area, or a universal thermodynamic uncertainty relation. It does not model finite-time reset operations, correlated baths, nonzero reset locations, or noisy torque measurement. Higher-point distributions and nonlinear resetting protocols are not classified. The literature comparison is not an independence audit; unindexed equivalent calculations remain possible.

## References

1. S. N. Majumdar, G. Schehr, P. Viot, and G. Oshanin, *Brownian gyrator model with stochastic resetting*, arXiv:2611.06322 (first submitted 2026-11-04), https://arxiv.org/abs/2611.06322.
2. P. Viot, A. Argun, G. Volpe, A. Imparato, L. Rondoni, and G. Oshanin, *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248, https://arxiv.org/abs/2307.05248; *Soft Matter* 20 (2024), 3154–3160.
3. E. S. Nascimento and W. A. M. Morgado, *Stationary properties of a non-Markovian Brownian gyrator*, *Journal of Statistical Mechanics* 2021, 013301, https://doi.org/10.1088/1742-5468/abd027.
