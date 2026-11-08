# Six vertices are sharp for seed-budget rank reversals in two-neighbor social contagion

## Finding

**Theorem.** Let \(G\) be a finite, connected, simple, undirected graph. At time zero a uniformly chosen \(k\)-element vertex set is active; subsequently every inactive vertex with at least two active neighbors becomes permanently active. Write \(c_G(k)\) for the number of \(k\)-element seed sets that eventually activate every vertex, and \(q_G(k)=c_G(k)/\binom{|V(G)|}{k}\).

Among pairs of connected graphs on the same number of vertices and with the same degree multiset, the smallest order at which their strict full-activation ranking can reverse as the seed budget \(k\) changes is **six**. At this first order, up to graph isomorphism and interchanging the two graphs, there is exactly one reversing pair: the theta graph \(A=\Theta(2,2,3)\), consisting of three internally disjoint paths of lengths two, two and three between two poles, and \(B\), consisting of two triangles connected by one bridge. Both have sorted degrees \((2,2,2,2,3,3)\) and seven edges.

Their complete contagious-set profiles, indexed by \(k=0,\ldots,6\), are
\[
(c_A(0),\ldots,c_A(6))=(0,0,0,10,14,6,1),\qquad
(c_B(0),\ldots,c_B(6))=(0,0,0,12,13,6,1).
\]
Consequently, \(q_A(3)=1/2<3/5=q_B(3)\), but \(q_A(4)=14/15>13/15=q_B(4)\). If each vertex is instead independently initially active with probability \(p\), the full-activation probabilities satisfy the exact identity
\[
R_A(p)-R_B(p)=p^3(1-p)^2(3p-2).
\]
Thus \(B\) wins for \(0<p<2/3\), \(A\) wins for \(2/3<p<1\), and the unique interior tie is \(p=2/3\).

## Assumptions and scope

The vertex threshold is the **absolute** number two, not a fraction of each vertex's degree. The update rule is deterministic and irreversible, applied simultaneously until stabilization. Randomness occurs only in the initially selected seeds. A strict ranking reversal requires at least two seed budgets with opposing strict inequalities; ties do not count as reversals. The comparison holds the vertex count, sorted degree sequence, and threshold fixed. The exact minimality and uniqueness statement concerns connected simple graphs on at most six vertices, and the Bernoulli-seeding identity concerns the displayed six-vertex pair.

For exact reproducibility, the graphs have vertex set \(\{0,1,2,3,4,5\}\) and edge lists
\[
E(A)=\{01,04,05,12,23,34,35\},\quad
E(B)=\{01,02,03,12,34,35,45\}.
\]
Here \(ij\) denotes the undirected edge between the two distinct integer-labelled vertices \(i\) and \(j\), not a numerical product.

## Proof

**1. Static obstruction criterion.** For any nonempty \(U\subseteq V(G)\), call \(U\) a *two-neighbor fort* when each vertex of \(U\) has at most one neighbor outside \(U\). For a seed set \(S\), complete activation fails if and only if there exists a fort disjoint from \(S\). Indeed, a fort cannot be activated from outside, even if every outside vertex becomes active. Conversely, if the dynamics stabilizes short of complete activation, its nonempty final inactive set is such a fort. This is an exact finite equivalence.

**2. The two profiles.** In \(A\), the only fort of cardinality two is \(\{1,2\}\), and the forts of cardinality three not containing that pair are precisely
\[
\{0,1,4\},\ \{0,1,5\},\ \{0,4,5\},\
\{2,3,4\},\ \{2,3,5\},\ \{3,4,5\}.
\]
A four-seed set therefore fails precisely when its two unseeded vertices are \(\{1,2\}\): one failure in \(\binom64=15\) choices. A three-seed set fails when its three unseeded vertices contain the pair \(\{1,2\}\) (four choices) or equal one of the six additional forts. These are disjoint cases, giving ten failures in \(\binom63=20\) choices. Thus \(c_A(4)=14\) and \(c_A(3)=10\).

In \(B\), the only forts of cardinality at most three containing no smaller fort are \(\{1,2\}\) and \(\{4,5\}\). Consequently two four-seed sets fail, and eight three-seed sets fail (four supersets of each of the two disjoint pairs). Thus \(c_B(4)=13\) and \(c_B(3)=12\). No seed set of cardinality zero or one can grow under a threshold of two. A contagious two-seed set would require at least \(2(6-2)=8\) distinct edges from newly activating vertices to previously active vertices, whereas both graphs have only seven edges; therefore \(c_A(2)=c_B(2)=0\). Every five-seed set activates the remaining degree-two-or-higher vertex immediately, giving \(c_A(5)=c_B(5)=6\). All vertices initially active gives one six-seed set. This proves the two profiles.

**3. Minimality and uniqueness.** To avoid relying on a graph-atlas completeness assertion, the standalone checker enumerates every simple graph on \(n\) *labelled* vertices for each integer \(1\le n\le6\). The \(\binom n2\) possible edges are indexed, and every one of the \(2^{\binom n2}\) bitmasks is visited. For each connected graph the checker examines every one of its \(2^n\) seed sets, computes its exact contagion closure, groups the resulting integer profile by sorted degree sequence, and compares every pair of distinct profiles within a group. This finite enumeration is exhaustive because the edge masks and seed masks exhaust their respective finite sets.

