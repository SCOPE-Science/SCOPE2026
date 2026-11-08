# A single \(\operatorname{PGL}_3(\mathbb F_4)\)-orbit of smooth extremal Frobenius-nonclassical plane sextics

## Finding

Let \(k=\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\), and call a smooth plane curve \(C=V(F)\subset\mathbb P^2_k\) *Frobenius nonclassical* if the fourth-power Frobenius image of each geometric point on \(C\) belongs to its embedded tangent line. Among geometrically smooth plane sextics with this property, there are **exactly 960 distinct plane equations up to nonzero scalar** over \(k\), and **exactly one** equivalence class under \(\operatorname{PGL}_3(k)\). The stabilizer in \(\operatorname{PGL}_3(k)\) of every such curve has order **63**. An explicit representative is
\[
C_0:\quad XYZ(X^3+Y^3+Z^3)+X^6+\alpha Y^6+(\alpha+1)Z^6=0.
\]
In particular these curves have genus \(10\) and no \(k\)-rational points. The no-rational-points property itself was already proved in the motivating literature for the entire extremal class, and is not claimed as new.

## Assumptions and scope

All forms, projective transformations, and equation counts are defined over \(k\), not merely its algebraic closure. Distinct nonzero scalar multiples define the same equation. Smoothness means geometric smoothness. Projective equivalence means equivalence under \(\operatorname{PGL}_3(k)\), rather than under a group over an extension field. The statement concerns degree-six plane curves over the four-element field, not every sextic or every Frobenius-nonclassical degree.

Theorem 1.6(3) of Asgarli–Duan–Lai gives the following exhaustive normal form for smooth Frobenius-nonclassical curves of degree \(q+2\) in characteristic two. At \(q=4\), after a unique scalar normalization,
\[
F=F_0+G(X^2,Y^2,Z^2),\qquad
F_0=XYZ(X^3+Y^3+Z^3),
\]
where \(G(U,V,W)\) is any homogeneous cubic over \(k\). Conversely, every *smooth* member of this family is Frobenius nonclassical. There are precisely ten cubic monomials, hence \(4^{10}=1{,}048{,}576\) normalized candidates. The unique normalization follows because the gradient of every such form is the nonzero fixed gradient of \(F_0\).

## Proof

**1. A complete geometric smoothness criterion.** In characteristic two, all partial derivatives of \(G(X^2,Y^2,Z^2)\) vanish. Direct differentiation gives
\[
\begin{aligned}
F_X&=Y^4Z+YZ^4,\\
F_Y&=X^4Z+XZ^4,\\
F_Z&=X^4Y+XY^4.
\end{aligned}
\]
Thus the gradient vanishes at a projective geometric point \([x:y:z]\) exactly when all pairwise products satisfy \(x^4y=xy^4\), \(x^4z=xz^4\), and \(y^4z=yz^4\). Given any nonzero coordinate, dividing the corresponding equations shows that each nonzero coordinate ratio is fixed by fourth-power Frobenius. Hence the common zero locus of the partial derivatives is exactly the \(21\)-point set \(\mathbb P^2(k)\). The Jacobian criterion therefore says that \(F\) is geometrically smooth **if and only if**
\[
F(P)\ne0\quad\text{for every }P\in\mathbb P^2(k).
\]
This criterion covers singularities over every algebraic extension; testing field points alone is exhaustive here because the gradient locus was proved to equal the rational projective plane.

**2. Exact count of the smooth coefficient vectors.** Order the ten degree-three monomials as \(U^iV^jW^{3-i-j}\) with \(i=0,1,2,3\), followed by \(j=0,\ldots,3-i\). Write \(G=\sum c_{ij}U^iV^jW^{3-i-j}\), with \(c_{ij}\in k\). Enumerate all \(21\) rational projective points using the disjoint representatives \((1,y,z)\), \((0,1,z)\), \((0,0,1)\), with \(y,z\in k\). Evaluate
\[
F_0(P)+\sum_{i+j\le3}c_{ij}x^{2i}y^{2j}z^{2(3-i-j)}
\]
exactly in \(k\), for each of the \(4^{10}\) coefficient tuples, retaining only tuples for which all \(21\) values are nonzero. This exhaustive count gives exactly **960** tuples. Two independently implemented finite-field arithmetic programs reproduce this count. The attached source files `verify_fnc_f4_count.cpp` and `verify_fnc_f4_sextics.py` specify every field operation, monomial order, and projective representative; neither requires any data file.

