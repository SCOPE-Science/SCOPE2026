# Sharp sixth-moment geometry of centered affine functions on tetrahedra

## Finding
Let \(T\subset\mathbb R^3\) be any nondegenerate tetrahedron with normalized uniform volume measure, and let \(f:T\to\mathbb R\) be any nonzero affine function with mean zero. Then
\[
\boxed{\frac{125}{21}\le\frac{\|f\|_6^6}{\|f\|_2^6}\le\frac{9875}{567}.}
\]
Both constants are sharp independently of tetrahedron shape. The lower equality holds if and only if its four vertex values are proportional, up to permutation, to \((1,1,-1,-1)\). The upper equality holds if and only if they are proportional, up to permutation, to \((3,-1,-1,-1)\). These are all equality cases.

More precisely, if the four real vertex values are \(a_1,\ldots,a_4\), put \(S_2=\sum_i a_i^2>0\), \(S_3=\sum_i a_i^3\), and \(E_4=\prod_i a_i\). Then \(\sum_i a_i=0\) and
\[
\frac{\|f\|_6^6}{\|f\|_2^6}=\frac{2000}{21}\left(\frac18+\frac{S_3^2}{9S_2^3}-\frac{E_4}{S_2^2}\right).
\]
The two sharp deficits split into independently nonnegative spectral-invariant terms:
\[
\begin{aligned}
\frac{\|f\|_6^6}{\|f\|_2^6}-\frac{125}{21}
&=\frac{2000}{21}\left[\frac{S_3^2}{9S_2^3}+\left(\frac1{16}-\frac{E_4}{S_2^2}\right)\right],\\
\frac{9875}{567}-\frac{\|f\|_6^6}{\|f\|_2^6}
&=\frac{2000}{21}\left[\left(\frac1{27}-\frac{S_3^2}{9S_2^3}\right)+\left(\frac{E_4}{S_2^2}+\frac1{48}\right)\right].
\end{aligned}
\]
Each parenthesized or squared term is nonnegative for every admissible vertex-value vector.

## Assumptions and scope
All scalars are real; the norm \(\|f\|_p=(\int_T |f|^p\,d\mu_T)^{1/p}\) uses uniform probability measure \(\mu_T\). A tetrahedron is nondegenerate if its vertices are affinely independent. Affine coordinate change does not affect the formula, since it maps uniform probability measure onto uniform probability measure and preserves the vertex-value tuple. No assertion is made about nonlinear polynomials, different dimensions, nonuniform measures, or other exponents.

## Proof
Write \(\lambda_1,\ldots,\lambda_4\) for barycentric coordinates. Their distribution under uniform volume measure is \(\mathrm{Dirichlet}(1,1,1,1)\); thus \(f=\sum_i a_i\lambda_i\) and its mean is \(\frac14\sum_i a_i\). For every nonnegative integer \(k\), the exact simplex integration identity is
\[
\mathbb E f^k=\frac{k!\,3!}{(k+3)!}\,h_k(a_1,a_2,a_3,a_4),
\]
where \(h_k\) is the complete homogeneous symmetric polynomial of degree \(k\). This follows by expanding the power and applying \(\mathbb E\prod_i\lambda_i^{b_i}=3!\prod_i b_i!/(k+3)!\) for \(\sum_i b_i=k\).

Since \(\sum_i a_i=0\), Newton's identities give \(e_2=-S_2/2\), \(e_3=S_3/3\), \(e_4=E_4\). The generating identity \(\sum_{k\ge0}h_k t^k=(1-e_1t+e_2t^2-e_3t^3+e_4t^4)^{-1}\) yields
\[
h_2=\frac{S_2}{2},\qquad h_6=\frac{S_2^3}{8}+\frac{S_3^2}{9}-S_2 E_4.
\]
Therefore \(\mathbb E f^2=S_2/20\), \(\mathbb E f^6=h_6/84\), and the displayed exact ratio follows.

