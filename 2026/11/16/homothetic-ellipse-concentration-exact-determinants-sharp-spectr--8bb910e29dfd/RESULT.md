# Homothetic ellipse concentration: exact determinants, sharp spectral hierarchy, and Chebyshev nodal collapse

## Finding
Let \(E=\{z=x+iy:x^2/a^2+y^2/b^2<1\}\) for \(a>b>0\). Let \(\mathcal P_N\) consist of all complex analytic polynomials of degree at most \(N\ge1\), with area inner product on \(E\). For \(0<t<1\), define the concentration operator \(T_N(t)\) by restricting energy to the homothetic subellipse \(tE\). Its \(N+1\) eigenvalues, in descending order \(\lambda_0(t)\ge\cdots\ge\lambda_N(t)>0\), satisfy an **exact, shape-independent determinant law**
\[
\boxed{\prod_{j=0}^N\lambda_j(t)=t^{(N+1)(N+2)}}.
\]
Moreover, **every eigenvalue has its own sharp shrinking-aperture power**, with an explicitly computable positive coefficient:
\[
\boxed{\lambda_j(t)\sim\frac{\Delta_{j+1}}{\Delta_j}t^{2j+2},\quad 0\le j\le N,\qquad\Delta_j=\det G_j\det (G^{-1})_j,\ \Delta_0=1,}
\]
where \(G\) is the normalized area-moment Gram matrix in the monomial basis and \(G_j\) denotes its first \(j\) rows and columns (similarly for \(G^{-1}\)). The extreme coefficients admit the closed forms below. The least-observable polynomial is eventually unique up to scalar; after rescaling its zeros by \(1/t\), they converge to the \(N\) distinct real zeros of the **monic Chebyshev polynomial of the second kind** on the focal segment of \(E\). Thus all its roots are real, simple, and inside \(tE\) for all sufficiently small \(t>0\).

## Assumptions and scope
Put \(d\mu(z)=dx\,dy/(\pi ab)\) on \(E\), of total mass one. The same density, without re-normalization, is used on \(tE\). The polynomial inner product is \(\langle f,g\rangle_E=\int_E f(z)\overline{g(z)}\,d\mu(z)\), and \(\langle T_N(t)f,g\rangle_E=\int_{tE}f(z)\overline{g(z)}\,d\mu(z)\). Thus \(0<T_N(t)<I\) and all eigenvalues are positive and strictly smaller than one. Define \(G=(G_{ij})_{0\le i,j\le N}\) with \(G_{ij}=\int_E z^i\overline z^{\,j}\,d\mu(z)\). For \(0\le j\le N+1\), \(G_j\) denotes its leading \(j\)-by-\(j\) principal block; the same convention applies to \((G^{-1})_j\). Every determinant is positive.

For explicit formulas put \(c=\sqrt{a^2-b^2}>0\), \(s=(a^2+b^2)/(a^2-b^2)>1\), and \(u=(a+b)/2\), \(v=(a-b)/2\). Let \(U_n\) be the standard Chebyshev polynomial of the second kind, \(U_0=1\), \(U_1(w)=2w\), \(U_{n+1}(w)=2wU_n(w)-U_{n-1}(w)\). Define the monic planar orthogonal polynomial
\[
P_N(w)=(c/2)^N U_N(w/c),\qquad H_N=\|P_N\|_E^2=\frac{(c^2/4)^N}{N+1}U_N(s),
\]
and the raw moment
\[
M_N=\int_E|z|^{2N}\,d\mu(z)=\frac1{N+1}\sum_{k=0}^N\binom Nk^2 u^{2k}v^{2(N-k)}.
\]
Then the sharp extreme spectral constants are
\[
\boxed{\lambda_N(t)\sim\frac{H_N}{M_N}t^{2N+2},\qquad \lambda_0(t)\sim K_N(0,0)t^2,}
\]
where the diagonal finite Bergman kernel is
\[
K_N(0,0)=\sum_{r=0}^{\lfloor N/2\rfloor}\frac{2r+1}{U_{2r}(s)}.
\]
Consequently, the sharp squared concentration-condition number obeys
\[
\boxed{\kappa_N(t)=\lambda_0(t)/\lambda_N(t)\sim K_N(0,0)\frac{M_N}{H_N}t^{-2N}.}
\]
All asymptotics fix \(N,a,b\) and take \(t\downarrow0\); no uniformity in growing \(N\) or varying eccentricity is asserted.

