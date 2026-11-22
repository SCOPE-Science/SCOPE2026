# The dodecahedral maximal-independent-set shattering complex and its mod-two homology

## Finding
Let \(D=GP(10,2)\) be the twenty-vertex dodecahedral graph, and let \(\mathcal M(D)\) consist of all inclusion-maximal independent vertex sets, regarded as binary membership concepts on \(V(D)\). The simplicial complex \(\mathscr S(D)\) of VC-shattered vertex supports has the exact face polynomial
\[
\Phi_D(z)=\sum_{S\in\mathscr S(D)}z^{|S|}=1+20z+160z^2+660z^3+1470z^4+1572z^5+310z^6.
\]
Hence \(\operatorname{VCdim}(\mathcal M(D))=6\). Its facets have exactly three cardinalities: ten of size four, 672 of size five, and 310 of size six. The ten four-vertex facets are precisely the ten sets of four vertices with all six pairwise graph distances equal to three (the existence of these ten tetrahedra was previously known in a different topological context).

The reduced homology over \(\mathbb F_2\) is
\[
\dim_{\mathbb F_2}\widetilde H_j(\mathscr S(D);\mathbb F_2)=
\begin{cases}10&j=3,\\326&j=4,\\5&j=5,\\0&\text{otherwise}.\end{cases}
\]
Thus \(\mathscr S(D)\) is nonpure and has nonzero mod-two homology in three consecutive dimensions; it is not the ordinary independence complex of \(D\).

## Assumptions and scope
All graphs are finite and simple. Explicitly, let \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\) be vertices, with undirected edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). A concept is an independent set maximal by inclusion, not necessarily of maximum cardinality. A support \(S\subseteq V(D)\) is shattered if every subset \(T\subseteq S\) equals \(M\cap S\) for some \(M\in\mathcal M(D)\). The empty support is included. The homology statement is only over \(\mathbb F_2\), with standard simplicial augmentation; no integral torsion or homotopy-type conclusion is asserted.

## Proof
First, a shattered support is independent: if it contained adjacent vertices, the all-positive trace on those vertices could not occur in an independent-set concept. There is also an absolute cardinality bound. The exhaustive classification below gives exactly 295 concepts, while a shattered support of nine vertices would require at least 512 distinct concepts. Thus it suffices to check independent supports of sizes zero through eight.

Encode \(u_i\) by bit \(i\), and \(v_i\) by bit \(10+i\), for \(0\leq i\leq9\). For every mask \(s\) let \(I(s)\) be its independence indicator. The recurrence \(I(0)=1\) and, for any set bit \(b\) of nonzero \(s\),
\[
I(s)=I(s\setminus\{b\})\,\mathbf1\bigl[N(b)\cap(s\setminus\{b\})=\varnothing\bigr]
\]
examines **every** one of the \(2^{20}\) subsets and tests independence exactly. A nonempty or empty independent mask \(m\) is inclusion-maximal if and only if every outside vertex has a neighbor in \(m\). This yields 295 maximal independent sets, separated by sizes six, seven and eight into 10, 280 and 5 sets. The ordinary independence-set counts by sizes zero through eight are
\[
(1,20,160,660,1510,1912,1240,320,5).
\]
For an independent support \(s\), compute the exact set of traces \(\{m\cap s:m\in\mathcal M(D)\}\) as bit masks. The support is shattered exactly when this trace set has cardinality \(2^{|s|}\). Exhausting all independent support masks through size eight yields the face-count vector, indexed by support cardinality,
\[
(1,20,160,660,1470,1572,310,0,0).
\]
As shattering is downward-closed, a shattered support is maximal precisely when adding any one outside vertex fails shattering. Exhausting these single-vertex extensions gives the facet counts 10, 672 and 310, in cardinalities four, five and six, with no facets in any other size. Enumerating all 4-subsets, and calculating each pairwise graph distance by breadth-first search, gives exactly ten equidistant distance-three tetrahedra, whose masks agree **exactly** with the ten size-four facets. This proves the enumerative and geometric assertions.

