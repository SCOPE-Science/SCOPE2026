# Reset-rate current reversal in a one-well periodic Brownian ratchet

## Finding

There exists a smooth periodic potential with exactly one nondegenerate local minimum and one nondegenerate local maximum per period, for which a Brownian particle reset at independent Poisson times to the minimum of its *current* potential well has a strictly negative long-time velocity at all sufficiently small positive resetting rates and a strictly positive long-time velocity at all sufficiently large resetting rates. In particular, the velocity vanishes at an intermediate resetting rate. An explicit periodic piecewise-affine potential also has this behavior.

The constructive witness uses period \(L=21/10\), left well boundary \(-A=-11/10\), right boundary \(B=1\), diffusion coefficient \(D=1\), and the potential, periodically continued,
\[
V(x)=\begin{cases}
-20x/11,&-11/10\le x\le0,\\
x/20,&0\le x\le9/10,\\
9/200+(391/20)(x-9/10),&9/10\le x\le1.
\end{cases}
\]
Its minimum is \(V(0)=0\), its unique periodic maximum is \(V(-11/10)=V(1)=2\), and the right well boundary is nearer the minimum than the left boundary. Nevertheless the rare-reset current is *negative*, while the frequent-reset current is positive. This is a direction reversal within one fixed potential, with no externally applied tilt or time-dependent potential.

## Assumptions and scope

