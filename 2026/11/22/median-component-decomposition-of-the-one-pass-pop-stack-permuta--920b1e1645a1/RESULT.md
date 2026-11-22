# Median-component decomposition of the one-pass pop-stack permutation graph

## Finding
For each integer \(n\ge 1\), let \(\mathcal L_n\) be the set of permutations of \(\{1,\ldots,n\}\) sorted by one deterministic left-to-right pop-stack pass. Equivalently, \(\mathcal L_n=\operatorname{Av}_n(231,312)\), the *layered permutations*. Form a graph \(G_n\) on \(\mathcal L_n\) by joining two permutations when they differ by a transposition of entries at adjacent positions.

**Component theorem.** Represent a layered permutation uniquely by its composition of decreasing-layer lengths. The positions and lengths of all parts of size at least three are invariants of a connected component, and these invariants completely determine the component. If these fixed long parts leave intervening gap lengths \(\ell_0,\ldots,\ell_r\ge0\), then the corresponding component is canonically isomorphic to
\[
\Gamma_{\max(\ell_0-1,0)}\square\cdots\square\Gamma_{\max(\ell_r-1,0)},
\]
where \(\Gamma_d\) is the graph of binary strings of length \(d\) without adjacent ones, with edges for one-bit flips, and \(\Gamma_0\) is a single vertex. Every component is therefore a median graph; it has \(\prod_{i=0}^r F_{\ell_i+1}\) vertices and diameter \(\sum_{i=0}^r\max(\ell_i-1,0)\), where \(F_0=0,F_1=1\) are Fibonacci numbers.

Let \(C_n\) and \(I_n\) denote the numbers of connected components and isolated vertices of \(G_n\). With \(C_0=I_0=1\) for the empty object, the complete ordinary generating functions are
\[
\sum_{n\ge0} C_nz^n=\frac{1-z}{(1-z)^2-z^3},\qquad
\sum_{n\ge0} I_nz^n=\frac{1-z^2}{1-z-z^3-z^4}.
\]
For \(n\ge3\) the graph has precisely \((n+1)2^{n-4}\) edges (and has one edge at \(n=2\), none at \(n=1\)). For \(n\ge2\), its unique largest component has \(F_{n+1}\) vertices and diameter \(n-1\). In particular, the fraction of all \(2^{n-1}\) one-pass sortable permutations reachable from the identity tends to zero exponentially.

**Optimal routing.** For two layered permutations, decide whether they belong to the same component by comparing the long-layer positions and sizes. If yes, encode each size-two part as a one in the corresponding gap's dimer-start string, and each unused possible start as zero. The exact graph distance is the sum of Hamming distances between these strings. An optimal path first splits dimers present only in the source, then creates the dimers present only in the target. All of these operations are legal adjacent-entry swaps.

## Assumptions and scope
The pop-stack operator used here reverses every maximal contiguous decreasing run in one pass. A size-\(s\) decreasing layer uses the next \(s\) consecutive values in decreasing order; layers appear in increasing value order. Adjacent swaps act on positions, not arbitrary pairs of positions. All permutations are labelled by the values \(1,\ldots,n\). The empty-length convention is used only to express generating functions. No assertion is made about permutations needing two or more pop-stack passes, or about unrestricted transpositions.

## Proof
**1. The swap criterion.** The standard characterization of one-pass pop-stack sortable permutations is the unique direct-sum decomposition into decreasing layers; this is the composition encoding stated in [1]. The inversion graph on *values* of a layered permutation is a disjoint union of complete graphs, one for each consecutive-value layer, with no edges between distinct layers. Swapping two entries in adjacent positions changes the relative order of exactly those two values, hence toggles just one edge of this inversion graph. A disjoint union of complete graphs can remain such a graph after one edge toggle, with the complete-graph classes remaining consecutive intervals, only by deleting the unique edge of a two-element class or adding an edge between two adjacent singleton classes. Indeed, for removal from a class of size at least three, another member witnesses a two-edge induced path, not a disjoint union of cliques; for addition between classes, any third member of either class gives the same obstruction. Thus a legal swap is **exactly** \(2\leftrightarrow1+1\) in the layer composition, at an actual layer position.

**2. Components and metrics.** The criterion fixes every layer of length at least three, including its position. Between consecutive fixed layers (and at the ends), the remaining gap of length \(\ell\) is tiled by parts of sizes one or two. The possible length-two starts are \(\ell-1\) sites, and no two can be consecutive. Toggling one allowed start is precisely the legal adjacent swap. Thus each gap yields \(\Gamma_{\ell-1}\) for \(\ell\ge1\), or a point for \(\ell=0\). Every gap can reach its all-singletons tiling by deleting its dimers, so these are the complete components, and distinct frozen-layer signatures cannot be connected. The Cartesian product description follows because moves in disjoint gaps commute.

