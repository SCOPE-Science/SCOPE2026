# A sharp Gaussian–logarithmic–stable trichotomy for renewal-reset quadratic occupation

## Finding

For Brownian diffusion restarted at i.i.d. exact-Pareto renewal times, the time-averaged quadratic displacement has a **finite deterministic limit whenever the reset interval has a finite second moment**, but its centered *fluctuation law* changes at the fourth waiting-time moment. The sharp result is

\[
\begin{aligned}
\alpha>4:&\quad \sqrt t\,(Q_t-\mu)\ \Rightarrow\ N(0,\sigma_\alpha^2),\\
\alpha=4:&\quad \sqrt{t/\log t}\,(Q_t-\mu)\ \Rightarrow\ N(0,7D^2/4),\\
2<\alpha<4:&\quad t^{1-2/\alpha}\,(Q_t-\mu)\ \Rightarrow\ S_{\alpha/2}.
\end{aligned}
\]

Here \(S_{\alpha/2}\) is a *non-Gaussian*, centered, spectrally positive stable law with its scale fixed explicitly below. Thus a finite long-run quadratic exposure does not ensure Gaussian sampling fluctuations. The statements concern fluctuations in distribution, not the finite-time variance or a functional limit theorem.

## Assumptions and scope

Fix \(D>0\) and \(\alpha>2\). Let \((T_i)_{i\ge1}\) be i.i.d. positive real reset durations, independent of independent standard Brownian motions \((W_i)_{i\ge1}\), with exact survival

\[
\Pr(T_i>u)=\begin{cases}1,&0\le u<1,\\u^{-\alpha},&u\ge1.\end{cases}
\]

Write \(S_n=\sum_{i=1}^nT_i\), \(N(t)=\max\{n:S_n\le t\}\), and \(A_t=t-S_{N(t)}\). At elapsed time \(a\) since the most recent reset, \(X_{S_n+a}=\sqrt{2D}\,W_{n+1}(a)\) for \(0\le a<T_{n+1}\). Define

\[
Q_t=\frac1t\int_0^t X_s^2\,ds,\qquad
m=\mathbb ET=\frac\alpha{\alpha-1},\qquad
\mu=\frac{D\mathbb ET^2}{\mathbb ET}=D\frac{\alpha-1}{\alpha-2}.
\]

The process starts with a reset at time zero; no equilibrium initialization or finite fourth waiting-time moment is imposed when \(2<\alpha\le4\). All convergence claims are as \(t\to\infty\).

For \(\alpha>4\), put \(q=\mu/D\) and \(a_j=\alpha/(\alpha-j)\) (only the finite moments \(j\le4<\alpha\) are used), then

\[
\sigma_\alpha^2=\frac{D^2}{m}\left(\frac73a_4-2qa_3+q^2a_2\right)>0.
\]

For \(2<\alpha<4\), write \(\beta=\alpha/2\in(1,2)\), let \(W\) be a standard Brownian motion on \([0,1]\), and define

\[
J=\int_0^1W_s^2ds,\quad c_\alpha=\mathbb E[(2DJ)^\beta],\quad
\mathbb E e^{iuS_\beta}=\exp\!\left\{\frac{\beta c_\alpha}{m}\Gamma(-\beta)(-iu)^\beta\right\}.
\]

The fractional power uses the principal complex branch. This characteristic function uniquely specifies the centered stable law, including its skewness and scale. For numerical evaluation,

\[
\mathbb E e^{-s(2DJ)}=(\cosh\sqrt{4Ds})^{-1/2},\quad
c_\alpha=\frac1{\Gamma(-\beta)}\int_0^\infty
\frac{(\cosh\sqrt{4Ds})^{-1/2}-1+Ds}{s^{1+\beta}}\,ds.
\]

The last integral is finite and positive for \(1<\beta<2\).

## Proof

**1. Exact cycle reward law.** Let \(R_i=\int_0^{T_i}(\sqrt{2D}W_i(s))^2ds\). Brownian self-similarity gives the joint representation

\[
(T_i,R_i)\stackrel d=(T_i,2DT_i^2J_i),
\]

where the \(J_i\) are i.i.d. copies of \(J\), independent of all waiting times. Wick's formula yields

