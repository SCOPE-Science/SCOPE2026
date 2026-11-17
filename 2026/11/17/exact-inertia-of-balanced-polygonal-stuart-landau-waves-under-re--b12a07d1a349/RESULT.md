# Exact inertia of balanced polygonal Stuart–Landau waves under real mean-field coupling

## Finding

The zero-order-parameter polygonal rotating waves of a finite, heterogeneously growing, globally coupled Stuart–Landau system admit a **complete real-coupling spectral-inertia classification**, including collinear degeneracies and inactive oscillators.

For every integer \(M\geq3\), let \(k>0\), \(c\in\mathbb R\), \(\omega\in\mathbb R\), and \(\beta_j\in\mathbb R\). Consider
\[
\dot z_j=(\beta_j+i\omega-k|z_j|^2)z_j+c\sum_{\ell=1}^M(z_\ell-z_j),\qquad 1\leq j\leq M.
\]
Assume \(\beta_j\ne Mc\) for every \(j\). Define the active set \(A=\{j:\beta_j>Mc\}\) of size \(a\geq3\), the inactive set \(I=\{1,\ldots,M\}\setminus A\), and \(r_j=\sqrt{(\beta_j-Mc)/k}\) for \(j\in A\). Suppose phases \(\theta_j\) satisfy \(\sum_{j\in A}r_je^{i\theta_j}=0\). Then
\[
z_j(t)=\begin{cases}r_je^{i(\omega t+\theta_j)},&j\in A,\\0,&j\in I\end{cases}
\]
is an exact solution. Let \((p,z,n)\) denote the counts of positive, zero and negative **real** eigenvalues, with multiplicities, of its \(2M\)-dimensional real co-rotating Jacobian. These are the signs of the real transverse Floquet exponents, with the neutral directions retained in \(z\).

If the active polygon is **noncollinear** (its side directions are not all parallel), the inertia is exactly
\[
(p,z,n)=\begin{cases}(2,\ a-2,\ 2M-a),&c>0,\\(0,\ a,\ 2M-a),&c=0,\\(0,\ a-2,\ 2M-a+2),&c<0.\end{cases}
\]
In particular, purely attractive real mean-field coupling gives **exactly two unstable directions**, irrespective of oscillator count, heterogeneity, and polygon shape. Purely repulsive real coupling has no unstable directions and has strictly attracting linear dynamics normal to the regular polygonal manifold.

If the active polygon is **collinear**, set \(d_j=2kr_j^2\) for \(j\in A\), \(d_j=Mc-\beta_j>0\) for \(j\in I\), and, when \(c>0\),
\[
\Gamma=c\sum_{j=1}^M\frac1{d_j}.
\]
For \(c<0\), the inertia is \((0,a-1,2M-a+1)\); for \(c=0\), it is \((0,a,2M-a)\); and for \(c>0\) it is
\[
(p,z,n)=\begin{cases}(1,a-1,2M-a),&\Gamma<1,\\(1,a,2M-a-1),&\Gamma=1,\\(2,a-1,2M-a-1),&\Gamma>1.\end{cases}
\]
Thus the singular collinear stratum has a separate, exact radial index transition. The result is a spectral classification; it makes no nonlinear stability assertion at a collinear zero eigenvalue.

## Assumptions and scope

The coupling is *real*, with no reactive component, and the nonlinear frequency-shift coefficient vanishes. The growth rates may be heterogeneous and may have either sign; active amplitudes are positive and all inactive growth rates lie strictly below \(Mc\). A zero-sum polygon must actually exist for the chosen radii. The angular frequency \(\omega\) is common: for \(\omega=0\) the rotating waves become equilibria, and otherwise their ordinary period is \(2\pi/|\omega|\). Inertia always refers to the stationary co-rotating frame. The classification includes generic noncollinear polygons and the exceptional collinear closures; it excludes the further degeneracies \(\beta_j=Mc\).

## Proof

