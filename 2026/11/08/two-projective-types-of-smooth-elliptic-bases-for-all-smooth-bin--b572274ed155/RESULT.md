# Two projective types of smooth elliptic bases for all-smooth binary quadric pencils

## Finding
Let \(k=\mathbb F_2\), let \(V=k[x_0,x_1,x_2,x_3]_2\), and let a **fully smooth pencil** be a two-dimensional \(k\)-vector subspace \(L\subset V\) such that each of its three nonzero quadratic forms defines a geometrically smooth surface in \(\mathbb P^3_k\). Its base is the scheme-theoretic intersection \(B_L=V(Q_0,Q_1)\) for any basis \(Q_0,Q_1\) of \(L\).

**Theorem.** Exactly \(10{,}080\) fully smooth pencils have a geometrically smooth base curve. They form exactly two orbits of \(\mathrm{PGL}_4(k)\), each of cardinality \(5{,}040\) and each with projective stabilizer of order \(4\). Their projective stabilizers are **nonisomorphic**: the two-point type has \(C_2\times C_2\) and the four-point type has \(C_4\). Their base curves are genus-one complete intersections of degree four, with \(2\) and \(4\) rational points, respectively. Their Hasse–Weil zeta numerators are respectively \(1-T+2T^2\) and \(1+T+2T^2\), so their Jacobians are not isogenous over \(k\).

The two projective types admit the following explicit representatives, with \(Q_0=x_0x_3+x_1x_2\) in both cases:

* **Two-point type:** \(Q_1=x_0^2+x_0x_2+x_0x_3+x_1x_3+x_2^2\).
* **Four-point type:** \(Q_1=x_0x_2+x_0x_3+x_1^2+x_1x_3+x_2^2\).

For context in the exhaustive proof, there are \(14{,}336\) fully smooth pencils altogether, in five projective orbits; the other \(4{,}256\) pencils have singular bases. This last classification is not advanced as a separate priority claim for the previously studied non-absolutely-irreducible bases.

## Assumptions and scope
The field is exactly \(\mathbb F_2\); a smooth quadric means geometrically smooth, not merely free of singular rational points. Pencils are unmarked two-dimensional vector subspaces, so their three nonzero members are not ordered. Equivalence is under rational changes of the four homogeneous coordinates; there is no extension of scalars in the classification. For each smooth base, adjunction for a smooth \((2,2)\) complete intersection in \(\mathbb P^3\) gives genus one and degree four. A rational point exists in each case, hence its base can be regarded as an elliptic curve after choosing one.

## Proof
**1. Exact smoothness criterion.** Write a form as
\[
Q=\sum_{i=0}^3 d_i x_i^2+ a_{01}x_0x_1+a_{02}x_0x_2+a_{03}x_0x_3+a_{12}x_1x_2+a_{13}x_1x_3+a_{23}x_2x_3.
\]
Its polar bilinear form has a \(4\)-by-\(4\) alternating matrix. Its determinant is the square of
\[
\pi(Q)=a_{01}a_{23}+a_{02}a_{13}+a_{03}a_{12}.
\]
A rank-four polar matrix rules out all gradient zeros. If the polar matrix is singular, its radical has dimension at least two; over an algebraic closure, the restriction of the quadratic to that radical vanishes at a nonzero vector, giving a geometric singular point. Thus \(Q\) is smooth if and only if \(\pi(Q)=1\). Exactly \(28\) of the \(64\) mixed-coefficient patterns satisfy this; independent choices of the four square coefficients give exactly \(448\) smooth forms.

**2. Complete finite enumeration.** Encode each form by a ten-bit integer in the monomial order
\[
(x_0^2,x_1^2,x_2^2,x_3^2,x_0x_1,x_0x_2,x_0x_3,x_1x_2,x_1x_3,x_2x_3).
\]
A pencil is represented by the lexicographically least pair from its set of three nonzero masks \(\{a,b,a\oplus b\}\). Enumerating \(a,b\) among the \(448\) smooth masks and retaining those with \(a\oplus b\) smooth, then deduplicating, produces exactly \(14{,}336\) pencils. Independently, the polar coefficient space has \(56\) admissible two-planes, each with \(16^2\) choices of quadratic refinements, giving \(56\cdot256=14{,}336\). All \(15\) rational projective points are enumerated, with the base-point cardinality distribution
\[
\begin{array}{c|rrrr}
\#B_L(\mathbb F_2)&0&2&4&6\\\hline
\#L&336&5040&5040&3920.
\end{array}
\]

