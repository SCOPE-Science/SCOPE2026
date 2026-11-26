# Six Hasse components and twenty-three transverse superspecial parameters for Ciani quartics in characteristic seven

## Finding
Let \(k=\overline{\mathbb F}_7\) and consider the standard coefficient-marked Ciani quartic
\[
C_{r,s,t}: X^4+Y^4+Z^4+rX^2Y^2+sY^2Z^2+tZ^2X^2=0.
\]
Let \(U\subset\mathbb A_k^3\) be its smooth-curve parameter space, namely
\[
U=\{(r,s,t):(r^2-4)(s^2-4)(t^2-4)\Delta\ne0\},\qquad
\Delta=r^2+s^2+t^2-rst-4.
\]
For \(i\in\{x,y,z\}\) set
\[
\begin{aligned}
B_x&=2rt-4s,&D_x&=B_x^2-(r^2-4)(t^2-4),\\
B_y&=2rs-4t,&D_y&=B_y^2-(r^2-4)(s^2-4),\\
B_z&=2st-4r,&D_z&=B_z^2-(s^2-4)(t^2-4).
\end{aligned}
\]
Then for every \((r,s,t)\in U(k)\), the geometric \(7\)-rank and Jacobian \(a\)-number satisfy
\[
f_7(C_{r,s,t})=\sum_{i\in\{x,y,z\}}\mathbf1_{B_iD_i\ne0},\qquad
a(C_{r,s,t})=3-f_7(C_{r,s,t}).
\]
The reduced nonordinary divisor in \(U\) has **exactly six geometrically irreducible, smooth components**, the hypersurfaces \(B_x,B_y,B_z,D_x,D_y,D_z=0\). Within each matching pair, \(V(B_i)\cap V(D_i)\cap U=\varnothing\).

The superspecial locus (equivalently the \(7\)-rank-zero locus) is a reduced zero-dimensional scheme of **length \(23\)**. At every one of its points, exactly three distinct nonordinary components meet, and their tangent hyperplanes are independent. Eleven points have coefficients in \(\mathbb F_7\), while twelve are defined over \(\mathbb F_{49}\) but not \(\mathbb F_7\). The incidence counts, according to whether the vanishing factor in the \(x,y,z\) quotient is of type \(B\) or \(D\), are
\[
\begin{array}{c|cccccccc}
\text{type}&BBB&BBD&BDB&DBB&BDD&DBD&DDB&DDD\\ \hline
\text{points}&1&2&2&2&4&4&4&4.
\end{array}
\]
All four values \(f_7=0,1,2,3\) occur among smooth curves in this family.

## Assumptions and scope
All statements are geometric over the algebraic closure of characteristic seven. A point means an **ordered, coefficient-marked** triple \((r,s,t)\) in the fixed standard equation, not an isomorphism class of unmarked quartics. Different coefficient triples may define isomorphic curves. The six components refer to divisors on the open coefficient space \(U\), not to the coarse moduli space. Source literature supplies the prime-to-seven elliptic quotient decomposition and the fact that superspecial smooth standard Ciani quartics have coefficient triples in \(\mathbb F_{49}\); the divisor geometry and marked intersection census are asserted here.

For an explicit geometric list, fix \(\eta\in\mathbb F_{49}\) with \(\eta^2=3\). The \(23\) triples are exactly: the origin; the six coordinate permutations of \((\pm1,0,0)\); the four triples in \(\{3,4\}^3\) satisfying \(rst=1\); and the twelve triples obtained by placing one entry \(a\in\{3,4\}\) and two entries \(b,c\in\{3\eta,4\eta\}\) in any three distinct coordinate positions, subject to \(abc=4\). These are disjoint families of sizes \(1,6,4,12\), respectively.

## Proof
**Elliptic quotients and Hasse factors.** Involution \(X\mapsto-X\) gives a genus-one quotient. On the chart \(Z=1\), putting \(u=Y\), \(v=2X^2+ru^2+t\) yields the birational model
\[
v^2=(r^2-4)u^4+(2rt-4s)u^2+(t^2-4).
\]
Its right-hand quartic is squarefree: its leading and constant coefficients are nonzero on \(U\), while the discriminant of the quadratic in \(u^2\) equals \(16\Delta\). In characteristic seven, the Hasse coefficient of the elliptic model is the coefficient of \(u^6\) in the cube of this quartic, namely
\[
B_x^3+6(r^2-4)(t^2-4)B_x=B_xD_x.
\]
The other two involutions similarly give \(B_yD_y\) and \(B_zD_z\). The classical decomposition of the Ciani Jacobian is an isogeny of degree eight to the product of the three elliptic quotients (Ohashi, Section 3). Since eight is prime to seven, it induces an isomorphism of their \(7\)-divisible groups. Each elliptic factor has \(7\)-rank one and \(a\)-number zero when ordinary, and \(7\)-rank zero and \(a\)-number one when supersingular. This proves both rank formulae. As a direct cross-check, the plane-quartic Hasse–Witt matrix is diagonal, and its three diagonal entries are exactly \(B_xD_x,B_yD_y,B_zD_z\); `verify_symbolic.py` checks these coefficient identities in \(\mathbb F_7[r,s,t]\).

