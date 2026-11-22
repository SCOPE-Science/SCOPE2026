# A sharp two-scale radial covariance cone on homogeneous trees and its atomic spectral collapse

## Finding
Let \(q\ge2\) be an integer, let \(T_q\) be the infinite \((q+1)\)-regular tree, and let \(d\) denote graph distance. For \(0<s<r<1\) and \(\lambda\ge0\) consider
\[
K_{q;r,s,\lambda}(x,y)=r^{d(x,y)}-\lambda s^{d(x,y)}.
\]
Its positive-semidefiniteness threshold on **all finite vertex sets** is exactly
\[
\boxed{\Gamma_q(r,s)=\begin{cases}
\displaystyle\frac{1-r^2}{1-s^2}\min\!\left\{
\frac{(1+\sqrt q\,s)^2}{(1+\sqrt q\,r)^2},
\frac{(1-\sqrt q\,s)^2}{(1-\sqrt q\,r)^2}\right\},&s<q^{-1/2},\\[7pt]
0,&s\ge q^{-1/2}.
\end{cases}}
\]
At \(r=q^{-1/2}\), interpret the second candidate in the minimum as \(+\infty\). Then \(K_{q;r,s,\lambda}\) is positive semidefinite for every finite vertex configuration **if and only if** \(0\le\lambda\le\Gamma_q(r,s)\).

When \(s<q^{-1/2}\), the minimum is attained at the *negative adjacency-band edge* when \(qrs<1\), at the *positive edge* when \(qrs>1\), and at every band frequency when \(qrs=1\). The last case is possible only for \(r>q^{-1/2}\); it is a genuine spectral-collapse line. With
\[
 s=\frac1{qr},\qquad B_r=\frac{q(1-r^2)}{q^2r^2-1},\qquad
 C_r=\frac{(q+1)(qr^2-1)}{q^2r^2-1},\qquad t_r=r^{-1}+qr,
\]
we have \(\Gamma_q(r,s)=B_r\) and **the entire continuous spherical spectral component cancels**:
\[
\boxed{K_{q;r,1/(qr),B_r}(x,y)=C_r\,\phi_{t_r}\!\bigl(d(x,y)\bigr),}
\]
where \(\phi_t(0)=1\), \(\phi_t(1)=t/(q+1)\), and
\(q\phi_t(n+1)=t\phi_t(n)-\phi_t(n-1)\) for \(n\ge1\).
Here \(t_r\in(2\sqrt q,q+1)\) is a complementary-series spherical parameter and \(C_r>0\).

Every admissible kernel **except possibly at the collapsed boundary** \(qrs=1\), \(\lambda=\Gamma_q(r,s)\) is strictly positive definite on every finite set of pairwise distinct vertices. No assertion of finite-site strictness is made at the collapsed boundary itself.

## Assumptions and scope
Positive semidefiniteness means
\(\sum_{i,j=1}^m\overline{c_i}c_j K(x_i,x_j)\ge0\) for all integers \(m\ge1\), arbitrary tree vertices \(x_i\) (including repetitions), and arbitrary complex coefficients \(c_i\). Strict positive definiteness refers to pairwise distinct vertices and nonzero coefficient vectors. The tree is infinite, with every vertex of degree \(q+1\); \(q\) is any finite integer at least two. The scales satisfy the strict order \(0<s<r<1\). The coefficient \(\lambda\) is nonnegative. The statement is not about finite balls, finite graphs, or the degree-two bi-infinite path.

## Proof
**1. The spherical criterion and reference measure.** Write \(A\) for the adjacency operator on \(\ell^2(T_q)\). Its spectrum is the full interval \(I_q=[-2\sqrt q,2\sqrt q]\) and its root spectral probability measure is
\[
 d\nu_q(t)=\frac{q+1}{2\pi}\frac{\sqrt{4q-t^2}}{(q+1)^2-t^2}\,1_{I_q}(t)\,dt.
\]
The normalized spherical polynomials \(\phi_t(n)\) are defined in the Finding. They have degree \(n\) in \(t\) and are positive-definite radial kernels for every \(t\in[-q-1,q+1]\). The radial Bochner criterion for homogeneous trees (see Vergara, Theorem 1.2) says that a real radial sequence \(f(n)\) is positive definite on \(T_q\) exactly when it has a unique representing finite positive Borel measure \(\mu\) on \([-q-1,q+1]\) with
\[
 f(n)=\int\phi_t(n)\,d\mu(t)\qquad(n\ge0).
\]
Uniqueness follows also from the fact that the \(\phi_t(n)\) span all polynomials. The reference measure represents the identity kernel:
\(\int\phi_t(n)d\nu_q(t)=1_{\{n=0\}}\). Moreover, for every bounded Borel multiplier \(G\), the kernel entries of \(G(A)\) obey
\[
 \langle\delta_x,G(A)\delta_y\rangle
 =\int_{I_q}\phi_t(d(x,y))G(t)\,d\nu_q(t).
\]
This follows by averaging the distance-\(n\) adjacency polynomial over a sphere around one vertex and then applying the spectral theorem.

