# Nine eight-dimensional spheres in the Tutte–Coxeter independence complex

## Finding
Let \(G\) be the Tutte–Coxeter graph (the cubic girth-eight cage) in its 30-vertex duad–syntheme presentation. Its ordinary independence complex has integral homotopy type
\[
\operatorname{Ind}(G)\simeq\bigvee^{9}S^{8}.
\]
In particular, its only nonzero reduced integral homology is \(\widetilde H_8(\operatorname{Ind}(G);\mathbb Z)\cong\mathbb Z^9\). Its maximal face cardinality is fifteen, hence simplices reach dimension fourteen, although the entire complex reduces by discrete Morse theory to eight-dimensional spheres.

## Assumptions and scope
Let \(U=\{0,1,2,3,4,5\}\). A **duad** is a two-element subset of \(U\); a **syntheme** is a partition of \(U\) into three duads. There are fifteen of each. The vertices of \(G\) are the disjoint union of the fifteen duads and fifteen synthemes, with adjacency \(d\sim s\) exactly when \(d\in s\). Each vertex has degree three and there are forty-five edges. This is the classical Cremona–Richmond/Tutte–Coxeter graph [1]. The verifier also checks its girth is eight. For every vertex set \(\sigma\subseteq V(G)\), define \(\sigma\in\operatorname{Ind}(G)\) if no two distinct elements of \(\sigma\) are adjacent. The empty face is included for enumerative and augmented-chain checks; it is not a topological point. All statements are integral and concern precisely this finite graph.

## Proof
**Face construction.** Order duads lexicographically and synthemes by the lexicographic ordering of their ordered triples of duad indices. Label duads \(0,\ldots,14\) and synthemes \(15,\ldots,29\), respectively. Represent a face by its 30-bit membership mask. For a remaining vertex mask \(A\), branch on its least set bit \(v\): independent subsets either omit \(v\), or contain \(v\) and omit its closed neighborhood. This enumerates every independent face exactly once. The 16 face counts indexed by face cardinality, including the empty face, are
\[
(1,30,390,2890,13515,41736,86610,120690,
111225,66090,24948,6420,1370,240,30,2).
\]
Their sum is \(476187\). Independently, for each subset \(D\) of the fifteen duads, the synthemes free to be chosen are precisely those containing no duad from \(D\). If their number is \(f(D)\), then the number of independent faces of size \(k\) is
\[
\sum_{D\subseteq\binom{U}{2}}\binom{f(D)}{k-|D|},
\]
with out-of-range binomial coefficients interpreted as zero. The standalone verifier evaluates this separate formula for every cardinality and obtains the same vector.

**Complete discrete-Morse matching.** Start with all faces, including the empty face, as unmatched. For \(v=0,1,\ldots,29\), pair every still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both are still unmatched, then remove both from further stages. At each stage every face has at most one partner because the two paired faces differ exactly in membership of \(v\). The resulting matching has precisely \(238089\) pairs, and only nine unmatched faces, each with cardinality nine (dimension eight). One of the matched pairs is \((\varnothing,\{0\})\). Deleting this pair from the matching and then removing the empty face gives a matching of the ordinary nonempty face poset with exactly one critical vertex and nine critical eight-dimensional faces.

**Acyclicity and integral homotopy.** The verifier checks all \(3,461,430\) covering relations \(\tau\succ\sigma\) between augmented faces. Orient every unmatched Hasse edge downward and every matched Hasse edge upward. An exhaustive topological sort visits all \(476187\) nodes, so this directed graph is acyclic. Restricting to nonempty faces and removing the empty-to-vertex matched edge cannot create a directed cycle. Thus the ordinary matching is acyclic. Forman's discrete-Morse theorem yields a CW complex with precisely one zero-cell and nine eight-cells and no other cells. Every attaching map of an eight-cell lands in the single zero-cell, so the CW complex is the wedge of nine eight-spheres. This establishes the integral homotopy equivalence, not merely a field-homology calculation.

## Verification
The self-contained standard-library `verify.py` reconstructs the graph, independently counts faces by two algorithms, evaluates the complete matching, enumerates all covering relations, and checks the entire directed graph by Kahn topological sorting. Execute `python3 verify.py` from a directory containing the file. The recorded output `verification_output.txt` is included with this report. The checks independently confirm the reduced Euler characteristic nine. All computations are exhaustive for this finite 30-vertex complex; no bound on unspecified sizes, random experiment, or nonterminating search is used.

## Relationship to prior work
The Tutte–Coxeter graph is a classical highly symmetric girth-eight cage [1]. Barmak [2] proved general suspension properties for independence complexes of triangle-free graphs; they do not specify the homotopy type of this graph. Jonsson [3] proved a general suspension description for bipartite independence complexes. Tsukuda [4, Corollary 5.3] gives an equivalent hypergraph-Alexander-dual suspension description. Neither general result supplies the nine-sphere count or its dimension without a further nontrivial calculation. Published calculations on the same Tutte–Coxeter graph of intrinsic Čech and Vietoris–Rips complexes use different simplex definitions, and their results do not imply the ordinary independent-set homotopy type [5]. A published Coxeter-graph independence calculation concerns a different 28-vertex cubic graph [6]. This theorem asserts only the exact finite independence-complex homotopy type, not general structural results about all cages.

## Limitations
This classification is specific to the duad–syntheme graph. It does not classify independence complexes of other generalized quadrangles, larger cages, induced subgraphs, or equivariant representations. The method is exhaustive and machine-reproducible, but independent mathematical audit and definitive publication-priority confirmation remain outstanding. General suspension theorems remain relevant background, not a claim of novelty by themselves.

## References
[1] J. Baez, *Tutte–Coxeter Graph*, Visual Insight, American Mathematical Society, 2015-08-15, https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/ .

[2] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02, https://arxiv.org/pdf/1007.0418 .

[3] J. Jonsson, *On the Topology of Independence Complexes of Triangle-Free Graphs*, dated 2011-02-21, https://people.kth.se/~jakobj/doc/preprints/indbip.pdf , especially Theorem 3.1.

[4] S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46, https://cdm.ucalgary.ca/article/download/62277/46773/178118 , especially Corollaries 4.11 and 5.3.

[5] *Scale-four Čech nerve of the Tutte–Coxeter graph is a wedge of 144 two-spheres*, archived public mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-scale-four-ech-nerve-of-the-tutte-coxeter-graph-is-a-wedge-of-14--e305f9b746a4/RESULT.md .

[6] *The Coxeter graph independence complex is a wedge of seven six-spheres*, archived public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-coxeter-graph-independence-complex-is-bigvee-7-s-6--8a1bdfa47e09 .
