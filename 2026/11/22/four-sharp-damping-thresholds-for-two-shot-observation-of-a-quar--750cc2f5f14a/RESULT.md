# Four sharp damping thresholds for two-shot observation of a quarter-turn oscillator

## Finding

Consider a known, discrete-time, damped planar rotation whose initial state is unknown and whose first coordinate can be measured **exactly twice** at distinct nonnegative integer times. Under independent, equal-variance observation noise, the five standard observability-information criteria have a complete infinite-horizon scheduling classification. Only observation lags one and two can be optimal, and four strictly ordered damping thresholds separate their competing choices.

Set \(A=\rho R_{\pi/4}\), where \(R_{\theta}\) is the standard planar rotation, \(0<\rho<1\), and \(q=\rho^2\). Write \(W_{s,t}\) for the initial-state information Gramian of two scalar readings at integers \(0\le s<t\). We optimize the following criteria over *all* distinct such times: (E) maximize \(\lambda_{\min}(W_{s,t})\); (A) minimize \(\operatorname{tr}(W_{s,t}^{-1})\); (D) maximize \(\det W_{s,t}\); (K) minimize the spectral condition number \(\kappa_2(W_{s,t})\); and (T) maximize \(\operatorname{tr}W_{s,t}\). Singular Gramians have A- and K-objective value \(+\infty\), and E- and D-objective value zero.

There are four thresholds, in strictly increasing order:

\[
\begin{aligned}
q_K&=0.34601433923582586\ldots, &q_K^4-2q_K^3-2q_K^2-2q_K+1&=0,\\
q_E&=0.403031716762685\ldots, &2q_E^3-2q_E^2-2q_E+1&=0,\\
q_A&=\sqrt2-1=0.414213562373095\ldots,\\
q_D&=\tfrac12.
\end{aligned}
\]

Each polynomial equation has **exactly one** solution in \((0,1)\). For each label \(X\in\{K,E,A,D\}\), the **only optimal lag** is \(t-s=1\) for \(0<q<q_X\), and \(t-s=2\) for \(q_X<q<1\); at \(q=q_X\), **both** lags, and no others, are optimal. For E, A and D, the **only optimal initial time** is \(s=0\). For K, **every** nonnegative integer \(s\) yields the same condition number at an optimal lag, and these are the complete optimal schedules. For T, the **unique** optimum is always \((s,t)=(0,1)\), independent of \(q\).

In particular, the K criterion switches first, followed in order by E, A and D, whereas T never switches. These distinct decisions arise for the **same two-measurement budget**, dynamics, noise and unknown initial state.

## Assumptions and scope

The deterministic state evolves as \(x_{k+1}=Ax_k\), with \(x_k\in\mathbb R^2\), \(A=\rho R_{\pi/4}\), \(0<\rho<1\). The unknown initial state is \(x_0\in\mathbb R^2\). Exactly two observations \(Y_j=e_1^{\mathsf T}x_j+\eta_j\) are taken at distinct nonnegative integer times \(j\in\{s,t\}\). The errors are uncorrelated with mean zero and common variance one; if Fisher-information terminology is used, take the errors to be independent standard Gaussian. All dynamical parameters are known. There is no process noise, no finite terminal horizon and no adaptive or repeated-time observation. With error variance \(\sigma^2>0\), replace \(W\) by \(W/\sigma^2\); the optimal timing conclusions are unchanged.

The information matrix is
\[
W_{s,t}=(A^s)^{\mathsf T}e_1e_1^{\mathsf T}A^s+(A^t)^{\mathsf T}e_1e_1^{\mathsf T}A^t.
\]
Its inverse is the ordinary covariance matrix of the generalized least-squares estimate when \(W\) is invertible. We do not optimize sampling *frequencies*, multiple independent sensor channels, continuous observation times, or nonlinear risk.

## Proof

**1. Two-time matrix invariants and a starting-time separation.** Let \(d=t-s\ge1\). Since \(A^s=\rho^sR_{s\pi/4}\) and rotations are orthogonal,
\[
W_{s,s+d}=q^s R_{-s\pi/4}\,W_{0,d}\,R_{s\pi/4}.
\]
The two rows of the initial-state observation matrix are unit directions with squared lengths \(1\) and \(q^d\), and angle \(d\pi/4\). The exact invariants are therefore
\[
\operatorname{tr}W_{0,d}=1+q^d,\qquad
\det W_{0,d}=q^d\sin^2(d\pi/4).
\tag{1}
\]
Multiplying \(W\) by \(q^s\) strictly worsens E, A, D and T when the unshifted Gramian is positive definite (or for T even when it is singular), because \(0<q<1\); thus their global optima start at \(s=0\). K is scale invariant, so its optimal lag is independent of \(s\). Singular lags cannot be optimal for E, A, D or K since lag one has full rank.

