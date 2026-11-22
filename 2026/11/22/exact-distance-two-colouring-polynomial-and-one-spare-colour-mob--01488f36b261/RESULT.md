# Exact distance-two colouring polynomial and one-spare-colour mobility of the Heawood graph

## Finding

Let \(H\) be the point-line incidence (Heawood) graph of the Fano plane, and let \(X=H^2\) be its square: two distinct vertices of \(X\) are adjacent precisely when their distance in \(H\) is at most two. A proper \(k\)-colouring of \(X\) uses named colours from \(\{1,\ldots,k\}\); unused colours are allowed. Its exact chromatic polynomial is
\[
P_X(t)=(t)_{\underline 7}\sum_{r=0}^{7}m_r(t-7)_{\underline{7-r}},\qquad
(m_0,\ldots,m_7)=(1,28,294,1456,3514,3864,1596,144),
\]
where \((z)_{\underline a}=z(z-1)\cdots(z-a+1)\) for \(a\ge1\) and \((z)_{\underline0}=1\). In particular, \(\chi(X)=7\), and \(P_X(7)=725760\), \(P_X(8)=70156800\).

Let \(R_k(X)\) join any two named proper \(k\)-colourings differing at exactly one vertex. The graph \(R_7(X)\) consists of 725760 isolated vertices. The graph \(R_8(X)\) has 70156800 vertices and exactly 298045440 edges, with the following complete degree structure:

* 5806080 colourings using exactly seven colours, each of degree 14;
* 64350720 colourings using all eight colours, each of degree 8;
* among the eight-used states, 40642560 have exactly two neighbours using seven colours, and 23708160 have none.

Consequently the count of edges between seven-used and eight-used configurations is 81285120, and the count entirely among eight-used configurations is 216760320. The eight-colour graph is connected; **this connectivity already follows from Merkel's 2021 theorem for three-independent-vertex-free graphs** and is not asserted to be a new general phenomenon. The distinct contribution claimed here is the precise chromatic polynomial and the complete named-state, degree, and transition-type census for this particular distance-two colouring problem.

## Assumptions and scope

All graphs are finite and simple. Model the Fano plane by points \(p_i\), lines \(\ell_j\), and incidence \(p_i\in\ell_j\) exactly when \(i-j\pmod 7\in\{0,1,3\}\). Each point is on three lines; every two points share exactly one line, dually every two lines meet in exactly one point. A legal distance-two colouring assigns different colours to every pair at distance at most two in the original incidence graph. Recolouring changes the colour at one vertex while retaining this condition. Exact numbers concern these fourteen labelled geometric vertices and named colour palettes; they are not counts modulo symmetry.

## Proof

**1. Two-clique structure.** Any two different points of \(H\) are at distance two, as are any two different lines. A point and line are at distance one when incident and distance three when nonincident. Therefore \(X\) is the union of two seven-vertex cliques, joined across shores at precisely the incident pairs. A colour can occur no more than once on either shore; it may be shared across shores if and only if the associated point-line pair is nonincident.

**2. Matching interpretation and chromatic polynomial.** Let \(B\) be the bipartite graph with the seven points and seven lines as shores, joining exactly nonincident point-line pairs (degree four). Every proper colouring is uniquely specified by seven distinct point colours, a size-\(r\) matching of \(B\) identifying which \(r\) lines reuse which point colours, and \(7-r\) injectively assigned colours not appearing on the point shore. The exact number is thus \((t)_{\underline7}\sum_r m_r(t-7)_{\underline{7-r}}\), where \(m_r\) counts \(r\)-edge matchings of \(B\).

For full reproducibility, number the lines \(\ell_0,\ldots,\ell_6\), and let \(D_j(S)\) count matchings using only the first \(j\) lines with set of occupied point indices exactly \(S\subseteq\{0,\ldots,6\}\). Initialize \(D_0(\varnothing)=1\), all other entries zero. For each \(j=0,\ldots,6\), propagate \(D_j(S)\) to \(D_{j+1}(S)\) (line unused) and to \(D_{j+1}(S\cup\{p\})\) once for every \(p\notin S\) not incident with \(\ell_j\). Finally \(m_r=\sum_{|S|=r}D_7(S)\). This is an exhaustive integer recurrence on 128 subsets at each of seven steps. Evaluation gives exactly \((1,28,294,1456,3514,3864,1596,144)\), independently recovered in two different geometric realizations by the attached programs. The clique bound gives \(\chi(X)\ge7\), and \(m_7=144>0\) yields seven-colourings, proving equality. At seven colours all 14 vertices are in seven two-vertex classes, so \(P_X(7)=m_7 7!=725760\). At eight colours there can only be seven or six repeated classes; hence \(P_X(8)=8!(m_7+m_6)=70156800\).

**3. Local moves.** With seven named colours, every vertex on either seven-clique already sees all other six colours on its own shore. No vertex can change colour, so \(R_7(X)\) has no edges. For eight named colours, a seven-used state consists of seven shared nonincident point-line pairs and one unused colour. Every vertex may change to the unused colour and no other move is possible: its degree is 14. There are \(8!m_7=5806080\) such states.

