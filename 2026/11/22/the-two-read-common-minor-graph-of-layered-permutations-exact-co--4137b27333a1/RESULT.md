# The two-read common-minor graph of layered permutations: exact components and edges

## Finding

For every integer \(n\geq1\), let \(G_n\) have as vertices the layered permutations of size \(n\), and join two distinct vertices when their sets of standardized single-entry-deletion patterns share at least **two distinct** members. Writing a layered permutation as the ordered composition of the lengths of its decreasing layers, the following hold.

1. **Complete local edge characterization.** Every edge, uniquely, comes from replacing a consecutive block of parts in exactly one of the two forms
   \[
   (1,2^{[t]})\longleftrightarrow(2^{[t]},1),\qquad
   (1,2^{[t]},1)\longleftrightarrow 2^{[t+1]},\quad t\geq1,
   \]
   with identical composition prefixes and suffixes. Here \(2^{[t]}\) means exactly \(t\) consecutive parts equal to \(2\), **not** an integer power. Each adjacent pair has exactly two common distinct deletion outputs; no pair has more.

2. **Exact edges.** With \(e_n=|E(G_n)|\),
   \[
     \sum_{n\geq1}e_nz^n=\frac{z^3(1-z)}{(1-2z)^2},\qquad
     e_1=e_2=0,\quad e_3=1,\quad e_n=(n-1)2^{n-4}\ (n\geq4).
   \]

3. **Complete connected-component classification.** In any composition, keep all parts at least \(3\) in their original order, and let the intervening, possibly empty, maximal blocks of \(1\)- and \(2\)-parts have respective total weights \(m_0,\ldots,m_h\). The heavy parts and these weights are invariant in every connected component. Independently for each block, the property “contains a part equal to \(2\)” is also invariant. These data classify the connected components *exactly*. A block of weight \(m\) containing a \(2\) contributes \(F_{m+1}-1\) vertices to the component, while a block containing no \(2\) contributes one, where \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). Consequently the component size is the product of these factors over all blocks.

4. **Component and isolation enumeration.** Let \(c_n\) be the number of connected components and \(i_n\) the number of isolated vertices. Set \(c_0=i_0=1\) only as generating-function conventions. Then
   \[
     \sum_{n\geq0}c_nz^n=
     \frac{(1-z)(1+z^2)}{(1-z)^2-z^3(1+z^2)},
   \]
   \[
     \sum_{n\geq0}i_nz^n=
     \frac{(1-z)(1+z^2-z^3)}{(1-z)^2-z^3(1+z^2-z^3)}.
   \]
   For \(n=1,\ldots,11\), the component counts are \(1,2,3,5,10,19,35,64,117,215,396\), and isolated counts are \(1,2,2,4,9,16,28,49,88,160,288\).

## Assumptions and scope

A layered permutation is a direct sum of decreasing permutations. Its unique layer-size composition \(a=(a_1,\ldots,a_k)\), with positive integer parts summing to \(n\), identifies it bijectively with a composition of \(n\). A standardized deletion is formed by removing one entry of the permutation and renumbering the remaining entries in increasing order. Its induced operation on \(a\) lowers one part at least \(2\) by one, or removes one part equal to \(1\); repeated outputs are deduplicated. For \(n=1\), the empty permutation is allowed as the single deletion output, but two different vertices do not exist. The graph is simple and undirected; two distinct common minor *types*, not two deletion positions yielding identical minors, are required.

## Proof

**Binary encoding of the deletion channel.** Encode \(a\) by the length-\(n\) binary word
\[
 b(a)=0^{a_1-1}1\,0^{a_2-1}1\cdots0^{a_k-1}1.
\]
This is a bijection with length-\(n\) binary words ending in \(1\). Decreasing a part at least \(2\) deletes a \(0\). Removing a singleton part deletes a \(1\) that is either initially positioned or belongs to a noninitial consecutive run of at least two \(1\)'s. Conversely, every resulting word ending in \(1\) obtained by deletion of a \(0\), or of a \(1\) from the initial run or any run of length at least two, is an allowed composition minor. The two equivalent ways of deleting a member of a run of \(1\)'s give the same binary output, so the preceding statement concerns *sets* of outputs.

**Two-common-read criterion.** For two unequal ordinary binary words of equal length, at most two distinct length-one-deletion outputs coincide. Exactly two coincide if and only if they agree outside one nonempty alternating interval of length at least two, on which they carry opposite phases \(1010\cdots\) and \(0101\cdots\). This standard alignment lemma follows by taking the first and last unequal positions: the two distinct common outputs must align one word one place to the left and one place to the right within that interval, forcing period two and opposite phases. See Cai et al., Proposition 9, for the full statement and proof. In the present terminal-\(1\) encoding, the alternating interval cannot include the final bit.

Let the common prefix and suffix outside the first-to-last unequal interval be \(U,V\). There is always one ordinary common output obtained by deleting a \(0\) from each word; its deletions are permitted. For *both* ordinary common outputs to be permitted, the endpoint \(1\)-deletions must also be attainable. The first alternating \(1\) has no adjacent \(1\) on its right, so its deletion is permitted exactly when \(U\) is empty or ends in \(1\). The last alternating \(1\) has no adjacent \(1\) on its left, so its deletion is permitted exactly when \(V\) starts in \(1\). The last condition uses the possible equivalent deletion of a neighboring \(1\) in a run. Thus an edge occurs exactly when the alternating interval is preceded by a \(1\) (or starts the word) **and** is followed by a \(1\). Inspecting the two parities of its length, the binary-to-composition conversion gives exactly the two displayed local transformations. Conversely these transformations have both distinct common ordinary outputs as permitted composition minors. The first and last unequal positions are unique, so each edge has exactly one such representation.

