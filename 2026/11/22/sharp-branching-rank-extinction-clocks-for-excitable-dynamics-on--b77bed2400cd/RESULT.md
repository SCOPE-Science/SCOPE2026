# Sharp branching-rank extinction clocks for excitable dynamics on forests

## Finding
Let \(F\) be a nonempty finite forest, \(\theta\ge2\) an integer contact threshold, and \(\kappa\ge3\) an integer number of states. In the synchronous \(\kappa\)-state Greenberg–Hastings process, a vertex at rest (state \(0\)) becomes excited (state \(1\)) when at least \(\theta\) distinct neighbors are excited; otherwise it stays at rest. Each positive state advances by one modulo \(\kappa\) at every update.

Define \(H_\theta(F)\) to be the greatest height of a rooted complete \(\theta\)-ary tree occurring as a (not necessarily induced) subgraph of \(F\), with height zero for a single vertex. If \(\tau(x)\) denotes the first update time when the entire trajectory from initial configuration \(x\) is at rest, then
\[
\boxed{\max_{x\in\{0,\ldots,\kappa-1\}^{V(F)}}\tau(x)=H_\theta(F)+\kappa-1.}
\]
For every integer \(n\ge1\), maximization also over all forests on \(n\) vertices yields the sharp, attained size-only law
\[
\boxed{\max_{|V(F)|=n}\max_x\tau(x)=\kappa-2+\left\lfloor\log_\theta\bigl((\theta-1)n+1\bigr)\right\rfloor.}
\]
Equivalently, a vertex excited at update \(t\) certifies \(\sum_{j=0}^{t}\theta^j\) distinct vertices in a complete branching witness contained in its component. The complete shape-sensitive clock is computable by a finite postorder recurrence.

## Assumptions and scope
Graphs are finite, undirected, simple and acyclic, with any number of components, and at least one vertex. States belong to \(\{0,1,\ldots,\kappa-1\}\). At each simultaneous update, \(1\to2\to\cdots\to\kappa-1\to0\) automatically. A vertex currently in state \(0\) changes to state \(1\) if and only if at least \(\theta\) *distinct* adjacent vertices currently have state \(1\). There is no stochastic updating. Time \(t=0\) is the initial state; \(\tau(x)=0\) for the all-rest state, and is otherwise the first \(t\) with all vertices at rest. Once all rest, the configuration stays at rest.

The height of the one-vertex rooted tree is \(0\). The complete \(\theta\)-ary tree of height \(h\) has every internal vertex equipped with exactly \(\theta\) rooted children and exactly \(\sum_{j=0}^{h}\theta^j=(\theta^{h+1}-1)/(\theta-1)\) vertices. Additional edges or vertices in the ambient forest do not matter to its existence. The term *branching rank* refers only to this explicitly defined height invariant, not to a claim of equivalence with any unqualified version of a classical Strahler number.

## Proof
**1. Excitation entails a complete branching witness.** If \(x_t(v)=1\) and \(t\ge1\), then at time \(t-1\) the vertex was at rest and at least \(\theta\) distinct neighbors of \(v\) were excited. An excited vertex at time \(s\) cannot also have been excited at time \(s-1\) or \(s-2\): its two immediate successor states are \(2\) and either \(3\) or \(0\), never \(1\), since \(\kappa\ge3\).

Starting from an excitation \((v,t)\), recursively select \(\theta\) different excited-neighbor events one time earlier at each positive time until time zero. Along any resulting backward temporal chain, immediate spatial reversal would require the same vertex to be excited at times separated by two, which is impossible. Thus each backward chain is a nonbacktracking walk. In a forest every nonbacktracking walk is a simple path; in particular, branches arising from distinct selected neighbors cannot reconverge, and a branch cannot reenter an ancestor. Consequently the selected events occupy pairwise distinct spatial vertices and form an embedded rooted complete \(\theta\)-ary tree of height \(t\), rooted at \(v\). Therefore \(t\le H_\theta(F)\), and in fact its component contains at least \((\theta^{t+1}-1)/(\theta-1)\) vertices.

**2. Universal extinction.** Put \(H=H_\theta(F)\). No vertex can be excited at any time \(t>H\). Every previously excited vertex passes through precisely \(\kappa-2\) refractory states and is at rest \(\kappa-1\) updates after its last excitation; initially refractory vertices clear no later. Thus every configuration is all-rest by time \(H+\kappa-1\). This proves the upper bound for the fixed forest.

**3. Attainment on every forest shape.** Select a rooted complete \(\theta\)-ary subtree of height \(H\). Give its depth-\(H\) leaves state \(1\), and give every other vertex of \(F\) state \(0\). At time \(j\), exactly the vertices at depth \(H-j\) of the selected subtree are excited for \(0\le j\le H\). Indeed, at each step precisely the parents of the previous excited level receive \(\theta\) excited children. No other vertex receives \(\theta\) excited neighbors: downward branches have no second incoming excitation, and an ambient component outside the selected subtree is attached to it along at most one edge because the graph is acyclic. The root is therefore excited at time \(H\), and remains nonzero through time \(H+\kappa-2\). By step 2 all vertices are zero at \(H+\kappa-1\), so the bound is attained. This argument includes \(H=0\).

