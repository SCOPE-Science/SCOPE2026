# Exact shattering polynomial of two-vertex cuts in a complete graph

## Finding
For every integer \(n\ge3\), consider the binary edge-query concept class
\[\mathcal D_{n,2}=\{\delta(A):A\subseteq[n],\ |A|=2\},\]
where \(\delta(A)=\{\{u,v\}:|\{u,v\}\cap A|=1\}\) is the edge cut of the complete graph. A query support \(S\subseteq\binom{[n]}2\) is shattered exactly in the following cases, and in no others:

1. \(S\) is empty, or \(|S|=1\).
2. \(|S|=2\) and \(n\ge5\), with no restriction on the two edges.
3. \(|S|=3\), \(n\ge6\), and the edge graph \(([n],S)\) without isolates is isomorphic to \(K_{1,3}\), \(P_4\), or \(P_3\sqcup K_2\).
4. \(|S|=4\), and the edge graph without isolates is one of \(K_{1,4}\), \(P_5\), or the five-vertex tree with degree sequence \((3,2,1,1,1)\), with \(n\ge7\); or it is \(P_3\sqcup P_3\), with \(n\ge8\).

Here \(P_j\) is the path on \(j\) vertices and \(K_{1,j}\) is the star with \(j\) leaves. In particular, the entire shattering polynomial is
\[
\begin{aligned}
\Phi_n(z)={}&1+\binom n2 z+\mathbf1_{n\ge5}\binom{\binom n2}{2}z^2\\
&+\mathbf1_{n\ge6}\left(16\binom n4+30\binom n5\right)z^3\\
&+\left(\mathbf1_{n\ge7}125\binom n5+\mathbf1_{n\ge8}90\binom n6\right)z^4.
\end{aligned}
\]
All higher coefficients vanish. Consequently,
\[\operatorname{VCdim}(\mathcal D_{n,2})=
\begin{cases}1,&n=3,4;\\2,&n=5;\\3,&n=6;\\4,&n\ge7.\end{cases}\]

## Assumptions and scope
Vertices are labeled; edges are unordered; the graph of each query support is simple. A hypothesis chooses **exactly two distinct vertices**. A query \(\{u,v\}\) has label one precisely when one but not both endpoints is selected. No empty or singleton selected sets are added. The formulas concern VC shattering of edge queries, not cut-space linear rank, minimum cuts, or the Littlestone dimension. In the above polynomial \(\mathbf1\) is the indicator of the displayed condition.

## Proof
Put \(s=|S|\) and let \(t\) be the number of endpoints of edges of \(S\). Associate to each vertex \(v\) its incidence row \(r_v\in\mathbb F_2^s\), with a one at the queried edges containing \(v\). The trace of the selected pair \(\{u,v\}\) is exactly \(r_u+r_v\) in \(\mathbb F_2^s\). The \(n-t\) isolated vertices contribute zero rows. This identity is an exact necessary-and-sufficient trace test.

**No five-edge shattering.** For any shattered nonempty support, its all-one trace comes from a pair \(\{a,b\}\). Thus every edge of \(S\) joins exactly one of \(a,b\) to a vertex outside the pair. In particular \(t\le s+2\). At most \(\binom t2+t+1\) distinct traces can be produced, grouping pairs into two active vertices, one active plus one isolated vertex, and two isolated vertices. If \(s=5\), then \(t\le7\) and this count is at most \(21+7+1=29<32\). Hence no five-edge support is shattered. Shattering is hereditary in supports, so nothing larger is shattered.

**Candidate structures through four edges.** The same trace-count bound rules out a three-edge shattered support with \(t\le3\), since then at most seven traces appear. With \(s=3\), the all-one constraint makes \(S\) a subgraph of a bipartite graph whose one side is of size two. If \(t=4\) the support is a tree, necessarily the claw or four-vertex path. If \(t=5\) it is a three-vertex path plus an edge. If \(t=6\) it consists of three disjoint edges, whose all-one trace requires three selected vertices, impossible. The claimed three-edge list follows.

With \(s=4\), \(t\le6\). There must be \(t\ge5\) because \(\binom42+4+1=11<16\). For \(t=5\), all-one implies the support is a connected tree, of which there are precisely three unlabeled five-vertex shapes: the four-star, the five-path, and the one-degree-three broom. For \(t=6\), it is a two-component forest. The possible component structures are \(P_4\sqcup K_2\), \(K_{1,3}\sqcup K_2\), and \(P_3\sqcup P_3\). The first requires at least three vertices to cover all four edges, hence has no all-one trace. The second has no trace simultaneously selecting exactly two of its three star edges and selecting its disjoint edge: selecting the star center yields all three star edges, while selecting leaves individually requires two vertices before accounting for the disjoint edge. Only the third remains.

