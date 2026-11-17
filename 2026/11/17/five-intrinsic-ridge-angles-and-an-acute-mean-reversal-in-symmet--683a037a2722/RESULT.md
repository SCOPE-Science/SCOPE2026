# Five intrinsic ridge angles and an acute-mean reversal in symmetric stochastic polytopes

## Finding

For an integer \(n\ge 3\), let
\[
\mathcal S_n=\{X\in\mathbb R^{n\times n}:X=X^{\mathsf T},\ X_{ij}\ge0,\ X\mathbf1=\mathbf1\}
\]
carry the Euclidean metric induced by the ambient Frobenius inner product \(\langle X,Y\rangle=\operatorname{tr}(X^{\mathsf T}Y)\). Distinct coordinate facets are indexed by the \(n\) diagonal positions \(ii\) and the \(\binom n2\) unordered off-diagonal positions \(ij\).

For \(n\ge4\), **every pair** of distinct coordinate facets intersects in a ridge. Thus the facet-adjacency graph is complete on \(F=n(n+1)/2\) facets, and the number of ridges is \(\binom F2\). The complete angle spectrum, with a zero multiplicity omitted, is given below. Put \(D=n^2-2n+2\). Angles are *interior* dihedral angles of the intrinsic polytope.

| Type of two zero-coordinate facets | Interior angle | Exact number |
|---|---|---:|
| Two distinct diagonals | \(\arccos[-1/(n-1)^2]\) | \(\binom n2\) |
| A diagonal and an incident off-diagonal | \(\arccos[\sqrt{2/D}]\) | \(n(n-1)\) |
| A diagonal and a nonincident off-diagonal | \(\arccos[-\sqrt2/((n-1)\sqrt D)]\) | \(\binom n2(n-2)\) |
| Two off-diagonals sharing one endpoint | \(\arccos[(n-2)/D]\) | \(n\binom{n-1}{2}\) |
| Two disjoint off-diagonals | \(\arccos[-2/D]\) | \(3\binom n4\) |

All five angles are different for every \(n\ge4\). For \(n=3\) there are six facets and nine ridges: the six diagonal–incident-off-diagonal pairs are **not** ridges, nor are any disjoint-off-diagonal pairs possible. The remaining three types occur three times each, with angles given by the same formulas.

Let \(\Theta_n\) be the angle of a ridge chosen uniformly from all ridges of \(\mathcal S_n\). The strict sign transition is
\[
\mathbb E\Theta_3>\frac\pi2,
\qquad \mathbb E\Theta_n<\frac\pi2\quad(n\ge4).
\]
Nevertheless, the probability of an obtuse ridge tends to one, and
\[
 n^2\left(\Theta_n-\frac\pi2\right)\xrightarrow{\mathsf P}2,
\qquad n^2\left(\mathbb E\Theta_n-\frac\pi2\right)\longrightarrow-2,
\qquad n^3\operatorname{Var}(\Theta_n)\longrightarrow4.
\]
Thus a vanishing proportion of acute ridges reverses the sign of the average angle at the first nontrivial scale.

## Assumptions and scope

The matrix is symmetric, entrywise nonnegative and has every row sum exactly one. The diagonal entries are variable; no trace condition is imposed. The ambient Frobenius metric is essential: the upper-triangular-coordinate metric would yield different numerical angles. All facets and ridges refer to the affine hull of \(\mathcal S_n\), which has dimension \(\binom n2\), not to the surrounding matrix space. Every facet named in the table is the nonredundant coordinate inequality \(X_{ij}\ge0\), counted once for \(i<j\).

## Proof

**1. Facets and pairwise intersections.** The \(\binom n2\) off-diagonal coordinates vary freely in a sufficiently small neighborhood of the identity matrix, with the diagonals fixed by row sums; hence \(\dim\mathcal S_n=\binom n2\). Each off-diagonal coordinate can be set to zero with all others positive by taking the other off-diagonal entries small and positive. Each diagonal entry can be set to zero while all other coordinates remain positive by assigning \(1/(n-1)\) to its incident off-diagonal entries and sufficiently small positive numbers to every other off-diagonal entry. Thus the asserted \(F\) inequalities are precisely the facets.

