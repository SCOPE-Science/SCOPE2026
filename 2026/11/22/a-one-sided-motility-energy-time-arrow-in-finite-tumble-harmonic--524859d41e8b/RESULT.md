# A one-sided motility–energy time arrow in finite-tumble harmonic transport

## Finding

In a harmonic trap, a particle that alternates between runs and finite-duration tumbles has a larger stationary covariance between present motor activity and future squared displacement than in the reverse time order. The difference is strictly positive at every positive lag and for all positive switching rates, and is unaffected by independent thermal Brownian noise. It measures time asymmetry of the joint motor and position observations, not a causal effect inferred from a covariance.

Let \(A(\tau)=\operatorname{Cov}(R_0,U_\tau^2)-\operatorname{Cov}(U_0^2,R_\tau)\), with the dimensionless stationary model defined below. For every \(\tau>0\), \(A(\tau)>0\). For \(s\ge0\),

\[\widehat A(s)=\int_0^\infty e^{-s\tau}A(\tau)\,d\tau=\frac{2ac(2s+3a+c+4)}{(a+1)(a+c)(a+c+2)(s+2)(s+a+c)(s+a+1)}.\]

The exact integrated signal and short-lag slope are

\[\int_0^\infty A(\tau)\,d\tau=\frac{ac(3a+c+4)}{(a+1)^2(a+c)^2(a+c+2)},\qquad A'(0+)=\frac{4ac}{(a+1)(a+c)(a+c+2)}.\]

For the equal-rate, trap-normalized example \(a=c=1\),

\[A(\tau)=\frac{\tau(1+\tau)}4e^{-2\tau},\]

whose unique maximum occurs at \(\tau=1/\sqrt2\).

## Assumptions and scope

Fix physical trap rate \(\kappa>0\), active speed \(v>0\), run-to-tumble switching rate \(\gamma_R>0\), tumble-to-run switching rate \(\gamma_T>0\), and independent thermal diffusion \(D\ge0\). The internal motor takes values \(S\in\{-1,0,+1\}\): each \(\pm1\) jumps to zero at rate \(\gamma_R\), and zero jumps to each sign at rate \(\gamma_T/2\). Each outgoing run direction is therefore redrawn fairly and independently; no orientation is retained through a tumble. The physical position solves

\[dX_t=(-\kappa X_t+vS_t)\,dt+\sqrt{2D}\,dW_t.\]

The irreducible motor chain is taken stationary on the whole time axis, independently of the two-sided Brownian motion. The stable linear filter \(X_t=v\int_{-\infty}^t e^{-\kappa(t-u)}S_u\,du+\sqrt{2D}\int_{-\infty}^t e^{-\kappa(t-u)}dW_u\) supplies the unique joint stationary solution and has all moments finite. Rescale to \(\tau=\kappa t\), \(U_\tau=\kappa X_{\tau/\kappa}/v\), \(R_\tau=S_{\tau/\kappa}^2\), \(a=\gamma_R/\kappa\), \(c=\gamma_T/\kappa\), and \(\delta=D\kappa/v^2\). Thus \(dU_\tau=(-U_\tau+S_\tau)\,d\tau+\sqrt{2\delta}\,dB_\tau\); the same letter \(S\) denotes the rescaled motor chain. All statements are for real \(a,c>0\), \(\delta\ge0\), and finite \(\tau\ge0\).

## Proof

Write \(k=a+c\), \(\ell=a+1\), \(Y=US\), and \(Z=U^2\). The joint Markov generator closes exactly on these functions:

\[\mathcal LR=c-kR,\qquad \mathcal LY=-\ell Y+R,\qquad \mathcal LZ=-2Z+2Y+2\delta.\]

The term \(2\delta\) is constant and disappears after centering. These identities hold because \(S=0\) in the tumble state, and the average new run sign is zero. Stationarity gives \(\mathbb ER=c/k\) and \(\mathbb EY=c/(k\ell)\). Since \(RY=Y\),

\[C_{RR}=\operatorname{Var}(R)=\frac{ac}{k^2},\qquad C_{RY}=\operatorname{Cov}(R,Y)=\frac{ac}{k^2\ell}.\]

To compute the third initial covariance, use \(\mathcal L(RZ)=-(k+2)RZ+2Y+cZ+2\delta R\). Stationarity and \(\mathbb EZ=\mathbb EY+\delta\) imply

\[C_{RZ}=\operatorname{Cov}(R,Z)=\frac{2ac}{\ell k^2(k+2)}.\]

For \(t\ge0\), let \(f_R(t)=\operatorname{Cov}(R_0,R_t)\), \(f_Y(t)=\operatorname{Cov}(R_0,Y_t)\), and \(f_Z(t)=\operatorname{Cov}(R_0,Z_t)\). The generator identities imply the triangular initial-value system

\[f_R'=-kf_R,\qquad f_Y'=-\ell f_Y+f_R,\qquad f_Z'=-2f_Z+2f_Y,\]

with initial data \(C_{RR},C_{RY},C_{RZ}\), respectively. Hence their Laplace transforms satisfy

\[\widehat f_Z(s)=\frac{C_{RZ}+2C_{RY}/(s+\ell)+2C_{RR}/[(s+\ell)(s+k)]}{s+2}.\]

Conversely, the autonomous two-state activity indicator has \(\mathbb E[R_t-\mathbb ER\mid R_0]=e^{-kt}(R_0-\mathbb ER)\), so

\[\operatorname{Cov}(Z_0,R_t)=C_{RZ}e^{-kt}.\]

Subtracting its Laplace transform from \(\widehat f_Z\), followed by exact factorization, yields

\[\widehat A(s)=\frac{2ac}{\ell k(k+2)}\left[\frac{2}{(s+2)(s+k)}+\frac{k+2}{(s+2)(s+k)(s+\ell)}\right].\]

Let \(g_q(t)=e^{-qt}\mathbf1_{\{t\ge0\}}\) and let \(*\) denote convolution on \([0,\infty)\). Inverting this last expression gives the **manifestly positive kernel**

\[A(t)=\frac{2ac}{\ell k(k+2)}\left[2(g_2*g_k)(t)+(k+2)(g_2*g_k*g_\ell)(t)\right].\]

Each exponential is strictly positive on nonnegative arguments, and both convolutions are strictly positive for every \(t>0\). The proof does not divide by rate differences and therefore also covers \(k=2\), \(k=\ell\), or \(\ell=2\). Putting \(s=0\) gives the integrated formula; the \(s\to\infty\) leading coefficient yields the short-lag derivative. At \(a=c=1\), inverse Laplace transformation gives the displayed elementary profile and differentiation gives its unique maximum.

The three displayed denominator factors need not give three distinct poles. Besides coincident rates, there is a cancellation when \(c=a+4\): the numerator factor \(2s+2\ell+k+2\) then equals \(2(s+k)\). Thus on this line the time signal simplifies to \(4ac(g_2*g_\ell)(t)/[\ell k(k+2)]\). The factors \(s+2\) and \(s+\ell\) never cancel for positive \(a,c\), since their corresponding numerator values are \(3a+c\) and \(k+2\), respectively. Neither cancellation nor coincidence alters the strict sign.

Finally, the active and thermal components of the stationary linear filter are independent, and the thermal part is a centered Gaussian. Because \(R\) depends only on the active motor, both mixed covariances involving \(U^2\) are unchanged by adding that independent Gaussian part. Equivalently, the centered generator system above contains no \(\delta\). Thus the theorem holds for all \(\delta\ge0\).

## Verification

The accompanying `check.py` uses Python, SymPy, NumPy, and SciPy. It checks the exact rational transform, positive-kernel identities, integrated signal and short-lag derivative symbolically, and compares matrix-semigroup evaluations with positive-convolution integrals at 30 rate/lag combinations, including repeated eigenvalues. Its event-driven Monte Carlo check uses 30,000 trajectories at \(a=c=1\), zero thermal diffusion, and lag one. The motor starts in stationarity, but the position starts at zero and is evolved for 18 dimensionless time units before the first observation. This is a finite burn-in approximation to stationary sampling, not exact joint stationary initialization. These checks supplement the analytic proof.

## Relationship to prior work

The finite-duration run/tumble Markov model and its conditional stationary densities are given by Sun, Ye and Chen [1], whose Section IV and summary treat conditional distributions rather than the stationary forward-minus-backward mixed covariance. Sun, Ye and Podgornik [2] derive stationary moments and time-Laplace transforms of transient positional moments, but do not state the two-time motor-to-energy versus energy-to-motor sign ordering. Basu and colleagues [3] determine a three-state trapped motor stationary position law for an equal-rate specialization; their spatial shape result does not imply the claimed strict all-lag ordering. The contribution here is the exact stationary mixed-lag law, including its strictly positive convolution at every positive lag and invariance under independent additive thermal diffusion. A fourth-order position-only time arrow in the same finite-tumble dynamics [4] involves different observables and can change sign with lag; it does not give this mixed covariance.

## Limitations

This is a one-dimensional, linear harmonic trap with symmetric independent orientation redraw and exponential run/tumble durations. The sign ordering is for a *jointly observed motor-state indicator and squared position*; it does not assert a position-only arrow of time, a universal entropy-production rate, a result for heavy-tailed pauses, or robustness under motor-dependent translational noise. Strictness requires both switching rates and active speed positive and a strictly positive lag. Scientific priority remains qualified by potentially unindexed equivalent work.

## References

[1] A. Sun, F. Ye, J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961 (first submitted 18 October 2026), https://arxiv.org/abs/2610.24961.
[2] A. Sun, F. Ye, R. Podgornik, *Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578 (2024), https://arxiv.org/abs/2409.00578.
[3] U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (2019), https://arxiv.org/abs/1910.10083.
[4] *A sharp time-arrow reversal diagram for a harmonically trapped finite-tumble particle*, Resultary public record (2026), https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-sharp-time-arrow-reversal-diagram-for-a-harmonically-trapped-f--dc843e2cf037.
