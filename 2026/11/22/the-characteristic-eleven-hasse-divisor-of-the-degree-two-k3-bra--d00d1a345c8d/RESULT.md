# The characteristic-eleven Hasse divisor of the degree-two K3 branch-sextic pencil

## Finding

Let \(k=\overline{\mathbb F}_{11}\) and let
\[
B_t:\quad X^6+Y^6+Z^6+tX^2Y^2Z^2=0\subset\mathbb P^2_k.
\]
For \(t^3\ne6\), the curve is smooth of genus \(10\). With respect to a standard adjoint-monomial basis, its Hasse--Witt matrix is permutation-conjugate to three scalar blocks \((A)\), three two-by-two blocks \(\left(\begin{smallmatrix}0&B\\B&0\end{smallmatrix}\right)\), and one scalar block \((C)\), where all coefficients lie in \(\mathbb F_{11}[t]\):
\[
A=t^2(1-t^3),\qquad B=2t(2t^3+1),\qquad
C=t(t^3-1)(t^3+2)(t^3+4).
\]
Consequently its Hasse determinant is **exactly**
\[
\det H_t=9t^{13}(t^3-1)^4(2t^3+1)^6(t^3+2)(t^3+4).
\]
For every geometrically smooth fiber, its geometric Jacobian \(11\)-rank and \(a\)-number are
\[
(f_t,a_t)=\begin{cases}
(0,10),&t=0,\\
(4,6),&t^3=5,\\
(6,4),&t^3=1,\\
(9,1),&t^3\in\{7,9\},\\
(10,0),&\text{otherwise.}
\end{cases}
\]
Thus the reduced nonordinary parameter locus comprises exactly \(13\) distinct geometric points, with Hasse-divisor multiplicities \(13\) at \(t=0\), \(4\) at the three roots of \(t^3=1\), \(6\) at the three roots of \(t^3=5\), and \(1\) at each of the six roots of \(t^3\in\{7,9\}\). The fiber at \(t=0\) is superspecial. All \(13\) geometric nonordinary parameters are defined over \(\mathbb F_{121}\); over \(\mathbb F_{11}\), they comprise five rational points and four closed points of degree two. Of the ten smooth \(\mathbb F_{11}\)-fibers, the ranks \(0,4,6,9,10\) occur with frequencies \(1,1,1,2,5\), respectively.

## Assumptions and scope

All assertions concern the displayed **coefficient-marked** plane-sextic pencil in characteristic \(11\), with parameter \(t\) in an algebraic closure; the singular parameter equation is \(t^3=6\). The \(11\)-rank is the dimension of the maximal stable Frobenius part of first cohomology, equivalently the \(p\)-rank of the Jacobian. The \(a\)-number is the dimension of the kernel of Cartier on regular differentials. The Hasse determinant is calculated with the basis below; its zero divisor is basis-independent although the nonzero scalar normalization is not.

## Proof

**Smoothness and genus.** The three partial derivatives are \(2X(3X^4+tY^2Z^2)\) and its cyclic permutations. A singular point cannot have any zero coordinate because the other two partials would force all three coordinates to vanish. At a singular point with \(XYZ\ne0\), multiplication by \(X^2,Y^2,Z^2\) shows that \(3X^6=3Y^6=3Z^6=-tX^2Y^2Z^2\). Multiplication of the three equalities forces \(t^3=-27=6\) in characteristic \(11\). Conversely, for each of the three roots of this equation, choose \(X^6=Y^6=Z^6=1\) and \(X^2Y^2Z^2=-3/t\), a cubic root of unity; such a point is singular. Hence smoothness is equivalent to \(t^3\ne6\). A smooth plane sextic has genus \((6-1)(6-2)/2=10\).

**Coefficient computation.** Order the adjoint-monomial basis of \(H^0(B_t,\Omega^1)\) by \((i,j,k)\) with \(i+j+k=3\), taking \(i=0,1,2,3\) and then \(j=0,\ldots,3-i\). For row \((i,j,k)\) and column \((r,s,u)\), the standard plane-curve Cartier/Hasse--Witt coefficient formula extracts the coefficient of
\[
X^{11(i+1)-(r+1)}Y^{11(j+1)-(s+1)}Z^{11(k+1)-(u+1)}
\]
from \((X^6+Y^6+Z^6+tX^2Y^2Z^2)^{10}\). Expanding multinomially, the only nonzero entries in this order are: diagonal entries \((0,0),(3,3),(9,9)\) all equal to \(A\); entries \((1,8),(8,1),(2,7),(7,2),(4,6),(6,4)\) all equal to \(B\); and entry \((5,5)\) equal to \(C\). In particular, the matrix is the indicated block-permutation matrix. Its determinant equals \((-1)^3A^3B^6C\), which simplifies to the asserted factored polynomial over \(\mathbb F_{11}\), since \(2^6=9\) in that field.

