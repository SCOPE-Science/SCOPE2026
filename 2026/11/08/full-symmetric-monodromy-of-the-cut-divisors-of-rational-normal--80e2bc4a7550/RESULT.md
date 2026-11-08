# Full symmetric monodromy of the cut divisors of rational-normal-scroll ruling curves

## Finding

For every integer \(d\ge2\) and integers \(n_1,\ldots,n_d\ge2\), let \(N=\sum_i n_i\) and \(m=N+d\). The curve of ruling \(d\)-planes of the rational normal scroll \(S(n_1,\ldots,n_d)\) in \(\operatorname{Gr}(d,m)\) meets the algebraic Grassmann cut locus of a general rank-\(d\) orthogonal projector in exactly \(N\) distinct points. Their geometric permutation monodromy is the full symmetric group \(\mathfrak S_N\). Equivalently, the generic cut equation has Galois group \(\mathfrak S_N\) over the function field of the parameter Grassmannian.

In particular, when \(N\ge5\), no radical formula can enumerate the individual generic cut points. This concerns intersections with the cut locus, **not** the number or monodromy of distance-critical points; those are different enumerative problems.

## Assumptions and scope

Work over \(\mathbb C\) with the standard nondegenerate symmetric bilinear form. For homogeneous coordinates \([u:v]\) on \(\mathbb P^1\), let \(A([u:v])\) be the \(d\)-by-\(m\) block-row matrix whose \(i\)-th row has one nonzero block
\[
(u^{n_i},u^{n_i-1}v,\ldots,v^{n_i}).
\]
Each row is nonzero, the blocks are disjoint, and the row span defines a morphism \(\mathcal R:\mathbb P^1\to\operatorname{Gr}(d,m)\). Its Plücker coordinates include independent monomials of total degree \(N\), so its image has degree \(N\) and the parametrization is injective (indeed the ratio of suitable adjacent Plücker coordinates recovers \([u:v]\)).

Choose an \(m\)-by-\(d\) matrix \(B\) of full column rank with \(\det(B^{\mathsf T}B)\ne0\). It spans a nondegenerate plane \(W\) whose symmetric orthogonal projector is
\[
Q=B(B^{\mathsf T}B)^{-1}B^{\mathsf T}.
\]
The algebraic cut condition is \(\operatorname{im} A(t)^{\mathsf T}\cap\ker Q\ne0\). Here 'general' means a point of a nonempty Zariski-open subset of the nondegenerate-plane Grassmannian; the cut divisor is counted on \(\mathbb P^1\), including the parameter at infinity.

## Proof

**1. A polynomial determinant describes precisely the cut points.** On the affine chart \(u=1\), write \(t=v/u\). The \(d\)-by-\(d\) matrix \(M_B(t)=A(t)B\) has entries
\[
(M_B(t))_{ij}=\sum_{r=0}^{n_i}b_{irj}t^r,
\]
where the coefficient coordinates \(b_{irj}\) are algebraically independent before restriction to the nondegenerate-frame open set. Since \(Q\) is the projection onto \(\operatorname{im}B\),
\[
\ker Q=\ker B^{\mathsf T},\qquad
\operatorname{im} A(t)^{\mathsf T}\cap\ker Q\ne0
\iff\det M_B(t)=0.
\]
The determinant is a section of \(\mathcal O_{\mathbb P^1}(N)\). It has generically degree \(N\) and simple zeros: specialize to diagonal \(M_B(t)\) with each diagonal polynomial of degree \(n_i\) a product of distinct real linear factors, no root shared between factors. Then \(\det M_B\) has precisely \(N\) simple roots, no root at infinity. The corresponding real frame has \(B^{\mathsf T}B\) positive definite because its nonzero columns have disjoint block supports. Nonvanishing of the leading coefficient, discriminant, and Gram determinant are open conditions, proving the first assertion.

**2. Two-point incidence proves double transitivity.** Consider ordered pairs of *different* finite parameters \((t_1,t_2)\). Joint evaluation of every degree-at-most-\(n_i\) row polynomial at these parameters is surjective, since \(n_i\ge2\) and the explicit linear interpolation
\[
\frac{t-t_2}{t_1-t_2}X+\frac{t-t_1}{t_2-t_1}Y
\]
attains any desired pair of matrices \((X,Y)\) at \((t_1,t_2)\). The remaining coefficients form an affine-space kernel of constant dimension on the base \(t_1\ne t_2\). The condition \(\det X=\det Y=0\) is a product of two irreducible determinantal hypersurfaces, times an affine space. Hence the incidence variety
\[
\big\{(B,t_1,t_2): t_1\ne t_2,\ \det M_B(t_1)=\det M_B(t_2)=0\big\}
\]
is irreducible. Restricting to the nonempty open locus of nondegenerate frames, leading coefficient nonzero and all simple roots preserves irreducibility. Its generic finite étale fiber is the set of \(N(N-1)\) ordered pairs of distinct cut roots. Thus the geometric monodromy acts transitively on ordered pairs, i.e. it is \(2\)-transitive.

