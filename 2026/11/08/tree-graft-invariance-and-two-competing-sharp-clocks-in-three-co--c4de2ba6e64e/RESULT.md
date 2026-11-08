# Tree-graft invariance and two competing sharp clocks in three-color cyclic dynamics

## Finding

Let \(G\) be formed from a complete graph \(K_c\), \(c\ge 3\), by identifying each clique vertex \(a\) with the root of a finite rooted tree \(T_a\). Apart from their distinct clique roots, these trees are disjoint, and there are no edges between them. At least one tree contains a nonroot vertex. Put
\[
 k=|V(G)|-c,\qquad H=\max_{a,v\in T_a}d_{T_a}(a,v)\ge1,\qquad D=\operatorname{diam}(G).
\]
Consider synchronous three-color cyclic cellular automaton (CCA): a vertex at color \(j\in\mathbb Z/3\mathbb Z\) increments to \(j+1\) exactly when some neighbor already has color \(j+1\). Let \(F\) be its global map, and let \(T(x)\) be the first time the labelled configuration \(F^t(x)\) belongs to a periodic orbit.

**Theorem.** The only recurrent configurations are three uniform fixed points and
\[
 Q_c=\frac{3^c-3\cdot2^c+3}{3}
\]
primitive three-cycle orbits. Each uniform fixed point has a basin of exactly \(3^k(2^c-1)\) labelled initial configurations. Each individual primitive three-cycle has a basin of exactly \(3^{k+1}\) initial configurations. In particular, with uniformly independent initial colors,
\[
 \Pr(\text{eventual period }3)=\frac{3^c-3\cdot2^c+3}{3^c},
\]
which is **independent of the number, shapes, branch degrees and attachment positions of the rooted trees**.

An initial configuration whose clique uses at most two colors reaches a uniform fixed point by update \(D\); the bound is attained among such configurations. An initial configuration whose clique uses all three colors reaches a primitive three-cycle by update \(2H\); this bound is also attained. Hence the sharp maximum first-periodic-entry time over all initial states is
\[
 \boxed{\max_x T(x)=\max\{D,2H\}},
 \qquad \boxed{F^{\max\{D,2H\}+3}=F^{\max\{D,2H\}}}.
\]
No earlier exponent works in the second identity. In the oscillatory regime, for each clique root \(a\) and \(v\in T_a\), the final periodic wave has color \(x(a)+t-d_{T_a}(a,v)\pmod3\) at time \(t\).

## Assumptions and scope

The graph is simple, finite and connected. Its clique \(K_c\) has \(c\ge3\) labelled vertices, with any finite rooted tree (possibly a one-vertex tree) identified at each clique vertex. There are no additional cycles outside the clique and no edges joining distinct grafts except the clique edges. The contact threshold is one, updates are simultaneous, and exactly three cyclic colors are used. Distances and first-entry times count discrete graph edges and complete synchronous updates, respectively. The basin of a periodic orbit includes the recurrent orbit itself; a primitive three-cycle counts once, not once per phase.

The historical synchronization-versus-oscillation criterion and the diameter upper bound in the conservative regime are established prior work, not new claims here. The contribution assessed here is the simultaneous tree-independent, orbit-by-orbit basin classification and the shape-sensitive **sharp** nonconservative clock \(2H\), including its competition with the diameter clock.

## Proof

**1. Clique dichotomy.** If the initial clique has all three colors, every clique vertex has a clique neighbor in its successor color. Thus the entire clique increments at every update, from time zero onward. If the initial clique has at most two colors, assign integer heights to its vertices, congruent to their colors modulo three, with differences at most one on clique edges: a single color uses one height; a two-color set \(\{j,j+1\}\) uses heights \(j,j+1\) (with a consistent integer representative). Extend uniquely along every rooted-tree edge, choosing the integer edge increment in \(\{-1,0,1\}\) matching the endpoint-color difference modulo three. This makes an integral one-Lipschitz lift of the whole graph.

**2. Conservative dynamics.** For any integral height configuration \(h\) that is one-Lipschitz along edges, the CCA update modulo three equals the integer closed-neighborhood maximum update
\[
 h_{t+1}(v)=\max_{u\in N[v]}h_t(u).
\]
Indeed, a neighbor in the successor color must be exactly one unit higher. The neighborhood maximum is either the current height or that height plus one. One-Lipschitzness is preserved: if \(v\sim w\), every height sampled in \(N[v]\) is bounded by \(h_t(v)+1\le\max_{u\in N[w]}h_t(u)+1\), and conversely. By induction,
\[
 h_t(v)=\max_{d_G(v,u)\le t}h_0(u).
\]
At time \(D\), every vertex holds the same global maximum; the resulting monochrome configuration is fixed. To prove sharpness choose an endpoint \(b\) of a diameter and set \(h_0(v)=d_G(b,v)\). Its clique heights take at most two consecutive values, so it is a legitimate non-rainbow configuration. At \(b\), the height is exactly \(t\) for \(t\le D\), while at a diametral opposite vertex the height is at least \(D\). The connected one-Lipschitz state cannot have all colors equal until all integer heights agree. Thus its first fixed entry is exactly \(D\).

