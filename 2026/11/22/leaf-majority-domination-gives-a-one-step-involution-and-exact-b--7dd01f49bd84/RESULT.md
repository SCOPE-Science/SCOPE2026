# Leaf-majority domination gives a one-step involution and exact basins over every core graph

## Finding

Let \(H=(V,E)\) be any finite simple graph with \(k=|V|\ge1\). Attach \(m_v\) individually labelled degree-one vertices to each core vertex \(v\), where \(m_v\ge d_H(v)+1\). On the resulting graph, run synchronous binary open-neighbour majority, retaining the current bit at a tie. Write \(F\) for its update map and \(M=\sum_{v\in V}m_v\).

**Complete one-step attractor classification.** Every state is periodic by time one, with the exact identity
\[
F^3=F.
\]
The recurrent configurations are exactly the \(2^{2k}\) states in which all \(m_v\) leaves at each core vertex agree with one another. The recurrent map swaps, at every core vertex, its core bit with its uniform leaf-block bit. Hence the system has precisely \(2^k\) fixed states and \((2^{2k}-2^k)/2\) primitive two-cycles, regardless of \(H\) and of the admissible multiplicities \(m_v\). Every one of these attractors has a nonempty basin.

The first-periodic-entry populations are exactly \(2^{2k}\) at time zero and \(2^{k+M}-2^{2k}\) at time one, with none later. In particular, the probability of starting at a periodic state under the uniform initial law is \(2^{k-M}\). At the minimum mantle size \(m_v=d_H(v)+1\), this is \(2^{-2|E|}\); for the complete core \(H=K_k\), it is \(2^{-k(k-1)}\).

**Exact individual attraction-basin formula.** For words \(a,b\in\{0,1\}^{V}\), define
\[
 s_v(a)=\sum_{u\in N_H(v)}a_u,
\qquad
 J_v(a,j)=
 \begin{cases}
  1,&2(j+s_v(a))>m_v+d_H(v),\\
  0,&2(j+s_v(a))<m_v+d_H(v),\\
  a_v,&2(j+s_v(a))=m_v+d_H(v).
 \end{cases}
\]
Put
\[
 W(a,b)=\prod_{v\in V}\left(\sum_{j=0}^{m_v}\binom{m_v}{j}
 \mathbf1\{J_v(a,j)=b_v\}\right).
\]
If \(z(a,b)\) denotes the state with core word \(a\) and each leaf-block word constant \(b_v\), then the basin of fixed state \(z(a,a)\) has size \(W(a,a)\); the basin of the two-cycle \(\{z(a,b),z(b,a)\}\), for \(a\ne b\), has size \(W(a,b)+W(b,a)\). These formulas determine **every** individual attractor basin for any finite core and permitted mantle.

## Assumptions and scope

The core \(H\) can be disconnected or edgeless. Its vertices, and every private leaf, are distinguished and labelled. Graphs are simple and undirected, with no self-loops. All vertices update simultaneously using only current neighbour bits; when exactly half the neighbours have bit one, the vertex retains its current bit. The time of first periodic entry of \(x\) is the least nonnegative \(t\) with \(F^{t+2}(x)=F^t(x)\). A basin is the set of all initial states eventually entering the specified fixed point or temporal two-cycle. No probabilistic hypothesis is used in the exact counts; the displayed probability refers only to uniform selection of a labelled initial configuration.

## Proof

**1. Uniformization.** Let \(x_v(t)\) be a core bit and \(y_{v,i}(t)\) the bit of its \(i\)-th private leaf. A leaf has the unique neighbour \(v\), so
\[
y_{v,i}(t+1)=x_v(t)\qquad(t\ge0).
\]
Thus at time one, each leaf block is uniform. Denote by \(\mathcal S\) the set of all such block-uniform states. Every state enters \(\mathcal S\) by the first update, and \(|\mathcal S|=2^{2k}\).

**2. Strict domination and swapping.** Consider \(z(a,b)\in\mathcal S\). At core vertex \(v\), exactly \(m_v\) pendant neighbours carry \(b_v\) and at most \(d_H(v)\) core neighbours carry the opposite bit. Since \(m_v>d_H(v)\), the strict neighbour majority is \(b_v\), independent of all other core bits and of tie retention. All pendant leaves copy \(a_v\). Consequently
\[
F(z(a,b))=z(b,a).
\]
This is an involution on all of \(\mathcal S\). Since every initial state is mapped into \(\mathcal S\) after one update, \(F^3=F\). Conversely, every state of \(\mathcal S\) is periodic, while no state outside \(\mathcal S\) can be periodic: a periodic state must belong to the forward-invariant image \(\mathcal S\). Thus the recurrent set equals \(\mathcal S\), and the exact fixed/two-cycle counts follow by counting diagonal and off-diagonal ordered pairs of core words.

**3. Exact entry-time census.** Each recurrent state is in \(\mathcal S\), hence exactly \(2^{2k}\) initial states have entry time zero. All others have entry time one. There are \(2^{k+M}\) initial configurations in total. The stated fraction and its edge-count specialization follow from \(M=\sum_v (d_H(v)+1)=k+2|E|\) at the minimum allowed mantle.