## Proof
**Exact Gram scaling.** For \(D_t=\operatorname{diag}(1,t,\ldots,t^N)\), homothety \(z=tw\) and the planar area Jacobian give \(G(t)=t^2D_tGD_t\) exactly. In an orthonormal coordinate system, \(T_N(t)\) has matrix \(A(t)=G^{-1/2}G(t)G^{-1/2}\), which is Hermitian positive definite. Therefore \(\det A(t)=t^{2(N+1)+2\sum_{j=0}^N j}=t^{(N+1)(N+2)}\). This isolated determinant identity is elementary and is not the claimed novelty by itself.

**All spectral powers and coefficients.** Fix \(1\le k\le N+1\). On the \(k\)-th exterior power, the positive operator \(\bigwedge^k A(t)\) has largest eigenvalue \(\lambda_0(t)\cdots\lambda_{k-1}(t)\). The \((I,J)\) minor of \(G(t)\) is \(t^{2k+\sum_{i\in I}i+\sum_{j\in J}j}\det G[I,J]\). Its unique smallest exponent \(k(k+1)\) occurs at \(I=J=\{0,\ldots,k-1\}\), giving a rank-one leading operator. Conjugating by \(\bigwedge^kG^{-1/2}\), its single nonzero leading eigenvalue is
\[
\Delta_k=\det G_k\det(G^{-1})_k>0.
\]
Hence \(\prod_{i=0}^{k-1}\lambda_i(t)\sim\Delta_k t^{k(k+1)}\). Divide consecutive identities to obtain every asserted power and coefficient \(\Delta_{j+1}/\Delta_j\). The powers differ by two, so all eigenvalues are distinct for sufficiently small \(t\), and in particular the minimizing eigenspace is one-dimensional.

**Evaluation and extreme constants.** The leading constant for \(k=1\) is \(G_{00}(G^{-1})_{00}=K_N(0,0)\), the squared norm of evaluation at zero. For \(k=N+1\), \(\Delta_{N+1}=1\). Jacobi's complementary-minor identity gives \(\det(G^{-1})_N=G_{NN}/\det G\), while \(\det G/\det G_N\) is the squared norm \(H_N\) of the monic degree-\(N\) polynomial orthogonal on \(E\). Thus \(\Delta_{N+1}/\Delta_N=H_N/G_{NN}=H_N/M_N\).

The planar Chebyshev orthogonality of Akemann–Nagao–Parra–Vernizzi identifies \(P_N(w)=(c/2)^NU_N(w/c)\), and gives exactly \(H_N=(c^2/4)^NU_N(s)/(N+1)\). The same orthogonality gives normalized basis \(U_j(z/c)/\sqrt{U_j(s)/(j+1)}\). As \(U_{2r}(0)=(-1)^r\) and \(U_{2r+1}(0)=0\), summing squared basis values at the center yields the stated \(K_N(0,0)\). Finally, writing \(z=r(ue^{i\theta}+ve^{-i\theta})\) in elliptic polar coordinates and taking the angular constant term of \(|z|^{2N}\) gives the stated binomial sum for \(M_N\). This completes the exact coefficient and condition-number formulas.

**Scaled eigenfunction and nodes.** Choose the least-eigenvalue polynomial \(f_t(z)=\sum_{j=0}^N a_j(t)z^j\), normalized by \(\|f_t\|_E=1\), with positive real leading coefficient. The minimal-eigenvalue bound above yields
\[
\int_E|t^{-N}f_t(tw)|^2d\mu(w)=t^{-2N-2}\lambda_N(t)=O(1).
\]
Because the fixed polynomial space has a positive definite Gram matrix, all coefficients of \(q_t(w)=t^{-N}f_t(tw)\) remain bounded. Consequently \(a_j(t)=O(t^{N-j})\) for \(j<N\). The outer normalization forces \(a_N(t)\to M_N^{-1/2}>0\). Dividing by \(a_N(t)\), the monic polynomials \(q_t/a_N(t)\) have bounded coefficients and an inner norm tending to \(H_N\) by the sharp \(\lambda_N\) formula. Every subsequential limit is therefore the **unique** monic minimizer of the planar \(L^2\) norm, namely \(P_N\); hence convergence is coefficientwise for the whole family. The roots of \(P_N\) are simple and real at \(c\cos(k\pi/(N+1))\), \(k=1,\ldots,N\). By continuity of simple roots and reality of the coefficients of the unique eigenvector, the roots of \(f_t\) are eventually all real, simple, and lie inside \(tE\), with positions
\[
\boxed{z_k(t)/t\longrightarrow c\cos\bigl(k\pi/(N+1)\bigr),\quad k=1,\ldots,N.}
\]

