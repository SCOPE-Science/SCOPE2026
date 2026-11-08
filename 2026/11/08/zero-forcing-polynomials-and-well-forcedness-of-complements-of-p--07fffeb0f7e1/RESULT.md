# Zero-forcing polynomials and well-forcedness of complements of paths and cycles

## Finding

For every integer \(n\ge5\), let \(P_n\) and \(C_n\) be the usual simple path and cycle on \(n\) labelled vertices, and write \(\overline H\) for a simple graph complement. Under *standard* zero forcing, the complete zero-forcing polynomials are

\[
\mathcal Z(\overline{P_n};z)
=z^{n-3}\left((n-3)^2+1+\binom n2z+nz^2+z^3\right),
\]
\[
\mathcal Z(\overline{C_n};z)
=z^{n-3}\left(n(n-4)+2\mathbf1_{\{n=6\}}+\binom n2z+nz^2+z^3\right).
\]

In particular, every inclusion-minimal zero-forcing set of either complement has cardinality exactly \(n-3\): both infinite graph families are **well-forced**. Their minimum-set multiplicities are respectively \((n-3)^2+1\) and \(n(n-4)+2\mathbf1_{\{n=6\}}\).

This finding concerns complete zero-forcing-set enumerators and the structure of minimal initial sets. The scalar equality \(Z(\overline{P_n})=Z(\overline{C_n})=n-3\) is already established in the cited literature and is not a novelty claim. The \(n=5\) cycle-complement case also coincides with the classical cycle.

## Assumptions and scope

Graphs are finite, simple, undirected, and have labelled vertices. A blue vertex may *force* its unique white neighbor blue; the initial blue set is zero forcing if a sequence of such moves colors every vertex blue. For a graph \(G\), set
\[\mathcal Z(G;z)=\sum_{S\subseteq V(G)\,\text{zero forcing}}z^{|S|}.\]
A zero-forcing set is *inclusion-minimal* when removing any of its vertices destroys zero forcing. It is *minimum* when its cardinality equals the zero-forcing number. A graph is well-forced when all its inclusion-minimal zero-forcing sets are minimum.

In the argument below, \(H\) denotes either \(P_n\) or \(C_n\); vertices initially white in \(\overline H\) form a set \(W\).

## Proof

**Step 1: a sharp white-set cutoff.** In \(\overline H\), each blue vertex has at most two nonneighbors within \(W\), because its degree in the underlying graph \(H\) is at most two. Thus if \(|W|\ge4\), every blue vertex sees at least two white neighbors and no first force is possible. Hence every successful set has at most three initially white vertices.

For \(|W|=3\), an initial blue vertex \(b\) can force if and only if it has exactly two original-graph neighbors, both in \(W\). These are the two vertices at distance one from an internal path vertex, or the two cyclic neighbors of a cycle vertex. Call such a vertex \(b\) a *witness center* of \(W\). Indeed, the two neighbors of \(b\) in \(H\) must be white, leaving exactly one white complement-neighbor to force. Conversely, each first force from a three-white configuration must arise this way.

A witness center always leads to a complete force. After it forces the third white vertex, the only two whites are the original neighbors \(b^-\) and \(b^+\) of \(b\). A vertex two steps from \(b\) along \(H\), on a side that exists, is blue and adjacent in \(\overline H\) to exactly one of the two remaining whites. Such a vertex exists for paths of order at least five and for cycles of order at least five. It forces one white; the last white has a blue neighbor in \(\overline H\) and can then be forced. Therefore a three-element \(W\) is admissible if and only if it has a witness center.

**Step 2: every pair of whites extends to an admissible triple.** Fix two distinct vertices \(u,v\) in \(H\). If they are at distance two, use their middle vertex as a witness center and choose the third white outside these three vertices, possible because \(n\ge5\). If their distance is at least three, take as third white the vertex two steps from \(u\) on a shortest \(u\)--\(v\) path; the intervening vertex is a witness center and is not white. If they are adjacent in a cycle, use the vertex three steps after one endpoint in the direction traversing their edge; the intermediate vertex two steps after that endpoint witnesses the two whites separated by two edges. All four vertices needed are distinct because \(n\ge5\). If they are adjacent path vertices \(i,i+1\), take \(i+3\) and witness \(i+2\) when \(i+3\le n\), and otherwise take \(i-2\) and witness \(i-1\). One alternative exists for every adjacent pair when \(n\ge5\). Thus every pair of whites lies in a successful white triple.

Zero forcing is monotone under adding initially blue vertices. Every blue set with at most two white vertices is therefore zero forcing, being a superset of a successful blue set having three whites. By Step 1 every zero-forcing set has at most three whites, and every three-white zero-forcing set is inclusion-minimal. Every set with fewer whites properly contains such a three-white set and is not inclusion-minimal. Hence the complements are well-forced, with zero-forcing number \(n-3\).

