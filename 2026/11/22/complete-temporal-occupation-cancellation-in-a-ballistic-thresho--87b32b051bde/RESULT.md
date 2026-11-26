# Sharp occupation-moment boundary for stationary ballistic threshold resetting

## Finding

For stationary fixed-length ballistic flights with independent positive durations of finite mean and an absolutely continuous duration law, the unscaled centered occupation integral has an explicit endpoint-difference limit. For any bounded real Borel observable that is not almost everywhere constant, the limiting absolute moment of order \(q>0\) is finite if and only if the flight duration has a finite moment of order \(q+1\). In particular, when the third duration moment is infinite, the unscaled integral still has a weak limit but its finite-window variance tends to infinity. The pathwise cancellation and endpoint convergence are the mechanism for this sharp moment boundary; they are not claimed as separate new results.

## Assumptions and scope

Fix \(L>0\). A flight of duration \(T\) moves as \(X(s)=L(1-s/T)\), \(0\le s<T\); upon hitting zero the particle resets instantaneously to \(L\). At each reset draw the next duration independently from a fixed absolutely continuous law on \((0,\infty)\) with \(0<\mathbb ET<\infty\). Use the stationary two-sided renewal process. At a stationary observation time the containing duration \(T^*\) has law \(t\Pr(T\in dt)/\mathbb ET\); independently, the fractional age \(U\) is uniform on \([0,1]\), so the position is uniform on \([0,L]\).

