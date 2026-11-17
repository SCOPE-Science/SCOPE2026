# Sharp global bias selection and inverse-time oscillatory damping in the four-species Volterra lattice

## Finding
Consider the four-component, homogeneous biased Volterra replicator introduced in [1],
\[
\dot u_i=u_i\big[(1+a)u_{i-1}-u_{i+1}-aC(u)\big],\qquad
C(u)=\sum_{j=1}^4u_ju_{j+1},
\]
with cyclic indices, \(a>-1\), \(u_i(0)>0\), and \(\sum_i u_i(0)=1\). Let \(U=(1/4,1/4,1/4,1/4)\),
\[
s=u_1+u_3-u_2-u_4,\quad x=u_1-u_3,\quad y=u_2-u_4,\quad E=x^2+y^2.
\]
For every \(a>0\), **every interior solution converges to \(U\)** even though the Jacobian at \(U\) has the nonzero imaginary pair \(\pm i(a+2)/4\). For every such solution with \(E(0)>0\), the exact universal envelope in original physical time is
\[
\boxed{\lim_{t\to\infty}tE(t)=
\frac{2[a^2+4(a+2)^2]}{a(a+2)^2}.}
\]
The exceptional set \(E(0)=0\) is invariant and converges exponentially, not with this inverse-time law. For \(-1<a<0\), every nonuniform interior solution instead approaches the boundary in the precise sense
\[
\prod_{i=1}^4u_i(t)\longrightarrow0,\qquad
\min_{1\le i\le4}u_i(t)\longrightarrow0.
\]
At \(a=0\), the product becomes conserved, and the known conservative periodic-orbit regime separates the two behaviors. The uniform initial state is stationary for every \(a\).

## Assumptions and scope
The system is an ordinary differential equation, not a reaction-diffusion equation; there are exactly four species, with no mutations or immigration. The four cyclic indices are read modulo four. Initial fractions are strictly positive and sum to one. The bias ranges over the entire source domain \(-1<a<\infty\). The inverse-time limit requires positive bias and \(x(0)^2+y(0)^2>0\). No statement is made about convergence to an individual boundary equilibrium for negative bias.

## Proof
**Invariant simplex and an exact product law.** The vector field is polynomial. Its sum vanishes on the unit simplex, and each face is invariant; therefore every interior solution remains positive for all finite times. The four-cycle identity
\[
C(u)=(u_1+u_3)(u_2+u_4)=\frac{1-s^2}{4}
\]
gives, for \(P=\prod_i u_i\),
\[
\frac{d}{dt}\log P
=\sum_i\big[(1+a)u_{i-1}-u_{i+1}-aC(u)\big]
=a(1-4C(u))=as^2.\tag{1}
\]
This identity is exact, including all nonlinear contributions.

**Global behavior for positive bias.** For \(a>0\), (1) makes \(P\) nondecreasing. Since \(P(t)\ge P(0)>0\), every coordinate stays at least \(P(0)\); the trajectory is precompact inside the positive simplex. LaSalle's invariance argument forces its omega-limit set into \(s=0\). Indeed, direct substitution of
\[
u_1=\frac{1+s+2x}{4},\quad u_3=\frac{1+s-2x}{4},\quad
u_2=\frac{1-s+2y}{4},\quad u_4=\frac{1-s-2y}{4}
\]
produces, with \(\kappa=a+2\),
\[
\begin{aligned}
\dot s&=-\frac a4s+\frac a4s^3-\kappa xy,\\
\dot x&=-\frac\kappa4(1+s)y-\frac a4sx+\frac a4s^2x,\\
\dot y&=\frac\kappa4(1-s)x+\frac a4sy+\frac a4s^2y.
\end{aligned}\tag{2}
\]
An orbit contained in \(s=0\) requires \(xy=0\) at every time, whereas its remaining equations reduce to \(\dot x=-\kappa y/4\), \(\dot y=\kappa x/4\). The only orbit satisfying both restrictions is \(x=y=0\). Thus the largest invariant subset of \(s=0\) is \(U\), proving global convergence. In particular, no nontrivial interior cycle can persist for positive bias.

**Negative-bias boundary selection.** If \(-1<a<0\), then \(P\) decreases. For nonuniform initial data \(P(0)<4^{-4}\); if the limit of \(P\) were positive, the trajectory would stay in a compact interior set, and the same invariant-set argument would force convergence to \(U\). That would make \(P(t)\to4^{-4}\), contradicting \(P(t)\le P(0)\). Hence \(P(t)\to0\). Since \((\min_i u_i)^4\le\prod_i u_i\), the minimum tends to zero.

