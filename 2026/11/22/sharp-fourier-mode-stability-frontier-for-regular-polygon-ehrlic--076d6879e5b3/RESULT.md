# Sharp Fourier-mode stability frontier for regular-polygon Ehrlich–Aberth iterates

## Finding

For every integer \(n\ge2\), consider the **simultaneous (Jacobi) Ehrlich–Aberth** root finder for \(p(z)=z^n-1\). Let \(\zeta=e^{2\pi i/n}\), and put
\[
\mathbf v(w)=(w\zeta^j)_{j=0}^{n-1},\qquad t=w^n,\qquad B=(n+1)t+n-1.
\]
For every complex \(w\ne0\) with \(B\ne0\), the one-step image is \(\mathcal E(\mathbf v(w))=\mathbf v(\Phi_n(w))\), where
\[
\Phi_n(w)=w\frac{(n-1)w^n+n+1}{(n+1)w^n+n-1}.
\]
If \(w^n=-(n+1)/(n-1)\), this step is defined but collapses all coordinates to zero, so it leaves the pairwise-distinct configuration space. At other admissible \(w\) the image is a nondegenerate regular polygon; further iteration still requires avoiding poles. The full \(n\)-by-\(n\) complex Jacobian at every admissible **input** \(\mathbf v(w)\), including these collapse inputs, is circulant. Its eigenvectors are the Fourier vectors \(\mathbf e_k=(\zeta^{kj})_{j=0}^{n-1}\), for \(1\le k\le n\), and its **entire spectrum** is
\[
\boxed{\lambda_k(w)=\frac{[n^2-1-2(k-1)(n+1-k)](w^n-1)^2}{[(n+1)w^n+n-1]^2}.}
\]
In particular its exact spectral and Euclidean operator norms coincide:
\[
\boxed{\|D\mathcal E(\mathbf v(w))\|_2=\rho(D\mathcal E(\mathbf v(w)))=
\frac{(n^2-1)|w^n-1|^2}{|(n+1)w^n+n-1|^2}.}
\]

For **every real initial radius** \(r>0\), the iteration \(r_{m+1}=\Phi_n(r_m)\) remains positive, never crosses \(1\), and converges monotonically to \(1\). Nonetheless there is a unique exact frontier for *infinitesimal ambient Euclidean nonexpansion*:
\[
\boxed{\|D\mathcal E(\mathbf v(r))\|_2\le1\quad\Longleftrightarrow\quad
r^n\ge\tau_n:=\frac{\sqrt{n^2-1}-(n-1)}{\sqrt{n^2-1}+(n+1)}.}
\]
The Jacobian strictly expands a perturbation in the complex scaling mode \(\mathbf e_1\) whenever \(0<r^n<\tau_n\), despite the convergence of the unperturbed symmetric orbit. For \(r^n>\tau_n\), it strictly contracts all infinitesimal ambient perturbations. At equality the scaling mode is norm-preserved. The orthogonal complement of the scaling mode is strictly contracted for **every** \(r>0\). Each positive-radius regular-polygon configuration lies in an open basin of convergence to the correctly ordered roots.

## Assumptions and scope

