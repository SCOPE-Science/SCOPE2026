# Sharp total Roman bondage for \(K_{2,2,m}\)

## Finding
For every integer \(m\geq 1\), let \(G_m=K_{2,2,m}\), the complete tripartite graph with part sizes \(2,2,m\). Its **total Roman bondage number** is
\[
 b_{tR}(G_m)=\begin{cases}1,&m=1,\\4,&m=2,\\5,&m\geq3.\end{cases}
\]
Thus the smallest nontrivial two-fixed-part tripartite family has a sharp transition at \(m=3\) and a stable edge-vulnerability threshold thereafter. The proof below is constructive, except for a completely specified finite exhaustive obstruction test for \(m=2,3,4\); a reduction proves those finite tests sufficient for every larger \(m\).

## Assumptions and scope
All graphs are finite, simple, undirected. For an isolate-free graph \(H\), a **total Roman dominating function** is a map \(f:V(H)\to\{0,1,2\}\) for which each zero-labelled vertex has a neighbour labelled \(2\), and the subgraph induced by the positive-labelled vertices has no isolated vertices. Write \(\gamma_{tR}(H)\) for the minimum sum of labels. The **total Roman bondage number** \(b_{tR}(H)\) is the minimum cardinality of an edge set \(F\subseteq E(H)\) for which \(H-F\) is isolate-free and \(\gamma_{tR}(H-F)>\gamma_{tR}(H)\); if none exists, it is infinite. A pair \(u,v\) is an **adjacent dominating pair** if \(uv\in E(H)\) and every vertex is equal or adjacent to at least one of \(u,v\). Here \(G_m\) has two parts \(A=\{a_0,a_1\}\), \(B=\{b_0,b_1\}\), and one part \(C=\{c_0,\ldots,c_{m-1}\}\), with all cross-part edges and no within-part edges.

## Proof
**Step 1: the weight-four criterion.** In any graph of order at least five without isolated or universal vertices, \(\gamma_{tR}(H)=4\) if and only if \(H\) has an adjacent dominating pair. A dominating adjacent pair receives labels \(2,2\) and all other vertices receive \(0\), giving a function of weight four. Conversely no function of weight at most three exists without a universal vertex: a function of weight three must have one \(2\)-vertex and one adjacent \(1\)-vertex, so its \(2\)-vertex is adjacent to every zero and to the other positive vertex. A weight-four function on at least five vertices must contain at least one \(2\). If two vertices carry \(2\), all positive vertices are those two, they must be adjacent, and every zero sees one of them. If exactly one vertex carries \(2\), the remaining positive weight consists of two \(1\)-vertices. The positive-induced graph has no isolate, hence the \(2\)-vertex has a positive neighbour and that adjacent pair dominates the third positive vertex; every zero is adjacent to the \(2\)-vertex. This proves the criterion. The same argument rules out weights one and two. The criterion is an elementary specialization of the domination-pair relationship used in the prior literature; it is not claimed as a new general theorem.

For \(m\geq2\), \(G_m\) has no universal vertex and has every cross-part edge as an adjacent dominating pair, so \(\gamma_{tR}(G_m)=4\). Deletion cannot create a universal vertex. Hence \(b_{tR}(G_m)\) is exactly the fewest deletions, leaving no isolated vertices, that destroy **all** adjacent dominating pairs. For \(m=1\), \(c_0\) is universal and \(\gamma_{tR}(G_1)=3\). Delete \(a_0c_0\): the remaining graph has no universal vertex and is isolate-free; its total Roman domination number exceeds three. Thus \(b_{tR}(G_1)=1\).

**Step 2: explicit upper bounds.** For \(m=2\), delete
\[
 F_2=\{a_0b_1,\ a_0c_1,\ a_1b_0,\ b_0c_0\}.
\]
The resulting graph has no isolated vertex and no adjacent dominating pair. These two properties are verified directly by the exhaustive adjacency checker in `verify.py` (and can be checked against its six vertices). Therefore \(b_{tR}(G_2)\leq4\).

For every \(m\geq3\), delete
\[
 F_m=\{a_0b_0,\ a_0c_1,\ a_1c_0,\ b_0c_0,\ b_1c_0\}.
\]
The residual graph has no isolated vertex. Any remaining edge from \(a_0\) to \(C\) misses \(c_1\); any remaining edge from \(a_1\) to \(C\) misses \(c_0\); and any remaining edge from either \(B\)-vertex to \(C\) misses \(c_0\). Among the remaining \(A\)-\(B\) edges, \(a_0b_1\) misses \(b_0\), \(a_1b_0\) misses \(a_0\), and \(a_1b_1\) misses \(c_0\). Thus no remaining edge dominates. The conclusion \(b_{tR}(G_m)\leq5\) follows.

