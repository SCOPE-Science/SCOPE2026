# A sharp three-regime law for dispersal and heterogeneous patch volatility

## Finding
Consider two environmentally forced population deviations with symmetric dispersal. The stationary variance at one patch has a **complete global three-regime classification** as dispersal increases: it strictly decreases, strictly increases, or decreases to one unique interior minimum and then increases. The classification is determined solely by the environmental noise covariance, not by the local recovery rate.

Let the local return rate be \(a>0\), symmetric migration rate be \(m\geq0\), and covariance matrix of environmental Brownian increments be
\[
\Sigma=\begin{pmatrix}Q&T\\T&R\end{pmatrix},\qquad Q,R>0,\quad |T|\leq\sqrt{QR}.
\]
Write \(V_1(m)\) for the stationary variance of the first patch's population deviation. Then
\[
V_1(m)=\frac{Q+R+2T}{8a}+\frac{Q+R-2T}{8(a+2m)}+\frac{Q-R}{4(a+m)}.
\tag{1}
\]
The complete classification is:

1. If \(Q\geq R\), then \(V_1\) strictly decreases for every finite increase in \(m\), except that \(Q=R=T\) gives a constant variance.
2. If \(Q<R\), set \(\Delta=R-Q>0\), \(L=Q+R-2T>0\), and \(h=\sqrt{L/\Delta}\). For \(h\leq1\), \(V_1\) strictly increases; for \(h\geq2\), it strictly decreases. For \(1<h<2\), it strictly decreases up to the **unique global minimum**
\[
\boxed{m_*=a\frac{h-1}{2-h}}
\]
and strictly increases thereafter. The three cases are equivalent, respectively, to \(T\geq Q\), to \(3R+2T\leq5Q\), and to \(T<Q\) together with \(3R+2T>5Q\).

In the interior-minimum regime, increasing dispersal eventually raises the patch's variance above its *isolated* variance precisely when \(R+2T>3Q\). Then the unique positive crossing rate is
\[
m_{\rm cross}=\frac{2a(Q-T)}{R+2T-3Q}.
\tag{2}
\]
When \(R+2T\leq3Q\), the interior minimum still exists, but every finite dispersal level has lower variance than isolation. In particular, for independent environmental noises \(T=0\) at the less noisy patch \(Q<R\), an interior optimum exists **exactly when** \(R/Q>5/3\), whereas variance eventually exceeds isolation **exactly when** \(R/Q>3\).

For every admissible parameter set, the stationary variance of total abundance deviation is independent of dispersal:
\[
\operatorname{Var}(X_1+X_2)=\frac{Q+R+2T}{2a},
\]
while cross-patch covariance strictly increases with dispersal unless the environmental drivers are perfectly identical. These two identities explain why changes in local variance need not match changes in aggregate variance.

## Assumptions and scope
Let \(B(t)=(B_1(t),B_2(t))\) be a centered two-dimensional Brownian process with \(d\langle B_1\rangle_t=Q\,dt\), \(d\langle B_2\rangle_t=R\,dt\), and \(d\langle B_1,B_2\rangle_t=T\,dt\). Its covariance matrix is positive semidefinite, so \(|T|\leq\sqrt{QR}\). Consider the Itô linear system for real-valued fluctuations
\[
\begin{aligned}
dX_1&=[-aX_1+m(X_2-X_1)]\,dt+dB_1,\\
dX_2&=[-aX_2+m(X_1-X_2)]\,dt+dB_2.
\end{aligned}
\tag{3}
\]
Both local recovery rates are the same, dispersal is symmetric, and additive noise intensities are allowed to differ and to be spatially correlated. Every \(a>0\), \(m\geq0\), \(Q,R>0\), and \(|T|\leq\sqrt{QR}\) is covered, including singular forcing. The deterministic drift eigenvalues are \(-a\) and \(-(a+2m)\), so (3) has a unique invariant centered Gaussian law and finite stationary second moments. The word *population* denotes linearized deviations around an ecological reference state; negative deviations are allowed, and no positivity or extinction statement is implied for the original nonlinear abundances.

## Proof
Define the sum and difference modes \(S=X_1+X_2\) and \(D=X_1-X_2\). Equation (3) gives two stable scalar equations with correlated drivers:
\[
dS=-aS\,dt+dB_1+dB_2,\qquad dD=-(a+2m)D\,dt+dB_1-dB_2.
\]
The three noise quadratic variations are \(L_S=Q+R+2T\), \(L_D=Q+R-2T\), and \(L_{SD}=Q-R\). Stationary Itô moment identities (equivalently, integrating the stochastic convolutions over the infinite past) give
\[
\operatorname{Var}(S)=\frac{L_S}{2a},\quad
\operatorname{Var}(D)=\frac{L_D}{2(a+2m)},\quad
\operatorname{Cov}(S,D)=\frac{Q-R}{2(a+m)}.
\tag{4}
\]
Since \(X_1=(S+D)/2\), equations (4) prove (1). Similarly, \(X_2=(S-D)/2\), yielding
\[
\operatorname{Var}(X_2)=\frac{L_S}{8a}+\frac{L_D}{8(a+2m)}-\frac{Q-R}{4(a+m)},\qquad
\operatorname{Cov}(X_1,X_2)=\frac{L_S}{8a}-\frac{L_D}{8(a+2m)}.
\tag{5}
\]
The sum-variance identity follows from the first part of (4); differentiating the covariance in (5) gives \(L_D/[4(a+2m)^2]\geq0\). Equality for all dispersal rates requires \(L_D=0\), which under the positive-semidefinite condition forces \(Q=R=T\).

