# Four projective classes of tangent-filling cubic pencils over \(\mathbb F_3\)

## Finding

Let \(k=\mathbb F_3\). A *tangent-filling cubic pencil* is a two-dimensional vector subspace \(U\subset k[X,Y,Z]_3\) such that each of the four members of \(\mathbb P(U)(k)\) defines a geometrically smooth cubic and the tangent lines at its \(k\)-rational points together cover \(\mathbb P^2(k)\). Tangent coverage is required for each member separately. No smoothness or coverage condition is imposed on non-rational members.

There are exactly **22,464** such pencils, comprising **four free orbits** of size **5,616** under \(\operatorname{PGL}_3(k)\). No vector subspace of dimension at least three has all its rational projective members smooth and tangent-filling, so the sharp maximum projective dimension is **one**.

Each such pencil has a **geometrically reduced base scheme of degree nine**. The four orbit representatives are listed below. In monomial order
\[
M=(X^3,Y^3,Z^3,X^2Y,X^2Z,XY^2,Y^2Z,XZ^2,YZ^2,XYZ),
\]
write \(F_c=\sum_{i=0}^9 a_iM_i\), where \(a_i\) are the base-three digits of \(c\), read least significant first. Each generator pair \((c_1,c_2)\) defines \(U=\langle F_{c_1},F_{c_2}\rangle_k\).

| Generator codes | Four member codes | Sorted rational-point counts | Rational base points | Orbit size |
| --- | --- | --- | ---: | ---: |
| (345, 3753) | (345, 3753, 4098, 5421) | \((6,6,6,7)\) | 4 | 5616 |
| (345, 3757) | (345, 3757, 4102, 4168) | \((6,6,6,7)\) | 4 | 5616 |
| (345, 6649) | (345, 6649, 6985, 7060) | \((4,4,7,7)\) | 3 | 5616 |
| (346, 3756) | (346, 3756, 4102, 5419) | \((4,6,6,6)\) | 3 | 5616 |

The totals by member profile are \(11{,}232\), \(5{,}616\), and \(5{,}616\), respectively. The first two rows are inequivalent even though they have the same member and base counts. Trivial stabilizers of pencils do not imply trivial automorphism groups of individual members.

## Assumptions and scope

All forms and coordinate transformations are over \(k\). A projective cubic is counted once per scalar class by requiring the first nonzero coefficient in the displayed monomial order to be one. A pencil is an unparameterized two-dimensional subspace, not an ordered generator pair. Equivalence is plane projective equivalence, not abstract isomorphism of elliptic curves or pencils. There are \(13\) rational projective points, \((3^{10}-1)/2=29{,}524\) normalized nonzero cubic forms, and \((27-1)(27-3)(27-9)/2=5{,}616\) elements of \(\operatorname{PGL}_3(k)\). Geometric smoothness means nonsingularity over an algebraic closure of \(k\).

## Proof

**Tangent coverage.** Take the thirteen projective points and thirteen dual lines with first nonzero coordinate one. For each normalized form \(F\), evaluate \(F(P)\) and \(\nabla F(P)\) at every rational projective point. A zero of \(F\) with nonzero gradient contributes the line with that gradient as its coefficients. The union contains all thirteen points exactly when \(F\) passes the tangent-coverage test. Exhaustion gives \(3{,}744\) forms passing the test. The numbers with four, six and seven nonsingular rational points are \(936\), \(1{,}872\), and \(936\), respectively. The smoothness test below makes these the corresponding counts of all rational points.

**Pencil census and group action.** For distinct normalized forms \(F,G\) that pass the coverage test, the remaining members of their span are the normalizations of \(F+G\) and \(F-G\). Retain a pair if both of these also pass. Every retained projective line arises from six unordered pairs; sorting and deduplicating the four member codes yields \(22{,}464\) pencils. This enumerates all candidate pencils without using geometric smoothness. Swapping \(X,Y\), swapping \(Y,Z\), scaling \(X\) by \(-1\), and substituting \(X\mapsto X+Y\) generate \(\operatorname{PGL}_3(k)\): permutations, scalings and additions of multiples of distinct coordinates suffice by elimination. Apply the substitutions to all member forms, then normalize and sort. The orbit search gives exactly the four rows above, with each orbit of size \(5{,}616\), the order of the group. All stabilizers are therefore trivial. Evaluation on the thirteen points gives the point-count profiles in the table.