**1. Exact relative equilibrium.** Set \(w_j=e^{-i\omega t}z_j\). The real-coupled vector field is
\[
\dot w_j=(\beta_j-Mc-k|w_j|^2)w_j+c\sum_{\ell=1}^M w_\ell.
\]
At the stated polygon, \(\sum_jw_j=0\); the local scalar coefficient vanishes for active \(j\), and inactive components vanish. Thus the displayed rotating wave is exact for all real \(c\), provided its radii and closure are admissible.

**2. Exact symmetric rank-two linearization.** Regard each \(w_j\) as a vector in \(\mathbb R^2\), put \(n_j=(\cos\theta_j,\sin\theta_j)\), and let \(U:(\mathbb R^2)^M\to\mathbb R^2\) send \(v=(v_1,\ldots,v_M)\) to \(\sum_jv_j\). Define a positive-semidefinite block-diagonal operator \(D\) by
\[
(Dv)_j=\begin{cases}2kr_j^2 n_j(n_j\cdot v_j),&j\in A,\\(Mc-\beta_j)v_j,&j\in I.\end{cases}
\]
Direct differentiation, including the derivative of the cubic saturation term, gives the exact real Jacobian
\[
\boxed{J=-D+cU^*U,\qquad U^*s=(s,\ldots,s).}
\]
The first term has \(a\) tangential zero directions (one for each active oscillator), and is strictly negative on all remaining directions. The second term is symmetric with rank at most two. In particular, no complex spectral estimates or numerical stability classifications are required.

**3. Noncollinear polygons, repulsive coupling.** For \(c<0\),
\[
\langle v,Jv\rangle=-\langle v,Dv\rangle-|c|\,|Uv|^2\leq0.
\]
Equality holds precisely when \(v_j=t_j(-\sin\theta_j,\cos\theta_j)\) for \(j\in A\), \(v_j=0\) for \(j\in I\), and \(\sum_{j\in A}t_j(-\sin\theta_j,\cos\theta_j)=0\). For noncollinear side directions, the final map from \(\mathbb R^a\) onto \(\mathbb R^2\) has rank two. The kernel therefore has dimension \(a-2\); all other \(2M-a+2\) eigenvalues are strictly negative. For \(c=0\) the zero eigenspace is the full \(a\)-dimensional active tangential space.

**4. Noncollinear polygons, attractive coupling.** If \(c>0\), the quadratic form of \(J\) is positive definite on a two-dimensional subspace of active tangential variations, because their sums range over all of \(\mathbb R^2\). Therefore \(J\) has at least two positive eigenvalues. On \(\ker U\), however, its quadratic form equals \(-\langle v,Dv\rangle\leq0\); since \(U\) has two-dimensional range, the positive index is at most two. To find the nullspace, suppose \(Jv=0\) and put \(s=Uv\). Projection of \(Jv=0\) onto each active tangent gives \(c\,s\cdot(-\sin\theta_j,\cos\theta_j)=0\). Noncollinearity forces \(s=0\), and consequently \(Dv=0\) and \(Uv=0\). This has dimension exactly \(a-2\) by the previous rank argument. The remaining \(2M-a\) eigenvalues are strictly negative. Thus the positive index equals two, with no other neutral eigenvalues.

**5. Collinear polygons.** Rotate axes so that every active \(n_j\) is \(+e_1\) or \(-e_1\). The Jacobian splits orthogonally into two real \(M\times M\) blocks. In the axial direction it is
\[
J_{\parallel}=-\operatorname{diag}(d_1,\ldots,d_M)+c\,\mathbf1\mathbf1^T.
\]
In the perpendicular direction it is
\[
J_{\perp}=-\operatorname{diag}(0\ (j\in A),\ Mc-\beta_j\ (j\in I))+c\,\mathbf1\mathbf1^T.
\]
For \(c<0\), the axial block is negative definite, whereas the perpendicular block is negative semidefinite with exactly \(a-1\) zero eigenvalues. For \(c>0\), the perpendicular block has exactly one positive eigenvalue, \(a-1\) zeros, and \(M-a\) negatives. Congruence by \(\operatorname{diag}(\sqrt{d_j})\) transforms the axial block into a matrix with the same inertia as \(-I+cqq^T\), where \(q_j=d_j^{-1/2}\). Its unique potentially nonnegative eigenvalue has the sign of \(\Gamma-1\), giving the three cases in the statement. At \(c=0\), the blocks reduce to the uncoupled radial damping and tangential neutrality. This proves the complete classification.

