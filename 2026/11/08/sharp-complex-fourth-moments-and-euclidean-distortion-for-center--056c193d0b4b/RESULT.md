# Sharp complex fourth moments and Euclidean distortion for centered affine functions on simplices

## Finding
Let \(m\ge3\), let \(\Delta\) be any nondegenerate real \((m-1)\)-simplex with normalized uniform volume measure, and let \(\lambda_1,\ldots,\lambda_m\) be its barycentric coordinate functions. For each nonzero vector \(z=(z_1,\ldots,z_m)\in\mathbb C^m\) satisfying \(\sum_jz_j=0\), set \(f_z=\sum_jz_j\lambda_j\). Then the **complete sharp normalized fourth-moment range** is
\[
\boxed{\frac{2(m+1)}{m+2}\ \le\ \frac{\int_\Delta|f_z|^4}{(\int_\Delta|f_z|^2)^2}\ \le\ \frac{3(m+1)(3m^2-7m+6)}{(m-1)(m+2)(m+3)}.}\tag{1}
\]
The lower equality cases are precisely the nonzero vectors satisfying
\[
|z_1|=\cdots=|z_m|,\qquad \sum_jz_j=\sum_jz_j^2=0.\tag{2}
\]
They exist for **every** \(m\ge3\), by taking all \(m\)-th roots of unity as coefficients. For \(m\ge4\), the upper equality cases are precisely complex scalar multiples and permutations of \((m-1,-1,\ldots,-1)\). For \(m=3\), upper equality consists of all nonzero complex scalar multiples of real zero-sum vectors. Every value between the endpoints is attained.

Let \(X_m\) denote this complex \((m-1)\)-dimensional centered affine space with its \(L^4(\Delta)\) norm. Its exact **complex-linear multiplicative Banach--Mazur distance** to complex Euclidean space is
\[
\boxed{d_{\mathrm{BM}}(X_m,\ell_2^{m-1}(\mathbb C))^4
=\frac{3(3m^2-7m+6)}{2(m-1)(m+3)}.}\tag{3}
\]
In particular, \(d_{\mathrm{BM}}^4\to9/2\), so the optimal distortion stays bounded as dimension grows. The ambient coefficient \(L^2\) inner product already gives an optimal Euclidean structure.

## Assumptions and scope
Volume is normalized to one, \(\lambda_j\ge0\) and \(\sum_j\lambda_j=1\) on \(\Delta\). The coefficients are complex and the affine function is centered because \(\mathbb E\lambda_j=1/m\). The simplex may have any shape: barycentric coordinates carry the uniform simplex law to the symmetric Dirichlet distribution with parameters \((1,\ldots,1)\). Write
\[
P=\sum_j|z_j|^2>0,\qquad Q=\sum_jz_j^2,\qquad R=\sum_j|z_j|^4,\qquad
c_m=\frac{m(m+1)}{(m+2)(m+3)}.\tag{4}
\]
The norm in (3) uses complex-linear isomorphisms and \(d_{\mathrm{BM}}(X,Y)=\inf_T\|T\|\,\|T^{-1}\|\), not its logarithm. The target Euclidean space has complex dimension \(m-1\).

## Proof
**1. Exact Dirichlet moments.** For nonnegative integers \(k_j\), the normalized simplex moment is
\[
\mathbb E\prod_{j=1}^m\lambda_j^{k_j}
=\frac{\prod_{j=1}^mk_j!}{m(m+1)\cdots(m+K-1)},\qquad K=\sum_jk_j.\tag{5}
\]
For \(Y=\sum_jz_j\lambda_j\) and formal variables \(u,v\), expanding (5) gives
\[
\sum_{r,s\ge0}\frac{(m)_{r+s}}{r!s!}\mathbb E[Y^r\overline Y^{\,s}]u^rv^s
=\prod_{j=1}^m(1-u z_j-v\overline z_j)^{-1}.\tag{6}
\]
Here \((m)_k=m(m+1)\cdots(m+k-1)\). Since \(\sum_jz_j=0\), the linear terms in the logarithm of the right side vanish. Its homogeneous degree-two terms are \(Qu^2/2+Puv+\overline Qv^2/2\); the coefficient of \(u^2v^2\) in the degree-four logarithm is \(3R/2\). Therefore coefficient extraction gives
\[
\mathbb E|Y|^2=\frac P{m(m+1)},\qquad
\mathbb E|Y|^4=\frac{2P^2+|Q|^2+6R}{m(m+1)(m+2)(m+3)}.\tag{7}
\]
Thus, defining \(K(z)=\mathbb E|Y|^4/(\mathbb E|Y|^2)^2\),
\[
K(z)=c_m\left(2+\frac{|Q|^2}{P^2}+6\frac R{P^2}\right).\tag{8}
\]

