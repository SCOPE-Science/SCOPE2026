# Sharp coordinatewise stability of Euclidean projections onto ball–cube intersections

## Finding

For each integer \(n\ge2\) and radius \(r>0\), consider the closed convex set
\[
C_{n,r}=\{z\in\mathbb R^n:\|z\|_\infty\le1,\ \|z\|_2\le r\}
\]
and its Euclidean nearest-point map \(P_{n,r}:\mathbb R^n\to C_{n,r}\). Write
\[
L_n(r)=\sup_{v\ne w}\frac{\|P_{n,r}(v)-P_{n,r}(w)\|_\infty}{\|v-w\|_\infty}.
\]
The following finite formula gives the exact global constant in every dimension, including the case in which the cube and ball boundaries are simultaneously active.

For \(r\ge\sqrt n\), \(L_n(r)=1\). For \(0<r<\sqrt n\), take each integer \(k\) satisfying \(0\le k\le n-2\) and \(k<r^2\), and define
\[
\begin{aligned}
m_k&=n-k,\quad c_k=(r^2-k)^{-1/2},\\
\alpha_k&=\sqrt{\max\{0,1-(m_k-1)c_k^2\}},\quad
\beta_k=\min\{1,c_k\},\\
a_k^*&=\sqrt{\frac{1-m_k^{-1/2}}2},\quad
\widehat a_k=\min\{\beta_k,\max\{\alpha_k,a_k^*\}\},\\
F_k&=1-\widehat a_k^2+\sqrt{m_k-1}\,\widehat a_k\sqrt{1-\widehat a_k^2}.
\end{aligned}
\]
Then
\[
\boxed{L_n(r)=\max\left\{1,\ \max_{\substack{0\le k\le n-2\\k<r^2}}F_k\right\}.}
\]
Every maximum in this formula is over a nonempty finite set. The following consequences expose its sharp geometry:

* For \(0<r\le1\), \(L_n(r)=(1+\sqrt n)/2\), the Euclidean-ball-only coefficient.
* At \(n=13\) and \(r=\sqrt5\), \(L_{13}(\sqrt5)=(3+\sqrt{33})/4\). A one-saturated-coordinate face is strictly more sensitive than every no-saturation face: its coefficient exceeds their maximum \(4(1+\sqrt3)/5\) by about \(0.000500016\).
* For each \(n\ge3\), \(\lim_{r\uparrow\sqrt n}L_n(r)=2-2/n>1=L_n(\sqrt n)\). The optimal Lipschitz constant jumps when the ball constraint becomes redundant, even though the convex sets vary continuously. In dimension two this limiting value is one.

## Assumptions and scope

All spaces and matrices are real. \(\|\cdot\|_2\) is the Euclidean norm; \(\|\cdot\|_\infty\) is the coordinate maximum. The projection minimizes \(\frac12\|z-v\|_2^2\) over \(C_{n,r}\), but both input and output sensitivity are measured in the **coordinate maximum norm**, not the Euclidean metric. The constants are two-input, global supremums; a derivative supremum may be approached by arbitrarily close but distinct inputs rather than attained by a finite pair. Scaling a cube with side half-width \(b>0\) and a ball with radius \(R\) changes \(r\) to \(R/b\) without changing the coefficient.

## Proof

**1. Projection structure.** Strict convexity of the objective yields a unique minimizer. Slater's condition holds for \(r>0\). The KKT system gives a scalar \(s=1+\lambda\ge1\) such that
\[
[P_{n,r}(v)]_i=\operatorname{clip}(v_i/s,-1,1).
\]
If \(\|\operatorname{clip}(v,-1,1)\|_2\le r\), one may take \(s=1\). Otherwise \(s>1\) is chosen so that the clipped vector has squared Euclidean norm \(r^2\). The root is unique in the relevant region where at least one coordinate remains free; this completely describes the projector.

