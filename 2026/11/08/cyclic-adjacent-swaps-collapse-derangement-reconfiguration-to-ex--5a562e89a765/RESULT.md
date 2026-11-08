# Cyclic adjacent swaps collapse derangement reconfiguration to excedance components

## Finding
For every integer \(n\ge3\), let \(R_n\) be the graph of fixed-point-free permutations (derangements) of \([n]=\{1,\ldots,n\}\), with an edge when a single pair of entries in consecutive positions on the position cycle \(C_n\) is swapped and the resulting permutation is still fixed-point-free. Thus swaps of positions \(1,n\) are allowed, unlike the usual linear adjacent-transposition graph.

**Theorem.** Two derangements belong to the same connected component of \(R_n\) if and only if they have the same number of excedances \(\operatorname{exc}(\pi)=|\{i:\pi(i)>i\}|\). Every integer \(1\le k\le n-1\) occurs, and exactly \(n-1\) components exist. The component indexed by \(k\) has the classical derangement Eulerian number
\[
D(n,k)=\sum_{j=0}^{n}(-1)^j\binom{n}{j}A(n-j,k)
\]
vertices, where \(A(m,k)\) counts permutations of \([m]\) with \(k\) excedances, with \(A(0,0)=1\). Exactly two vertices are isolated, the left and right one-step rotations \((2,3,\ldots,n,1)\) and \((n,1,2,\ldots,n-1)\). Without the boundary-position swap, exactly \(2^{n-2}\) components occur; the new result identifies the precise collapse caused by adding just that one local generator.

## Assumptions and scope
Positions and values are labelled \(1,\ldots,n\) and must not be quotiented by rotation or dihedral symmetry. A derangement is a permutation \(\pi\) satisfying \(\pi(i)\ne i\) for all \(i\). The cyclic position adjacency is \(\{\{1,2\},\ldots,\{n-1,n\},\{n,1\}\}\). Legal swaps preserve the derangement condition at both endpoints. The excedance statistic is taken in the *linear* fixed labelling and not modulo \(n\). The formula for component size is a standard inclusion-exclusion count, not claimed to be a new enumeration in isolation. This theorem does not assert exact graph diameters or connectivity under different moves.

## Proof
Write \(p_{\pi}(v)=\pi^{-1}(v)\) for the position occupied by value \(v\), and define its early-position signature
\[
L(\pi)=\{v\in\{2,\ldots,n-1\}:p_{\pi}(v)<v\}.
\]
In any derangement, value \(1\) is late (position greater than one) and value \(n\) is early (position less than \(n\)). Hence
\[
\operatorname{exc}(\pi)=1+|L(\pi)|.
\]
A legal swap of positions \(j,j+1\), with \(1\le j<n\), never moves a value across its own position: such crossing would place it at its forbidden fixed point in one endpoint. Therefore every non-wrapping swap preserves the entire signature \(L\).

**Each signature sector is connected without wrapping.** Fix any subset \(L\subseteq\{2,\ldots,n-1\}\). Let \(E=L\cup\{n\}\) be the early values, and let \(T=[n]\setminus E\) be the late values. Define \(w_L\) to be the word listing the values in \(E\) in increasing order, followed by the values in \(T\) in increasing order. For \(v\in E\), its rank in the first block is less than \(v\); for \(v\in T\), its position is \(v+1+|\{a\in L:a>v\}|\), hence greater than \(v\). Thus \(w_L\) is a derangement with signature \(L\).

Starting from any word with signature \(L\), repeatedly move the smallest not-yet-placed early value leftward to its place in the initial block, using adjacent swaps. Every crossed unplaced early value is larger and remains to the left of its own index after moving right once. Every crossed late value must be smaller than the moving early value, so its rightward displacement leaves it late. Once the early block is sorted, sort the remaining late block ascending by repeatedly moving the smallest unplaced late value to its leftmost remaining position. Crossed late values move right; the moving value ends at its canonical position, strictly greater than its label. All intermediate permutations remain derangements. This gives an explicit legal path from any state of the sector to \(w_L\), proving connectedness of each fixed-\(L\) sector.