**Frobenius stability and strata.** A scalar one-by-one block contributes one to geometric stable Frobenius rank precisely when its entry is nonzero. Each two-by-two block exchanges two basis vectors, with nonzero scalars precisely when \(B\ne0\), and therefore contributes either two or zero stable dimensions under every positive iterate, including semilinear twists. Hence the Jacobian \(11\)-rank equals the one-step matrix rank, explicitly
\[
f_t=3\mathbf 1_{A(t)\ne0}+6\mathbf 1_{B(t)\ne0}+\mathbf 1_{C(t)\ne0}.
\]
The \(a\)-number equals \(10-\operatorname{rank}H_t=10-f_t\). The roots of \(A,B,C\) are, respectively, \(t=0\) or \(t^3=1\); \(t=0\) or \(t^3=5\); and \(t=0\) or \(t^3\in\{1,9,7\}\). All these values are disjoint from the singular condition \(t^3=6\). Substitution gives the five strata. At \(t=0\) Cartier vanishes on all ten holomorphic differentials, giving \(a=10\) and hence a superspecial Jacobian.

**Multiplicity and rationality.** Every equation \(t^3=c\) with \(c\ne0\) has three simple roots in the algebraic closure. The exponent of each factor in the displayed Hasse determinant gives the stated multiplicity. Because \(\gcd(3,10)=1\), each of the four values \(c=1,5,7,9\) has exactly one cube root in \(\mathbb F_{11}\); its other two roots are conjugate over \(\mathbb F_{121}\), since that field contains the cube roots of unity. There are therefore five rational and four quadratic closed nonordinary points. The only rational singular parameter is \(t=8\). Evaluating the five rank cases at the other ten values gives the frequency vector.

## Verification

The standalone standard-library-only script `VERIFY.py` constructs the two coefficient tables for the homogeneous expansion and the affine-chart expansion independently, compares the resulting ten-by-ten matrices, verifies all entries and the exact determinant factorization, and performs exact finite-field Gaussian elimination for every rational parameter. It also verifies stabilization under twenty iterates of Frobenius on all ten smooth rational fibers and checks the rational parameter strata. Run `python3 VERIFY.py`; expected output begins `GENUS10_BRANCH_SEXTIC_HASSE_VERIFIED`. The geometric statement is proved by the symbolic block argument above, not inferred from finite-point enumeration.

## Relationship to prior work

Bouyer--Costa--Festi--Nicholls--West (first public preprint March 6, 2017) study degree-two K3 surfaces \(W^2=X^6+Y^6+Z^6+tX^2Y^2Z^2\), with the displayed sextics as branch curves, and establish the characteristic-zero smoothness threshold. Bartoli--Giulietti--Kawakita--Montanucci (first public preprint October 18, 2019), Section 5, investigate the same sextic family in finite characteristic and its Jacobian decomposition and maximality. Neither inspected text supplies the characteristic-eleven Hasse determinant with multiplicities or the exact parameter-wise geometric \(p\)-rank strata. The later plane-sextic automorphism classification of Badr--Bars and collaborators addresses automorphism strata, not the present characteristic-eleven Cartier calculation. This theorem refines those results; it does not claim the family, its automorphisms, Jacobian decomposition, singularity condition in characteristic zero, or Fermat superspeciality as new.

## Limitations

The theorem concerns one characteristic and one coefficient-marked pencil. It does not classify geometric isomorphism classes, Newton polygons beyond their \(11\)-ranks, full Weil polynomials, or the positive-characteristic Picard/Newton strata of the associated K3 surfaces. Published or unindexed equivalent Hasse computations cannot be excluded absolutely. The computations certify their stated finite identities, not a formal or independent review.

## References

1. F. Bouyer, E. Costa, D. Festi, C. Nicholls, M. West, *On the arithmetic of a family of degree-two K3 surfaces*, arXiv:1703.02127, first posted 2017-03-06, https://arxiv.org/abs/1703.02127 .
2. D. Bartoli, M. Giulietti, M. Kawakita, M. Montanucci, *New examples of maximal curves with low genus*, arXiv:1910.11098, first posted 2019-10-18, Section 5, https://arxiv.org/abs/1910.11098 .
3. E. Badr, F. Bars et al., *The stratification by automorphism groups of smooth plane sextic curves*, 2025, https://doi.org/10.1007/s10231-025-01558-z .
