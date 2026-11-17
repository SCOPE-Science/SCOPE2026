# A five-step majority clock and 120 recurrent symmetry types on the \(4\times5\) torus

## Finding

Let \(G=C_4\square C_5\) be the labelled Cartesian-product graph with vertices \((x,y)\in\mathbb Z/4\mathbb Z\times\mathbb Z/5\mathbb Z\). Under synchronous binary majority with current-state tie retention, **all** \(2^{20}=1,048,576\) initial configurations eventually have least period one or two, and the complete recurrent-orbit and entrance-time census is as follows. There are exactly **3,186 fixed configurations** and **3,225 primitive two-cycles** (6,450 configurations). Their respective complete attraction basins have **747,626** and **300,950** configurations. Thus the total number of temporal cycles is **6,411**.

The first periodic-entry time is the least \(t\ge0\) for which \(F^{t+2}(s)=F^t(s)\). The joint population table is exact:

| First entry \(t\) | Eventual period 1 | Eventual period 2 | Total |
|:--:|--:|--:|--:|
| 0 | 3,186 | 6,450 | 9,636 |
| 1 | 96,300 | 94,740 | 191,040 |
| 2 | 346,900 | 138,400 | 485,300 |
| 3 | 226,680 | 51,120 | 277,800 |
| 4 | 68,760 | 10,080 | 78,840 |
| 5 | 5,800 | 160 | 5,960 |
| **All** | **747,626** | **300,950** | **1,048,576** |

The first periodic-entry bound **five** is sharp and attained by exactly **5,960** states. Under translations and reflections in each coordinate and global complementation, the **6,411** periodic temporal cycles partition into **120 geometric types**: **53** classes of fixed configurations and **67** of primitive two-cycles. This symmetry group has order \(160\).

## Assumptions and scope

The graph has 20 distinct labelled vertices and exactly four distinct neighbors per vertex, namely \((x\pm1,y)\) and \((x,y\pm1)\), interpreted modulo 4 and 5. A configuration is a function \(s:V(G)\to\{0,1\}\). All sites update simultaneously according to
\[
F(s)(v)=\begin{cases}1,&\sum_{u\sim v}s(u)\ge3,\\0,&\sum_{u\sim v}s(u)\le1,\\s(v),&\sum_{u\sim v}s(u)=2.\end{cases}
\]
A *primitive period-two orbit* is a pair \(\{s,F(s)\}\) with \(F^2(s)=s\) and \(F(s)\ne s\). Its attraction basin includes both orbit states. The *first entry* \(t\) is the distance along the deterministic transition map from the initial state to its first periodic state. The spatial group consists of the \(80\) maps \((x,y)\mapsto(\epsilon x+a,\delta y+b)\), \(\epsilon,\delta\in\{\pm1\}\), \(a\in\mathbb Z/4\), \(b\in\mathbb Z/5\), extended by independent bitwise color complementation. Two temporal cycles are geometrically equivalent when a group element maps one cycle onto the other; time rotation within a cycle is ignored. No claim is made about other grid sizes or other tie rules.

## Proof

This is an exact, finite computer-assisted proof, with two standalone and algorithmically independent exhaustive implementations included as source files. No floating point computation or probabilistic sampling is used.

**First exhaustive construction.** In `verify_indegree.cpp`, each state is encoded by an integer from \(0\) through \(2^{20}-1\) using row-major vertex indexing. The program constructs \(F(s)\) by four explicit modular-neighbor lookups for every vertex. For each target state its transition indegree is accumulated. Repeatedly removing indegree-zero states produces a list of **all** nonrecurrent states, because in any finite functional graph precisely the directed-cycle vertices survive indegree peeling. Every surviving cycle is traversed exactly once to assign its least period, and the peeled list is processed backwards to assign to every initial state its unique target cycle and exact first-entry depth. The program then counts cycles, states and the joint depth/period table. To determine geometric cycle classes, it explicitly generates the \(80\) coordinate symmetries, adds global bit complementation, and unions temporal cycles related by these generators. All 160 transformations preserve the local majority-with-retained-ties rule; the resulting equivalence classes therefore form the announced quotient.

