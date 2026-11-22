# An infinite ladder of quadratic sampling folds in stable two-gene feedback dynamics

## Finding

A smooth two-gene negative-feedback flow can determine its hidden concentration from a continuously measured coordinate and its derivative, yet **two exact, noiseless coordinate snapshots can be noninjective at infinitely many sampling times and in an open interval around each**. The mechanism is a nonzero second variation of the sampled output, not merely a singular linearized observability matrix. We give an explicit curvature formula throughout the equal-decay, equal-small-signal-gain class and a positive, globally attracting logistic realization.

Define
\[
D=(\gamma^2+a^2)(\gamma^2+9a^2),\qquad
K=\gamma(\gamma^2+7a^2)F''(y_*)+6a^3G''(x_*).
\]
For every integer \(k\ge1\), write \(T_k=k\pi/a\), and let \(P_T(v)\) be the first coordinate at time \(T\) of the flow started at \((x_*,y_*+v)\). Then
\[
P_{T_k}'(0)=0,\qquad
P_{T_k}''(0)=\frac{(-1)^ke^{-\gamma T_k}\bigl(1-(-1)^ke^{-\gamma T_k}\bigr)}{D}\,K.
\]
If \(K\ne0\), these are nondegenerate quadratic extrema, with signs alternating as \(k\) changes parity. For every \(k\), a nearby continuously differentiable curve of quadratic extrema exists for all times in some open interval around \(T_k\), including nonresonant times. Its initial-value displacement has sharp first derivative
\[
v_k'(T_k)=\frac{aD}{K\bigl(1-(-1)^ke^{-\gamma T_k}\bigr)}.
\]
Therefore, at each such time the observation pair \((x(0),x(T))\) is exactly identical for two distinct nearby initial hidden concentrations.

## Assumptions and scope

Assume \(\gamma,a>0\), and \(F,G\) are \(C^3\) on a neighborhood of a point \((x_*,y_*)\) satisfying
\[
F(y_*)=\gamma x_*,\quad G(x_*)=\gamma y_*,\quad
F'(y_*)=-a,\quad G'(x_*)=a.
\]
The local assertion is about the ordinary finite-time solution flow of
\[
\dot x=F(y)-\gamma x,\qquad \dot y=G(x)-\gamma y
\]
and its two-snapshot first-coordinate observation, with the first observation fixed to \(x(0)=x_*\). All quantifiers \(k\ge1\) range over the positive integers. The time neighborhoods and initial-condition neighborhoods may shrink with \(k\); no uniform-in-\(k\) width is asserted. Only local existence of indistinguishable pairs is asserted, not that every pair or any fixed pair remains indistinguishable at all sample times.

For a fully positive logistic example, take \(\gamma=a=1\), \((x_*,y_*)=(1,1)\) and
\[
F(y)=\frac{4/3}{1+\exp(4(y-1)-\log3)},\qquad
G(x)=\frac{2}{1+\exp(-2(x-1))}.
\]
Then \(F(1)=G(1)=1\), \(F'(1)=-1\), \(G'(1)=1\), \(F''(1)=-2\), \(G''(1)=0\), so \(D=20\), \(K=-16\). For strictly positive initial states sufficiently near \((1,1)\), all observations and both initial states are physically positive.

## Proof