## Verification
A standalone script `CHECK.py` performs exact rational moment calculations and Chebyshev orthogonality checks for eccentric axes \((a,b)=(3,2),(5,1)\), degrees \(1\le N\le6\), and two nonzero homothetic scales. It verifies the determinant law symbolically; all leading constants, the complete spectral hierarchy, and scaled eigenfunction coefficients are additionally compared with 90-digit eigenvalue calculations at two small scales. A successful run prints `HOMOTHETIC_ELLIPSE_CONCENTRATION_PASS`. The theorem for arbitrary fixed degree and all noncircular ellipses is proven above; finite checks are corroborative only. Use `python CHECK.py` with the dependencies in `requirements.txt`.

## Relationship to prior work
Akemann, Nagao, Parra, and Vernizzi (arXiv:1905.02397, posted 2019-05-07) establish orthogonality and norms of planar Chebyshev/Gegenbauer polynomials on ellipses. These are used openly as an ingredient, not claimed new; their inspected sections do not establish shrinking-subellipse concentration eigenvalues, the universal determinant, or the least-mode nodal rescaling. Nagao, Akemann, Kieburg, and Parra (arXiv:1905.07977) use the same polynomial kernels for planar Coulomb-gas correlations and different large-particle limits. A related publicly archived mathematical result, *Explicit shrinking-window eigenvalue hierarchy for Dunkl–Hermite and Gegenbauer concentration* (2026), proves all spectral powers for **one-dimensional real-interval weights**, not analytic polynomials integrated over an interior two-dimensional ellipse; it does not imply the present planar Chebyshev extreme coefficients or limiting nodal geometry. A publicly archived finite Bergman ellipse-kernel zero theorem (2026) concerns zeros of \(K_N(z,0)\) as eccentricity varies, rather than least-eigenvector zeros for homothetically shrinking apertures. Finite-dimensional exterior-power asymptotics and the determinant scaling are standard tools. The contribution assessed here is their complete ellipse-specific combination with explicit sharp extremal coefficients and the least-mode nodal theorem, not those tools alone.

## Limitations
The band degree and the ellipse are fixed as \(t\downarrow0\). No growing-degree double-scaling, uniform eccentricity limit, noise-optimal algorithm, or nonhomothetic observation geometry is established. The sharp constants are exact but can be ill-conditioned to evaluate through high-order moments numerically; the formulas do not assert a stable algorithm. The circle limit \(a=b\) is excluded from the nodal statement because the focal segment collapses. Originality is assessed against identified accessible literature and records, not certified against all historical or unindexed equivalents. Independent mathematical audit has not been performed.

## References
1. G. Akemann, T. Nagao, I. Parra, G. Vernizzi, *Gegenbauer and other planar orthogonal polynomials on an ellipse in the complex plane*, arXiv:1905.02397v1 (2019-05-07), especially the unweighted planar Chebyshev orthogonality and norm formulas. https://arxiv.org/abs/1905.02397
2. T. Nagao, G. Akemann, M. Kieburg, I. Parra, *Families of two-dimensional Coulomb gases on an ellipse: correlation functions and universality*, arXiv:1905.07977v1 (2019-05-20), finite-rank kernels in Section 3. https://arxiv.org/abs/1905.07977
3. *Explicit shrinking-window eigenvalue hierarchy for Dunkl–Hermite and Gegenbauer concentration*, publicly archived mathematical note (2026), theorem statement and proof.
4. *Real-to-nonreal zeros in finite Bergman kernels of ellipses: the first sharp bifurcation*, publicly archived mathematical note (2026), theorem statement and proof.
