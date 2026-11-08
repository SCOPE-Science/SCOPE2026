# Cyclic-order orientation shattering: a universal three-query obstruction and the six-label complex

## Finding

Let \(X\) be a set of \(n\ge 3\) distinct labels. A hypothesis is an oriented cyclic total order on \(X\), modulo cyclic rotation, and each query is a three-element subset \(\{a,b,c\}\) with \(a<b<c\). Its answer is \(1\) precisely when the circular orientation of \((a,b,c)\) agrees with this increasing order; the reverse orientation gives \(0\). A query support is *shattered* if every bit assignment to its queries is realized by at least one cyclic total order.

**Universal three-query theorem.** For every \(n\ge3\), a family of exactly three distinct queries is shattered if and only if it is not a family of three of the four three-element subsets of a common four-element set. In particular, all two-query supports are shattered on their underlying labels.

**Complete six-label theorem.** On six labeled elements, the entire shattering polynomial is
\[
\Phi_6(z)=1+20z+190z^2+1080z^3+3420z^4+1680z^5+30z^6.
\]
Therefore \(\operatorname{VCdim}=6\). The inclusion-maximal shattered supports number \(840\) of size \(4\), \(1500\) of size \(5\), and \(30\) of size \(6\). The shattering complex is nonpure, with facets of three different dimensions. Under the full symmetric group on labels, these facets split into ten orbits: size-four orbit counts \(120,360,360\); size-five counts \(60,180,180,360,360,360\); and one size-six orbit of size \(30\).

## Assumptions and scope

All labels are distinct and every cyclic orientation is admissible. The label order only chooses one of two answers for each three-subset; changing that choice complements a coordinate and does not change shattering. No orientation reversal is identified: clockwise and counterclockwise orders are different hypotheses. There are exactly \((n-1)!\) such cyclic orders. The finite enumerative results beyond three-query supports are asserted only for \(n=6\), not for arbitrary \(n\). All counts are for query supports, not multisets, with a fixed labeled ground set. A facet is maximal under inclusion among shattered supports.

## Proof

**Restriction and extension.** For any collection of triple queries, let \(Y\subseteq X\) be the union of their labels. Restricting a cyclic order on \(X\) to \(Y\) leaves every answer unchanged. Conversely, any cyclic order on \(Y\) extends to one on \(X\) by inserting the unused labels in arbitrary positions. Hence the set of possible answer vectors depends only on the query labels, not on unused elements.

**Three-query classification.** Every family of three distinct triples involves at most nine labels. The finite proof therefore reduces to the case of exactly nine labels. The standalone verifier enumerates all \(8!=40320\) oriented cyclic orders on those nine labels. It constructs all \(\binom93=84\) binary query columns and explicitly examines every one of the \(\binom{84}{3}=95284\) three-query supports, testing the presence of all eight bit vectors. Exactly \(504\) supports fail. Independently, for each of the \(\binom94=126\) four-element subsets, its four three-element subsets give four distinct three-query supports. These are \(4\binom94=504\) different supports. None can be shattered: their answers depend only on the cyclic order of four labels, of which there are just \(3!=6<2^3\). The program compares the *actual sets* of failures and four-label triples, not merely their cardinalities, proving equality. The restriction-extension argument yields the theorem for all \(n\). For two-query supports, the union of the labels has size at most six. The exhaustive cases on three through six labels check all such pairs; restriction-extension proves the assertion for every larger ground set. For the one-query case \(n=3\), both circular orientations occur.

**Six-label census.** Fix the six labels \(\{0,1,2,3,4,5\}\), index their twenty three-element subsets lexicographically, and fix label zero at the start of each cyclic order. The resulting \(5!=120\) permutations enumerate every distinct hypothesis once. For any candidate query support \(S\), bit masks for the corresponding query columns are intersected iteratively to test whether all \(2^{|S|}\) answer fibers are nonempty. All candidate supports of sizes \(0\) through \(6\) are tested, a total of
\[
\sum_{k=0}^{6}\binom{20}{k}=60460
\]
sets. The accepted support counts in successive sizes are exactly \(1,20,190,1080,3420,1680,30\). No support of size seven can be shattered because such a support would require at least \(2^7=128\) different hypotheses and only \(120\) exist; downward closure excludes every larger support. This establishes the full polynomial and VC dimension.

