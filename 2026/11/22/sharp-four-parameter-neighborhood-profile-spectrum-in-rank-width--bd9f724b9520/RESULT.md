# Sharp four-parameter neighborhood-profile spectrum in rank-width-one graphs

## Finding
Let \(G\) be a finite simple undirected graph of rank-width at most one, and let \(A\subseteq V(G)\) contain exactly four vertices. For its open-neighborhood profile family
\[
\mathcal{N}_G(A)=\{N_G(v)\cap A:v\in V(G)\},
\]
the bound \(|\mathcal{N}_G(A)|\le12\) holds. It is sharp, and every integer from \(1\) through \(12\) occurs for some finite distance-hereditary graph and four-element set \(A\).

Moreover, the maximum size of a set shattered by open-neighborhood profiles over all finite rank-width-one graphs is exactly three. A connected eight-vertex distance-hereditary graph shatters three vertices; eight is the least possible number of vertices in any graph witnessing the shattering of a triple.

## Assumptions and scope
Graphs are finite, simple, and undirected. The neighborhoods \(N_G(v)\) are *open*: \(v\notin N_G(v)\). The parameter set is a set of distinct vertices, although the vertices realizing neighborhood profiles may themselves lie in it. Rank-width is defined by subcubic leaf-labelled decomposition trees with every cut-adjacency matrix having binary rank at most one. Such graphs are precisely the distance-hereditary graphs, equivalently those obtainable by isolated, pendant, true-twin and false-twin vertex additions. Shattering means realizing all \(2^{|A|}\) subsets of \(A\) as open-neighborhood traces. The result does not count equality-sensitive complete quantifier-free types and does not assert a bound for arbitrary larger parameter sets.

## Proof
**Four-leaf split.** Fix a rank-width-one decomposition tree of \(G\) and mark the four leaves corresponding to \(A\). Prune branches with no marks and suppress unmarked degree-two vertices. The resulting unrooted binary tree has four labelled leaves and a central edge separating them into two pairs. At least one edge of the original decomposition induces this same split. Write \(V(G)=X\sqcup Y\), with \(A_X=A\cap X\) and \(A_Y=A\cap Y\) both of size two.

**Cut-rank restriction.** Since the binary adjacency matrix between \(X\) and \(Y\) has rank at most one, rows restricted to the two columns indexed by \(A_Y\) can represent at most two different bitstrings. Thus the traces of vertices from \(X\), represented as ordered pairs \((N_G(v)\cap A_X,N_G(v)\cap A_Y)\), occupy at most two of the four possible columns of the four-by-four profile table. By symmetry, traces of vertices from \(Y\) occupy at most two rows. Two full columns together with two full rows cover at most
\[
2\cdot4+2\cdot4-2\cdot2=12
\]
cells. Therefore \(|\mathcal N_G(A)|\le12\). In particular no four-element set is shattered; no larger set can be shattered either, since any subset of a shattered set is shattered.

**Sharpness and all intermediate values.** A connected thirteen-vertex graph with labelled vertex set \(\{0,\ldots,12\}\), four parameters \(A=(7,10,0,11)\) in that order, and edges listed below realizes twelve different profiles:

```text
0-1  0-3  0-7  0-8  0-9  0-10
1-2  1-9  1-11
2-7  2-8  2-10  2-11
3-9  4-11  4-5  6-7
7-8  7-9  7-10  7-11
8-9  8-10  8-11
9-10  10-11  10-12
```

Its twelve traces (bit positions in the displayed order of \(A\)) are

```text
0000 0001 0010 0011 0100 0111
1000 1011 1100 1101 1110 1111
```

An explicit sequence of *deletions* certifying distance heredity is:

```text
5 pendant to 4; 4 pendant to 11; 6 pendant to 7; 12 pendant to 10;
0 true twin of 9; 3 pendant to 9; 2 true twin of 11;
7 true twin of 8; 8 true twin of 10; 1 false twin of 10;
9 pendant to 10; 10 pendant to 11; 11 remains.
```

