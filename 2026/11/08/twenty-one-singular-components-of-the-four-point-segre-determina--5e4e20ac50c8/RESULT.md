# Twenty-one singular components of the four-point Segre determinant

## Finding

Let \(Q=\mathbb P^1_{\mathbb C}\times\mathbb P^1_{\mathbb C}\subset\mathbb P^3_{\mathbb C}\) be the smooth Segre quadric. Let \(D\subset Q^4\) be the hypersurface of ordered quadruples whose four Segre vectors are linearly dependent, equivalently whose four points lie in a projective plane. Then the **reduced singular locus of \(D\) has exactly twenty-one irreducible components**: two of dimension five and nineteen of dimension four. There are no additional components.

More precisely, the components are two ruling components \(R_a,R_b\), seven two-value components \(B_{\{I,J\}}\), and twelve tangent-pair components \(T_{ij}^{+},T_{ij}^{-}\) defined below. Each component has generically an ordinary nondegenerate transverse quadratic singularity of codimension three (for a ruling component) or codimension four (for each other component). The hypersurface \(D\) is irreducible and normal.

## Assumptions and scope

Everything is over \(\mathbb C\). The product \(Q^4\) is smooth of dimension eight; the hypersurface \(D\) has dimension seven. Write each point as \(p_i=(a_i,b_i)\), with \(a_i,b_i\in\mathbb P^1\). On the standard affine chart \(p_i=(x_i,y_i)\), the defining equation is
\[
F=\det\begin{pmatrix}
1&x_1&y_1&x_1y_1\\
1&x_2&y_2&x_2y_2\\
1&x_3&y_3&x_3y_3\\
1&x_4&y_4&x_4y_4
\end{pmatrix}.
\]
This determinant is a global multihomogeneous section, so its zero and singular sets are independent of affine charts or choices of nonzero Segre representatives.

The two ruling components are
\[
R_a=\{a_1=a_2=a_3=a_4\},\qquad
R_b=\{b_1=b_2=b_3=b_4\}.
\]
For each nonempty proper **unordered** bipartition \(\{I,J\}\) of \(\{1,2,3,4\}\), put
\[
B_{\{I,J\}}=\{p_i=p\ (i\in I),\ p_j=q\ (j\in J),\ p,q\in Q\}.
\]
There are \((2^4-2)/2=7\) such components.

For an unordered pair \(\{i,j\}\), let \(k<\ell\) be the complementary labels. Define
\[
\begin{aligned}
T_{ij}^{+}&=\{p_i=p_j=(a,b),\ p_k=(a,b'),\ p_\ell=(a',b)\},\\
T_{ij}^{-}&=\{p_i=p_j=(a,b),\ p_k=(a',b),\ p_\ell=(a,b')\},
\end{aligned}
\]
where \(a,a',b,b'\) range freely in \(\mathbb P^1\). Equalities among the variable parameters are allowed, making these loci closed. There are six unordered pairs and two orientations, giving twelve components.

The term *generic transverse ordinary quadratic singularity* means that at a general smooth point of the stated singular-locus component, the quadratic term of a local equation on the smooth eightfold has rank equal to the component's codimension; analytically the hypersurface is locally a product of the component with an ordinary quadratic cone transverse to it. This statement does not classify the intersections of the twenty-one components or assert the singular scheme is reduced.

## Proof

**1. Rank stratification and the derivative.** Let \(M\) be the matrix with four Segre row vectors. At a point of matrix rank at most two, the adjugate of \(M\) vanishes, hence every first partial derivative of the determinant along \(Q^4\) vanishes. Thus the entire rank-at-most-two locus lies in \(\operatorname{Sing}(D)\).

Suppose \(\operatorname{rank}(M)=3\). There is a unique relation vector \(c=(c_1,c_2,c_3,c_4)\) between its rows, up to scalar, and a unique projective plane \(H\subset\mathbb P^3\) containing the four points. The adjugate has rank one, so the differential of the determinant is a nonzero scalar multiple of
\[
\mathrm dF=\sum_{i=1}^4 c_i\,h(\mathrm dv_i),
\]
where \(h\) is a linear form defining \(H\) and \(v_i\) are local Segre row representatives. The tangent directions of the four factors are independent. Consequently, \(\mathrm dF=0\) precisely when \(H\) contains the embedded tangent plane \(T_{p_i}Q\) for every index with \(c_i\ne0\).