Let \(V\) be a continuous \(L\)-periodic potential that is piecewise \(C^1\) with bounded derivative, with one minimum at each \(nL\), and one maximum at each \(nL-A\) (equivalently \(nL+B\)), where \(A,B>0\) and \(L=A+B\). Between resets the unwrapped particle follows the diffusion
\[
 dX_t=-V'(X_t)\,dt+\sqrt 2\,dW_t,
\]
where the value of \(V'\) at the finitely many corners is immaterial to the diffusion law. At independent Poisson times of rate \(r>0\), set \(X_t=nL\) if \(X_{t-}\in(nL-A,nL+B]\). The reset site is the minimum of the occupied well, not a fixed external point, and the reset itself is instantaneous. Define \(v(r)=\lim_{t\to\infty}\mathbb E[X_t-X_0]/t\), with \(X_0=0\). The same velocity is the almost-sure long-time winding velocity. All assertions concern \(D=1\); rescaling extends the construction to any fixed positive diffusion coefficient.

## Proof

**1. Exact renewal reduction.** Let \(\widehat X_t\) be the diffusion without resets, started at \(0\), let \(\tau\sim\operatorname{Exp}(r)\) be independent, and define the integer \(K_t\) uniquely by \(\widehat X_t-K_tL\in(-A,B]\). Successive reset-to-reset changes of reset site are independent copies of \(LK_\tau\); their holding times are independent identically distributed exponential durations of mean \(1/r\) (the displacement and duration within each cycle may be dependent). Since the drift is bounded, both the cell displacements and the within-cycle residual position have finite first moments, and the latter is \(o(t)\) in mean and almost surely after division by \(t\). The renewal-reward theorem consequently gives
\[
 v(r)=rL\,m(r),\qquad m(r)=\mathbb E[K_\tau]. \tag{1}
\]

**2. Harmonic coordinate.** Set
\[
 Z_+=\int_{-A}^{B}e^{V(x)}\,dx,\qquad
 Z_-=\int_{-A}^{B}e^{-V(x)}\,dx,\qquad
 h(x)=\frac{L}{Z_+}\int_0^xe^{V(u)}\,du.
\]
Then \(h(x+L)=h(x)+L\), and \(h''-V'h'=0\) almost everywhere. Its derivative is globally bounded and continuous, so the generalized Itô formula yields a true martingale \(h(\widehat X_t)\). Optional stopping at the independent exponential time is legitimate by the linear-growth bound on \(h\), bounded drift, and finite Gaussian-exponential moments. Write \(Y_t=\widehat X_t-K_tL\in(-A,B]\). Hence
\[
 0=\mathbb E[h(\widehat X_\tau)]
 =\mathbb E[h(Y_\tau)]+L\mathbb E[K_\tau],\qquad
 m(r)=-\frac1L\mathbb E[h(Y_\tau)]. \tag{2}
\]
The diffusion modulo \(L\) is ergodic on the circle, with invariant density \(\pi(y)=e^{-V(y)}/Z_-\). Its exponential resolvent distribution converges weakly to \(\pi\) as \(r\downarrow0\). Since \(h\) is bounded on one cell, equation (2), followed by Fubini's theorem, proves
\[
 \lim_{r\downarrow0}m(r)
 =\frac{J_L-J_R}{Z_+Z_-},\tag{3}
\]
where
\[
 J_L=\int_{-A}^{0}\!dx\int_{-A}^{x}\!dy\,e^{V(x)-V(y)},\qquad
 J_R=\int_0^{B}\!dx\int_x^{B}\!dy\,e^{V(x)-V(y)}.
\]
The order of integration matters: both quantities are strictly positive. Formula (3) is a signed competition between two weighted triangular areas, not merely geometric barrier distances.

**3. Strict rare-reset sign for the explicit potential.** On the entire left arm, \(V(x)=-20x/11\) and \((20/11)A=2\). Direct integration gives
\[
 J_L=\frac{121}{400}(1+e^{-2})<\frac{121}{350}.
\]
The last inequality follows from \(e^2>7\), itself immediate from the positive Taylor series. On the first \(9/10\) units of the right arm, the slope is \(1/20\); retaining only pairs of points in that subinterval gives the strict estimate
\[
 J_R>\frac{81}{200}e^{-9/200}>
 \frac{81}{200}\left(1-\frac9{200}\right)
 =\frac{15471}{40000}>\frac{121}{350}.
\]
Thus \(J_R>J_L\), and equations (1)–(3) imply \(v(r)<0\) for all sufficiently small \(r>0\). Numerical values, not needed for the proof, are \(J_L\approx0.34343892318\), \(J_R\approx0.44050458740\), and \(m(0+)\approx-0.01459385345\).

**4. Strict frequent-reset sign whenever \(A>B\).** More generally let \(M=\lVert V'\rVert_\infty<\infty\). Couple the unreset diffusion to \(B_t=\sqrt2 W_t\). Pathwise,
\[
 B_t-Mt\le \widehat X_t\le B_t+Mt.
\]
For an independent \(\tau\sim\operatorname{Exp}(r)\), define \(\omega=\sqrt{M^2+4r}\), \(\lambda_+=(\omega+M)/2\), and \(\lambda_-=(\omega-M)/2\). The asymmetric-Laplace law of \(B_\tau-M\tau\) gives, for every \(x>0\),
\[
 \mathbb P(B_\tau-M\tau\ge x)=\frac{\lambda_-}{\omega}e^{-\lambda_+x},\qquad
 \mathbb P(B_\tau-M\tau\le-x)=\frac{\lambda_+}{\omega}e^{-\lambda_-x}.
\]
Because a rightward jump to another reset site requires \(\widehat X_\tau\ge B\), while leftward jumps through \(n\) sites require \(\widehat X_\tau\le -A-(n-1)L\), the positive and negative parts of \(K_\tau\) obey
\[
 \begin{aligned}
 \mathbb E[(K_\tau)_+]&\ge\frac{\lambda_-}{\omega}e^{-\lambda_+B},\\
 \mathbb E[(-K_\tau)_+]&\le
 \frac{\lambda_+}{\omega}
 \frac{e^{-\lambda_- A}}{1-e^{-\lambda_-L}}.
 \end{aligned}\tag{4}
\]
Since \(\lambda_\pm=\sqrt r+O(1)\), the ratio of the upper bound to the lower bound in (4) tends to zero whenever \(A>B\). Therefore \(m(r)>0\) for all sufficiently large \(r\). The explicit witness has \(11/10>1\), so its frequent-reset velocity is positive. Continuity of \(m(r)=\mathbb E[K_\tau]\) on \((0,\infty)\) follows by exponential-time integral representation and locally uniform dominated convergence, because bounded drift yields finite exponential-time displacement moments. By the intermediate value theorem the current changes sign at least once. No uniqueness of that zero is claimed.

**5. Smooth single-well realization.** Periodically convolve the displayed piecewise-affine \(V\) with a symmetric, strictly positive on its support, smooth mollifier of sufficiently small radius \(\varepsilon\). Its slope is strictly negative to the left of the original minimum and strictly positive to its right, except for the periodic maximum, with a positive-to-positive change at \(9/10\). Smoothing produces exactly one strict minimum and exactly one strict maximum per period: near each original extremum the convolved derivative crosses zero monotonically and only once, while outside those neighborhoods its sign is unchanged. Both extrema are nondegenerate for a mollifier with positive smooth density on the relevant crossing neighborhoods. Translate the minimum to \(0\). The left and right barrier distances converge respectively to \(A=11/10\) and \(B=1\); thus the strict inequality \(A_\varepsilon>B_\varepsilon\) persists. The weighted integrals \(J_{L,\varepsilon}\) and \(J_{R,\varepsilon}\) depend continuously on the uniform potential and moving endpoints, so \(J_{R,\varepsilon}>J_{L,\varepsilon}\) persists. Steps 2–4 apply to the smooth potential and prove both signs and an intervening zero. This establishes the claimed smooth theorem.

## Verification

A standalone standard-library checker, `verify_ratchet.py`, independently evaluates all three affine-segment integrals, partition functions, the signed small-rate coefficient, and the strict rational separation \(J_L<121/350<15471/40000<J_R\). It also computes the two Gaussian-exponential-time probability bounds used in the large-rate argument. Execute with `python verify_ratchet.py` from the extracted package. Separately, a reversible finite-volume discretization of the modulo-cell resolvent was compared with the analytic small-rate limit and returned a negative velocity at rates \(r=0.001,1,10\) and positive velocity at \(r=30,60,100\) using a grid of 8,400 cells; these finite-resolution checks are illustrative, not proof of the universal sign assertions.

## Relationship to prior work

Ghosh, Nayak, Liu, Li and Marchesoni (2023) introduced and numerically examined local-potential-minimum stochastic resetting in an asymmetric periodic substrate. Their displayed sinusoidal-ratchet example has one current direction, and their fast-reset analysis addresses escape suppression; the present result instead proves that a single *fixed* potential can exhibit opposite current directions at different resetting rates. The construction is not a reversal caused by externally switching a potential or by changing its spatial asymmetry. Roberts, Sezik and Lardet (2024) consider a distinct alternating free-diffusion/potential-on resetting protocol, for which the force and reset dynamics differ. Prior results for periodic reset sites without a confining potential and for tilted or dynamically rocked ratchets do not imply the sign criterion (3) together with the high-rate nearest-barrier theorem (4).

## Limitations

The existence theorem does not count all velocity zeros, bound their exact locations, or establish stability under noisy finite-time measurements. The piecewise-affine formula has corner forces and is used as a transparent certificate; the smooth result is existential, obtained by sufficiently small periodic convolution. Finite-volume numerical evidence is not a substitute for either of the analytic inequalities. The investigated primary literature is not an exhaustive publication-priority certification, and a stronger, unindexed general resetting theorem may subsume the result.

## References

1. P. K. Ghosh, S. Nayak, Y. Liu, Y. Li and F. Marchesoni, *Autonomous Ratcheting by Stochastic Resetting* (2023), https://arxiv.org/abs/2307.06202, first posted 2023-07-12.
2. D. Roberts, E. Sezik and C. Lardet, *Ratchet-mediated resetting: Current, efficiency, and exact solution* (2024), https://arxiv.org/abs/2405.10698.
3. Fang, Tian and Zeng, *Stochastic resetting-induced reentrance phenomena of inertial Brownian particle in rough periodic potential* (2023), https://doi.org/10.1140/epjp/s13360-023-04443-x, abstract-only comparison; different inertial, biased rough-potential setting.
