# Component geometry and connected-fiber census for one-pass bubble-sort inverse images

## Finding
Let \(B\) be one left-to-right pass of adjacent compare-exchange bubble sort on permutations of \([n]\). For a possible output \(\sigma\), let \(G(\sigma)\) be the graph whose vertices are all permutations \(\pi\) with \(B(\pi)=\sigma\), adjacent when they differ by one transposition of *consecutive positions*.

The graph is empty unless \(\sigma_n=n\). For \(n\ge2\) and \(\sigma_n=n\), write \(1=r_1<\cdots<r_k=n\) for the positions of the left-to-right records in \(\sigma\), and put \(m=k-1\). Partition the index interval \(\{1,\ldots,m\}\) at each \(j\ge2\) for which \(r_j>r_{j-1}+1\). Let the successive positive block lengths be \(L_0,L_1,\ldots,L_s\).

Define \(E_L\) on all \(L\)-bit words, with an edge for flipping bit one freely or flipping bit \(j\ge2\) when bit \(j-1\) is zero, and set \(E_0=K_1\). Define \(H_L\), for \(L\ge1\), by the same rule but with its first bit never flippable. Then there is a natural graph isomorphism
\[
G(\sigma)\cong E_{L_0}\mathbin{\square}H_{L_1}\mathbin{\square}\cdots\mathbin{\square}H_{L_s},
\qquad H_L\cong\left(\bigsqcup_{h=0}^{L-1}E_h\right)\sqcup E_0.
\]
Here \(\square\) denotes Cartesian graph product and \(\sqcup\) disjoint union. Consequently, the number of components is exactly
\[
c(\sigma)=\prod_{i=1}^{s}(L_i+1),
\]
and every component size is obtained, with multiplicity, by choosing independently one of the \(L_i+1\) values \(2^{L_i-1},2^{L_i-2},\ldots,2,1,1\) for each \(i\ge1\), and multiplying their product by \(2^{L_0}\). Every nonempty fiber of length \(n\ge2\) has no isolated vertices.

The fiber is connected precisely when \(s=0\), equivalently when all its nonfinal record positions are the consecutive initial positions \(1,\ldots,k-1\). Among the \((n-1)!\) nonempty fibers of length \(n\ge2\), exactly
\[
C_n=(n-2)!\sum_{j=0}^{n-2}\frac{1}{j!}
\]
are connected. Thus the connected-fiber proportion is asymptotic to \(e/(n-1)\).

More precisely, if \(a\) is the number of indices \(j\in\{2,\ldots,m\}\) with \(r_j=r_{j-1}+1\), then \(G(\sigma)\) has \(2^{m-1}\) edges when \(m=1\), and \(2^{m-1}+a2^{m-2}\) edges when \(m\ge2\). The \(n=1\) case is a single-vertex graph.

## Assumptions and scope
The permutations are of distinct, named symbols \(1,\ldots,n\); \(B\) performs one full left-to-right pass, swapping an inverted neighboring pair at each comparison. Only the *source* permutations in a fixed exact inverse fiber are vertices. A graph edge must preserve that one-pass output after a single adjacent-position swap. The graph is simple and undirected. Component multiplicities and all formulae refer to labeled permutations, not permutation-pattern or rotation orbits.

The count \(C_n\) is a count of distinct **nonempty inverse fibers** (equivalently output permutations ending in \(n\)), not a count of components across all fibers. Empty inverse fibers are excluded from that count. The theorem uses the established record-subset parametrization of one-pass bubble-sort preimages, which is restated below for reproducibility.