The Gauss map of a smooth quadric surface is injective: a tangent plane is tangent at exactly one point. Therefore all points with nonzero relation coefficient must be the same point \(p\). The relation has support of size at least two. If it had support of size three or four, at least three rows would equal \(p\), making matrix rank at most two. Hence at rank three the relation support consists of **exactly two indices** \(i,j\), and \(p_i=p_j=p\). The other two points are distinct from \(p\), and their span with \(p\) is the plane \(H\). The singularity condition says exactly that \(H=T_pQ\).

**2. All rank-three singular points.** On the Segre quadric, the tangent plane section is the union of the two distinct ruling lines through \(p\). The two remaining points must lie on these two lines. Because the four rows have rank three, the remaining two points cannot lie on the same ruling through \(p\); each must be on one of the opposite rulings. This is exactly the set of rank-three points lying in one of \(T_{ij}^{+}\) or \(T_{ij}^{-}\). Conversely, every rank-three point on these loci has a duplicate row and all its rows in the tangent plane at that duplicate point. The derivative criterion proves it is singular.

**3. All rank-two singular points.** If the four points represent at most two distinct points, their configuration belongs to a two-value component \(B_{\{I,J\}}\), including the all-equal diagonal. Otherwise a rank-at-most-two configuration has at least three distinct collinear points on \(Q\). A projective line meeting a quadric surface in three distinct points is contained in the quadric; every line contained in \(Q\) is in one of its two rulings. Thus the entire quadruple lies on a ruling line, hence in \(R_a\) or \(R_b\). Conversely, every configuration in those components has matrix rank at most two. Combining steps 1–3 gives the claimed **set-theoretically exact** union of twenty-one closed subsets.

**4. Irreducible components and dimensions.** Each \(R_a\) and \(R_b\) is isomorphic to \((\mathbb P^1)^5\) and is irreducible of dimension five. Each two-value locus is isomorphic to \(Q^2\), and has dimension four. Each tangent-pair locus is isomorphic to \((\mathbb P^1)^4\), and has dimension four. At a general point of a ruling component all four points are distinct on one ruling line; such a point belongs to no other listed locus. At a general two-value point the two distinct values differ in both \(\mathbb P^1\)-coordinates and have exactly that prescribed partition; such a point belongs to no other listed locus. At a general tangent-pair point there are exactly three distinct values, only the designated pair is repeated, and the two other values occupy the two opposite tangent rulings; both the repeated pair and its orientation are intrinsic. Therefore no listed irreducible subset lies in another, and these twenty-one subsets are exactly the irreducible components of the reduced singular locus. The maximum singular-locus dimension is five.

**5. Irreducibility and normality.** Let \((\mathbb P^3)^\vee\) parameterize planes. On its dense open subset of planes meeting \(Q\) in a smooth irreducible conic \(C_H\), the incidence family of ordered four-tuples in \(C_H^4\) is irreducible of dimension \(3+4=7\): it is the fourth fiber product of a family of smooth conics with irreducible generic fiber. A general quadruple of distinct points on \(C_H\) spans \(H\), and a rank-three quadruple determines its plane uniquely. The omitted tangent-plane family has dimension at most \(2+4=6\): tangent planes to \(Q\) are parameterized by \(Q\), and their intersection with \(Q\) is the union of two lines, so choosing four points gives at most four further parameters. The rank-at-most-two strata have dimension at most five. Since a nonzero global determinant section on a smooth eightfold defines a pure seven-dimensional divisor, neither omitted family supports another irreducible component. Hence the non-tangent plane incidence image is dense in all of \(D\), and \(D\) is irreducible of dimension seven. The determinant is generically smooth: a general plane section is transverse to \(Q\), so the derivative criterion from step 1 cannot vanish at a general rank-three quadruple. As a hypersurface in a smooth variety, \(D\) is Cohen–Macaulay, hence satisfies \(S_2\); since its singular locus has dimension five, codimension two inside \(D\), it satisfies \(R_1\). Serre's criterion proves normality.