\[
\mathbb EJ=\frac12,\quad
\mathbb EJ^2=\int_0^1\!\int_0^1\!
\bigl(su+2\min(s,u)^2\bigr)ds\,du=\frac7{12}.
\]

Consequently \(\mathbb ER=D\mathbb ET^2\), \(\mathbb ER^2=(7/3)D^2\mathbb ET^4\) whenever finite, and \(\mathbb E(RT)=D\mathbb ET^3\). The Laplace transform of \(J\) follows from the eigenvalues \(\lambda_j=[\pi^2(j-1/2)^2]^{-1}\) of the Brownian covariance kernel: \(J\stackrel d=\sum_{j\ge1}\lambda_jZ_j^2\), with independent standard Gaussian \(Z_j\); the product identity for \(\cosh\) gives the formula above.

**2. Centering and the unfinished interval.** Put \(Y_i=R_i-\mu T_i\). Then \(\mathbb EY_i=0\) since \(\alpha>2\). The exact decomposition is

\[
t(Q_t-\mu)=\sum_{i=1}^{N(t)}Y_i+U_t-\mu A_t,
\quad U_t=\int_0^{A_t}(\sqrt{2D}W_{N(t)+1}(s))^2ds.
\]

The ordinary renewal theorem for non-arithmetic positive interarrivals of finite mean implies that the age \(A_t\) is tight. Since the current Brownian leg is independent of reset times, conditional Brownian scaling implies that \(U_t\) is also tight. Thus \(U_t-\mu A_t=O_{\mathbb P}(1)\), negligible after division by any normalization diverging to infinity. Moreover, \(\mathbb ER<\infty\) and the full terminal cycle reward divided by \(t\) tends to zero almost surely by Borel–Cantelli and \(N(t)/t\to1/m\); the renewal reward strong law therefore gives \(Q_t\to\mu\) almost surely.

**3. The finite-fourth-moment regime.** For \(\alpha>4\), \(Y_i\) have finite positive variance

\[
\mathbb EY_i^2=D^2\left(\frac73\mathbb ET^4-2q\mathbb ET^3+q^2\mathbb ET^2\right).
\]

Apply the i.i.d. central limit theorem and the renewal random-index theorem. The functional i.i.d. invariance principle combined with the uniform renewal law gives the same conclusion even though \(Y_i\) and \(T_i\) are correlated. With \(N(t)/t\to1/m\), and the negligible incomplete term, the limiting variance is \(\mathbb EY_i^2/m\), as claimed. At \(D=1,\alpha=6\), the exact value is \(\sigma_6^2=695/192\).

**4. Stable domain \(2<\alpha<4\).** Since \(\Pr(T_i^2>x)=x^{-\beta}\) for \(x\ge1\), Breiman's product-tail lemma applies to \(R_i=T_i^2(2DJ_i)\): Brownian quadratic area has moments of every positive order, and hence

\[
\Pr(R_i>x)\sim c_\alpha x^{-\beta}.
\]

The subtraction \(-\mu T_i\) does not change the positive-tail constant: on \(T_i\le\varepsilon x/\mu\), \(R_i>(1+\varepsilon)x\) implies \(Y_i>x\), while \(Y_i>x\) implies \(R_i>x\), and \(\Pr(T_i>\varepsilon x/\mu)=O(x^{-\alpha})=o(x^{-\beta})\). Also \(Y_i\ge-\mu T_i\), so \(\Pr(Y_i<-x)=O(x^{-\alpha})=o(x^{-\beta})\). Therefore

\[
\Pr(Y_i>x)\sim c_\alpha x^{-\beta},\qquad
\Pr(Y_i<-x)=o(x^{-\beta}).
\]

These are precisely the centered spectrally positive \(\beta\)-stable domain-of-attraction conditions, with Lévy measure \(\beta c_\alpha x^{-1-\beta}\mathbf 1_{x>0}dx\). Its characteristic exponent is \(\beta c_\alpha\Gamma(-\beta)(-iu)^\beta\). For sums indexed by \(N(t)\), the functional stable limit theorem and the random time-change law \(N(t)/t\to1/m\) supply the factor \(1/m\) in the exponent. Dividing \(t(Q_t-\mu)\) by \(t^{1/\beta}\) proves the stated stable limit.

**5. Logarithmic boundary \(\alpha=4\).** Here \(\beta=2\) and \(Y_i\) has \(\Pr(Y_i>x)\sim c_4x^{-2}\), negligible negative tail, and