**4. Exact basin fibres.** Fix initial core word \(a\). Choose arbitrary bits on the \(m_v\) initial leaves at each \(v\), and let \(j\) be their number of ones. The core output bit at \(v\) after one update is exactly \(J_v(a,j)\), including its equality/tie case. There are \(\binom{m_v}{j}\) assignments of that leaf block. Once \(a\) is fixed, the initial choices in distinct leaf blocks are independent, and the core output word \(b\) has exactly \(W(a,b)\) preimages. Every one of these preimages maps to \(z(b,a)\) in one update. It therefore enters the fixed state \(z(a,a)\) when \(a=b\), or the unordered two-cycle \(\{z(a,b),z(b,a)\}\) when \(a\ne b\). The two phases have disjoint initial-core conditions, hence their weights add, proving the individual basin formulas. Moreover, for every \(a,b\) the choice of an all-\(b_v\) initial leaf block makes the output \(b_v\) by strict domination, so \(W(a,b)\ge1\). All attractors are therefore realized by nonempty basins.

**5. Sharp local leaf threshold.** The strict inequality is necessary for guaranteed domination of the core neighbourhood vote by its leaf block: with \(m_v=d_H(v)\), choosing opposite homogeneous votes among the core and leaf neighbours produces a tie, and the retained core bit can oppose the leaf block. It is not claimed that every such smaller mantle loses the one-step identity. For a concrete failure of the general theorem under the relaxed uniform condition, take \(H=K_2\) and attach one leaf to each core vertex. In the vertex order (core 0, core 1, its two private leaves), the initial word \((0,1,0,0)\) follows
\[
(0,1,0,0)\to(0,0,0,1)\to(0,0,0,0)\to(0,0,0,0),
\]
so its first image is not periodic and \(F^3\ne F\).

**6. Small exact example.** On the double star with one edge joining two core vertices and two private leaves at each, there are four fixed states with basin sizes \(9,9,1,1\). Its six two-cycles have basin sizes \(18,6,6,6,6,2\). The ten basins sum to all \(64\) labelled configurations. Thus the core graph affects basin weights even though all recurrent orbit counts are topology-independent.

## Verification

The proof is exact for all finite cores; computation is independent corroboration rather than extrapolation. `verify_exhaustive.py` directly constructs full neighbour lists and verifies \(F^3=F\), the complete fibre weights \(W(a,b)\), the recurrent-state count and positive fibres for every initial state of all labelled core graphs on one through three vertices with each mantle equal to its minimum or one more, plus four selected four-vertex cores. It reports `EXHAUSTIVE_OK cases=78 initial_states=1363612`; output is included in `verify_exhaustive_output.txt`.

`verify_orbits.py` independently encodes states as tuples of named vertices, follows full trajectories, identifies the distinct attractor orbits and their individual empirical basins, and checks the global period and first-entry counts on six test networks (including a four-vertex star and path); it reports `ORBIT_VERIFY_OK cases=6 states=37956`. Its output includes a concrete failing boundary configuration and is in `verify_orbits_output.txt`. Reproduce using `python3 verify_exhaustive.py` and `python3 verify_orbits.py`, with Python's standard library only.

## Relationship to prior work

Goles and Olivos proved eventual period at most two for finite symmetric threshold systems [1]. Benjamini and coauthors [2] explain that framework and study majority convergence on unimodular and random graphs. Neither theorem fixes a one-step entry time or counts basins in the arbitrary leaf-dominant class.

Benjamini, Zakharov and Zhukovskii [3, Section 3.1] identify *passive* vertices in finite odd-degree trees whose opinions are already two-step-stationary. That local mechanism overlaps with the strict pendant majority used here; therefore the tree-case periodicity mechanism is **not** claimed as novel in isolation. Their work is restricted to trees and odd degrees and does not give the graph-independent complete recurrent orbit count or the full basin-fibre formula for arbitrary core graphs, including those with cycles.

The published result [4] for a single pendant leaf on every degree-at-most-two core gives a uniform two-step cutoff \(F^4=F^2\), rather than the present one-step involution or an individual-basin formula. The clique-corona classification [5] handles one private leaf per clique vertex and a distinct parity-sensitive regime. Those results are relevant but neither covers the degree-dominating multilayer mantles over arbitrary core graphs. Previous exact basin enumerations for particular graphs likewise do not assert the topology-independent involution plus the universal binomial product.

## Limitations

The theorem requires a private leaf surplus at **every** core vertex; it does not classify graphs with lower leaf multiplicities, or randomized, asynchronous, weighted and non-binary updates. The boundary example shows that dropping the uniform condition can fail but does not establish a converse for each possible core. The basin formula can require exponentially many evaluations to list all basins for large cores, despite being exact and locally factorized. Available published-source and indexed-record comparisons leave residual risk of an unindexed equivalent in threshold-network or cellular-automaton terminology. No independent external validation has been performed.

## References

[1] E. Goles and J. Olivos, "Periodic behaviour of generalized threshold functions," *Discrete Mathematics* **30** (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.

[2] I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, "Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs," arXiv:1405.2486v1, publicly posted 2014-05-11, https://arxiv.org/abs/1405.2486.

[3] I. Benjamini, G. Zakharov and M. Zhukovskii, "Majority Dynamics on Finite Trees," *Random Structures & Algorithms* **69** (2026), e70092, https://doi.org/10.1002/rsa.70092.

[4] "Uniform two-step periodicity for majority dynamics on degree-two leaf coronas," https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-uniform-two-step-periodicity-for-majority-dynamics-on-degree-two--830f30f39271/RESULT.md.

[5] "Exact parity-split recurrence and three-step stabilization on clique coronas," https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-exact-parity-split-recurrence-and-three-step-stabilization-on-cl--40e5470e6eb4/RESULT.md.
