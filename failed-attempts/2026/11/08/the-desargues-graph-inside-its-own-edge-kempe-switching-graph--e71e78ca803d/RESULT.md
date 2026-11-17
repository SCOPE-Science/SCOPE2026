# The Desargues graph inside its own edge-Kempe switching graph

## Finding

Let \(D=\operatorname{GP}(10,3)\) be the twenty-vertex Desargues graph. Let \(\mathcal K(D)\) have one vertex for each proper three-edge-colouring of \(D\), modulo a *global* permutation of the three colours. Two distinct vertices are adjacent precisely when one colouring is obtained from the other by exchanging two colours along **one entire connected alternating cycle**, again modulo global colour permutations. (Exchanging the colours of all alternating cycles at once is not a new state.)

**Theorem.** The resulting simple reconfiguration graph is

\[
\mathcal K(D)\cong D\,\sqcup\,6K_2.
\]

In particular, the twenty-state nontrivial component is itself isomorphic to the original Desargues graph. There are exactly \(32\) unlabelled three-edge-colourings, \(36\) switching edges, and seven components. The large component is cubic, bipartite, girth six and diameter five; the other six components are single edges. Its distance geometry, not merely its number of components, is determined.

## Assumptions and scope

Write \(V(D)=\{u_i,v_i:i\in\mathbb Z/10\mathbb Z\}\), with \(u_i=i\) and \(v_i=10+i\). Its \(30\) undirected edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\), for \(i\in\mathbb Z/10\mathbb Z\). Each undirected edge appears once. Edges in the certificate are ordered lexicographically as pairs of vertex numbers \(0,\ldots,19\). All graph vertices and edges are distinct and fixed; only the *three colours*, not the vertices, are identified under global permutations.

A proper edge-three-colouring assigns one of three colours to each of the \(30\) edges so that every vertex sees all three colours. The three colour classes are perfect matchings. A switch must act on one entire cycle of the even two-factor formed by two classes. The graph is simple: loops and duplicate transitions are discarded.

## Proof

**1. Exact exhaustive census has a finite completeness proof.** Every perfect matching is visited exactly once by the recursive procedure: select the smallest still-unmatched vertex and branch over each incident edge to an unmatched neighbour, then recur. This cannot omit a matching because its edge at the selected vertex occurs in exactly one branch; it cannot duplicate a matching because that first edge is forced by the matching and subsequent choices are forced similarly. Applying this procedure to the explicit \(30\)-edge list yields \(60\) perfect matchings. The two-factor complement of each perfect matching is obtained by tracing its degree-two connected components, producing the complete table:

| Complementary cycle lengths | Perfect matchings |
|---|---:|
| \((20)\) | 24 |
| \((10,10)\) | 36 |

All complementary cycles have even length. For any perfect matching \(M\) with \(c\) such cycles, the complementary two-factor has \(2^{c-1}\) ways to split its cycle edges into an **unlabelled pair** of alternating perfect matchings: choose independently which parity class each cycle contributes to the first remaining colour, and divide by simultaneous interchange of the two colours. An unlabelled three-edge-colouring is counted exactly three times when choosing which of its three matchings plays the distinguished role of \(M\). Hence the number of states is exactly

\[
\frac{24\cdot 1+36\cdot2}{3}=32.
\]

The complete 32-state list, in lexicographic order as strings of 30 colour digits, is embedded in `certificate.json`. The separate `verify_matchings.py` program implements precisely the above complete matching recursion, alternating partitions and matching-based toggles. The separate `verify_colouring.py` program starts instead from edgewise proper-colouring backtracking and independently obtains \(192\) *named* colourings, yielding \(32\) unlabelled states. Both routines enumerate all candidates, not a sample.

**2. Every possible move is enumerated.** For each of the \(32\) states, there are three unordered pairs of colours. The union of each pair is a spanning even two-factor. Tracing *all* its connected cycles and swapping exactly one of those cycles, then canonically relabelling the three colours, enumerates every legal neighbour by definition. The exhaustive output has \(36\) distinct undirected edges, listed explicitly in `certificate.json` as ordered state-index pairs. No induced edge is omitted: there are only three possible colour pairs, and each connected component of their two-factor is traced; no extraneous edge is allowed because exchanging on a complete alternating cycle preserves properness.

**3. A concrete isomorphism certifies the structural claim.** The same certificate supplies a list `large_component_to_GP` of twenty pairs \((s,v)\), sending a state index \(s\) to the vertex number \(v\) of \(D\). Inspection by the two standalone verification routines proves that the map is bijective and that the image of the \(30\) switching edges among these states is **exactly** the original \(30\)-edge set of \(D\), not just a subset. The other twelve states form the six listed disjoint edges `other_components`, with no edges to the first twenty states or between the pairs. Thus \(\mathcal K(D)\cong D\sqcup6K_2\). All claimed metrics follow immediately from this explicit isomorphism and direct breadth-first distance checks (the original Desargues graph has girth six and diameter five).

This is a **finite exhaustive proof with a compact, checkable certificate**, not a proposed generalisation to other generalized Petersen graphs. The exhaustive steps are bounded by 20 vertices, 30 edges, 60 matchings and 32 states.

## Verification

Run both standalone Python 3 standard-library verifiers from the directory containing `certificate.json`:

```
python3 verify_colouring.py
python3 verify_matchings.py
```

The first independently enumerates all edge colourings using degree-three incidence constraints and verifies every state and switch against the certificate. The second enumerates all perfect matchings, constructs factorisations by alternating cycles, and independently creates the transition graph by symmetric-difference exchanges of matchings. Both check the twenty-state vertex bijection and six remaining edges. Both complete successfully on the packaged files. The complete certificate is small enough for separate manual inspection.

## Relationship to prior work

Belcastro and Haas, initially publicly posted September 8, 2012, define and study edge-Kempe equivalence for cubic graph three-edge-colourings. In particular, their graph-cut methods, planar-bipartite theorem, and calculations for prism and Möbius ladder families concern numbers of equivalence classes. Goedgebeur and Östergård (first posted May 4, 2021) enumerate equivalence classes of cubic graphs through order 30 and bipartite cubic graphs through order 36. Their tables record aggregate distributions by graph order, and their algorithm is capable of recovering component counts. Such enumeration can cover the weaker invariant "seven classes" without specifying the present graph's full unlabelled adjacency or a self-isomorphic twenty-state component. Neither inspected primary text presents the Desargues graph reappearance \(\mathcal K(D)\cong D\sqcup6K_2\). The structural identification, rather than a generic implementation of Kempe switching, is the distinct assertion.

## Limitations

Only the specified graph \(D\), move rule and quotient by global **colour** permutations are covered. The theorem does not concern edge-colourings with individually named colours as separate states, vertex Kempe switches, transitions that simultaneously switch multiple cycles, or quotienting by graph automorphisms. The comparison with earlier aggregate computational tables is necessarily priority-qualified: a previously unindexed graph-specific computation or unpublished dataset interpretation might already encode the same adjacency. No independent scholarly audit has occurred.

## References

1. S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730v1 (first public arXiv date 2012-09-08); later *Discrete Mathematics* **325** (2014), 77–84. https://arxiv.org/abs/1209.1730
2. J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, arXiv:2105.01363v1 (first posted 2021-05-04), *Discrete Mathematics* **345** (2022), 112963. https://arxiv.org/abs/2105.01363
3. E. W. Weisstein, *Desargues Graph*, MathWorld, https://mathworld.wolfram.com/DesarguesGraph.html (background graph identification only).