**2. Sharp lower bound and exact stability.** Cauchy--Schwarz gives \(R\ge P^2/m\), with equality exactly when all \(|z_j|\) agree. Also \(|Q|^2\ge0\). Hence
\[
\boxed{K(z)-\frac{2(m+1)}{m+2}
=\frac{c_m}{P^2}\left(|Q|^2+6\sum_{j=1}^m\left(|z_j|^2-\frac Pm\right)^2\right).}\tag{9}
\]
The right side vanishes exactly for (2). Taking \(z_j=e^{2\pi i(j-1)/m}\) gives both \(\sum z_j=0\) and \(\sum z_j^2=0\) for every integer \(m\ge3\); this proves sharpness in all dimensions. The two nonnegative terms in (9) separately measure phase cancellation and modulus imbalance.

**3. Spectral fourth-power lemma.** For each real zero-sum vector \(x\in\mathbb R^m\),
\[
\sum_jx_j^4\le u_m\left(\sum_jx_j^2\right)^2,
\qquad u_m=\frac{m^2-3m+3}{m(m-1)}.\tag{10}
\]
For \(m=3\), direct expansion gives equality for every real zero-sum vector (and for \(m=2\) the same elementary identity holds). Suppose \(m\ge4\), normalize \(\sum x_j^2=1\) and maximize the fourth sum on the zero-sum sphere. Lagrange multipliers imply every coordinate is a root of the depressed cubic \(4t^3-2\alpha t-\beta\), giving at most three distinct values. If all three values \(a<b<c\) occur, then \(a+b+c=0\). The second derivative of the constrained Lagrangian equals the cubic derivative, strictly positive at \(a\) and \(c\). Repeating either extremal coordinate would permit the tangent variation \((+1,-1)\) between two equal coordinates, with positive constrained second variation, impossible at a maximum. Thus \(a,c\) occur once each and \(b\) occurs \(m-2\) times. The root-sum and zero-sum equations force \((m-3)b=0\), hence \(b=0\) and \(a=-c\); the corresponding ratio is \(1/2\), strictly below \(u_m\) for \(m\ge4\). Every maximizing vector thus has only two coordinate levels. If the levels have multiplicities \(k,m-k\), substituting the zero-sum condition gives the ratio \(m/[k(m-k)]-3/m\), largest exactly at \(k=1\) or \(m-1\). This yields (10), with the indicated outlier equality patterns.

For complex \(z=x+iy\), both \(x\) and \(y\) are real zero-sum. By (10) and Cauchy--Schwarz,
\[
\begin{aligned}
R&=\sum_j(x_j^2+y_j^2)^2\\
&\le\left(\sqrt{\sum_jx_j^4}+\sqrt{\sum_jy_j^4}\right)^2
\le u_m\left(\sum_j(x_j^2+y_j^2)\right)^2=u_mP^2.
\end{aligned}\tag{11}
\]
Also \(|Q|\le P\), with equality exactly when all nonzero \(z_j^2\) have the same argument, equivalently \(z\) is a complex scalar multiple of a real vector. Substitution in (8) gives \(K\le c_m(3+6u_m)\), which simplifies to the upper endpoint in (1). Equality forces common phase and real equality in (10). For \(m\ge4\), exactly the stated outlier patterns occur. For \(m=3\), every common-phase real zero-sum vector attains equality. Both endpoints are attained; the unit sphere in the complex zero-sum hyperplane is connected, so continuity yields every intermediate value.