**2. Local derivatives on smooth strata.** Suppose \(s>1\), exactly \(k\) output coordinates are saturated at \(\pm1\), and \(m=n-k\) coordinates form the nonempty free set \(J\). Necessarily \(k<r^2\), and on that stratum
\[
P_{n,r}(v)_J=\rho_k\frac{v_J}{\|v_J\|_2},\qquad \rho_k=\sqrt{r^2-k}.
\]
Set \(u=v_J/\|v_J\|_2\), so \(\|u\|_2=1\) and \(\rho_k|u_i|<1\) for all \(i\in J\). Saturated output coordinates are locally constant; the only nonzero derivative block is
\[
D_JP_{n,r}(v)=\frac{\rho_k}{\|v_J\|_2}(I_m-uu^{\mathsf T}).
\]
Because \(s=\|v_J\|_2/\rho_k>1\), its scalar prefactor is below one. If \(m=1\) the derivative block is zero. Ball-inactive strata have a diagonal clipping derivative of maximum-row-sum norm at most one.

**3. Sharp constrained row-sum bound.** For \(m\ge2\), the induced maximum-norm matrix coefficient is
\[
\|I_m-uu^{\mathsf T}\|_{\infty\to\infty}
=\max_i\left(1-u_i^2+|u_i|\sum_{j\ne i}|u_j|\right).
\]
Fix a prospective norming row and let \(a=|u_i|\). By Cauchy–Schwarz,
\[
\sum_{j\ne i}|u_j|\le\sqrt{m-1}\sqrt{1-a^2},
\]
with equality exactly when all other absolute coordinates are equal. The coordinate cap \(|u_j|\le c_k\) allows such an equality vector if and only if
\[
\sqrt{\max\{0,1-(m-1)c_k^2\}}\le a\le\min\{1,c_k\},
\]
which is precisely \([\alpha_k,\beta_k]\). The interval is nonempty since \(r^2<n\), so \(c_k>1/\sqrt m\). It suffices to maximize
\[
f_m(a)=1-a^2+\sqrt{m-1}\,a\sqrt{1-a^2}
\]
on that interval. Writing \(t=2a^2-1\), we have
\[
f_m(a)=\tfrac12\bigl(1-t+\sqrt{m-1}\sqrt{1-t^2}\bigr).
\]
The last expression is strictly increasing up to \(t=-1/\sqrt m\) and strictly decreasing afterward. Hence its maximum is at \(a_m^*\), clamped to the permitted interval, and equals \(F_k\).

**4. Global upper bound.** The nearest-point map is nonexpansive in Euclidean norm and therefore globally Lipschitz in the coordinate maximum norm with some finite coefficient. Away from finitely many regularity strata and their analytic transition boundaries, the derivatives are those described in step 2. On every such open stratum the maximum norm of the Jacobian is bounded by the displayed finite maximum (or by one). Integrating along generic line segments whose intersections with the stratum boundaries have measure zero gives this same global Lipschitz bound. Arbitrary endpoints follow by continuity (alternatively, apply the convex-hull property of generalized Jacobians).

**5. Sharpness at every feasible face.** Fix \(k\), choose a unit vector \(u\) with one absolute component \(a\in(\alpha_k,\beta_k)\) and all remaining absolute components \(\sqrt{(1-a^2)/(m-1)}\). Choose \(z\) whose first \(k\) coordinates equal one and whose free coordinates are \(\rho_k u\). For any \(s>1\), let \(v_J=sz_J\) and choose the first \(k\) components of \(v\) strictly greater than \(s\). The KKT equations show that \(P_{n,r}(v)=z\), with those \(k\) coordinates saturated. The derivative row-sum there is \(f_m(a)/s\). Let \(s\downarrow1\) and \(a\) approach the maximizing \(\widehat a_k\) from inside its feasible interval. This realizes \(F_k\) as a limit of two-input sensitivity quotients. The coefficient one follows from interior inputs where the projector is the identity. Thus the finite formula is exact, not merely an upper bound.

