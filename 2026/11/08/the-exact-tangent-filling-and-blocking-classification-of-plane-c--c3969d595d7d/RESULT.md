# The exact tangent-filling and blocking classification of plane cubics over \(\mathbb F_4\)

## Finding
Let \(F\) vary over the homogeneous nonzero ternary cubics with coefficients in \(\mathbb F_4\), modulo multiplication by a nonzero field scalar, and let \(C_F\) be its plane zero locus. Assume that every point of \(C_F(\mathbb F_4)\) is nonsingular on \(C_F\) (no geometric smoothness assumption). Say **blocking** means that every rational line contains a rational curve point; say **tangent-filling** means that the union of tangent lines at rational curve points is the entire rational projective plane.

**Theorem.** For every such \(F\), blocking and tangent-filling are equivalent. Precisely \(6328\) scalar-normalized equations satisfy either property, in two and only two \(\operatorname{PGL}_3(\mathbb F_4)\)-orbits:

| Orbit | Equations | Rational curve points | Stabilizer order | Geometric form |
| --- | ---: | ---: | ---: | --- |
| Hermitian | 280 | 9 | 216 | Smooth cubic \(X^3+Y^3+Z^3=0\) |
| External line-conic | 6048 | 10 | 10 | \(Z(X^2+XY+\alpha Y^2+Z^2)=0\) where \(\alpha^2+\alpha+1=0\) |

In particular, among *geometrically smooth* plane cubics, the two incidence properties are equivalent and hold exactly for the \(280\) scalar-normalized equations projectively equivalent to the Hermitian cubic. The other \(6048\) cubics are geometrically reducible, but have no singular points over \(\mathbb F_4\). No implication for larger fields is asserted.

## Assumptions and scope
Fix the field \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\), with coefficients represented by \(0,1,\alpha,\alpha+1\), encoded as \(0,1,2,3\). The projective plane has \(21\) rational points and \(21\) rational lines, each line having \(5\) rational points. A rational point of \(C_F\) is nonsingular when its three homogeneous partial derivatives are not all zero. The tangent line at such a point has coefficient vector equal to the gradient, with Euler's identity ensuring that the point is on that line.

Every cubic is represented by the ten coefficients, in the fixed order \[(X^3,Y^3,Z^3,X^2Y,X^2Z,XY^2,Y^2Z,XZ^2,YZ^2,XYZ).\] The integer mask is \(\sum_{i=0}^{9}a_i4^i\), where \(a_i\) is the encoded coefficient. Scalar normalization requires the first nonzero coefficient to be \(1\). There are \[(4^{10}-1)/3=349525\] such masks. The two representative masks are \(21\) and \(270608\), respectively.

## Proof
**1. Exhaustive incidence and rational-smoothness classification.** The standalone C++ program `verify_f4_cubic_census.cpp` enumerates every integer from \(1\) to \(4^{10}-1\), retains precisely the masks having first nonzero base-four digit \(1\), and evaluates the corresponding cubic and its three formal partial derivatives at all \(21\) projective points. It rejects a mask if any rational zero has vanishing gradient. For every remaining cubic it computes the union of its rational tangents and tests all \(21\) rational lines for intersection with the rational zero set. Each incidence test uses all points/lines, not samples or probabilistic computations. Field multiplication is polynomial reduction modulo \(\alpha^2+\alpha+1\); addition is bitwise XOR. The exact check shows that \(248928\) masks are rational-pointwise nonsingular, of which \(6328\) are tangent-filling and \(6328\) blocking, and that the two selected mask sets coincide. These sets comprise \(280\) masks having \(9\) rational zeros and \(6048\) having \(10\) rational zeros. None with other rational-point counts qualifies. The other \(100597\) masks have a rational singular zero and are outside the theorem's domain.