For all four real values with zero sum, four elementary, sharp inequalities hold:
\[
-\frac1{48}\le\frac{E_4}{S_2^2}\le\frac1{16},\qquad \frac{S_3^2}{S_2^3}\le\frac13.
\]
The product upper bound is AM--GM applied to the four nonnegative squares: \(\prod_i a_i^2\le(S_2/4)^4\). Equality requires equal absolute values; the zero-sum condition then requires exactly two positive and two negative values. For the lower bound on the product, a negative product forces three nonzero entries to have one sign and one to have the other (or vice versa). Write the outlier magnitude as \(b>0\) and the other magnitudes \(u,v,w>0\), with \(u+v+w=b\). By Cauchy--Schwarz and AM--GM,
\[
S_2=b^2+u^2+v^2+w^2\ge\frac43 b^2,\qquad
|E_4|=buvw\le\frac{b^4}{27}\le\frac{S_2^2}{48}.
\]
Equality is possible exactly when \(u=v=w=b/3\), giving the \((3,-1,-1,-1)\) pattern. A nonnegative product automatically satisfies the lower product bound.

For the cubic bound, normalize \(S_2=1\). The smooth function \(S_3\) attains extrema on the compact sphere cut out by \(\sum_i a_i=0\). Lagrange multipliers show that each coordinate solves a common quadratic equation, \(3a_i^2=\alpha+2\beta a_i\), so there are at most two distinct values. A multiplicity split of \(k\) and \(4-k\) gives \(|S_3|=|4-2k|/\sqrt{4k(4-k)}\) for \(k=1,2,3\). These are \(1/\sqrt3,0,1/\sqrt3\), respectively. Thus \(S_3^2/S_2^3\le1/3\), with equality exactly for the one-versus-three pattern. The constraint gradients are independent on the unit zero-sum sphere, so the multiplier argument exhausts extrema.

The exact two deficit identities follow algebraically from the moment formula. Their constituent terms are all nonnegative by the preceding inequalities. Equality at the lower endpoint requires \(E_4/S_2^2=1/16\), hence exactly the balanced two-versus-two patterns; it also has \(S_3=0\). Equality at the upper endpoint requires simultaneously \(S_3^2/S_2^3=1/3\) and \(E_4/S_2^2=-1/48\), which hold exactly in the one-versus-three patterns. Substitution gives the stated rational constants. This proves all assertions for every tetrahedron.

## Verification
The standalone `verify.py` symbolically expands all sixth-degree complete homogeneous polynomial terms after imposing the zero-sum constraint. It verifies the sixth-moment polynomial and both exact deficit identities in rational arithmetic, checks both sharp endpoint patterns, and independently reconstructs Dirichlet mixed-moment normalizations. Run `python verify.py` with SymPy installed. Its finite symbolic checks corroborate the algebra; the global inequalities and equality classes follow from the analytic AM--GM, Cauchy--Schwarz and Lagrange-multiplier arguments above.

## Relationship to prior work
Baldoni, Berline, De Loera, Köppe and Vergne prove general polynomial integration formulas and algorithms on simplices; their general integration framework supplies moment calculations, not the two optimal sixth-moment constants or full equality cases. Gravin, Pasechnik, Shapiro and Shapiro develop general polytope moment generating functions. The new claim here is specifically the **sharp two-sided optimization of the normalized sixth moment over the complete real centered affine space on a tetrahedron**, together with exact nonnegative extremality deficits. General moment formulas alone must be supplemented by the constrained sharp cubic and product bounds to recover it. The absence of an indexed identical statement cannot rule out unindexed specialized norm-inequality literature.

## Limitations
This is a finite-dimensional, single-exponent theorem, not a dimension-free inequality, a classification for all exponents, or a claim about arbitrary functions. SymPy checks are exact for the explicit polynomial identities, but independent mathematical audit is not provided. Equivalent sharp bounds might exist in historical norm-comparison sources not accessible in the inspected literature.

## References
1. V. Baldoni, N. Berline, J. A. De Loera, M. Köppe, M. Vergne, *How to integrate a polynomial over a simplex*, arXiv:0809.2083, first public September 11, 2008; *Mathematics of Computation* 80 (2011), 297–325.
2. N. Gravin, D. Pasechnik, B. Shapiro, M. Shapiro, *On moments of a polytope*, arXiv:1210.3193, first public October 11, 2012.
