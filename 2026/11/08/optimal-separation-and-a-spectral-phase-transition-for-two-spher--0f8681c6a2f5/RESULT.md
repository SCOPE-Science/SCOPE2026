# Optimal separation and a spectral phase transition for two spherical sampling caps

## Finding
Let \(0<t<1\), set \(\rho=\arccos t\), and let \(u,v\in\mathbb S^2\) have separation angle \(\theta\in[2\rho,\pi]\). Thus their equal closed spherical caps \(C_t(u)=\{x\in\mathbb S^2:x\cdot u\ge t\}\) and \(C_t(v)\) have disjoint interiors. Equip \(\mathbb S^2\) with normalized area measure \(\sigma\), and consider the five-dimensional **real homogeneous degree-two spherical harmonic space**
\[
\mathcal H_2=\{h_A(x)=x^{\mathsf T}Ax:A=A^{\mathsf T}\in\mathbb R^{3\times3},\ \operatorname{tr}A=0\}.
\]
Write \(R_{t,u,v}\) for restriction from \(L^2(\sigma)\) to \(L^2(C_t(u)\cup C_t(v),\sigma|_{C_t(u)\cup C_t(v)})\), with **no renormalization of the restricted measure**. Let \(\lambda_{\min}(t,\theta)\) be the smallest eigenvalue of \(R_{t,u,v}^{*}R_{t,u,v}\) on \(\mathcal H_2\).

**Optimal placement theorem.** Among all disjoint-interior placements of two caps of this radius, \(\lambda_{\min}(t,\theta)\) is uniquely maximized at
\[
\boxed{\theta_*(t)=\max\{2\arccos t,\ \pi/2\}.}
\]
Equivalently, the optimal centers are orthogonal whenever this is geometrically feasible; otherwise the caps are tangent. This is an exact maximin sampling and sharp stable-reconstruction statement, not merely a trace or average-energy bound.

**Exact algebraic reconstruction constant.** Put \(q=\cos\theta\), and define
\[
\mu_2=\frac12-\frac{15t}{16}+\frac{5t^3}{8}-\frac{3t^5}{16},\quad
\beta=\frac{15}{8}t(1-t^2)^2,\quad
\gamma=\frac{15}{32}t(1-t^2)(7t^2-3).
\]
For \(r=q^2\) define
\[
T(r)=\frac{4\beta+\gamma(1+3r)}3,\qquad
D(r)=\frac{\beta(\beta+\gamma)(1-r)}3,\qquad
\phi(r)=\frac{T(r)-\sqrt{T(r)^2-4D(r)}}2.
\]
The **exact least concentration eigenvalue at every admissible placement** is
\[
\boxed{\lambda_{\min}(t,\theta)=2\mu_2+
\min\!\left\{\frac{\beta}{2}(1-|\cos\theta|),\ \phi(\cos^2\theta)\right\}.}
\]
It is positive. Consequently the exact norm of stable inversion from the sampled norm back to the full-sphere norm is \(\|R_{t,u,v}^{-1}\|=\lambda_{\min}(t,\theta)^{-1/2}\), where the inverse is defined on the range of restriction. Substitution of \(\theta_*(t)\) gives the globally best such norm.

**Sharp worst-mode transition for orthogonal caps.** If \(t\ge1/\sqrt2\), the optimal centers are orthogonal and
\[
\boxed{\lambda_{\min}(t,\theta_*)=2\mu_2+
\begin{cases}
(\beta+\gamma)/3,&1/\sqrt2\le t\le\sqrt5/3,\\
\beta/2,&\sqrt5/3\le t<1.
\end{cases}}
\]
For \(1/\sqrt2\le t<\sqrt5/3\), the least-eigenvalue space is one-dimensional, consisting of a diagonal traceless quadratic form relative to the bisector/difference/transverse axes. For \(\sqrt5/3<t<1\), it is the two-dimensional span of the mixed transverse quadratics. At the exact transition \(t=\sqrt5/3\), it has dimension three. All these claims are invariant under common rotation of the two caps.

## Assumptions and scope
Everything is real. The cap radius satisfies \(0<\rho<\pi/2\); centers are constrained by \(2\rho\le\theta\le\pi\). Contact along cap boundaries is permitted, since such contact has zero surface measure. Both cap areas and the full-sphere harmonic norm use the **same normalized full-sphere measure**. Quadratic harmonics are homogeneous degree two and traceless, **without constants or degree-one harmonics**. We use the Frobenius inner product \(\langle A,B\rangle_F=\operatorname{tr}(AB)\); the exact identity \(\|h_A\|_{L^2(\sigma)}^2=\frac2{15}\|A\|_F^2\) fixes normalization.

