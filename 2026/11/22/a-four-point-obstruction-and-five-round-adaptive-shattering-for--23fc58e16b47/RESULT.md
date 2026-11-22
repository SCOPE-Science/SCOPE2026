# A four-point obstruction and five-round adaptive shattering for two-line symmetric differences in \(\operatorname{PG}(2,3)\)

## Finding
Let \(P\) be the thirteen rational points of \(\operatorname{PG}(2,\mathbb F_3)\), and let \(\mathcal L\) be its thirteen four-point projective lines. Consider the concept family
\[
\mathcal H=\{\ell\mathbin{\triangle}m:\ell,m\in\mathcal L,\ \ell\ne m\},
\]
with Boolean point-membership queries. Here \(\triangle\) denotes symmetric difference, and identical concepts are identified. There are exactly 78 concepts, each containing six points.

**Theorem.** A support \(S\subseteq P\) is VC-shattered by \(\mathcal H\) if and only if either \(|S|\le3\), or \(|S|=4\) and \(S\) is not a projective line. In particular its full shattered-support polynomial and dimensions are
\[
\Phi_{\mathcal H}(z)=\sum_{S\text{ shattered}}z^{|S|}=1+13z+78z^2+286z^3+702z^4,
\qquad \operatorname{VCdim}(\mathcal H)=4,
\qquad \operatorname{Ldim}(\mathcal H)=5.
\]
The shattered-support complex is pure of dimension three. Its 702 facets split into exactly two projective-collineation orbits: 468 four-sets with precisely three points on a line, and 234 four-arcs (no three collinear). Thus the natural line-pair parity concept class has a strict one-round adaptive advantage despite its pure finite shattering complex.

## Assumptions and scope
Everything is finite and exact. Points are one-dimensional subspaces of \(\mathbb F_3^3\); a projective line is the zero set of a nonzero linear form, with its form identified up to nonzero scalar. The concept associated with an unordered *distinct* line pair consists of the points on exactly one of those two lines. The empty two-line sum and all sums of three or more lines are excluded. Shattering means that \(\{C\cap S:C\in\mathcal H\}=2^S\). The Littlestone dimension is the maximum depth of a complete binary tree of point queries in which every root-to-leaf sequence of prescribed yes/no answers is realized by at least one fixed concept. Queries may depend on earlier answers; their repetitions cannot create a nontrivial split.

The theorem concerns only \(\operatorname{PG}(2,3)\) and its fixed two-line symmetric-difference family, not all projective-plane orders or the full binary linear span of line vectors. In particular, binary symmetric difference is *not* the same as the difference of incidence vectors over the field \(\mathbb F_3\).

## Proof
**1. Canonical incidence model.** Normalize every nonzero vector of \(\mathbb F_3^3\) by making its first nonzero coordinate equal to one and order the resulting thirteen triples lexicographically, indexed \(0,1,\ldots,12\). Use the same normalized triples as linear forms to order the thirteen lines. The resulting line point-index sets, from line zero to line twelve, are:

```text
(1,4,7,10) (0,4,5,6) (3,4,9,11) (2,4,8,12)
(0,1,2,3) (1,6,9,12) (1,5,8,11) (0,10,11,12)
(3,6,8,10) (2,5,9,10) (0,7,8,9) (2,6,7,11)
(3,5,7,12)
```
Every pair of distinct projective lines meets once, so its symmetric difference has \(3+3=6\) points. The thirteen line-incidence vectors over \(\mathbb F_2\) have exactly one nontrivial linear dependency, the sum of all thirteen [2, Lemma 1]. Thus equality between the symmetric differences of two distinct line pairs would yield an impossible nonzero dependency involving at most four distinct lines; consequently \(|\mathcal H|=\binom{13}{2}=78\). The reconstructed coordinate table independently confirms this.

**2. Complete static classification.** The projective linear group \(\operatorname{PGL}(3,3)\) acts on point supports and preserves the 78 concepts. Enumerating the \(3^9\) matrices over \(\mathbb F_3\), retaining exactly the invertible ones and dividing their common scalar action, gives 5616 distinct projective point permutations. Applied to four-sets, these have precisely three orbits:

| Representative point indices | Orbit size | Geometry | Shattered? |
|---|---:|---|---|
| \((0,1,2,3)\) | 13 | Entire line | No |
| \((0,1,2,4)\) | 468 | Exactly three collinear | Yes |
| \((1,2,4,5)\) | 234 | Four-arc | Yes |

A whole line cannot be a positive trace of any symmetric difference: if it is one of the two summand lines, exactly three of its four points remain; otherwise each summand intersects it in one point, so at most two of its points remain. For each of the other two representatives, `certificate.json` lists an unordered line pair for *each* of its sixteen binary traces, in ascending four-bit trace order. The verifier regenerates the lines from coordinates and checks all 32 witness relations, so both representative four-sets are shattered. Projective equivariance gives all 468+234=702 shattered four-sets.

Every support of at most three points extends to one of these two non-line four-sets: a collinear triple can be extended with a point off its line, and a noncollinear triple can be extended by any fourth point. Shattering is hereditary. Thus all 1, 13, 78 and 286 supports in cardinalities 0, 1, 2 and 3 respectively are shattered.

