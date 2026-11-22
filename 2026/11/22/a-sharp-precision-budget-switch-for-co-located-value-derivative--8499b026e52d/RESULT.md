# A sharp precision-budget switch for co-located value–derivative Wiener quadrature

## Finding

Let \(B\) be standard Brownian motion on \([0,1]\), let \(X(t)=\int_0^t B(u)\,du\), and set \(J=\int_0^1X(t)\,dt\). At a single deterministic site \(z\in[0,1]\), choose nonnegative Gaussian measurement precisions \(p,q\) satisfying \(p+q=P>0\). Observe independently perturbed \(X(z)\) and \(X'(z)=B(z)\), with noise variances \(1/p\) and \(1/q\) respectively; a zero precision deletes that channel. Minimize the Bayes mean-square error \(\mathbb E[(J-\mathbb E[J\mid\text{observations}])^2]\) globally over all sites and precision splits.

Define
\[
 z_B(P)=\frac{P-2+\sqrt{P^2+8P+4}}{3P},\qquad
 V_B(P)=\frac{Pz_B(P)^2(2-z_B(P))^2}{4(1+Pz_B(P))},\qquad
 V_E(P)=\frac{P+1}{3(P+4)}.
\]
There is a **unique** \(P_*\in(8,9)\) satisfying \(V_B(P_*)=V_E(P_*)\), with
\[
P_*=8.578152164906413\ldots,\qquad z_B(P_*)=0.725481854958253\ldots.
\]
For every \(0<P<P_*\), the **unique** optimum is \((z,p,q)=(z_B(P),0,P)\): all precision is allocated to the derivative reading at an interior site. For every \(P>P_*\), the **unique** optimum is
\[
\boxed{(z,p,q)=(1,P-2,2)}.
\]
At \(P=P_*\), precisely these two distinct designs are optimal and no others are. The exact minimum Bayes mean-square error is
\[
\boxed{R_*(P)=\begin{cases}
\frac13-V_B(P),&0<P\le P_*,\\[2pt]
\frac1{P+4},&P\ge P_*.
\end{cases}}
\]
Thus the optimum switches discontinuously from derivative-only interior sensing to mixed endpoint sensing. After the switch, the optimal derivative precision is exactly \(2\), independent of the growing total budget.

## Assumptions and scope

The path begins at \(B(0)=0\); all observations are jointly Gaussian with Brownian motion, have independent centered Gaussian measurement errors, and are obtained at one common, nonadaptive, predetermined time. The total *precision*, not total variance, is \(P\); the observation noise is independent of the process. The estimator may be any square-integrable function of the observations, and Gaussian conditional expectation is optimal. The result covers all real \(P>0\), all \(z\in[0,1]\), both zero-precision boundaries, and the switching equality. The coefficient \(X'(z)=B(z)\) is an ordinary path derivative because integrated Brownian motion is continuously differentiable. This statement concerns a single colocated two-channel site, not two independently located sensors.

## Proof

**1. Exact Gaussian reduction.** The white-noise (Itô) kernels for \(J\), \(X(z)\), and \(B(z)\) are respectively \(f(u)=1-u\), \(g_z(u)=(z-u)_+\), and \(h_z(u)=\mathbf1_{\{u<z\}}\). Consequently \(\operatorname{Var}(J)=1/3\), and with the channel order \((X(z),B(z))\),
\[
K(z)=\begin{pmatrix}z^3/3&z^2/2\\z^2/2&z\end{pmatrix},\qquad
c(z)=\begin{pmatrix}z^2(3-z)/6\\z(2-z)/2\end{pmatrix}.
\]
For fixed positive \(p,q\), Gaussian conditioning gives the variance reduction \(c(z)^\mathsf T[K(z)+\operatorname{diag}(1/p,1/q)]^{-1}c(z)\), with continuous one-channel limiting interpretations. More usefully, the corresponding Bayes error equals
\[
\min_{a,b\in\mathbb R}\Big\{\int_0^1[f(u)-a g_z(u)-b h_z(u)]^2\,du+\frac{a^2}{p}+\frac{b^2}{q}\Big\}.
\]
Minimizing first over \(p,q\ge0\) with \(p+q=P\) uses Cauchy–Schwarz and gives exactly \((|a|+|b|)^2/P\), attained uniquely when \(p:q=|a|:|b|\) if both coefficients are nonzero.

**2. Neither optimal coefficient is negative.** For \(z>0\), if \(a<0\), replace \((a,b)\) by \((0,b+az/2)\). On \([0,z]\), this preserves the mean of the linear approximation, strictly decreases the centered squared error by \(z^3((1-a)^2-1)/12>0\), and does not increase the precision penalty because \(|b+az/2|\le |b|+|a|z/2<|a|+|b|\). Outside \([0,z]\) both approximations are zero. Thus \(a\ge0\). If \(a>0,b<0\), first-order stationarity in this open orthant uses the positive-definite matrix \(K+P^{-1}\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\), whose unique solution has
\[
b=\frac{Pz^3(1-z)+12-2z^2}{Pz^3+4z^2+12z+12}>0,
\]
a contradiction. The case \(a=0,b<0\) is strictly worse than \((0,0)\), since \(f,h_z\ge0\). Therefore \(a,b\ge0\). Moreover, \(b=0,a>0\) is never a minimum: at its coefficient-wise optimum \(a=c_1/(K_{11}+1/P)\), the right derivative when turning on \(b\) is negative, because
\[
c_2(K_{11}+1/P)-c_1(K_{12}+1/P)
=\frac{z[Pz^3(1-z)+2z^2-12z+12]}{12P}>0.
\]
So the derivative channel is always used when \(z>0\).

**3. Conditional coefficient activation.** In the positive quadrant, the penalty is \((a+b)^2/P\). With \(D=Pz^3+4z^2-12z+12>0\), the unconstrained normal equations give
\[
a=\frac{Pz^3-2z^2+12z-12}{D},\qquad
b=\frac{Pz^3(1-z)+2z^2-12z+12}{D}.
\]
The second numerator is strictly positive for \(0<z\le1\). Thus the optimum uses only \(b\) when \(Pz^3\le 2z^2-12z+12\), and both channels otherwise. Define \(P_0(z)=(2z^2-12z+12)/z^3\), strictly decreasing from \(+\infty\) to \(2\). For \(P\le2\), only the derivative channel can be optimal; for \(P>2\), a unique activation site \(z_0(P)\in(0,1)\) satisfies \(P=P_0(z_0)\) and the mixed solution is active precisely for \(z>z_0\).

In the derivative-only region the variance reduction is
\[
V_B(z,P)=\frac{Pz^2(2-z)^2}{4(1+Pz)}.
\]
Its derivative has the sign of \(4-4z+2Pz-3Pz^2\) (for \(0<z<1\)), which has exactly one zero in \((0,1)\), namely \(z_B(P)\). Consequently the derivative-only branch's unrestricted global maximum is \(V_B(P)\).

**4. No mixed interior maximum.** In the mixed-active region the variance reduction is
\[
V_M(z,P)=\frac{z\{Pz^5-3Pz^4+3Pz^3+z^4-12z^3+48z^2-72z+36\}}{3(Pz^3+4z^2-12z+12)}.
\]
Its derivative has the sign of the polynomial
\[
\begin{aligned}
U(z,P)&=P^2z^6(1-z)^2+2Pz^3(3z^4-18z^3+40z^2-36z+12)\\
&\quad+4(z^2-6z+6)(z^4-6z^3+15z^2-18z+6).
\end{aligned}
\]
Indeed \(\partial_zV_M=U/D^2\). To count zeros on \((0,1)\), use \(z=t/(1+t)\). The coefficients of \((1+t)^8U(t/(1+t),P)\), in ascending powers of \(t\), are
\[
144,\ 576,\ 816,\ 24(P+12),\ 12(4P-41),\ 32(P-21),\ P^2+12P-356,\ 2(3P-44),\ 2(P-4).
\]
For \(0<P\le4\) the nonzero coefficients have at most one sign change; for \(4<P<P_c\) they have at most two, where
\[
z_c=\frac{6-\sqrt6}{5},\qquad P_c=P_0(z_c)=12.531972647421808\ldots.
\]
Descartes' rule consequently bounds the number of positive zeros, with multiplicity, by one and two respectively.

At the activation site \(z=z_0(P)\), direct substitution gives
\[
U(z_0,P)=4(z_0-2)^2(z_0^2-6z_0+6)(5z_0^2-12z_0+6).
\]
Also \(U(0,P)=144\) and \(U(1,P)=2(P-4)\). If \(2<P\le4\), these signs plus the one-zero bound imply \(U<0\) throughout the mixed interior, so \(V_M\) decreases from its activation boundary. If \(4<P<P_c\), then \(z_0>z_c\) and the signs are \(+,-,+\) at \(0,z_0,1\). The two-zero bound forces precisely one mixed-active zero, crossing from negative to positive; it is a local **minimum**, not a maximum.

For completeness, at \(P=P_c\), \(U(z_c,P_c)=\partial_zU(z_c,P_c)=0\), so \(z_c\) is a double zero. The two-sign-change bound, together with \(U(0,P_c)>0\) and \(U(1,P_c)>0\), gives \(U(z,P_c)\ge0\) throughout \([0,1]\). For larger \(P\), set \(w=P-P_0(z)\ge0\) in the mixed-active region. An exact expansion is
\[
\begin{aligned}
U(z,P_0(z)+w)&=z^6(1-z)^2w^2\\
&\quad+2z^3(z-2)(5z^3-24z^2+30z-12)w\\
&\quad+4(z-2)^2(z^2-6z+6)(5z^2-12z+6).
\end{aligned}
\]
The middle coefficient is positive for \(0<z\le1\): putting \(r=1-z\) gives \(5z^3-24z^2+30z-12=-5r^3-9r^2+3r-1<0\). For \(z\le z_c\) the constant term is nonnegative, so \(U\ge0\). For \(z\ge z_c\), \(P_0(z)\le P_c\); the displayed expansion shows \(U\) is increasing in \(P\) above \(P_0(z)\), whence \(U(z,P)\ge U(z,P_c)\ge0\) for \(P\ge P_c\). Thus no mixed interior maximizer exists for any \(P>0\): every mixed-active branch has its maximum at its activation boundary (where it equals the pure-derivative branch) or at \(z=1\).

**5. Comparison and uniqueness.** At \(z=1\) the mixed coefficients are \(a=(P-2)/(P+4)\) and \(b=2/(P+4)\), so when \(P>2\) the unique optimal allocation at that site is \((p,q)=(P-2,2)\), with variance reduction \(V_E(P)\) and Bayes error \(1/(P+4)\). The preceding steps reduce the complete global problem to comparing \(V_B(P)\) and \(V_E(P)\) for \(P>2\).

The stationarity relation for the derivative-only optimizer is
\[
P=\frac{4(1-z_B)}{z_B(3z_B-2)},\qquad 2/3<z_B<1,
\]
which is strictly decreasing in \(z_B\). By the envelope derivative,
\[
V_B'(P)=\frac{z_B^2(3z_B-2)^2}{4},\qquad
V_E'(P)=\frac{z_B^2(3z_B-2)^2}{16(3z_B^2-3z_B+1)^2}.
\]
Their derivative difference changes sign exactly once as \(z_B\) passes \((3+\sqrt3)/6\), from positive to negative as \(P\) increases. At \(P=2\), the derivative-only trial \(z=3/4\) gives variance reduction \(45/256>1/6=V_E(2)\); as \(P\to\infty\), \(V_B(P)\to8/27<1/3=\lim V_E(P)\). Hence the curves cross precisely once at \(P_*\). Strictness of all branch arguments proves unique designs away from the crossing and exactly two at equality, establishing the theorem.

## Verification

Run `python check.py` with Python 3, SymPy, NumPy and SciPy. The script checks all symbolic identities used in Steps 3–5, the polynomial transform and shift, the double-root certificate, the endpoint and derivative-only allocations, and a numerical bracket for the unique crossing. It independently integrates the five relevant white-noise kernel products at 21 sites and tests 131,599 additional feasible design competitors by direct Gaussian covariance inversion. Its latest execution printed `PASS`. These finite comparisons are diagnostics only: globality and uniqueness depend on the exact sign/Descartes argument above, not on the grid.

## Relationship to prior work

Wu, Aoi and Pillow (arXiv:1704.00060, first public 31 March 2017) develop Gaussian-process quadrature using values and derivatives, including joint covariance conditioning and active location selection; their Sections 3 and 5.2 do not provide the integrated-Wiener, freely allocated *two-channel precision* classification here. Prüher and Särkkä (IEEE MLSP 2016, DOI 10.1109/MLSP.2016.7738903) also show how derivative information enters Gaussian-process quadrature, but their published description concerns moment transformations, not the present sharp joint design. Foster, Lyons and Oberhauser (arXiv:1904.06998, 15 April 2019) provide polynomial representations of Brownian paths respecting time integrals; this is distinct from a two-channel measurement-precision allocation. Karvonen, Kanagawa and Särkkä (arXiv:1812.08509, 20 December 2018) study positivity/magnitude of Bayesian quadrature weights under kernel and point-optimality assumptions, rather than two-channel budget phase transitions. These comparisons are about implication and observation model, not keyword absence. A previously established either-instrument, single-noise observation rule for the same integrated-Wiener target optimizes one selected channel, whereas the present high-budget optimum *simultaneously uses both channels*, with a new exact switching rule. A stationary Matérn value/derivative allocation model has a different covariance, target and phase classification. No universal claim of publication priority is made.

## Limitations

The result is exact only for unit-duration, zero-start once-integrated standard Brownian motion, one colocated site, independent Gaussian measurement errors, continuously divisible total precision, squared-error Bayes estimation and known covariance. It does not include separate sites for the two channels, measurement cost overhead, correlated calibration errors, adaptive decisions, non-Gaussian process priors, or other integration targets. The computed decimal digits are approximate; \(P_*\) is defined by an exact uniquely solvable equation. Independent mathematical validation and exhaustive publication-priority verification have not been performed.

## References

1. A. Wu, M. C. Aoi and J. W. Pillow, *Exploiting gradients and Hessians in Bayesian optimization and Bayesian quadrature*, arXiv:1704.00060 (first submitted 31 March 2017), https://arxiv.org/abs/1704.00060.
2. J. Prüher and S. Särkkä, *On the Use of Gradient Information in Gaussian Process Quadratures*, MLSP (2016), DOI:10.1109/MLSP.2016.7738903.
3. J. Foster, T. Lyons and H. Oberhauser, *An Optimal Polynomial Approximation of Brownian Motion*, arXiv:1904.06998 (15 April 2019), https://arxiv.org/abs/1904.06998.
4. T. Karvonen, M. Kanagawa and S. Särkkä, *On the Positivity and Magnitudes of Bayesian Quadrature Weights*, arXiv:1812.08509 (20 December 2018), https://arxiv.org/abs/1812.08509.
5. X. Xi, F.-X. Briol and M. Girolami, *Bayesian Quadrature for Multiple Related Integrals*, arXiv:1801.04153 (12 January 2018), https://arxiv.org/abs/1801.04153.