For bounded real Borel \(f\), put
\[
 \bar f=L^{-1}\int_0^L f(x)\,dx,\qquad H(u)=\int_0^u [f(L(1-v))-\bar f]dv,\qquad
 Y(t)=\int_0^t [f(X_s)-\bar f]ds.
\]
Write \(\Phi(s)\) for the duration times \(H\) of the fractional age in the flight containing \(s\). Its stationary marginal is \(\Phi=T^*H(U)\); let \(\Phi'\) be an independent copy. If \(f\) is almost everywhere constant then \(Y(t)=0\); the strict moment and variance conclusions below concern only non-a.e.-constant \(f\).

## Proof

On a flight, fractional age increases at rate \(1/T\), so the absolutely continuous primitive \(TH\) has time derivative \(f(X_s)-\bar f\) almost everywhere. Because \(H(0)=H(1)=0\), the primitive is consistent across resets. In particular every full-flight centered reward vanishes, and
\[
Y(t)=\Phi(t)-\Phi(0).
\]

For a bounded continuous test function \(g\) of duration and fractional age, a process started at a reset has time-\(t\) expectation equal to the forward renewal convolution with \(h(v)=\mathbb E[\mathbf1_{T>v}g(T,v/T)]\) (the integrand is zero when \(T\le v\)). Here \(h\) is continuous, by absolute continuity of the duration law and dominated convergence. Its absolute value is bounded by \(\|g\|_\infty\Pr(T>v)\), an integrable decreasing envelope, making \(h\) directly Riemann integrable. The nonarithmetic key renewal theorem gives the limit
\[
\frac{1}{\mathbb ET}\int_0^\infty h(v)dv
=\frac{1}{\mathbb ET}\mathbb E[T\int_0^1g(T,u)du]=\mathbb E g(T^*,U).
\]
At stationarity, condition on the initial flight and its finite residual life. After its next reset the fresh process is independent, with the limit just derived. Bounded convergence on products of initial and terminal tests yields convergence to independent stationary endpoints. The continuous map \((T,u)\mapsto TH(u)\) then gives \(Y(t)\Rightarrow \Phi'-\Phi\), with characteristic function
\[
\left|\frac{1}{\mathbb ET}\mathbb E[T\int_0^1 e^{isTH(u)}du]\right|^2.
\]
This symmetric limit need not be Gaussian. Tightness of \(Y(t)\) implies \(Y(t)/\sqrt t\to0\) in probability even when its variance diverges.

Independence in the stationary duration–phase law gives, for every \(q>0\) and non-a.e.-constant \(f\),
\[
\mathbb E|\Phi|^q=\frac{\mathbb ET^{q+1}}{\mathbb ET}\int_0^1 |H(u)|^qdu.
\]
The integral is finite and strictly positive by continuity and the almost-everywhere derivative of \(H\). A finite moment of \(\Phi\) gives a finite moment of the independent difference by the elementary two-term bound. Conversely, choose \(M>0\) with \(\Pr(|\Phi'|\le M)>0\). On \(\{ |\Phi|>2M,\ |\Phi'|\le M\}\) the difference has magnitude at least \(|\Phi|/2\); independence preserves any infinite tail moment. Thus \(\mathbb E|\Phi'-\Phi|^q<\infty\) if and only if \(\mathbb ET^{q+1}<\infty\). For \(T=L/V\) and velocity density \(\phi(v)\sim c v^\beta\) near zero, \(\beta>0\), the condition is \(q<\beta\) (equality diverges).

Stationarity and boundedness of \(f\) imply \(\mathbb EY(t)=0\) and finite variance for every finite \(t\). When \(\mathbb ET^3=\infty\), for each \(M\) the bounded continuous test \(x^2\wedge M\) gives \(\liminf_{t\to\infty}\mathbb E Y(t)^2\ge\mathbb E[(\Phi'-\Phi)^2\wedge M]\). The lower bound tends to infinity as \(M\to\infty\). When \(\mathbb ET^3<\infty\), asymptotic independence implies that the covariance of \(\Phi(0)\) and \(\Phi(t)\) tends to zero: truncate both at a fixed absolute level and then remove the truncation via Cauchy–Schwarz and their common square-integrable marginal. Hence
\[
\operatorname{Var}\left[t^{-1}\int_0^t f(X_s)ds\right]\sim \frac{2}{t^2}
\left[\frac{\mathbb ET^3}{\mathbb ET}\int_0^1 H(u)^2du-
\left(\frac{\mathbb ET^2}{\mathbb ET}\int_0^1 H(u)du\right)^2\right].
\]
The bracket is positive for non-a.e.-constant \(f\) since \(H\) is continuous, vanishes at both endpoints, and is not constant, and \(T^*>0\) is independent of \(U\).

For \(f(x)=x\), \(H(u)=Lu(1-u)/2\); the integrals of \(H\) and \(H^2\) are \(L/12\) and \(L^2/120\). Thus the limiting unscaled variance in the finite-third-moment case is \(L^2[\mathbb ET^3/(60\mathbb ET)-(\mathbb ET^2)^2/(72(\mathbb ET)^2)]\), equal to \(2L^2/(45\lambda^2)\) for an exponential duration of rate \(\lambda\).

## Verification and limits

The supplied `checker.py` contains rational checks for four polynomial observables and for the exponential example, plus a finite-window exponential-flight simulation. The renewal argument, not simulation, proves the weak limit, the moment threshold and the divergence statement. No universal heavy-tail divergence rate or all-exponent moment-convergence assertion is made. The proof concerns instantaneous fixed-distance ballistic resets, not waiting at the reset point or stochastic within-flight paths.

## Relationship to prior work

Das, Majumdar and Pal, [*Freezing transition and shock-like transients in ballistic random walks under threshold resetting*](https://arxiv.org/abs/2611.16733), establish the model and uniform stationary position law. *Universal boundary fluctuations and negative memory in ballistic threshold resetting* ([record](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-universal-boundary-fluctuations-and-negative-memory-in-ballistic--3fafd0c137ae)) states the exact endpoint identity, independent-copy endpoint limit and sharp variance coefficient in a finite-third-moment theorem. Its endpoint mixing argument itself uses only finite mean, and it notes possible infinite variance coefficients without a third moment. *Endpoint laws and quadratic variance suppression for ballistic threshold-reset averages* ([record](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-endpoint-laws-and-quadratic-variance-suppression-for-ballistic-t--b33291d37acb)) also treats endpoint laws for Gamma durations. The shared public date does not determine order. The focus here is the necessary-and-sufficient moment criterion at every positive exponent and the resulting inevitable finite-window variance divergence for nondegenerate observables when the third moment is infinite. The stationary distribution and convergence machinery come from standard renewal theory; related threshold-reset sluggish diffusion occupation results have stochastic within-cycle centered rewards, rather than the exact ballistic cancellation.