**2. Exact representing measures for the geometric profiles.** Put
\[
 F_u(t)=\frac{1-u^2}{1+qu^2-ut},\qquad 0<u<1.
\]
If \(u<q^{-1/2}\), the radial columns \(u^{d(\cdot,y)}\) lie in \(\ell^2\) and satisfy
\[
 (I-uA+qu^2I)u^{d(\cdot,y)}=(1-u^2)\delta_y.
\]
Consequently \(u^d\) has representing measure \(F_u\nu_q\). At \(u=q^{-1/2}\) the same conclusion follows by taking \(u\uparrow q^{-1/2}\): the geometric kernels converge pointwise, their compactly supported representing probability measures converge weakly by uniqueness, and their densities converge away from the positive band edge. Indeed, \(1+qu^2-ut=(1-\sqrt q\,u)^2+u(2\sqrt q-t)\), so near the critical radius the densities \(F_u\,d\nu_q/dt\) are dominated near the upper edge by a constant multiple of \((2\sqrt q-t)^{-1/2}\), an integrable function. Dominated convergence therefore preserves total mass one, and no atom appears.

If \(u>q^{-1/2}\), let \(v_u=(qu)^{-1}\), so \(0<v_u<q^{-1/2}\), and define
\[
 B_u=\frac{q(1-u^2)}{q^2u^2-1},\qquad
 C_u=\frac{(q+1)(qu^2-1)}{q^2u^2-1},\qquad
 t_u=u^{-1}+qu.
\]
Both \(B_u,C_u\) are positive, \(B_u+C_u=1\), and \(2\sqrt q<t_u<q+1\). The elementary rational identity
\[
 F_u(t)=B_uF_{v_u}(t)
\]
shows that \(F_u\nu_q\) represents the radial sequence \(B_uv_u^n\). Since both \(u^n\) and \(v_u^n\) solve the same second-order recurrence \(qf(n+1)=t_uf(n)-f(n-1)\) for \(n\ge1\), and since direct substitution verifies the values at \(n=0,1\), we have the exact identity
\[
 u^n=B_uv_u^n+C_u\phi_{t_u}(n)\quad(n\ge0).
\]
Thus for every \(0<u<1\) the complete (and unique) spherical representing measure of \(u^d\) is
\[
 \boxed{d\mu_u(t)=F_u(t)\,d\nu_q(t)
  +1_{\{u>q^{-1/2}\}}C_u\,\delta_{t_u}(dt).}
\]
For \(u=q^{-1/2}\), only the continuous term is present. This formula is particularly important because the out-of-band atom is essential, not an optional correction.

**3. Nonexistence of a positive subtraction above critical decay.** By linearity, the signed measure representing \(K_{q;r,s,\lambda}\) is \(\mu_r-\lambda\mu_s\). If \(s>q^{-1/2}\), \(\mu_s\) has a strictly positive atom at \(t_s\). Since \(r>s>q^{-1/2}\), \(t_r\ne t_s\) (the function \(u\mapsto u^{-1}+qu\) is strictly increasing above the critical radius), so \(\mu_r\) has no atom at \(t_s\). Every \(\lambda>0\) therefore gives a negative atom, forbidden by uniqueness of the positive spherical measure. If \(s=q^{-1/2}\), then necessarily \(r>q^{-1/2}\). The ratio \(F_r(t)/F_s(t)\) tends to zero as \(t\uparrow2\sqrt q\), because \(F_s\) diverges while \(F_r\) remains finite. Hence every \(\lambda>0\) creates a negative absolutely continuous component near the upper band edge. In both cases the sharp threshold is zero, and \(\lambda=0\) is admissible by positive definiteness of \(r^d\).

**4. Sharp positive threshold below critical decay.** Suppose \(s<q^{-1/2}\). The measure \(\mu_s\) has no atom, and the only possible atom of \(\mu_r\) is nonnegative. Therefore positivity is equivalent to
\[
 F_r(t)-\lambda F_s(t)\ge0\quad(t\in(-2\sqrt q,2\sqrt q)),
\]
with endpoints interpreted by limits. Both functions are positive in the band interior. Their ratio is
\[
 R_{r,s}(t)=\frac{F_r(t)}{F_s(t)}
 =\frac{1-r^2}{1-s^2}\frac{1+qs^2-st}{1+qr^2-rt}.
\]
Its derivative has the sign of \(1-qrs\), since
\[
 R'_{r,s}(t)=\frac{(1-r^2)(r-s)(1-qrs)}{(1-s^2)(1+qr^2-rt)^2}.
\]
It is therefore minimized at \(-2\sqrt q\) if \(qrs<1\), at \(+2\sqrt q\) if \(qrs>1\), and everywhere if \(qrs=1\). Using \(1+qu^2\pm2\sqrt q\,u=(1\pm\sqrt q\,u)^2\) gives exactly the stated two-candidate expression for \(\Gamma_q(r,s)\). The second candidate is interpreted as infinity when \(r=q^{-1/2}\); the actual infimum is then the finite negative-edge candidate. Negative measure on any nonempty part of the band violates radial positive definiteness, proving sharp necessity as well as sufficiency.

