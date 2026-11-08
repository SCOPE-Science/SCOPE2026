# Exact perfect-edge-domination polynomial of \(C_n\square K_2\)

## Finding

For every integer \(n\ge3\), let \(G_n=C_n\square K_2\) be the labelled circular ladder, with two labelled rows and cyclically indexed columns. An edge set \(F\subseteq E(G_n)\) is *perfect edge dominating* when every edge not belonging to \(F\) shares an endpoint with **exactly one** edge of \(F\). Selected edges may dominate one another; this is not the same as an efficient edge dominating set or a dominating induced matching.

Define the cardinality polynomial
\[
\mathcal E_n(z)=\sum_{F\text{ perfect edge dominating}}z^{|F|}.
\]
Then
\[
\boxed{\mathcal E_n(z)=z^{3n}+6\,\mathbf{1}_{6\mid n}\,z^n.}
\]
More precisely, \(E(G_n)\) is always a perfect edge dominating set. There are no other such sets unless \(6\mid n\); if \(6\mid n\), there are precisely six additional ones, each containing exactly \(n\) edges. With a zero/one column encoded as (top horizontal edge, bottom horizontal edge, rung), these six sets are the six cyclic shifts of the period-six word
\[
(000),(010),(011),(000),(100),(101).
\]
The symbols indicate edge membership; shifts are by whole columns, not by individual bits. Thus the minimum size is \(3n\) when \(6\nmid n\), and \(n\) when \(6\mid n\).

## Assumptions and scope

All graphs are finite and simple. The cycle \(C_n\) has \(n\ge3\) vertices, and all \(3n\) graph edges are distinct and individually identifiable. The top horizontal edge at column \(i\) joins top vertices \(i\) and \(i+1\pmod n\), and likewise for the bottom row. The rung at column \(i\) joins the two vertices in that column. The requirement concerns unselected edges only. No quotient by graph automorphisms is taken.

## Proof

Associate to each column \(i\) its state \(x_i\in\{0,1,\ldots,7\}\), whose three binary digits are respectively top horizontal, bottom horizontal, and rung membership in \(F\). Write \(t(x),b(x),r(x)\) for these three bits. The original definition gives three necessary and sufficient conditions for the edges at column \(i\):
\[
\begin{aligned}
&r(x_i)=1\quad\text{or}\quad t(x_{i-1})+t(x_i)+b(x_{i-1})+b(x_i)=1,\\
&t(x_i)=1\quad\text{or}\quad t(x_{i-1})+t(x_{i+1})+r(x_i)+r(x_{i+1})=1,\\
&b(x_i)=1\quad\text{or}\quad b(x_{i-1})+b(x_{i+1})+r(x_i)+r(x_{i+1})=1.
\end{aligned}
\]
All indices are cyclic. For example, if the top horizontal edge of column \(i\) is omitted, its four adjacent edges are precisely the top horizontal edges in columns \(i-1\) and \(i+1\), and the rungs in columns \(i\) and \(i+1\). The first line analogously checks the omitted rung. These conditions are therefore an exact reformulation, not merely necessary restrictions.

Construct a finite directed graph \(T\) with all \(64\) ordered pairs \((a,b)\), for \(a,b\in\{0,\ldots,7\}\), as its vertices. Draw an arc \((a,b)\to(b,c)\) precisely when the preceding three conditions hold at the middle column with \((x_{i-1},x_i,x_{i+1})=(a,b,c)\). A labelled cyclic edge selection on \(G_n\) is equivalent to a directed closed walk of length \(n\) in \(T\) with a distinguished initial pair. Conversely, the vertex pairs along such a walk reconstruct one and only one length-\(n\) cyclic column word, including for \(n=3\).