Differentiating (1) produces the exact derivative factorization
\[
4V_1'(m)=\frac{R-Q}{(a+m)^2}-\frac{Q+R-2T}{(a+2m)^2}.
\tag{6}
\]
The second numerator \(L_D\) is nonnegative. If \(Q\geq R\), both terms on the right are nonpositive, and at least one is strictly negative unless \(Q=R=T\). This proves case 1.

For \(Q<R\), positive semidefiniteness implies \(L_D>0\). Divide (6) by \(\Delta/(a+2m)^2>0\). The sign is the sign of
\[
\left(\frac{a+2m}{a+m}\right)^2-h^2.
\tag{7}
\]
The ratio \((a+2m)/(a+m)\) grows strictly from \(1\) at \(m=0\) to \(2\) as \(m\to\infty\), never attaining \(2\) at finite \(m\). Consequently \(h\leq1\) gives strict increase on \([0,\infty)\) (possibly with derivative zero only at the origin); \(h\geq2\) gives strict decrease; and \(1<h<2\) gives exactly one change from negative to positive derivative. Solving the unique equality in (7) gives \(m_*\). The identities
\[
L_D-\Delta=2(Q-T),\qquad L_D-4\Delta=5Q-3R-2T
\]
prove the stated parameter tests, including all boundary cases.

Finally, direct subtraction of the isolated variance \(V_1(0)=Q/(2a)\) from (1) yields
\[
V_1(m)-V_1(0)=\frac{m\,[2a(T-Q)+(R+2T-3Q)m]}{4a(a+m)(a+2m)}.
\tag{8}
\]
For an interior minimum, \(T<Q\), so the initial slope in (8) is negative. Its numerator has a second positive zero precisely when \(R+2T>3Q\), and solving for this zero gives (2). If the latter inequality fails, the difference remains negative at every finite positive dispersal rate. Setting \(T=0\) reduces the interior-minimum condition to \(3R>5Q\) and the eventual-baseline-crossing condition to \(R>3Q\). All classifications are sharp.

## Verification
The included standalone `verify.py` uses symbolic algebra to solve the full stationary Lyapunov equation and compare its entries with (1), (4), and (5). It also verifies the derivative, the baseline-crossing factorization, the high-dispersal limit, and independent exact-rational stationary equations for positive-semidefinite environmental covariance matrices constructed from integer Brownian-loading vectors. The final extracted package passed 55,338 assertions.

For an exact example, choose \(a=1\), \(Q=1\), \(R=4\), and \(T=0\). Then \(h=\sqrt{5/3}\) and the optimal finite dispersal rate is \(m_*=(\sqrt{5/3}-1)/(2-\sqrt{5/3})\approx0.41042619\). The variance starts at \(1/2\), reaches approximately \(0.43649167\), returns exactly to \(1/2\) at \(m=2\), and tends to \(5/8\) as dispersal grows without bound. Replacing \(T=0\) by \(T=3/2\) while keeping \(Q=1\), \(R=4\) makes the variance strictly increasing instead, even though the local drift rates are unchanged. Both covariance matrices are positive semidefinite.

## Relationship to prior work
Abbott (2011) analyzes synchrony and dispersal-induced stability using an autoregressive framework with equal environmental shock variance across patches and a common spatial correlation. Wang, Haegeman, and Loreau (2015) provide the closest continuous-time population-fluctuation model and stationary Lyapunov equation; their displayed environmental covariance assumes a common marginal variance at every patch. In their equal-variance specialization, the local stationary variance is monotone, and no unequal-noise three-regime classification follows by merely adjusting their spatial correlation. The present theorem changes the environmental marginal variances while retaining equal local recovery and symmetric dispersal; it resolves the resulting exact low-variance-patch switching thresholds and unique optimal finite rate. The invariant total-variance identity and the general Lyapunov technique are not claimed as new methods. The 2015 article's supplementary appendices were listed but not fully accessible for examination, so historical priority remains provisional; an equivalent treatment elsewhere in linear stochastic population ecology cannot be ruled out.

## Limitations
The exact theorem concerns the stationary variance of a linear Gaussian fluctuation model, not persistence or extinction probabilities, nonlinear population stability, optimal ecological management in a spatially realistic habitat, colored-noise dynamics, heterogeneous recovery rates, or finite-time transients. The assumption of symmetric dispersal and equal local recovery is essential for the two-mode decomposition. No field parameter estimates are supplied. The stationary variance may be a poor proxy for extinction probability when nonlinearities, demographic discreteness, or absorbing zero boundaries matter. Historical novelty has been checked against accessible literature and mathematical records, not independently certified.

## References
- Abbott, K. C. (2011). *A dispersal-induced paradox: synchrony and stability in stochastic metapopulations*. Ecology Letters 14, 1158–1169. First published 2011-08-04. https://doi.org/10.1111/j.1461-0248.2011.01670.x
- Wang, S., Haegeman, B., and Loreau, M. (2015). *Dispersal and metapopulation stability*. PeerJ 3:e1295. Publicly dated 2015-10-01. https://doi.org/10.7717/peerj.1295 and https://pmc.ncbi.nlm.nih.gov/articles/PMC4636407/
- Keeling, M. J. (2000). *Metapopulation moments: coupling, stochasticity and persistence*. Journal of Animal Ecology 69, 725–736. https://doi.org/10.1046/j.1365-2656.2000.00430.x
