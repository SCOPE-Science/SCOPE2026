# Minimum power domination and exact propagation-time census of the Hoffman–Singleton graph

## Finding

Let \(H\) be the Hoffman–Singleton graph, the unique strongly regular graph with parameters \((50,7,0,1)\). Its ordinary power-domination number is exactly
\[
\gamma_P(H)=6.
\]
There are exactly \(2{,}329{,}950\) minimum power-dominating six-vertex sets. For every such set \(S\), let \(r(S)\) be the number of synchronous observation rounds needed, **including the initial closed-neighborhood observation as round one**, and let \(e(S)=|E(H[S])|\). The entire joint distribution \(A_{r,e}=\#\{S:|S|=6,\;S\text{ power dominates }H,\;r(S)=r,\;e(S)=e\}\) is:

| \(r\) | \(e=0\) | \(e=1\) | \(e=2\) |
|---:|---:|---:|---:|
| 2 | 12,950 | 0 | 0 |
| 3 | 448,000 | 63,000 | 0 |
| 4 | 378,000 | 630,000 | 294,000 |
| 5 | 0 | 378,000 | 126,000 |

Every other entry is zero. In particular, no minimum power-dominating set induces three or more edges, and the sharp minimum and maximum completion rounds among minimum sets are two and five. The uniformly random six-set is power dominating with probability \(317/2162\).

## Assumptions and scope

All graphs are finite, simple, undirected. Use the following explicit model, with indices modulo five. Its fifty vertices are \(P_{h,j}\) and \(Q_{i,j}\), for \(h,i,j\in\{0,1,2,3,4\}\). Include the undirected edges
\[
P_{h,j}P_{h,j\pm1},\qquad Q_{i,j}Q_{i,j\pm2},\qquad P_{h,j}Q_{i,hi+j}
\]
for all indicated indices. The resulting graph is the Hoffman–Singleton graph. A power-dominating set \(S\) observes \(N[S]\) on round one. On each subsequent synchronous round, every already observed vertex with precisely one unobserved neighbor forces that neighbor; simultaneous forcing is based on the observed set at the beginning of that round.

No structural conclusion about other strongly regular graphs or Moore graphs is claimed.

## Proof

The claim is a finite exhaustive theorem with a deterministic, completely specified enumeration proof. Label \(P_{h,j}\) by \(5h+j\) and \(Q_{i,j}\) by \(25+5i+j\). For a selected set \(S\), let \(O_1=N[S]\). Define recursively
\[
F_t=\{v\notin O_t:\exists u\in O_t\text{ with }N(u)\setminus O_t=\{v\}\},\qquad O_{t+1}=O_t\cup F_t.
\]
Stop on \(O_t=V(H)\) (success, with completion round \(t\)) or \(F_t=\varnothing\) (failure). This recurrence is precisely the definition of ordinary synchronous power domination: induction on \(t\) establishes that every forcing wave is correct, and its strictly increasing observed sets guarantee termination within fifty rounds.

The file `census_pentagons.cpp` constructs all fifty open-neighborhood bitmasks using the displayed modular edges. It traverses every \(k\)-subset, in lexicographic index order, for successive cardinalities \(1\le k\le6\), using a depth-\(k\) loop and no symmetry pruning or unproved exclusions. For each subset, it computes the exact recurrence using fifty-bit integer operations and tallies both the completion round and the number of edges induced by the six selected vertices. Its exhaustive cardinality counts are:

| \(k\) | Candidate sets \(\binom{50}{k}\) | Successful sets |
|---:|---:|---:|
| 1 | 50 | 0 |
| 2 | 1,225 | 0 |
| 3 | 19,600 | 0 |
| 4 | 230,300 | 0 |
| 5 | 2,118,760 | 0 |
| 6 | 15,890,700 | 2,329,950 |

The program prints exactly the eight nonzero cells in `COUNTS.tsv`. As all smaller cardinalities have zero successes and six has a positive count, \(\gamma_P(H)=6\). The table follows from exhaustive accumulation of all fifteen million six-sets. Since every six-set has at most \(6(7+1)=48\) initial closed-neighborhood incidences, round one cannot already observe fifty vertices; the minimum observed round of two is sharp. The table also gives the stated induced-edge restriction and maximum completion round.

An independent enumeration proof is encoded in `census_fano.cpp`. It builds the same uniquely specified \((50,7,0,1)\) graph by taking fifteen Fano planes in the even-permutation orbit of a fixed labelled Fano plane and thirty-five three-subsets of seven points. Join each plane to its seven lines, and join two three-subsets if disjoint. It verifies all degrees and all adjacent/nonadjacent common-neighbor counts before starting. Its separate lexicographic combination iterator and vertex-scanning forcing recurrence exhaust every five-set and six-set, with no use of the pentagon construction or its bit-twiddling forcing loop. It reproduces every cell in `COUNTS.tsv`, including no successful five-sets.

## Verification

From this directory, with a C++17 compiler:

```sh
g++ -O3 -std=c++17 census_pentagons.cpp -o census_pentagons
./census_pentagons > counts_a.txt
g++ -O3 -std=c++17 census_fano.cpp -o census_fano
./census_fano > counts_b.txt
diff -u counts_a.txt counts_b.txt
```

Both output files must contain eight rows of the form `6 r e count` in the order of `COUNTS.tsv` after its header. The former program additionally prints candidate counts for each cardinality from one through six on standard error; the latter prints candidate counts for five and six. Both processes terminate normally and their outputs coincide. Both programs and the table are embedded, standalone files. The count sum equals \(2{,}329{,}950\) and \(2{,}329{,}950/15{,}890{,}700=317/2162\).

## Relationship to prior work

Smith and Hicks developed general integer-programming and fort-based approaches to minimum power domination (first publicly available on 25 May 2021). Those general computational methods do not themselves supply the joint exact census stated here in their accessible abstract; the article's full text was not accessible during this comparison, so no claim about its entire contents is made. Dorbec and collaborators' bounds on generalized power domination of regular graphs concern a different broad theorem and do not imply these exact Hoffman–Singleton counts. The construction and strongly regular parameters of the Hoffman–Singleton graph are classical. Searches of scientific literature and available indexed result summaries did not reveal this exact finite invariant; a missing or unindexed table remains possible.

## Limitations

This is an exact finite computer-assisted enumeration, not a formula for other graph orders, not a symbolic structural characterization of every successful six-set, and not an independently audited result. Reproducibility depends on running the bundled programs with a conforming C++17 compiler. The 2021 computational-methods article was inspected only through its accessible abstract and bibliography, because full-text access was unavailable; it remains a literature-comparison risk. The standard graph model and synchronous round convention are essential.

## References

1. L. A. Smith and I. V. Hicks, “New computational approaches for the power dominating set problem: Set covering and the neighborhoods of zero forcing forts,” *Networks* 79 (2022), 202–219; first public online date 25 May 2021. DOI: https://doi.org/10.1002/net.22056.
2. P. Dorbec and collaborators, “Generalized Power Domination in Regular Graphs,” *SIAM Journal on Discrete Mathematics* (2013). DOI: https://doi.org/10.1137/120891356.
3. Hoffman–Singleton graph, standard pentagon–pentagram construction and parameters: https://en.wikipedia.org/wiki/Hoffman%E2%80%93Singleton_graph.