Let \(\phi_t\) denote the local flow, and set \((X(t,v),Y(t,v))=\phi_t(x_*,y_*+v)\). The first variation \((u,w)=\partial_v(X,Y)|_{v=0}\) is governed by
\[
\begin{pmatrix}\dot u\\\dot w\end{pmatrix}
=\begin{pmatrix}-\gamma&-a\\a&-\gamma\end{pmatrix}
\begin{pmatrix}u\\w\end{pmatrix},\qquad (u(0),w(0))=(0,1),
\]
hence
\[
u(t)=-e^{-\gamma t}\sin(at),\qquad w(t)=e^{-\gamma t}\cos(at).
\]
In particular, \(P_T'(0)=-e^{-\gamma T}\sin(aT)\), which vanishes at \(T_k=k\pi/a\) and has time derivative \(-a(-1)^ke^{-\gamma T_k}\) there.

The second variation \((U,W)=\partial_v^2(X,Y)|_{v=0}\), initially zero, solves
\[
\frac{d}{dt}\begin{pmatrix}U\\W\end{pmatrix}
=\begin{pmatrix}-\gamma&-a\\a&-\gamma\end{pmatrix}
\begin{pmatrix}U\\W\end{pmatrix}
+\begin{pmatrix}F''(y_*)w(t)^2\\G''(x_*)u(t)^2\end{pmatrix}.
\]
Variation of constants and the half-rotation identities for sine and cosine give
\[
U(T_k)=(-1)^ke^{-\gamma T_k}\int_0^{T_k}e^{-\gamma s}
\bigl[F''(y_*)\cos^3(as)+G''(x_*)\sin^3(as)\bigr]\,ds.
\]
Put \(r_k=(-1)^ke^{-\gamma T_k}\). By triple-angle identities or elementary Laplace integration,
\[
\int_0^{T_k}e^{-\gamma s}\cos^3(as)\,ds
=(1-r_k)\frac{\gamma(\gamma^2+7a^2)}D,\qquad
\int_0^{T_k}e^{-\gamma s}\sin^3(as)\,ds
=(1-r_k)\frac{6a^3}D.
\]
Thus \(P_{T_k}''(0)=r_k(1-r_k)K/D\). Since \(|r_k|<1\), this is nonzero precisely when \(K\ne0\). Its sign is \((-1)^k\operatorname{sgn}K\).

Apply the implicit function theorem to \(H(T,v)=\partial_vP_T(v)\) at each \((T_k,0)\). The nonzero derivative \(\partial_vH=P_{T_k}''(0)\) yields a smooth local critical-point curve \(v=v_k(T)\). Continuity preserves the strict sign of \(\partial_v^2P_T\) near it. Every such critical point is a local quadratic extremum, hence every sufficiently near output value on the proper side is attained at *two distinct* nearby \(v\) values. Differentiating \(H(T,v_k(T))=0\) gives
\[
v_k'(T_k)=-\frac{\partial_T\partial_vP_T|_{(T_k,0)}}{P_{T_k}''(0)}
=\frac{aD}{K(1-r_k)}.
\]
This proves both the exact resonant curvature and open-time persistence.

For the logistic example, the displayed derivatives imply
\[
P_{k\pi}''(0)=-\frac45(-1)^ke^{-k\pi}\bigl(1-(-1)^ke^{-k\pi}\bigr),\quad
v_k'(k\pi)=-\frac5{4(1-(-1)^ke^{-k\pi})}.
\]
Consequently odd \(k\) give strict minima and even \(k\) give strict maxima. All positive trajectories of the logistic system are ultimately bounded: \(0<F(y)<4/3\) and \(0<G(x)<2\) make \([0,4/3]\times[0,2]\) forward invariant and attracting up to the boundary. An equilibrium must satisfy \(x=F(G(x))/1\), whose right side is strictly decreasing, so \((1,1)\) is the unique equilibrium in the nonnegative quadrant. The constant divergence equals \(-2\), prohibiting periodic orbits; the unique equilibrium is a hyperbolic sink (eigenvalues \(-1\pm i\)). Bounded positive orbits therefore converge to it by planar limit-set theory, because boundary accumulation is prevented by strictly positive inward vector fields. This establishes the claimed global attraction independently of sampling ambiguity.

Finally, since \(F\) is strictly decreasing, knowing \((x(t),\dot x(t))\) at any time gives \(y(t)=F^{-1}(\dot x(t)+x(t))\) when the observed value is in the range of \(F\). This continuous-time reconstruction does not imply two-snapshot injectivity.

## Verification

The accompanying standalone `check_fold.py` uses SymPy to verify the exact cubic-trigonometric integrals for the first four resonances, and SciPy high-accuracy variational integration to check the logistic first and second derivatives for \(k=1,2,3,4\). It also solves a genuinely nonresonant equal-output pair. At \(T=\pi+0.02\), the two initial hidden concentrations are approximately \(0.95670098564\) and \(0.99690862440\); their common later first coordinate is approximately \(0.99999755182034\), whereas the equilibrium-local first derivative at this detuned time is nonzero. The analytic variation-of-constants argument, not these finite computations, proves the assertion for every integer \(k\ge1\).

Run `python check_fold.py` with Python, NumPy, SciPy and SymPy installed. The script reads no external data.

## Relationship to prior work

Belgacem (2026) establishes invertibility of the instantaneous nonlinear observability map built from a measured coordinate and its time derivative, plus explicit Luenberger observer bounds for sigmoidal two-gene networks. That result does not state injectivity of the finite two-snapshot map studied here; our example demonstrates why such an inference would be invalid.

Baranowski (2026) investigates nonlinear sampled-output singularities and a cubic no-fold regime. Its damped pendulum has a symmetry-forced vanishing quadratic term at resonance, and folds emerge on one detuning side. The present result instead computes a nonzero *quadratic* resonant jet across every half-rotation of a two-gene feedback focus; its folds already exist at resonance and persist on both sides. The implicit-function-theorem step is standard singularity theory, not claimed as a new general fold theorem. Aeyels (1981) concerns generic observability with sufficiently many samples and does not imply injectivity of two samples in this specific model.

## Limitations

The curvature formula assumes equal degradation rates and equal-magnitude opposing equilibrium slopes. It does not extend automatically to unequal rates or to points where \(K=0\). Distinct initial hidden concentrations are shown to match at *two* sampled times only; full continuous-time trajectories remain distinguishable. The timing neighborhoods and initial-state separations are not uniform in resonance index. There is no claim of robust ambiguity after adding three or more arbitrary samples, and no claim concerning measurement noise, parameter identification, or error-optimal estimation. Historical priority remains subject to independent mathematical review.

## References

- Ismail Belgacem, *Luenberger observers for two-gene regulatory networks with sigmoidal regulation: explicit observability conditioning, polytopic convergence certificates, and a logistic–Hill comparison*, arXiv:2611.17232v1 (first public 2026-11-12). https://arxiv.org/html/2611.17232v1
- Jerzy Baranowski, *Singular Sampling in Nonlinear Observability: Higher-Order Minimax Laws and Timing Crossovers*, arXiv:2610.15906v1 (2026). https://arxiv.org/abs/2610.15906
- Dirk Aeyels, *Generic Observability of Differentiable Systems*, SIAM J. Control Optim. (1981), doi:10.1137/0319037. https://doi.org/10.1137/0319037