**3. Projective action and transitivity.** Let \(A\in\operatorname{GL}_3(k)\). The gradient from Step 1 can be written as a cross product \(\mathbf x^{[4]}\times\mathbf x\), so the cross-product transformation rule implies
\[
\nabla(F_0(A\mathbf x))=\det(A)\,\nabla F_0(\mathbf x).
\]
Consequently
\[
(\det A)^{-1}F(A\mathbf x)=F_0(\mathbf x)+G_A(X^2,Y^2,Z^2)
\]
for a uniquely determined cubic \(G_A\): the difference has every partial derivative zero, so all its monomial exponents are even, and \(k\) is perfect. This gives an exact affine action on the ten coefficients. It depends only on the projective class of \(A\), because multiplying \(A\) by \(\lambda\in k^\times\) multiplies the displayed transformed degree-six form by \(\lambda^3=1\).

To compute each coefficient transformation, the Python verifier selects ten rational projective points on which evaluation of the ten square-cubic monomials has rank ten, evaluates the transformed form at those points, and solves the resulting exact \(k\)-linear system. The program checks the recovered affine action independently at all \(21\) projective points, on the constant part and on each monomial basis vector.

Apply eight explicit invertible coordinate transformations: the six shears \(X_i\mapsto X_i+aX_j\), with \((i,j)=(0,1),(1,2),(2,0)\) and \(a\in\{1,\alpha\}\), the scaling \(X\mapsto\alpha X\), and the swap \(X\leftrightarrow Y\). A breadth-first orbit search on the resulting ten-coordinate vectors, starting from the lexicographically smallest smooth vector, visits **all 960** smooth vectors. Each transformation maps the 960-element set to itself; the test explicitly checks this for all eight transformations. Thus one \(\operatorname{PGL}_3(k)\)-orbit already contains all smooth normalized forms. Since
\[
|\operatorname{PGL}_3(k)|=\frac{(4^3-1)(4^3-4)(4^3-4^2)}{4-1}=60{,}480,
\]
the orbit–stabilizer theorem gives stabilizer size \(60{,}480/960=63\).

**Independent direct group check.** The C++ verifier also loops over all \(4^9\) matrices with entries in \(k\). Exactly \(181{,}440\) matrices are invertible. For each invertible \(A\), it checks at the 21 rational points whether \(F(A P)=\det(A)F(P)\) for the diagonal representative. The evaluation map for cubics \(G(X^2,Y^2,Z^2)\) has rank ten on these 21 points, as independently verified by exact Gaussian elimination in the same program; therefore these values determine equality of the **polynomials**, not merely equality of functions on a small finite set. Exactly **189** invertible matrices stabilize the normalized representative. Dividing the two matrix counts gives an orbit of size \(181{,}440/189=960\). Thus the C++ calculation alone proves the same one-orbit conclusion without the Python breadth-first computation. The corresponding projective stabilizer has \(189/3=63\) elements.

**4. Explicit representative.** The minimum coefficient encoding found by the exhaustive orbit calculation is \([3,0,0,2,0,0,0,0,0,1]\), with the field elements \(2=\alpha\) and \(3=\alpha+1\) encoded as two-bit integers. This is exactly \(C_0\) displayed above. Smoothness can also be verified by hand: at a rational projective point with one or two nonzero coordinates, the mixed term vanishes and the diagonal coefficients sum to a nonzero element. With three nonzero coordinates, all sixth powers equal \(1\), the diagonal coefficients sum to \(1+\alpha+(\alpha+1)=0\), and \(X^3+Y^3+Z^3=1\), leaving the nonzero value \(XYZ\). So \(C_0\) avoids all \(21\) rational points and is geometrically smooth by Step 1. Its genus is \((6-1)(6-2)/2=10\).

