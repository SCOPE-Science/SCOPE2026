# Exact three-agent action budgets for binary common refinements of effectivity partitions

## Finding

Let \(U\) be a nonempty finite set of outcomes and let \(\mathcal P_a\), for \(a\in\{1,2,3\}\), be a partition of \(U\) into nonempty blocks. Assume that **every** joint intersection
\[
C_{ijk}=P_{1,i}\cap P_{2,j}\cap P_{3,k}
\]
is nonempty and has cardinality \(1\) or \(2\). For each block \(P_{a,i}\), prescribe a positive integer \(b_{a,i}\) of distinguishable actions of agent \(a\) whose exact set of possible outcomes is that block.

**Exact action-budget criterion.** A deterministic three-agent simultaneous-action outcome table with precisely these actions and exact effectivity families \(\mathcal P_1,\mathcal P_2,\mathcal P_3\) exists **if and only if**, for every joint intersection of size two,
\[
\boxed{\#\{a\in\{1,2,3\}:b_{a,i_a}\ge2\}\ge2.}
\]
Intersections of size one impose no further condition. The criterion classifies all positive integer budget vectors, not just a sufficient equal-copy bound.

**Sharp simultaneous minimum.** Define a finite undirected graph \(H\) with a distinct vertex \((a,i)\) for each block of each partition. Each doubleton joint intersection contributes the three edges of a triangle on its three block-vertices; singleton intersections add no edges. Write \(N=|\mathcal P_1|+|\mathcal P_2|+|\mathcal P_3|\), and let \(\tau(H)\) and \(\alpha(H)\) be the minimum vertex-cover size and maximum independent-set size. Then the minimum total number of actions over all exact deterministic realizations is
\[
\boxed{\min\sum_{a=1}^{3}\sum_i b_{a,i}=N+\tau(H)=2N-\alpha(H).}
\]
Every minimum cover furnishes an optimal vector: give two actions to its block-vertices and one to all other blocks. Conversely, the set of doubled block types in any optimal vector is a minimum cover, and every optimal vector uses only one or two actions per block type.

For example, when each partition has two blocks and seven of the eight joint intersections are singleton while one is doubleton, the exact minimum is \(8\) actions: the graph has one triangle and three isolated vertices, so \(N=6\), \(\tau(H)=2\). This is an instance-sensitive optimization, not a claim that all three agents need uniform copy factors.

## Assumptions and scope

At one local state a deterministic game is a function \(o:A_1\times A_2\times A_3\to U\), where each \(A_a\) is a finite nonempty set of agent-\(a\) actions. Its actual-effectivity neighborhood of action \(s\in A_a\) is
\[
E_a(s)=\{o(s_1,s_2,s_3):s_a=s,\ s_j\in A_j\text{ for }j\ne a\}.
\]
The specified families mean that the **set** of values \(E_a(s)\), over all agent-\(a\) actions, equals \(\mathcal P_a\), and exactly \(b_{a,i}\) actions have value \(P_{a,i}\). Distinct actions may have the same effectivity neighborhood. No outcome outside \(U\) is permitted, and every action profile has one outcome.

The partitions may contain different numbers of blocks. Their joint refinement is transverse (every triple cell nonempty) and binary (all joint cells have at most two elements). Both conditions are substantive: the proof uses the uniqueness of a block of each partition containing a given outcome and the two-coloring of doubleton cells. The theorem is local; separate local representations may be combined state by state. It makes no assertion about coalitional actual effectivity, general overlapping neighborhood families, or cells with three or more outcomes.

## Proof

**1. A cellwise necessary capacity.** Fix indices \((i,j,k)\) for a doubleton cell \(C_{ijk}=\{u,v\}\). Suppose at most one of \(b_{1,i},b_{2,j},b_{3,k}\) exceeds one; if there is such an agent, choose it as \(a\), otherwise choose any agent. Fix one action \(s\) of agent \(a\) with the indicated block. In order for its exact neighborhood to contain **both** \(u\) and \(v\), there must be action completions producing these distinct outcomes. Since each \(\mathcal P_h\) partitions \(U\), an opponent action that can produce either \(u\) or \(v\) must have the unique block \(P_{h,i_h}\) containing that outcome. Both opponents have only one action of their respective indicated types, so at most one complete profile with \(s\) can have outcome in \(C_{ijk}\). The two required outcomes cannot both occur. Thus at least two of the three multiplicities must be at least two.

This argument also shows why a multiplicity increase for only one agent cannot supply the necessary coverage: fixing one of that agent's actions destroys its own variability. It uses no assumptions about the outcomes in other joint cells.

**2. Constructing every feasible budget vector.** For each action type \((a,i)\), index its copies by \(t=0,\ldots,b_{a,i}-1\). Consider a triple of chosen types \((i,j,k)\). The output of every profile with these types must belong to \(C_{ijk}\).

If \(|C_{ijk}|=1\), always output its unique member. Otherwise label the two outcomes of the cell \(u_0,u_1\), and choose any two distinct agents \(p,q\) with \(b_{p,i_p},b_{q,i_q}\ge2\), guaranteed by the criterion. For a profile whose copy indices are \((t_1,t_2,t_3)\), set
\[
o((i,t_1),(j,t_2),(k,t_3))=u_{(t_p+t_q)\bmod2}.
\]
(The symbols \(u_0,u_1\) are chosen separately in each cell.) Since each chosen copy-index range includes \(0\) and \(1\), the parity of either index can be varied while holding all other indices fixed.

Fix any agent \(a\), any of its actions \((i_a,t_a)\), and any point \(u\in P_{a,i_a}\). The other two partitions determine unique blocks containing \(u\), so \(u\) lies in a unique joint cell of three types with the fixed type of agent \(a\). If the cell is singleton, every profile using those types outputs \(u\). If the cell is doubleton, at least one of the two agents \(p,q\) used in its output formula differs from \(a\). Varying that agent's copy index between zero and one changes the output between \(u_0\) and \(u_1\) while leaving the fixed action unchanged. In either case \(u\) appears in \(E_a(i_a,t_a)\). Conversely every output under the fixed action belongs to its block, by the cell containment. Consequently \(E_a(i_a,t_a)=P_{a,i_a}\) for all agents and action copies. This proves sufficiency, including arbitrary multiplicities greater than two.

**3. Exact optimum.** Let \(D\) be the set of block-vertices with \(b_{a,i}\ge2\). A doubleton cell imposes at least two vertices of its triangle in \(D\), equivalently \(D\) meets each edge of that triangle. Thus the budget criterion is exactly \(D\) being a vertex cover of \(H\). Every positive-integer vector costs at least \(N+|D|\ge N+\tau(H)\). Conversely, if \(D\) is a minimum vertex cover, set \(b_{a,i}=2\) on \(D\) and \(b_{a,i}=1\) outside. The construction in step 2 realizes this choice with exactly \(N+\tau(H)\) actions. If an optimal vector had any entry exceeding two, reducing that entry to two would preserve the criterion and lower the cost. Hence all optimum entries are one or two, and their doubled vertices necessarily form a minimum cover. Finally \(\tau(H)=N-\alpha(H)\) is the standard complement relation between vertex covers and independent sets on the same finite graph.

## Verification

The bundled Python standard-library program `verify.py` builds the complete outcome table and checks the **full** possible-outcome set of each individual action against its requested partition block, independently of the proof's symbolic argument. It performs the following finite checks:

- Exhaustive evaluation of binary-valued three-dimensional action tables with each multiplicity in \(\{1,2\}\), independently confirming the exact feasible multiplicity patterns for a doubleton cell.
- Every one of the \(256\) singleton/doubleton patterns for a \(2\times2\times2\) joint refinement. For each, it finds a minimum vertex cover by exhaustive subset enumeration, reconstructs the optimizing game table, checks all exact action neighborhoods, and enumerates all \(64\) possible doubled-type subsets to compare the graph-cover criterion against the direct two-per-cell criterion. The computed minimum cover sizes are distributed as \(1,20,58,177\) patterns for cover sizes \(0,2,3,4\), respectively.
- A fixed-seed sample of \(800\) heterogeneous instances with one through three blocks per partition and positive action multiplicities up to four; \(565\) satisfy the exact criterion and all \(565\) reconstructed games pass per-action neighborhood comparison.

Run `python3 verify.py` with Python 3 and no third-party packages. The expected output begins `VERIFY_OK local_exact=8 masks=256`. These finite checks are corroboration, not a substitute for the all-finite theorem proved above.

## Relationship to prior work

Ciardelli's *Inquisitive Action Logic* (arXiv:2606.31866, 2026) gives necessary and sufficient qualitative conditions for finite neighborhood families to come from a concurrent game. It does not determine exact local action multiplicities or their optimal total for an individual frame. The assumption of nonempty transverse cells places the present partitions inside the representable class.

The published *Exact action profiles for partition-valued two-agent effectivity* (2026) gives the full copy-budget region for **two** agents and arbitrary partition-intersection cardinalities. Its cell-rectangle argument and lower bounds require two agents; it does not cover three-agent cells, for which the exact two-copied-types condition replaces both-sided multiplicity lower bounds. The present result is not inferred by treating the third agent's actions as a second-agent block, since that would lose the requirement for each third-agent action to realize its own block.

The published *Exact heterogeneous action-budget region for finite actual-effectivity representations* (2026) determines action counts **uniform over all neighborhoods of a fixed agent** that work for every frame of a given outcome-range size, rather than the exact instance-sensitive one-copy/two-copy pattern for each partition block. *Chromatic compression of finite actual-effectivity action representations* (2026) gives a sufficient bound, uniform within each agent's family, using a conflict-graph coloring. Neither gives the graph-theoretic necessity or the sharp minimum cover expression here. The elementary vertex-cover identity and parity-based two-symbol array are not claimed to be new in isolation; the new assertion is their exact relation to simultaneous-action realization and optimal per-block resources in the stated class.

Chen, Ju and Ågotnes (2026) treat representation of actual powers for two agents, not these three-agent local action-copy budgets. Older game-form and three-way array terminology could encode an equivalent theorem; the historical-priority comparison is necessarily provisional.

## Limitations

The theorem requires exactly three agents, partition-valued individual neighborhood families, full transversality, and joint cells of size at most two. It does not give optimal budgets for larger joint cells, overlapping neighborhoods, nondeterministic actions, or coalitional outcome abilities. Computing \(\tau(H)\) is an exact finite combinatorial optimization prescription, not a polynomial-time algorithm guarantee. The proof is self-contained, but independent specialist review and exhaustive historical-priority certification have not been performed.

## References

1. Ivano Ciardelli, *Inquisitive Action Logic*, arXiv:2606.31866v1, first posted 2026-06-30, Section 2 and Theorem 2.2. https://arxiv.org/html/2606.31866
2. *Exact action profiles for partition-valued two-agent effectivity*, mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-action-profiles-for-partition-valued-two-agent-effectivity--ab8e933d61f4
3. *Exact heterogeneous action-budget region for finite actual-effectivity representations*, mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-heterogeneous-action-budget-region-for-finite-actual-effec--e6ecbe7ccc64
4. *Chromatic compression of finite actual-effectivity action representations*, mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-chromatic-compression-of-finite-actual-effectivity-action-repres--fdd82819f033
5. Zixuan Chen, Fengkui Ju and Thomas Ågotnes, *Representation Theorems for Actual Powers over Two-Agent General Concurrent Game Frames*, arXiv:2610.15476 (2026). https://arxiv.org/abs/2610.15476