**Independent reconstruction.** In `verify_trajectory.cpp`, the vertices use column-major encoding, with a separately written transition evaluator. It follows every not-yet-classified trajectory until a repeated or previously classified state is encountered, identifies the full cycle and unwinds the trajectory stack. It independently computes all basin and first-entry populations. In addition, it directly tests \(F(s)=s\) and \(F^2(s)=s\) for all \(2^{20}\) states to verify the recurrent counts without relying on the trajectory routine. Instead of the first program's union-find quotient, it obtains the number of symmetry orbits by Burnside's lemma, using the fact that a symmetry fixes a temporal cycle exactly when it sends a chosen representative into that same cycle. Its sums of fixed temporal cycles over all 160 transformations are **8,480** for period one and **10,720** for period two, giving \(8,480/160=53\) and \(10,720/160=67\).

Both independently complete enumerations report that only periods one and two exist, with maximal first-entry time five, and that the complete joint table is as printed. The algorithms visit all states, not a sample; integer counters suffice at this state-space size. The independent algorithms, their source files and raw outputs are included for reproducibility. This supplies an exhaustive finite proof of every numerical assertion above.

## Verification

Run both provided C++17 sources from a directory containing the files:

```sh
g++ -O3 -std=c++17 verify_indegree.cpp -o check_indegree
./check_indegree 4 5 > replay_indegree.txt
g++ -O3 -std=c++17 verify_trajectory.cpp -o check_trajectory
./check_trajectory > replay_trajectory.txt
```

The packaged outputs `out_indegree.txt` and `out_trajectory.txt` were produced by compiling and executing these exact source files. The independent outputs agree on **3,186** fixed states, **3,225** primitive two-cycles, the complete 12-cell joint time/period table, the exact five-update cutoff, and **53** plus **67** symmetry classes. They separately reconstruct the transition table rather than importing one another's computed data. The direct fixed and two-period tests in the second program return 3,186 and 6,450 states. The first program additionally prints the complete distribution of individual temporal-cycle basin sizes, grouped by period and basin cardinality. Its histogram is not needed to infer the main counts.

## Relationship to prior work

Goles and Olivos's classical period-two theorem for finite symmetric threshold systems, cited in Benjamini et al., already implies the broad restriction to eventual period one or two; no novelty is claimed for that restriction alone. The established 2014 majority-dynamics literature treats convergence and disagreement on infinite unimodular and random graphs, not this exact labelled torus basin computation. Nakar and Ron (2025) study the same threshold-three rule on arbitrary two-dimensional tori and characterize *periodic configurations* structurally. Their classification must not be mistaken for the full forward-time attraction census; it does not supply the precise 4-by-5 entrance shells, basin counts or geometric temporal-cycle quotient above.

A previously published exact \(C_4\square C_4\cong Q_4\) majority-dynamics computation concerns a different, bipartite 16-vertex graph. The present 20-vertex \(C_4\square C_5\) contains an odd pentagonal cycle and is not isomorphic to \(Q_4\). The previous width-three torus fixed-point enumeration likewise does not cover the present four-row basin dynamics, and a dodecahedral 20-vertex census concerns a cubic rather than 4-regular graph. The exact-census literature searches did not identify a covering 4-by-5 result; absence from search results is not proof of absolute priority.

## Limitations

This result is restricted to labelled \(C_4\square C_5\), with four distinct neighbors and incumbent tie retention, and does not produce a formula for all rectangular tori. The proof is exhaustive computation supported by two separately developed implementations, not an external formal certificate or independent mathematical audit. Existing broad period-two and structural periodic-state theorems are credited. Unindexed computations and inaccessible historical sources could limit historical originality; only the specified exact finite census is claimed. No statistical inference or universality beyond the stated finite graph is asserted.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first public arXiv posting **2014-05-11**, arXiv:1405.2486. https://arxiv.org/abs/1405.2486
3. Y. Nakar and D. Ron, *Characterizing and Testing Configuration Stability in Two-Dimensional Threshold Cellular Automata*, arXiv:2507.14569, first public **2025-07-19**. https://arxiv.org/abs/2507.14569
4. Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics **70** (1988), DOI: 10.1016/0012-365X(88)90005-2 (one-dimensional cyclic majority, distinct setting).
5. *Thirty geometric recurrent classes and a sharp four-step clock for majority dynamics on the four-cube*, public mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-thirty-geometric-recurrent-classes-and-a-sharp-four-step-clock-f--c8cd34678da7 (different graph).
6. *Exact fixed-point entropy gap for majority tie-breaking on a width-three torus*, public mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-fixed-point-entropy-gap-for-majority-tie-breaking-on-a-wid--d7b5940b2c83 (different width and invariant).
