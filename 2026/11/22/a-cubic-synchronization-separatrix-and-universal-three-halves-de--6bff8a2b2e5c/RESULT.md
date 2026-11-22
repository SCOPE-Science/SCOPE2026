# A cubic synchronization separatrix and universal three-halves decay in a sine-memory map

## Finding

In the three-dimensional discrete cosine–memristor map of Peng et al. [1], the zero-input-gain slice admits an exact reduction to a two-dimensional sine-memory recurrence. At the critical coupling, a unique nonlinear threshold separates initial data that remain strictly below the maximally neutral memory phase from those that reach it. The critical orbit approaches that phase with a universal inverse-square clock and has a cubic, rather than linear, threshold opening.

Fix \(k=1/10\), \(\mu=0\), \(h=1/2\), and any positive amplification parameter \(\gamma\), as in the parameter domain of [1]. Put \(q=k/\log 3\). On the invariant plane \(x+y=2q\), write \(u=x-y\) and \(w=\pi/2-z\). For each \(w_0\in(0,1)\), there exists exactly one \(U(w_0)\in(0,w_0)\) with the following properties, for initial data \(u_0\in(0,w_0)\):

1. If \(u_0<U(w_0)\), then \(w_n\) remains positive and converges to a strictly positive limit, while \(u_n\) converges exponentially to zero.
2. If \(u_0>U(w_0)\), then the orbit reaches \(w_n\le 0\) in finitely many iterates (equivalently, its memory phase reaches or crosses \(\pi/2\)). No assertion is made about its later orbit.
3. If \(u_0=U(w_0)\), then \(w_n>0\) for every finite \(n\), \(w_n\to0\), and
\[
\lim_{n\to\infty}n w_n^2=3,\qquad
\lim_{n\to\infty}n^{3/2}u_n=\frac{\sqrt3}{2}.
\]

The unique threshold has the sharp small-phase expansion
\[
U(w)=\frac{w^3}{6}+\frac{w^5}{120}+O(w^7)
\quad(w\downarrow0).
\]
Thus the source map has a genuine algebraically convergent critical synchronization orbit even though nearby noncrossing orbits synchronize exponentially.

## Assumptions and scope

The three-dimensional map is, on its real domain,
\[
\begin{aligned}
x_{n+1}&=P_{\mu,\gamma}(x_n)+h\sin(z_n)(x_n-y_n),\\
y_{n+1}&=P_{\mu,\gamma}(y_n)-h\sin(z_n)(x_n-y_n),\\
z_{n+1}&=z_n+x_n-y_n,\\
P_{\mu,\gamma}(t)&=\frac{k\cos(4\pi\mu\gamma t(1-t))}
{\log(3-4\mu t(1-t))}.
\end{aligned}
\]
On \(\mu=0\), the denominator is \(\log3>0\) for all real states and \(P_{0,\gamma}\equiv q\). The sum of the first two updated coordinates is then exactly \(2q\); hence the plane \(x+y=2q\) is invariant, and every initial state enters it after one iteration. The theorem concerns the stated positive-deviation sector of that plane, not arbitrary initial conditions or positive \(\mu\).

For \(h=1/2\), the two remaining coordinates obey the exact recurrence
\[
\boxed{\quad w_{n+1}=w_n-u_n,\qquad u_{n+1}=u_n\cos w_n.\quad}
\]
The interval \(0<w_0<1\) is chosen so that \(\cos w>0\) and is strictly decreasing throughout any pre-crossing trajectory. Initial \(u_0\) is strictly between zero and \(w_0\). The variable \(u\) is the signed difference \(x-y\), not a norm or a rounded quantity. Iteration time \(n\) is a nonnegative integer.

## Proof

