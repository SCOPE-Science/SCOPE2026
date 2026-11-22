# Three tritangent counts reconstruct eight-point Frobenius splitting on degree-one del Pezzo surfaces

## Finding

Let \(q\) be a prime power of characteristic at least five. Let \(B\) be a Frobenius-stable reduced set of eight geometric points in \(\mathbb P^2_{\mathbb F_q}\) in del Pezzo general position: no three collinear, no six on a conic, and no cubic through all eight singular at one of them. Let \(S=\operatorname{Bl}_B(\mathbb P^2)\) be the degree-one del Pezzo surface. Its anti-bicanonical morphism is a double cover of a quadric cone, with smooth genus-four canonical branch curve \(C\).

Let \(\Theta\) be the reduced finite étale scheme of the \(120\) geometric odd theta characteristics of \(C\), equivalently its \(120\) theta-tritangent planes, and let \(T_n=\#\Theta(\mathbb F_{q^n})\). Then the triple \((T_1,T_2,T_3)\) uniquely determines the permutation cycle partition of geometric Frobenius on \(B\), among all \(22\) partitions of eight. Hence it determines all \(T_n\) and the zeta function of \(\Theta\). Precisely, if \(f_n,u_n,v_n\) denote the numbers of cycles of lengths \(1,2,3\), respectively, in the permutation \(\sigma^n\) on \(B\), then

\[
T_n=f_n+2\left(\binom{f_n}{2}+u_n\right)+\binom{f_n}{3}+f_nu_n+v_n.
\]

Across the \(22\) possible Frobenius partitions, the first count alone has \(13\) different values, the first two counts give \(20\) different ordered pairs, and all three counts give \(22\) different triples. In particular, degree three is sharp: the partitions \((1,7)\) and \((3,5)\) both give \((T_1,T_2)=(1,1)\), while their values of \(T_3\) are \(1\) and \(10\), respectively. They are realized by smooth degree-one del Pezzo surfaces over the same finite field whenever \(q>1456\) and the characteristic is at least five.

## Assumptions and scope

All points of \(B\) are distinct over the algebraic closure; the eight-point set is defined over the base field, but its individual points need not be. The ordering of \(B\) is only a geometric device; an arbitrary Frobenius permutation \(\sigma\in\mathfrak S_8\) acts on such a labeling. The theorem concerns the finite étale scheme of theta-tritangent *planes* and counts planes defined over extension fields, not necessarily planes with three individually rational contact points. Characteristic at least five avoids characteristic-two theta and double-cover issues and characteristic-three degeneracies. No hypothesis that \(B\) has rational points is imposed. The theorem is conditional on general position for arbitrary \(q\); the uniform existence assertion is stated only for \(q>1456\).

The \(\Theta\)-zeta function is defined as \(Z(\Theta,t)=\exp(\sum_{n\ge1}T_nt^n/n)\). If the induced Frobenius permutation of \(\Theta\) has \(a_d\) cycles of length \(d\), then \(Z(\Theta,t)=\prod_d(1-t^d)^{-a_d}\). This is the zeta function of the zero-dimensional tritangent configuration, not the Hasse–Weil zeta function of \(C\) or \(S\).

## Proof

**1. The tritangent action.** The \(240\) exceptional curves on a split degree-one del Pezzo surface are partitioned into \(120\) unordered pairs by the Bertini involution. Each pair maps to one odd-theta tritangent plane of the canonical genus-four branch curve. This description is equivariant under permutations of the eight blow-up points. The classical enumeration by degrees and multiplicity patterns of plane curves gives exactly four permutation families:

\[
\begin{array}{c|c|c}
\text{family}&\text{index set}&\text{number}\\\hline
\text{exceptional versus sextic}&\{1,\ldots,8\}&8\\
\text{line versus quintic}&\binom{[8]}2&28\\
\text{conic versus quartic}&\binom{[8]}5\simeq\binom{[8]}3&56\\
\text{complementary cubic pair}&\binom{[8]}2&28
\end{array}
\]

Here the last \(28\) entries are the unordered Bertini pairs of the \(56\) cubics having one double base point and one omitted base point. In terms of the ordered two distinct labels \((i,j)\) associated with those cubics, Bertini interchanges \((i,j)\) and \((j,i)\); thus the resulting plane is indexed by the unordered two-subset \(\{i,j\}\). The total is \(8+28+56+28=120\). The geometric identification and all four multiplicity patterns are documented in the primary literature and the publicly accessible tritangent-construction source listed below. In odd characteristic, odd genus-four theta characteristics each have a unique effective divisor of degree three: parity gives odd positive \(h^0\), while Clifford's inequality bounds \(h^0\le2\). Thus the corresponding tritangent planes are distinct and the described action applies to the full theta-tritangent scheme.

**2. Fixed-point formula.** An unordered \(k\)-subset of \([8]\) is fixed by a permutation precisely when it is a disjoint union of permutation cycles. Fixed singletons number \(f_n\); fixed two-subsets number \(\binom{f_n}2+u_n\); and fixed three-subsets number \(\binom{f_n}3+f_nu_n+v_n\). Adding the four index families establishes the displayed formula. If \(\sigma\) has a cycle of length \(d\), its \(n\)-th power has \(\gcd(d,n)\) cycles of length \(d/\gcd(d,n)\). Hence the formula computes \(T_n\) for every positive \(n\) directly from the original partition.

**3. Exhaustive 22-partition comparison.** The included `verify_tritangents.py` generates *all* integer partitions of eight, constructs a concrete permutation of each type, constructs all \(120\) distinct labeled subsets, and calculates its exact orbit decomposition. It independently recomputes fixed-point counts from the preceding formula at each exponent through the permutation order and asserts agreement for each class. It verifies that the numbers of distinct signatures after one, two, and three extension counts are respectively \(13,20,22\). Consequently the three-count map on the \(22\) classes is injective. The full \(22\)-row table, including every induced Frobenius orbit spectrum, appears in `tritangent_22_spectra.csv`, from which the product formula for the zeta function is immediately effective. The only collisions for the first two counts are \((1,7)\) versus \((3,5)\), with first-two values \((1,1)\), and \((1,1,6)\) versus \((2,3,3)\), with first-two values \((4,6)\); the third counts break both.

**4. Geometric realization of sharpness.** We give an explicit sufficient uniform field-size bound rather than assuming formal permutations are realized by smooth surfaces. Use the affine chart \([x:y:1]\) and let \(\mathbb A^{16}\) parametrize eight *ordered* points. Form a polynomial \(P\) that is the product of all \(56\) determinants testing collinearity of triples, all \(28\) determinants testing membership of six points on a conic, and all \(8\) determinants testing the existence of a cubic through all eight singular at a specified point. For the last condition, use the \(10\times10\) matrix of eight cubic evaluations and the two first partial derivatives at the specified point; Euler's relation shows that the omitted third derivative is redundant given the evaluation at that point, since the characteristic is not three. The degrees of the three kinds of determinants are at most \(3\), \(12\), and \(28\), so \(\deg P\le56\cdot3+28\cdot12+8\cdot28=728\). The open general-position locus is nonempty over an algebraic closure, so \(P\) is nonzero. Permuting the labels changes \(P\) by at most a sign, hence \(P^2\) is \(\mathfrak S_8\)-invariant and has degree at most \(1456\).

For any permutation \(\sigma\in\mathfrak S_8\), twist the eight-point affine space by its finite étale Frobenius descent datum. This twist is an \(\mathbb F_q\)-affine \(16\)-space: its factors are the affine Weil restrictions of \(\mathbb A^2\) along the cycles of \(\sigma\). The invariant polynomial \(P^2\) descends to a nonzero polynomial of total degree at most \(1456\) on this affine space (a linear change of coordinates over an algebraic closure suffices to verify nonvanishing and the degree bound). For \(q>1456\), the elementary polynomial zero bound for nonzero polynomials of degree less than \(q\) gives a rational point where the polynomial does not vanish. It corresponds to a reduced Frobenius-stable eight-point set with permutation type \(\sigma\), in general position. Applying this to \((1,7)\) and \((3,5)\) gives the geometric witnesses required to show that two extension counts are not universally sufficient.

## Verification

Run `python3 verify_tritangents.py` with a Python 3 interpreter and the standard library. The program constructs the \(120\) subsets without assuming the fixed-point formula, computes cycle decompositions for every partition and confirms the formula for every exponent up to each Frobenius order. It asserts \(22\) classes, signature counts \((13,20,22)\), the exact two remaining two-count collisions, and the sharp \((1,7)\)/\((3,5)\) example. It writes the \(22\)-row CSV; a failure of any assertion terminates the process. The finite enumeration verifies the only nontrivial classification computation. The infinite family and the field-size realizability come from the arguments above, not extrapolation from finite-field samples.

## Relationship to prior work

Kulkarni–Ren–Sayyary Namin–Sturmfels establish the degree-one del Pezzo/space-sextic relationship and the classical tritangent geometry, with a focus on real points. Celik–Kulkarni–Ren–Sayyary Namin, particularly Section 4.2 and Definition 4.4, explicitly prove the Bertini-pair correspondence and list all four types of sizes \(8+28+56+28\); their reconstruction is from equations and tritangent data, not from just three finite-extension counts. The MathRepo construction documents the same four multiplicity patterns. The later work on recovering plane curves from branch points studies other geometric reconstruction problems; none of the examined sources states the present three-extension arithmetic inversion table. Related finite-field results about small-field tritangents on other genus-four models or exceptional curves on one degree-one del Pezzo example do not imply the uniform \(22\)-class result. The finite permutation calculation is elementary once the geometric representation is known, so an unindexed earlier character computation is a residual novelty risk.

## Limitations

The theorem applies to the \(\mathfrak S_8\)-subfamily of degree-one del Pezzo surfaces obtained from eight Frobenius-stable blow-up points, not the unrestricted \(W(E_8)\) Frobenius forms. It recovers the splitting partition on the *chosen* blow-up set and the zero-dimensional tritangent zeta function, not the curve's Weil polynomial, the surface's isomorphism class, or an arbitrary del Pezzo marking. The realization bound \(q>1456\) is only sufficient and is not claimed optimal. The exhaustive computation classifies a finite permutation action, not the geometry or smoothness of any particular input surface. No independent mathematical audit has been performed.

## References

- R. Kulkarni, Y. Ren, M. Sayyary Namin, B. Sturmfels, *Real Space Sextics and their Tritangents*, preprint first publicly posted 2017-12-18, https://arxiv.org/abs/1712.06274.
- T. Ö. Celik, A. Kulkarni, Y. Ren, M. Sayyary Namin, *Tritangents and Their Space Sextics*, first publicly posted 2018-05-29, https://arxiv.org/abs/1805.11702, especially Definition 4.4 and Section 4.2.
- D. Agostini et al., *Recovery of Plane Curves from Branch Points*, preprint https://arxiv.org/abs/2205.11287; published version, https://link.springer.com/article/10.1007/s00454-023-00538-5.
- *Space Sextics from Blowing up 8 Points in the Plane*, MathRepo, Max Planck Institute for Mathematics in the Sciences, https://mathrepo.mis.mpg.de/spaceSexticCurves/tritangentsDelPezzo.html (especially `MakeMultiplicityMap`, `multmap0` through `multmap3`, and `AllTritangentsInP3`).