**Sharp nonlinear relaxation at positive bias.** Linearization of (2) at the origin has one stable eigenvalue \(-a/4\) and a center pair \(\pm i\omega\), where \(\omega=\kappa/4>0\). Put \(D=a^2+4\kappa^2\). The quadratic jet of a local center manifold, obtained from its invariance equation, is
\[
 s=h_2(x,y)+O((x^2+y^2)^{3/2}),\qquad
 h_2=\frac{4\kappa^2}{D}(x^2-y^2)-\frac{4a\kappa}{D}xy.\tag{3}
\]
Indeed, with \(L(x,y)=(-\omega y,\omega x)\), this polynomial satisfies
\[
Dh_2\cdot L=-\frac a4 h_2-\kappa xy,
\]
which is exactly the homogeneous degree-two center-manifold equation. Differentiating \(E=x^2+y^2\) in (2) yields the exact identity
\[
 \dot E=s\left[-\kappa xy+\frac a2(y^2-x^2)\right]
 +\frac a2s^2E.\tag{4}
\]
For a center-manifold solution, substitute (3), write \(x=\sqrt E\cos\theta\), \(y=\sqrt E\sin\theta\), and use \(\dot\theta=\omega+O(E)\). Then
\[
\dot E=E^2F(\theta)+O(E^{5/2}),\quad
F(\theta)=h_2(\cos\theta,\sin\theta)
\left[-\kappa\cos\theta\sin\theta+
\frac a2(\sin^2\theta-\cos^2\theta)\right].
\]
Direct elementary trigonometric integration gives
\[
\frac1{2\pi}\int_0^{2\pi}F(\theta)\,d\theta
=-\beta,\qquad \beta=\frac{a\kappa^2}{2D}>0.\tag{5}
\]
Let \(g(\theta)\) be the zero-mean periodic solution of \(\omega g'(\theta)=F(\theta)+\beta\), and put \(Z=E-g(\theta)E^2\). Then
\[
\dot Z=-\beta Z^2+O(Z^{5/2}).\tag{6}
\]
Any nonzero center orbit tending to the origin therefore satisfies \((1/Z)'=\beta+o(1)\), hence \(tE\to1/\beta=2D/(a\kappa^2)\). Ordinary center-manifold exponential tracking transfers this limit to every solution other than those on the strong-stable manifold: the tracking error is exponentially small compared with \(t^{-1/2}\). Finally, the invariant line \(x=y=0\) obeys \(\dot s=-(a/4)s(1-s^2)\) and is tangent to the unique stable eigendirection. By local uniqueness of the strong-stable manifold, it is exactly the exceptional exponentially convergent set. The flow preserves this line in both directions, so its initial-data characterization \(E(0)=0\) is global. This proves the claimed full-limit coefficient, without inferring an infinite-time assertion from finite integration.

**Zero bias (comparison, not a new assertion).** At \(a=0\), the factors \(u_1u_3\) and \(u_2u_4\) are conserved. The equilibrium set contains the interior segment \(u_1=u_3\), \(u_2=u_4\); nonstationary interior trajectories are periodic, consistent with the conservative four-strategy classification [2,3].

## Verification
Run the self-contained symbolic and numerical reproducer with `python verify.py` (Python with SymPy and SciPy). It checks (2), (1), the quadratic invariance identity (3), the exact angular mean (5), and finite-trajectory approaches to the predicted envelope for two positive bias values. The checker prints:

`VERIFY_OK exact_four_cycle=3 exact_product_law=1 center_manifold=1 quartic_average=1 finite_decay_examples=2`

The global LaSalle step and the infinite-time center reduction are analytical arguments. Their truth does not depend on the finite trajectory comparisons.

## Relationship to prior work
The model, its bias parameter, four-cycle eigenvalues, and finite-time illustrations belong to Visomirski and Griffin [1]. Their Section 2 examines the center spectrum and interprets oscillations as nondecaying. The exact product law, global interior attraction/escape dichotomy, and universal inverse-time envelope above go beyond that linear and numerical analysis. The conservative classification in Yin, Chen and Sinopoli [2] applies to skew-symmetric payoff games, not to the nonzero bias in [1]. Durney, Case, Pleimling and Zia [3] study cyclic replacement dynamics with conservative pairwise transfers and different rate structures; their exponential collective variable does not yield the present nonzero-bias product identity and coefficient. The graph-integrability treatment [4] also concerns skew-symmetric replicator systems. A separately published spatial even-cycle result concerns negative-bias frozen patterns with diffusion, rather than the positive-bias homogeneous convergence and rate here. Center manifolds, averaging and LaSalle's principle are established tools, not claimed as new. These source comparisons support a provisional, not definitive, priority assessment.

## Limitations
The global conclusions require strictly positive four-species initial conditions. For negative bias, only approach to the simplex boundary is proved, not convergence to a specified edge state. For positive bias, the exact inverse-time coefficient excludes the invariant exponential-decay line. The proof does not treat spatial diffusion, stochastic populations, immigration, or cycles of other lengths. No independent scientific audit has been performed.

## References
1. M. Visomirski and C. Griffin, *Coherent Structures and Travelling Waves in Spatial Replicators from a Biased Volterra Lattice*, arXiv:2601.06314v1 (first public 2026-01-09), Section 2 and later spatial sections.
2. H. Yin, X. Chen and B. Sinopoli, *On Permanence / Coexistence of Conservative Replicator Dynamics with Four Strategies*, arXiv:2604.06117 (first public 2026-04-07), Sections 1 and 3.
3. B. R. Durney, S. O. Case, M. Pleimling and R. K. P. Zia, *Saddles, Arrows, and Spirals: Deterministic Trajectories in Cyclic Competition of Four Species*, arXiv:1103.1535 (2011), Sections II–III.
4. M. Visomirski and C. Griffin, *Integrability of generalised skew-symmetric replicator equations via graph embeddings*, Journal of Physics A (2024), DOI:10.1088/1751-8121/ad996e.
