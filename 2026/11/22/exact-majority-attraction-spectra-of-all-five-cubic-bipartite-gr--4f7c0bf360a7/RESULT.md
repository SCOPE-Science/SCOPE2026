# Exact majority attraction spectra of all five cubic bipartite graphs on twelve vertices

## Finding

Let \(G\) range over **all connected simple cubic bipartite graphs on twelve vertices**, up to unlabelled graph isomorphism. There are exactly five such graphs. For synchronous binary strict neighbor majority \(F_G:\{0,1\}^{12}\to\{0,1\}^{12}\), every one of the \(2^{12}=4096\) states satisfies the **sharp universal identity**

\[
F_G^4(x)=F_G^2(x).
\]

Consequently the first time \(\tau_G(x)=\min\{t\geq0:F_G^{t+2}(x)=F_G^t(x)\}\) is at most two, and for **each** of the five graphs some state has \(\tau_G(x)=2\). No periodic orbit has prime length other than one or two.

The complete counts of initially recurrent states, fixed configurations, primitive two-cycle orbits and eventual two-cycle basins are as follows. Each \(B_i\) is specified canonically by its six binary biadjacency row masks in `GRAPH_DATA.json`. A row mask has bit \(j\) set exactly when its left vertex is adjacent to right vertex \(j\), counting from zero.

| Graph | Number of squares | Fixed configurations | Primitive two-cycle orbits | Initial states eventually in two-cycles | Largest individual attractor basin |
|---|---:|---:|---:|---:|---:|
| \(B_1\) | 10 | 4 | 6 | 3072 | 512 |
| \(B_2\) | 6 | 10 | 45 | 3384 | 576 |
| \(B_3=C_6\square K_2\), the hexagonal prism | 6 | 22 | 231 | 3516 | 512 |
| \(B_4\) | 4 | 14 | 91 | 3372 | 648 |
| \(B_5\), the Franklin graph | 3 | 16 | 120 | 3312 | 722 |

Here a *basin* is the set of initial configurations eventually reaching one specified attractor orbit, not merely one phase of it. The final column is its maximum cardinality. The complete multiset of basin sizes (all fixed points and two-cycle orbits) is provided for every graph in `GRAPH_DATA.json`, rather than just the maxima.

The exact first-entry census is displayed in the following table: each cell gives \((N_{t,1},N_{t,2})\), where \(N_{t,p}\) counts initial configurations with first periodic-entry time \(t\) and eventual least period \(p\).

| Graph | \(t=0\) | \(t=1\) | \(t=2\) |
|---|---|---|---|
| \(B_1\) | (4,12) | (412,1172) | (608,1888) |
| \(B_2\) | (10,90) | (222,1038) | (480,2256) |
| \(B_3\) | (22,462) | (246,1974) | (312,1080) |
| \(B_4\) | (14,182) | (150,950) | (560,2240) |
| \(B_5\) | (16,240) | (144,1200) | (624,1872) |

The hexagonal prism uniquely maximizes both the number of primitive two-cycle orbits (231) and the uniform-initialization probability of eventual oscillation (\(3516/4096=879/1024\)) among these five graphs. Yet \(B_2\) and the prism both have six squares and very different periodic-state populations, so the square count is not sufficient to determine the majority dynamics. The Franklin graph, having only three squares, instead uniquely maximizes the size of the largest individual basin (722).

## Assumptions and scope

Graphs are finite, undirected, loopless and simple; *cubic* means every degree is exactly three. A connected cubic bipartite twelve-vertex graph has two bipartition shores of six vertices, because its three edges at each vertex count equally on both sides. All initial binary configurations are labelled by vertices, even though graphs are classified up to isomorphism. The simultaneous update satisfies

\[
(F_G(x))_v=1\quad\Longleftrightarrow\quad\sum_{w\sim v}x_w\geq2.
\]

Because each degree is odd, ties never arise. \(\tau_G(x)\) is the *first* periodic-entry time: \(\tau=0\) means already periodic. The least eventual period is determined at time \(\tau\), not from the initial state when \(\tau>0\). These counts do not assert a uniform bound for cubic bipartite graphs of arbitrary order.

## Proof

**Step 1: exhaust all graph isomorphism classes.** Label the two shores \(0,\ldots,5\) and \(6,\ldots,11\). A graph is a \(6\)-tuple of masks between zero and 63 with three set bits per row and exactly three set bits in each of the six columns. Given any such graph, choose a left vertex and send its three right neighbors to \(6,7,8\). Its row mask becomes seven. Permuting the other five left vertices puts their masks in nondecreasing order. Therefore every isomorphism type is represented in the finite enumeration of `check_classification.py`: choose five further masks *with repetition* from the twenty weight-three masks, enforce all six column sums, and retain connected matrices. Exactly 147 matrices survive. A connected bipartite graph has a uniquely determined bipartition up to exchanging shores. Thus two matrices are isomorphic if and only if one can be obtained from the other through permutations of left and right labels, optionally followed by transpose. Exhaustive canonicalization over all \(6!\) column permutations, sorted rows and both shore orientations leaves exactly the five canonical row tuples listed in `GRAPH_DATA.json`. The script verifies the standard identifications of \(B_3\) with the hexagonal prism and \(B_5\) with the Franklin graph by explicit graph isomorphisms.