To realize two prescribed zero coordinates with all other entries positive, use the following witnesses. For two off-diagonal zeros, assign a small common positive number to every remaining off-diagonal entry and choose positive diagonal residuals. For two diagonal zeros at \(i,j\), put \(X_{ij}=3/4\), assign \(1/[4(n-2)]\) to each edge joining \(i\) or \(j\) to another index, and assign sufficiently small positive numbers to off-diagonal entries among those other indices; their diagonal residuals are positive. For diagonal zero at \(i\) and off-diagonal zero at \(jk\) with \(i\notin\{j,k\}\), put \(X_{i\ell}=1/(n-1)\) for each \(\ell\ne i\) and take the remaining allowed off-diagonal entries small and positive; all other diagonals stay positive. For diagonal zero at \(i\) and incident off-diagonal zero at \(ij\), the same construction works with \(X_{i\ell}=1/(n-2)\) for \(\ell\notin\{i,j\}\), **if and only if \(n\ge4\)**. When \(n=3\), the two zeros instead force \(X_{ik}=1\) for the third index, and force \(X_{jk}=X_{kk}=0\), giving a vertex rather than a ridge. The relevant coordinate constraints are linearly independent along the affine hull (equivalently, their projected normal Gram determinant is positive as computed below); hence each all-other-positive witness has codimension exactly two. These are all facet pairs, proving the ridge criterion and counts.

**2. Intrinsic normal products.** Write \(R(X)=X\mathbf1\) on the Euclidean space of symmetric matrices and \(P\) for orthogonal projection to \(\ker R\). Its adjoint is \(R^*u=(u\mathbf1^{\mathsf T}+\mathbf1u^{\mathsf T})/2\), so
\[
 RR^*=\frac n2I+\frac12\mathbf1\mathbf1^{\mathsf T},
\qquad (RR^*)^{-1}=\frac2nI-\frac1{n^2}\mathbf1\mathbf1^{\mathsf T},
\qquad P=I-R^*(RR^*)^{-1}R.
\]
The raw Frobenius coordinate gradients are \(G_{ii}=E_{ii}\) and \(G_{ij}=(E_{ij}+E_{ji})/2\) for \(i<j\); thus \(RG_{ii}=e_i\) and \(RG_{ij}=(e_i+e_j)/2\). Direct substitution into
\[
 \langle PG_a,PG_b\rangle
 =\langle G_a,G_b\rangle-(RG_a)^{\mathsf T}(RR^*)^{-1}(RG_b)
\]
gives squared norms \((n-1)^2/n^2\) for diagonal facets and \(D/(2n^2)\) for off-diagonal facets. For the five types in table order, the products of **unnormalized** projected gradients are respectively
\[
\frac1{n^2},\quad -\frac{n-1}{n^2},\quad\frac1{n^2},\quad-\frac{n-2}{2n^2},\quad\frac1{n^2}.
\]
Interior dihedral angle satisfies \(\cos\theta=-\langle PG_a,PG_b\rangle/(\|PG_a\|\|PG_b\|)\), proving all five formulas. For \(n\ge4\) they are distinct: the positive cosines satisfy \(0<(n-2)/D<\sqrt{2/D}\), and the magnitudes of the three negative cosines satisfy
\[
0<\frac1{(n-1)^2}<\frac{\sqrt2}{(n-1)\sqrt D}<\frac2D.
\]