The incidence identity \(\#Q_0(k)+\#Q_1(k)+\#(Q_0+Q_1)(k)=15+2\#B_L(k)\) provides a separate check: each of the fifteen rational projective points outside the base lies on exactly one of the three quadrics, while each base point lies on all three.

**3. Exhaustive rational-projective orbits.** The twelve elementary transvections \(x_i\mapsto x_i+x_j\) for \(i\ne j\) generate \(\mathrm{GL}_4(\mathbb F_2)=\mathrm{PGL}_4(\mathbb F_2)\), of order \(20{,}160\). Their exact action on each encoded form is computed by evaluating at the four standard basis vectors and at their six pairwise sums. Breadth-first traversal of every orbit from the least unvisited pencil exhausts all \(14{,}336\) pencils and gives:

| Canonical pair of form masks | Orbit cardinality | Base rational points | Rational-point counts on three quadrics | Stabilizer order |
|---|---:|---:|---|---:|
| `(192,352)` | 560 | 6 | `(9,9,9)` | 36 |
| `(192,353)` | 3360 | 6 | `(9,9,9)` | 6 |
| `(192,357)` | 5040 | 2 | `(5,5,9)` | 4 |
| `(192,358)` | 5040 | 4 | `(5,9,9)` | 4 |
| `(198,367)` | 336 | 0 | `(5,5,5)` | 60 |

The total of these disjoint orbit sizes is \(14{,}336\). The two indicated representatives translate to the equations in the theorem. For the two-point representative, the four row-bitmask matrices fixing its pencil are `(1,2,4,8)`, `(3,2,12,8)`, `(4,8,1,2)`, and `(12,8,3,2)`; the three nonidentity matrices have order two. For the four-point representative they are `(1,2,4,8)`, `(8,4,2,1)`, `(10,13,11,5)`, `(5,11,13,10)`; their orders are one, two, four, four. All are verified by direct substitution and multiplication, and no further stabilizers are possible by the orbit–stabilizer formula. Hence the groups are \(C_2\times C_2\) and \(C_4\), respectively.

**4. Exact geometric smoothness of the bases.** For each of `(192,357)` and `(192,358)`, let \(f,g\) denote the two printed forms. The Jacobian ideal of their common zero scheme is generated by \(f,g\) and the six \(2\)-by-\(2\) minors of \((\nabla f,\nabla g)\). In each of the four affine charts \(x_i=1\), reduced Gröbner bases over \(\mathbb F_2\) are **exactly** \(\{1\}\) for both representatives (eight unit-ideal certificates in all), proving geometric nonsingularity. As two independent quadrics form a complete intersection, these are smooth connected genus-one quartics. The remaining orbit bases contain \(0\) or \(6\) rational points. A geometrically smooth genus-one base would have between \(1\) and \(5\) rational points by Hasse's inequality \(|\#B(\mathbb F_2)-3|\le2\sqrt2\). Hence none of the remaining bases is smooth. This proves the two-orbit classification.

**5. Arithmetic distinction.** The two smooth-base orbit representatives have exactly \(2\) and \(4\) rational points by direct exhaustive evaluation. For an elliptic curve over \(\mathbb F_2\), the Frobenius trace is \(t=3-\#E(\mathbb F_2)\), so \(t=1\) and \(t=-1\). The zeta numerator is \(1-tT+2T^2\). Different Frobenius characteristic polynomials exclude an isogeny over \(\mathbb F_2\). Independently, direct field arithmetic gives for the two types respectively \((\#E(\mathbb F_4),\#E(\mathbb F_8))=(8,14)\) and \((8,4)\).

## Verification
Run `python verify_binary_quadric_pencils.py` with Python 3.10 or newer and SymPy available. The script enumerates all encoded forms, checks the polar rank directly by binary Gaussian elimination, counts the pencils a second way using polar refinements, computes the full transvection-orbit partition, verifies explicit cyclic-versus-Klein stabilizer certificates and orbit-invariant projective point counts, computes eight projective Jacobian-unit ideals by exact characteristic-two Gröbner bases, and independently enumerates the smooth bases over \(\mathbb F_4\) and \(\mathbb F_8\). It also tests the elementary parity obstruction to three-dimensional fully smooth linear systems. Expected terminal signature:

`BINARY_QUADRIC_PENCIL_SMOOTH_BASE_ORBITS_PASS 14336 5 5040 5040 10080`

No random sampling or floating-point tests are used. Enumeration of finite objects is exhaustive because all masks and projective points are traversed, and the listed transvections generate the entire rational projective group. The full geometric smoothness assertions are separately covered by exact unit-ideal certificates, not inferred from absence of singular rational points.

## Relationship to prior work
Asgarli and Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169 (first posted March 14, 2022), Section 3 and especially Proposition 3.5, construct fully smooth pencils of quadric surfaces in even characteristic. That work establishes existence but does not state the two rational-projective classes of those pencils having smooth elliptic bases, their exact cardinalities, or their distinct Frobenius traces. Bruen and Hirschfeld, *Intersections in projective space II: Pencils of quadrics*, *European Journal of Combinatorics* 9 (1988), 255–270, DOI 10.1016/S0195-6698(88)80017-9, give an older classification whose accessible abstract specifies **non-absolutely-irreducible base curves**. That earlier classification is material to the three singular-base orbits but its publicly accessible abstract does not settle the smooth-base claim here. Fevola, Mandelshtam and Sturmfels, *Pencils of Quadrics: Old and New*, arXiv:2009.04334, concerns a different characteristic-zero framework. These are implications-based comparisons, not assertions that all historical papers were inspected in full.

## Limitations
The theorem is specific to \(\mathbb F_2\) and to pairs of quadrics in \(\mathbb P^3\). It does not classify pencils over larger finite fields, embeddings over their algebraic closures, or all elliptic curves. Some earlier finite-geometry classifications may imply parts of this finite result without using the same terminology; in particular the complete 1988 source was unavailable for full-text inspection. The attached computation is independently replayable but is not a substitute for an independent mathematical audit.

## References
1. Shamil Asgarli and Dragos Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169 (2022), https://arxiv.org/abs/2203.07169 (Section 3, Proposition 3.5).
2. Aiden A. Bruen and James W. P. Hirschfeld, *Intersections in projective space II: Pencils of quadrics*, *European Journal of Combinatorics* 9 (1988), 255–270, https://doi.org/10.1016/S0195-6698(88)80017-9 (abstract accessible; full text not inspected).
3. Claudio Fevola, Yelena Mandelshtam, Bernd Sturmfels, *Pencils of Quadrics: Old and New*, arXiv:2009.04334, https://arxiv.org/abs/2009.04334.
