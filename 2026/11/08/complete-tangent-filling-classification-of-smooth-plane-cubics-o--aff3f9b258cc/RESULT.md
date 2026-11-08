# Complete tangent-filling classification of smooth plane cubics over \(\mathbb F_3\)

## Finding

A projective plane curve \(C\) over \(\mathbb F_3\) is **tangent-filling** if the tangent lines at its smooth \(\mathbb F_3\)-points together contain every point of \(\mathbb P^2(\mathbb F_3)\). There are precisely three \(\operatorname{PGL}_3(\mathbb F_3)\)-equivalence classes of tangent-filling geometrically smooth plane cubics:

| Representative cubic \(F=0\) | \(\#C(\mathbb F_3)\) | Scalar-normalized equations | Stabilizer order |
|---|---:|---:|---:|
| \(F_4=Y^3+XZ^2-X^2Y\) | 4 | 936 | 6 |
| \(F_6=Y^2Z+XZ^2+XYZ+X^2Y\) | 6 | 1872 | 3 |
| \(F_7=Y^3+XZ^2+X^2Z-X^2Y\) | 7 | 936 | 6 |

In particular, there are \(3744\) tangent-filling scalar-normalized cubics among all \(16848\) geometrically smooth scalar-normalized cubics, giving the exact probability \(3744/16848=2/9\). Here a scalar-normalized cubic is a nonzero homogeneous cubic whose first nonzero coefficient in a fixed ten-monomial ordering is \(1\); this represents one equation modulo nonzero scalar multiplication. The minimum degree of a geometrically irreducible tangent-filling plane curve over \(\mathbb F_3\) is therefore \(3\).

The rational-point count alone does **not** decide tangent-filling: both filling and nonfilling smooth cubics exist with \(4\) rational points, and likewise with \(6\) rational points.

## Assumptions and scope

The base field is exactly \(\mathbb F_3\), and equivalence means coordinate change by \(\operatorname{PGL}_3(\mathbb F_3)\). The counting measure is uniform on the set of homogeneous cubic equations modulo nonzero scalars, *not* uniform on isomorphism classes or abstract elliptic curves. All smoothness assertions are geometric, over an algebraic closure. Tangents must occur at smooth rational points.

## Proof

**Exhaustive incidence reduction.** The \(\mathbb F_3\)-vector space of ternary cubics has dimension \(10\); its nonzero vectors modulo scalar give exactly \((3^{10}-1)/2=29524\) equations. The projective plane has \(13\) rational points and \(13\) rational lines, each line containing \(4\) points. Represent each projective point by the unique vector in \(\{0,1,2\}^3\) whose first nonzero entry is \(1\). Let the ten monomials be \(X^iY^jZ^k\) for \(i+j+k=3\), in lexicographic exponent order. For each of the \(29524\) scalar-normalized coefficient vectors, evaluate the cubic and its three formal partial derivatives at each of the \(13\) normalized points. Whenever \(F(P)=0\) and \(\nabla F(P)\ne0\), the line \(\nabla F(P)\cdot(X,Y,Z)=0\) is the tangent at \(P\). The union of the resulting line masks equals the all-\(13\)-point mask for precisely \(936+1872+936=3744\) equations. Their respective rational-point and distinct-tangent-line counts are \((4,4)\), \((6,6)\), \((7,7)\). This is a complete finite enumeration, not sampling; the first bundled standalone program supplies executable loop bounds and arithmetic.

**Direct tangent-line witnesses.** Write \( [a:b:c]\) for the line \(aX+bY+cZ=0\). The lines obtained from the rational points of the three representatives are, respectively: for \(F_4\), \([1:0:0], [0:1:0], [1:2:0], [1:1:0]\); for \(F_6\), \([1:0:0], [0:0:1], [0:1:0], [1:2:0], [1:0:2], [0:1:2]\); and for \(F_7\), \([1:0:0], [0:1:2], [1:1:1], [1:2:1], [0:1:1], [1:1:2], [1:2:2]\). Substitution of these explicit line equations at all \(13\) rational points confirms that each list covers the plane. All three lists consist of distinct rational tangent lines. In the \(F_4\) case, these are precisely the four lines of the pencil through \([0:0:1]\).

**Projective orbit partition.** Enumerate all invertible \(3\times3\) matrices over \(\mathbb F_3\), modulo common nonzero scalar, yielding \(|\operatorname{PGL}_3(\mathbb F_3)|=5616\). For each of the three displayed representatives, apply each matrix to the \(13\) projective points and transform the cubic evaluations using degree-three homogeneity: if \(AP=tP'\) with \(P'\) normalized, then \(F(AP)=t^3F(P')=tF(P')\) in \(\mathbb F_3\). The evaluation vector uniquely determines the cubic class: an exhaustive check of all \(29524\) normalized forms verifies injectivity. The three orbits have sizes \(936,1872,936\), each exactly the entire tangent-filling stratum with its indicated rational-point count. Their union is all \(3744\) candidate equations. Their stabilizer orders are \(5616/936=6\), \(5616/1872=3\), and \(6\). Because rational-point counts are projective invariants, the three orbits are distinct.

**Geometric smoothness.** For both \(F_4\) and \(F_7\), the derivative \(F_Y=-X^2\). At any hypothetical singular point, \(X=0\), then \(F_X=Z^2\) forces \(Z=0\), and the defining equation forces \(Y=0\), impossible in projective space. For \(F_6\), derivatives over \(\mathbb F_3\) are
\[
 F_X=Z^2+YZ-XY,\qquad F_Y=-YZ+XZ+X^2,\qquad F_Z=Y^2-XZ+XY.
\]
If \(X=0\), the derivatives force first \(Y=0\), then \(Z=0\). If \(X\ne0\), set \(X=1\); the equations \(F_Z=F_Y=0\) give \(Z=Y^2+Y\) and \(Y^3-Y=1\). Reducing \(F_6(1,Y,Y^2+Y)\) modulo \(Y^3-Y-1\) gives \((Y-1)^2\); its vanishing requires \(Y=1\), contradicting \(Y^3-Y=1\). Therefore all three are smooth. Smoothness is preserved by projective coordinate changes, so every tangent-filling equation in the three orbits is geometrically smooth.

**Smooth denominator.** For completeness, the second standalone verifier partitions *all* \(29524\) normalized cubic equations into \(25\) projective orbits. It checks one representative of each orbit for singular points on every affine chart \(X=1\), \(Y=1\), \(Z=1\), using exact reduced Gröbner bases over \(\mathbb F_3\) for the ideal \((F,F_X,F_Y,F_Z)\). Such an affine ideal is the unit ideal precisely when there is no geometric singular point on the chart, by the algebraically closed Nullstellensatz. Exactly \(10\) projective orbits are smooth, with weighted orbit total \(16848\). Thus the conditional fraction is \(3744/16848=2/9\).

**Minimal degree.** A line has just one tangent line and cannot fill \(13\) points. A geometrically irreducible conic over \(\mathbb F_3\) is smooth; it has \(4\) rational points and hence \(4\) rational tangents. No three of these tangents are concurrent because the dual of a smooth conic is a smooth conic. Their union contains \(4\cdot4-\binom42=10<13\) points. A geometrically reducible but base-field irreducible conic has no smooth rational points (its rational points, if any, lie in the intersection of its conjugate components). Therefore no irreducible curve of degree \(1\) or \(2\) is tangent-filling, while the displayed smooth cubics are.

## Verification

Run \(`python3 verify_tangent_cubics_f3.py`\), requiring only the Python standard library; it prints \(`TANGENT_FILLING_CUBICS_F3_CLASSIFICATION_PASS`\) after exhaustively testing the \(29524\) forms and \(5616\) projective actions. Run \(`python3 verify_all_smooth_cubics_f3.py`\) in the same directory with SymPy installed; it prints \(`SMOOTH_CUBIC_ORBIT_CENSUS_F3_PASS`\) after its exact Gröbner classification of \(25\) orbits and weighted smooth total. Both were executed successfully on their packaged source paths. The explicit smoothness arguments above do not rely on these computations. The exact finite census uses exhaustive algorithms, not statistical extrapolation or an infinite-field claim.

## Relationship to prior work

Asgarli and Ghioca's *Tangent-filling plane curves over finite fields* (first public 26 February 2023), especially Definition (d), Theorems 1.1–1.3, Remark 1.4, and Question 1.5, introduces the property, obtains general exclusion bounds and explicit families, and asks for the minimum degree for each \(\mathbb F_q\). It does not enumerate the smooth cubic case \(q=3\), its tangent-incidence projective orbits, or the conditional probability. Their characteristic-three remark concerns a different \(q-1\)-degree family and does not imply this classification.

Ishitsuka's *Linear determinantal representations of smooth plane cubics over finite fields* (2016), Sections 5–7, uses Schoof's enumeration to count classes with prescribed numbers of rational points or determinantal representations, not whether rational tangent lines cover the plane. Its rational-point counts alone cannot imply this incidence classification: the counts \(4\) and \(6\) each occur among filling and nonfilling smooth models. Prior standard results on smooth ternary cubics and the projective plane are used only as background. No priority or independent-validation claim is made.

## Limitations

All classification and probability claims concern exactly \(\mathbb F_3\), scalar-normalized plane cubic equations, and coordinate equivalence over the ground field. The theorem does not count abstract elliptic isomorphism classes or extend the classification to other field sizes. Exact enumeration is the proof of the finite orbit table; while reproducible, it is not an independent mathematical audit. An equivalent older classification under another vocabulary or in unindexed finite-geometry literature remains a priority risk.

## References

1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420 (first public 2023-02-26), https://arxiv.org/html/2302.13420v2 .
2. Y. Ishitsuka, *Linear determinantal representations of smooth plane cubics over finite fields*, arXiv:1604.00115 (first public 2016-04-01), https://arxiv.org/html/1604.00115v2 .