**6. Dynamical interpretation.** Since \(J\) is real symmetric, every eigenvalue is real and the inertia counts actual exponentially growing, neutral, and decaying linear directions. For \(\omega\ne0\), an eigenvalue \(\lambda\) corresponds to the Floquet multiplier \(e^{2\pi\lambda/|\omega|}\). Thus the two positive eigenvalues for an attractive noncollinear polygon are genuine unstable Floquet directions. For negative coupling, the strict negativity off the \(a-2\) tangent directions establishes normal linear attraction at every regular polygon.

## Verification

The companion standalone Python program `verify_inertia.py` tests the direct Jacobian formula against central finite differences for 56 noncollinear polygon examples with heterogeneous active and inactive oscillators of dimensions three through nine. It also checks their predicted signed eigenvalue counts. Symbolic SymPy calculations independently factor the Jacobian characteristic polynomials for an exact equilateral three-oscillator polygon and an exact collinear four-oscillator polygon, including the collinear \(\Gamma=1\) degeneracy.

For the equilateral triangle with radii one and cubic coefficient one, the characteristic polynomial is exactly
\[
\lambda(\lambda+2)\bigl(\lambda^2+(2-3c)\lambda-3c\bigr)^2.
\]
For the collinear four-state \((1,1,-1,-1)\), it is
\[
\lambda^3(\lambda-4c)(\lambda+2)^3(\lambda+2-4c).
\]
These examples expose respectively the two unstable directions and the additional radial crossing at \(c=1/2\). The finite calculations are illustrative checks; the proof above covers all admissible finite sizes and parameter values.

## Relationship to prior work

Zhao and Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators* (arXiv:2610.08239v1, publicly submitted October 6, 2026), provide the motivating model, exact zero-order-parameter polygon constructions, a real-coupling gradient potential, and numerical classifications of transverse stability for complex coupling. They do **not** give the all-size signed inertia or a collinear transition formula. In particular, their principal numerical coupling path imposes \(C_r=C_i/4\): its zero-reactive point has zero real coupling, unlike the nonzero real-coupling slices classified here.

Millán, Poyato, Reynolds and Tudisco, *Synchronization of coupled Stuart–Landau oscillators: How heterogeneity can facilitate synchronization* (arXiv:2510.05243v1), prove strong synchronization and amplitude-death results for positive real coupling with strictly sectorial initial configurations; noncollinear zero-mean polygons cannot be strictly sectorial and their spectral inertia is not classified there. Related finite-rank analyses of oscillation quenching concern different equilibria and do not imply the index formula here. Classical rank-one inertia and gradient-flow techniques are used as tools and are not themselves claimed as new.

## Limitations

The result is confined to finite, all-to-all real coupling, with equal intrinsic frequencies and no amplitude-dependent frequency shift. The sign classification is linear, not a classification of global attraction basins. Collinear polygons possess extra neutral directions, so a vanishing eigenvalue is not a claim of nonlinear neutral stability or of an additional smooth manifold. At excluded birth/death parameters \(\beta_j=Mc\), the inactive/active splitting must be reconsidered. Reactive coupling can stabilize polygonal states, and this theorem makes no claim about that general complex-coupling regime. Historical originality and independent verification remain subject to outside review.

## References

1. L. Zhao and N. Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators*, arXiv:2610.08239v1 (October 6, 2026), https://arxiv.org/html/2610.08239 .
2. A. P. Millán, D. Poyato, D. N. Reynolds and F. Tudisco, *Synchronization of coupled Stuart–Landau oscillators: How heterogeneity can facilitate synchronization*, arXiv:2510.05243v1 (October 6, 2025), https://arxiv.org/pdf/2510.05243 .
3. I. León and D. Pazó, *Phase reduction beyond the first order: The case of the mean-field complex Ginzburg–Landau equation*, Phys. Rev. E 100, 012211 (2019), https://doi.org/10.1103/PhysRevE.100.012211 .
