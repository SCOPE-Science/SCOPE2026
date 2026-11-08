# Twelve projective classes of smooth cubic pencils without rational base points over \(\mathbb F_2\)

## Finding

Let \(V=\mathbb F_2[X,Y,Z]_3\), and let \(\mathcal P\subset V\) be a two-dimensional vector subspace. Call \(\mathcal P\) a *rationally base-point-free smooth pencil* if each of its three nonzero forms defines a geometrically smooth plane cubic and the three cubics have no common point in \(\mathbb P^2(\mathbb F_2)\). The base-point condition is **only over the ground field**; every pencil of cubics has geometric base points over the algebraic closure.

**Theorem.** There are exactly \(2,016\) such pencils. Under \(\operatorname{PGL}_3(\mathbb F_2)\), they comprise exactly **twelve** projective-equivalence classes, all with trivial stabilizer and orbit size \(168\). Exactly \(672\) pencils have no blocking member, and exactly \(1,344\) have one blocking member (none has more than one). A blocking member is a cubic whose rational points meet every rational line.

A *smooth net* means a three-dimensional vector subspace of \(V\) with all seven nonzero cubics geometrically smooth. The exact numbers of pencils lying in \(0,1,2\) smooth nets are respectively \(504,840,672\). Thus **exactly 504 pencils, forming three free projective orbits, cannot be enlarged to a smooth net.**

Using the coefficient-mask convention below, complete orbit representatives and invariants are:

| Class | Three nonzero coefficient masks | Rational-point counts | Blocking members | Smooth-net extensions |
|---:|---|---|---:|---:|
| 1 | `7, 249, 254` | 1, 3, 3 | 1 | 1 |
| 2 | `7, 761, 766` | 2, 2, 3 | 1 | 1 |
| 3 | `15, 199, 200` | 1, 3, 3 | 0 | 1 |
| 4 | `15, 677, 682` | 2, 2, 3 | 0 | 2 |
| 5 | `15, 721, 734` | 2, 2, 3 | 0 | 0 |
| 6 | `15, 758, 761` | 2, 2, 3 | 0 | 0 |
| 7 | `31, 172, 179` | 1, 1, 5 | 1 | 2 |
| 8 | `31, 675, 700` | 1, 2, 4 | 1 | 2 |
| 9 | `31, 705, 734` | 1, 2, 4 | 1 | 2 |
| 10 | `31, 711, 728` | 1, 2, 4 | 1 | 1 |
| 11 | `31, 750, 753` | 1, 2, 4 | 1 | 0 |
| 12 | `31, 835, 860` | 1, 2, 4 | 1 | 1 |

Every class in the table has orbit size \(168\) and stabilizer order \(1\). The counts of blocking members and containing smooth nets are invariants of the entire pencil, not of a chosen generating pair.

## Assumptions and scope

The base field is \(\mathbb F_2\), and every smoothness assertion means smooth over \(\overline{\mathbb F}_2\). The vector space \(V\) has dimension \(10\). Its ordered monomial basis is \((X^3,Y^3,Z^3,X^2Y,X^2Z,XY^2,Y^2Z,XZ^2,YZ^2,XYZ)\). A positive integer mask \(m\) between \(1\) and \(1,023\) denotes \(F_m=\sum_{i=0}^9 ((m\operatorname{ div }2^i)\bmod2)M_i\), where \(M_i\) is the \(i\)-th monomial in the displayed order. In this characteristic a pencil \(\langle F_a,F_b\rangle\) has exactly three nonzero forms \(F_a,F_b,F_{a\oplus b}\), with \(\oplus\) bitwise exclusive-or.

The projective group acts on forms by invertible coordinate substitution. Since \(\mathbb F_2^\times=\{1\}\), no coefficient scalar quotient is needed. The rational projective plane has seven points and seven lines. A rationally base-point-free pencil's three rational point sets are disjoint and partition the seven points. No claim is made about pencils over larger fields, higher degrees, or geometric base-point freeness.

## Proof

**1. Smooth cubic test.** In characteristic two the Euler identity for any degree-three homogeneous form is \(F=X F_X+Y F_Y+Z F_Z\). Hence a geometrically singular point is exactly a nonzero common zero of the three partial derivatives over the algebraic closure. These derivatives are homogeneous quadrics. Their ideal has no projective zero over the algebraic closure precisely when the affine ideal is zero-dimensional; since the ideal is homogeneous and has the origin as a zero, a zero-dimensional affine zero set must consist only of the origin. The verifier computes exact Gröbner bases over \(\mathbb F_2\) for every one of the \(2^{10}-1=1,023\) nonzero cubics, obtaining exactly \(336\) geometrically smooth forms. An independent direct search of partial-derivative common zeros over \(\mathbb F_2,\mathbb F_4,\mathbb F_8,\mathbb F_{16}\) identifies exactly the same \(687\) nonsmooth forms; this latter finite-field search is a consistency check, not the proof of geometric smoothness.

