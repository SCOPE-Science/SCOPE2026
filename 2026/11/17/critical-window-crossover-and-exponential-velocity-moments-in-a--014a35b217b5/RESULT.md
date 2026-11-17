# Critical-window crossover and exponential velocity moments in a cubic global center

## Finding
For fixed \(\alpha,\beta>0\), consider the cubic polynomial center
\[
\dot x=y,\qquad \dot y=-x(1+\alpha x^2+\beta y^2),
\]
and let \((x_A(t),y_A(t))\) be the periodic trajectory through \((A,0)\), with minimal **original physical-time** period \(T_A\). Sample \(t\) uniformly from one such period. For fixed real \(q\ge0\), define the amplitude-normalized velocity moment
\[
M_q(A)=\frac1{T_A}\int_0^{T_A}\left|\frac{y_A(t)}A\right|^qdt,
\qquad \gamma=\sqrt{\alpha/\beta}.
\]
**The new assertion is the sharp moment law, including its singular order-one window.** At every fixed order,
\[
\boxed{\begin{aligned}
M_q(A)&\longrightarrow \frac{\gamma^q}{\cos(\pi q/2)},&&0\le q<1,\\[2pt]
M_1(A)&\sim \frac{2\sqrt{\alpha\beta}}\pi A^2,&&q=1,\\[2pt]
M_q(A)&\sim\gamma^q A\sqrt{\frac{2\beta}{\pi(q-1)}}
\exp\!\left(\frac{\beta(q-1)A^2}{2}\right),&&q>1.
\end{aligned}}
\tag{A}
\]
More sharply, let the moment order approach the threshold on its **natural squared-amplitude scale**: \(q_A=1+\lambda/A^2\) for any fixed \(\lambda\in\mathbb R\). Then
\[
\boxed{\frac{M_{1+\lambda/A^2}(A)}{A^2}\longrightarrow
\frac{2\sqrt{\alpha\beta}}\pi\,
\mathcal F_\beta(\lambda),\qquad
\mathcal F_\beta(\lambda)=\int_0^1
\exp\!\left(\frac{\beta\lambda}{2}(1-u^2)\right)\,du.}
\tag{B}
\]
The convergence in (B) is **uniform for \(\lambda\) in every fixed compact real interval**, and \(\mathcal F_\beta(0)=1\). This gives a nondegenerate, explicitly evaluable interpolation between moment orders just below and just above one. In particular, the critical-order moment grows quadratically in \(A\), whereas **each fixed order above one** has an exponentially growing high-amplitude moment with a sharp prefactor.

For context, the exact same oscillator already has a known high-amplitude turning-gap/arcsine law and leading period
\[
T_A\sim 2\pi/(A^2\sqrt{\alpha\beta}).
\]
These background results and the associated weak Cauchy velocity occupation law (with independent fair sign of the position) are reconstructed below solely to normalize and prove the **new unbounded-observable moment assertions**. They are **not claimed as additional original findings**. The moment formula at orders above one and the uniform transition (B) require control of extremely rare high-velocity orbit segments not determined by weak convergence or total-variation convergence of the turning-gap law alone.

## Assumptions and scope
The real coefficients \(\alpha,\beta\) are strictly positive and **fixed** as \(A\to\infty\). All initial conditions \((A,0)\) have \(A>0\), and the original unrescaled vector field fixes the time convention. The background joint convergence is weak convergence of probability measures on \(\mathbb R^2\) against bounded continuous functions. The fixed-order moment statements hold for each fixed real \(q\ge0\); the additional window varies the order only as \(q_A=1+\lambda/A^2\), with \(\lambda\) fixed or restricted to a compact real interval. The point \((0,0)\) is the only equilibrium; it is excluded from the periodic trajectories. No claim is made at \(\alpha=0\), \(\beta=0\), with varying parameters, or for arbitrarily fast-growing observables beyond the stated fixed moments.

