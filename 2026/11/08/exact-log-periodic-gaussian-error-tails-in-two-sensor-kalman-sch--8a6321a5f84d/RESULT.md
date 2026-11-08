# Exact log-periodic Gaussian-error tails in two-sensor Kalman scheduling

## Finding
Consider two independent scalar unstable Gaussian systems with identical multiplier \(a>1\) and process-noise variance \(q>0\). Each time, an exact sensor measurement is allocated to one of the two coordinates; its selection switches from the previous coordinate with probability \(\varepsilon\in(0,1]\). The stationary estimation-error magnitude and conditional posterior covariance have an explicit common renewal representation. For \(0<\varepsilon<1\), write
\[
B=a^2,\qquad r=1-\varepsilon,\qquad C=\frac{q}{B-1},\qquad \beta=-\frac{\log r}{\log B}.
\]
Let \(T\) denote the trace of the posterior covariance and \(E\) the Euclidean norm of the posterior estimation error. Then
\[
\Pr(T>t)=r^{\lfloor\log_B(1+t/C)\rfloor}\quad(t\ge0),\qquad
\mathbb E T=\begin{cases}\frac{q}{1-rB}&rB<1,\\+\infty&rB\ge1.\end{cases}
\]
For each \(p>0\), \(\mathbb E T^p<\infty\) precisely when \(p<\beta\), and \(\mathbb E E^p<\infty\) precisely when \(p<2\beta\). The variance tail has sharp, unequal power-law envelopes:
\[
\liminf_{t\to\infty}t^\beta\Pr(T>t)=C^\beta,\qquad
\limsup_{t\to\infty}t^\beta\Pr(T>t)=C^\beta/r.
\]
The genuinely Gaussian estimation error also has a *nonconstant logarithmically periodic* power-law amplitude. Uniformly in the phase \(\vartheta=\{\log_B(z^2/C)\}\),
\[
\Pr(E>z)=z^{-2\beta}\bigl(H(\vartheta)+o(1)\bigr)\quad(z\to\infty),
\]
where the strictly positive continuous period-one function is
\[
H(\vartheta)=\frac{C^\beta\varepsilon}{r}
\sum_{j\in\mathbb Z} B^{\beta(\vartheta-j)}
\operatorname{erfc}\!\left(\frac{B^{(\vartheta-j)/2}}{\sqrt2}\right).
\]
Every Fourier coefficient of \(H\) is nonzero. Specifically, for any \(n\in\mathbb Z\), putting \(s_n=\beta-2\pi i n/\log B\),
\[
\widehat H(n)=\frac{C^\beta\varepsilon}{r\log B}\,
\frac{2^{s_n}\Gamma(s_n+\tfrac12)}{\sqrt\pi\,s_n}\ne0.
\]
Thus no constant \(c\) satisfies \(\Pr(E>z)\sim c z^{-2\beta}\).

For a charge \(\lambda>0\) per sensor switch, optimizing the stationary objective \(J(\varepsilon)=\mathbb ET+\lambda\varepsilon\) over the symmetric Markov protocols above gives the unique policy
\[
\varepsilon_*=
\begin{cases}
1,&\lambda\le qB,\\
\frac{B-1+\sqrt{qB/\lambda}}{B},&\lambda>qB.
\end{cases}
\]
The attained minimum is respectively \(q+\lambda\) or \(2\sqrt{q\lambda/B}+(B-1)\lambda/B\). At \(\varepsilon=1\), the sensor alternates deterministically, \(T=q\) almost surely and \(E\) is \(\sqrt q\) times the absolute value of a standard Gaussian, so all its moments exist.

## Assumptions and scope
At integer time \(t\), first predict \(x_t=a x_{t-1}+w_{t-1}\in\mathbb R^2\), where \(w_t\) are independent \(N(0,qI_2)\). Then observe exactly the single coordinate \(x_{t,J_t}\). The sensor allocation \(J_t\in\{1,2\}\) is independent of the process noises, follows the stationary symmetric Markov chain with \(\Pr(J_t\ne J_{t-1})=\varepsilon\), and the estimation rule is the Gaussian conditional-mean estimator. Quantities \(T\) and \(E\) are post-observation, not prior-prediction errors. The result concerns \(a>1\), \(q>0\), \(0<\varepsilon\le1\), and \(\lambda>0\); the Gaussian noise has two independent coordinates. A stationary error law exists even when its moments diverge, because both coordinates are perfectly reset infinitely often. The latent unstable state itself need not have a stationary distribution.