## Proof
**Record-subset parametrization.** The one-pass sorting theorem of Bouvel, Cioni and Ferrari states that if \(\sigma_n=n\), its preimages correspond bijectively to subsets of its first \(k-1\) record values. Write \(\mu_j=\sigma_{r_j}\). For a chosen subset \(S=\{\mu_{i_1},\ldots,\mu_{i_t}\}\), form the unique decomposition
\[
\sigma=A_0\mu_{i_1}A_1\mu_{i_2}A_2\cdots\mu_{i_t}A_tn.
\]
The associated preimage is
\[
\pi=\mu_{i_1}A_0\mu_{i_2}A_1\cdots\mu_{i_t}A_{t-1}nA_t.
\]
The convention for an empty subset is \(\pi=nA_0\), where \(\sigma=A_0n\). In this correspondence, the records of \(\pi\) are exactly \(S\cup\{n\}\). Encode \(S\) by \(b\in\{0,1\}^m\), with \(b_j=0\) if \(\mu_j\in S\) and \(b_j=1\) otherwise. The right-to-left inverse algorithm chooses a swap at \(r_j\) precisely when \(b_j=1\), and makes compulsory swaps at nonrecord positions. This directly constructs every vertex without identifying distinct source permutations.

**Exact edge rule.** Swapping neighboring entries of any permutation changes the set of its left-to-right record *values* by at most one: record status after the swapped pair is unchanged because the prefix maximum after that pair is unchanged; within the pair only the smaller entry can change record status, and this occurs exactly when both entries exceed the preceding prefix maximum. Thus two adjacent, distinct preimages cannot have identical record subsets, since the parametrization has exactly one preimage for each subset. They must differ in a single bit \(b_j\).

Fix the values of all bits except \(b_j\), and let \(\nu\) be the first selected record to the right of \(\mu_j\), taking \(\nu=n\) when necessary. Let \(W\) be the consecutive subword of \(\sigma\) strictly between \(\mu_j\) and the previously selected record to its left; for \(j=1\), take \(W\) to be the prefix preceding \(\mu_1\), which is empty. Applying the displayed record-subset construction to the two choices for \(b_j\) shows that the two source permutations agree outside a local factor, where their respective factors are
\[
\mu_j W\nu\qquad\text{and}\qquad\nu W\mu_j.
\]
They differ by a single adjacent transposition if and only if \(W\) is empty. For \(j=1\) this is automatic. For \(j\ge2\), it means that \(\mu_{j-1}\) was selected (so \(b_{j-1}=0\)) and occupies the position immediately preceding \(\mu_j\) in \(\sigma\) (so \(r_j=r_{j-1}+1\)). Hence the complete bit-flip rule is
\[
\begin{aligned}
&b_1\text{ may always be toggled};\\
&b_j\text{ may be toggled for }2\le j\le m
\iff r_j=r_{j-1}+1\text{ and }b_{j-1}=0.
\end{aligned}
\]
There are no other edges. The conclusion also follows by tracing the compulsory and optional steps in the right-to-left preimage algorithm, and does not assume the inverse-fiber graph to be connected.

**Product factors.** Whenever \(r_j>r_{j-1}+1\), bit \(b_j\) is permanently frozen in the allowed-move graph. This splits the bit-index chain into exactly the specified blocks. Moves never involve coordinates from different blocks, and the frozen first bit of any later block does not consult a preceding block. The first block is \(E_{L_0}\); all remaining blocks are \(H_{L_i}\), proving the Cartesian product formula.

The graph \(E_L\) is connected for every \(L\ge0\): starting from any bit word, set the first bit to zero if necessary, then the second, and so on, always using a permitted flip. In \(H_L\), let \(t\) count the leading ones. If \(t<L\), the leading \(t\) ones and the following zero cannot change, and all \(L-t-1\) remaining bits form a connected \(E_{L-t-1}\). If \(t=L\), the all-ones word is an additional isolated component of \(H_L\). Thus \(H_L\) has components \(E_{L-1},E_{L-2},\ldots,E_0,E_0\). This proves the component multiplicities and cardinalities. As \(L_0\ge1\), the first bit can always be flipped and no vertex of the full fiber graph is isolated.

**Edges and global connected-fiber count.** For \(m\ge1\), the first bit contributes \(2^{m-1}\) undirected edges. Each other permitted bit index contributes \(2^{m-2}\), since exactly one half of the assignments to the preceding bit allows toggling it, and each edge is counted once. This yields the edge formula.