Use exact arithmetic in the iteration map \(\mathcal E:\mathbb C^n\dashrightarrow\mathbb C^n\) with coordinates
\[
\mathcal E_i(\mathbf z)=z_i-\frac{p(z_i)}{p'(z_i)-p(z_i)\sum_{j\ne i}(z_i-z_j)^{-1}}.
\]
All \(n\) coordinates update **in parallel**, with no sequential updates, damping, deflation, or floating-point rounding. The domain consists of pairwise-distinct configurations away from poles; an image need not belong to the domain. The normalization \(p(z)=z^n-1\), ordered approximations \(\mathbf v(w)\), and the standard complex Euclidean norm are fixed. The complex Jacobian is the holomorphic derivative, equivalently its complex-linear realification. The scalar convergence statement requires \(r>0\), not arbitrary complex \(w\). The spectral identity remains valid for admissible complex \(w\).

## Proof

**Step 1: regular-polygon reduction and collapse exception.** Write \(z_i=w\zeta^i\). Roots-of-unity identities give
\[
\sum_{j\ne i}\frac1{z_i-z_j}=\frac{n-1}{2z_i},\qquad p(z_i)=t-1,\qquad p'(z_i)=\frac{nt}{z_i}.
\]
Consequently the denominator of the correction equals \(B/(2z_i)\), and substitution yields \(\mathcal E_i(\mathbf v(w))=\Phi_n(w)\zeta^i\). For \(w\ne0\) and \(B\ne0\), the output scale vanishes precisely at \(w^n=-(n+1)/(n-1)\); there \(B=-4n/(n-1)\ne0\). Thus the regular-polygon reduction is an identity in the ambient space, not invariance of the nondegenerate pairwise-distinct domain for all complex inputs.

**Step 2: exact Jacobian.** Denote by \(D_i\) the denominator of the correction. Differentiation in a different coordinate gives, for \(j\ne i\),
\[
\frac{\partial\mathcal E_i}{\partial z_j}=-\frac{p(z_i)^2}{D_i^2(z_i-z_j)^2}
=-\frac{4(t-1)^2}{B^2(1-\zeta^{j-i})^2}.
\]
Thus all off-diagonal entries depend only on \(j-i\pmod n\); the diagonal entries are also independent of \(i\) by the same rotational covariance. The Jacobian is circulant and diagonalized unitarily by the Fourier vectors \(\mathbf e_k\).

For \(S_k=\sum_{\ell=1}^{n-1}\zeta^{k\ell}/(1-\zeta^\ell)^2\), use \(T_k=\sum_{\ell=1}^{n-1}\zeta^{k\ell}/(1-\zeta^\ell)\). Pairing conjugate roots gives \(T_0=(n-1)/2\). Then \(T_1=-(n-1)/2\), and \(T_{k+1}-T_k=1\) for \(1\le k<n\), so \(T_k=k-(n+1)/2\). The difference \(S_{k+1}-S_k=-T_k\) proves
\[
S_k-S_1=\frac{(k-1)(n+1-k)}2,\qquad 1\le k\le n.
\]
The first Fourier vector represents complex scaling (including the real radial direction at positive \(w\)), hence its eigenvalue is \(\Phi_n'(w)\). Direct differentiation gives
\[
\Phi_n'(w)=\frac{(n^2-1)(t-1)^2}{B^2}.
\]
Comparing the off-diagonal Fourier sums to the first eigenvalue yields the displayed entire spectrum, with no approximation.

**Step 3: spectral norm and sharp frontier.** The mode coefficients
\[
C_{n,k}=n^2-1-2(k-1)(n+1-k)
\]
are strictly positive (since \((k-1)(n+1-k)\le n^2/4\)) and have unique maximum \(C_{n,1}=n^2-1\). A circulant is unitarily diagonalizable, so its Euclidean operator norm is precisely the largest eigenvalue modulus. For real \(r>0\), the norm expression is strictly decreasing as a function of \(t=r^n\) on \((0,1)\), from \((n+1)/(n-1)>1\) to zero; for \(t\ge1\) it is smaller than \(1\). Solving \(\sqrt{n^2-1}(1-t)=(n+1)t+n-1\) gives the unique positive threshold \(\tau_n\), proving necessity, sufficiency, and boundary equality.

For \(2\le k\le n\), \((k-1)(n+1-k)\ge n-1\), hence \(C_{n,k}\le(n-1)^2\). Since \((n-1)|t-1|<(n+1)t+n-1\) for all \(t>0\), each such mode has modulus strictly below one on the positive-radius family. Thus any strict expansion there requires a nonzero component in the scaling mode.

**Step 4: monotone global radial convergence and open basin.** Direct algebra gives
\[
\Phi_n(r)-r=\frac{2r(1-r^n)}{(n+1)r^n+n-1},
\]
and the exact factorization
\[
\Phi_n(r)-1=\frac{(r-1)^3}{(n+1)r^n+n-1}
\sum_{j=0}^{n-2}(j+1)(n-1-j)r^j.
\]
All coefficients in the last sum are positive. Therefore radii strictly between zero and one increase without overshooting, while radii greater than one decrease without undershooting. Their limits must be the unique positive fixed point \(1\). The factorization additionally proves cubic local convergence. The Jacobian vanishes at the ordered root vector, giving a Euclidean contracting neighborhood there. Every positive-radius regular-polygon configuration enters that neighborhood after finitely many steps; continuity of the corresponding finite iterate provides an open neighborhood converging to the same ordered roots. This does not claim that all initial configurations converge.

## Verification

The accompanying standard-library Python artifact `verify.py` checks the polynomial and derivative identities by exact integer polynomial arithmetic for degrees \(2\) through \(40\), tests Fourier eigenvalues against coordinate-wise analytic differentiation evaluated numerically at sampled positive radii for degrees \(2\) through \(12\), and checks threshold-side inequalities. These are finite checks; the arbitrary-degree theorem, including the complex collapse exception, is established by the algebraic proof above. Run `python3 verify.py` to perform the supplied checks.

## Relationship to prior work

Grabbel, Srkalovic and Schleicher (arXiv:2611.02143v1, first posted 2026-11-01) give a nonconvergence construction for the Ehrlich–Aberth map in degree at least seven, including full-cycle eigenvalues of an exceptional orbit. Their cycle does not yield a Fourier diagonalization or a sharp norm frontier on the binomial regular-polygon family. Reinke (arXiv:2011.01660) constructs diverging Ehrlich–Aberth orbits and establishes Möbius equivariance; the present claim concerns a separate globally convergent invariant family and its transverse linearization. Shemyakov et al. (arXiv:2004.03217) compare root-finding efficiency and standard local convergence, including evenly spaced initial circles, but do not present this full circulant Jacobian spectrum or the expansion threshold in the accessible complete preprint. Known cubic local convergence is background, not the novelty claim.

## Limitations

No guarantee is made for general polynomials, arbitrary initial configurations, Gauss–Seidel variants, or finite-precision implementations. The frontier concerns a **single-step derivative norm at a symmetric configuration**, not a global nonlinear Lipschitz constant or an obstruction to long-time convergence. A complete historical-priority assessment of all older specialist literature, including original implementations of Aberth's method, remains open. No independent mathematical audit has been performed.

## References

1. Torben Grabbel, Nedim Srkalovic and Dierk Schleicher, *The Ehrlich–Aberth root finder is not generally convergent*, arXiv:2611.02143v1 (2026-11-01), https://arxiv.org/abs/2611.02143.
2. Bernhard Reinke, *Diverging orbits for the Ehrlich–Aberth and the Weierstrass root finders*, arXiv:2011.01660; *Proceedings of the American Mathematical Society* 150 (2022), 1287–1300, https://arxiv.org/abs/2011.01660.
3. Sergey Shemyakov, Roman Chernov, Dzmitry Rumiantsau, Dierk Schleicher, Simon Schmitt and Anton Shemyakov, *Finding polynomial roots by dynamical systems—a case study*, arXiv:2004.03217 (2020), https://arxiv.org/abs/2004.03217.
4. L. W. Ehrlich, *A modified Newton method for polynomials*, *Communications of the ACM* 10 (1967), 107–108, https://doi.org/10.1145/363067.363115.
