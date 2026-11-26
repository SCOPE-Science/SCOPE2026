# Exact two-turning-point kurtosis law for a critically damped oscillator driven by resetting walls

## Finding
Consider a unit-mass critically damped oscillator between two independent diffusing walls, with dimensionless equations
\[
\dot q=v,\qquad \dot v=-q-2v+\frac{Z_1+Z_2}{2}.
\]
Each wall has Brownian diffusivity \(D>0\) between independent rate-\(r>0\) Poisson resets to zero: \(dZ_i=\sqrt{2D}\,dW_i\) away from jumps. There is a unique stationary law with moments through order four. Its velocity variance and *excess* kurtosis satisfy
\[
\operatorname{Var}(v)=\frac{D}{2(r+1)^2},\qquad
K(r)=\frac{3B(r)}{8r(r+2)^3(r+3)^4},
\]
where
\[
B(r)=105r^7+838r^6+2603r^5+3942r^4+2995r^3+1230r^2+729r+486.
\]
The variance decreases strictly with reset rate. In contrast, \(K\) has **exactly two** positive critical rates: a strict local minimum at \(r_-=0.593772375820\ldots\) with \(K(r_-)=0.586071657410\ldots\), followed by a strict local maximum at \(r_+=6.484200994476\ldots\) with \(K(r_+)=1.762266343988\ldots\). It decreases on \((0,r_-)\), increases on \((r_-,r_+)\), and decreases on \((r_+,\infty)\). Its limiting laws are
\[
K(r)\sim\frac{9}{32r}\quad(r\downarrow0),\qquad K(r)\sim\frac{315}{8r}\quad(r\to\infty).
\]
The existence of at least two such turning points persists under every sufficiently small perturbation of the positive oscillator damping coefficient away from its critically damped value \(2\), with the other stated parameters fixed.

## Assumptions and scope
The equation is dimensionless, with natural oscillator frequency \(1\), total stiffness \(1\), and critical viscous damping \(2\). The two walls have equal positive diffusivities and equal positive reset rates, and are independent of one another and of the oscillator's initial condition. The oscillator itself never resets. There is no additional thermal noise. The stationary velocity has zero mean. The excess kurtosis is \(\mathbb E[v^4]/\mathbb E[v^2]^2-3\), not the uncentered fourth-moment ratio. The exact number and locations of critical rates are asserted for critical damping; nearby damping is asserted to retain *at least* two turning points, without an exact count.

The model is the one-oscillator two-wall reduction of the resetting-wall forcing introduced by Sarkar and Roy (2023); unlike a thermally driven oscillator, the forcing paths are not jointly Gaussian after averaging over reset clocks. The result concerns the instantaneous stationary velocity, not time-averaged energy currents or thermodynamic-limit chain profiles.

## Proof
**1. Stationary construction.** Each reset-Brownian wall has a unique stationary realization from a two-sided rate-\(r\) Poisson clock and independent Brownian increments. Its law is centered, with finite moments of every order. The deterministic oscillator impulse response is exponentially integrable: the characteristic polynomial is \((s+1)^2\). Convolution from the infinite past with the two stationary wall forces therefore gives a unique stationary oscillator state with finite fourth moments.

**2. One-wall moment recursion.** It suffices to solve the normalized one-wall system
\[
\dot x=u,\quad\dot u=-x-2u+z,
\]
where \(z\) is Brownian with diffusivity \(1\) between rate-\(r\) resets to zero. Define \(M_{abc}=\mathbb E[x^a u^b z^c]\) for nonnegative integers \(a,b,c\). The stationary generator applied to the indicated monomial gives the *exact* recurrence
\[
\begin{aligned}
0={}&aM_{a-1,b+1,c}-bM_{a+1,b-1,c}-2bM_{a,b,c}\\
&+bM_{a,b-1,c+1}+c(c-1)M_{a,b,c-2}
-r\mathbf1_{\{c>0\}}M_{a,b,c}.
\end{aligned}
\]
Terms with zero prefactors are omitted. Set \(M_{000}=1\). Solve the finite linear systems at total degrees one through four, in increasing degree; diffusion supplies only known lower-degree moments. The homogeneous coefficient matrices at degrees two and four have determinants respectively \(8r(r+1)^2\) and \(-1024r(r+1)^2(r+2)^3(r+3)^4\), so the solutions are unique for every \(r>0\). Their needed components are
\[
\mathbb E[u^2]=\frac{1}{(r+1)^2},\qquad
\mathbb E[u^4]=\frac{3A(r)}{4r(r+1)^3(r+2)^3(r+3)^4},
\]
with
\[
A(r)=4r^7+173r^6+1217r^5+3722r^4+6112r^3+5739r^2+2835r+486.
\]
Each identity can be checked by substitution of the exact full degree-four solution into the displayed recurrence; the included stand-alone checker performs this symbolic elimination and comparison.