**2. Eliminate all but two lags.** If \(d\equiv0\pmod4\), then \(\sin^2(d\pi/4)=0\) and the Gramian is singular. If \(d\) is odd, its squared angle sine is \(1/2\); if \(d\equiv2\pmod4\), it is \(1\). For a fixed nonzero sine-square \(c\), put \(z=q^d\in(0,1)\). An orthogonal change of coordinates makes the information matrix \(e_1e_1^{\mathsf T}+z vv^{\mathsf T}\), where \(v\) is a fixed unit direction with squared determinant \(c>0\). Increasing \(z\) strictly increases its smaller eigenvalue and determinant, and strictly decreases the inverse trace. The strict increase for the smaller eigenvalue follows because its normalized smaller eigenvector cannot be parallel to \(e_1\) or orthogonal to \(v\) for a nonparallel pair with \(0<z<1\); alternatively the explicit eigenvalue formula in step 3 differentiates positively. The determinant is \(cz\) and inverse trace is \((1+z)/(cz)\). For K, the dimensionless normalized determinant
\[
J(z,c)=\frac{\det W}{(\operatorname{tr}W)^2}=\frac{cz}{(1+z)^2}
\]
is strictly increasing on \(0<z<1\), since its derivative is \(c(1-z)/(1+z)^3>0\). In dimension two, \(J=\kappa_2(W)/(1+\kappa_2(W))^2\), which is strictly decreasing with \(\kappa_2(W)\ge1\). The trace \(1+z\) is strictly increasing. Thus within either angular class the **smallest positive lag** is strictly better for every criterion. Those representatives are \(d=1\) and \(d=2\). This comparison also proves no later lag can tie.

