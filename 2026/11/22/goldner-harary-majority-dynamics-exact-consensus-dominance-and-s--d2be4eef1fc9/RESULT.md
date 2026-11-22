# Goldner–Harary majority dynamics: exact consensus dominance and seven oscillation symmetries

## Finding

Let \(G\) be the eleven-vertex Goldner–Harary graph, with the vertex labels and 27 undirected edges given by the Sage `GoldnerHararyGraph` edge dictionary reproduced in `verify_transition.py`. For synchronous binary open-neighbor majority with tie retention, the complete dynamical map \(F:\{0,1\}^{11}\to\{0,1\}^{11}\) has exactly **two fixed configurations**, namely the constant configurations, and **47 primitive temporal two-cycles**. Every configuration is periodic after at most four updates, sharply:

\[
F^{6}=F^{4},\qquad F^{5}\ne F^{3}.
\]

Each unanimous fixed point attracts exactly **935** of the \(2^{11}=2{,}048\) initial configurations. The 47 primitive two-cycles have individual basin sizes **2** (27 cycles), **6** (18 cycles), and **8** (two cycles). Consequently, the exact consensus-attraction fraction under uniform initial states is \(935/1024\), while the oscillatory-attraction fraction is \(89/1024\). The entrance-time census for first arrival on the eventual period-one or period-two orbit is:

| First entrance time \(t\) | \(0\) | \(1\) | \(2\) | \(3\) | \(4\) |
|---|---:|---:|---:|---:|---:|
| Number of initial configurations | 96 | 742 | 850 | 324 | 36 |

The graph has 12 automorphisms, under which the 47 temporal two-cycles fall into **seven** spatial-equivalence classes of cardinalities \(2,3,6,6,6,12,12\). The two fixed configurations form separate symmetry classes.

## Assumptions and scope

The vertex set is \(V=\{0,1,\ldots,10\}\), indexed exactly by the named graph constructor in the cited Sage graph-generator source. The graph is undirected, simple and loopless; its degree multiset is six vertices of degree three, two of degree six, and three of degree eight. A state \(x\) is encoded by the integer \(\sum_{i=0}^{10}2^{i}x_i\), where \(x_i\in\{0,1\}\). At each synchronous step, vertex \(i\) adopts 1 when more than half of its open neighbors have state 1; adopts 0 when fewer than half have state 1; and otherwise retains \(x_i\). All statements concern this deterministic labelled finite system, not random sequential majority voting or a general class of planar graphs.

A primitive temporal two-cycle is an unordered pair \(\{u,v\}\) with \(F(u)=v\ne u\) and \(F(v)=u\). Its basin consists of all initial states that eventually enter that pair. The first-entry time is the minimum nonnegative \(t\) such that \(F^t(x)\) lies on its eventual cycle. Spatial equivalence identifies cycles under automorphisms of \(G\), allowing interchange of the two temporal phases.

## Proof

The proof is a finite exhaustive classification with two logically distinct implementations and a complete machine-readable basin catalog.

**Finite domain and exact transition.** `verify_transition.py` constructs the eleven adjacency bitmasks from the finite Sage edge dictionary and for each integer state \(x\in\{0,\ldots,2047\}\) computes every output bit by an integer comparison of twice its active-neighbor count with the vertex degree. Therefore `NEXT` contains exactly the image of every state under the specified rule, with no sampling or rounding.

**Exhaustive functional digraph.** Every state has exactly one outgoing arc. The program removes all indegree-zero states until only directed cycles remain. This removes exactly the nonperiodic states: a vertex on a directed cycle never has indegree zero during peeling, whereas every other vertex in a finite functional digraph lies in a directed in-tree feeding a cycle and is eventually peeled. Reading the removal list backward assigns each transient vertex the cycle of its successor and an entry depth one larger than its successor's. This exhausts all 2,048 states, assigns every state exactly one eventual cycle and counts each basin by integer summation. The resulting 49 orbit records appear individually in `basin_catalog.csv`, whose rows are checked by both independent programs. Their orbit periods, basin sizes and entry depths establish every numerical statement above. In particular, there are exactly 36 depth-four states, so the worst-case bound is attained. One explicit trajectory, in the specified integer encoding, is \(179\to119\to51\to49\to0\), first reaching its fixed point at update four.