**3. Sign of the mean.** For \(n=3\) the three retained types are equally frequent, and their mean-angle deviation is
\[
\frac13\left(\arcsin\frac14+\arcsin\frac1{\sqrt{10}}-\arcsin\frac15\right)>0.
\]
For \(n\ge4\), use \(f(x)=\arcsin x\), convex on \([0,1]\) with \(f(0)=0\). The total acute contribution from incident diagonal/off-diagonal pairs exceeds the obtuse contribution from nonincident diagonal/off-diagonal pairs in absolute value: \(f(t/(n-1))\le f(t)/(n-1)\), and the second class has only \((n-2)/2\) times the multiplicity of the first. Likewise, the excess acute contribution from off-diagonal pairs sharing an endpoint over the obtuse contribution of disjoint off-diagonal pairs is at least
\[
 n\binom{n-1}{2}\frac{n-1}{4}\arcsin\frac2D,
\]
because \(f(((n-2)/2)y)\ge((n-2)/2)f(y)\). This exceeds the remaining obtuse diagonal–diagonal contribution \(\binom n2 f(1/(n-1)^2)\): sufficient is
\[
\frac{(n-1)(n-2)}{2D}>\frac\pi{2(n-1)^2},
\]
which holds for \(n\ge4\), since \(D=(n-1)^2+1\le(10/9)(n-1)^2\), \((n-1)(n-2)\ge6\), and \(\pi<4\). Hence the exact mean deviation is negative in every dimension \(n\ge4\).

**4. Limits and variance.** The disjoint-off-diagonal class has probability \(1-O(n^{-1})\) and angle \(\pi/2+2n^{-2}+O(n^{-3})\). The sharing-endpoint class has probability \(4n^{-1}+O(n^{-2})\) and angle \(\pi/2-n^{-1}+O(n^{-2})\). Every other class contributes only \(O(n^{-3})\) to the unscaled mean deviation and \(O(n^{-4})\) to its second moment. Consequently, the mean deviation is \(-2n^{-2}+o(n^{-2})\), the second moment of the deviation is \(4n^{-3}+o(n^{-3})\), and its squared mean is \(O(n^{-4})\). This gives the three claimed limits and the obtuse-proportion statement.

## Verification

A standalone exact-arithmetic checker accompanies this result. It expresses the tangent space in the basis \(B_{ij}=E_{ij}+E_{ji}-E_{ii}-E_{jj}\), independently forms the Gram matrix \(4I+A(L(K_n))\), inverts it over rational numbers, computes every coordinate-normal product, and checks a strictly positive witness for all remaining coordinates at every proposed ridge. It exhausts all facet pairs for \(n=3,4,5,6,7\), including the exceptional non-ridge pairs. The symbolic proof above, not finite enumeration, establishes the theorem for all \(n\ge3\).

Reproduce with `python3 check_symmetric_stochastic.py` using Python's standard library.

## Relationship to prior work

Brualdi and Cao classified vertices and linear dimensions for symmetric, Hankel-symmetric and centrosymmetric doubly stochastic matrices. Their symmetric-vertex description includes odd-cycle half-integral vertices and provides the foundational family, but does not supply the intrinsic ridge-angle multiset or the mean-angle asymptotics. De Jong and Wulkenhaar studied asymptotic volumes of symmetric stochastic polytopes with prescribed diagonal entries; those volume formulas neither determine codimension-two incidence nor the Frobenius dihedral angles. The present result is about the **full variable-diagonal** symmetric stochastic polytope, not an ordinary transportation polytope nor a fixed-trace section.

## Limitations

The statement is restricted to the canonical Frobenius metric, and to \(n\ge3\). It gives no result on volume, smooth curvature, or angles of trace-constrained sections. Historical priority is provisional: the identified sources do not cover this exact metric statement, but an unindexed equivalent derivation is possible. The finite checker verifies only dimensions three through seven and is not an infinite-dimensional certificate.

## References

1. R. A. Brualdi and L. Cao, *Symmetric, Hankel-symmetric, and Centrosymmetric Doubly Stochastic Matrices*, arXiv:1712.03129v1, first posted 2017-12-08, https://arxiv.org/abs/1712.03129.
2. J. de Jong and R. Wulkenhaar, *The asymptotic volume of diagonal subpolytopes of symmetric stochastic matrices*, arXiv:1701.07719, first posted 2017-01-26, https://arxiv.org/abs/1701.07719.
