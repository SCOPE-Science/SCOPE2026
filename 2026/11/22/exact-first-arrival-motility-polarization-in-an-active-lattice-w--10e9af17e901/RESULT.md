# Exact first-arrival motility polarization in an active lattice walker

## Finding
For a one-dimensional active nearest-neighbor lattice particle, the internal motility direction observed **at its first contact with a target** has an exact, distance-dependent polarization. Define
\[
\begin{aligned}
b&=\epsilon/D,\quad g=\gamma/D,\\
\rho&=\frac{1-b^2}{1+b^2+g+\sqrt{(g+2)(g+2b^2)}},\\
K&=\frac12\left(1+b\sqrt{\frac{g+2}{g+2b^2}}\right).
\end{aligned}
\]
For any integer target distance \(N\ge1\), the first-hit motility-state law is
\[
\boxed{\Pr(\sigma_{\tau_N}=+1)=K+\left(\frac12-K\right)\rho^N.}
\]
This is an unconditional probability, because the first hit occurs almost surely whenever \(\gamma>0\). For \(0<b<1\), \(0<\rho<1\), \(1/2<K<1\), and the arrival polarization strictly increases with target distance, to \(K\) at an exactly geometric rate. In particular, at fixed distance,
\[
\lim_{\gamma\to\infty}\Pr(\sigma_{\tau_N}=+1)=\frac{1+b}{2},
\]
whereas the unmarked position process becomes a symmetric nearest-neighbor walk in the same fast-tumbling limit. The motility mark at the stopping time retains a nontrivial local directional sampling bias.

## Assumptions and scope
Let \((X_t,\sigma_t)\) be a continuous-time Markov chain on \(\mathbb Z\times\{+1,-1\}\), with generator
\[
(\mathcal L f)(x,s)=(D+\epsilon s)[f(x+1,s)-f(x,s)]
+(D-\epsilon s)[f(x-1,s)-f(x,s)]
+\gamma[f(x,-s)-f(x,s)].
\]
Here \(D>0\), \(0\le\epsilon\le D\), \(\gamma>0\), \(X_0=0\), and \(\Pr(\sigma_0=\pm1)=1/2\). The first contact time is \(\tau_N=\inf\{t\ge0:X_t=N\}\) for a fixed integer \(N\ge1\). No resetting occurs, and the motility state is read at the contact instant (state changes and spatial jumps are not simultaneous with positive probability). Even at \(\epsilon=D\), the process is well defined. Distinguish this motility mark from the incoming *step direction*, which is necessarily rightward on first contact with a target to the right in one dimension.

More generally let \(u_s(n)=\Pr_{(N-n,s)}(\sigma_{\tau_N}=+1)\) for any integer \(n\ge0\). Both initial-state functions are explicit:
\[
 u_+(n)=K+(1-K)\rho^n,\qquad
 u_-(n)=K(1-\rho^n).
\]
In particular \(u_+(0)=1\) and \(u_-(0)=0\); the fair-start law is their arithmetic mean at \(n=N\).

## Proof
**Almost-sure contact.** For positive reversal rate, the process
\[
M_t=X_t+(\epsilon/\gamma)\sigma_t
\]
is a martingale: the positional drift is \(2\epsilon\sigma_t\), canceled by the internal-state generator acting on \((\epsilon/\gamma)\sigma_t\). Fix \(L>0\), stop at the first visit to \(-L\) or \(N\). That exit time is finite almost surely because the finite internal-state interval has a path to either boundary from every state, even when \(\epsilon=D\). Bounded optional stopping, with \(c=\epsilon/\gamma\), yields
\[
\Pr(\tau_{-L}<\tau_N)\le\frac{N+2c}{N+L}.
\]
The right side tends to zero as \(L\to\infty\); consequently \(\Pr(\tau_N<\infty)=1\). This also establishes uniqueness of a bounded harmonic solution with prescribed contact values: stop at the same two boundaries, and bound the unknown far-left contribution by its uniform norm times the displayed probability.

**Backward equations.** First-step conditioning for \(n\ge1\) gives
\[
\begin{aligned}
0={}&(D+\epsilon)u_+(n-1)+(D-\epsilon)u_+(n+1)
+\gamma u_-(n)-(2D+\gamma)u_+(n),\\
0={}&(D-\epsilon)u_-(n-1)+(D+\epsilon)u_-(n+1)
+\gamma u_+(n)-(2D+\gamma)u_-(n).
\end{aligned}
\]
The boundary conditions are \(u_+(0)=1\), \(u_-(0)=0\). A geometric mode \(u_s(n)=v_s z^n\) produces characteristic factor
\[
(z-1)^2\big[(D^2-\epsilon^2)z^2
-2(D^2+\epsilon^2+D\gamma)z+(D^2-\epsilon^2)\big].
\]
The single nonconstant decaying root is exactly \(\rho\) above; when \(\epsilon=D\), its continuous limiting value is zero. The ansatz
\[
 u_+(n)=K+(1-K)\rho^n,\qquad
 u_-(n)=K-K\rho^n
\]
satisfies the two boundary values. The symmetric equation for \(u_++u_-\) implies
\[
2K-1=b\frac{1+\rho}{1-\rho}
=b\sqrt{\frac{g+2}{g+2b^2}},
\]
and substitution into the antisymmetric equation confirms the decaying eigenmode. The resulting functions are bounded; by uniqueness from optional stopping they equal the hitting probabilities. The case \(b=0\) follows directly with \(K=1/2\), and \(b=1\) with \(K=1\), \(\rho=0\).