**Global identity.** The finite digraph contains only cycles of periods one and two and every state has entry depth at most four, so \(F^6=F^4\) pointwise on the entire state space. The depth-four witness proves \(F^5\ne F^3\), and direct integer assertions verify both statements on all states.

**Spatial classes.** `verify_symmetry.py` enumerates every possible degree-preserving permutation, checks adjacency preservation on all 27 edges, and obtains exactly 12 graph automorphisms. Commutation \(F(gx)=gF(x)\) is verified for every initial state and all 12 permutations. Applying these permutations to the 49 recurrent temporal orbits yields two singleton fixed-point classes and seven two-cycle classes of sizes \(2,3,6,6,6,12,12\).

## Verification

Run from the directory containing the delivered source files and `basin_catalog.csv` with Python 3.10 or later:

```sh
python3 verify_transition.py
python3 verify_trajectories.py
python3 verify_symmetry.py
```

`verify_trajectories.py` independently specifies all 27 edges rather than importing the transition implementation, uses signed-neighbor votes rather than bit counts, and traces every state until its first repeated state. It independently recovers the same cycle keys, exact basin catalog and sharp entry bound. The symmetry program independently reconstructs adjacency from a separate edge list. The three checkers require only the Python standard library. The 49-row data file lists each recurrent cycle, with `phase0` and `phase1` the smaller and larger integer state, its exact period and individual basin size. For a fixed point the two phases coincide.

## Relationship to prior work

The finite period-at-most-two theorem of Goles and Olivos is discussed by Benjamini, Chan, O'Donnell, Tamuz and Tan (2014, arXiv:1405.2486v1, Section 1), but that theorem supplies no exact Goldner–Harary entrance times, orbit counts, or basin sizes. Lima, Moreira and Araújo (arXiv:1205.5297v1, 2012) study stochastic majority-vote dynamics on much larger Apollonian networks, measuring a noise-driven phase transition; their model updates spins with stochastic flip probabilities rather than the deterministic synchronous map considered here. This difference is material even though the Goldner–Harary graph is a planar 3-tree and hence an Apollonian network. The named graph and its explicit labelled edges are specified in the Sage graph-generator source; it supplies graph structure, not the dynamical census. These sources, together with searches for exact values, synonyms and broader covering results, did not yield an implication of the classification above; absence from indexed sources is not proof of absolute historical novelty.

## Limitations

This is a complete finite theorem only for the specified Goldner–Harary graph and synchronous binary tie-retaining rule. It does not claim analogous basin concentration for all maximal planar graphs, all 3-trees, or all Apollonian networks, nor any stochastic consensus law. Exhaustive verification covers the full stated finite domain but is not a formal proof inside a proof assistant. Publication-priority searches cannot rule out an unindexed earlier computation. Independent external validation has not been performed.

## References

1. A. Goldner and F. Harary, “Note on a smallest nonhamiltonian maximal planar graph,” *Bulletin Malaysian Mathematical Sciences Society* 6(1) (1975), 41–42. Bibliographic description: https://mathworld.wolfram.com/Goldner-HararyGraph.html .
2. Sage graph-generators source, `GoldnerHararyGraph`, edge dictionary in `smallgraphs.py`: https://sources.debian.org/src/sagemath/10.10-3/src/sage/graphs/generators/smallgraphs.py (function definition).
3. F. W. S. Lima, A. A. Moreira and A. D. Araújo, “Non-nequilibrium model on Apollonian networks,” arXiv:1205.5297v1, first publicly posted 2012-05-23. https://arxiv.org/abs/1205.5297 .
4. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486v1, first publicly posted 2014-05-11. https://arxiv.org/html/1405.2486v1 .
5. E. Goles and J. Olivos, “Comportement périodique des fonctions à seuil binaires et applications,” *Discrete Applied Mathematics* 3 (1981), 93–105, DOI:10.1016/0166-218X(81)90034-2.
