# The fifteen rational-line/tritangent profiles of smooth cubic surfaces over \(\mathbb F_2\)

## Finding

For a geometrically smooth cubic surface \(S\) over \(\mathbb F_2\), let \(\ell(S)\) count rational lines on the surface. Let \(t(S)\) count rational tritangent planes: \(\mathbb F_2\)-rational planes \(H\) such that the cubic curve \(H\cap S\) is the union of three **distinct geometric lines**, possibly conjugate and not individually rational.

Among all \(2^{20}-1=1{,}048{,}575\) nonzero homogeneous cubic forms in four variables, exactly \(322{,}560\) define smooth surfaces. These form \(36\) projective-equivalence classes, and their complete joint \((\ell,t)\)-distribution is:

| \(\ell\) | \(t\) | Defining equations | Projective orbits |
|---:|---:|---:|---:|
| 0 | 0 | 64,512 | 4 |
| 0 | 1 | 59,640 | 7 |
| 0 | 3 | 11,200 | 2 |
| 0 | 9 | 840 | 1 |
| 1 | 0 | 23,520 | 2 |
| 1 | 1 | 75,600 | 6 |
| 1 | 2 | 15,120 | 2 |
| 1 | 3 | 420 | 1 |
| 2 | 0 | 40,320 | 2 |
| 3 | 0 | 1,120 | 1 |
| 3 | 4 | 16,800 | 3 |
| 3 | 7 | 420 | 1 |
| 5 | 3 | 11,340 | 2 |
| 9 | 6 | 1,680 | 1 |
| 15 | 15 | 28 | 1 |
| **Total** | | **322,560** | **36** |

The sharp possible number of rational tritangent planes is \(15\), attained by exactly \(28\) equations in one projective orbit; every rational plane is tritangent on that orbit. In particular, \(840\) equations in a single orbit have **no rational lines but nine rational tritangent planes**. This distinguishes rational tritangents from planes containing rational line triples and demonstrates that \(\ell\) alone does not determine \(t\).

## Assumptions and scope

The base field is \(k=\mathbb F_2\). A surface is geometrically smooth if its four partial derivatives have no common nonzero root in \(\overline{k}^4\). Nonzero homogeneous cubics are counted without division by change-of-coordinate orbits; there is no nontrivial coefficient scalar in \(k^\times\). The projective group \(\operatorname{PGL}_4(k)\) has order \(20{,}160\). An \(k\)-plane is **tritangent** precisely when its geometric section consists of three distinct lines, not necessarily with rational components. This avoids confusing tritangents with tangent planes at rational points.

Two explicit orbit witnesses (writing projective coordinates \(x_0,x_1,x_2,x_3\)) are:

\[
F_{15,15}=x_0^2x_3+x_0x_3^2+x_1^2x_2+x_1x_2^2,
\]

whose orbit has \(28\) equations, and

\[
F_{0,9}=x_0^2x_3+x_0x_3^2+x_1^3+x_1x_2^2+x_1x_2x_3+x_1x_3^2+x_2^3+x_2x_3^2+x_3^3,
\]

whose orbit has \(840\) equations. Their compact integer masks in the verifier's declared monomial ordering are `66880` and `67195`, respectively.

## Proof

**Exhaustion of the equations and coordinate orbits.** There are \(\binom{6}{3}=20\) cubic monomials. The verification code indexes them by the exponent quadruples \((a,b,c,3-a-b-c)\) in nested increasing-exponent order. It builds the action on all bit-mask polynomials by substitution with the variable swap, the four-cycle, and an elementary shear. Direct closure of the corresponding four-by-four matrices yields all \(20{,}160\) elements of \(\mathrm{GL}_4(k)\), hence their 141 computed orbits partition every one of the \(1{,}048{,}575\) nonzero equations. `orbits.csv` is a short orbit-size certificate; `verify.py` does not trust it, but regenerates and verifies every orbit and the complete disjoint union.

**Geometric smoothness.** For each orbit representative, compute all four partial derivatives of the homogeneous cubic. In each of the four standard affine charts, their ideal must have reduced Gröbner basis \(\{1\}\) over \(k\), by the weak Nullstellensatz over \(\overline k\). The verifier performs that exact calculation in SymPy over characteristic two, not just a rational-point test. This gives precisely 36 smooth orbits with total orbit weight \(322{,}560\).

