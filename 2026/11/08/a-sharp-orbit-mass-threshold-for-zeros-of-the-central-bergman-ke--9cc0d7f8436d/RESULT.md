# A sharp orbit-mass threshold for zeros of the central Bergman kernel

## Finding
Let \(q\ge2\) be an integer, \(0<\rho<1\) and \(t>0\). Start with normalized area measure on the unit disk and add equal point masses at the vertices of a regular \(q\)-gon of radius \(\rho\). For the resulting analytic reproducing kernel \(K_t\), put \(r=\rho^q\) and
\[
T_q(\rho)=\frac{(1-r^2)^2}{q r\big((q+1)+qr+(q-1)r^2\big)}.
\]
Then the central fiber \(z\mapsto K_t(z,0)\) has no zeros in the open unit disk for \(0<t\le T_q(\rho)\), and precisely \(q\) distinct simple zeros for \(t>T_q(\rho)\). At equality the same \(q\) roots lie on the unit circle; for strictly larger masses the zeros form a centered regular polygon and converge radially to the added mass points as \(t\to\infty\).

There are two contrasting sharp asymptotic regimes:
\[
T_q(\rho)\sim\frac43(1-\rho)^2\quad(\rho\uparrow1,\ q\text{ fixed}),
\qquad
T_q(\rho)\sim\frac{\rho^{-q}}{q(q+1)}\quad(q\to\infty,\ \rho\text{ fixed}).
\]
Thus, despite the full rotationally symmetric area background, a finite cyclic orbit of singular masses can induce arbitrarily many zeros in the *central* reproducing-kernel fiber. This distinguishes such measures from radial densities, whose central fibers are constant.

## Assumptions and scope
Write \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), let \(dA/\pi\) denote normalized planar area, and set \(\zeta=e^{2\pi i/q}\) and \(a_j=\rho\zeta^j\) for \(j=0,\dots,q-1\). Equip the usual analytic Bergman space \(A^2(\mathbb D)\) with
\[
\langle f,g\rangle_t=\int_{\mathbb D}f\overline g\,\frac{dA}{\pi}
+t\sum_{j=0}^{q-1}f(a_j)\overline{g(a_j)}.
\]
All point evaluations at the interior masses are bounded on \(A^2(\mathbb D)\); hence this norm is equivalent to the standard Bergman norm, and the positive definite reproducing kernel \(K_t(z,w)\) exists. The result concerns the zero set of one polarized fiber, \(w=0\), not zeros of its positive diagonal \(K_t(z,z)\) or every other fiber. Multiplicities are analytic multiplicities in \(z\).

## Proof
**1. Finite-rank kernel identity.** The unperturbed kernel is \(K_0(z,w)=(1-z\overline w)^{-2}\). Put \(v(z)=(K_0(z,a_0),\ldots,K_0(z,a_{q-1}))^{\mathsf T}\) and \(G=(K_0(a_i,a_j))_{0\le i,j<q}\). The standard resolvent identity for the positive finite-rank evaluation operator gives
\[
K_t(z,w)=K_0(z,w)-t\,v(z)^{\mathsf T}(I+tG)^{-1}\overline{v(w)}.
\]
This follows directly by substituting it into the reproducing identity, or by applying \((I+tE^*E)^{-1}=I-t E^*(I+tEE^*)^{-1}E\) to the evaluation map \(E f=(f(a_j))_j\).

**2. Cyclic character reduction.** The constant vector \(\mathbf 1\) is an eigenvector of the circulant Gram matrix \(G\). Set \(r=\rho^q\) and \(h_q(y)=(1+(q-1)y)/(1-y)^2\). Expanding the geometric series and summing over roots of unity gives
\[
\sum_{j=0}^{q-1}K_0(z,a_j)=q\sum_{m=0}^{\infty}(qm+1)(\rho z)^{qm}
=q h_q((\rho z)^q)
\]
and the Gram row sum is
\[
L=q h_q(r^2)=q\frac{1+(q-1)r^2}{(1-r^2)^2}.
\]
Since \(v(0)={\bf1}\), the exact fiber formula is
\[
K_t(z,0)=1-\beta h_q((\rho z)^q),\qquad
\beta=\frac{qt}{1+tL}.
\]
The rational function is holomorphic in \(|z|\le1\), since its poles require \(|\rho z|=1\).