**6. Three consequences.** If \(r\le1\), the Euclidean ball lies in the cube, so the only relevant global projector is Euclidean radial clipping. The unconstrained row bound is \((1+\sqrt n)/2\), attained in the derivative limit at \(a_n^*\).

For \(n=13\), \(r^2=5\), the no-saturation face has \(k=0,m=13,c_0=1/\sqrt5\) and its norming row is restricted to \(a=1/\sqrt5\), giving \(F_0=4(1+\sqrt3)/5\). The \(k=1,m=12,c_1=1/2\) face gives \(F_1=(3+\sqrt{33})/4\). The strict inequality \(F_1>F_0\) reduces, after squaring positive sides, to \(7>4\sqrt3\). For every \(k\ge2\), the unrestricted row bound is at most \((1+\sqrt{11})/2<F_1\). Thus \(F_1\) is the exact maximum; the cap-boundary witness is approached through strictly free coordinates.

Finally, as \(r\uparrow\sqrt n\), each permitted interval collapses to \(a=1/\sqrt{n-k}\), and hence \(F_k\to2-2/(n-k)\). The largest limit is \(2-2/n\) from \(k=0\). At \(r=\sqrt n\), the constraint \(\|z\|_2\le r\) is redundant in the cube, and coordinate clipping has coefficient one.

## Verification

The accompanying standalone Python file `CHECK.py` evaluates the finite formula, a scalar-bisection implementation of the Euclidean projector, randomized numerical Jacobians, the limiting regimes, and the explicit thirteen-coordinate face witness. Execute `python CHECK.py` using only the Python standard library. Its reported finite checks supplement, but cannot replace, the proof of the all-dimensional sharp coefficient. No external numerical files or training data are required.

## Relationship to prior work

Bauschke–Bui–Wang (2017) study metric projection onto intersections of cones with balls or spheres, giving a distinct intersection-projection framework. Liu–Wang–Song (2019) analyze algorithms for Euclidean projection onto \(\ell_1\)- and \(\ell_2\)-ball/sphere intersections; their norm geometry is different and their statements do not give two-input coordinatewise conditioning of \(B_\infty\cap rB_2\). Vasil'eva (2020) studies Kolmogorov widths of finite-dimensional norm-ball intersections, which includes the present underlying set geometry but optimizes subspace approximation rather than the metric projector's perturbation modulus. A previous sharp weighted sensitivity result for Euclidean-ball clipping addresses the special regime \(r\le1\), not the mixed active ball–box regime \(1<r<\sqrt n\). The saturated-face formula and the discontinuous sharp coefficient are not implied by those comparisons.

## Limitations

This is a real finite-dimensional Euclidean nearest-point projection theorem for centered, uniformly bounded coordinates and an origin-centered ball. It does not cover nonuniform box limits, translated balls, alternate minimization metrics, or infinite-dimensional uniform estimates. The global sharp coefficient may be a limiting local quotient rather than an attained finite pair. Historical priority could be affected by unindexed literature on box-constrained trust-region projectors; the inspected sources did not yield the same theorem. No independent external mathematical audit has been performed.

## References

1. H. H. Bauschke, M. N. Bui, X. Wang, *Projecting onto the intersection of a cone and a sphere*, arXiv:1708.00585 (first posted August 2, 2017). https://arxiv.org/abs/1708.00585
2. H. Liu, H. Wang, M. Song, *A unified approach for projections onto the intersection of \(\ell_1\) and \(\ell_2\) balls or spheres*, arXiv:1911.03946 (first posted November 10, 2019). https://arxiv.org/abs/1911.03946
3. A. A. Vasil'eva, *Kolmogorov widths of the intersection of two finite-dimensional balls*, arXiv:2007.04894 (first posted July 9, 2020). https://arxiv.org/html/2007.04894v1
4. *Sharp weighted coordinate sensitivity of Euclidean-ball clipping*, publicly indexed mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-weighted-coordinate-sensitivity-of-euclidean-ball-clipping--78696bf157c3
