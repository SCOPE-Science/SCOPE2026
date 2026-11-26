# Complete Frobenius spectra of Göpel kernels for Cayley-octad quartics

## Finding

Let \(k=\mathbb F_q\) have odd characteristic, let \(C/k\) be a smooth nonhyperelliptic genus-three curve, and suppose \(C\) has a Frobenius-stable regular Cayley octad \(\Omega\) of eight geometric points. Write \(\sigma\in S_8\) for the Frobenius permutation of this octad. Let \(\mathcal G\) be the finite étale set of maximal Weil-isotropic subgroups of \(J(C)[2]\), each of order eight. There are exactly 135 geometric members. Their **full Frobenius cycle profile** is determined by the partition of eight specifying \(\sigma\), as follows. The fixed-kernel column separates the two canonical sorts of Lagrangian subgroup.

| Octad Frobenius type | Göpel orbit profile | Rational kernels: matching + affine | Rational bitangents |
|---|---|---:|---:|
| \(8\) | \(1\,2^{5}\,4^{7}\,8^{12}\) | 1 + 0 = 1 | 0 |
| \(7,1\) | \(1^{2}\,7^{19}\) | 0 + 2 = 2 | 0 |
| \(6,2\) | \(1^{3}\,2^{3}\,3^{12}\,6^{15}\) | 1 + 2 = 3 | 1 |
| \(6,1^{2}\) | \(1\,2^{4}\,3^{2}\,6^{20}\) | 1 + 0 = 1 | 1 |
| \(5,3\) | \(15^{9}\) | 0 + 0 = 0 | 0 |
| \(5,2,1\) | \(5^{3}\,10^{12}\) | 0 + 0 = 0 | 1 |
| \(5,1^{3}\) | \(5^{27}\) | 0 + 0 = 0 | 3 |
| \(4^{2}\) | \(1^{11}\,2^{14}\,4^{24}\) | 5 + 6 = 11 | 0 |
| \(4,3,1\) | \(3\,6^{2}\,12^{10}\) | 0 + 0 = 0 | 0 |
| \(4,2^{2}\) | \(1^{3}\,2^{6}\,4^{30}\) | 3 + 0 = 3 | 2 |
| \(4,2,1^{2}\) | \(1^{3}\,2^{6}\,4^{30}\) | 1 + 2 = 3 | 2 |
| \(4,1^{4}\) | \(1^{3}\,2^{6}\,4^{30}\) | 3 + 0 = 3 | 6 |
| \(3^{2},2\) | \(1^{3}\,2^{3}\,3^{4}\,6^{19}\) | 3 + 0 = 3 | 1 |
| \(3^{2},1^{2}\) | \(1^{9}\,3^{42}\) | 3 + 6 = 9 | 1 |
| \(3,2^{2},1\) | \(3^{5}\,6^{20}\) | 0 + 0 = 0 | 2 |
| \(3,2,1^{3}\) | \(3^{5}\,6^{20}\) | 0 + 0 = 0 | 4 |
| \(3,1^{5}\) | \(3^{45}\) | 0 + 0 = 0 | 10 |
| \(2^{4}\) | \(1^{39}\,2^{48}\) | 25 + 14 = 39 | 4 |
| \(2^{3},1^{2}\) | \(1^{7}\,2^{64}\) | 7 + 0 = 7 | 4 |
| \(2^{2},1^{4}\) | \(1^{15}\,2^{60}\) | 9 + 6 = 15 | 8 |
| \(2,1^{6}\) | \(1^{15}\,2^{60}\) | 15 + 0 = 15 | 16 |
| \(1^{8}\) | \(1^{135}\) | 105 + 30 = 135 | 28 |

