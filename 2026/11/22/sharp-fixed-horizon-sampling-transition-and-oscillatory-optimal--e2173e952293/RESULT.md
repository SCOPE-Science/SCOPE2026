# Sharp fixed-horizon sampling transition and oscillatory optimal-time drift for a damped rotation frame

## Finding

For every \(a,\omega,T>0\), consider three independent scalar observations of the two unknown initial coordinates of the stable planar rotation \(e^{-as}R(\omega s)\), with two observation events prescribed at times \(0\) and \(T\) and the third at a freely chosen \(t\in[0,T]\). An observation at an already prescribed endpoint is an **independent replicate**. Define
\[
\theta=\arctan(\omega/a),\qquad T_c=\theta/\omega.
\]
The determinant of the information Gram matrix has **exactly two optimal placements, \(t=0,T\), when \(0<T\le T_c\)**. For every \(T>T_c\), it has **exactly one optimal placement \(t_*(T)\) in the open interval**, and
\[
0<t_*(T)<\min\{T,\pi/\omega\}.
\]
This is an all-horizon statement: arbitrarily many completed rotations and repeated phase resonances cannot create a second global optimum. The unique interior optimizer is the strict-local-maximum solution in the indicated first-rotation interval of the explicit scalar equation
\[
\sin(2\omega t)-\frac{2a}{\omega}\sin^2(\omega t)
=e^{-2aT}\left[\sin(2\omega(T-t))
+\frac{2a}{\omega}\sin^2(\omega(T-t))\right].
\tag{1}
\]
For fixed \(\eta=a/\omega>0\), put \(\Phi=\omega T\) and \(\theta=\arctan(1/\eta)\). Then as \(T\to\infty\),
\[
\omega t_*(T)=\theta-\frac{e^{-2aT}}2
\left[\sin 2(\Phi-\theta)+2\eta\sin^2(\Phi-\theta)\right]
+O_{\eta}(e^{-4aT}).
\tag{2}
\]
In particular, \(t_*(T)\to T_c\), but there are infinitely many unbounded horizons for which \(t_*(T)<T_c\) and infinitely many for which \(t_*(T)>T_c\). The approach to the limiting optimal time is thus genuinely oscillatory, rather than one-sided.

## Assumptions and scope

Let \(A,B\in\mathbb R\) be unknown deterministic initial-state coordinates. For \(s\ge0\), measure
\[
Y(s)=e^{-as}\big(A\cos(\omega s)+B\sin(\omega s)\big)+\epsilon_s,
\]
where the errors for the three **measurement events** are independent, have mean zero, and have common variance \(\sigma^2>0\). When using a Fisher-information interpretation, additionally assume independent Gaussian errors. Observations at equal physical times are independent replicates; they are not the same random variable measured twice. The design matrix \(H_t\) has rows \(e^{-as}(\cos(\omega s),\sin(\omega s))\) for \(s=0,t,T\), and the information matrix is \(G_t=\sigma^{-2}H_t^{\mathsf T}H_t\). Multiplying \(\det G_t\) by \(\sigma^4\) does not change optimal times. Every nonzero scalar observation vector of the planar rotation yields the same optimal times after a fixed orthogonal change of coordinates and multiplication by its squared norm.

The rates \(a,\omega\), terminal horizon \(T\), sample budget, scalar-output architecture, and noise variance are fixed and known. Only the third observation time varies. Optimization is for the determinant of a two-dimensional information matrix, not for the smallest eigenvalue, correlated process noise, unknown frequency, or an arbitrary schedule with additional freely chosen events. The primary mathematical object is a finite dynamical frame of three semigroup-orbit vectors.

## Proof

**1. Determinant and endpoint equality.** The \(2\times2\) determinant formed by observation rows at \(s_i<s_j\) is \(e^{-a(s_i+s_j)}\sin(\omega(s_j-s_i))\). The Cauchy--Binet identity therefore gives, without a nonsingularity assumption,
\[
\sigma^4\det G_t=e^{-2at}\sin^2(\omega t)
+e^{-2aT}\sin^2(\omega T)
+e^{-2a(t+T)}\sin^2(\omega(T-t)).
\tag{3}
\]
Set \(x=\omega t\), \(\Phi=\omega T\), \(\eta=a/\omega\) and \(q=e^{-2\eta\Phi}\in(0,1)\). Up to the constant \(q\sin^2\Phi\), optimizing (3) is equivalent to optimizing
\[
f(x)=e^{-2\eta x}\big[\sin^2x+q\sin^2(\Phi-x)\big],\qquad 0\le x\le\Phi.
\tag{4}
\]
Both endpoints have exactly the same value \(f(0)=f(\Phi)=q\sin^2\Phi\). This equality reflects independent replication, not time-reversal symmetry of the damped semigroup.