## Proof
**Renewal representation.** Let \(K\ge1\) be the number of consecutive times the current sensor has selected its presently observed coordinate, including the current time. For \(0<\varepsilon<1\), stationarity gives \(\Pr(K=k)=\varepsilon r^{k-1}\), for all integers \(k\ge1\): \(K=k\) means exactly one switch \(k-1\) steps ago and no subsequent switch. The currently observed coordinate has zero posterior error. The other was last observed precisely \(k\) time steps ago, so its accumulated prediction variance is \(q\sum_{j=0}^{k-1}B^j=C(B^k-1)\). Independence of noise and allocation implies the exact joint representation
\[
(T,E)\ \stackrel d=\ \bigl(C(B^K-1),\sqrt{C(B^K-1)}\,|G|\bigr),
\quad G\sim N(0,1),\quad G\perp K.
\]
This representation also proves stationary uniqueness for the error law by coupling: after each coordinate is measured at least once, all initial error information is erased. At \(\varepsilon=1\), \(K=1\) deterministically.

**Exact risk and moment boundary.** For \(t\ge0\), the event \(T>t\) is \(K>\log_B(1+t/C)\); the geometric survival function gives the stated floor expression. Since \(T\) grows proportionally to \(B^K\), \(\sum_{k\ge1}\varepsilon r^{k-1}T_k^p\) converges exactly when \(rB^p<1\). Independently multiplying by the \(p\)-th absolute Gaussian moment gives the error threshold. Summing the geometric series,
\[
\mathbb ET=C\left(\frac{\varepsilon B}{1-rB}-1\right)
=\frac q{1-rB},\quad rB<1.
\]
Writing \(u=\log_B(1+t/C)\), \(r^{\lfloor u\rfloor}=B^{-\beta u}B^{\beta\{u\}}\); the phase ranges over every value in \([0,1)\), proving the exact lower and upper envelopes.

**Gaussian-error periodic tail.** Set \(z^2/C=B^{N+\vartheta}\) with \(N=\lfloor\log_B(z^2/C)\rfloor\to\infty\) and \(0\le\vartheta<1\). Conditional on \(K=k\), \(\Pr(E>z\mid K=k)=\operatorname{erfc}(z/\sqrt{2C(B^k-1)})\). Substitute \(k=N+j\) and multiply by \(z^{2\beta}\). The resulting summands are
\[
\frac{C^\beta\varepsilon}{r}
B^{\beta(\vartheta-j)}
\operatorname{erfc}\!\left(
\frac{B^{(\vartheta-j)/2}}{\sqrt{2(1-B^{-(N+j)})}}
\right),\quad j\ge1-N.
\]
For fixed \(j\) these converge uniformly in the phase to the summands defining \(H\). For \(j\to+\infty\), the terms are bounded by a geometric sequence \(O(r^j)\); for \(j\to-\infty\), the standard complementary-Gaussian bound \(\operatorname{erfc}(x)\le e^{-x^2}\) dominates the exponential prefactor by a superexponentially decaying sequence. The same majorants are uniform in \(N\) and \(\vartheta\), so dominated convergence for the two tails proves the uniform asymptotic. Translation of the sum's index proves period one and absolute uniform convergence establishes continuity and positivity.

**Nonconstant amplitude.** Write \(f(y)=B^{\beta y}\Pr(G^2>B^y)\). Then \(H(\vartheta)=C^\beta\varepsilon r^{-1}\sum_{j\in\mathbb Z}f(\vartheta-j)\). Periodization and \(u=B^y\) give
\[
\widehat H(n)=\frac{C^\beta\varepsilon}{r\log B}\int_0^\infty u^{s_n-1}\Pr(G^2>u)\,du.
\]
Integration by parts (\(\Re s_n=\beta>0\)) transforms the integral into \(\mathbb E(G^2)^{s_n}/s_n\), and the Gaussian-gamma moment is \(2^{s_n}\Gamma(s_n+1/2)/\sqrt\pi\). The gamma function has no zeros and \(s_n\ne0\), so every Fourier coefficient is nonzero. In particular \(\widehat H(1)\ne0\), proving a nontrivial oscillation and excluding a constant-tail asymptotic.