## Proof
**1. Single-cap tensor.** By axial symmetry, the normalized concentration quadratic form for one cap is, for every traceless symmetric \(A\),
\[
\frac{\int_{C_t(u)}h_A^2\,d\sigma}{\int_{\mathbb S^2}h_A^2\,d\sigma}
=\mu_2\|A\|_F^2+\beta\|Au\|^2+\gamma(u^{\mathsf T}Au)^2
\quad(\|A\|_F=1).
\]
For arbitrary \(A\), the right side is divided by \(\|A\|_F^2\). To verify the coefficients, split the five-dimensional traceless-symmetric space into axial angular orders zero, one, and two. Their respective one-cap eigenvalues are
\[
\mu_0=\frac12-\frac{5t}{8}+\frac{5t^3}{4}-\frac{9t^5}{8},\qquad
\mu_1=\frac12-\frac{5t^3}{4}+\frac{3t^5}{4},\qquad
\mu_2=\frac12-\frac{15t}{16}+\frac{5t^3}{8}-\frac{3t^5}{16}.
\]
These follow directly by integrating, respectively, the normalized squares of \(3z^2-1\), \(zx\), and \(x^2-y^2\) with \(z\) uniform on \([-1,1]\) and longitude uniform on \([0,2\pi]\). The orthogonal order-one squared-component sum is \(2(\|Au\|^2-(u^{\mathsf T}Au)^2)\); the order-zero squared component is \(\tfrac32(u^{\mathsf T}Au)^2\). Hence \(\beta=2(\mu_1-\mu_2)\) and \(\gamma=\tfrac32(\mu_0-\mu_2)-2(\mu_1-\mu_2)\), which simplify to the expressions above. In particular,
\[
\beta>0,\qquad\beta+\gamma=\frac{15}{32}t(1-t^2)(1+3t^2)>0.
\]

**2. Exact five-sector reduction.** Choose orthonormal axes with \(u=(c,0,s)\), \(v=(c,0,-s)\), \(c^2=(1+q)/2\), \(s^2=(1-q)/2\). Add the two single-cap quadratic forms (the cap interiors do not overlap). The three Frobenius-normalized off-diagonal quadratic forms \(xy\), \(yz\), and \(xz\) are eigenmodes with eigenvalues
\[
\lambda_{xy}=2\mu_2+\frac{\beta}{2}(1+q),\quad
\lambda_{yz}=2\mu_2+\frac{\beta}{2}(1-q),\quad
\lambda_{xz}=2\mu_2+\beta+\gamma(1-q^2).
\]
The remaining diagonal traceless two-dimensional block has the form \(2\mu_2 I+H(q)\), where the trace and determinant of \(H(q)\) are exactly
\[
\operatorname{tr}H(q)=T(q^2),\qquad\det H(q)=D(q^2).
\]
For example, in the Frobenius-orthonormal diagonal basis \(\operatorname{diag}(1,-1,0)/\sqrt2\), \(\operatorname{diag}(1,1,-2)/\sqrt6\), the entries of \(H(q)\) are
\[
\begin{aligned}
H_{11}&=\frac{(1+q)(2\beta+\gamma(1+q))}{4},\\
H_{12}&=\frac{\sqrt3(1+q)(2\beta+\gamma(3q-1))}{12},\\
H_{22}&=\frac{-6\beta q+10\beta+\gamma(9q^2-6q+1)}{12}.
\end{aligned}
\]
The remaining two eigenvalues are \(2\mu_2+\frac12(T\pm\sqrt{T^2-4D})\). This determines the **entire five-dimensional spectrum**, including multiplicities at coincidences.

**3. Eliminate the \(xz\)-mode from the least eigenvalue.** The smaller of the \(xy\) and \(yz\) eigenvalues is \(\lambda_o=2\mu_2+\frac\beta2(1-|q|)\). Exactly,
\[
\lambda_{xz}-\lambda_o=(1+|q|)\left[\frac\beta2+\gamma(1-|q|)\right].
\]
If \(t^2\ge1/5\), the bracket is positive since \(\gamma\ge-\beta/2\); in the equality boundary the admissible disjoint separation keeps \(q\ne0\). If \(t^2<1/5\), cap disjointness implies \(|q|\ge1-2t^2\), and \(\gamma<0\) gives
\[
\frac\beta2+\gamma(1-|q|)\ge\frac\beta2+2t^2\gamma
=\frac{\beta(1-4t^2+7t^4)}{2(1-t^2)}>0.
\]
The quadratic \(1-4z+7z^2\) is positive for all real \(z\) (negative discriminant). Thus the \(xz\)-mode is never least in the admissible domain, proving the advertised exact least-eigenvalue formula.