The connected labelled-graph counts are respectively \((1,1,4,38,728,26704)\) at orders one through six. Through four vertices, every connected degree sequence specifies a single unlabelled graph. At five vertices, only two degree sequences admit more than one unlabelled graph: \( (1,2,2,2,3) \), whose two profiles are \( (0,0,0,5,4,1) \) and \( (0,0,0,4,4,1) \), and \( (2,2,2,3,3) \), whose profiles are \( (0,0,4,9,5,1) \) and \( (0,0,4,10,5,1) \). Both pairs are pointwise ordered. Therefore there are no reversing pairs of degree-matched profiles through five vertices. At six vertices there is exactly one reversing pair of profiles, both in degree class \((2,2,2,2,3,3)\), and these profiles are precisely those proved above. There are exactly 180 labelled graphs with the first reversing profile and 90 with the second. Direct enumeration of vertex permutations shows that \(A\) has four automorphisms and \(B\) has eight. Their isomorphism-orbit sizes are therefore \(6!/4=180\) and \(6!/8=90\), exhausting their entire respective labelled-profile classes. Thus each reversing profile is represented by exactly one unlabelled graph, establishing uniqueness as well as minimality.

**4. Independent-seed crossover.** Under independent Bernoulli seeding, grouping seed sets by their cardinality yields \(R_G(p)=\sum_{k=0}^{6}c_G(k)p^k(1-p)^{6-k}\). Subtraction of the displayed profiles gives
\[
R_A(p)-R_B(p)=-2p^3(1-p)^3+p^4(1-p)^2
=p^3(1-p)^2(3p-2).
\]
The factors prove the asserted strict sign classification on \((0,1)\).

## Verification

The included self-contained `verify.py` runs on standard Python 3 without third-party packages: `python3 verify.py`. It independently evaluates seed closure and the fort obstruction for each seed set of both witnesses, performs the complete labelled-graph census through six vertices, and verifies the uniqueness claim using vertex-permutation automorphism counts and orbit-stabilizer. It also checks the polynomial identity at eleven rational grid points, while the algebraic factorization above—not those eleven checks—proves the identity for all real \(p\).

The verified census has 68 sorted-degree classes among connected six-vertex graphs, and only one reversing profile pair. Its output concludes with `ALL_CHECKS_PASSED`. A separate graph-atlas enumeration of connected unlabelled graphs up to six vertices independently reproduced the sharpness and witness profiles; that auxiliary comparison is not needed to run the supplied checker.

## Relationship to prior work

The threshold-cascade formulation and its social interpretation follow the classical work of Watts (2002). Freund, Poloczek and Reichman (2015) study the existence of small contagious sets under minimum-degree and edge-count conditions; Feige, Krivelevich and Reichman (2016) give asymptotic threshold and minimum-contagious-set results on random graphs. Guilbeault and Centola (2021) analyze degree-preserving rewiring and the spreading capacity of complex contagions using simulations and bridge-width measures. These sources establish that graph structure matters, but their inspected claims do not give this exact all-seed-cardinality rank reversal, the order-six uniqueness statement, or the \(2/3\) independent-seeding crossover for this pair. The present result is a finite exact comparison, not a general theory of large networks.

## Limitations

The cutoff was proved by complete finite enumeration, not by a symbolic classification valid at arbitrarily many vertices. The model does not include heterogeneous thresholds, stochastic transmission after seeding, evolving ties, or empirical adoption behavior. The comparison applies to uniform fixed-budget seed sets or independent equal-probability seeding, not targeted or clustered seeding. Historical priority is provisional: related older literature may contain an equivalent small-graph profile even if described under different terms; no independent expert validation is claimed.

## References

1. D. J. Watts, "A simple model of global cascades on random networks," *PNAS* 99 (2002), 5766–5771. Published 2002-04-30. DOI: https://doi.org/10.1073/pnas.082090499 ; open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC122850/ .
2. D. Freund, M. Poloczek and D. Reichman, "Contagious Sets in Dense Graphs," arXiv:1503.00158 (2015). https://arxiv.org/pdf/1503.00158 .
3. U. Feige, M. Krivelevich and D. Reichman, "Contagious Sets in Random Graphs," arXiv:1602.01751 (2016). First preprint 2016-02-04. https://arxiv.org/pdf/1602.01751 .
4. D. Guilbeault and D. Centola, "Topological measures for identifying and predicting the spread of complex contagions," *Nature Communications* 12 (2021), 4430. https://pmc.ncbi.nlm.nih.gov/articles/PMC8292353/ .
5. D. Centola and M. Macy, "Complex Contagions and the Weakness of Long Ties," *American Journal of Sociology* 113 (2007), 702–734. https://doi.org/10.1086/521848 . Only its abstract and bibliographic page were accessible in the source inspection.