## Proof
**1. Exact periodic ovals.** Set \(X=x^2\) and \(Y=y^2\). On each non-axis arc, the equations imply
\[
\frac{dY}{dX}=-(1+\alpha X+\beta Y).
\]
Consequently
\[
H(x,y)=e^{\beta x^2}\left(y^2+\frac\alpha\beta x^2+\frac{\beta-\alpha}{\beta^2}\right)
\]
is constant: the derivative of the displayed bracket with respect to \(X\) is minus \(\beta\) times that bracket. For the level through \((A,0)\), write \(s=A^2-x^2\). The **exact** positive-square-speed graph is
\[
\begin{split}
Y_A(s)&=\frac{\alpha A^2}{\beta}(e^{\beta s}-1)
+\frac{\beta-\alpha}{\beta^2}(e^{\beta s}-1)
+\frac\alpha\beta s\\
&=\int_0^s [1+\alpha(A^2-s+u)]e^{\beta u}\,du,\quad 0\le s\le A^2.
\end{split}
\tag{1}
\]
The integral proves \(Y_A(s)>0\) for \(0<s\le A^2\), and \(Y_A(0)=0\). Thus the branches \(y=\pm\sqrt{Y_A(A^2-x^2)}\) for \(-A\le x\le A\) make a smooth simple closed regular level, with precisely the two turning points at \(x=\pm A\). The origin is the only equilibrium because \(\dot x=0\) entails \(y=0\) and then \(\dot y=-x(1+\alpha x^2)\); it does not lie on this level. A nonvanishing smooth planar flow traverses the oval in finite time, and its full traversal is its minimal period. Reflection and time reversal make the four quadrants equal in physical-time duration.

**2. Exact physical-time coordinate.** Set
\[
v_A(s)=\frac{\sqrt{Y_A(s)}}A,\qquad
D_A=\int_0^{A^2}\frac{ds}{\sqrt{1-s/A^2}\,v_A(s)}.
\tag{2}
\]
Since \(dt=|dx|/|y|\) along each quadrant and \(|dx|=ds/[2\sqrt{A^2-s}]\),
\[
T_A=\frac{2D_A}{A^2}.
\tag{3}
\]
Conditioned on any one of the four sign quadrants, the random variable \(s=A^2-x_A(t)^2\) has **exact** density
\[
p_A(s)=\frac{\mathbf1_{(0,A^2)}(s)}{D_A\sqrt{1-s/A^2}\,v_A(s)}.
\tag{4}
\]
Every quadrant gives the same conditional density and has probability \(1/4\), so the two signs are independent fair signs, jointly independent of \(s\), at each finite \(A\).

**3. The turning layer and period.** Put \(\gamma=\sqrt{\alpha/\beta}\). Equation (1) gives for every fixed \(s>0\)
\[
v_A(s)\longrightarrow v_\infty(s)=\gamma\sqrt{e^{\beta s}-1}.
\tag{5}
\]
This convergence passes through the **integral** in (2). To verify the moving-endpoint integrability, choose \(A\) so large that \(\alpha/\beta+(\beta-\alpha)/(\beta^2A^2)\ge\alpha/(2\beta)\). Then (1) yields
\[
v_A(s)^2\ge\frac{\alpha}{2\beta}(e^{\beta s}-1).
\]
For \(s\le A^2/2\), the other factor \((1-s/A^2)^{-1/2}\) is at most \(\sqrt2\), and the reciprocal of \(\sqrt{e^{\beta s}-1}\) is integrable at zero and at infinity. On \(A^2/2<s<A^2\), the integral is bounded by a constant times
\[
e^{-\beta A^2/4}\int_{A^2/2}^{A^2}\frac{ds}{\sqrt{1-s/A^2}}
\le 2A^2e^{-\beta A^2/4},
\]
which tends to zero. Hence dominated convergence on the first part and this tail bound give
\[
D_A\longrightarrow \frac1\gamma\int_0^\infty\frac{ds}{\sqrt{e^{\beta s}-1}}
=\frac{\pi}{\beta\gamma}=\frac\pi{\sqrt{\alpha\beta}}.
\tag{6}
\]
The integral evaluates via \(r=e^{-\beta s}\) as \(\beta^{-1}B(1/2,1/2)=\pi/\beta\). Equation (3) gives the asserted sharp period scale. Equations (4)–(6) also show that \(s\) converges **in distribution** to the density
\[
p_\infty(s)=\frac\beta{\pi\sqrt{e^{\beta s}-1}},\qquad s>0.
\tag{7}
\]
In fact, extending the densities by zero beyond \(A^2\), their pointwise convergence and unit integrals give convergence in total variation by Scheffé's lemma. This stronger assertion is only for the turning-layer variable \(s\).

**4. The joint Cauchy law.** On any one quadrant, the signs of \(x\) and \(y\) are fixed and
\[
\left(\frac{|x|}{A},\frac{|y|}A\right)
=\left(\sqrt{1-s/A^2},v_A(s)\right)
\longrightarrow\left(1,\gamma\sqrt{e^{\beta s}-1}\right)
\]
under the converging tight layer laws. Indeed convergence of these functions is uniform on any compact subinterval of \((0,\infty)\), and the limiting layer density assigns arbitrarily small mass outside a suitable such interval. Make the exact substitution \(\Theta=\arccos(e^{-\beta s/2})\). By (7), \(\Theta\) is uniform on \((0,\pi/2)\), and \(\sqrt{e^{\beta s}-1}=\tan\Theta\). Therefore the limit of \(|y|/A\) is \(\gamma\tan\Theta\), a half-Cauchy law of scale \(\gamma\); inserting its exact independent fair sign makes it symmetric Cauchy. The independent fair sign of \(x\) yields the stated joint law.