**Step 2: exhaust every orbit for each canonical graph.** On each of the five representatives, encode \(x\) by the integer whose binary digits are the twelve vertex states. Form the exact transition array of length 4096, using the neighbor-mask formula

\[
F_G(x)=\sum_{v=0}^{11}2^v\,\mathbf 1\{\operatorname{popcount}(x\mathbin{\&}M_v)\geq2\}.
\]

The code evaluates \(x,F_G(x),F_G^2(x),F_G^3(x),F_G^4(x)\) for every \(x\) and checks equality of the second and fourth iterates **for every state**. This is a finite exhaustive proof, not inference from samples. The same loop records the least \(t\in\{0,1,2\}\) for which the iterates two apart agree, the least period \(1\) or \(2\), and the canonical unordered attractor orbit; it counts each orbit's basin. The resulting complete \(5\times3\times2\) first-entry counts and all basin size multiplicities agree with `GRAPH_DATA.json`. Every graph's \(t=2\) row has positive total, proving the bound sharp on each isomorphism type. Every graph's immediate two-periodic-state count is even and equals twice the reported primitive two-cycle orbit count.

**Step 3: independent algorithmic cross-check.** `check_dynamics.py` constructs the update function a second way from explicit adjacency lists and follows each trajectory until the first repeated state; this algorithm neither assumes a two-cycle nor the time-two bound. Its independently reconstructed entrance, period and basin histograms agree exactly with the direct-four-iterate computation for all \(5\times4096=20{,}480\) graph/configuration pairs. `check_classification.py` independently checks graph connectivity, degrees, four-cycle counts and the named graph isomorphisms.

**Step 4: extremal comparisons.** Comparison of the five exhaustive rows gives the unique maximum 231 primitive two-cycle orbits and 3516 eventually oscillating initial states at \(B_3\), whereas 722 is the unique maximum individual basin at \(B_5\). The two graphs with six squares have different first-entry tables, so equality of the number of four-cycles does not imply equality of the majority-dynamical census.

## Verification

Extract `GRAPH_DATA.json`, `check_classification.py`, and `check_dynamics.py` from the same package into one directory, then run:

```sh
python3 check_classification.py
python3 check_dynamics.py
```

Only the Python standard library is needed. The observed terminal lines were `CLASSIFICATION_PASS normalized_connected_candidates=147 isomorphism_classes=5` and `DYNAMICS_PASS two_implementations graph_classes=5 initial_states=20480 every_configuration_F4_equals_F2 true`. The scripts also print the exact intermediate counts, graph encodings, and basin-size multiplicities. The independent adjacency-list trajectory test checks the orbit population without relying on the four-iterate identity.

## Relationship to prior work

Goles and Olivos established the general eventual period-at-most-two phenomenon for symmetric threshold networks. Kaaser, Mallmann-Trenn and Natale (2015, first arXiv version) proved a general graph-majority voting-time bound and module-based improvements; their general odd-degree bound yields \(1+18-12/2=13\) updates for these graphs, not the sharp bound two or their attraction-basin spectra. The Franklin graph and its standard crossed-prism representation are classical. Prior work has also classified five cubic bipartite graphs at order twelve for graph domination, but a graph-domination census does not imply the synchronous-majority orbit or basin distribution. The new contribution here is the exact **complete-class, dynamical first-entry and basin classification**, not either the classical period-two theorem or the enumeration of graph isomorphism classes in isolation.

## Limitations

This is a fully finite exhaustive result for twelve vertices, not an infinite-family stabilization theorem. It makes no assertion about the unique mechanism behind the class-dependent orbit populations or about cubic graphs at larger orders. The proof is reproducible exact computation coupled to exhaustive graph isomorphism classification, without a short symbolic derivation of each table entry. Historical priority remains uncertain for potentially unindexed graph-specific tables or inaccessible complete texts. No external independent mathematical audit has been performed.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1, first posted **2015-08-14**; especially Definition 3, Theorem 1.2, Corollary 3.4 and Appendix C. https://arxiv.org/abs/1508.03519
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486 (2014). https://arxiv.org/abs/1405.2486
4. E. W. Weisstein, *Franklin Graph*, MathWorld, https://mathworld.wolfram.com/FranklinGraph.html; see the \(12\)-vertex cubic crossed-prism structure and LCF notation.
