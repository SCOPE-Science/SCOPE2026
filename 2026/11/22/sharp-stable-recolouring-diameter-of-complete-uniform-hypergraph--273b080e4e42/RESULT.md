# Sharp stable recolouring diameter of complete uniform hypergraphs

## Finding

Let \(n\ge1\), \(r\ge2\), and \(k\ge n+1\) be integers. Write \(K_n^{(r)}\) for the hypergraph on \([n]\) whose edges are all \(r\)-element subsets (empty when \(n<r\)). A proper named \(k\)-colouring gives each vertex one of \(k\) colours, with no monochromatic hyperedge. Let \(\mathcal R_k(H)\) be the graph of proper colourings joined by single-vertex recolourings.

**Theorem.** For every such \(n,r,k\), \(\mathcal R_k(K_n^{(r)})\) is connected, and

\[
\operatorname{diam}\mathcal R_k(K_n^{(r)})
=n+\left\lfloor\frac{n}{2(r-1)}\right\rfloor.
\]

Thus the stable recolouring diameter of \(K_n^{(r)}\) is exactly the displayed number, and its stability threshold is at most \(n+1\). The theorem does not determine the least stability threshold. The specialization \(r=2\) is the familiar complete-graph value; the uniform-hypergraph extension \(r\ge3\) is the focus.

## Assumptions and scope

All vertices and colours are labelled; colours that happen to be unused remain available. Every hyperedge has size \(r\ge2\); if \(r>n\) the hypergraph is empty. Set \(q=r-1\). Because every \(r\)-subset is an edge, properness is equivalent to the occupancy bound \(\lvert\gamma^{-1}(c)\rvert\le q\) for every colour \(c\). Each move changes exactly one vertex to a different colour and must respect this bound. The claimed diameter is the maximum shortest-path distance over all pairs of these legal labelled colourings. For \(n=1\), the diameter is \(1\).

## Proof

**Upper bound via saturated directed components.** Fix any two proper colourings \(\alpha,\beta\), and maintain a current proper colouring \(\gamma\), initially \(\alpha\). A vertex is *unsettled* when its current and target colours differ. Whenever an unsettled vertex's target colour has fewer than \(q\) occupants, recolour it immediately to its target. Such a move settles one vertex without moving a settled vertex. Repeat until this is impossible or all vertices are settled.

In a stage with unsettled vertices and no such direct move, form a finite directed multigraph on the colour labels: for each unsettled vertex \(i\), draw the directed arc \(\gamma(i)\to\beta(i)\) labelled by \(i\). Arcs have no loops. Every colour with a positive indegree is saturated, since otherwise a direct move would be available. Let \(C\) be a sink strongly connected component of the subgraph on colours incident with arcs, so no arcs leave \(C\).

We first show that \(C\) is nontrivial and isolated. If \(C=\{c\}\), it has at least one entering arc, since the vertex \(c\) is incident with an arc and has no outgoing arc. Its current colour class is full of \(q\) settled vertices, but the target additionally asks for an entering vertex of colour \(c\); this contradicts properness of \(\beta\). Thus \(\lvert C\rvert\ge2\). Every colour \(c\in C\) has an incoming arc and is full. Let \(d^+(c)\), \(d^-(c)\) be outgoing and incoming arc multiplicities and let \(f(c)\) be the number of currently settled vertices of colour \(c\). Then \(f(c)+d^+(c)=q\), and properness of \(\beta\) gives \(f(c)+d^-(c)\le q\). Hence \(d^-(c)\le d^+(c)\). Summing over \(C\), using that no arc leaves the component, yields

\[
0\le\sum_{c\in C}\big(d^+(c)-d^-(c)\big)
=-\#\{\text{arcs entering }C\text{ from outside}\}\le0.
\]

It follows that no arc enters \(C\), and \(d^+(c)=d^-(c)\) for every \(c\in C\). The arcs inside \(C\) therefore form a strongly connected Eulerian directed multigraph, with at least two distinct colour vertices, each containing exactly \(q\) current tokens.

Choose an Euler tour through all arcs of \(C\), written as a cyclic sequence
\[
u_0\to u_1\to\cdots\to u_m=u_0,
\]
where the arc \(u_{j-1}\to u_j\) belongs to a distinct unsettled vertex \(i_j\). Because \(k\ge n+1\), there is an unused colour \(z\). Temporarily recolour \(i_1\) from \(u_0\) to \(z\), creating one vacancy in colour \(u_0\). Next process \(i_m,i_{m-1},\ldots,i_2\), each directly to its target colour; the current vacancy makes that target available. Finally recolour \(i_1\) from \(z\) to \(u_1\). This is a legal sequence of exactly \(m+1\) moves, settles all \(m\) formerly unsettled vertices associated with \(C\), and never disturbs a settled vertex. By the equality \(f(c)+d^-(c)=q\), all \(q\) vertices of every colour \(c\in C\) are now settled; no remaining unsettled vertex can be coloured \(c\) or require colour \(c\).