**5. The sharp moment transition.** From (4), for every \(q\ge0\),
\[
M_q(A)=\frac{I_q(A)}{D_A},\qquad
I_q(A)=\int_0^{A^2}\frac{v_A(s)^{q-1}}{\sqrt{1-s/A^2}}\,ds.
\tag{8}
\]
For \(0\le q<1\), the lower bound in Step 3 dominates \(v_A(s)^{q-1}\) by a constant times \((e^{\beta s}-1)^{(q-1)/2}\), integrable on \((0,\infty)\). Split again at \(A^2/2\); the upper half is bounded by \(C_q A^2e^{-\beta(1-q)A^2/4}\) and vanishes. The lower half is treated by dominated convergence. Writing \(r=e^{-\beta s}\), one obtains
\[
I_q(A)\longrightarrow\frac{\gamma^{q-1}}\beta
B\!\left(\frac{1-q}{2},\frac{1+q}{2}\right)
=\frac{\pi\gamma^{q-1}}{\beta\cos(\pi q/2)}.
\]
Dividing by (6) proves the subcritical moment limit.

For \(q=1\), the numerator in (8) is exactly \(I_1(A)=\int_0^{A^2}(1-s/A^2)^{-1/2}ds=2A^2\), and (6) gives the displayed polynomial asymptotic.

For fixed \(q>1\), set \(u=A^2-s\) in (8) and factor out the growing term:
\[
\frac{I_q(A)}{A e^{\beta(q-1)A^2/2}}=
\int_0^{A^2}\frac{1}{\sqrt u}
\left[e^{-\beta A^2/2}v_A(A^2-u)\right]^{q-1}\,du.
\tag{9}
\]
For every fixed \(u\ge0\), the bracket converges to \(\gamma e^{-\beta u/2}\). From (1), uniformly for all sufficiently large \(A\), \(v_A(s)\le C e^{\beta s/2}\) for \(0\le s\le A^2\), so the integrand in (9) is dominated by \(C_q u^{-1/2}e^{-\beta(q-1)u/2}\), integrable on \((0,\infty)\). Thus
\[
\frac{I_q(A)}{A e^{\beta(q-1)A^2/2}}
\longrightarrow\gamma^{q-1}\sqrt{\frac{2\pi}{\beta(q-1)}}.
\]
Dividing by (6) gives the asserted exponential high-moment coefficient. No finite-amplitude computation was used to prove a limit.


