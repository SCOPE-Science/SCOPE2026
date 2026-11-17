# All-bandwidth determinant factorization and chamber-unique spherical ring designs

## Finding

For each integer \(L\geq2\), place one sampling node at the south pole and \(2j+1\) equally spaced nodes on an independently rotated nonpolar latitude circle of height \(x_j\), for every \(1\leq j<L\). Let \(M_L\) be the square evaluation matrix for the standard orthonormal complex spherical harmonics of degrees \(0,\ldots,L-1\). Fix \(x_0=-1\). Then

\[
\boxed{\left|\det M_L\right|^2=C_L\prod_{j=1}^{L-1}(1-x_j^2)^{j(j+1)}\prod_{0\leq i<j<L}|x_j-x_i|^{2(2i+1)}.}
\]

The positive, explicit constant \(C_L\), defined below, depends only on the bandlimit. It is independent of all independent rotations of the rings. Consequently, the samples interpolate every degree-bounded spherical polynomial if and only if all nonpolar ring heights are pairwise distinct.

Moreover, on the domain \(x_1,\ldots,x_{L-1}\in(-1,1)\), with all heights distinct, the squared determinant has **exactly \((L-1)!\) strict local maxima**: one and only one in each strict height-ordering chamber. Each is nondegenerate; its logarithm has everywhere negative-definite Hessian on that chamber. Thus every ordering chamber has a uniquely solvable smooth, strictly concave determinant-design problem, although the global best ordering is not classified here.

## Assumptions and scope

The sphere is the unit \(\mathbb S^2\), and the harmonics are orthonormal with respect to its full-area measure. All \(L^2=\sum_{j=0}^{L-1}(2j+1)\) samples have equal weight in the evaluation determinant. On ring \(j\), with \(1\leq j<L\), nodes have polar coordinate \(\cos\theta=x_j\), and longitudes \(\phi_j+2\pi r/(2j+1)\) for \(0\leq r\leq2j\), where \(\phi_j\) is arbitrary. The polar node has \(x_0=-1\) and an irrelevant longitude. The coefficients are \(Y_\ell^m\) with \(0\leq\ell<L\) and \(-\ell\leq m\leq\ell\), in any fixed order; the squared determinant is order-independent.

Define the positive normalizers and polynomial leading coefficients

\[
 N_{\ell,k}^{2}=\frac{2\ell+1}{4\pi}\frac{(\ell-k)!}{(\ell+k)!},\qquad
 a_{\ell,k}=\frac{(2\ell)!}{2^\ell\ell!(\ell-k)!},\quad 0\le k\le\ell.
\]

The constant is explicitly

\[
 C_L=\prod_{j=0}^{L-1}(2j+1)^{2j+1}
 \prod_{m=-(L-1)}^{L-1}\prod_{\ell=|m|}^{L-1}
 N_{\ell,|m|}^{2}a_{\ell,|m|}^{2}.
\]

No condition-number claim or uniform-in-bandlimit stability assertion is made. No global optimal height ordering is asserted.

## Proof

**1. Angular Fourier triangularization.** On the ring with \(2j+1\) nodes apply its unitary discrete Fourier transform to the evaluation rows. For each Fourier residue \(q\in\{-j,\ldots,j\}\), a column of azimuthal order \(m\) contributes only if \(m\equiv q\pmod{2j+1}\). If \(|m|<|q|\), this is impossible: \(m\) and \(q\) lie in an interval of length less than \(2j+1\) and are unequal. Order the Fourier-transformed rows by decreasing absolute residue and the harmonic columns by decreasing absolute order. The transformed matrix is block upper triangular, with one diagonal block for each signed azimuthal order \(m\). Its rows are precisely \(j=|m|,\ldots,L-1\), and its columns are \(\ell=|m|,\ldots,L-1\). The block entries have absolute-value-equivalent form

\[
 (B_m)_{j\ell}=\sqrt{2j+1}\,N_{\ell,|m|}\,
 (1-x_j^2)^{|m|/2}\,\frac{d^{|m|}}{dx^{|m|}}P_\ell(x_j),
\]

up to row phases of modulus one and column signs of modulus one. Here \(P_\ell\) is the ordinary Legendre polynomial; the signs account for the associated-Legendre convention and negative orders. In particular, angular phases cannot affect the determinant magnitude.

**2. Vandermonde evaluation.** For \(k=|m|\), the polynomials \(P_\ell^{(k)}\), \(k\leq\ell<L\), have consecutive degrees \(0,1,\ldots,L-k-1\) and leading coefficients \(a_{\ell,k}\). Therefore

\[
 |\det B_m|^2=\left(\prod_{j=k}^{L-1}(2j+1)(1-x_j^2)^k\right)
 \left(\prod_{\ell=k}^{L-1}N_{\ell,k}^2 a_{\ell,k}^2\right)
 \left(\prod_{k\le i<j<L}|x_j-x_i|^2\right).
\]