## Verification

Compile and run the standalone C++17 program with `c++ -O2 -std=c++17 verify_fnc_f4_count.cpp -o verify && ./verify`. It independently exhausts all \(4^{10}\) ten-tuples and all \(4^9\) projective-matrix representatives using integer-based arithmetic in \(k\), reporting `F4_EXTREMAL_SEXTICS_COUNT_PASS 960` and `F4_EXTREMAL_SEXTICS_PGL_ORBIT_PASS 181440 189 960`.

Run the standalone Python 3 program with `python verify_fnc_f4_sextics.py` (requires NumPy). It independently performs all \(4^{10}\) evaluations and verifies the projective affine action and the orbit search. Its final line is `SMOOTH_F4_FNC_SEXTIC_UNIQUE_ORBIT_PASS`; preceding lines report the count \(960\), group order \(60{,}480\), orbit size \(960\), stabilizer order \(63\), and the representative coefficients. Both programs were executed on the files included with this result and returned their indicated success lines.

## Relationship to prior work

Asgarli, Duan, and Lai, Theorem 1.6(3), supply the **complete defining-family normal form**; their Example 4.11 explicitly constructs a degree-six member over \(\mathbb F_4\), and Corollary 4.9 proves the absence of rational points for every smooth extremal member. None of those statements gives the number of smooth coefficient models, the number of \(\operatorname{PGL}_3(\mathbb F_4)\)-orbits, a diagonal representative, or the order of its rational projective stabilizer. The present classification starts from, rather than reclaims, that normal form.

A close geometric comparison is Borges, Korchmáros, and Speziali, Theorem 4.21, which classifies degree-\(q+2\) curves invariant under a **specified Singer-normalizer subgroup**, up to projectivity over \(\mathbb F_{q^3}\), as Pellikaan curves. Its hypothesis presupposes the given symmetry and its equivalence is allowed over a larger field. It does not establish that every smooth Frobenius-nonclassical sextic over \(\mathbb F_4\) has that symmetry or determine equivalence **over \(\mathbb F_4\)**, and it does not supply the 960-equation census. The present claim is deliberately limited to that sharper rational-field classification. Algebraic-closure equivalence alone would not imply rational-field transitivity.

Earlier Cossidente–Siciliano work on Singer automorphisms (2003, 2006) is another relevant comparison, but its published claims assume automorphisms of Singer type; the 2003 article full text was not available for direct inspection. This is a residual priority risk rather than evidence of complete rational-field coverage.

Targeted searches for the aliases *maximal-degree Frobenius-nonclassical sextic*, *extremal characteristic-two plane curve*, *Singer-normalizer/Pellikaan sextic*, and the numerical pair \((960,63)\) did not identify a prior statement of this exact classification. This negative search is not proof of historical priority.

## Limitations

This determines the rational projective classification of these degree-six plane models only; it does not classify all abstract genus-ten curves, automorphisms defined over extension fields, or analogous extremal families over larger even fields. The coefficient count and transitivity are finite exhaustive computations backed by complete source code, not an independent formal proof assistant certificate. The projective stabilizer order \(63\) is over \(\mathbb F_4\) and is not asserted to equal the geometric automorphism-group order. Priority is not independently audited; older finite-geometry or Singer-cycle results could imply an equivalent rational-field classification.

## References

1. S. Asgarli, L. Duan, K.-W. Lai, *Frobenius nonclassical hypersurfaces*, arXiv:2207.11981 (first posted 2022-07-25), especially Theorem 1.6(3), Corollary 4.9, and Example 4.11. https://arxiv.org/abs/2207.11981
2. H. Borges, G. Korchmáros, P. Speziali, *Plane curves with a large linear automorphism group in characteristic p*, arXiv:2202.05765 (first posted 2022-02-11), especially Section 4.6 and Theorem 4.21. https://arxiv.org/abs/2202.05765

3. A. Cossidente, A. Siciliano, *Plane algebraic curves with Singer automorphisms*, J. Number Theory 99 (2003), 373–382, DOI:10.1016/S0022-314X(02)00070-7 (public abstract; original full text not examined).