**2. All pencils and rational base loci.** Each two-dimensional vector subspace is uniquely represented by its sorted triple \((a,b,c)\) of nonzero masks, satisfying \(a\oplus b=c\). There are exactly \(\left[{10\atop 2}\right]_2=((2^{10}-1)(2^{10}-2))/6=174,251\) such subspaces. Two complete enumerations (one first filtering to the smooth masks, the other starting with all \(174,251\) subspaces) agree that precisely \(5,544\) have all three members smooth and precisely \(2,016\) of those have no rational base point. The latter test evaluates the two generators at all seven rational points; its result is independent of which two of the three members are chosen.

**3. Projective orbits.** Every invertible three-by-three matrix over \(\mathbb F_2\) occurs uniquely among the \(7^3\) triples of nonzero binary row vectors having rank three. This gives \(|\operatorname{PGL}_3(\mathbb F_2)|=|\operatorname{GL}_3(\mathbb F_2)|=168\). Exact polynomial substitution expands each of the ten monomials and produces a linear action on masks. For the lexicographically smallest remaining pencil, computing its images under all 168 matrices and removing the orbit gives the twelve representatives shown. Each orbit has all 168 members; the twelve orbits are pairwise disjoint and exhaust all \(2,016\) pencils. Orbit-stabilizer gives trivial stabilizers.

**4. Incidence and extendability.** For each mask the verifier evaluates the cubic at all seven nonzero binary triples, obtaining its seven-bit rational-point set. The seven lines are the three-point sets defined by nonzero binary linear forms. Testing intersection with all lines gives exactly eight projective orbits with one blocking member and four with none, hence the counts \(1,344\) and \(672\). The reported rational-point profiles sum to seven for every pencil, as required by the base-point-free partition.

To test extension to a smooth net, for a pencil with nonzero members \(a,b,c\) the verifier enumerates masks \(v\notin\{0,a,b,c\}\) and requires \(v,v\oplus a,v\oplus b,v\oplus c\) all to be smooth. Every compatible three-dimensional net contributes exactly four such \(v\), so dividing the count by four gives exactly the number of containing smooth nets, without duplicate counting. Across all pencils, this gives multiplicities \(0,1,2\) in amounts \(504,840,672\). Applying the orbit calculation proves that the nonextendable pencils comprise precisely classes 5, 6, and 11 of the table. This completes the classification.

## Verification

Run `python verify_binary_smooth_pencils.py` with Python 3.10 or later and SymPy 1.12 or later. The script has no external data dependencies. It enumerates all nonzero forms, all two-dimensional subspaces, all projective transformations, rational incidence sets, and smooth-net extensions; it checks the full twelve-row certificate and ends with `BINARY_SMOOTH_BASEPOINTFREE_CUBIC_PENCILS_PASS`. All arithmetic is exact in characteristic two. The supplied source code is part of the proof specification and contains every needed normalization and expected count. Finite-extension singular-point tests are supplementary cross-checks; geometric smoothness is certified by the algebraic-closure ideal criterion.

## Relationship to prior work

Asgarli, Ghioca, and Yip [1] study the proportion of blocking members in pencils whose base loci contain no rational point; their partition observation and general bounds motivate the present finite exact classification, but do not enumerate smooth binary cubic pencil orbits or their possible extensions. Asgarli and Ghioca [2] investigate existence of all-smooth pencils; Asgarli, Ghioca, and Reichstein [3] construct larger all-smooth linear systems. Their existence statements do not imply an exhaustive orbit classification. The earlier complete classification of eight projective orbits of smooth *nets* over \(\mathbb F_2\) [4] concerns higher-dimensional systems: notably, the \(504\) nonextendable pencils here cannot appear as subpencils of such a net. Asgarli, Ghioca, and Yip [5] construct completely nonblocking pencils without requiring all members smooth; that existence theorem does not give these counts.

## Limitations

The classification is restricted to rational base-point freeness in the fixed space of cubic forms over \(\mathbb F_2\). Geometric base points do occur, by Bézout. The exact finite computation is described and reproducible, but it does not provide a uniform formula in other characteristics or higher degree. Possible equivalent older finite-geometry/elliptic-pencil tabulations remain a historical-priority risk. No independent mathematical audit or independent validation is asserted.

## References

[1] S. Asgarli, D. Ghioca, C. H. Yip, *Proportion of blocking curves in a pencil*, arXiv:2301.06019, first public 2023-01-15 (especially Question 1.1, Theorems 1.3--1.5, and Proposition 2.1).

[2] S. Asgarli, D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first public 2022-03-14.

[3] S. Asgarli, D. Ghioca, Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918, first public 2022-07-02.

[4] *Exact classification of smooth binary cubic nets*, prior mathematical record `92da2c65-3ae2-4c8d-9cef-f7e25d39f5bd`, concerning 864 nets in eight projective orbits.

[5] S. Asgarli, D. Ghioca, C. H. Yip, *Existence of pencils with nonblocking hypersurfaces*, arXiv:2301.09215, first public 2023-01-22.
