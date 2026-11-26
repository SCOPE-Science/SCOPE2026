# Hidden translation and sharp leafwise pitchfork in a three-dimensional sine map

## Finding

Consider the real map of Rajagopal, Kanagaraj, Volos and Karthikeyan [1],
\[
F(x,y,z)=\bigl(y,\sin z,\alpha+\beta x+\gamma y-\delta\sin z+\mu z\bigr).
\]
Assume \(\mu=1\), \(\delta=\beta+\gamma\), \(\beta>0\), and \(\gamma\ge0\). Put \(s=\beta+\delta\) and \(W=z+\beta x+\delta y\). Then \(W\circ F=W+\alpha\). If \(\alpha\ne0\), every orbit satisfies \(z_n/n\to\alpha\), and there is no invariant Borel probability on \(\mathbb R^3\).

If \(0<s<1\), the circle skew product with phase \(\theta=W\bmod 2\pi\) has a unique continuous invariant graph \(h_\alpha=(X_\alpha,Y_\alpha):\mathbb R/(2\pi\mathbb Z)\to[-1,1]^2\). For every initial state,
\[
\|(x_n,y_n)-h_\alpha(\theta_n)\|_\infty
\le s^{\lfloor n/2\rfloor}\|(x_0,y_0)-h_\alpha(\theta_0)\|_\infty,
\qquad \theta_n= W(x_0,y_0,z_0)+n\alpha\pmod{2\pi}.
\]
For irrational \(\alpha/(2\pi)\), the empirical distributions of the bounded-coordinate pair converge weakly to \((h_\alpha)_*m\) for every initial state, where \(m\) is normalized Haar measure on the circle. The two coordinate means coincide, with
\[
\left|\int Y_\alpha\,dm-\frac{\beta\sin(2\alpha)+\delta\sin\alpha}{2}\right|\le \frac32s^2.
\]
If \(\alpha=0\) and \(s<1\), each invariant plane \(W=w\) has exactly one equilibrium, attracting every trajectory in that plane. The invariant Borel probabilities are precisely the mixtures of the equilibrium point masses.

The threshold \(s<1\) is sharp for uniform leafwise uniqueness and exponential contraction. At \(\alpha=0\), the central fixed point \((0,0,\pi)\) on \(W=\pi\) has leafwise eigenvalue one when \(s=1\); for every \(s>1\) the plane contains at least two additional equilibria. Fix \(0<\beta_0\le\delta_0\), \(\beta_0+\delta_0=1\), and set \(\beta=t\beta_0\), \(\delta=t\delta_0\), and \(\gamma=\delta-\beta\). On the plane \(W=\pi\) in each system, the transition at \(t=1\) is supercritical: for all sufficiently small \(t-1>0\) there are exactly three equilibria, the central one is unstable in the plane, and the two others attract in the plane. Their common first and second coordinates are
\[
r_\pm(t)=\pm\sqrt{6(t-1)}+O((t-1)^{3/2}).
\]

## Assumptions and scope

All initial states are allowed; no restriction on the initial real value of \(W\) or \(z\) is needed. All parameters and coordinates are real. The graph is a graph in the quotient by the period of the phase, not a compact invariant graph of the full real map with nonzero drift. The pitchfork stability statement concerns a single invariant plane in each zero-drift system; it does not assert ambient hyperbolicity.

## Proof

**Translation and phase reduction.** Direct substitution gives \(W\circ F=\alpha+\mu z+\beta x+(\gamma+\beta)y\), which is \(W+\alpha\) on the cancellation surface. Using \(z=W-\beta x-\delta y\), the phase advances by \(\alpha\), with fiber map \(G_\theta(x,y)=(y,\sin(\theta-\beta x-\delta y))\). For \(n\ge2\), both \(x_n\) and \(y_n\) are in \([-1,1]\), so \(z_n=W_0+n\alpha-\beta x_n-\delta y_n\) gives the drift limit. An invariant probability would give, under \(W\), a probability on \(\mathbb R\) invariant by translation through \(\alpha\); if \(\alpha\ne0\), the disjoint half-open intervals of length \(|\alpha|\) in this translation orbit could not all have the same mass and sum to one.

**Invariant graph and convergence.** For fibers sharing a phase, the vector of absolute errors is dominated after one step by multiplication by
\[
M=\begin{pmatrix}0&1\\\beta&\delta\end{pmatrix}.
\]
If \(s<1\), then \(\|M\|_\infty=1\), while the row sums of \(M^2\) are \(s\) and \(\beta+\delta s=s-\delta(1-s)\). Thus two steps contract by at most \(s\), uniformly in the phases. The graph transform on the complete max-norm space of continuous periodic pairs is \((\mathcal T h)(\theta)=G_{\theta-\alpha}(h(\theta-\alpha))\). Its square is a strict contraction. Its unique fixed point is fixed by \(\mathcal T\) because \(\mathcal T\) commutes with its square. Invariance forces both components to be in \([-1,1]\). The same bounds on one and two steps give the asserted attraction rate for all initial states.

