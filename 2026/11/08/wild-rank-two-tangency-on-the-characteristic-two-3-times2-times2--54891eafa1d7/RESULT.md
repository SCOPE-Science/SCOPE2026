# Wild rank-two tangency on the characteristic-two \(3\times2\times2\) hyperdeterminant

## Finding
Let \(k\) be algebraically closed of characteristic two. Let \(\mathcal H\subset\mathbb P^{11}_k\) be the degree-six boundary-format hyperdeterminantal hypersurface of \(3\times2\times2\) tensors. At a rank-two flattening whose kernel line is tangent to the Segre quadric, the scheme-theoretic singular locus has an exact six-dimensional transverse-chart presentation with Jacobian ideal
\[
J=(x^2,xy,y^2,tx,ty)=(x,y)^2+t(x,y).
\]
Consequently a transverse fiber at this rank-two tangency has length three, with algebra \(k[x,y]/(x,y)^2\), whereas the generic transverse fiber at an ordinary rank-two point is reduced of length one. In characteristic not two, the corresponding tangent fiber has length two. Over the function field of the tangency divisor in characteristic two, the unique geometric contact point is defined by a purely inseparable quadratic extension.

## Assumptions and scope
Work in projective space of \(3\times4\) matrices, identifying the four columns with the basis of \(k^2\otimes k^2\). Write \(p_0,p_1,p_2,p_3\) for signed maximal minors of a \(3\times4\) matrix; the hyperdeterminant, up to an overall scalar, is \(p_0p_3-p_1p_2\). Its vanishing for matrices of rank three is equivalent to the one-dimensional kernel being represented by a decomposable tensor. When the rank is two or lower, all four maximal minors vanish.

The local calculation is valid near the displayed rank-two matrices, in the open Grassmannian chart where the second and fourth columns form an independent pair, and near the tangency divisor where \(1+c\) is a unit. No claim is made about the complete singular scheme at lower ranks or the behavior at every point of the closure of the tangency divisor. The comparison with odd characteristic refers to the same standard transverse model at its tangent binary quadratic.

## Proof
**1. A complete transverse coordinate chart.** In the open set of rank at least two where columns two and four form an independent pair, ordinary invertible row operations and affine coordinate choices put the matrix in the form
\[
N=\begin{pmatrix}
-a&1&-(1+c)&0\\
-b&0&-d&1\\
y&0&-x&0
\end{pmatrix}.
\]
The six displayed variables \(a,b,c,d,x,y\), together with six free parameters describing the two pivot columns and the chosen third-row complement, form regular coordinates on an affine neighborhood of the original rank-two matrix. Row operations only multiply the maximal minors by a unit, so they preserve the local hypersurface and its Jacobian singular scheme up to an étale/local-coordinate isomorphism. The rank-two locus on this chart is exactly \(x=y=0\).

**2. Hyperdeterminantal equation.** The signed minors, arranged as the kernel vector of \(N\), are
\[
(p_0,p_1,p_2,p_3)=(x,ax+(1+c)y,y,bx+dy).
\]
They obey \(N(p_0,p_1,p_2,p_3)^\top=0\). Substitution in the Segre quadric equation gives, *without discarded higher terms*,
\[
H=b x^2+(d-a)xy-(1+c)y^2.
\]
Write \(t=d-a\). This gives a complete local equation of the hyperdeterminantal hypersurface, up to multiplication by a unit.

**3. Full characteristic-two Jacobian ideal.** The derivatives with respect to \(a,b,c,d,x,y\), calculated in characteristic two, generate respectively \(xy,x^2,y^2,xy,ty,tx\). Since \(H\in(x^2,xy,y^2)\), adding its equation does not change the ideal. Therefore
\[
J=(x^2,xy,y^2,tx,ty).
\]
Its radical is \((x,y)\). At points where \(t\) is invertible it is exactly \((x,y)\), so the ordinary rank-two singular scheme is reduced there. At \(t=0\), with the other base parameters held fixed, its scheme-theoretic transverse fiber is
\[
\operatorname{Spec}k[x,y]/(x,y)^2,
\]
which has basis \(1,x,y\) and length three. This fiber is a local Artin scheme, not a declaration that all infinitesimal directions of the global scheme have length three.

**4. The tangency and its inseparable incidence.** Restricting the Segre quadric to the kernel line gives the binary quadratic \(b x^2+txy-(1+c)y^2\). Its discriminant in characteristic two is \(t^2\). The reduced tangency divisor, in the displayed rank-two chart, is \(t=0\). At its generic point, both \(b\) and \(1+c\) are nonzero and the geometric contact point satisfies
\[
(x/y)^2=(1+c)/b.
\]
The rational function \((1+c)/b\) is not a square in the rational function field \(k(a,b,c)\), because its divisor has odd valuation at \(b=0\). Adjoining its square root is therefore a purely inseparable extension of degree two. The contact-point incidence over the generic point is radicial of degree two, despite having exactly one geometric point.

**5. Odd-characteristic boundary.** Over any algebraically closed field of characteristic not two, at the tangency point \(a=b=c=d=x=y=0\) the above equation is \(-y^2\) to second order in the transverse variables. Taking the full Jacobian and fixing the four base parameters gives the ideal \((x^2,y)\), with quotient \(k[x]/(x^2)\) of length two. More generally, for a tangent binary quadratic with nonzero square coefficient, completing the square reduces its transverse Jacobian fiber to an isomorphic length-two algebra. Thus the jump from two to three at the characteristic-two tangency is intrinsic to this family of transverse singular schemes.

## Verification
The accompanying standalone `verify.py`, requiring Python 3 with SymPy, independently calculates the signed maximal minors of \(N\), derives the precise hyperdeterminantal equation and six partial derivatives, verifies their characteristic-two reduction, and checks the two transverse Artin-algebra bases with exact Gröbner computations. Execute `python verify.py`. The included `verification_output.txt` was generated by executing that same file and ends with `ALL_CHECKS_PASSED`. The finite symbolic check does not constitute an independent historical-priority review; the generic purely inseparable extension is established by the divisor-valuation argument in the proof.

## Relationship to prior work
Weyman–Zelevinsky [1] classify the reduced irreducible components of singular loci of hyperdeterminants in characteristic zero; their boundary-format results do not give the characteristic-two scheme-theoretic Jacobian ideal or its length-three tangent fiber. Bremner [2] gives an explicit degree-six polynomial for \(2\times2\times3\) arrays; the polynomial and the boundary-format construction are *not* new. The present calculation compares a local nonreduced Jacobian fiber across characteristics and determines the nontrivial purely inseparable generic contact incidence. The available literature searches did not find those exact linked statements, but such absence is not a proof of historical novelty.

## Limitations
The local Jacobian statement holds on the indicated rank-two chart near the tangency divisor; it is not a classification of all singularities or all positive-characteristic hyperdeterminants. Its geometric contact incidence is described over the tangency function field, and the field is assumed algebraically closed for the geometric fiber statement. The algebraic proof is self-contained once the classical boundary-format hyperdeterminant is identified with the Segre quadric applied to maximal minors. Independent audit and exhaustive historical-priority certification have not been performed.

## References
[1] J. Weyman and A. Zelevinsky, “Singularities of hyperdeterminants”, Annales de l’Institut Fourier **46** (1996), 591–644. DOI: 10.5802/aif.1526. https://archive.numdam.org/articles/10.5802/aif.1526/ .
[2] M. R. Bremner, “A hyperdeterminant for 2 × 2 × 3 arrays”, first posted 2011-06-15, arXiv:1106.2988, https://arxiv.org/abs/1106.2988 .