**2. Exactly two critical points in each whole rotation period.** Multiplying \(f'(x)\) by \(e^{2\eta x}\) yields
\[
F(x)=\sin2x-2\eta\sin^2x
-q\big[\sin2(\Phi-x)+2\eta\sin^2(\Phi-x)\big].
\tag{5}
\]
Write \(g(x)=\sin^2x+q\sin^2(\Phi-x)=A-\frac12R\cos(2x-\delta)\), where
\[
A=\frac{1+q}{2},\qquad
R=\sqrt{(1-q)^2+4q\cos^2\Phi}>0,
\]
and choose \(\delta\) with \(R\cos\delta=1+q\cos2\Phi\) and \(R\sin\delta=q\sin2\Phi\). Then
\[
F(x)=R\big[\sin(2x-\delta)+\eta\cos(2x-\delta)\big]-\eta(1+q).
\]
The sinusoid's amplitude is *strictly greater* than the positive constant on the right because
\[
(1+\eta^2)R^2-\eta^2(1+q)^2
=4q\big[\sinh^2(\eta\Phi)+\cos^2\Phi-\eta^2\sin^2\Phi\big]>0.
\tag{6}
\]
Indeed \(\sinh(\eta\Phi)>\eta\Phi\ge\eta|\sin\Phi|\) for every positive \(\eta,\Phi\). Thus \(F\) has exactly two simple zeros, one crossing up and one crossing down, in each interval of length \(\pi\) containing no root at its endpoints. Accordingly \(f\) has at most one strict local maximum in every such interval, with no degenerate critical points. For any interval shorter than \(\pi\), \(f'\) has at most two zeros in its interior.

**3. The sharp short-horizon boundary.** Put \(\theta=\arctan(1/\eta)\in(0,\pi/2)\). For \(0<\Phi\le\theta\), differentiating (4) at the endpoints gives
\[
F(0)=-2q\sin\Phi(\cos\Phi+\eta\sin\Phi)<0,
\qquad F(\Phi)=2\sin\Phi(\cos\Phi-\eta\sin\Phi)\ge0.
\tag{7}
\]
When \(\Phi<\theta\), the sinusoid in Step 2 and these opposite signs force precisely one simple interior zero of \(F\), a local minimum. Consequently both endpoints, and only the endpoints, maximize \(f\). At \(\Phi=\theta\), the endpoint \(x=\Phi\) is stationary and direct differentiation gives \(F'(\Phi)=2(q-1)<0\); immediately to its left \(F>0\), so there remains exactly one interior local minimum and no interior maximum. Both endpoints remain the only global maximizers. This proves the transition including equality.

**4. Every longer horizon has one interior global maximum.** For \(\theta<\Phi<\pi\), equation (7) gives \(F(\Phi)<0\). Therefore \(f(x)>f(\Phi)=f(0)\) at points sufficiently close to \(\Phi\) from the left. A global optimum must lie in the interior. The interval has length less than \(\pi\), so Step 2 shows there is at most one interior local maximum; it is strict and hence uniquely optimal. At \(\Phi=\pi\), formula (4) reduces to \(f(x)=(1+q)e^{-2\eta x}\sin^2x\), with unique maximum \(x=\theta\).

For \(\Phi>\pi\), the identity
\[
f(x+\pi)=e^{-2\eta\pi}f(x)
\tag{8}
\]
holds whenever both arguments are in \([0,\Phi]\). Every point after the first complete rotation is therefore strictly dominated by a point one period earlier unless both values vanish; a positive global maximum must lie in \([0,\pi)\). The test point \(x=\theta\) strictly beats the left endpoint: since \(f(0)\le q\le e^{-2\eta\pi}\),
\[
f(\theta)\ge\frac{e^{-2\eta\theta}}{1+\eta^2}>e^{-2\eta\pi}\ge f(0).
\tag{9}
\]
For the middle strict inequality, \(\log(1+\eta^2)\le\eta<2\eta(\pi-\theta)\); the first inequality follows by differentiating \(\eta-\log(1+\eta^2)\), whose derivative is \((\eta-1)^2/(1+\eta^2)\ge0\). By (8), \(f(\pi)<f(0)\). Hence the global maximum is strictly interior to \((0,\pi)\), and the two-root periodic structure in Step 2 gives a unique local maximum there. This proves the global all-horizon classification and equation (1), which is \(F=0\) in unscaled variables.

**5. Uniform large-horizon expansion and infinitely many crossings.** For fixed \(\eta>0\), the function \(f\) from (4) converges in \(C^2([0,\pi])\) to \(f_0(x)=e^{-2\eta x}\sin^2x\) as \(q=e^{-2\eta\Phi}\to0\), uniformly in the oscillatory phase \(\Phi\). The latter has exactly one global maximum at \(x=\theta\). Its stationarity function \(F_0(x)=\sin2x-2\eta\sin^2x\) satisfies \(F_0(\theta)=0\) and \(F_0'(\theta)=-2\). The implicit-function estimate for the unique maximizing root, uniform in \(\Phi\), is therefore
\[
x_*=\theta-\frac q2\big[\sin2(\Phi-\theta)+2\eta\sin^2(\Phi-\theta)\big]+O_{\eta}(q^2),
\]
which is (2). The bracket is positive at sufficiently small positive phases \(r\), but negative at phases \(\pi-r\) with the same sufficiently small \(r>0\), because it equals \(2r+O_{\eta}(r^2)\) and \(-2r+O_{\eta}(r^2)\), respectively. Choosing arbitrarily large horizons \(\Phi=\theta+n\pi+r\) and \(\Phi=\theta+(n+1)\pi-r\) for integers \(n\to\infty\), the uniform quadratic remainder is smaller than the signed first-order term. This proves infinitely many optimal times on each side of \(T_c\).

## Verification

The standalone Python 3 standard-library script `verify.py` independently computes the information objective, derivative roots, and dense-grid maxima over 84 combinations of damping and horizons including the equality threshold, many rotation periods and large damping. It also checks the long-horizon oscillatory expansion. Running `python3 verify.py` reports `PINNED_ROTATION_FRAME_DIAGNOSTIC_OK 382`. Those finite calculations are diagnostic; all real-parameter quantifiers and uniqueness statements are established by Steps 1--5.

For illustration, at \(a=\omega=1\) the critical horizon is \(T_c=\pi/4\). At \(T=1\), the unique optimal free time is approximately \(0.7409827186\), while at \(T=0.5\) only repeating the first or last observation is optimal. At \(T=4\), the optimal time is approximately \(0.7853719629\), already close to \(\pi/4\).

## Relationship to prior work

Bailey, Gallardo-Gutiérrez and Partington (2026) characterize infinite continuous semigroup frames and their cogenerator descriptions; their theorem does not optimize a three-event, fixed-horizon information determinant. A published exact oscillator-frame study treats **equally spaced** events \(0,h,2h\), optimizing \(h\) and obtaining a strong-damping determinant envelope; that sampling geometry cannot imply a free interior measurement with compulsory \(0,T\) and the present all-horizon uniqueness and oscillatory offset. Published pinned-Jordan and pinned-two-real-exponential calculations establish sharp threshold phenomena for *nonoscillatory* regression families. Neither gives the periodic sine structure (6), the first-rotation dominance (8), or the alternating large-horizon sign in (2). Baran, Szák-Kocsis and Stehlík (2017) study a *stationary complex Ornstein--Uhlenbeck stochastic process* with two-coordinate observations, correlated process noise, and trend or covariance-parameter estimation; their Fisher objective is not (3), which concerns two deterministic initial amplitudes and scalar observations with independent noise. Krauss, Lopez and Müller (2022) establish sample observability under missing time measurements, not the sharp noisy determinant design.

The Cauchy--Binet identity, elementary trigonometric transformation, and implicit-function expansion are standard tools; the claimed contribution is the **combined global classification**, critical horizon and oscillatory optimal-time drift for the specified dynamical frame, not these tools in isolation.

## Limitations

The theorem fixes two unknown initial coordinates, a scalar real observation, known stable damping and rotation, independent homoscedastic errors and exactly three events with two pinned endpoints. A repeated endpoint must be interpreted as a fresh independent measurement. General continuous-frame classification, process-noise models, unknown generator parameters, nonuniform noise, more observations, or minimax eigenvalue criteria are outside its scope. The long-horizon remainder is for fixed positive \(a/\omega\), not uniform as damping vanishes. No general publication-priority guarantee is possible; broader optimal-design literature could contain an equivalent special-case argument. The finite checker is not an infinite-parameter proof.

## References

1. V. Bailey, E. A. Gallardo-Gutiérrez and J. R. Partington, *Frames Associated with \(C_0\)-Semigroups*, arXiv:2611.13867v1, first public 2026-11-10, https://arxiv.org/html/2611.13867v1 .
2. *Sharp strong-damping observability envelope for three-time oscillator sampling*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-strong-damping-observability-envelope-for-three-time-oscil--718ab126a5c2 .
3. *A sharp horizon transition for pinned observations of two exponential modes*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-horizon-transition-for-pinned-observations-of-two-expone--fd2b83b9ab32 .
4. *A sharp horizon bifurcation for pinned damped-Jordan observation timing*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-horizon-bifurcation-for-pinned-damped-jordan-observation--8ad879b45d26 .
5. S. Baran, C. Szák-Kocsis and M. Stehlík, *D-optimal designs for complex Ornstein-Uhlenbeck processes*, arXiv:1704.05719v1, first public 2017-04-19, https://arxiv.org/html/1704.05719v1 .
6. I. Krauss, V. G. Lopez and M. A. Müller, *Sample-based observability of linear discrete-time systems*, arXiv:2204.06451v3, first public 2022-04-13, https://arxiv.org/html/2204.06451v3 .