Consequently a rational \(2,2,2\)-isogeny kernel exists for all octad types except these seven partitions: \((5,3), (5,2,1), (5,1,1,1), (4,3,1), (3,2,2,1), (3,2,1,1,1), (3,1,1,1,1,1)\). For octad type \((8)\), exactly one rational kernel exists although no bitangent is individually rational; type \((7,1)\) has exactly two such kernels and again no rational bitangent. Conversely, type \((3,1,1,1,1,1)\) has ten rational bitangents but no rational kernel.

For each row \(c_d\) denotes the number of Göpel Frobenius cycles of length \(d\). The finite étale scheme of Göpel kernels consequently has zeta function \[Z(\mathcal G/k,T)=\prod_{d\ge1}(1-T^d)^{-c_d}.\] Its rational points after extension to \(\mathbb F_{q^n}\) are \(\sum_{d\mid n}d c_d\), for every integer \(n\ge1\).

## Assumptions and scope

The curve is a geometrically smooth plane quartic, the ground field is finite of characteristic different from two, and a **geometric regular Cayley octad stable as an unordered set under Frobenius** is specified. The octad need not consist of rational individual points. The 28 geometric odd theta characteristics/bitangents correspond to its two-element subsets. No assertion is made that all 22 permutation types occur for every given finite field. A Frobenius-stable maximal isotropic subgroup is a subgroup scheme defined over \(k\) because \(J(C)[2]\) is finite étale; it need not consist of eight rational points. Such a subgroup gives a polarized quotient isogeny of degree eight, but the quotient is not asserted to be a Jacobian.

## Proof

**(1) Symplectic model.** Classical Cayley-octad marking identifies the symplectic space of geometric two-torsion with \[V=\{S\subseteq\Omega: |S|\equiv0\pmod2\}/\langle\Omega\rangle.\] Addition is symmetric difference modulo complementation. Since even subsets form a 7-dimensional binary vector space and complementation divides by its one-dimensional radical, \(\dim_{\mathbb F_2}V=6\). The Weil pairing is the parity of intersection, \(\langle[S],[T]\rangle=|S\cap T|\bmod2\). The mapping is equivariant for permutations of the octad. This classical identification is a premise taken from the cited Cayley-octad and theta literature, not a new assertion about arbitrary unmarked quartics.

**(2) Two explicit kinds of maximal isotropic subgroup.** A perfect matching on the eight labels partitions them into four unordered pairs \(P_1,\ldots,P_4\). Their four classes in \(V\) satisfy \(\sum_i[P_i]=0\), are mutually orthogonal, and span a three-dimensional space; the resulting subgroup has four weight-two nonzero classes. Different matchings give different subgroups. Their number is \(8!/(2^4 4!)=105\).

Identify the eight labels with the eight points of an affine three-space over \(\mathbb F_2\). Each of its seven nonzero linear forms determines a four-element affine hyperplane, taken modulo complement. Their seven classes together with zero form a three-dimensional totally isotropic subgroup: the intersection of two distinct hyperplanes has two points, and symmetric difference of two hyperplane indicators equals a third indicator modulo complementation. Up to affine relabelling there are \(8!/|\operatorname{AGL}(3,2)|=40320/1344=30\) distinct affine structures, all giving different subgroups. None contains a weight-two element, so this family is disjoint from the 105 matching groups.

A six-dimensional symplectic vector space over \(\mathbb F_2\) has \((2+1)(4+1)(8+1)=135\) maximal isotropic three-subspaces. Therefore the two constructions exhaust **every** Göpel subgroup. The decomposition into 105 Pascal and 30 Fano configurations is classical; the arithmetic cycle table is the contribution considered here.

**(3) Frobenius orbit classification.** Permuting the eight labels permutes matchings and affine structures, hence permutes the complete 135-element set. Its conjugacy class in \(S_8\) is determined exactly by a partition of eight; there are 22 such partitions. For each row, use the canonical permutation whose disjoint cycles have the specified lengths, act on all 135 three-subspaces by permuting the underlying even subsets, and find the cycles. Each operation is an explicit finite permutation and therefore the counts hold for **every** curve satisfying the hypotheses, not just a sample of finite-field equations. The listed profile has weighted sum 135 in every row. The matching and affine fixed counts independently add to its number of singleton cycles. A separate bitangent count follows from the action of \(\sigma\) on the 28 unordered pairs of labels.