**Edge generating function.** The generating function for arbitrary, including empty, composition prefixes or suffixes by total weight is
\[
 A(z)=\frac1{1-\sum_{j\geq1}z^j}=\frac{1-z}{1-2z}.
\]
Orient swap edges from a block \((1,2^{[t]})\), and consolidation edges from a block \((1,2^{[t]},1)\). Since the differing interval is unique, each edge is counted once by a marked block, with arbitrary common prefix and suffix. Hence
\[
 E(z)=A(z)^2\sum_{t\geq1}(z^{2t+1}+z^{2t+2})
 =A(z)^2\frac{z^3}{1-z}
 =\frac{z^3(1-z)}{(1-2z)^2}.
\]
Expansion proves the exact coefficients, including the short exceptions.

**Components.** Every local transformation modifies only \(1\)'s and \(2\)'s, leaving all parts at least \(3\) unchanged in order and preserving the weight of each intervening block. A block with no \(2\) admits no move, while a block containing a \(2\) cannot lose its last \(2\). It remains to show that all compositions of a fixed weight \(m\) using only \(1\)'s and \(2\)'s and containing a \(2\) are mutually connected. The \(t=1\) swap \((1,2)\leftrightarrow(2,1)\) allows all \(1\)'s to pass all \(2\)'s, putting any chosen \(2\) between two \(1\)'s when two are present. Then \((1,2,1)\leftrightarrow(2,2)\) eliminates two \(1\)'s. Iterate until no \(1\) remains (even \(m\)) or just one remains (odd \(m\)); swaps place the final \(1\) canonically. This joins every such block to the same canonical representative. The number of compositions of \(m\) with parts in \(\{1,2\}\) is \(F_{m+1}\), and exactly one uses no \(2\). Independent component factors now give the asserted product formula.

**Component counting.** A gap between heavier parts of total weight \(m\) has one possible component type for \(m=0,1\), and exactly two for \(m\geq2\): all \(1\)'s versus at least one \(2\). Thus its component-count series is
\[
 K(z)=1+z+2\sum_{m\geq2}z^m=\frac{1+z^2}{1-z}.
\]
The generating function for one heavy part, of size at least \(3\), is \(B(z)=z^3/(1-z)\). A composition is a gap followed by any number of (heavy part, gap) pairs, so \(C(z)=K(z)/(1-B(z)K(z))\), proving the first rational expression. A component is a singleton precisely when every gap is either all \(1\)'s or consists of exactly one \(2\); a gap of two or more \(2\)'s can consolidate backward to a block containing \(1\)'s and has component size greater than one. The isolated-gap series is \(J(z)=1/(1-z)+z^2\), giving \(I(z)=J(z)/(1-B(z)J(z))\). Algebra yields the second expression.

## Verification

Two standalone Python 3 checkers accompany this text. `check_direct.py` independently constructs the deletion-minor sets for all compositions with \(1\leq n\leq11\), compares every pair against the proposed local moves, confirms edge counts, and constructs all graph components to verify the invariant and Fibonacci size product. `check_binary.py` independently enumerates binary encodings and permissible deletions, verifies their correspondence with composition minors, and checks edge, component and isolation counts against rational generating functions for \(1\leq n\leq11\). Both passed when executed from the package's own exact files. These finite checks supplement, but do not replace, the all-length proof.

## Relationship to prior work

Raykova (2006) initiated the permutation-minor reconstruction setting, including the layered restriction. Vatter (arXiv:math/0610477, first posted October 16, 2006) formulated composition deletions and proved full-set reconstruction for \(n\geq3k+1\); this concerns an entire deck, not its pairwise two-output overlap graph. McNamara and Sagan (arXiv:1107.5070) analyze Möbius functions of generalized subword-order intervals, and McNamara and Steingrímsson (arXiv:1305.5569) analyze interval topology and rank-two interval populations; neither result directly counts or classifies the connected components of the same-rank graph defined here. Cai, Kiah, Nguyen and Yaakobi (arXiv:2001.01376, Proposition 9) supply the unrestricted one-bit-deletion alternating-interval criterion used in the proof, but the restricted admissibility filter and component analysis are additional. The edge coefficient sequence itself is already recorded in OEIS A001792 and A049610 under different combinatorial interpretations: **no priority claim is made for the numerical sequence alone**.

## Limitations

Novelty is qualified by the possibility of earlier unindexed equivalent work, especially work phrased as rank-level common-lower-cover graphs or matching-reconfiguration graphs. The result classifies connectivity and counts edges and isolated vertices, but does **not** determine individual optimal two-read codebook sizes (maximum independent sets) or claim a general theorem for arbitrary permutation classes. The full text of Raykova's paper was not materially inspected; its publisher abstract and date were checked. Independent expert validation has not been carried out.

## References

- M. Raykova, *Permutation Reconstruction from Minors*, Electronic Journal of Combinatorics 13 (2006), R66; first publication August 3, 2006. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v13i1r66
- V. Vatter, *Reconstructing compositions*, arXiv:math/0610477v1, October 16, 2006; Discrete Mathematics 308 (2008), 1524–1530. https://arxiv.org/pdf/math/0610477
- P. R. W. McNamara and B. E. Sagan, *The Möbius function of generalized subword order*, arXiv:1107.5070 (2011). https://arxiv.org/pdf/1107.5070
- P. R. W. McNamara and E. Steingrímsson, *On the topology of the permutation pattern poset*, arXiv:1305.5569 (2013). https://arxiv.org/pdf/1305.5569
- K. Cai, H. M. Kiah, T. T. Nguyen and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376 (2020), Proposition 9. https://arxiv.org/html/2001.01376v2
- OEIS A001792 and A049610 (existing integer sequences). https://oeis.org/A001792 ; https://oeis.org/A049610
