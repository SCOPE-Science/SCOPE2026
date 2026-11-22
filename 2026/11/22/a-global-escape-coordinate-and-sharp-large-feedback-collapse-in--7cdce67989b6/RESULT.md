# A global escape coordinate and sharp large-feedback collapse in a three-dimensional sine map

## Finding

For the real three-dimensional map
\[
F(x,y,z)=\bigl(y,\sin z,\alpha+\beta x+\gamma y-\delta\sin z+\mu z\bigr),
\]
put \(B=|\beta|+|\gamma|+|\delta|\). If \(\mu>1+B\), there is a *global continuous escape coordinate*
\[
H(x,y,z)=\lim_{n\to\infty}\mu^{-n}\pi_zF^n(x,y,z)
\]
with \(H\circ F=\mu H\). For each fixed \((x,y)\), the map \(z\mapsto H(x,y,z)\) is a strictly increasing homeomorphism of \(\mathbb R\) onto itself. Thus
\[
\Psi(x,y,z)=(x,y,H(x,y,z))
\]
is a global homeomorphism conjugating \(F\) to a triangular skew map whose third coordinate is exactly multiplied by \(\mu\) at every step.

The zero set \(H^{-1}(0)\) is a smooth invariant graph \(z=\phi(x,y)\) over the entire real plane. Every orbit on it converges exponentially to the unique equilibrium, whereas every orbit off it escapes with the sign of \(H\) and has the sharp expansion law
\[
\pi_zF^n(x,y,z)=\mu^nH(x,y,z)+O(1).
\]
For every initial state and every \(n\ge2\), the error is bounded in absolute value by \((|\alpha|+B)/(\mu-1)\), independently of its initial coordinates. The equilibrium is the only compact, fully invariant nonempty set and the only invariant Borel probability is its point mass. The constant \(1+B\) is optimal as a coefficient-uniform strict large-feedback bound: at every \(1<\mu<1+B\) a coefficient choice with this prescribed \(B>0\) has at least three equilibria.

## Assumptions and scope

The state space is \(\mathbb R^3\); \(\alpha,\beta,\gamma,\delta\) are arbitrary real constants; \(\mu>1+|\beta|+|\gamma|+|\delta|\). Iteration means the full, unwrapped real recurrence, not a circle quotient. An invariant compact set here means a nonempty compact \(K\) satisfying \(F(K)=K\), not merely \(F(K)\subseteq K\). An invariant Borel probability is a countably additive probability on \(\mathbb R^3\) satisfying \(F_*\nu=\nu\).

Define \((x_n,y_n,z_n)=F^n(x_0,y_0,z_0)\), and \(c_n=\alpha+\beta x_n+\gamma y_n-\delta\sin z_n\). For \(n\ge2\), \(x_n=\sin z_{n-2}\) and \(y_n=\sin z_{n-1}\), so \(|c_n|\le |\alpha|+B\).

## Proof

**1. Global escape coordinate.** Since \(z_{n+1}=\mu z_n+c_n\), iteration of the variation-of-constants identity gives
\[
\mu^{-n}z_n=z_0+\sum_{j=0}^{n-1}\mu^{-j-1}c_j.
\]
The first two \(c_j\) are finite and all later terms are uniformly bounded. Therefore the series converges for every initial state, defining \(H\). For \(n\ge2\),
\[
|z_n-\mu^nH|\le \sum_{j=n}^\infty\mu^{n-j-1}(|\alpha|+B)
=\frac{|\alpha|+B}{\mu-1}.
\]
The convergence \(\mu^{-n}z_n\to H\) is uniform on the *entire* state space for \(n\ge2\), as the tail bound after scaling is independent of the initial state. Thus \(H\) is continuous. Shifting the orbit gives \(H(F(P))=\mu H(P)\).

