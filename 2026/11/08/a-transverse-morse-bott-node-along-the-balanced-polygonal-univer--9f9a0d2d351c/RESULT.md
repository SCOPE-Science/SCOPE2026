# A transverse Morse–Bott node along the balanced polygonal universal-adjoint line

## Finding
Let \(n\geq 8\) be an integer, read subscripts cyclically modulo \(n\), and choose positive real coefficients \(u_1,\ldots,u_n\). In \(\mathbb P^{n-1}_{\mathbb C}\) define the universal-adjoint hypersurface
\[
 X_u=V(F_u),\qquad
 F_u(x)=\sum_{i=1}^n u_i\prod_{j\notin\{i,i+1\}}x_j.
\]
Set \(\mathbb T=\{[x_1:\cdots:x_n]:\prod_i x_i\ne0\}\). The hypersurface is singular in \(\mathbb T\) if and only if
\[
 n\equiv0\pmod4\quad\text{and}\quad
 \prod_{i\ \mathrm{odd}}u_i=\prod_{i\ \mathrm{even}}u_i.
\]
On this balanced locus, the full-torus singular scheme is a smooth, reduced one-dimensional subvariety \(L_u\cap\mathbb T\), where \(L_u\cong\mathbb P^1\) is the projective line given by the cyclic linear recurrence
\[
 x_{i+2}=-\frac{u_{i+1}}{u_i}\,x_i\qquad(i\bmod n).
\]
At **every** point of \(L_u\cap\mathbb T\), the analytic germ of \(X_u\) is the product of a smooth one-dimensional germ and an ordinary quadratic hypersurface singularity of complex dimension \(n-3\): in local analytic coordinates,
\[
 (X_u,p)\simeq\bigl(\{z_1^2+\cdots+z_{n-2}^2=0\},0\bigr)
 \times(\mathbb C,0).
\]
In particular, the ambient hypersurface has transverse multiplicity two along its unique full-torus singular line. For parameters not satisfying the displayed balance, there are no singular points in \(\mathbb T\). This is a classification **on the projective full-coordinate torus only**, not of all singularities on coordinate-boundary strata.

## Assumptions and scope
The coefficients are positive real numbers, as for the signed absolute determinants \(u_i=|\det(U_i,U_{i+1})|\) of consecutive rays of the normal fan of a convex polygon. The proof itself applies to any positive coefficient vector, whether or not it is realizable by such a fan. Regular polygons of \(n=4m\ge8\) sides supply actual fan examples with equal coefficients. The base field for the analytic statement is \(\mathbb C\); characteristic zero is essential for the holomorphic Morse–Bott normal form. For simplicity the degenerate quadrilateral case \(n=4\), already explicitly treated in the motivating paper, is excluded.

## Proof
**1. Convert the Jacobian equations to an alternating cycle.** On the full-coordinate torus put \(P=\prod_{i=1}^n x_i\), \(y_i=u_i/(x_i x_{i+1})\), and \(G=\sum_i y_i\), so \(F_u=PG\). Let \(D_i=x_i\partial/\partial x_i\). At a singular point, \(G=0\), and hence
\[
 D_iF_u=P(G-y_{i-1}-y_i)=-P(y_{i-1}+y_i)=0.
\]
Therefore \(y_i=-y_{i-1}\) for every \(i\). Since every \(u_i\) and \(x_i\) is nonzero, no \(y_i\) vanishes. If \(n\) is odd, the cyclic relations contradict nonvanishing. If \(n\) is even, alternating nonzero \(y_i\) exist. Multiplying the odd- and even-index equations separately gives
\[
 \frac{\prod_{i\ \mathrm{odd}}u_i}{\prod_{i\ \mathrm{even}}u_i}
 =\frac{\prod_{i\ \mathrm{odd}}y_i}{\prod_{i\ \mathrm{even}}y_i}
 =(-1)^{n/2}.
\]
For positive coefficients the ratio on the left is positive, forcing \(4\mid n\) and the stated equality of products. Conversely, if these conditions hold, one may choose arbitrary \(a,b\in\mathbb C^*\), put \(x_1=a,x_2=b\), and use \(x_{i+2}=-u_{i+1}x_i/u_i\). The two cyclic closure conditions are equivalent to the same coefficient balance, so this gives all nonzero solutions to the alternating relations. They have \(G=0\) because \(n\) is even, and their logarithmic derivatives all vanish. Thus they are precisely the full-torus singular points.