**4. Optimal Euclidean norm and complex Banach--Mazur distance.** Let \(q\) be an arbitrary positive-definite Hermitian quadratic form on this space, and choose optimal constants \(\alpha,\beta>0\) with \(\alpha\|f_z\|_4^2\le q(z)\le\beta\|f_z\|_4^2\). Coordinate permutations preserve the simplex integral and the centered coefficient hyperplane. Averaging \(q\) over all permutations preserves these inequalities and does not increase \(\sqrt{\beta/\alpha}\). A permutation-invariant Hermitian form on the complex zero-sum hyperplane is necessarily a positive multiple of \(P\): its matrix can be extended by zero on the constant line, and permutation invariance forces one common diagonal and one common off-diagonal entry. Thus the optimal Euclidean quadratic form is \(P\). For this form the fourth power of its radial distortion equals \(K_{\max}/K_{\min}\), because \(\|f_z\|_2^2=P/[m(m+1)]\). Division of the sharp endpoints in (1) proves (3).

## Verification
The standalone `verify.py` program uses exact rational arithmetic for normalized Dirichlet moments of Gaussian-integer coefficient tuples. It independently computes the fourth moment by expanding all four barycentric indices with factorial weights, and compares this with (7). It also checks the upper equality family in dimensions \(3\) to \(74\), the algebraic Banach--Mazur ratio, the explicit nonnegative identity (9), and the real triangle identity on a finite lattice. Floating-point roots-of-unity checks confirm lower equality in dimensions \(3\) to \(59\). These finite computations are diagnostic only; the preceding proof establishes all integer dimensions \(m\ge3\).

## Relationship to prior work
Baldoni, Berline, De Loera, Köppe and Vergne developed general methods for integrating polynomials over simplices (2008), supplying the Dirichlet moment setting behind (5); their investigated integration statements do not provide the sharp complex \(L^4/L^2\) optimization and geometric equality classification. Cahill, Fickus, Mixon, Poteet and Strawn (2011) analyze tight frame realizations, relevant to equal-modulus phase-balanced design conditions but not the affine-simplex fourth-moment space. The published note *Exact complex Euclidean distortion of zero-sum \(\ell_4\) hyperplanes* (2026) establishes (10) in a complex coordinate norm and its own exact distance; the new simplex norm is an **integrated Dirichlet norm**, has the additional nonnegative \(|Q|^2\) interaction, and has uniformly bounded distortion as dimension tends to infinity, whereas the coordinate norm has unbounded Euclidean distortion. The present proof independently reconstructs the needed zero-sum fourth-power lemma and applies it to a distinct norm. Earlier results for real affine functions on a triangle concern a real subspace; in the complex triangle the ratio instead spans \([8/5,12/5]\), exhibiting a genuine scalar-field distinction.

## Limitations
All statements concern complex-valued **centered affine** functions with uniform volume measure on a nondegenerate simplex of real dimension at least two and exponent four. No analogous sharp theorem for other exponents, higher-degree polynomials, nonuniform Dirichlet parameters, vector-valued norms, or real-only coefficient spaces in arbitrary dimensions is claimed. The full phase-design lower equality family is characterized by algebraic conditions, not enumerated modulo every finite symmetry. The method combines classical moment integration, a zero-sum fourth-power inequality, and permutation symmetrization; a semantically equivalent specialized historical result could exist outside the inspected sources.

## References
1. V. Baldoni, N. Berline, J. A. De Loera, M. Köppe, M. Vergne, *How to Integrate a Polynomial over a Simplex*, arXiv:0809.2083v1 (first submitted 2008-09-11), https://arxiv.org/abs/0809.2083. The open paper's definitions and integration-method sections were inspected.
2. J. Cahill, M. Fickus, D. G. Mixon, M. J. Poteet, N. K. Strawn, *Constructing finite frames of a given spectrum and set of lengths*, arXiv:1106.0921v1 (first submitted 2011-06-05), https://arxiv.org/abs/1106.0921. The open introduction and frame-construction statements were inspected.
3. *Exact complex Euclidean distortion of zero-sum \(\ell_4\) hyperplanes* (2026), published mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-complex-euclidean-distortion-of-zero-sum-ell-4-hyperplanes--f5d77d1ed7ff. The theorem and complete proof were inspected for overlap.