**Empirical law and mean.** Irrational rotation is uniquely ergodic. Empirical averages of bounded continuous test functions of the fiber therefore converge to their Haar averages on the graph: convergence to the graph makes the discrepancy in test-function values tend to zero, by uniform continuity on the bounded region containing the iterates after step two. The relation \(X_\alpha(\theta+\alpha)=Y_\alpha(\theta)\) gives equal means. The zero-coupling comparison pair is \(X^{(0)}(\theta)=\sin(\theta-2\alpha)\), \(Y^{(0)}(\theta)=\sin(\theta-\alpha)\). In the invariant equation for \(Y_\alpha(\theta+\alpha)\) the displacement of the sine's argument has absolute value at most \(s\), so \(\|Y_\alpha-Y^{(0)}\|_\infty\le s\), and the shift relation gives \(\|X_\alpha-X^{(0)}\|_\infty\le s\). Taylor expansion in the displacement on the right of
\[
Y_\alpha(\theta+\alpha)=\sin(\theta-\beta X_\alpha(\theta)-\delta Y_\alpha(\theta))
\]
has remainder at most \(s^2/2\); replacing the graph by the comparison pair in the linear term costs at most \(s^2\). Integrating and using \(\int\cos\theta\sin(\theta-k\alpha)\,dm=-\sin(k\alpha)/2\) yields the claimed bound.

**Zero drift and the transition.** For \(\alpha=0\), a fixed point in \(W=w\) has \(x=y=r\), \(z=w-sr\), with \(r=\sin(w-sr)\). For \(s<1\) the scalar equation is a contraction. Its unique solution is continuous in \(w\) (indeed the Lipschitz constant is at most \(1/(1-s)\)). Fiber convergence implies convergence to this equilibrium in the full plane, because \(z=w-\beta x-\delta y\). By Poincaré recurrence, any invariant Borel probability is supported on the equilibrium curve, which gives the mixture assertion; conversely any such mixture is invariant.

At \(w=\pi\) the equation is \(r=\sin(sr)\). For \(s\le1\), \(|\sin(sr)|<|r|\) for nonzero \(r\). For \(s>1\), the difference \(\sin(sr)-r\) is positive sufficiently close to zero on the right and nonpositive at one. There is a positive root and oddness gives a negative one. Near \(t=s=1\), the function \(r\mapsto \sin(tr)/r\) is strictly decreasing on \(0<r\le1\) (use \(tr\in(0,\pi)\)), so the positive root is unique. It tends to zero by compactness and uniqueness at \(t=1\). Expanding the sine gives \(t-1=t^3r^2/6+O(r^4)\). Since \(r\to0\), this first implies \(r^2=O(t-1)\) and then \(r^2=6(t-1)/t^3+O((t-1)^2)\), giving the asserted branches.

In coordinates \((x,y)\) on the plane \(W=\pi\), the fiber map is \((y,\sin(\pi-t\beta_0x-t\delta_0y))\). Its derivative at \((r,r)\) is
\[
D G_\pi(r,r)=\begin{pmatrix}0&1\\t\beta_0\cos(tr)&t\delta_0\cos(tr)\end{pmatrix}.
\]
In particular the top right entry remains \(1\). With \(q=t\cos(tr)\) the characteristic polynomial is \(\lambda^2-q\delta_0\lambda-q\beta_0\). At \(q=1\) its roots are \(1\) and \(-\beta_0\), and the derivative of the root through \(1\) with respect to \(q\) is \(1/(1+\beta_0)\). On the central branch \(q=t\), so the positive root crosses above one as \(t\) increases through one. Off center the branch expansion gives \(q=1-2(t-1)+O((t-1)^2)\), and the positive root is \(1-2(t-1)/(1+\beta_0)+O((t-1)^2)\). The other root stays strictly inside the unit circle by continuity, since \(0<\beta_0\le1/2\). This proves the leafwise stability assertions. At \(t=1\), the eigenvalue one precludes a uniform exponential attraction inequality with decay factor less than one: differentiating the bound at the fixed point would bound the derivative of the \(n\)-th iterate along that eigenvector by a decaying quantity. For \(t>1\) uniqueness already fails.

## Verification

The standard-library `check_resonance.py` provides finite replay checks of the drift, fiber bound, branch locations, actual leafwise Jacobian and mean diagnostic. The all-time and all-parameter statements follow analytically from the proof; the finite checks cannot establish them.

## Relationship to prior work and limitations

Equation (1) of [1] supplies the same map and the meaning of the linear feedback; its numerical parameter and symmetry studies are not the uniform cancellation-surface result. The precursor [2] omits the linear feedback term. Standard contraction theory and the square-root scaling of a scalar sine fixed-point pitchfork are not themselves new. The distinguishing content is their combination with the explicit resonant translation, uniform all-phase attraction and quantitative bias in this feedback model, with the stability transition on its invariant leaf. The cancellation surface is codimension two; these claims do not establish behavior away from it, attraction for arbitrary large gain, or priority over every related sine-map reduction.

## References

1. K. Rajagopal, S. Kanagaraj, C. Volos and A. Karthikeyan, “Influence of Parametric Symmetry on the Dynamics of 3D Sinusoidal Discrete Systems,” *Symmetry* **15** (2023), 780. https://doi.org/10.3390/sym15040780
2. M. Mammeri, “Symmetry and Periodic-Chaos in 3-D Sinusoid Discrete Maps,” *Bulletin of Mathematical Analysis and Applications* **9** (2017), no. 1, 1–8. https://emis.muni.cz/journals/BMAA/repository/docs/BMAA9-1-1.pdf
3. T. Withers, *Invariant Graphs of Skew Product Dynamical Systems*, PhD thesis, University of Manchester (2017). https://research.manchester.ac.uk/en/studentTheses/invariant-graphs-of-skew-product-dynamical-systems/