**The wrapping swap connects all signatures of fixed cardinality.** Write \(a=\pi(1)\) and \(b=\pi(n)\). Swapping first and last positions is legal exactly when \(a\ne n\) and \(b\ne1\). Necessarily, both \(a,b\) are internal values, with \(a\in L(\pi)\) and \(b\notin L(\pi)\). The new signature is
\[
L'=(L\setminus\{a\})\cup\{b\}.
\]
In particular \(|L'|=|L|\), so excedance count is invariant under *every* allowed swap. Conversely, when both \(L\) and its complement among internal values are nonempty, the canonical word \(w_L\) begins with \(a=\min L\) and ends with \(b=\max(\{2,\ldots,n-1\}\setminus L)\). Its boundary swap is legal and replaces \(a\) with \(b\). If \(L\) is not the set of the largest \(|L|\) internal values, then \(b>a\), and the sum of signature elements strictly increases. Repeating the corresponding signature-sector paths followed by boundary swaps reaches the unique largest-element signature of this cardinality. Reversibility proves that all derangements with the same excedance number are connected. Since every \(L\) has a canonical derangement \(w_L\), all \(n-1\) excedance counts occur.

**Counts and isolated states.** For a prescribed fixed-point set of size \(j\), delete its positions and corresponding values in increasing order. The resulting order-isomorphic permutation on \(n-j\) elements has exactly the same number of excedances. Inclusion-exclusion therefore gives the displayed \(D(n,k)\) formula. When \(L=\varnothing\), the late constraint forces the unique word \((n,1,2,\ldots,n-1)\); when \(L=\{2,\ldots,n-1\}\), the early constraint forces \((2,3,\ldots,n,1)\). Both have no permitted boundary swap and no other state with their signature, hence are isolated. In every intermediate sector, the canonical state has a boundary edge, and path-sector connectivity ensures no state is isolated. Thus precisely two isolated vertices occur.

The path-only statement is included to make the sharp contrast explicit: the signature sectors are individually connected, and every subset \(L\subseteq\{2,\ldots,n-1\}\) occurs, giving \(2^{n-2}\) components without the boundary generator. This finishes the proof.

## Verification
Two independently constructed exhaustive programs are supplied as `VERIFY_CYCLIC.py` and `VERIFY_CYCLIC_INDEPENDENT.cpp`. The Python program lists every derangement, constructs edges by direct legal cyclic swaps, and breadth-first-searches components for orders \(3\le n\le8\), also checking that each fixed-signature sector is connected under path swaps. The C++17 program independently enumerates permutations, constructs unions by cyclic transpositions, tests component constancy of excedance counts and precisely two isolated states through order \(9\). These finite checks support the all-order argument; they do not replace it. For example, at \(n=9\) there are \(133496\) configurations and eight connected components.

## Relationship to prior work
The classical derangement and Eulerian numbers are established enumerative objects, and Steingrímsson–Williams [1] studies excedance statistics; the present contribution concerns a new *configuration graph and its connectivity*, not the number of derangements itself. Albasini–Zagaglia Salvi [2] calls a permutation an 'adjacent cycle derangement' when each of its cycles contains consecutive integer labels. That is a condition on the cycles of a **single permutation**, not adjacency between permutations by swapping cyclically neighboring *positions*; its enumerative results do not determine our components. Clark [3] studies graph derangements and existence/cycle types, not swaps preserving fixed-point-freeness. Ganesan [4] considers Cayley graphs on *all* permutations generated by transpositions; restricting vertices to derangements invalidates any immediate Cayley connectivity conclusion. Assaf [5] uses 'cyclic derangements' for elements of wreath products, a different combinatorial object. The corresponding path-only reconfiguration has \(2^{n-2}\) sectors as proved above; that calculation alone does not establish the effect of the single wrap-around generator, which is determined here.

## Limitations
All results concern only this exact cyclic-position adjacent-swap model, not arbitrary transpositions, adjacent-value swaps, or quotients under rotation. The component-size formula is standard inclusion-exclusion. No new enumeration of Eulerian numbers, sharp component diameters, or general Markov mixing-time result is claimed. The historical-priority search cannot exclude unindexed equivalent work under permutahedral or affine-permutation terminology; independent scholarly evaluation is not performed.

## References
[1] E. Steingrímsson and L. K. Williams, *Permutation Tableaux and Permutation Patterns*, arXiv:math/0507149v1, 2005-07-07.
[2] L. de Francesco Albasini and N. Zagaglia Salvi, *On the Adjacent Cycle Derangements*, International Scholarly Research Notices (2012), doi:10.5402/2012/340357.
[3] P. L. Clark, *Graph Derangements*, arXiv:1306.6436v1, 2013-06-27.
[4] A. Ganesan, *Automorphism Group of the Complete Transposition Graph*, arXiv:1404.7363v1, 2014.
[5] S. H. Assaf, *Cyclic Derangements*, Electronic Journal of Combinatorics 17 (2010), #R163, doi:10.37236/435.