**6. Generic transverse quadratic types.** At a smooth general point of an irreducible singular-locus component \(S\) of codimension \(c\) in \(Q^4\), the Hessian of a local equation vanishes on all tangent directions to \(S\), so its rank is at most \(c\). To establish equality, it suffices by openness and symmetry to find one exact rational point of each generic configuration type where the Hessian has rank \(c\). There are four types: a ruling point, a two-value point with partition size \(1+3\), a two-value point with partition size \(2+2\), and a rank-three tangent-pair point. The attached exact-arithmetic verifier uses coordinates \((x_1,y_1,\ldots,x_4,y_4)\) and exhibits respectively the following rational witnesses and Hessian ranks:
\[
\begin{array}{c|c|c}
\text{type}&(p_1,p_2,p_3,p_4)&\operatorname{rank}(\operatorname{Hess}F)\\\hline
\text{ruling}&((0,0),(0,1),(0,2),(0,3))&3\\
1+3&((0,0),(0,0),(0,0),(1,1))&4\\
2+2&((0,0),(0,0),(1,1),(1,1))&4\\
\text{tangent pair}&((0,0),(0,0),(0,2),(3,0))&4
\end{array}
\]
The displayed Hessian ranks can be independently verified from the polynomial determinant; the attached code also supplies explicit nonzero minors. Relabeling the points and interchanging the two Segre factors sends the components to representatives of these four combinatorial types (without requiring transitivity on all parameter values). Each representative has an irreducible parameter space, so the corresponding nonzero Hessian minor persists on a dense open subset; by these symmetries the rank is maximal on a nonempty open subset of every component. The complex analytic Morse–Bott lemma applied transverse to that smooth singular stratum gives the asserted ordinary quadratic germs. No generic-type assertion is made at the intersections of the components.

## Verification

The standalone file `segredet_singularity_verify.py` uses exact finite arithmetic. Running `python segredet_singularity_verify.py` enumerates every configuration in \(Q(\mathbb F_2)^4\), checks singularity by all tangent derivatives of the determinant, and independently compares the result with the stated twenty-one geometric pieces. It finds \(6561\) total configurations, \(4617\) determinant-zero configurations, and \(1161\) singular configurations (\(729\) of matrix rank at most two, \(432\) singular of rank three). This is an exhaustive finite-field check, not a proof of the characteristic-zero theorem.

With SymPy installed, the script constructs the exact integral determinant and Hessian and evaluates all four rational witness types in Step 6, proving rank-three and rank-four nondegeneracy at those witnesses by exact rational minors. These exact witnesses, plus openness of nonvanishing minors and the geometric argument, establish generic rank. The script performs no approximate or floating-point calculations.

## Relationship to prior work

Pratt's *The Segre Determinant* (2025, arXiv:2505.09204), especially Example 1.1, gives the same four-point equation in a cross-ratio form and develops its Chow–Lam and algebraic-vision interpretations. Alstad, Duff and Katzman's *Segre-Determinantal Loci and the Image Variety for Three Flatland Cameras* (2026, arXiv:2606.31965) proves structural properties of related Segre-determinantal ideals, including primality and Cohen–Macaulayness of suitable maximal-minor ideals. Those works provide the natural geometric setting and foundational equation.

The present result describes a different invariant: the **complete reduced singular-locus components of the four-point determinant**, including its rank-three tangent-plane pieces, and their generic transverse singularity types. The rank-at-most-two strata alone account for only nine of the twenty-one components. No claim is made that the defining determinant or the classical classification of lines on a quadric is new.

## Limitations

All arguments and generic transverse analytic types are established over \(\mathbb C\). This does not identify the full Jacobian singular **scheme** or its nilpotent or embedded structure, nor all analytic germs at component intersections. The finite-field enumerations are verification checks, not assertions about every positive characteristic. The status of historical priority is provisional; older work might describe the same locus using cross-ratio boundary divisors or incidence geometry. The review is not independent validation.

## References

- Elizabeth Pratt, *The Segre Determinant* (2025), arXiv:2505.09204, https://arxiv.org/abs/2505.09204.
- Colin Alstad, Timothy Duff, and Mordechai Katzman, *Segre-Determinantal Loci and the Image Variety for Three Flatland Cameras* (2026), arXiv:2606.31965, https://arxiv.org/abs/2606.31965.