\[
c_4=\mathbb E[(2DJ)^2]=\frac73D^2,\qquad
\mathbb E[Y_i^2\mathbf1_{\{|Y_i|\le z\}}]\sim2c_4\log z.
\]

The truncated-variance normal domain-of-attraction theorem yields

\[
\frac{\sum_{i=1}^nY_i}{\sqrt{c_4n\log n}}\ \Rightarrow\ N(0,1).
\]

The same random time-change argument and \(m=4/3\) imply

\[
\sqrt{\frac t{\log t}}(Q_t-\mu)\Rightarrow N\!\left(0,\frac{c_4}{m}\right)=N\!\left(0,\frac74D^2\right).
\]

This completes all three regimes, including the terminal partial cycle.

## Verification

Run `python checker.py` with Python 3, NumPy and SciPy. The standalone deterministic checks compare the exact Gaussian covariance integral with the Brownian Karhunen–Loève expansion, the associated Laplace-product identity, exact Pareto moment constants, critical and Gaussian coefficients, a fractional stable-law amplitude computed by quadrature, characteristic-exponent sign conditions, and independently simulated Brownian cycles. The run used the checker extracted from this complete package; finite checks are supporting diagnostics, **not** proof of the infinite-horizon distributional limits. In particular, the proof's Brownian scaling, regular variation, renewal-age tightness, and stable limit theorems are the necessary analytic steps.

## Relationship to prior work

Zamparo's 2022 general renewal-reward treatment establishes additive-functional laws of large numbers and a finite-second-reward-moment central limit theorem, including polynomial Brownian observables under suitable reset moments. Thus the \(\alpha>4\) Gaussian regime is a **specialization of known general machinery**, not claimed independently as a new central limit theorem. Its Section 3.1 does not establish the infinite-variance stable and logarithmic boundary distributions for this quadratic observable. Barkai, Flaquer-Galmés and Méndez (2023) analyze ergodic properties and invariant densities for power-law Brownian resetting rather than the centered quadratic-occupation fluctuation law. Méndez and Flaquer-Galmés (2025) analyze general characteristic-function and moment methods with an explicit focus on half-occupation statistics, but do not state this sharp three-regime quadratic-displacement weak limit. The mathematical contribution here is the explicit physical-observable specialization of the *infinite-variance* stable and logarithmic critical regimes, including normalized constants and treatment of the unfinished excursion. The general heavy-tail and regenerative limit tools themselves are established probability theory, not newly invented tools.

## Limitations

The reset waiting-time law is **exactly** Pareto with lower cutoff one. A different cutoff changes the dimensional normalizations; merely asymptotically Pareto clocks may require slowly varying normalizers. The theorem assumes independent complete resets and no drift or force between resets. It gives weak limits and an almost-sure mean only, not finite-time moment convergence, concentration inequalities, a functional central limit theorem, or claims for \(\alpha\le2\). Gaussianity above the fourth-moment threshold was already implied by general regenerative theorems. Publication priority of the explicit critical and stable quadratic case is not guaranteed: older, differently indexed regular-variation literature could imply this as a special case.

## References

1. M. Zamparo, *Statistical fluctuations under resetting: rigorous results*, arXiv:2207.07521 (first publicly posted 2022-07-15), Sections 1, 3.1, 4; https://arxiv.org/html/2207.07521v2.
2. E. Barkai, R. Flaquer-Galmés, V. Méndez, *Ergodic properties of Brownian motion under stochastic resetting*, arXiv:2306.13621 (first posted 2023-06-23); https://arxiv.org/abs/2306.13621.
3. V. Méndez and R. Flaquer-Galmés, *Statistical properties of stochastic functionals under general resetting*, arXiv:2507.05955 (2025), Sections III–V; https://arxiv.org/html/2507.05955.
4. F. den Hollander, S. N. Majumdar, J. M. Meylahn, H. Touchette, *Properties of additive functionals of Brownian motion with resetting*, arXiv:1801.09909 (2018); https://arxiv.org/abs/1801.09909.
5. Classical Brownian Karhunen–Loève expansion, Breiman product-tail theorem, stable domain-of-attraction theory, and renewal-reward/random-index limit theorems are invoked in their standard forms.
