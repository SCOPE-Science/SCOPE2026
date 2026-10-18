# Equality at \(n/2\) for \((1,2)\)-domination in cubic graphs
## Finding
For every finite connected simple cubic graph \(G\) of order \(n\),
\[
\gamma_{1,2}(G)=\frac n2
\]
if and only if the vertices admit a bipartition \(V(G)=A\sqcup B\) such that the cut \(E(A,B)\) is a perfect matching of \(G\). Equivalently, equality in the universal lower bound \(\gamma_{1,2}(G)\ge n/2\) occurs exactly when \(G\) has a perfect matching cut.

In every equality witness, every vertex has exactly one neighbor across the cut. Consequently \(G[A]\) and \(G[B]\) are 2-regular, and both \(A\) and \(B\) are minimum \((1,2)\)-dominating sets.
## Assumptions and scope
Graphs are finite, simple, connected, and cubic. A set \(D\subseteq V(G)\) is \((1,2)\)-dominating when every vertex outside \(D\) has a neighbor in \(D\), and every vertex of \(D\) has at least two neighbors in \(D\). The number \(\gamma_{1,2}(G)\) is the minimum size of such a set.

A perfect matching cut means a bipartition \(V(G)=A\sqcup B\) for which the set of edges with one endpoint in each shore is a perfect matching of the whole graph.
## Proof
Let \(D\) be any \((1,2)\)-dominating set and put \(R=V(G)\setminus D\). Write \(c=|E(D,R)|\).

Because \(G\) is cubic and every vertex of \(D\) has at least two neighbors in \(D\), each vertex of \(D\) has at most one neighbor in \(R\). Hence
\[
c\le |D|.
\]
Because \(D\) dominates \(R\), every vertex of \(R\) has at least one neighbor in \(D\). Hence
\[
c\ge |R|=n-|D|.
\]
Combining the inequalities gives \(|D|\ge n/2\).

Suppose now that \(\gamma_{1,2}(G)=n/2\), and let \(D\) be a minimum set. Then \(|D|=|R|=n/2\), so the two displayed inequalities force \(c=n/2\). Since every vertex of \(D\) has at most one crossing neighbor and the sum of those crossing degrees is \(|D|\), every vertex of \(D\) has exactly one crossing neighbor. Likewise, every vertex of \(R\) has at least one crossing neighbor and the sum is \(|R|\), so every vertex of \(R\) has exactly one crossing neighbor. Thus \(E(D,R)\) is a perfect matching. Cubicity then leaves exactly two neighbors on the same shore at every vertex, so both induced shores are 2-regular.

Conversely, suppose \(V(G)=A\sqcup B\) and \(E(A,B)\) is a perfect matching. Every vertex has exactly one crossing neighbor and therefore exactly two neighbors on its own shore. Thus every vertex of \(A\) has two neighbors in \(A\), while every vertex of \(B\) has a neighbor in \(A\); hence \(A\) is \((1,2)\)-dominating. The perfect matching gives \(|A|=|B|=n/2\), so the lower bound yields \(\gamma_{1,2}(G)=n/2\). The same argument applies to \(B\).
## Verification
The proof is purely counting and does not depend on a finite search. The accompanying verifier independently enumerates every labeled simple cubic graph on four and six vertices, computes \((1,2)\)-domination directly from the definition, tests all vertex bipartitions for a perfect matching cut, and checks the equivalence and the claimed structure of every equality witness.
## Relationship to prior work
Radić and Tepeh's 2026 preprint studies 1-limited domination on cubic graphs and recalls the established sharp bound \(n/2\le\gamma_{1,2}(G)\le3n/4\). It gives exact values for Goldberg snarks, while its searchable full text does not state a perfect-matching-cut characterization of the lower-bound equality case. The 2026 paper of Knor, Sedlar, and Škrekovski studies the relationship with the induced-cycles vertex number and constructs counterexamples to two different conjectures; its stated results concern values strictly above \(n/2\), not the equality characterization here.

The older 2021 paper of Fakharan, Gorzin, Henning, Jafari, and Touserkani is the source cited for the sharp \(n/2\) lower bound. Its abstract and bibliographic record were accessible during comparison, but a complete lawful open full text was not located; this is retained as the main literature risk.
## Limitations
The theorem characterizes only equality at the lower endpoint \(n/2\); it does not determine \(\gamma_{1,2}(G)\) above that endpoint. It also does not classify perfect matching cuts themselves or give a new algorithmic complexity result. The principal originality risk is that the same equality characterization may appear in older literature under matching-cut terminology not exposed by the accessible records.
## References
1. G. Radić and A. Tepeh, *On 1-limited and (1, 2)-domination in cubic graphs*, arXiv:2610.01796v1, first public 2026-10-01; MSC 2020 05C69, 68Q25.
2. M. H. Fakharan, A. A. Gorzin, M. A. Henning, A. Jafari, and R. Touserkani, *On (1, 2)-domination in cubic graphs*, Discrete Mathematics 344 (2021), 112546, doi:10.1016/j.disc.2021.112546.
3. M. Knor, J. Sedlar, and R. Škrekovski, *Counterexamples to two conjectures on (1, 2)-domination in cubic graphs*, arXiv:2608.17851, first public 2026-08-18.