**5. Atomic collapse and strict finite-site positivity.** The equality \(qrs=1\) implies \(r>q^{-1/2}>s\) under \(s<r\). By the rational identity in Step 2, the quotient \(R_{r,s}(t)\) is constant and equals \(B_r\); thus the difference of the continuous components vanishes identically at \(\lambda=\Gamma_q(r,s)=B_r\). Its only remaining representing mass is \(C_r\delta_{t_r}\), producing the displayed complementary-series identity.

Away from this collapsed boundary, the continuous spectral density \(F_r-\lambda F_s\) is strictly positive for \(\nu_q\)-almost every frequency whenever \(\lambda\le\Gamma_q(r,s)\) and \(s<q^{-1/2}\). The same holds when \(s\ge q^{-1/2}\) at its only admissible weight \(\lambda=0\): \(F_r>0\) on the open band. For any finitely supported nonzero coefficient vector \(c\) on distinct vertices, set \(Q_c(t)=\sum_{i,j}\bar c_ic_j\phi_t(d(x_i,x_j))\). Every \(Q_c(t)\) is nonnegative by spherical positive definiteness, and
\(\int Q_c(t)\,d\nu_q(t)=\sum_i|c_i|^2>0\). Integrating against a strictly positive density yields a strictly positive quadratic form. This proves finite-site strictness in all asserted cases, completing the proof. \(\square\)

## Verification
The standalone program `verify_tree_two_scale.py` uses exact symbolic arithmetic to verify the resolvent density identity, the positive atom and continuous-mass normalization, the spherical recurrence and derivative formula. It also checks 35 exact moments at the rational spectral-collapse example \(q=2\), \(r=4/5\), \(s=5/8\), \(\lambda=6/13\):
\[
 \left(\frac45\right)^n-\frac6{13}\left(\frac58\right)^n
 =\frac7{13}\phi_{57/20}(n)\quad(n\ge0).
\]
Four supplementary finite-vertex Gram tests are included. Run `python verify_tree_two_scale.py` with SymPy and NumPy. The finite tests do not establish the all-finite-sets classification; that follows from the unique spherical representing measure and the continuous-band/atom analysis.

## Relationship to prior work
Vergara's 2019 radial Bochner theorem supplies a general necessary-and-sufficient representation for positive-definite kernels on homogeneous trees. The present result evaluates that criterion for an ordered **pair of distinct geometric decay rates**, determines the exact scalar subtraction cone, and exhibits the continuous-to-atomic spectral cancellation. The published first-order profile \(r^d(1+b d)\) has a different one-scale parameter and a cone collapse governed by a polynomial multiplier; it does not state this two-scale atom obstruction or exact ratio. A published quadratic-distance classification likewise assumes one subcritical scale. A published two-scale exponential comparison concerns the *two-sphere*, where discrete Legendre coefficients replace the tree's continuous principal band and complementary atom. Picardello's 2023 paper investigates spherical representations of semi-homogeneous trees, rather than the present signed two-scale kernel on homogeneous trees. These comparisons do not amount to exhaustive historical priority certification.

## Limitations
The classification assumes \(q\ge2\), \(0<s<r<1\) and \(\lambda\ge0\); it does not address irregular trees, the bi-infinite path, finite trees, nongeometric profiles, or negative subtraction coefficients. The spectral-collapse result identifies a positive semidefinite complementary spherical kernel but makes no claim about finite-site strictness on that single boundary line. The sharp formula follows from a classical general spherical Bochner theorem, and a differently worded prior calculation of this special family cannot be ruled out absolutely. Supplementary checks are finite; independent scientific validation has not been performed.

## References
1. I. Vergara, *Positive definite radial kernels on homogeneous trees and products*, arXiv:1907.11476, first public 2019-07-26, Theorem 1.2 and Section 6; https://arxiv.org/abs/1907.11476.
2. M. A. Picardello, *Positive definite functions on semi-homogeneous trees and spherical representations*, arXiv:2309.03850, first public 2023-09-07, Sections 1, 4–5; https://arxiv.org/abs/2309.03850.
3. U. Haagerup and S. Knudby, *A Lévy–Khinchin formula for free groups*, arXiv:1304.5763, first public 2013-04-21; https://arxiv.org/abs/1304.5763.
4. *A sharp positive-definiteness cone and its collapse for first-order exponential kernels on regular trees*, published mathematical result, 2026-10-25; https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-positive-definiteness-cone-and-its-collapse-for-first-or--0ea4651dd31d.
5. *Extreme-point geometry of quadratic geometric covariances on homogeneous trees*, published mathematical result, 2026-11-16; https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-extreme-point-geometry-of-quadratic-geometric-covariances-on-hom--2a7f8734ecad.
6. *Exact two-scale exponential covariance domination on the two-sphere*, published mathematical result, 2026-10-26; https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-two-scale-exponential-covariance-domination-on-the-two-sph--4e0d440866a1.
7. H. Kesten, *Symmetric random walks on groups*, Trans. Amer. Math. Soc. **92** (1959), 336–354, for the regular-tree adjacency spectral law.
