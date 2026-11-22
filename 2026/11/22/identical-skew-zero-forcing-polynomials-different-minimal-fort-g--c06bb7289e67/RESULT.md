# Identical skew-zero-forcing polynomials, different minimal-fort geometry for two strongly regular graphs

## Finding

The sixteen-vertex Shrikhande graph \(S\) and the \(4\times4\) rook graph \(R\) have the **same complete skew-zero-forcing polynomial**, despite having different induced configurations among their smallest skew forts:

\[
\begin{aligned}
\mathcal Z^{-}(S;z)=\mathcal Z^{-}(R;z)
={}&4032z^{10}+3648z^{11}+1760z^{12}\\
&+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\end{aligned}
\]

Thus each graph has skew-zero-forcing number \(10\), with precisely \(4032\) minimum skew-zero-forcing sets. **Each graph has exactly \(316\) inclusion-minimal skew forts:** \(60\) of order four and \(256\) of order six, and no other sizes.

The sixty smallest forts separate geometrically as follows (the type is the graph induced by the four white vertices):

| Induced four-vertex graph | Shrikhande \(S\) | Rook \(R\) |
|:--|--:|--:|
| Four isolated vertices, \(4K_1\) | 16 | 24 |
| Four-cycle, \(C_4\) | 12 | 36 |
| Triangle and isolated vertex, \(K_3\sqcup K_1\) | 32 | 0 |
| **Total** | **60** | **60** |

The polynomial equality therefore does not reflect identical families of minimal obstructions. In particular, one graph has thirty-two triangular four-forts, whereas the other has none.

## Assumptions and scope

All graphs are finite, simple and undirected. Both vertex sets are \(V=\mathbb Z_4\times\mathbb Z_4\), with vertices numbered \(4a+b\), where \(a,b\in\{0,1,2,3\}\). Distinct vertices \((a,b),(c,d)\) are adjacent in \(R\) exactly if \(a=c\) or \(b=d\). They are adjacent in \(S\) exactly if
\[
(c-a,d-b)\pmod 4\in\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}.
\]

The skew color-change rule is: any vertex, **whether initially blue or white**, with exactly one white neighbor can color that neighbor blue. Blue never returns to white. A set \(B\subseteq V\) is skew zero forcing if sequential legal moves can make all of \(V\) blue. Write
\[
\mathcal Z^{-}(G;z)=\sum_{B\text{ skew zero forcing}} z^{|B|}.
\]
A **skew fort** is a nonempty subset \(F\subseteq V\) for which every vertex of \(V\) has either zero or at least two neighbors in \(F\). A skew fort is *inclusion-minimal* if it contains no proper nonempty skew fort. These are not conventional forts for the rule where witnesses must themselves be blue.

## Proof

**Obstruction lemma.** A blue set \(B\) is not skew zero forcing if and only if \(V\setminus B\) contains a skew fort. Indeed, if the process cannot finish, at a terminal configuration the nonempty set \(F\) of remaining white vertices has no vertex with exactly one white neighbor, so is a skew fort. Conversely, if the original white set contains \(F\), no first vertex of \(F\) can be forced: before such a step the entire \(F\) remains white, and every candidate witness adjacent to that vertex has at least two neighbors in \(F\). This proves both implications and independence of the legal forcing order.

**Finite exhaustive certificate.** Label all sixteen vertices as specified. For every \(0\le w<2^{16}\), interpret the binary support of \(w\) as the white set \(W\). Compute \(d_W(v)=|N(v)\cap W|\). Determine whether \(W\ne\varnothing\) and \(d_W(v)\ne1\) for every \(v\), then inspect every strict submask \(U\subsetneq W\) for the same predicate to classify inclusion-minimal forts. Separately, starting from \(V\setminus W\), repeatedly color all white vertices that are the unique white neighbor of any vertex. Because the blue set grows strictly when a forcing step exists, this halts after at most sixteen rounds; all \(2^{16}\) white sets are tested for each graph.

For each blue cardinality \(b\in\{0,\ldots,16\}\), the computed number of successes is (for both graphs):

| \(b\) | 0–9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Count | 0 | 4032 | 3648 | 1760 | 560 | 120 | 16 | 1 |

The independent programs agree exactly on every coefficient, on all minimal-fort cardinality counts, and on the induced-degree counts of the 60 order-four forts. The Python checker further validates each of the 316 labeled minimal-fort masks per graph against the embedded certificate. The three possible degree multisets at order four are \((0,0,0,0)\), \((2,2,2,2)\), and \((0,2,2,2)\), respectively describing the displayed induced graphs. The enumerations thereby establish both the polynomial equality and the nonequivalence of the order-four obstruction geometries.