**4. Sharp size law.** For a forest with \(n\) vertices, the witness in step 1 implies \((\theta^{H+1}-1)/(\theta-1)\le n\). Hence
\[
H\le\left\lfloor\log_\theta((\theta-1)n+1)\right\rfloor-1.
\]
Let the right side be \(h\). A complete \(\theta\)-ary tree of height \(h\) has at most \(n\) vertices. Add the remaining vertices as a pendant path at one of its leaves, producing an \(n\)-vertex tree. The full subtree still exists, so its branching rank is at least \(h\); the size inequality makes it at most \(h\). Step 3 attains extinction time \(h+\kappa-1\), which is the displayed formula.

**5. Computability.** For an oriented tree edge \(v\mid p\), define \(h(v\mid p)\) as the largest complete \(\theta\)-ary height at \(v\) in the component obtained by excluding the neighbor \(p\). List the values \(h(u\mid v)\), over neighbors \(u\ne p\), in nonincreasing order. If fewer than \(\theta\) such neighbors exist, \(h(v\mid p)=0\); otherwise it equals one plus their \(\theta\)-th largest value. A rerooting or message-passing calculation evaluates these finite recurrences and then takes \(H_\theta(F)=\max_v h(v\mid\bot)\) over all components. This is a concrete graph invariant determined before selecting initial colors.

## Verification
The standalone program `verify_exhaustive.py` enumerates every initial state on every unlabelled tree through nine vertices in its largest test regime, with five threshold/state-count regimes, and compares the measured maximum first-rest time against the complete-subtree recurrence. It checked \(241\) tree-and-parameter cases comprising \(1{,}882{,}829\) full trajectories, and all assertions passed. The second standalone program `verify_witness.py` builds actual complete-branching witness initial states using an independent adjacency-list recurrence, checks their precise last-excitation and all-rest times, and checked \(8{,}896\) complete-tree and randomly generated tree instances for thresholds \(2,3,4,5\) and state counts \(3,4,5,6\). The recorded outputs appear in `verification_output.txt`.

To reproduce with Python 3 and NetworkX, run `python3 verify_exhaustive.py` and `python3 verify_witness.py` in a directory containing the packaged scripts; the second requires only Python's standard library. The exact all-forest theorem is established by the proof, not inferred from finite experiments. No statement is made about graphs with cycles, threshold one, or fewer than three states.

## Relationship to prior work
Fisch, Gravner and Griffeath's 1993 threshold-range preprint studies generalized excitable cellular automata on lattices, giving an archival model source rather than a tree-specific exact clock. Gravner, Lyu and Sivakoff (2016) analyze three-state single-contact excitation on arbitrary graphs and finite-tree synchronization, not the multi-contact branching-rank law. Bello and Sivakoff (2021), Lemma 2.7(ii), prove for threshold at least two that a rooted tree of depth \(d\) is all-rest by time \(d+\kappa\); their statement does not identify the sharp maximum time on an arbitrary forest or the complete \(\theta\)-ary witness invariant. For example, long paths have \(H_2=1\) and exact maximum time \(\kappa\), while a depth-based bound grows with length.

A published finite-graph density-obstruction theorem, *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics* (2026), bounds the total number of excitation events under \(\rho(G)<\theta\). Every forest satisfies this inequality when \(\theta\ge2\), but its event budget does not imply the sharp logarithmic size clock or its shape-by-shape equality. Doba's 2018 finite-graph analysis assumes one excited neighbor suffices for activation; it covers different dynamics. These comparisons do not rule out unindexed equivalent tree-specific arguments.

## Limitations
The graph must be a forest; causal branches can recombine across cycles. The refractory separation argument uses \(\kappa\ge3\), and the exponential growth of witnesses uses \(\theta\ge2\). The result is an exact worst-case transient theorem, not a probability distribution of extinction times, nor a fixed-initial-state formula. The extremizing configuration is explicit, but not asserted unique. Published literature was searched by aliases and implication comparisons, with residual risk of an earlier equivalent bound in unindexed work. Independent expert validation has not been performed.

## References
1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001 (first publicly posted 1993-04-02), https://arxiv.org/abs/patt-sol/9304001.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (2016-10-24), https://arxiv.org/abs/1610.07320.
3. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees*, arXiv:2108.06404 (2021-08-13), especially Lemma 2.7, https://arxiv.org/abs/2108.06404.
4. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126, https://doi.org/10.25088/ComplexSystems.27.2.101.
5. *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics*, public research record dated 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-densest-subgraph-threshold-and-finite-excitation-budget-for-th--352367f51e91.