For five-sets the same exact projective action has precisely three orbits, of sizes 117, 702 and 468. Their point-index representatives are respectively \((0,1,2,3,4)\), \((0,1,2,4,5)\), and \((1,2,3,4,5)\). The first contains a whole line and is already ruled out. For the second, the all-positive five-point trace is absent. For the third, the trace whose positive points are \(\{1,2,3,4\}\) is absent. Each absence is verified by comparison with every one of the 78 concept masks, and the group action carries it to the whole corresponding orbit. There is therefore no shattered five-set. By heredity no larger shattered support exists. The orbit sizes total \(\binom{13}{4}=715\) and \(\binom{13}{5}=1287\), respectively, so no four- or five-set is omitted. This proves the polynomial, purity, and facet orbit counts.

**3. Adaptive dimension.** Each of the 78 hypotheses has six positive coordinates among thirteen. Projective pair transitivity or direct incidence counting shows that any point belongs to exactly 36 concepts, and any pair of distinct points belongs jointly to exactly 15 concepts. In a hypothetical complete depth-six query tree, the root-positive child has 36 hypotheses. A depth-five subtree there would need, at its next nontrivial query, at least 16 hypotheses on *both* outcomes; instead a distinct point splits the root-positive family into 15 positive and 21 negative hypotheses, and repeating the root yields an empty child. Thus depth six is impossible. For depth five, `certificate.json` supplies the 31 internal point-query indices in binary-heap order and a distinct unordered line pair at each of the 32 leaves, ordered left-to-right. A left edge encodes answer zero and a right edge answer one. The verifier walks all five edges of each path and checks the indicated concept against the query at every ancestor. These 32 explicit witnesses establish a complete depth-five tree. Hence \(\operatorname{Ldim}=5\).

## Verification
The package contains `certificate.json`, `verify_projective.py`, and an independently constructed `verify_cyclic.py`. Execute both scripts in the same directory using Python 3.10 or later, without external dependencies. The projective verifier reconstructs all thirteen points and lines from homogeneous coordinates, all 78 pair-sums, 8192 support traces, the 5616 projective permutations, the four- and five-support orbit partitions, the two complete 16-trace certificates, and every path in the depth-five tree. The second program constructs the *same abstract plane independently* using the cyclic \((13,4,1)\) difference set \(\{0,1,3,9\}\), enumerates all 8192 supports, and obtains the adaptive dimension via a separate recursive split test rather than using the provided tree. Both programs terminate with explicit PASS markers and otherwise fail by assertion. Exact count and hash checks for the embedded artifacts are recorded in the accompanying verification documentation.

## Relationship to prior work
The 2020 work of Benediktsson, Macpherson and Adler [1] studies VC dimension and density of graph-neighborhood set systems on Johnson and Hamming graphs; its concepts are graph neighborhoods rather than symmetric differences of projective lines. Balister, Bollobás, Füredi and Thompson [2] study minimum *weights* of symmetric differences of line collections, including a small-order numerical table and the fact that two distinct lines have symmetric difference of size \(2q\); those weight results do not determine pointwise Boolean traces, their complete face complex, or adaptive decision trees. De Boeck and Van de Voorde [3] study minimum-weight codewords in prime-power projective-plane incidence codes and their duals; the difference of line vectors appears in that context, but their objects and conclusions are coding weight bounds rather than VC/Littlestone shattering for this exact 78-concept family.

Indexed descriptions of a published classification of **two-line unions** in projective planes [4] and a classification of the order-three plane's **stopping sets** [5] were also checked. A union of two lines retains their common point, whereas the present symmetric difference deletes it; neither the reported five-support shattering count for unions nor the stopping-set polynomial implies the present four-support predicate, its two facet orbits, or the adaptive five-round tree. The quoted numerical overlap of 702 with an unrelated five-support count in [4] is not an implication between the results.

## Limitations
The group and trace enumerations are finite exact computations with accompanying complete standalone programs, not deductions for arbitrary field size. The structural upper bound on adaptive depth is analytic, but the depth-five lower bound is an explicit finite certificate. No claim about independence of mathematical audit, comprehensive priority across unindexed archives, or a general prime-power classification is made. The available indexed description of [4] could not be supplemented with its full published document; this is a residual priority risk, not affirmative evidence of novelty. The claim concerns a fixed geometry whose coordinate and cyclic incidence descriptions are independently reproducible.

## References
[1] B. G. Benediktsson, D. Macpherson, I. Adler, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first public 2020-07-31; Discrete Applied Mathematics 312 (2022), 29–44. https://arxiv.org/abs/2007.16042

[2] P. Balister, B. Bollobás, Z. Füredi, J. Thompson, *Minimal symmetric differences of lines in projective planes*, arXiv:1303.4117, first public 2013-03-17; Journal of Combinatorial Designs 22 (2014), 435–451. https://www.memphis.edu/msci/people/pbalistr/projectiveplane.pdf

[3] M. De Boeck, G. Van de Voorde, *Embedded antipodal planes and the minimum weight of the dual code of points and lines in projective planes of order* \(p^2\), arXiv:2203.16129, first public 2022-03-30. https://arxiv.org/abs/2203.16129

[4] *Finite-order exceptions and the shattering polynomial of two-line unions in projective planes*, published result indexed in 2026; https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-finite-order-exceptions-and-the-shattering-polynomial-of-two-lin--94f22e63c9c6

[5] *Complete stopping configurations and erasure-failure spectrum of the order-three projective plane*, published result indexed in 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-complete-stopping-configurations-and-erasure-failure-spectrum-of--fc9b95f1c3c6