Resume direct moves and, as necessary, eliminate further isolated saturated components. Every such *Euler episode* costs exactly one move beyond its number of newly settled vertices. Each episode permanently settles all \(q\) vertices in at least two distinct saturated colour classes. The sets of vertices charged to different Euler episodes are pairwise disjoint. Thus the total number of episodes is at most \(\lfloor n/(2q)\rfloor\). Every initially unsettled vertex requires exactly one settling move, and no settled vertex is moved again, so the total path length is at most
\[
\big\lvert\{i:\alpha(i)\ne\beta(i)\}\big\rvert+\left\lfloor\frac{n}{2q}\right\rfloor
\le n+\left\lfloor\frac{n}{2q}\right\rfloor.
\]
This proves connectedness and the diameter upper bound.

**Sharp lower bound.** Write \(n=2qt+s\), where \(t=\lfloor n/(2q)\rfloor\) and \(0\le s<2q\). Partition \(2qt\) of the vertices into \(t\) blocks of \(2q\) vertices. Within each block use two private colours, \(a_j,b_j\); colour \(q\) vertices with \(a_j\), the other \(q\) with \(b_j\) in \(\alpha\), and interchange these colours in \(\beta\). For the remaining \(s\) vertices, assign private pairwise distinct colours in \(\alpha\) and rotate these colours cyclically when \(s\ge2\). When \(s=1\), give the last vertex a new, initially unused colour in \(\beta\). If \(t=0\) the same construction applies to all vertices; for \(n=1\) use two different colours. Every colour class has size at most \(q\), and both colourings use at most \(n+1\) named colours, so they exist for every \(k\ge n+1\). Every vertex changes its colour between \(\alpha\) and \(\beta\).

In each one of the \(t\) disjoint two-colour blocks, consider the **first** time any vertex in that block changes colour along an arbitrary valid recolouring sequence. At that instant both its potential target colours \(a_j,b_j\) are still full with \(q\) occupants, because no vertex of the block has yet moved and no other block contains those names initially. (If an external vertex has moved into a block colour, that colour remains full and the first block move cannot go to its target either.) The first block move therefore cannot be a direct-to-target recolouring. Hence each block forces at least one recolouring beyond the \(n\) indispensable first-to-target recolourings, and distinct blocks force distinct extra moves. Every path has length at least \(n+t\). Combined with the upper bound, this gives the equality.

## Verification

The included Python 3 program `verify_capacity_recolor.py` checks the legal occupancy interpretation, performs all-state breadth-first search from partition-orbit representatives for 17 parameter pairs \(1\le n\le6\), \(1\le q\le3\) (excluding \((n,q)=(6,3)\)), and checks the exact asserted diameter in each case with \(k=n+1\). It separately constructs lower-bound colourings and executes the Euler-tour algorithm across \(1\le n\le15\), \(1\le q\le5\), including randomized legal endpoints, validating every individual move and upper bound. The last run returned `VERIFY_OK`. These finite checks corroborate, but do not replace, the unrestricted proof.

## Relationship to prior work

W. Cames van Batenburg, *Large diameter for (\(\Delta+2\))-colouring reconfiguration*, arXiv:2611.17022v1 (public 2026-11-12), Section 7, Lemma 15, proves \(n\le\operatorname{diam}\mathcal R_k(H)\le2n-1\) for loopless hypergraphs when \(k\ge\Delta^*(H)+2\), and Question 18 asks for stable diameters and stability thresholds. The present theorem answers the stable-diameter portion on the complete uniform-hypergraph family, using a different occupancy/Euler-tour argument and a sharp matching lower construction.

S. Cambie, W. Cames van Batenburg and D. W. Cranston, *Sharp Bounds on Lengths of Linear Recolouring Sequences*, arXiv:2412.19695v1 (2024-12-27), Section 2, gives a renaming lemma involving cycles of whole colour classes. It concerns a common underlying partition and does not yield the capacity-constrained all-pairs bound with the factor \(2(r-1)\). The known complete-graph \(r=2\) case is a boundary specialization, not asserted as a new result.

## Limitations

The formula is proved for \(k\ge n+1\), with no claim of the exact least stability threshold or a formula for smaller palettes. The proof assumes named colours and standard weak hypergraph properness (no monochromatic edge). No unindexed or historical statement of equivalent capacity-constrained token-routing results is excluded; further independent priority review is warranted. Computational verification is finite; no independent mathematical audit has been performed.

## References

1. W. Cames van Batenburg, *Large diameter for \((\Delta+2)\)-colouring reconfiguration*, arXiv:2611.17022v1, 2026-11-12. https://arxiv.org/html/2611.17022v1
2. S. Cambie, W. Cames van Batenburg, D. W. Cranston, *Sharp Bounds on Lengths of Linear Recolouring Sequences*, arXiv:2412.19695v1, 2024-12-27. https://arxiv.org/html/2412.19695v1