**Step 3: count successful three-white sets for paths.** For each of the \(n-2\) internal vertices \(b\), the event that \(b\) witnesses \(W\) chooses the two neighbors of \(b\) as white, keeps \(b\) blue, and chooses the third white from the remaining \(n-3\) vertices. This gives \((n-2)(n-3)\) counted witness events. Two different witness centers can occur together precisely when they differ by two positions along the path, producing one common white triple. There are \(n-4\) such pairs, and no triple of witness centers can fit three whites. Inclusion--exclusion gives
\[
(n-2)(n-3)-(n-4)=(n-3)^2+1.
\]

**Step 4: count successful three-white sets for cycles.** There are \(n\) possible witness centers, each accounting for \(n-3\) white triples. Two centers can witness the same white triple precisely if they are cyclically two steps apart. There are \(n\) unordered pairs of such centers for \(n\ge5\), with one common white triple per pair. For \(n\ne6\), three witnesses are impossible. For \(n=6\), exactly the two alternating white triples have three witnesses, so inclusion--exclusion adds these two triple intersections back. The count is therefore
\[
n(n-3)-n+2\mathbf1_{\{n=6\}}=n(n-4)+2\mathbf1_{\{n=6\}}.
\]

**Step 5: complete the polynomials.** Step 2 shows that every white set with zero, one or two vertices is admissible. Their contributions are \(z^n+nz^{n-1}+\binom n2z^{n-2}\). Steps 3--4 give exactly the coefficients at \(z^{n-3}\), while Step 1 makes all lower-degree coefficients zero. This proves the stated polynomials and the well-forced classification.

## Verification

The standalone `verify.py` constructs the complement adjacency relations without using the counting formulas, exhaustively tests the literal sequential forcing rule for every initial subset for both graph families of orders \(5\) through \(12\), checks every polynomial coefficient and inclusion-minimal forcing set, and checks the witness-center condition independently. The computations test \(16{,}320\) labelled initial subsets across \(16\) graph profiles. The unrestricted theorem follows from the preceding proof, not from these finite computations.

## Relationship to prior work

Boyer et al. (arXiv:1801.08910, first submitted 2018-01-26) introduced and studied zero-forcing polynomials and prove general high-degree coefficient identities; their work covers the definitions, several graph families, and top coefficients \(1,n,\binom n2\) here. Their inspected paper does not give the complete polynomials for complements of arbitrary paths and cycles.

Curl et al. (arXiv:2206.03932, first submitted 2022-06-08) determine the zero-forcing number of complements of nonstar trees and of unicyclic graph classes, encompassing the scalar lower bound \(n-3\) for the families here. This prior scalar claim is not re-presented as novel; the new content is exact multiplicities for every initial-set size and the classification of all inclusion-minimal sets.

Jacob (arXiv:2309.06234, 2023) introduces zero-forcing span and establishes span-one statements for certain other graph families. These complements also have span one, but their complete polynomials are not a consequence of the inspected classifications. Grood et al. (arXiv:2312.14298, 2023) define and study well-forced graphs, especially trees. The complement families are not covered by their tree classification. The integer sequence \((n-3)^2+1\) is a pre-existing square-plus-one numerical sequence, not independently a new integer sequence. No novelty is claimed for the numerical sequence without its zero-forcing interpretation.

## Limitations

The formulas use standard zero forcing, not skew, positive-semidefinite, or power domination. They cover complements only of simple paths and cycles, for \(n\ge5\); no arbitrary maximum-degree-two disjoint-union classification is asserted. The smallest cycle-complement example is a classical cycle, and established scalar and highest-coefficient results are acknowledged. Prior-coverage uncertainty remains for unindexed equivalent descriptions using forts, failed zero-forcing sets, or Z-Grundy formulations. Independent mathematical audit has not been conducted.

## References

1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (2018-01-26), https://arxiv.org/abs/1801.08910.
2. E. Curl, S. Fallat, R. Moruzzi Jr., C. Reinhart, D. Young, *On the zero forcing number of the complement of graphs with forbidden subgraphs*, arXiv:2206.03932v1 (2022-06-08), https://arxiv.org/abs/2206.03932.
3. B. Jacob, *The zero forcing span of a graph*, arXiv:2309.06234v1 (2023-09-12), https://arxiv.org/abs/2309.06234.
4. C. Grood, R. Haas, B. Jacob, E. King, S. Nasserasr, *Well-forced graphs*, arXiv:2312.14298v1 (2023-12-21), https://arxiv.org/abs/2312.14298.