**3. Exact two-lag objective comparison.** For lag one, equation (1) gives \(\operatorname{tr}W_{0,1}=1+q\) and \(\det W_{0,1}=q/2\); for lag two, the Gramian is diagonal up to an orthogonal change with eigenvalues \(1\) and \(q^2\). Consequently
\[
\begin{array}{c|cc}
&d=1&d=2\\\hline
\lambda_{\min}&\dfrac{1+q-\sqrt{1+q^2}}2&q^2\\
\operatorname{tr}W^{-1}&\dfrac{2(1+q)}q&\dfrac{1+q^2}{q^2}\\
\det W&q/2&q^2\\
J=\det W/(\operatorname{tr}W)^2&\dfrac{q}{2(1+q)^2}&\dfrac{q^2}{(1+q^2)^2}\\
\operatorname{tr}W&1+q&1+q^2
\end{array}
\tag{2}
\]
The E scores coincide if and only if \(\sqrt{1+q^2}=1+q-2q^2\), whose right-hand side is positive on \((0,1)\). Squaring, and removing the harmless factor \(2q\), yields \(P_E(q)=2q^3-2q^2-2q+1=0\). Since \(P_E'(q)=2(3q+1)(q-1)<0\) on \((0,1)\), with \(P_E(0)>0>P_E(1)\), it has a unique root. For \(q\downarrow0\), lag one has larger smaller eigenvalue, and for \(q\uparrow1\), lag two does, establishing the orientation and the unique E crossover.

The A scores are equal just when \(2q(1+q)=1+q^2\), i.e. \(q^2+2q-1=0\), with the unique positive root \(\sqrt2-1\). For D, \(q/2=q^2\) gives \(q=1/2\). For K, condition-number equality is exactly equality of \(J\) scores, equivalent to
\[
(1+q^2)^2=2q(1+q)^2.
\]
Dividing by \(q^2>0\), setting \(v=q+q^{-1}>2\), and simplifying gives \(v^2-2v-4=0\). The positive root is \(v=1+\sqrt5\), which corresponds to exactly one \(q_K\in(0,1)\), since \(q+q^{-1}\) is strictly decreasing there. Equivalently \(q_K\) solves \(q^4-2q^3-2q^2-2q+1=0\). As \(q\to0\), \(J_1/J_2\to\infty\) and lag one has better conditioning; as \(q\to1\), lag two has better conditioning. Both orientations are therefore as claimed. T always prefers \(1+q>1+q^2\).

**4. Strict separation, endpoints, and completeness.** The K root is in \((34/100,35/100)\), the E root is in \((40/100,41/100)\), the A threshold is in \((41/100,42/100)\), and the D root is \(1/2\). The polynomial signs on these rational interval endpoints (checked by exact arithmetic) and the uniqueness arguments prove the four thresholds are strictly ordered. At each equality, the two candidate lags tie, and Step 2 excludes all others. Step 1 supplies precisely the initial-time qualification, including the entire family of optimal K schedules. All claims hold for every \(q\in(0,1)\) and every integer pair \(0\le s<t\), without a finite enumeration hypothesis.

## Verification

Run `python3 verify.py` with Python 3 standard library from the extracted package. The script checks exact coefficient identities for the E, A and K crossover polynomials, rational brackets of their unique roots, and direct Gramian formulas for multiple \(\rho\), starts and lags. It performs 6970 supplementary finite comparison checks of the five criteria over sampled damping values and lags through 64. The proof, not those finite checks, establishes all positive integer lags, all damping parameters and uniqueness.

## Relationship to prior work

Baran, Szák-Kocsis and Stehlík (2017) discuss the D/A/E/T/K information criteria in experimental design and optimize D criteria for stationary complex Ornstein–Uhlenbeck processes with correlated process observations and unknown trend or covariance parameters. Their experiment is not the deterministic initial-state reconstruction model in this finding, and their published D-optimal lag does not imply the four crossover equations above.

Siami, Olshevsky and Jadbabaie (2018) formulate general controllability/observability Gramian scheduling metrics and derive approximation guarantees for sparse actuator activation. Siami and Jadbabaie (2020) extend sparse sensing/actuation approximation to joint schedules. These do not provide exact single-output, exactly two-observation discrete-time global optimizers or a criterion-ordering phase diagram for the specified rotation.

A previously documented continuous-time two-observation theorem treats worst-direction (E) optimal timing of a damped planar rotation with a continuously variable lag. Its all-positive-real-time optimum is a different feasible-set problem; it does not determine the integer-lag E threshold and does not cover the A/D/K/T disagreement derived here. Related published work on three equally spaced readings of a damped planar mode optimizes a Fisher determinant envelope rather than classifying the present two-reading schedule across five criteria. These comparisons establish different assumptions and logical conclusions, not priority against all possible earlier oscillator-design literature.

## Limitations

The exact laws are specialized to rotation by \(\pi/4\) per discrete step, a scalar first-coordinate sensor, homogeneous exponential decay, and two nonadaptive equal-precision measurements. The condition-number objective does not select an absolute initial time; all shifts of either optimal lag are tied for K. The results do not claim a general solution for other rotation angles, unequal observation noise, unknown dynamics, stochastic process noise, finite deadline, or more samples. The polynomial equations are algebraic consequences of the two-by-two information matrix; the contribution is the motivated, complete, distinct-criterion global scheduling classification. Historical priority remains provisional pending independent literature review.

## References

1. S. Baran, C. Szák-Kocsis, M. Stehlík, *D-optimal designs for complex Ornstein–Uhlenbeck processes*, arXiv:1704.05719v1, April 19, 2017. https://arxiv.org/abs/1704.05719
2. M. Siami, A. Olshevsky, A. Jadbabaie, *Deterministic and Randomized Actuator Scheduling With Guaranteed Performance Bounds*, arXiv:1805.00606v1, May 2, 2018. https://arxiv.org/abs/1805.00606
3. M. Siami, A. Jadbabaie, *A Separation Theorem for Joint Sensor and Actuator Scheduling with Guaranteed Performance Bounds*, arXiv:2005.03143v1, May 6, 2020. https://arxiv.org/abs/2005.03143
4. *Sharp strong-damping observability envelope for three-time oscillator sampling*, public mathematical result. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-strong-damping-observability-envelope-for-three-time-oscil--718ab126a5c2
5. *Horizon-universal spectral majorization for a damped cyclic actuator*, public mathematical result. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-horizon-universal-spectral-majorization-for-a-damped-cyclic-actu--50b398f70222