**Distance and tumbling limits.** For \(0<b<1\), the difference between successive fair-start polarizations is \((K-1/2)(1-\rho)\rho^N>0\). The limit as \(N\to\infty\) is \(K\). As \(g\to\infty\), \(\rho\to0\) and \(K\to(1+b)/2\). The internal Markov chain equilibrates on the fast time scale, so averaging its two conditional spatial jump rates gives a symmetric walk with right/left rates \(D\) on every fixed observation horizon. Nevertheless, observing the state *at an inward jump into the target* is event-biased, yielding the non-half limiting probability. In the opposite direction, for fixed \(0<b\le1\), \(K\to1\) and \(\rho\to(1-b)/(1+b)\) as \(g\downarrow0\), so the stated weak-tumbling limit follows. At exactly \(g=0\), the positive-oriented drift hits the positive target almost surely, while the negative-oriented drift does so with probability \(((1-b)/(1+b))^N\); therefore the total hit probability is only \([1+((1-b)/(1+b))^N]/2\), whereas the probability of a positive motility state at contact is \(1/2\). This explains the noncommuting zero-rate limit without assigning a motility mark to trajectories that never hit.

## Verification
The supplied standalone `checker.py` constructs the full two-component backward generator on a finite interval, reflecting at its far left boundary and absorbing at the positive target. It solves an independent sparse linear system for the hitting-state probability at many physically distinct parameters and target distances. For a far-left reflecting boundary, agreement with the infinite-half-line result is controlled by the exponentially small decaying mode; the chosen lower-boundary positions are sufficiently distant for the stated numerical tolerance. It also checks weak-/fast-tumbling limits and exact endpoints. To reproduce, run `python checker.py` with Python, NumPy, and SciPy. The deterministic checker is a diagnostic, not a substitute for the bounded-harmonic uniqueness argument.

## Relationship to prior work
Jose, Mandal, Barma and Ramola introduced the exact lattice motility model and derived position marginals and large-deviation properties. Jose subsequently derived **position-only** first-passage-time distributions and asymptotics for this model, including the important failure of a naive effective-diffusivity approximation. These established results are used as model context, not claimed here. The first-arrival **latent motility mark**, its exact spatial interpolation and its fast-tumbling limit are different observables. In particular a scalar first-passage-time transform does not by itself identify the joint contact polarity.

Marris and Giuggioli's correlated lattice walk uses a previous-displacement orientation, with directional first passage meaning the direction of entry, rather than an independent flipping motility state. These processes are not equivalent for generic \(0<b<1\). At successive spatial jump epochs in the present model, writing \(J_j\in\{+1,-1\}\) for the jump signs and \(c=D/(D+\gamma)\), the stationary correlations are \(\mathbb E[J_jJ_{j+k}]=b^2c^k\) for every \(k\ge1\). Thus
\[
\mathbb E[J_jJ_{j+2}]-\mathbb E[J_jJ_{j+1}]^2
=b^2(1-b^2)c^2>0.
\]
A symmetric one-step Markov direction process has equal two-step correlation and squared one-step correlation. This is a concrete obstruction to substituting that different motion model.

## Limitations
The result concerns the lattice and a single right-hand point target, with memory measured in the motility direction at the first arrival. No formula for the joint arrival-time/mark transform, finite windows, spatially dependent tumbling, non-Poisson clocks, or multiple targets is asserted. The fast-switching statement is about a fixed positive target distance and fixed finite observation horizons for unmarked position convergence; it is not a universal continuum-boundary result. The \(\gamma=0\) model has defective hitting and is explicitly excluded from the main formula. The exact result can be extracted from the two-state backward boundary-value problem; literature comparisons do not establish absolute publication priority.

## References
1. S. Jose, D. Mandal, M. Barma and K. Ramola, *Active Random Walks in One and Two Dimensions*, arXiv:2202.02995 (first public 7 February 2022), https://arxiv.org/abs/2202.02995.
2. S. Jose, *First passage statistics of active random walks on one and two dimensional lattices*, arXiv:2206.04562 (first public 9 June 2022), https://arxiv.org/abs/2206.04562.
3. D. Marris and L. Giuggioli, *Persistent and anti-Persistent Motion in Bounded and Unbounded Space: Resolution of the First-Passage Problem*, arXiv:2404.13360 (first public 20 April 2024), https://arxiv.org/abs/2404.13360.
4. H. Larralde, *First-passage probabilities and mean number of sites visited by a persistent random walker in one- and two-dimensional lattices*, Physical Review E 102, 062129 (2020), https://doi.org/10.1103/PhysRevE.102.062129. Its full text was not accessible in the present literature comparison, so potential overlap is a residual priority risk.