**Step 3: finite lower-bound certificates.** Label \(a_0,a_1,b_0,b_1,c_0,\dots\) by \(0,1,2,3,4,\dots\). The standalone exhaustive checker enumerates every edge-deletion set of size at most \(3\) for \(G_2\), and of size at most \(4\) for each of \(G_3,G_4\). It computes the residual neighbours from the full original edge list, skips deletion sets that produce isolated vertices, and checks, for every surviving edge, whether its endpoints' **closed** neighbourhoods cover the entire vertex set. The exact complete enumeration gives:

| Graph | Maximum deleted edges | All deletion sets | Isolate-free deletion sets | Isolate-free sets with no dominating edge |
| --- | ---: | ---: | ---: | ---: |
| \(G_2\) | 3 | 299 | 299 | 0 |
| \(G_3\) | 4 | 2517 | 2514 | 0 |
| \(G_4\) | 4 | 6196 | 6192 | 0 |

The executable `verify.py` contains the full, finite, deterministic certificate-generating algorithm, including assertions for each qualifying set and its enumeration counts. There are no timeouts, samples, solver assumptions, or unexplored cases within these finite instances. Therefore \(b_{tR}(G_2)\geq4\), \(b_{tR}(G_3)\geq5\), and \(b_{tR}(G_4)\geq5\).

**Step 4: a four-representative reduction for every \(m>4\).** Suppose at most four edges have been deleted from \(G_m\), and the residual graph has no isolates. At most four vertices in \(C\) touch a deleted edge, because \(C\) is an independent part. Choose a four-element subset \(C'\subset C\) containing all such vertices; retain all of \(A\cup B\) and the vertices of \(C'\). The induced residual graph is exactly \(G_4\) with the same deleted edges, and it has no isolated vertex: each vertex in \(A\cup B\) originally has at least six neighbours within the restricted graph, so four deletions cannot isolate it; a vertex of \(C'\) has exactly the same four neighbours in the restricted and unrestricted graphs. The finite certificate for \(G_4\) gives a remaining adjacent dominating edge in this induced graph. That edge contains a vertex of \(A\cup B\), and it also dominates every omitted vertex of \(C\), since those omitted vertices are incident to no deleted edges. Consequently it is an adjacent dominating edge of the full residual graph, contradiction. Thus at least five deletions are required for every \(m>4\). Combining Steps 1--4 proves all cases.

## Verification
Run `python3 verify.py` in the directory containing this file and the standalone script. The program exhaustively checks the finite lower-bound obstruction sets, the explicit upper-bound deletion sets for \(1\leq m\leq50\), and separately computes total Roman domination numbers from the original labeling definition for the graphs and displayed deletion sets for \(1\leq m\leq5\). The direct labeling computations are diagnostic checks, not the infinite proof. The reduction in Step 4 is essential to extend the finite certificates to all \(m\). The expected final output is `VERIFY_OK`.

## Relationship to prior work
Khosh-Ahang Ghasr and Nazari-Moghaddam introduced the total Roman bondage question, characterized its connection with total bondage when the original total Roman domination number is four, and established exact values for complete graphs, complete bipartite graphs and several other families [1]. Their general reduction to total domination is recognized as prior work. Gamlath and Wei studied total bondage and proved upper bounds for complete multipartite graphs, not the sharp \(K_{2,2,m}\) sequence [2]. Appel and collaborators developed the more general \(k\)-total bondage number and provided results for complete and complete bipartite graphs [3]. The present assertion is the explicit sharp tripartite sequence and its finite-representative proof. No exact formula for this sequence was found in the examined sources; historical priority remains provisional.

## Limitations
Only the part sizes \((2,2,m)\) are determined. The theorem does not give the total Roman bondage number of general complete tripartite or multipartite graphs, nor does it enumerate all minimum edge-deletion sets. The lower bounds use finite exhaustive computation as an exact certificate; they are not purely handwritten case classifications. Reproduction requires executing `verify.py`. No claim of independent certification, priority proof, or polynomial-time algorithm for general graphs is made.

## References
[1] F. Khosh-Ahang Ghasr and S. Nazari-Moghaddam, *Total Roman bondage number of a graph*, arXiv:2602.08758, first public version 2026-02-09. https://arxiv.org/abs/2602.08758

[2] E. G. K. M. Gamlath and B. Wei, *On Total Bondage Number of Graphs*, arXiv:2401.16615, first public version 2024-01-29. https://arxiv.org/abs/2401.16615

[3] J.-P. Appel, G. Fischberg, K. Kelley, N. Shank and E. Sosis, *The \(k\)-Total Bondage Number of a Graph*, arXiv:2506.07000, first public version 2025-06-08. https://arxiv.org/abs/2506.07000