**6. The order-one critical window (the central new transition).** Write \(q_A=1+\lambda/A^2\) and substitute \(s=A^2t\) into (8):
\[
\frac{I_{q_A}(A)}{A^2}=\int_0^1\frac{\exp\bigl[(\lambda/A^2)\log v_A(A^2t)\bigr]}{\sqrt{1-t}}\,dt.
\tag{10}
\]
For every \(0<t<1\), formula (1) yields
\[
\frac{\log v_A(A^2t)}{A^2}\longrightarrow\frac{\beta t}{2}.
\]
The convergence of the integral in (10) is locally uniform in \(\lambda\). Here are bounds at the two endpoints: from (1), for all sufficiently large \(A\), one has \(c\sqrt{e^{\beta s}-1}\le v_A(s)\le C e^{\beta s/2}\) on \(0<s\le A^2\), for fixed positive constants \(c,C\). Given \(|\lambda|\le L\), the upper bound controls positive exponents uniformly by \(C_L e^{L\beta t/2}\). The lower bound controls negative exponents; on \(0<s<1\) it gives at most a constant times \(s^{-L/(2A^2)}\), which, with \(s=A^2t\) and large \(A\), is bounded by \(C_Lt^{-1/4}\), whereas for \(s\ge1\) it is bounded uniformly. Thus the full integrand is dominated, uniformly on \(|\lambda|\le L\), by an integrable multiple of \((1+t^{-1/4})(1-t)^{-1/2}\). For each interior \(t\), convergence of the exponential is uniform on compact \(\lambda\)-sets. Dominated convergence for the compact-set supremum gives
\[
\sup_{|\lambda|\le L}\left|\frac{I_{1+\lambda/A^2}(A)}{A^2}
-\int_0^1\frac{e^{\beta\lambda t/2}}{\sqrt{1-t}}\,dt\right|\longrightarrow0.
\]
Dividing by \(D_A\to\pi/\sqrt{\alpha\beta}\) and changing variables \(t=1-u^2\) proves (B), including compact-uniformity. The crossover is genuinely nonconstant: \(\mathcal F_\beta'(\lambda)>0\) for all real \(\lambda\). For reference, its large-positive-argument tail is \(\mathcal F_\beta(\lambda)\sim e^{\beta\lambda/2}\sqrt{\pi/(2\beta\lambda)}\), matching the fixed-supercritical coefficient on their common scale. The latter tail follows from a standard elementary Gaussian integral, without asserting a uniform two-parameter matching theorem beyond (B).

## Verification
A standalone Python-standard-library checker `verify.py` reconstructs the exact speed graph (1), evaluates the physical-time quarter integrals using a desingularizing angular coordinate, checks the four-quadrant normalization and first absolute velocity moment identity, compares representative finite-amplitude periods and moments with all three fixed-order regimes, and numerically tests the critical-window profile in (B). Run `python verify.py` from the same directory. The checker prints `CUBIC_CENTER_CAUCHY_MOMENT_CHECK_OK` on success. The infinite quantifiers and limiting distribution follow from the analytic proof in Steps 1–5, **not** from finitely sampled trajectories or quadrature values.

## Relationship to prior work
Appis and Llibre (published online 5 April 2024, Theorem 4(d)) classified the present **reversible cubic global center** within their case \(a_1=a_2=a_3=a_5=a_7=0\), \(a_4=-\alpha<0\), \(a_6=-\beta<0\). Their full accessible article's purpose is the qualitative center classification, not time-sampled high-order velocity moments.

Existing exact period and turning-layer results for this **same oscillator** already establish the sharp period normalization \(T_A\sim2\pi/(A^2\sqrt{\alpha\beta})\) and a total-variation limit for the squared turning gap \(A^2-x^2\), with arcsine exponential transform; these statements are acknowledged as **previously established**, including their stronger parameter-uniform formulation. The scaled Cauchy velocity law is an elementary consequence of that turning-gap statement and the exact speed graph, so **neither it nor the leading period is asserted as new**. In contrast, total variation of turning-gap measures does not control moments of the unbounded observable \(|y/A|^q\) whose maximum grows exponentially with \(A^2\). Formula (A) for \(q>1\), with its exact exponential prefactor, and the locally uniform critical-window law (B) use separate estimates of these rare high-speed passages; neither statement follows from the bounded-test-function or total-variation turning-gap conclusion alone.

Another previously established Cauchy occupation theorem treats \(\dot X=(1+\kappa X^2)Y,\ \dot Y=-X\), equivalent after coordinate exchange to the zero-\(\alpha\) boundary of the present flow. That theorem has a different physical-period scale and does not cover the strictly positive restoring coefficient considered here. The published unequal-coefficient logarithmic-layer law for \(\dot x=y(1+\alpha x^2),\ \dot y=-x(1+\beta y^2)\) concerns a distinct vector field and does not imply (A)–(B). Broad period-function theory does not independently furnish the velocity-moment transition in these particular physical-time coordinates.

## Limitations
The theorem is restricted to strictly positive fixed coefficients and high amplitude on the unique periodic oval through \((A,0)\). The background Cauchy law is weak (not claimed in total variation on the changing joint phase space), and the new statements concern the fixed-order moments and the critical window only. The source classifications establish the existence of the center, while previously known turning-layer results provide the period and bounded-observable laws, not the new exponential-moment and order-window coefficients. Related nonlinear oscillator literature may contain unindexed equivalent formulations, so publication priority has not been independently certified. The numerical checker is a finite reproducibility aid rather than an infinite certificate, and independent mathematical audit has not been performed.

## References
1. R. F. Appis and J. Llibre, *Global centers of a family of cubic systems*, *Aequationes Mathematicae* 98 (2024), 1373–1389; first publicly published 2024-04-05, DOI:10.1007/s00010-024-01051-7. Full open-access article, in particular Theorem 4(d) and its proof: https://link.springer.com/article/10.1007/s00010-024-01051-7.
2. J. Llibre and G. Rondón, *Global centers of a class of cubic polynomial differential systems*, arXiv:2310.07454v1 (2023-10-11), DOI:10.1007/s12215-024-01034-2. Classification of a related cubic polynomial class: https://ddd.uab.cat/pub/artpub/2024/303176/LliRon2023-preprint.pdf. This is background, not asserted as covering the specific coefficient pair.
3. A. Cima, A. Gasull and F. Mañosas, *Period function for a class of Hamiltonian systems*, *Journal of Differential Equations* 168 (2000), 180–199, DOI:10.1006/jdeq.2000.3912. General period-function framework; not a source for the stated occupation law.