**1. Order and an exact threshold.** While \(w_n>0\), the recurrence gives \(0<u_{n+1}<u_n\) and \(w_{n+1}<w_n\). Given two initial values \(u_0<v_0\) with the same \(w_0\), as long as both phase deficits remain positive, induction gives \(u_n<v_n\) and \(w_n(u_0)>w_n(v_0)\). Indeed, \(0<w_n(v_0)<w_n(u_0)<1\) implies \(\cos w_n(v_0)>\cos w_n(u_0)\), preserving the strict order of the amplitudes.

Let \(C\) be the set of initial amplitudes in \((0,w_0)\) whose trajectories eventually have \(w_n<0\). It is upward closed by this comparison and relatively open by finite-iterate continuity. It is nonempty: initial amplitudes sufficiently near \(w_0\) cross in at most two steps. Its complement contains a nonempty open interval near zero: with \(\theta=w_0/2\), as long as \(w_n\ge\theta\) one has \(u_n\le u_0(\cos\theta)^n\); if \(u_0<\theta(1-\cos\theta)\), their total sum is below \(\theta\), so \(w_n\) can never descend to \(\theta\). Accordingly \(U(w_0):=\inf C\) belongs to \((0,w_0)\). Since \(C\) is open, \(U(w_0)\notin C\), and its trajectory stays strictly above zero (a zero phase deficit would produce a negative deficit at the next step).

**2. The critical orbit tends to zero.** On the threshold trajectory \(w_n\downarrow\ell\ge0\), and \(\sum_{j\ge n}u_j=w_n-\ell\), so \(u_n\downarrow0\). If \(\ell>0\), choose \(N\) so large that \(u_N\) is small compared with \(\ell(1-\cos(\ell/2))\). The finite map to time \(N\) varies continuously with \(u_0\); on a neighborhood of the threshold initial condition, \(w_N\) remains above \(3\ell/4\), and the ensuing geometric upper bound on \(\sum_{j\ge N}u_j\) keeps every later \(w_j\) above \(\ell/2\). This gives a neighborhood of \(U(w_0)\) disjoint from \(C\), contradicting its definition as a boundary point. Hence \(\ell=0\). For any smaller initial amplitude, the order comparison makes its phase deficit exceed the critical deficit by at least \(U(w_0)-u_0\) from time one onward, so its limit is strictly positive; its amplitude consequently decays exponentially. Any larger initial amplitude belongs to \(C\), by upward closure and the definition of the infimum. This completes the trichotomy and uniqueness.

**3. Integral comparison on the critical orbit.** Define \(f(w)=1-\cos w\) and \(I(w)=\int_0^w f(s)\,ds=w-\sin w\). Along a critical orbit, \(w_n-w_{n+1}=u_n\) and \(u_n-u_{n+1}=u_n f(w_n)\). Summing over all future iterates gives the exact right-endpoint Riemann sum
\[
u_n=\sum_{j=n}^{\infty}(w_j-w_{j+1})f(w_j).
\]
Because \(f\) increases on \([0,1]\), this sum is at least \(I(w_n)\). Each right-endpoint rectangle exceeds its integral by at most \(\tfrac12\sin(w_n)u_j^2\). Since \(\sum_{j\ge n}u_j=w_n\), \(u_j\le u_n\), and \(\sin w_n\le w_n\),
\[
0\le u_n-I(w_n)\le \tfrac12 u_n w_n^2.
\]
Therefore, for the unique threshold function, at every \(w\in(0,1)\),
\[
\boxed{\quad w-\sin w\ \le U(w)\ \le
\frac{w-\sin w}{1-w^2/2}.\quad}
\]
In particular \(U(w)=w^3/6+O(w^5)\), uniformly as \(w\downarrow0\).