**3. A simple collision gives a transposition.** Choose a real diagonal specialization whose first factor is
\[
f_1(t)=t^2\prod_{j=1}^{n_1-2}(t-c_j),
\]
with all \(c_j\) nonzero and distinct, and whose other factors \(f_i(t)\) have simple real roots disjoint from each other and from zero. Empty products are \(1\). The associated real Gram matrix is positive definite. Vary only the constant coefficient of \(f_1\) by \(\epsilon\), replacing \(f_1\) with \(f_1+\epsilon\), leaving the other factors unchanged. For small nonzero \(\epsilon\), all \(N\) roots are simple and the Gram determinant stays nonzero. Near \(t=0\), precisely two roots solve \(ct^2+O(t^3)+\epsilon=0\), where \(c\ne0\). Going around \(\epsilon=0\) interchanges exactly these two roots while all others return to themselves. Hence a transposition lies in monodromy.

A \(2\)-transitive subgroup of \(\mathfrak S_N\) containing a transposition contains its conjugate across every unordered pair, hence all transpositions and therefore the full \(\mathfrak S_N\).

**4. Passage from frames to the Grassmannian.** The map from full-rank nondegenerate frames \(B\) to their spans \(W\) is a surjective principal \(\operatorname{GL}_d\)-bundle. Replacing \(B\) by \(BC\) multiplies \(\det M_B(t)\) by \(\det C\), without changing its roots. Every loop in the frame open set projects to a loop in the parameter Grassmannian with exactly the same root permutation. Since the frame monodromy is \(\mathfrak S_N\), so is the monodromy over nondegenerate planes, equivalently rank-\(d\) symmetric projectors. The usual identification of geometric monodromy with the function-field Galois group completes the proof.

## Verification

The standalone file `verify.py` checks exact symbolic identities with SymPy, including squarefree determinant witnesses for block degrees \((2,2)\), \((2,3)\), \((2,4)\), \((3,3)\) and \((2,2,2)\); independent two-point evaluation for a generic \(3\)-by-\(3\) polynomial matrix; simple-order discriminant vanishing in three collision examples; and the projector cut-condition determinant identity on \(S(2,3)\). Execute `python verify.py` with SymPy installed. It prints `VERIFY_OK`. The universal incidence irreducibility and monodromy steps are established by the proof, not extrapolated from these finite tests.

## Relationship to prior work

Friedman–Hoşten–Rosana (2026, Example 2.1 and Theorem 2.2) introduce the same ruling-plane curve and give its Euclidean-distance critical-point degree; Section 4 defines the algebraic cut locus. The present count of **cut-locus intersections**, and more importantly their full permutation monodromy under Grassmannian data, are separate from the cited critical-point enumeration. Friedman–Rosana–Sturmfels (2026) discuss the corresponding distance-optimization setting for lines. Esterov–Lang (2022/2026) determine root monodromy for polynomials **generic with respect to a prescribed coefficient support**; this determinant polynomial instead has constrained, correlated coefficients. The two-point incidence and collision proof verifies maximal monodromy for this particular restricted family. General monodromy principles and the ordinary Galois theory of generic polynomials are used, not claimed as new.

## Limitations

Only permutation monodromy, not the full braid monodromy or the integral topology of the discriminant complement, is determined. The theorem assumes complex characteristic zero, positive block degrees at least two, and generic nondegenerate Grassmannian data. Degenerate special frames and cut-root multiplicity profiles are not classified. Although a complete statement and proof are supplied, specialist historical-priority and independent mathematical reviews remain outstanding.

## References

1. H. Friedman, S. Hoşten, A. Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018, first submitted 2026-10-01, especially Example 2.1, Theorem 2.2 and Section 4. https://arxiv.org/abs/2610.02018
2. H. Friedman, A. Rosana, B. Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843, first submitted 2026-01-30. https://arxiv.org/abs/2601.22843
3. A. Esterov, L. Lang, *Permuting the roots of univariate polynomials whose coefficients depend on parameters*, arXiv:2204.14235 (2022); J. Eur. Math. Soc. (2026), DOI 10.4171/JEMS/1788. https://arxiv.org/abs/2204.14235