The independently checked strongly regular local statistics are degree six and exactly two common neighbors for each pair of distinct vertices, verifying that the two graph encodings have the expected parameters \((16,6,2,2)\). This is a finite theorem about these two explicitly labeled graphs, not an assertion about all strongly regular graphs.

## Verification

The artifact `checks/check_cpp.cpp` implements bitmask-based forcing, brute-force minimality over all forts, and a separate containment test of the obstruction lemma for all \(65{,}536\) possible initial white sets on each graph. Compile with `g++ -std=c++17 -O2 -Wall -Wextra checks/check_cpp.cpp -o check_cpp` and execute `./check_cpp`.

The artifact `checks/check_python.py` independently constructs the two graphs using Python sets, examines every cardinality layer using `itertools.combinations`, performs forcing without bit operations, and calculates inclusion-minimal forts in increasing size order. Run with `python3 checks/check_python.py` from a directory containing `data/` alongside `checks/`. It verifies every row of `data/FORCING_COUNTS.csv` and `data/MINIMAL_SKEW_FORTS.csv` against the recomputation, including all labeled minimal-fort masks and their induced-degree sequences. These two checkers use distinct enumeration strategies. Neither uses randomized sampling.

Both programs were run on the exact versions embedded with this result, and all assertions passed. The CSV tables encode 34 forcing-coefficient rows and 632 labeled minimum-obstruction rows, respectively. The certificates are finite, exhaustive and reproducible but do not constitute an independently reviewed publication.

## Relationship to prior work

The skew color-change rule and skew zero-forcing number are from the 2010 paper on minimum skew rank by the IMA–ISU research group, whose first verified public availability was 11 February 2010; its Section 3.1 allows a *white* vertex to force and thus differs decisively from ordinary zero forcing. The later paper on failed skew zero forcing develops obstruction concepts, but its inspected material does not contain the present two-graph classification. Abiad and collaborators' work on cospectral graphs with different zero-forcing numbers discusses this exact Shrikhande–rook pair under **positive-semidefinite** zero forcing; it does not yield the skew polynomial or the minimal skew-fort geometry here.

A previously recorded general rook-graph theorem on Grundy total domination already gives the **skew forcing number** \(Z^{-}(R)=10\) as a specialization; that numerical optimum is not claimed as new. It does not provide the complete polynomial or the Shrikhande comparison. An earlier ordinary zero-forcing census of these graphs gives different tenth- and eleventh-degree coefficients. As an independent control, the two programs here also reproduce those ordinary coefficients: for \(R\) they are \(3456,3504\), and for \(S\) they are \(3616,3600\). These *ordinary* results are not claimed as new and do not imply the present skew-forcing equality. Similarly, ordinary rook-graph fort classifications require a blue witness and are not classifications under the skew rule.

## Limitations

The result concerns only the two specified 16-vertex graphs. It does not assert equality of skew-zero-forcing polynomials for arbitrary cospectral or strongly regular graphs, and it does not classify the isomorphism types of the order-six minimal forts. The proof includes executable exhaustive checks rather than a closed-form symbolic derivation of every coefficient. The computed values are exact, but unpublished or unindexed historical computations could predate the finding; global historical priority is not certified. Independent scholarly validation has not been performed.

## References

1. IMA–ISU Research Group on Minimum Rank, *Minimum rank of skew-symmetric matrices described by a graph*, Linear Algebra and its Applications **432** (2010), 2457–2472, DOI: https://doi.org/10.1016/j.laa.2009.10.001. First public availability reported as 11 February 2010. Accessible full text: https://www.academia.edu/27468386/Minimum_rank_of_skew_symmetric_matrices_described_by_a_graph_.
2. Ansill, Jacob, Penzellna and Saavedra, *Failed skew zero forcing on a graph*, 2016, https://www.academia.edu/58516479/Failed_skew_zero_forcing_on_a_graph.
3. Abiad et al., *Constructions of cospectral graphs with different zero forcing numbers*, Electronic Journal of Linear Algebra, full text: https://journals.uwyo.edu/index.php/ela/article/download/6737/5787/11861.
4. *Failed Skew Zero Forcing Numbers of Path Powers and Circulant Graphs*, 2025, https://www.mdpi.com/2673-9909/5/2/32. Studied a different graph family.