**2. Independent geometric decomposition.** The separate Python program `verify_f4_cubic_geometry.py` re-implements arithmetic via a hard-coded \(4\)-element field multiplication table. It enumerates all \({21\choose7}\), \({21\choose8}\), and \({21\choose9}\) point subsets satisfying the necessary nontrivial blocking condition of meeting each line in between one and three points. The counts are \(360,0,280\), respectively, with the \(280\) nine-point configurations being the nine-point unitals. It separately enumerates every normalized quadratic form and finds \(1008\) nonsingular conics, each admitting exactly \(6\) rational lines disjoint from the conic. Forming \(LQ\) for every such external pair gives exactly \(6048\) distinct scalar-normalized cubic equations, all belonging to the selected incidence set. Their rational point sets also number \(6048\). The remaining \(280\) selected equations determine precisely the \(280\) unital point configurations.

**3. Exact projective orbit check.** The Python verifier enumerates all \(60480\) elements of \(\operatorname{PGL}_3(\mathbb F_4)\) as normalized invertible matrices (allowing all scalar multiples of the second and third independent columns). Under the resulting complete point permutations, the Hermitian representative's nine-point zero set has orbit size \(280\), exactly the unital sets; the external line-conic representative's ten-point zero set has orbit size \(6048\), exactly the enumerated external line-conic sets. In each class its rational point-set determines a unique selected normalized equation, so these point-set orbit counts equal the equation-orbit counts. Orbit–stabilizer yields \(60480/280=216\) and \(60480/6048=10\). The first orbit is geometrically smooth because the Hermitian representative has three partial derivatives \(X^2,Y^2,Z^2\), which never simultaneously vanish projectively, and smoothness is projectively invariant. The second consists of a line and smooth conic whose intersection contains no rational point, hence every rational point of the union is smooth, despite geometric reducibility. The two classes exhaust all \(6328\) selected equations.

Together (1)–(3) prove the equivalence, enumeration, and orbit assertion.

## Verification
From the directory containing the two packaged programs, run

```bash
c++ -O2 -std=c++17 verify_f4_cubic_census.cpp -o cubic_census
./cubic_census candidate_masks.txt
python3 verify_f4_cubic_geometry.py candidate_masks.txt
```

The checked outputs end with `F4_CUBIC_TANGENT_BLOCKING_CENSUS_PASS 349525 6328 280 6048` and `F4_CUBIC_INDEPENDENT_GEOMETRY_PASS 60480 1008 6048 280 6048`. Both programs use only standard C++17/Python3 facilities. The first enumerates *all cubic equations* and their gradients; the second checks an independent finite-geometric classification, conic factorization, and every projective transformation. The `candidate_masks.txt` file is generated by the first command and is not a missing external dependency.

## Relationship to prior work
Prior exact small-field enumerations already give the 280 smooth Hermitian tangent-filling cubics and, more broadly, 11,368 tangent-filling cubic equations over the field of four elements (11,088 having a rational line component); those figures are background, not claimed as new. Asgarli, Ghioca and Yip [1] study plane curves whose rational points form blocking sets and exhibit the Hermitian cubic over the field of four elements as a boundary example. Asgarli and Ghioca [2] define tangent-filling curves and discuss Hermitian examples. Those papers motivate the two properties and establish examples, but neither states the simultaneous exhaustive \(6328\)-equation classification, the \(6048\) rationally nonsingular reducible family, or the equivalence of blocking and tangent-filling within the full rationally nonsingular cubic domain. Classical unital theory supplies background for the nine-point Hermitian configuration; classifying nine-point designs alone does not imply the theorem's incidence equivalence for all cubic equations or the external line-conic orbit count.

## Limitations
The smooth-Hermitian subcase and full tangent-filling counts have been computed previously; the contribution is their joint restriction with blocking and the rationally nonsingular external line–conic two-orbit classification. The result is finite-field-specific to \(\mathbb F_4\); no analogous equivalence is asserted in any other field. The rational-pointwise nonsingularity assumption is indispensable to the tangent-line definition used. The proof is an exact, reproducible exhaustive finite classification, not a field-uniform symbolic argument. Priority against every older or unindexed finite-geometric table is not independently certified, and no independent mathematical audit has been performed.

## References
[1] S. Asgarli, D. Ghioca and C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299, first publicly posted 2022-08-28.

[2] S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, first publicly posted 2023-02-26.