For any two nonadjacent-one bitstrings \(a,b\), first delete each one in \(a\setminus b\), then insert each one in \(b\setminus a\). All intermediate strings avoid adjacent ones, and the path length is their Hamming distance, also a lower bound because each move changes one coordinate. Hence the Cartesian-product metric is the sum of the Hamming distances. Two complementary alternating strings, both admissible, achieve Hamming distance \(d\) in \(\Gamma_d\), so its diameter is \(d\). Coordinatewise majority of any three nonadjacent-one strings also avoids adjacent ones: if it had adjacent ones, two of the three input strings would each support each site, forcing one input to contain both. Together with the Hamming geodesic this gives the unique median vertex (the coordinatewise majority), so every factor and product is median. The standard count of no-adjacent-one length-\(d\) strings is \(F_{d+2}\), yielding the stated component size.

**3. Component and isolate series.** Let \(A(z)=1/(1-z)\) encode the length of a gap, and \(B(z)=z^3/(1-z)\) encode a frozen long layer. The *signature* of a component is uniquely an initial gap, followed by any number of repetitions of a long layer and another gap, hence has generating function
\[
A(z)\sum_{r\ge0}(B(z)A(z))^r
=\frac{1-z}{(1-z)^2-z^3}.
\]
A factor \(\Gamma_{\max(\ell-1,0)}\) is a singleton exactly when \(\ell\in\{0,1\}\). Replacing \(A(z)\) by \(1+z\) gives the isolated-component series
\[
\frac{1+z}{1-z^3(1+z)/(1-z)}=\frac{1-z^2}{1-z-z^3-z^4}.
\]

**4. Edges and the largest component.** Count edges by their unique endpoint having a size-two layer, and fix that layer's first position. At either end there are \(2^{n-3}\) choices of the compositions on the remaining positions; at each of the \(n-3\) interior positions there are \(2^{n-4}\) choices. Thus, for \(n\ge3\),
\[
|E(G_n)|=2\cdot2^{n-3}+(n-3)2^{n-4}=(n+1)2^{n-4}.
\]
The signature with no frozen layers yields the Fibonacci cube \(\Gamma_{n-1}\), which has \(F_{n+1}\) vertices and diameter \(n-1\). Any other signature has at least one long layer, and total free gap length \(L<n\). The identity \(F_{a+b+1}=F_{a+1}F_{b+1}+F_aF_b\) for positive \(a,b\), with the zero-length cases immediate, gives \(\prod_iF_{\ell_i+1}\le F_{L+1}<F_{n+1}\). Thus this largest component is unique for \(n\ge2\). By Binet's formula \(F_{n+1}/2^{n-1}\) decays exponentially because the golden ratio is less than two.

## Verification
Run `python3 verify.py` from the directory containing this file. The script constructs the actual graph from the layer-derived permutations, checks its edges by **swapping actual adjacent entries**, independently enumerates all permutations and tests the pop-stack algorithm for \(n\le8\), checks every pairwise shortest distance for \(n\le8\), and verifies component and isolate enumerators, size formulas, edge counts, and largest components through \(n=12\). It also checks the rational generating-function recurrences through coefficient 120. The script reports `PASS` if and only if these finite checks succeed. The all-length results above follow from the written proof, not from the finite tests.

## Relationship to prior work
Pudwell and Smith [1] explicitly state that one-pass pop-stack sortable permutations are the layered class \(\operatorname{Av}(231,312)\) and identify this class with compositions. This **existing input characterization is not new**. Bauer and Copenhaver [2] study the number of pop-stack iterations necessary to sort arbitrary permutations; their operator agrees with the one here, but the adjacent-swap graph of the *already one-pass sortable* class is a different object. The new contribution here is the exact criterion for an edge *inside* that class, the complete component-product decomposition, optimal within-component metric and exact component/isolation enumerators. General Fibonacci-cube theory supplies properties of the factors but does not alone identify which such factors occur in this permutation graph. Related work on adjacent swaps in other permutation restrictions does not imply this decomposition without the specific layer-invariance lemma.

## Limitations
This is an exact statement only for one-pass pop-stack sortable permutations and **position-adjacent** transpositions. The originality conclusion is based on inspected relevant sources and searches, not an exhaustive priority guarantee: an earlier equivalent statement in the weak-order or permutation-class literature remains possible. Independent external mathematical validation has not been performed. Finite verification stops at the ranges explicitly stated above.

## References
[1] Lara Pudwell and Rebecca Smith, *Two-stack-sorting with pop stacks*, arXiv:1801.05005 (first public 2018-01-15), published in *Australasian Journal of Combinatorics* 74(1), 2019, 179–195. https://arxiv.org/abs/1801.05005 ; full text: https://faculty.valpo.edu/lpudwell/papers/popstacks.pdf .

[2] Morgan Bauer and Keith Copenhaver, *A new lower bound for deterministic pop-stack-sorting*, arXiv:2307.08188 (first public 2023-07-17). https://arxiv.org/abs/2307.08188 .

[3] Murray Elder and Yoong Kuan Goh, *\(k\)-Pop Stack Sortable Permutations and \(2\)-Avoidance*, *Electronic Journal of Combinatorics* 28(1), P1.54 (2021). https://doi.org/10.37236/9606 .