**2. The solution set is a line, not merely a parametrized curve.** The recurrence is linear in the coordinates and preserves parity. Every odd-index coordinate is a fixed nonzero scalar multiple of \(a\), and every even-index coordinate is a fixed nonzero scalar multiple of \(b\). Hence the solutions in projective space are exactly the full-coordinate points of a projective line \(L_u\). Its two endpoints have one parity of coordinates zero; they also belong to the projective singular locus by Zariski closedness, but no assertion about their analytic transverse type is made.

**3. Compute the complete normal Hessian.** At any full-torus singular point, apply \(D_jD_i\) to \(F_u=PG\). Using \(y_{i-1}+y_i=0\), its entries are
\[
 (D_jD_iF_u)_p=
 \begin{cases}
 P(p)y_i(p),&j=i+1,\\
 P(p)y_{i-1}(p),&j=i-1,\\
 0,&\text{otherwise}.
 \end{cases}
\]
The diagonal entries are zero. This is the weighted adjacency matrix of an \(n\)-cycle whose consecutive edge weights alternate between two opposite nonzero numbers. If \(w=(w_1,\ldots,w_n)\) belongs to its kernel, the equation at vertex \(i\) reduces to \(w_{i+1}=w_{i-1}\). Because \(n\) is even, its nullspace consists exactly of the two-periodic vectors and has dimension two. Thus the logarithmic Hessian, and hence the ordinary affine Hessian (obtained by invertible diagonal changes of coordinates at a critical point), has rank exactly \(n-2\).

The affine two-dimensional nullspace consists of the scale and line-parameter directions. Passing to a projective affine chart removes the scale direction and leaves a one-dimensional Hessian nullspace tangent to \(L_u\cap\mathbb T\). Since the critical locus is exactly this smooth line there, the holomorphic Morse–Bott lemma splits off its one-dimensional parameter and diagonalizes the nondegenerate normal quadratic form. The resulting hypersurface equation is the claimed sum of \(n-2\) squares. Moreover, in these coordinates the Jacobian ideal is generated by the normal coordinates, so the full-torus singular scheme is reduced and equal to \(L_u\cap\mathbb T\). This completes the proof.

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic and the original sum-of-monomials formula. It constructs points on the singular line for \(n=8,12,16\) with equal coefficients, plus \(n=8\) with nonconstant positive rational balanced coefficients. In each case it verifies \(F=0\), all ordinary partial derivatives vanish, the full Hessian has rank \(n-2\), and the matrix agrees entrywise with the logarithmic Hessian formula. Run `python3 verify.py`; the successful last line is `EXACT_BALANCED_ADJOINT_CHECKS_PASS`. These are finite corroborations only: the all-\(n\) assertion follows from the symbolic recurrence and exact Hessian-kernel argument above.

## Relationship to prior work
Telen, *Toric Amplitudes and Universal Adjoints* (arXiv:2504.00897), Theorem 7.11, proves that outside the balance and divisibility conditions there are no singular points off the toric irrelevant locus. His proof obtains the alternating kernel of a monomial-image matrix and its toric binomial compatibility. His Example 7.12 exhibits a singular line for one balanced octagon, and his quadrilateral example identifies a reducible quadric. We do **not** claim novelty for the necessary balance condition, its matrix-kernel reformulation, the octagonal example, or general Morse–Bott theory. The present calculation establishes the converse simultaneously for every positive-weight polygonal cyclic adjoint and identifies the exact full-torus singular scheme and transverse analytic ordinary-double-point normal form at every such point. Kohn and Ranestad study Warren–Wachspress adjoints on the original polygon plane and Wachspress varieties; those are distinct from the full universal-adjoint hypersurface in \(\mathbb P^{n-1}\) and do not imply its transverse analytic classification.

## Limitations
The theorem does not classify singularities where any homogeneous coordinate vanishes. In particular it does not determine the local analytic type at either endpoint of \(L_u\) or enumerate components contained in the irrelevant locus. The coefficient balance describes singularities in the full-coordinate torus, not the entire projective discriminant (boundary singularities may exist for all coefficients). No independent mathematical validation or historical-priority certification has been performed. A general toric-discriminant or Laurent-polynomial critical-locus theorem could encompass the stated family under another name; this remains a literature-priority risk.

## References
1. S. Telen, *Toric Amplitudes and Universal Adjoints*, arXiv:2504.00897, first submitted 2025-04-01; *Journal of the London Mathematical Society* 113 (2026), e70468, DOI: 10.1112/jlms.70468. Primary text: https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.70468 . In particular Theorem 7.11 and Example 7.12.
2. K. Kohn and K. Ranestad, *Projective Geometry of Wachspress Coordinates*, arXiv:1904.02123, *Foundations of Computational Mathematics* 20 (2020), 1135–1173, DOI: 10.1007/s10208-019-09441-z. Primary text: https://link.springer.com/article/10.1007/s10208-019-09441-z .