At each deletion the named relationship holds in the currently remaining induced graph. Reversing the sequence builds the graph by valid distance-hereditary extensions. Among the four parameter vertices, exactly three neighborhood profiles occur; each of the other nine vertices realizes a different new profile. Keeping all four parameter vertices and any chosen \(r\) of the other nine vertices produces a distance-hereditary induced subgraph with exactly \(3+r\) profiles, for each integer \(0\le r\le9\). Four isolated vertices yield one profile, while the four-vertex star with the entire vertex set as parameters yields two. This establishes every possible count from one through twelve.

**Sharp shattering rank.** Take a triangle on vertices \(0,1,2\), attach respective leaves \(3,4,5\), add a true twin \(6\) of vertex \(0\) (adjacent also to \(3\)), and attach leaf \(7\) to vertex \(5\). These are distance-hereditary extensions. The open-neighborhood traces on \(\{0,1,2\}\) are all eight subsets: vertices \(0,1,2\) realize the three two-element subsets, vertices \(3,4,5\) the three singleton subsets, vertex \(6\) the full subset and vertex \(7\) the empty subset. The graph is connected and has eight vertices. Every graph shattering three vertices must have at least eight vertices, because one vertex realizes at most one of the eight distinct traces. Combined with the four-parameter obstruction, its class has maximal open-neighborhood VC dimension three.

## Verification
The bundled standalone Python 3 file `checker.py` constructs both witness graphs, directly enumerates their traces, checks connectedness, and produces independent pendant/twin reduction certificates. It additionally checks all \(1\) through \(12\) attainable four-parameter counts by vertex deletion and exhaustively enumerates the possible two-row/two-column strip bounds. Run `python3 checker.py`; no third-party Python dependencies are required. Computation checks the finite witnesses, while the universal upper bound and absence of shattered quadruples are proved by the rank-decomposition argument, not by enumeration.

## Relationship to prior work
Dreier, Mählmann, and Toruńczyk (2026) develop a general finite-model theory of types over parameter sets in monadically dependent graphs; their November 5 preprint defines neighborhood complexity and VC dimension, but does not state the precise four-parameter profile spectrum for rank-width one. Bousquet and Thomassé (2014), Section 3.2, prove a broad rank-width bound for distance-\(2\)VC dimension and establish the fundamental cross-cut binary-rank partition lemma used here. That lemma provides the route to the twelve-profile upper bound but does not by itself supply its tight witness, the entire attainable spectrum, or the minimal eight-vertex three-point shattering example. Dreier and collaborators (July 2026) prove almost-linear neighborhood complexity in the wider monadically dependent setting, without an explicit fixed-four spectrum. Distance-hereditary graph characterizations by twin and pendant extensions are standard.

## Limitations
The statement is restricted to open adjacency neighborhoods and fixed four-parameter spectra, not higher quantifier ranks, equality-sensitive complete types, closed neighborhoods, or arbitrary distances. The thirteen-vertex witness is not claimed to have minimum order among four-parameter extremizers. General sharp neighborhood-complexity formulas for all parameter sizes remain outside the result. Earlier equivalent sharp rank-width-one observations may exist outside the inspected literature; publication priority and mathematical proof have not been independently audited.

## References
1. Jan Dreier, Nikolas Mählmann and Szymon Toruńczyk, *First-Order Model Checking on Monadically Dependent Graph Classes*, arXiv:2611.08143v1, November 5, 2026. https://arxiv.org/html/2611.08143v1
2. Nicolas Bousquet and Stéphan Thomassé, *VC-dimension and Erdős–Pósa property*, arXiv:1412.1793v1, December 4, 2014, Section 3.2. https://arxiv.org/html/1412.1793v1
3. Jan Dreier, Nikolas Mählmann, Rose McCarty, Michał Pilipczuk and Szymon Toruńczyk, *Neighborhood Complexity and Radius-1 Merge-Width in Monadically Dependent Graph Classes*, arXiv:2607.10941v1, July 12, 2026. https://arxiv.org/abs/2607.10941
4. Nicholas Connolly, Shin Nishio and Kae Nemoto, *Local Equivalence Classes of Distance-Hereditary Graphs using Split Decompositions*, arXiv:2602.23825, February 27, 2026, Sections I and IV. https://arxiv.org/abs/2602.23825