**Facets and symmetry.** A face is a facet if and only if no one-coordinate extension is a shattered face. The program computes these one-coordinate extensions and finds the three stated facet counts. It enumerates all \(6!=720\) relabelings of triples, applies each relabeling to every facet support, and partitions the resulting facet sets into the ten stated orbits. It also gives an explicit size-six query support and one cyclic order for each of its \(64\) binary labelings; a separate calculation verifies those witnesses by direct orientation evaluation.

**Second concept-oracle construction.** For each four labels \(a<b<c<d\), the three-orientation indicators satisfy the additive relation
\[
\chi_{abc}+\chi_{acd}=\chi_{abd}+\chi_{bcd}.
\]
This is the binary-admitted-vector characterization of cyclic permutations in Abram--Chapelier-Laget--Reutenauer (Theorem 21, with a possible uniform bit-complement convention). The verifier *independently* enumerates every one of the \(2^{20}\) binary twenty-query vectors satisfying all fifteen such equations, obtains exactly \(120\), and compares the resulting set with the direct permutation construction. The face calculation, facet-orbit representatives, and explicit label witnesses are saved in the accompanying certificate.

## Verification

Run \(`python3 verify.py`\) from a directory containing the supplied `verify.py` and `certificates.json`. The verifier is Python standard-library-only; it checks the certificate against a fresh exhaustive recomputation. It prints:

`CIRCULAR_TRIPLE_SHATTER_PASS 95284_three_query_supports 504_quadruple_obstructions 120_cyclic_orders 120_cocycles 60460_six_label_supports 6421_faces 2370_facets 10_orbits 64_witnesses`

The 9-label calculation is exhaustive for three-coordinate supports by the proved nine-label reduction. The 6-label calculation is exhaustive for all shattering supports by the hypothesis-count bound. The two six-label concept enumerations use distinct constraints; both feed the same independently checked face certificate. All integer counts and orbits are reproducible from the supplied code and data.

## Relationship to prior work

Abram, Chapelier-Laget, and Reutenauer (2020 preprint, 2021 journal) give the crucial binary four-term characterization of circular permutations, here reused and credited. Their theorem already implies that these finite enumerations are possible, but the inspected work does not directly state the universal three-query forbidden-configuration result or the six-label face, facet and orbit numbers. Ayyer, Josuat-Vergès, and Ramassamy (2018 preprint, 2020 journal) count extensions of specialized consecutive partial cyclic-order constraints, not the complete Boolean-query shattering complex. Johnson and Wickes (2021 preprint) study how permutation *families* shatter label subsets under all induced linear permutations, a different predicate and quantifier order. Fiorini and Fishburn (2003) study extension obstructions of partial cyclic orders; only their abstract was accessible and this creates a material priority risk.

## Limitations

This is a finite classification of the six-label shattering complex plus a uniform three-coordinate theorem. It does not determine the VC or Littlestone dimensions for all larger ground sets, a complete higher-order obstruction theory, or arbitrary finite partial-order satisfiability. The 2003 cyclic-order extension paper could not be inspected in full. The universal three-query proof relies on the supplied exhaustive 9-label test, rather than a conceptual human-scale classification. Independent mathematical verification has not been performed.

## References

1. A. Abram, N. Chapelier-Laget, C. Reutenauer, *An Order on Circular Permutations*, arXiv:2010.06528 (2020, version 1 dated October 13); *Electronic Journal of Combinatorics* 28(3), P3.31 (2021), DOI:10.37236/9982, especially Theorem 21.
2. A. Ayyer, M. Josuat-Vergès, S. Ramassamy, *Extensions of Partial Cyclic Orders and Consecutive Coordinate Polytopes*, arXiv:1803.10351 (2018); *Annales Henri Lebesgue* 3 (2020), 275–297, DOI:10.5802/ahl.33.
3. C. Johnson, M. Wickes, *Shattering k-sets with Permutations*, arXiv:2112.01946 (2021).
4. S. Fiorini, P. C. Fishburn, *Extendability of Cyclic Orders*, *Order* 20 (2003), 151–171, DOI:10.1023/B:ORDE.0000009252.21331.22 (abstract consulted).