**2. Strict fiber order.** Fix \(x_0,y_0\) and compare two solutions with initial \(z'_0>z_0\). Let \(e_n=z'_n-z_n\) and \(\lambda=\mu-B>1\). At \(n=0\), \(e_1\ge(\mu-|\delta|)e_0>0\). At \(n=1\), using the identical initial \(y_0\),
\[
e_2\ge(\mu-|\delta|)e_1-|\gamma|e_0\ge\lambda e_1>0.
\]
For \(n\ge2\), if \(e_n\ge e_{n-1}\ge e_{n-2}>0\), the sine function's unit Lipschitz bound yields
\[
e_{n+1}\ge\mu e_n-|\delta|e_n-|\gamma|e_{n-1}-|\beta|e_{n-2}
\ge\lambda e_n.
\]
Consequently \(e_n\ge\lambda^ne_0\), and the order never reverses. Since \(\mu^{-n}e_n\to H(x_0,y_0,z'_0)-H(x_0,y_0,z_0)\), the limit is nonnegative. If it were zero, the uniform \(O(1)\) remainder in Step 1 would imply bounded \(e_n\), contrary to exponential growth. Hence it is strictly positive. For fixed \(x_0,y_0\), the full series satisfies
\[
|H(x_0,y_0,z_0)-z_0|\le\frac{C(x_0,y_0)}{\mu-1},
\]
where
\[
C(x,y)=|\alpha|+|\beta|\max(1,|x|,|y|)
+|\gamma|\max(1,|y|)+|\delta|.
\]
Thus each fiber map is continuous, strictly increasing, and tends to \(\pm\infty\) at its respective ends. It is a homeomorphism. Its inverse varies continuously with \((x,y)\), using uniform bounds on compact base sets and strict monotonicity. Therefore \(\Psi\) is a homeomorphism and
\[
\Psi F\Psi^{-1}(u,v,w)
=\bigl(v,\sin\psi(u,v,w),\mu w\bigr),
\]
with \(\psi(u,v,\cdot)\) the inverse of \(z\mapsto H(u,v,z)\).

**3. Smooth separating graph and convergence.** There is exactly one root \(\phi(x,y)\) of \(H(x,y,z)=0\) in each vertical fiber. The error bound from Step 1 shows that \(H=0\) is equivalent to boundedness of the complete forward orbit. For smoothness, fix \((x_0,y_0)\) and solve for the bounded scalar sequence \(z=(z_n)_{n\ge0}\) on \(\ell^\infty(\mathbb N_0)\). Define the backward fixed-point operator \(T_{x_0,y_0}\) by
\[
(Tz)_n=\frac{z_{n+1}-c_n(z;x_0,y_0)}{\mu},
\]
where
\[
\begin{aligned}
c_0&=\alpha+\beta x_0+\gamma y_0-\delta\sin z_0,\\
c_1&=\alpha+\beta y_0+\gamma\sin z_0-\delta\sin z_1,\\
c_n&=\alpha+\beta\sin z_{n-2}+\gamma\sin z_{n-1}-\delta\sin z_n\quad(n\ge2).
\end{aligned}
\]
This operator is a contraction with Lipschitz constant at most \((1+B)/\mu<1\), uniformly in its arguments. Its unique fixed point is the sole bounded forward scalar sequence for the prescribed \((x_0,y_0)\), and its first term is \(\phi(x_0,y_0)\). The Banach-space implicit function theorem, applied to the smooth bounded-derivative sine substitution on \(\ell^\infty\), shows that \(\phi\) is \(C^\infty\). In particular,
\[
|\phi(x,y)-\phi(x',y')|\le
\frac{\max\{|\beta||x-x'|+|\gamma||y-y'|,\ |\beta||y-y'|\}}{\mu-1-B}.
\]
The graph is invariant because every tail of a bounded orbit remains bounded.

A unique fixed point exists: writing it as \((\sin s,\sin s,s)\), its scalar equation is
\[
(\mu-1)s+(\beta+\gamma-\delta)\sin s+\alpha=0,
\]
whose derivative is at least \(\mu-1-B>0\). To see that all graph orbits converge to it, the omega-limit set of any bounded forward orbit is compact and satisfies \(F(\omega)=\omega\), so each point in it admits a bounded bilateral trajectory. For a bounded bilateral trajectory the coordinate \(z_n\) is a fixed point in \(\ell^\infty(\mathbb Z)\) of
\[
(\mathcal Tz)_n=\mu^{-1}\bigl(z_{n+1}-\alpha-\beta\sin z_{n-2}
-\gamma\sin z_{n-1}+\delta\sin z_n\bigr).
\]
This is again a contraction of factor \((1+B)/\mu<1\). Its unique fixed sequence is the constant equilibrium sequence. Therefore every bounded orbit converges to the equilibrium.

For exponential convergence, put \(c=\cos s\). The equilibrium Jacobian has polynomial
\[
P(\xi)=\xi^3-(\mu-\delta c)\xi^2-\gamma c\xi-\beta c.
\]
Along the homotopy replacing \((\beta,\gamma,\delta)\) by \(t(\beta,\gamma,\delta)\), \(0\le t\le1\), no root can lie on \(|\xi|=1\): a unit root would imply \(\mu\le1+tB\), impossible. At \(t=0\), the spectrum is \(\{0,0,\mu\}\). Thus the equilibrium is hyperbolic with two stable and one unstable eigenvalues. Every convergent graph orbit eventually lies in its local stable manifold and hence converges exponentially.

**4. Escape, recurrence and measures.** If \(H\ne0\), Step 1 gives \(z_n=\mu^nH+O(1)\), so \(z_n\to+\infty\) for \(H>0\) and \(z_n\to-\infty\) for \(H<0\). The first two coordinates stay bounded after at most two iterates. A compact set satisfying \(F(K)=K\) gives a bounded bilateral orbit through each of its points, so the bilateral uniqueness above forces \(K\) to be the singleton equilibrium. Every nonfixed point is either escaping or converges to the equilibrium, and therefore cannot be recurrent. By Poincaré recurrence an invariant Borel probability must be supported on recurrent points; it is necessarily the equilibrium point mass.

**5. Sharpness of the uniform gain.** Choose \(\alpha=\beta=\gamma=0\) and \(\delta=B>0\). For any \(1<\mu<1+B\), equilibria satisfy \((\mu-1)s=B\sin s\). Besides \(s=0\), this equation has a strictly positive solution in \((0,\pi)\) and its negative: near zero the right side has the larger slope and at \(s=\pi\) the left side is positive. Thus the compact-recurrence collapse fails below the stated coefficient-uniform threshold. At \(\mu=1+B\), the origin in this witness has a unit multiplier, showing why strict hyperbolicity cannot extend uniformly through equality. This sharpness is uniform over coefficient choices; the sufficient bound is not claimed to be necessary for an individual fixed coefficient tuple.

## Verification

The accompanying `check.py` independently recomputes the characteristic polynomial and fixed-point derivative symbolically; it also tests the phase order, the uniform scaled-escape remainder, the exceptional bounded fiber, and the three-equilibrium sharpness witness on representative real parameters. Run `python check.py` with Python 3, SymPy, and the standard library. The checker prints `VERIFY_OK` on the tested identities and diagnostics. These finite diagnostics are supplementary: the assertions for every initial state, all iterates and all parameters follow from the inequalities and contraction arguments above, not from computation.

## Relationship to prior work

Rajagopal, Kanagaraj, Volos and Karthikeyan (2023), Section 2, introduce the self-feedback 3D sine map and investigate periodic, chaotic and hyperchaotic behavior numerically as feedback varies. Their Section 3 and associated diagrams do not provide a global feedback threshold, an all-state escape coordinate or a rigorous classification of compact recurrence for strong feedback. Earlier sine-delay maps without self-feedback are related but do not directly imply the strong-feedback escape conjugacy.

Chen and Li (2022 online; 2023 journal volume) establish general stable-manifold and bounded-complete-trajectory theory for difference equations with delay. That broad invariant-manifold framework is prior coverage for qualitative stable-set existence and convergence, and neither general manifold existence nor its standard contraction proof is claimed as the new contribution. The precise all-state scalar escape coordinate, its strict fiber homeomorphism, uniform error bound, exact sign partition, and coefficient-uniform sharp witness for this specified sinusoidal map are the assessed model-specific statement. The full Chen–Li proof was not accessible for complete comparison; equivalent general global-linearization corollaries remain a residual originality risk.

## Limitations

The large-feedback bound is sufficient, not necessary for every fixed coefficient choice, and the endpoint is not classified in general. The topological skew product need not be differentiably conjugate; only continuity of the escape coordinate and smoothness of its zero graph are established. The theorem does not classify the low-feedback chaotic regime, cryptographic randomness or higher-dimensional network couplings. Prior-work comparisons do not constitute proof of worldwide novelty, and no independent mathematical audit has been performed.

## References

1. K. Rajagopal, S. Kanagaraj, C. Volos and A. Karthikeyan, *Influence of Parametric Symmetry on the Dynamics of 3D Sinusoidal Discrete Systems*, Symmetry 15 (2023), 780, published March 23, 2023. https://doi.org/10.3390/sym15040780
2. F. Chen and D. Li, *On the stable manifolds of difference equations with infinite delay*, Discrete and Continuous Dynamical Systems B 28 (2023), 3487–3506, first published November 23, 2022. https://doi.org/10.3934/dcdsb.2022227