**4. Quintic opening.** Write \(E_n=u_n-I(w_n)\). Taylor expansion on each interval \([w_{j+1},w_j]\), with uniformly bounded derivatives on \([0,1]\), yields
\[
E_n=\frac12\sum_{j\ge n}\sin(w_j)u_j^2
+O\left(\sum_{j\ge n}u_j^3\right).
\]
The cubic estimate just proved gives \(u_j=\tfrac16 w_j^3+O(w_j^5)\), hence \(\sin(w_j)u_j=\tfrac16w_j^4+O(w_j^6)\). Moreover \(\sum_{j\ge n}u_j^3\le u_n^2w_n=O(w_n^7)\), and the Riemann-sum comparison for \(t^4\) gives \(\sum_{j\ge n}w_j^4u_j=w_n^5/5+O(w_n^7)\). It follows that \(E_n=w_n^5/60+O(w_n^7)\). Since \(I(w)=w^3/6-w^5/120+O(w^7)\), taking \(n=0\) proves
\[
U(w)=\frac16w^3+\frac1{120}w^5+O(w^7).
\]

**5. The universal decay clock.** On the critical orbit \(u_n/w_n\to0\) by the cubic estimate. Thus
\[
\frac1{w_{n+1}^2}-\frac1{w_n^2}
=\frac{2w_nu_n-u_n^2}{w_n^2(w_n-u_n)^2}
\longrightarrow\frac13.
\]
The Cesàro average of these increments gives \(w_n^{-2}/n\to1/3\). Consequently \(w_n\sim\sqrt{3/n}\), and substituting into \(u_n\sim w_n^3/6\) yields \(u_n\sim (\sqrt3/2)n^{-3/2}\). On the invariant plane the original coordinates are \(x_n=q+u_n/2\), \(y_n=q-u_n/2\), and \(z_n=\pi/2-w_n\), completing the claimed synchronization asymptotics.

## Verification

The proof above is analytic and does not rely on a numerical cutoff. The standalone Python 3 file `check.py` evaluates the exact reduction and its local algebra, tests selected finite crossing/nocrossing orbits, and produces high-iteration diagnostics for a ninth-order approximation to the threshold curve. Run it from the same directory using `python3 check.py`. These diagnostics corroborate but do not certify the infinite-time theorem. The inequalities in Step 3 and the limiting increment in Step 5 are the rigorous certificates of the asymptotic claim.

## Relationship to prior work

Peng et al. [1, Section 2, equation (3); Section 3] introduce this precise cosine–memristor map and investigate equilibrium spectra, simulations, bifurcations and basin patterns. Their paper does not supply the global one-sided threshold \(U\), the fifth-order discrete correction, or the nonlinear critical convergence law in this zero-input-gain slice. The results here do not imply the reported chaotic or hyperchaotic behavior at positive input gain.

Earlier mathematical work on parabolic dynamics and neutral synchronization provides conceptual background for algebraic relaxation, but the proof here is self-contained and identifies the exact one-sided basin boundary in this specific real recurrence. A previously recorded result on the same map concerns the high-amplification limit at fixed strictly positive \(\mu\) and equilibrium-line root counts; its parameter assumptions and claims do not imply the zero-gain separatrix theorem.

## Limitations

The result is confined to \(\mu=0\), \(h=1/2\), the invariant plane \(x+y=2q\), and positive initial deviations \(0<u_0<w_0<1\). The crossing alternative only identifies the first passage of \(z_n\) through the phase \(\pi/2\), not its subsequent global fate. The analytic theorem does not address finite-precision hardware, cryptographic security, or chaotic attractors at positive \(\mu\). There has been no independent mathematical validation; publication priority beyond the searched and inspected literature remains uncertain.

## References

[1] S. Peng, H. Shi, R. Li, Q. Xiang, S. Dai, Y. Li, “Simulink Modeling and Analysis of a Three-Dimensional Discrete Memristor Map,” *Symmetry* **16** (2024), 990, first public 2024-08-05, https://doi.org/10.3390/sym16080990 (especially equations (1)–(7) and Sections 2–3).

[2] M. Astorg and L. Boc Thaler, “Dynamics of skew-products tangent to the identity,” arXiv:2204.02644 (2022), https://arxiv.org/abs/2204.02644. Background only: holomorphic skew-product theory with different hypotheses; no claim of covering the present real global threshold.