**Geometric smoothness and exhaustiveness.** The same substitutions put the individual coverage-passing forms into three orbits, with smallest codes \(345,346,3105\) and sizes \(936,936,1872\), respectively. The symbolic test checks the thirteen distinct codes appearing in the four pencil representatives. On each affine chart it substitutes the fixed coordinate equal to one into the form and its three homogeneous partial derivatives. Their ideal is the unit ideal over \(k\) in the two remaining variables. Thus there is no geometric singularity on any of the charts. Every coverage-passing form occurs in one of the candidate pencils, as checked by taking the union of the computed member codes; each is therefore projectively equivalent to a tested form. This establishes geometric smoothness and shows that the candidate census is exactly the required census.

**Maximal dimension.** Any qualifying net contains a qualifying pencil, so after a coordinate change it contains one of the four representative pencils. Fix generators \(F,G\) of this pencil. A third generator must be one of the \(3{,}740\) normalized tangent-coverage forms \(H\) outside the pencil. Exactly the nine new projective members are obtained by normalizing \(H+sF+tG\), \(s,t\in k\): each class outside the pencil has a unique representative with coefficient of \(H\) equal to one. Exhaustion checks that no candidate has all nine new members passing the coverage test, in any of the four classes. This also rules out higher-dimensional systems, which would contain a net. The existing pencils give sharpness.

**Base schemes.** Two distinct geometrically smooth plane cubics are geometrically irreducible, since different positive-degree components would meet and cause a singularity. They have no common component, so the base complete intersection has length nine by Bézout. For each representative pair, on each chart the ideal obtained from \(F,G\) and the three \(2\times2\) minors of their homogeneous gradient matrix is the unit ideal. Consequently the gradients are independent at each geometric base point. On a chart their restrictions to the free coordinates are still independent: by Euler's identity at a common zero, the partial derivative in the fixed coordinate is determined by those in the two free coordinates. The Jacobian criterion gives a transverse intersection and a geometrically reduced base, consisting of nine geometric points. Direct projective evaluation gives four, four, three and three rational base points, respectively. Both properties transport along the orbits.

## Verification

Use Python 3 and SymPy. Run the four scripts from a writable copy of the record's directory, with the portable `base_reduced.py` from this version alongside the other programs:

```sh
python3 enumerate_tf_pencils.py
python3 verify_tf_smooth.py
python3 check_nets.py
python3 base_reduced.py
```

The census script writes `tf_pencil_orbits.csv`. The smoothness and net scripts reuse the census. The base verifier is self-contained apart from SymPy: it decodes the four displayed generator pairs and fails if any of the twelve chart ideals is not the unit ideal. The base verifier does not itself enumerate pencils, compute smoothness, or count rational base points. The computations use exact arithmetic in characteristic three, including Gröbner basis computations for the geometric assertions, and do not approximate algebraic-closure checks by finite extension-field sampling.

## Relationship to prior work

Asgarli–Ghioca introduced tangent-filling and studied individual curves [1]. In particular, the census of \(3{,}744\) individual tangent-filling cubics in three orbits over \(\mathbb F_3\), including their smoothness and point counts, is already recorded in [4]. It is included here to support the pencil census, not as a new claim. The individual-curve orbit table does not classify four-member lines in the form space, the base schemes, or the net obstruction. The smooth-pencil existence work [2] does not impose tangent coverage. The blocking-pencil results [3] instead impose conditions on the rational point set, not on the union of rational tangent lines, and principally assume a rationally empty base. Each pencil here has three or four rational base points.

## Limitations

The result is restricted to rational members of ternary cubic systems over \(\mathbb F_3\). It does not classify their non-rational members, other degrees or fields, or abstract genus-one isomorphism. The proof of exhaustiveness uses finite arithmetic and exact Gröbner computations. Historical priority is not asserted beyond the compared results.

## References

1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, https://arxiv.org/abs/2302.13420.
2. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, https://arxiv.org/abs/2203.07169.
3. S. Asgarli, D. Ghioca, and C. H. Yip, *Proportion of blocking curves in a pencil*, arXiv:2301.06019, https://arxiv.org/abs/2301.06019.
4. *Tangent-filling plane cubics over \(\mathbb F_3\): three projective classes*, published finding `91eb1857066d` (2026-10-18), [finding and proof](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-tangent-filling-plane-cubics-over-mathbb-f-3-three-projective-cl--91eb1857066d/RESULT.md).