**3. Two independent walls.** Linearity and uniqueness give \(v=(u_1+u_2)/2\), for two independent copies of the one-wall stationary response, rescaled by \(\sqrt D\). Thus
\[
\mathbb E[v^2]=\frac D2\mathbb E[u^2],\qquad
\mathbb E[v^4]=\frac{D^2}{16}\left(2\mathbb E[u^4]+6\mathbb E[u^2]^2\right).
\]
Substitution and elementary factorization yield the claimed exact rational \(K(r)\). Every coefficient of \(B\) is strictly positive, establishing \(K(r)>0\) throughout the domain.

**4. Exactly two critical rates.** Differentiate and factor:
\[
K'(r)=-\frac{3P(r)}{8r^2(r+2)^4(r+3)^5},
\]
where
\[
\begin{aligned}
P(r)={}&105r^9+311r^8-2675r^7-17181r^6-39613r^5\\
&-42611r^4-16077r^3+8901r^2+10692r+2916.
\end{aligned}
\]
The descending coefficient sequence of \(P\) changes sign exactly twice. Descartes' rule bounds the number of positive roots counted with multiplicity by two. Direct exact-rational evaluation gives \(P(1/4)>0\), \(P(2)=-3326712<0\), and \(P(10)=87766512936>0\). The intermediate-value theorem produces one root in \((1/4,2)\) and a second in \((2,10)\); hence there are exactly two, each simple. Since \(P(0)>0\), the signs of \(K'\) are negative, positive, negative on the successive intervals. The numerical values stated above are approximations to these uniquely characterized algebraic roots. The limiting laws follow directly by comparing the leading and constant coefficients of \(B\).

**5. Persistence under nearby damping.** Replace \(-2v\) with \(-\delta v\), for \(\delta>0\) near \(2\). The oscillator remains linearly stable, and every finite stationary moment is a smooth function of \((r,\delta)\). At \(\delta=2\), the derivative of excess kurtosis with respect to \(r\) is strictly negative at \(r=1/4\), strictly positive at \(r=2\), and strictly negative at \(r=10\). Continuity preserves these three signs for all \(\delta\) sufficiently close to \(2\), giving at least one local minimum and one local maximum by compactness and elementary calculus. No exact two-root classification away from \(\delta=2\) is claimed.

## Verification
Run `python verify_kurtosis.py` with SymPy and NumPy installed. The program independently constructs and solves homogeneous moment matrices for degrees one through four, checks the two determinants, verifies the exact second and fourth moments, factors the two-wall kurtosis and its derivative, checks both asymptotic limits, and establishes the two-root count by Descartes and exact signs. For an independent stochastic check it propagates the *conditional Gaussian covariance* between Poisson reset events using the exact linear flow, sampling the random variances rather than using the fourth-moment recurrence. The saved `verification_output.txt` records the passing results. The stochastic estimates are finite-sample consistency tests, never the proof of exact formulas or the root count.

## Relationship to prior work
Sarkar and Roy, *Stationary state of harmonic chains driven by boundary resetting* (first arXiv public release 2023-07-12, arXiv:2307.06127), introduce the independent Brownian resetting-wall reservoirs. They compute stationary second-order velocity correlations and numerically measure finite-size kurtosis and its approximately inverse-size decay. They do not derive the exact one-oscillator critical-damping fourth-moment formula or the two-turning-point reset-rate phase structure established here. Their numerical observation of non-Gaussianity is not claimed as new.

The earlier active-reservoir harmonic-chain studies of Santra and Basu (arXiv:2201.00796) and Sarkar, Santra, and Basu (arXiv:2210.09035) treat different boundary-force laws (including run-and-tumble, active Brownian, and active Ornstein–Uhlenbeck forcing); their second-order and transport formulas alone do not determine this fourth-order reset-Brownian invariant. Previous general results for linear systems driven by Brownian resetting reservoirs establish fourth-cumulant positivity, which this result does not re-claim; positivity alone cannot imply the **two exact extrema and their order**. The complete adjacent-source priority question remains open to independent scholarly checking.

## Limitations
The exact global turning-point count is restricted to a critically damped oscillator with two identically distributed *independent* Brownian walls and zero extra thermal forcing. The nearby-damping result is only an existence statement. No exact finite-chain \(N\ge2\) kurtosis phase diagram, energy-current distribution, or universal statement for arbitrary boundary noises is proved. Numerical critical rates are approximations to uniquely defined polynomial roots, not additional exact formulas. No independent audit or external verification has occurred.

## References
Sarkar, R., and Roy, P., *Stationary state of harmonic chains driven by boundary resetting*, arXiv:2307.06127 (first version 2023-07-12), https://arxiv.org/html/2307.06127v3 .

Santra, I., and Basu, U., *Activity driven transport in harmonic chains*, arXiv:2201.00796 (2022), https://arxiv.org/abs/2201.00796 .

Sarkar, R., Santra, I., and Basu, U., *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035 (2022), https://arxiv.org/abs/2210.09035 .