**Exact realization, including minimum \(n\).** The incidence-row test reduces sufficiency for each surviving isomorphism type to a fixed table of at most six active vertices and zero, one, or two zero rows. Entries below count distinct traces when the number of unqueried/isolated vertices is \(0,1,2\), respectively:

| Edge support type | Query count | Active vertices | Traces for 0, 1, 2 isolated vertices |
| --- | ---: | ---: | --- |
| \(K_2\) | 1 | 2 | \(1,2,2\) |
| \(P_3\) | 2 | 3 | \(3,3,4\) |
| \(K_2\sqcup K_2\) | 2 | 4 | \(2,4,4\) |
| \(K_{1,3}\) | 3 | 4 | \(3,7,8\) |
| \(P_4\) | 3 | 4 | \(3,7,8\) |
| \(P_3\sqcup K_2\) | 3 | 5 | \(7,8,8\) |
| \(K_{1,4}\) | 4 | 5 | \(10,15,16\) |
| five-vertex broom | 4 | 5 | \(10,15,16\) |
| \(P_5\) | 4 | 5 | \(10,15,16\) |
| \(P_3\sqcup P_3\) | 4 | 6 | \(15,15,16\) |

For clarity, each entry is obtained without sampling: write one incidence row per active vertex, form every pairwise distinct-row sum, and, where appropriate, include sums with one or two zero rows. For each row of the table, having all \(2^s\) traces is equivalent to shattering. More than two inactive vertices add no new trace types, so the table proves the exact thresholds for all \(n\).

**Enumerating supports.** There are \(\binom n2\) singleton supports and \(\binom{\binom n2}{2}\) two-edge supports. On four labeled vertices, a three-star has four realizations and a four-vertex path has twelve, contributing \(16\binom n4\). A \(P_3\sqcup K_2\) has ten choices of its path-vertex triple and three choices of its center, contributing \(30\binom n5\). On five labeled vertices the four-star, broom, and path have respectively \(5,60,60\) realizations; on six labeled vertices there are \(\binom63\cdot3\cdot3/2=90\) ways to form two disjoint three-vertex paths. Thus the four-edge coefficient is \(125\binom n5+90\binom n6\), subject to the exact size thresholds. This proves the polynomial and dimension formula.

## Verification
The accompanying standalone Python 3 program `verify.py` uses only the standard library. For every \(3\le n\le8\), it exhaustively enumerates all query supports of cardinality at most four, directly computes every trace from the \(\binom n2\) admissible hypotheses, compares shattering with the stated graph-shape criterion, and confirms all five coefficients of \(\Phi_n\). It also exhaustively rejects all five-edge supports through \(n=6\). Its expected final line is `TWO_VERTEX_CUTS_PASS 37358 supports including every size <=4 through n=8`. The unrestricted assertion is proved above and is not inferred from these finite tests.

## Relationship to prior work
Lee, Li, Santha, and Zhang (2020) study the **real-linear dimension** of characteristic vectors of minimum cuts of weighted graphs, a different invariant from surjectivity of projections of the fixed-two-vertex cut family. Coudert, Csikós, Ducoffe, and Viennot (2024) study the VC dimension of **vertex closed-neighborhood** systems of graphs, not fixed-size cut vectors queried on edges. Neither inspected work states the motif-by-motif shattering characterization or its generating polynomial; the present work makes no priority claim for the general definition of shattering, general cut vector notation, or incidence-vector identities.

## Limitations
The result concerns only the full edge set of a complete simple graph and cuts whose selected shore contains exactly two vertices. It does not determine the online Littlestone dimension or analogous formulas for general prescribed shore sizes, and the available literature comparison cannot exclude overlooked equivalent statements under different terminology. Exhaustive computation stops at the stated finite orders; proof for all orders is mathematical.

## References
1. Troy Lee, Tongyang Li, Miklos Santha, and Shengyu Zhang, *On the Cut Dimension of a Graph*, arXiv:2011.05085 (first public version 2020-11-10), https://arxiv.org/abs/2011.05085.
2. David Coudert, Mónika Csikós, Guillaume Ducoffe, and Laurent Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588 (first public version 2024-05-13), https://arxiv.org/abs/2405.07588.