The following finite lemma is the critical computation: the directed graph has exactly \(102\) arcs, and the only vertices lying on any directed cycle are
\[
(7,7),\ (0,2),\ (2,3),\ (3,0),\ (0,4),\ (4,5),\ (5,0).
\]
The arcs among these vertices are exactly the self-loop at \((7,7)\) and the directed six-cycle
\[
(0,2)\to(2,3)\to(3,0)\to(0,4)\to(4,5)\to(5,0)\to(0,2).
\]
Here is a fully specified exhaustive verification of the lemma: enumerate the \(8^3=512\) triples \((a,b,c)\), apply the displayed three Boolean tests to form the arcs, and for each of the \(64\) pair states conduct positive-length directed reachability back to itself. Exactly the seven states displayed above pass. Check the arcs induced by those seven states using the same tests. The included standalone `verify.py` implements this enumeration using only integer arithmetic and built-in Python data structures and asserts the complete result. Because this is a finite check of a fixed graph independent of \(n\), it proves the lemma for every cycle order, rather than extrapolating from small graph instances.

Every directed closed walk lies entirely on a directed cycle (in particular, every state it visits has a positive-length return). The finite lemma consequently leaves only two possibilities: \(n\) repetitions of the loop at \((7,7)\), or a walk around the directed six-cycle, possible precisely when \(6\mid n\). The loop encodes all three edges selected in each column and has total size \(3n\). Along the directed six-cycle the first components of successive state pairs are \(0,2,3,0,4,5\), corresponding to the displayed six-column word. This word selects \(0+1+2+0+1+2=6\) edges per six columns and hence selects \(n\) edges over \(n\) columns. There are precisely six distinct initial states and thus six distinct labelled selections. Summing their weights establishes the formula and the full classification. \(\square\)

## Verification

Run `python verify.py` from the directory containing this file. The verifier constructs the entire \(64\)-state directed graph directly from the local conditions and checks that its cyclic-state graph is exactly the one-loop/six-cycle disjoint union. As a second, independent test, it enumerates every edge subset of \(G_n\) for \(3\le n\le7\), computes edge adjacency directly from endpoint incidence, and checks the original perfect-edge-domination definition. It additionally checks all six explicit periodic selections for \(n=6,12,18,24\). The checker prints `VERIFY_OK` on success. The finite-state lemma, together with its exact equivalence to the graph condition, supplies the proof for unbounded \(n\); the separate small-order experiments are corroboration only.

## Relationship to prior work

Grippo, Lin, Moyano and Vera (arXiv:2607.03894; first posted 2026-07-04) study counting perfect edge dominating sets, extremal trees, forests and chordal graphs, and algorithms for generalized series-parallel and chordal classes. Their accessible introduction and preliminaries explicitly distinguish perfect edge domination from dominating induced matchings. The current formula addresses the nonchordal circular-ladder family and derives an explicit all-set count, rather than a general computational procedure. Direct searches for perfect edge domination of circular ladders, prisms and generalized Petersen graphs revealed no covering enumeration; nevertheless, historical priority is provisional.

Mahmoodi, Behmaram, Došlić and Asadi (2024) note that cycle prisms have no dominating induced matchings because their edges lie on four-cycles. This does not exclude the six additional perfect edge dominating sets here: they are *not* matchings, and the perfect condition deliberately imposes no constraint on the domination counts of selected edges. Earlier edge-domination results on prisms and vertex-domination enumerations concern other predicates. The present result does not assert a new enumeration for those predicates.

## Limitations

The result is restricted to the ordinary labelled circular ladder with two rows, with \(n\ge3\). It neither counts automorphism orbits nor treats open ladders, Möbius ladders or general cubic graphs. The arithmetic finite-state certificate proves the local lemma but is not an independent human proof of that 64-state enumeration. The original 2026 arXiv paper's accessible introduction and preliminaries were inspected, while its remaining full text and PDF could not be retrieved during this review. An undiscovered equivalent or stronger earlier theorem remains possible; no independent audit has been performed.

## References

- Luciano N. Grippo, Min Chih Lin, Verónica Moyano, Camilo Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894, posted 2026-07-04. https://arxiv.org/abs/2607.03894
- Luciano N. Grippo, Min Chih Lin, Camilo Vera, *Perfect Edge Domination in \(P_6\)-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, arXiv:2509.04598, posted 2025-09-04. https://arxiv.org/abs/2509.04598
- A. Mahmoodi, A. Behmaram, T. Došlić, N. Asadi, *Dominating induced matchings and other graph parameters*, AKCE International Journal of Graphs and Combinatorics 21 (2024), 261–267. https://doi.org/10.1080/09728600.2024.2342310