**Switching-price optimum.** For \(0<\varepsilon\le1\), finiteness of the mean requires \(\varepsilon>1-1/B\). On this interval \(J(\varepsilon)=q/(B\varepsilon-(B-1))+\lambda\varepsilon\), which is strictly convex: \(J''(\varepsilon)=2qB^2/(B\varepsilon-(B-1))^3>0\). Its unique unconstrained critical point obeys \(B\varepsilon-(B-1)=\sqrt{qB/\lambda}\). This point lies below or at \(1\) exactly when \(\lambda\ge qB\). Otherwise the unique constrained minimum is \(1\). Substitution yields the claimed optimal values. No global claim is made outside symmetric Markov allocations.

## Verification
An independent standalone script `check.py` uses exact fractions to verify Markov-run probabilities and the truncated-expectation remainder identity for many parameters; it separately sums Gaussian-mixture tails, checks the phase asymptotic, numerically integrates the first Fourier coefficient and checks the switching-cost optimum against a dense independent grid. Execute `python check.py` with Python 3 and `mpmath` installed. The accompanying `check_output.txt` records the actual execution. These finite and numerical checks test formulas, not the infinite asymptotics, uniformity, uniqueness or nonvanishing of gamma, which are proved above.

## Relationship to prior work
Marelli, Sui, Rohr and Fu (2018, arXiv:1806.08098) study random measurement equations and multichannel sensor-scheduling stability. Mo and Sinopoli (2012) establish general covariance-tail decay rates and criticality under Gilbert–Elliott dropouts. Pezzutto, Schenato and Dey (2019) study actual error heavy tails, proving a pure power-law asymptotic under non-arithmetic assumptions; they specifically describe the arithmetic exact-reset case as having difficult, unresolved coefficient calculations (their Section 5, Remarks 2 and 3). The present special two-coordinate, zero-measurement-noise model has a scalar exact-reset geometric-age reduction: its power exponents and mean-risk threshold are consistent with that prior theory. The assessed additional result is the explicit, provably **nonconstant** Gaussian-error periodic function together with *all* its Fourier coefficients, in the sensor-switching design setting, plus the exact optimal switching-price frontier within the stated policy class. The calculation does not establish previously unknown general heavy-tail exponents or general sensor-scheduling stability theory.

## Limitations
Exact measurements, independent identical unstable modes, identical process-noise variance, two coordinates, and symmetric time-homogeneous Markov selection are essential assumptions. The switching-price optimum does not range over adaptive, asymmetric or history-dependent policies. The oscillation amplitude can be very small and may be numerically difficult to observe. More generally, special arithmetic examples can have explicit multiplicative oscillations without implying the same phenomenon for non-arithmetic measurement gains. No independent scientific audit has been performed.

## References
- D. Marelli, T. Sui, E. Rohr, M. Fu, “Stability of Kalman Filtering with a Random Measurement Equation: Application to Sensor Scheduling with Intermittent Observations,” arXiv:1806.08098, first submitted 2018-06-21, https://arxiv.org/abs/1806.08098.
- M. Pezzutto, L. Schenato, S. Dey, “Heavy-tails in Kalman filtering with packet losses,” *European Journal of Control* 50 (2019), 62–71, https://doi.org/10.1016/j.ejcon.2019.05.003; lawful full text https://mural.maynoothuniversity.ie/id/eprint/16360/1/out.pdf.
- Y. Mo, B. Sinopoli, “Kalman Filtering With Intermittent Observations: Tail Distribution and Critical Value,” *IEEE Transactions on Automatic Control* 57 (2012), 677–689, https://doi.org/10.1109/TAC.2011.2166309.
- L. Calle, S. D. Bopardikar, “Probabilistic Performance Bounds for Randomized Sensor Selection in Kalman Filtering,” arXiv:2103.11182, https://arxiv.org/abs/2103.11182.