**3. Complete root classification.** For \(t>0\), \(0<\beta<B=q/L<1\). Write \(y=(\rho z)^q\). After clearing a denominator nonzero on \(|z|\le1\), the root equation is
\[
(1-y)^2=\beta(1+(q-1)y),
\]
i.e.,
\[
y^2-(2+(q-1)\beta)y+1-\beta=0.
\]
Its discriminant is \(4q\beta+(q-1)^2\beta^2>0\). The two roots are positive and distinct, with \(0<y_-<1<y_+\): the product \(1-\beta\) is positive, the sum is positive, and the quadratic takes value \(-q\beta<0\) at \(y=1\). Hence the only possible roots of \(K_t(z,0)\) inside the disk are the \(q\) simple solutions of \((\rho z)^q=y_-\). These solutions lie inside exactly when \(y_-<r\), on the boundary exactly when \(y_-=r\), and outside when \(y_->r\).

On \(0<y<1\), \(g(y)=(1-y)^2/(1+(q-1)y)\) is strictly decreasing. Thus \(y_-=g^{-1}(\beta)\), and the crossing occurs exactly when \(\beta=g(r)=(1-r)^2/(1+(q-1)r)\). Solving \(qt/(1+tL)=g(r)\) and simplifying yields
\[
t=T_q(\rho)=\frac{(1-r^2)^2}{q r((q+1)+qr+(q-1)r^2)}.
\]
This number is positive. Strict monotonicity of \(t\mapsto\beta\) gives the zero/no-zero dichotomy. At the crossing the derivative with respect to \(y\) of the defining quadratic is nonzero, as its roots are distinct, and \(dy/dz=q\rho^q z^{q-1}\ne0\); hence all \(q\) roots are simple, including at the boundary.

**4. Infinite-mass and asymptotic laws.** As \(t\to\infty\), \(\beta\uparrow B=g(r^2)\), hence \(y_-\downarrow r^2\). Thus the roots \(z_j=\rho^{-1}y_-^{1/q}\zeta^j\) tend to \(\rho\zeta^j=a_j\) radially from outside the atom orbit. For fixed \(q\), \(1-\rho^{2q}\sim2q(1-\rho)\) and the denominator of \(T_q\) tends to \(3q^2\). For fixed \(\rho<1\), \(r=\rho^q\to0\), and the denominator is asymptotic to \(q(q+1)r\). Both displayed asymptotic statements follow.

## Verification
The accompanying `verify_atomic_orbit.py` recomputes the symbolic threshold identity, the character-sum formula for selected exact integer orders, and direct Gram-matrix reconstructions for selected radii and masses on both sides of the critical value. The numerical checks are illustrative; the complete classification for every integer order and every real parameter is proved by the finite-rank and quadratic arguments above. No finite simulation is treated as a proof of an all-parameter statement.

## Relationship to prior work
The general finite-mass perturbation framework appears in Beckermann–Putinar–Saff–Stylianopoulos (arXiv:1812.06560, first public version 2018-12-16), particularly its finite-rank and Christoffel–Darboux kernel analysis. Those general formulas provide a tool for this proof but do not themselves state the sharp cyclic orbit crossing, the exact central zero count, or its two scaling regimes. Perälä (arXiv:1703.05976, 2017) establishes arbitrarily many kernel zeros for carefully chosen *radial weights*, but also shows that a radial-weight central kernel is constant, so the present central-fiber effect has different hypotheses and conclusions. Putinar (2021) analyzes area measure plus finitely many point masses for moment/cloud questions but does not give this root-location threshold. These distinctions concern explicit mathematical statements, not priority by wording alone.

## Limitations
The theorem is for equal positive atomic masses on one regular polygon and normalized area measure on \(\mathbb D\). It does not cover unequal masses, noncyclic configurations, every point in the second kernel argument, non-disk domains, or general singular perturbations. General low-rank update identities are classical and do not constitute the new claim. No independent external audit is claimed. An unlocated equivalent treatment of root locations for cyclic Uvarov perturbations would affect historical priority.

## References
- B. Beckermann, M. Putinar, E. B. Saff, and N. Stylianopoulos, *Perturbations of Christoffel–Darboux kernels. I: detection of outliers*, arXiv:1812.06560v1 (2018), later *Foundations of Computational Mathematics* (2020). https://arxiv.org/abs/1812.06560
- A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976v1 (2017), later *Journal of Geometric Analysis* (2018). https://arxiv.org/abs/1703.05976
- M. Putinar, *Moment Estimates of the Cloud of a Planar Measure*, *Acta Applicandae Mathematicae* 176, article 2 (2021), doi:10.1007/s10440-021-00443-0. https://doi.org/10.1007/s10440-021-00443-0