The graph is connected if and only if there are no frozen-index cuts. For a connected fiber with \(k\) records, the first \(k-1\) positions are increasing records and, if \(k<n\), the \((k-1)\)-st entry must be \(n-1\): otherwise the missing value \(n-1\) creates another record before the final \(n\). This characterization also holds at \(k=n\). Choose the first \(k-2\) increasing entries from \(1,\ldots,n-2\) and permute the remaining \(n-k\) entries before final \(n\). The number is
\[
\binom{n-2}{k-2}(n-k)!=\frac{(n-2)!}{(k-2)!},
\qquad 2\le k\le n.
\]
Summing over \(k\) gives \(C_n\). There are exactly \((n-1)!\) outputs ending in \(n\), so the connected fraction is \(\sum_{j=0}^{n-2}1/j!\) divided by \(n-1\), asymptotic to \(e/(n-1)\).

## Verification
Run `python3 verify.py` in a directory containing this document and the accompanying standalone `verify.py`. The code explicitly constructs the inverse bit masks, executes the ordinary compare-exchange pass, enumerates actual adjacent-swap edges, and independently breadth-first-searches every connected component. For each nonempty fiber of lengths one through eight it checks the edge predicate, exact edge count, full component-size multiset, vertex uniqueness and the connected-fiber formula. It additionally checks the connected-fiber count with exact integer arithmetic through length \(250\). The pass is finite diagnostic evidence; the all-length conclusions follow from the proof above, not from extrapolation of these checks.

For example, \(\sigma=(2,1,3,4,5)\) has three independent-component sizes \(4,2,2\), despite having eight preimages, illustrating that a power-of-two fiber cardinality does not imply connected adjacent-swap reconfiguration.

## Relationship to prior work
Bouvel, Cioni and Ferrari (2022), Theorem 2.2 and Corollary 2.3, establish the record-subset bijection and the number \(2^{k-1}\) of preimages, and study rooted trees obtained by *repeated complete bubble-sort passes*. The present theorem takes that parametrization as its input but studies the **induced adjacent-transposition graph within one fixed inverse fiber**, a different adjacency relation. It adds a position-gap-dependent exact edge rule, a complete Cartesian-factor/component classification and an all-size count of which output fibers remain connected. Their sorting-tree adjacency joins inputs to their outputs, not two inputs with equal output.

Xu and Zhou (2023) study generalized four-connectivity of the full bubble-sort Cayley graph on all permutations; that result is not an induced-fiber connectivity classification. General facilitated-hypercube descriptions help recognize the connected factors, but do not determine how the record gaps freeze coordinates in a bubble-sort inverse fiber. The result does not claim novelty for the elementary facilitated-bit graph by itself.

## Limitations
The classification concerns **one** left-to-right pass, permutations of distinct values, and swaps of consecutive positions only. It does not classify fibers of multiple passes, adjacent swaps allowing output changes en route, arbitrary-position transpositions, or sorting operators other than the specified one. Exhaustive tests through length eight do not certify an all-length statement; that is established by the independent record and block arguments. The literature comparisons cannot exclude every unindexed or differently formulated prior appearance. Independent validation has not been performed.

## References
1. M. Bouvel, L. Cioni and L. Ferrari, *Preimages under the bubblesort operator*, arXiv:2204.12936v1, first posted 2022-04-27, Theorem 2.2 and Corollary 2.3, https://arxiv.org/html/2204.12936v1 ; *Electronic Journal of Combinatorics* 29(4) (2022), P4.32, https://doi.org/10.37236/11390.
2. L. Xu and B. Zhou, *The generalized 4-connectivity of bubble-sort graphs*, arXiv:2303.13864v1, first posted 2023-03-24, https://arxiv.org/abs/2303.13864.
3. M. Albert, M. Atkinson, M. Bouvel, A. Claesson and M. Dukes, *On the inverse image of pattern classes under bubble sort*, *Journal of Combinatorics* 2(2) (2011), 231–243, https://pureportal.strath.ac.uk/en/publications/on-the-inverse-image-of-pattern-classes-under-bubble-sort/.