For an eight-used state, exactly six pairs share colours. One point \(p\) has a colour unique to the point shore, and one line \(\ell\) has a colour unique to the line shore. On either shore, recolouring a vertex can only use the unique colour missing on that shore. The new colour is present at the opposite-shore singleton, so the move is legal precisely when the recoloured vertex is nonincident with that singleton. Each point has four nonincident lines, and dually; there are exactly four legal recolourings on each shore, a total of eight. Thus the \(8!m_6=64350720\) eight-used states have degree eight.

Exactly two of these eight moves decrease the number of used colours from eight to seven if the singleton point and singleton line are nonincident; if they are incident, none do. A size-six nonincidence matching extends to a perfect matching exactly when its unmatched point and unmatched line are nonincident. Deleting one of seven edges from any of the \(m_7=144\) perfect matchings bijects with an extendible size-six matching, so precisely \(7m_7=1008\) of the 1596 six-matchings are extendible and 588 are not. Multiplying by \(8!\) proves the two transition subclasses: 40642560 and 23708160. The seven-used-to-eight-used edge count is \(8!m_7\cdot14=81285120\). The remaining edges are \((8!m_6\cdot8-81285120)/2=216760320\). Combining the two categories proves the asserted total edge count.

**4. Connectivity and its provenance.** The graph \(X\) is co-bipartite, hence contains no independent triple. Since \(\chi(X)=7\), Merkel's 2021 Theorem 2 implies \(R_8(X)\) is connected. This implication is **prior knowledge**, not an independent originality claim. As a supplementary explicit finite check, fix the seven point-colours and normalize named eight-colourings; there are \(m_7+m_6=1740\) canonical states. Each legal point recolouring is followed by a corresponding canonical global colour permutation, while line recolourings remain literal. Both independent programs construct this 1740-state projected graph and check connectedness by breadth-first search. In any seven-used colouring, recolour a point of a shared point-line colour class to the unused colour, then its (nonincident) matching line to the unused colour; this legally swaps the two colour names globally. Such swaps generate every name permutation, so the canonical connectedness also lifts to the full named-colouring graph. Only the finite census is new; connectivity is separately implied by the published theorem.

## Verification

The standalone `verify_cyclic.py` encodes the seven cyclic triples \(\{j,j+1,j+3\}\), computes the matching recurrence, enumerates the 1740 canonical eight-colour states, validates their legal one-vertex transitions, checks reciprocity, degree and cross-stratum distributions, and tests connectivity. Run with `python3 verify_cyclic.py`.

The independent `verify_binary.cpp` instead builds the Fano plane using the seven nonzero vectors and normals of \(\mathbb F_2^3\), with incidence determined by zero dot product. It independently implements the 128-state matching DP and all canonical colour-change checks. Compile with `g++ -std=c++17 -O2 verify_binary.cpp -o verify_binary` and run `./verify_binary`. Both produce the asserted integers. The certificate enumerates 1740 normalized states, **not** all 70156800 named states; the symmetry-lift argument and published mixing theorem handle named connectedness without pretending that all 70 million states were enumerated.

## Relationship to prior work

Johnson, Kratsch, Kratsch, Patel and Paulusma (2014 preprint) formulate shortest-path graph-colouring reconfiguration, but their general complexity theorems do not enumerate the square of the Heawood graph. Bonsma and Paulusma (2015 preprint) develop contracted solution graphs, not the present numerical invariant. Merkel (2021) proves all seven-colourable graphs with no independent triple have connected eight-colouring reconfiguration graphs; **this subsumes the present connectivity conclusion** but does not specify these state counts, degrees, polynomial or transition strata. Banerjee, Engels and Hoang (2024 preprint; later revised) study general distance-colouring reconfiguration, and their inspected abstract, introductory definitions and relevant results do not list the Heawood-square counts. The standard matching interpretation for colouring a two-clique graph is not claimed as new; the exact Fano-specific matching coefficients and ensuing full palette-transition census are the claim.

## Limitations

This is an exact finite result on one canonical incidence graph, not a general theorem about projective planes of arbitrary order. It gives neither the exact diameter nor mixing time of the eight-colour reconfiguration graph. Its originality rests on best-knowledge comparisons with accessible primary literature; an unindexed table of the chromatic or nonincidence matching polynomial, or an independent earlier calculation of the precise transition census, would reduce novelty.

## References

1. M. Johnson, D. Kratsch, S. Kratsch, V. Patel, and D. Paulusma, *Finding Shortest Paths between Graph Colourings*, initial public arXiv version 25 March 2014, https://arxiv.org/abs/1403.6347.
2. P. Bonsma and D. Paulusma, *Using Contracted Solution Graphs for Solving Reconfiguration Problems*, 2015, https://arxiv.org/abs/1509.06357.
3. O. Merkel, *Recolouring weakly chordal graphs and the complement of triangle-free graphs*, 2021, https://arxiv.org/abs/2106.11087, Theorem 2.
4. N. Banerjee, C. Engels, and D. A. Hoang, *Distance Recoloring*, 2024 preprint, https://arxiv.org/abs/2402.12705.