Multiply this equality over \(m=-(L-1),\ldots,L-1\). A fixed ring \(j\) occurs in \(2j+1\) blocks and contributes the factor \((2j+1)^{2j+1}\). Its \((1-x_j^2)\) exponent is \(\sum_{m=-j}^{j}|m|=j(j+1)\). A pair \(i<j\) appears in precisely \(2i+1\) blocks, so its distance exponent is \(2(2i+1)\). This proves the displayed determinant formula and the exact nonsingularity criterion.

**3. Strict concavity in each height-ordering chamber.** Removing the positive constant, define

\[
 F_L(x)=\sum_{j=1}^{L-1}j(j+1)\log(1-x_j^2)
 +\sum_{0\le i<j<L}2(2i+1)\log|x_j-x_i|,
 \qquad x_0=-1.
\]

On every strict height-ordering chamber, \(F_L\) is smooth, and for any nonzero real vector \(v=(v_1,\ldots,v_{L-1})\), setting \(v_0=0\) yields

\[
 v^{\mathsf T}(\nabla^2F_L)v
 =-\sum_{j=1}^{L-1}\frac{2j(j+1)(1+x_j^2)}{(1-x_j^2)^2}v_j^2
 -\sum_{0\le i<j<L}\frac{2(2i+1)}{(x_j-x_i)^2}(v_j-v_i)^2<0.
\]

Every ordering chamber is a nonempty open convex polytope. At each of its boundary points, at least one height approaches a pole or two heights collide; the corresponding logarithmic factor tends to \(-\infty\), and all other logarithmic terms remain bounded above. Therefore each chamber has a global interior maximum. Strict concavity makes it unique, and the displayed Hessian makes it nondegenerate. Distinct chambers are separated by zero-determinant collisions, which cannot be local maxima; hence the entire nonsingular domain contains exactly \((L-1)!\) local maxima.

**4. Explicit critical equations.** Each unique chamber maximizer solves, for every \(1\leq j<L\),

\[
 -\frac{2j(j+1)x_j}{1-x_j^2}
 +\sum_{i=0}^{j-1}\frac{2(2i+1)}{x_j-x_i}
 +\sum_{k=j+1}^{L-1}\frac{2(2j+1)}{x_j-x_k}=0.
\]

Within its prescribed chamber this system has exactly one solution, and its negative-definite Hessian provides a local stability and uniqueness certificate.

## Verification

The standalone file `CHECKER.py` recomputes the exact normalizing constant in rational arithmetic, compares direct complex evaluation determinants with the product formula over independently rotated rings at several bandlimits, and checks the differentiated logarithmic energy. Run it in the same directory with `python CHECKER.py`; NumPy, SciPy and SymPy are required. The finite tests corroborate, but do not replace, the proof above.

For an independent small-degree normalization check, \(C_2=729/(1024\pi^4)\) and \(C_3=5189853515625/(1073741824\pi^9)\). The former yields a single-ring optimal height of \(1/3\). The latter specializes to the known nine-node determinant identity; no novelty is claimed for that special case.

## Relationship to prior work

The ring counts \(1,3,\ldots,2L-1\) and their per-order associated-Legendre sampling matrices are established by Khalid, Kennedy and McEwen (2014) and studied by Nafees and collaborators (2017). Those papers optimize conditioning of per-order systems, rather than the global determinant, and do not state the explicit all-bandwidth weighted Vandermonde product or the one-maximizer-per-ordering landscape. The latter result builds on their triangular Fourier structure, not a new ring construction.

Dell'Accio, Nudo, Pérez and Piñar (2026) treat spherical interpolation–regression with rank conditions on Vandermonde matrices and provide the recent motivation for exact finite sample design; their main theorem concerns constrained least-squares reconstruction and symmetry, not the present ring determinant. Haines (2024) considers optimal regression designs through spherical designs, a different feasible design class and criterion. A previously reported quadratic-band nine-node determinant is included as a special case, but its closed-form optimal heights are not a new contribution here. An older factorization implicit in interpolation or weighted Fekete-design literature remains a genuine priority risk.

## Limitations

The strict maxima are classified **within** each permutation chamber, not ranked across chambers. The overall largest value is the maximum over these finitely many unique chamber maxima, but no all-degree formula for the best permutation is proved. Determinant maximization does not imply best spectral condition number or smallest reconstruction error. The polar choice fixes the global rotation gauge; no theorem about arbitrary displaced single-point rings is claimed.

## References

- F. Dell'Accio, F. Nudo, T. E. Pérez and M. A. Piñar, *Polynomial interpolation–regression on the sphere*, arXiv:2605.13124, first posted May 13, 2026. https://arxiv.org/abs/2605.13124
- Z. Khalid, R. A. Kennedy and J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661 (2014). https://arxiv.org/abs/1403.4661
- W. Nafees, Z. Khalid, R. A. Kennedy and J. D. McEwen, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations*, arXiv:1709.02497 (2017). https://arxiv.org/abs/1709.02497
- L. M. Haines, *Optimal designs for spherical harmonic regression*, *Statistical Papers*, published December 9, 2024. https://doi.org/10.1007/s00362-024-01630-5