**Exactly all rational tritangent sections.** A plane section of a smooth cubic surface that is a union of lines must be reduced: if a line \(L\) occurred with multiplicity two, its anticanonical degree \((-K_S)\cdot L=1\) would contradict \(L^2=-1\) and the fact that two distinct surface lines meet in at most one geometric point. (In the triple-line case the contradiction is even stronger.) Thus the three lines are distinct. A Frobenius-stable triple of geometric plane lines has one of only three cycle partitions: \(1+1+1\), \(1+2\), \(3\). Over \(\mathbb F_2\) there are exactly \(7\) rational plane lines, \(7\) pairs of nonrational lines of \(\mathbb F_4\)-degree two, and \(22\) Frobenius triples of \(\mathbb F_8\)-degree three. Consequently the complete set of ternary cubics with three distinct geometric line factors consists of exactly

\[
\binom{7}{3}+7\cdot7+22=35+49+22=106
\]

forms. The verifier constructs their coefficient masks from the products of conjugate linear forms using the explicit binary fields \(\mathbb F_4\) and \(\mathbb F_8\), and checks coefficient descent to \(\mathbb F_2\). Unique factorization ensures no double-counting among the three types.

**All sections.** There are exactly \(15\) rational hyperplanes in \(\mathbb P^3(k)\). For each, choose a basis of its three-dimensional vector subspace, substitute the basis variables into every smooth representative, and compare its ternary cubic mask with the 106 exact tritangent masks. Separately, test all \(35\) two-dimensional \(k\)-subspaces to count contained lines. Each representative's \((\ell,t)\) is invariant under \(\operatorname{PGL}_4(k)\); weighting by the certified orbit size proves the entire table. The claimed sharp bound follows because there are only 15 rational hyperplanes, and the unique size-28 orbit meets it.

## Verification

The standalone artifacts `verify.py` and `orbits.csv` are included. Run `python verify.py` with Python 3 and SymPy installed. The checker regenerates the order-20,160 linear group, independently exhausts the full nonzero cubic-form action, proves geometric smoothness via four-chart characteristic-two Gröbner bases, constructs the 106 reducible section forms from field arithmetic, tests every rational plane and line on each smooth orbit representative, and asserts each frequency and both extremal witnesses. The successful execution prints `BINARY_CUBIC_TRITANGENT_CENSUS_VERIFIED` and the full distributions. This is an exhaustive finite proof rather than a sample or a heuristic.

## Relationship to prior work

Dickson's projective classification of cubic surfaces over the binary field and Karaoğlu's 2021 complete F2 list with rational lines, points, Eckardt and double-point information provide the orbit-theoretic setting, not the arithmetic tritangent table. McKean's 2021 paper treats possible numbers of rational lines more generally. Brundu, Logar and Polli (2022 preprint) discuss all 45 geometric tritangent planes and automorphisms over an algebraically closed characteristic-zero field. The present table refines binary rational-line classification with Galois-stable tritangent plane sections (including irreducible cubic sections splitting as three conjugate lines); the 36 classes, 27 geometric lines, 45 geometric tritangents, and total smooth-form count are not claimed as discoveries.

## Limitations

The theorem is specific to the binary field and concerns rational hyperplane sections of smooth cubic surfaces, not an exact classification of tritangent orbit splitting over arbitrary extension fields. The frequency table counts equations, and the separate orbit column counts projective equivalence classes; it does not address non-linear abstract isomorphisms. The priority comparison covers identified primary works and mathematical-search records but cannot exclude every unindexed prior table. Independent mathematical audit has not been performed.

## References

- S. McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217 (first public 2021-01-20), https://arxiv.org/abs/2101.08217.
- F. Karaoğlu, *Nonsingular cubic surfaces over \(\mathbb F_{2^k}\)*, Turkish J. Math. **45** (2021), 2492–2510, DOI:10.3906/mat-2102-10, https://doi.org/10.3906/mat-2102-10.
- M. Brundu, A. Logar and F. Polli, *Construction of symmetric cubic surfaces*, arXiv:2207.04493 (2022 preprint), https://arxiv.org/abs/2207.04493.