**(4) Arithmetic descent and zeta functions.** For a finite étale scheme over \(\mathbb F_q\), rational points are precisely geometric Frobenius-fixed points, and Frobenius cycles of length \(d\) are the closed points of degree \(d\). The displayed criterion, extension-field counts, and zeta factorization therefore follow. This does not assert that a curve exists for every partition over every field.

## Verification

Run `python3 verify_gopel135.py` with Python 3, no packages. The verifier uses independent exhaustive constructions: (i) all mutually orthogonal independent triples in \(V\) to recover 135 distinct subspaces; (ii) all 105 matchings and all 30 transported affine hyperplane systems, checking equality to the first set. It then enumerates each of the 22 conjugacy types, reconstructs the induced 135-point permutation, checks that its profile sums to 135, checks matching-plus-affine fixed counts, and counts individually fixed pairs of labels. It finishes with `GOPEL135_OCTAD_FROBENIUS_EXHAUSTIVE_OK`. The loops range over **all** elements of the relevant finite sets, so this constitutes an exhaustive finite proof of the arithmetic table in conjunction with the structural reduction above, not an extrapolation from example curves.

## Relationship to prior work

Ren–Sam–Schrader–Sturmfels, *The Universal Kummer Threefold* (arXiv:1208.1229, first public 2012-08-06), Section 6, gives the 135 Lagrangians and their 30 Fano/105 Pascal decomposition. It is the central antecedent: neither that geometric decomposition nor the number 135 is new. Kondō (2010), *Moduli of Plane Quartics, Göpel Invariants and Borcherds Products*, develops Göpel configurations and moduli. Elsenhans–Jahnel (arXiv:1710.07279) treats Galois actions on Cayley octads and bitangents, not the 22-case 135-kernel action. Bergvall (arXiv:2106.13072, later published 2023) treats cohomology and structures marked by Göpel subsets; its explicitly inspected Göpel section gives the 135 configurations, but not the complete finite-field Frobenius orbit table. Related arithmetic classifications of hyperelliptic genus-three two-torsion kernels concern a different Galois permutation representation. The present result is the entire cyclic Frobenius orbit portrait for this octad-marked genus-three case. The known geometric permutation representation logically makes the table computable; this claim is the checked explicit arithmetic classification, **not** an assertion that the group action itself was undiscovered.

## Limitations

The table is conditional on the existence of a Frobenius-stable regular Cayley octad. It does not show which cycle partitions are realized for a particular field size or classify all unmarked quartics. It counts \(k\)-defined subgroup schemes, not pointwise rational kernels, and does not claim that the polarized quotient is a Jacobian. The orbit structure arises through known classical geometry; historical priority of the numerical arithmetic table remains subject to unindexed tables or character computations. Independent external mathematical review has not been carried out.

## References

1. Q. Ren, S. V. Sam, G. Schrader, B. Sturmfels, *The Universal Kummer Threefold*, arXiv:1208.1229 (submitted 2012-08-06), Section 6; https://arxiv.org/abs/1208.1229.
2. S. Kondō, *Moduli of Plane Quartics, Göpel Invariants and Borcherds Products*, IMRN (published online 2010-09-22), https://doi.org/10.1093/imrn/rnq190.
3. A.-S. Elsenhans, J. Jahnel, *On plane quartics with a Galois invariant Cayley octad*, arXiv:1710.07279 (2017), https://arxiv.org/abs/1710.07279.
4. O. Bergvall, *Arithmetic and topology of classical structures associated to plane quartics*, arXiv:2106.13072 (2021), https://arxiv.org/abs/2106.13072.