**3. Forced rooted-tree dynamics.** Suppose all three clique colors occur initially. Fix a clique root \(a\) and write its initial color as an integer \(b_a\in\{0,1,2\}\). Its forced height is \(h_t(a)=b_a+t\). Lift initial colors along its rooted tree so that adjacent heights differ by at most one. Every nonroot vertex is still governed by the integer closed-neighborhood maximum, while its root is forced upward one unit at each update. The one-Lipschitz property on tree edges persists: on an edge away from the root both endpoints use maxima; on a root edge a child initially one step behind must increment when the root increments, and other initial relative heights cannot produce a gap greater than one. Consequently
\[
 b_a+t-d(a,v)\le h_t(v)\qquad(v\in T_a).
\]
Let \(H_a=\max_{u\in T_a}d(a,u)\), and let \(M_a=\max_{u\in T_a}h_0(u)\le b_a+H_a\). Induction on the nonroot maximum update, using the depth change of at most one across a tree edge, gives
\[
 h_t(v)\le\max\{M_a,\ b_a+t-d(a,v)\}.
\]
Thus for \(t\ge H_a+d(a,v)\), upper and lower bounds coincide:
\[
 h_t(v)=b_a+t-d(a,v).
\]
Every graft is therefore in its unique forced traveling-wave phase at time \(2H\). All vertices then increment at every subsequent step, because each nonroot tree vertex sees its parent one color ahead and every clique vertex already has a successor-colored clique neighbor. The full state has least period three.

Sharpness: choose a tree of height \(H\), and initialize each of its vertices at color \(b_a+d(a,v)\pmod3\), equivalently lift \(h_0(v)=b_a+d(a,v)\). Give the clique a rainbow coloring. For a deepest leaf \(w\), the initial height \(b_a+H\) is its maximal possible height until time \(2H-1\), because the displayed upper bound is then \(b_a+H\). Its height at that time is therefore \(b_a+H\), whereas the recurrent-wave value is \(b_a+H-1\). The colors differ modulo three. No periodic state with this rainbow clique can have a different tree wave, so first entry cannot occur earlier than \(2H\). The preceding upper bound supplies equality.

**4. Counts.** Among \(3^c\) clique colorings, exactly \(R_c=3^c-3\cdot2^c+3\) use all three colors, by inclusion-exclusion. All \(R_c\) rainbow clique colorings are immediately in three-step rotational orbits, and three phases form each orbit. There are \(Q_c=R_c/3\) such clique orbits. For every prescribed initial clique phase, all \(3^k\) initial assignments of the nonclique tree vertices reach the same forced wave, independently of those assignments. Each primitive three-cycle consequently receives exactly \(3\cdot3^k=3^{k+1}\) initial states.

The remaining \(3\cdot2^c-3\) clique colorings are conservative. Every choice of the \(k\) tree colors synchronizes, giving \(3^k(3\cdot2^c-3)\) fixed-basin states. Global color rotation permutes the three fixed points transitively, so each basin contains precisely \(3^k(2^c-1)\) states. These account for the entire \(3^{c+k}\)-state phase space. The two independently attained sharp time bounds yield the claimed global maximum and polynomial identity.

## Verification

The standalone file `verify_tree_grafts.cpp` independently constructs graphs, updates every labelled color directly at each vertex, searches for the first recurrence, and checks the two classes, individual orbit basin sizes, and sharp time bounds. Thirteen representative nonisomorphic graft systems, including branching trees and attachments at different clique roots, passed exhaustive enumeration, totaling 269,811 labelled configurations (with exact per-case totals in `direct_enumeration.log`; no extrapolation is used). The independent `verify_height_lifts.py` compares direct color updates against the integer-lift dynamics on 7,000 deterministically seeded random clique-of-trees instances, including non-rainbow consensus and rainbow traveling-wave cases. Its output is in `height_comparison.log`.

The infinite-graph-family proof above is independent of the finite tests. All computations are reproducible with C++17 and Python 3 standard libraries, respectively:

```sh
g++ -O2 -std=c++17 verify_tree_grafts.cpp -o verify_tree_grafts
./verify_tree_grafts
python3 verify_height_lifts.py
```

## Relationship to prior work

Gravner, Lyu and Sivakoff's 2016 preprint establishes the threshold-one three-color CCA rule, a general walk/max-height comparison (Lemma 1), and a conservative-circulation criterion with a diameter synchronization bound for finite graphs (Theorem 3). Those general conclusions are not novel here. Their theorem does not tabulate the primitive orbits or individual basin sizes for arbitrary clique-grafted forests and does not assert the sharp \(2H\) entrance time in the nonconservative case. The present exact graph-family calculation uses the same established max-plus viewpoint but proves the additional forced-root estimates and sharpness constructions.

A known special-case calculation for a clique with one pendant leaf gives an exact nine-state basin for each three-cycle. That case has one root with one extra vertex, \(H=1\), and is strictly contained in the present arbitrary-size, arbitrary-branching, multi-root family. General tree-only synchronization results cannot directly classify the rainbow-clique regime because their graphs have no cycling core.

## Limitations

The claim is restricted to threshold-one CCA with three colors and to graphs with a single complete cyclic core plus attached trees; it does not classify multiple cyclic blocks, general connected graphs, four or more colors, or altered update rules. The result does not give the complete distribution of first-entry times within each basin, beyond the sharp bounds. It does not establish bibliographic uniqueness, and the priority of the specialized formulas remains subject to unindexed or inaccessible publications. Computational checks cover finitely many cases; the proof, not the simulation, establishes every allowed parameter.

## References

1. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, publicly posted 2016-10-24. https://arxiv.org/abs/1610.07320 . The published version is *Annals of Applied Probability* 28 (2018), 3324–3357, DOI:10.1214/17-AAP1350.
2. The author's open full text of the published version, https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf (especially the introduction, Lemma 1, Theorem 3 and its proof).