**4. Strict monotonicity in the absolute center inner product.** Let \(r=q^2\in[0,1)\) and let \(\phi(r)\) be the smaller eigenvalue of \(H\). The characteristic polynomial is
\[
F_r(z)=z^2-T(r)z+D(r).
\]
For \(0\le r_1<r_2<1\), evaluate it at \(z=\phi(r_1)\):
\[
F_{r_2}(\phi(r_1))=-(r_2-r_1)
\left[\gamma\phi(r_1)+\frac{\beta(\beta+\gamma)}3\right].
\]
The bracket is positive. This is immediate if \(\gamma\ge0\). If \(\gamma<0\), the smaller eigenvalue at \(r=0\) is \(x_0=(\beta+\gamma)/3\), while \(F_r(x_0)=-(\beta+\gamma)^2r/3<0\) for \(r>0\). Hence \(\phi(r)\le x_0\), so the bracket is at least \((\beta+\gamma)^2/3>0\). Therefore \(F_{r_2}(\phi(r_1))<0\), which places \(\phi(r_1)\) strictly between the two roots of \(F_{r_2}\), giving \(\phi(r_2)<\phi(r_1)\). The off-diagonal candidate \(\beta(1-|q|)/2\) also strictly decreases with \(|q|\). Thus \(\lambda_{\min}\) is **strictly decreasing** in \(|q|\) throughout the admissible center-separation range.

**5. Geometry of the optimum and the phase transition.** Disjointness is \(-1\le q\le2t^2-1\). The admissible value of \(q\) closest to zero is uniquely \(q_*(t)=\min\{0,2t^2-1\}\), giving \(\theta_*(t)\). When \(t\ge1/\sqrt2\), this is \(q_*=0\); the two diagonal-block offsets are \(\beta\) and \((\beta+\gamma)/3\), while the smaller off-diagonal offset is \(\beta/2\) with multiplicity two. The diagonal candidate crosses the off-diagonal candidate exactly when
\[
\frac{\beta+\gamma}{3}-\frac\beta2
=\frac{5t(1-t^2)(9t^2-5)}{32}=0.
\]
Since \(0<t<1\), the sole crossing is \(t=\sqrt5/3\). This proves all asserted multiplicities and identifies the worst-conditioned harmonic directions. A nonzero quadratic polynomial cannot vanish on a spherical cap interior; hence all restriction eigenvalues are positive and the inversion formula follows by the finite-dimensional singular-value theorem.

## Verification
The standalone checker `check_two_caps.py` uses exact rational moment integration in cap-aligned coordinates and independently compares every entry of the five-dimensional Gram form with the analytic tensor expression. It also checks exact off-diagonal eigenvalues, the trace and determinant of the remaining two-dimensional block, and disjoint cap geometry across 33 rational cases. In a separate numerical grid it compares the claimed optimum against 19,829 other feasible placements and checks the predicted mode transition. Its expected success markers are `EXACT_CAP_MOMENT_TENSORS_AND_FIVE_EIGEN_SECTORS_OK`, `TWO_CAP_ANGLE_OPTIMALITY_GRID_OK`, `ORTHOGONAL_THREE_MODE_TRANSITION_OK`, and `ALL_QUADRATIC_SPHERICAL_TWO_CAP_CHECKS_OK`. The grid is diagnostic, **not** an infinite proof; steps 1–5 prove the all-parameter theorem.

## Relationship to prior work
Simons, Dahlen and Wieczorek (2004 preprint; 2006 journal version) formulate spherical spatiospectral concentration as a finite Gram-matrix eigenproblem for arbitrary measurable regions and develop explicit methods particularly for axisymmetric single caps. Their general Gram operator and cap rotations underlie the setup; no claim of inventing this operator is made. Simons and Dahlen (2006) analyze **antipodal** double polar caps and their complements; that region has fixed separation \(\pi\). Neither inspected treatment states the present optimal separation over **arbitrary distinct non-antipodal pairs**, the monotone least-eigenvalue law for the isolated real degree-two space, or its sharp one-to-two dimensional worst-mode transition. The general matrix procedure makes numerical instances computable, but it does not by itself give the all-angle maximin theorem.

The mathematical claims are conditional on the stated domain; no priority or exhaustive novelty certificate is asserted. Related higher-bandwidth and alternative sampling designs could contain a stronger equivalent result not identified by the inspected material.

## Limitations
Only two equal spherical caps with disjoint interiors and the real degree-two **homogeneous** harmonic space are covered. The theorem does not cover arbitrary overlapping cap unions (where integrals cannot simply be added), anisotropic surface weights, unequal cap sizes, complex harmonic coefficients, constants and degree-one modes, or degree at least three. The optimality concerns the **smallest** concentration eigenvalue (worst-case stable recovery), not the largest concentration eigenvalue, determinant, trace, or statistical estimator with nonuniform noise. No external independent audit has been performed.

## References
1. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1, publicly posted 2004-08-31; SIAM Review 48 (2006), 504–536, doi:10.1137/S0036144504445765. In particular Sections 3–5 and the general Gram-eigenvalue construction.
2. F. J. Simons and F. A. Dahlen, *Spherical Slepian functions and the polar gap in geodesy*, Geophysical Journal International 166 (2006), 1039–1061, doi:10.1111/j.1365-246X.2006.03065.x, especially Sections 3–5 and 4.2 on antipodal double caps.
3. W. Erb and S. Mathias, *An alternative to Slepian functions on the unit sphere—A space-frequency analysis based on localized spherical polynomials*, arXiv:1307.3862 (2013), on a related but different localized-basis construction.