For the homology calculation, take the augmented simplicial chain complex of the verified shattered supports over \(\mathbb F_2\), with the standard boundary given by the sum of all one-element deletions. Let \(F_k\) be the family of shattered supports of size \(k\), where \(F_0=\{\varnothing\}\). Form the exact binary boundary matrix from \(\mathbb F_2^{F_k}\) to \(\mathbb F_2^{F_{k-1}}\) by placing a one at \((\tau,\sigma)\) exactly when \(\tau=\sigma\setminus\{v\}\) for one vertex \(v\). Deterministic bitwise Gaussian elimination gives ranks, in order \(k=1,\ldots,6\),
\[
(1,19,141,519,941,305).
\]
The rank for the zero differential out of \(F_0\), and for degrees above six, is zero. Rank-nullity gives reduced Betti numbers by cardinality-indexed chain degree \(k\): \((0,0,0,0,10,326,5)\). A face of size \(k\) has simplicial dimension \(k-1\), giving the asserted degree-three, degree-four and degree-five homology ranks. The alternating face count \(1-20+160-660+1470-1572+310=-311\) agrees with \(10-326+5=-311\), providing an additional exact consistency check.

These finite calculations are proofs because both complete programs specify the graph and entire search spaces, enumerate all masks without sampling, construct every concept and every relevant face, compute exact trace sets, and perform exact finite-field elimination. The two implementations use different algorithms for identifying the concepts: a full independent-subset maximality test in C++ and Bron--Kerbosch maximal-clique search in the complement graph in Python. Every expected count and rank is asserted against an actual computed value, not inserted as a substitute for computation.

## Verification
Compile and run `verify_dodecahedron.cpp` with `g++ -O2 -std=c++17 verify_dodecahedron.cpp -o verify_dodecahedron && ./verify_dodecahedron`. Independently run `python3 verify_dodecahedron.py`; this script uses only the Python standard library. Both programs build the labeled graph from the displayed edge rule, enumerate all concepts and support traces, verify the face polynomial and facet counts, and independently compute all mod-two boundary ranks. The Python program additionally checks the ten distance-three tetrahedra. Both terminate with a `PASS` message; failure of an asserted invariant raises an error. No random seeds, hidden input data or external graph libraries are required.

## Relationship to prior work
Liu, Shangguan, Skokan and Xu (arXiv:2403.17910, first public 2024-03-26, especially Lemma 27) identify the maximal-independent-set membership hypergraph as a dual system and give a general VC-dimension bound using bipartite induced matchings. That bound supplies neither the dodecahedral shattered faces nor their homology. Benediktsson, Macpherson and Adler (arXiv:2007.16042, first public 2020-07-31) investigate open graph-neighborhood membership concepts for Hamming and Johnson graphs, not maximal independent sets of the dodecahedron.

Saleh, Titz Mite and Witzel (arXiv:2302.14388, first public 2023-02-28, Lemma 4.1) already exhibit the ten distance-three dodecahedral tetrahedra. **Their existence and count are not claimed as new.** The finding here is that precisely these ten tetrahedra are the exceptional size-four facets of the *maximal-independent-set shattering complex*. Published online results on the ordinary dodecahedral independence complex show a wedge of four five-spheres and count all its independent faces; that is a different simplicial complex with different face counts. A general published online result for maximal-independent-set shattering on graphs with attached private leaves concerns whiskered graphs; this dodecahedral graph has no private leaves, and the theorem does not supply the present count or homology.

## Limitations
The classification concerns only the indicated twenty-vertex graph and inclusion-maximal independent sets, not arbitrary cubic graphs or all generalized Petersen graphs. The topological conclusion is mod-two homology, not integral homology or a homotopy equivalence. The exact finite proof uses exhaustive computation with two independently written verifiers rather than a short case-free symbolic enumeration. The ten equidistant tetrahedra were known previously; any claim of novelty is confined to their shattering-facet role, the complete shattering polynomial, and the homology of this specific complex. Unindexed exact classifications could affect priority, and an external mathematical audit has not been performed.

## References
1. H. Liu, C. Shangguan, J. Skokan, Z. Xu, *Beyond chromatic threshold via the \((p,q)\)-theorem, and a sharp blow-up phenomenon*, arXiv:2403.17910, first public 2024-03-26; SoCG 2024. https://arxiv.org/abs/2403.17910
2. B. G. Benediktsson, D. Macpherson, I. Adler, *Vapnik--Chervonenkis dimension and density on Johnson and Hamming graphs*, arXiv:2007.16042, first public 2020-07-31. https://arxiv.org/abs/2007.16042
3. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris--Rips complexes of Platonic solids*, arXiv:2302.14388, first public 2023-02-28. https://arxiv.org/abs/2302.14388
4. D. D. D. Jin, D. G. L. Wang, *On the minimum vertex cover of generalized Petersen graphs*, 2019, DOI 10.1016/j.dam.2018.12.011; graph-theoretic independence questions, not support shattering. https://doi.org/10.1016/j.dam.2018.12.011