**The six divisor components.** Each \(B_i\) has a nonzero constant partial derivative with respect to the omitted coefficient, so its zero locus is smooth and irreducible. For instance, \(D_x=0\) is, after the invertible polynomial substitution \(w=2rt-4s\), the equation
\[
w^2=(r^2-4)(t^2-4).
\]
The right side is not a square in \(k(r,t)\), because each of its four distinct linear factors occurs with odd valuation. Hence \(D_x\) is absolutely irreducible by Gauss's lemma. Its singular points in affine three-space satisfy \(w=0\), \(r=\pm2\), and \(t=\pm2\), and therefore all lie outside \(U\). The argument is symmetric for \(D_y,D_z\). Moreover, \(B_x=D_x=0\) would force \((r^2-4)(t^2-4)=0\), excluded on \(U\), and similarly for the other pairs. All six components are nonempty on \(U\): for example, \((0,0,0)\) belongs to all \(B\)-components, and \((3,3,4)\) to all \(D\)-components. The six polynomials are pairwise nonassociate irreducibles, hence exhaust the components of the reduced nonordinary divisor.

**Complete superspecial locus.** Ohashi's Theorem 1.1 proves that a smooth superspecial standard Ciani quartic has its coefficients in \(\mathbb F_{7^2}\). Therefore it suffices to check all \(49^3=117649\) ordered triples in that field, imposing the stated open smoothness condition. The standalone `verify_field.py` uses \(\mathbb F_{49}=\mathbb F_7[\eta]/(\eta^2-3)\), exact field addition/multiplication, and exhaustively tests the three equations \(B_iD_i=0\). It obtains exactly the above explicit \(23\) triples, the eight type counts, and the \(11+12\) field-of-definition split. Its four further common zeros lie outside \(U\) and are not counted. Completeness over the algebraic closure follows from the cited theorem, not from extrapolating finite experiments.

**Reducedness and transverse incidence.** On \(U\), each common zero has exactly one vanishing factor from each pair \((B_i,D_i)\). Taking the three gradients of these chosen factors, `verify_field.py` computes their exact \(3\)-by-\(3\) determinant at every one of the \(23\) triples and checks it is nonzero in \(\mathbb F_{49}\). The Jacobian criterion therefore proves the common-zero scheme is reduced at every geometric point and the three branches meet transversely. The explicit list has examples of all four \(7\)-ranks: \((0,0,0)\) has rank zero; generic points on pairwise intersections outside the finite rank-zero set have rank one; generic points of any single component have rank two; and the complement of the nonordinary divisor is nonempty and has rank three. These existence statements also follow from the six distinct irreducible divisors in the three-dimensional irreducible open \(U\).

## Verification
From the extracted files in this package, run `python3 verify_symbolic.py` (with SymPy) and `python3 verify_field.py` (Python standard library). Expected terminal markers are `CIANI_CHAR7_SYMBOLIC_FACTORIZATION_OK` and `CIANI_CHAR7_F49_EXHAUSTIVE_23_TRANSVERSE_POINTS_OK`. The latter also prints the eight branch counts and the split \(11+12\). The first reconstructs coefficients of the sixth power of the plane quartic; the second is a complete finite-field sweep, not a Monte Carlo sample, and independently tests smoothness and gradient determinants. The external field-of-definition theorem is the necessary bridge from a finite census to a geometric classification.

## Relationship to prior work
Ohashi's 2022 study supplies Ciani smoothness, elliptic quotients, the prime-to-characteristic isogeny, and the \(\mathbb F_{p^2}\) rationality theorem for superspecial coefficients. It does **not** state the six-branch characteristic-seven Hasse divisor or the \(23\)-point transverse marked incidence classification. Moriya–Kudo (2022) develop general genus-three Howe-curve enumeration, report nonhyperelliptic isomorphism-class counts for primes \(11\) through \(47\), and do not provide this particular coefficient-marked rank-divisor stratification in characteristic seven. Bouw et al. (2020) analyze stable reduction types on the same three-dimensional Ciani moduli stratum, not its characteristic-seven Hasse incidence divisor. The general elliptic Hasse coefficient and all other standard inputs are acknowledged rather than counted as original contributions.

## Limitations
This result does not classify unmarked isomorphism classes, Newton polygons, or stable reductions of every characteristic-seven Ciani quartic. The exact \(23\)-point count is a geometric marked count, and some points can represent isomorphic curves. The existence of a full earlier unindexed equivalent computation remains a priority risk. The argument relies on the published standard-form field-of-definition theorem; independent external validation of this finding has not been performed.

## References
1. R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996, first public version 2022-01-31; especially Lemma 2.1, Section 3, and Theorem 1.1.
2. T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926, first public version 2022-09-07; especially Section 5 and Table 2.
3. I. Bouw, N. Coppola, P. Kılıçer, S. Kunzweiler, E. Lorenzo García, and A. Somoza, *Reduction type of genus-3 curves in a special stratum of their moduli space*, arXiv:2003.07633, first public version 2020-03-17.
4. J. D. Achter and E. W. Howe, *Hasse–Witt and Cartier–Manin matrices: a warning and a request*, arXiv:1710.10726, first public version 2017-10-30 (conventions for semilinear operators).
