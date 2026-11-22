# A sharp collapse threshold for mixed two- and three-edge multi-theta matching complexes

## Finding
Let \(a,b\ge0\) be integers with \(a+b\ge2\). Let \(T_{a,b}\) have two distinct terminals and \(a+b\) pairwise internally vertex-disjoint terminal-to-terminal paths; exactly \(a\) paths have two edges and exactly \(b\) have three edges. There are no further edges. The ordinary matching complex \(\mathcal M(T_{a,b})\) has faces precisely the pairwise vertex-disjoint graph edges, including the empty face.

The complete *integral homotopy* classification is
\[
\mathcal M(T_{a,b})\simeq
\begin{cases}
S^0,&b=0,\ a=2,\\
\bigvee^{a^2-3a+1}S^1,&b=0,\ a\ge3,\\
\bigvee^{2a-1}S^1,&b=1,\ a\ge1,\\
S^1\vee S^1,&b=2,\\
*,&b\ge3.
\end{cases}
\]
Moreover, for \(b\ge3\) there is a complete acyclic simplicial matching with one critical vertex, hence an elementary simplicial collapse to a point. The first three regimes, and the universal two-circle plateau, identify a sharp transition at the third length-three arm.

## Assumptions and scope
Each path's interior vertices are private to that path, and all paths share only the two terminals. The graph is simple; path lengths are numbers of edges. The symbols \(S^0\) and \(S^1\) denote the ordinary zero- and one-spheres; a wedge of \(r\) circles denotes a connected one-dimensional CW complex with first integral Betti number \(r\). The symbol \(*\) means a contractible complex. All integer choices within the displayed domain are covered, with no upper bound on either parameter. No perfect-matching, multipath, or higher-matching complex is being classified.

## Proof
Index the arms by \(i=0,\ldots,a+b-1\), putting the short arms first. Write \(x_i\) for the edge adjacent to the first terminal and \(z_i\) for the edge adjacent to the second. Every long arm \(i=a+j\) also has its middle edge \(y_j\), where \(0\le j<b\). For a short arm, \(x_i\) and \(z_i\) meet at its interior vertex and cannot coexist. For a long arm, \(x_i\) and \(z_i\) are disjoint, but \(y_j\) meets both. All distinct \(x\)-edges mutually intersect at the first terminal; all distinct \(z\)-edges intersect at the second. Distinct middle edges are pairwise disjoint.

Consequently, for every simplex \(F\), its set \(S(F)\) of endpoint edges has at most one \(x\)-edge and at most one \(z\)-edge, with \(x_i,z_i\) forbidden together precisely when \(i<a\). Fixing a permitted outer set \(S\), the fiber of simplices with \(S(F)=S\) is the Boolean face poset of the available middle edges
\[
J(S)=\{j\in\{0,\ldots,b-1\}:x_{a+j}\notin S,\ z_{a+j}\notin S\}.
\]

When \(b\ge1\), for every fiber with \(J(S)\ne\varnothing\), pair each face with the face obtained by toggling \(y_{\min J(S)}\). The empty face is not in the nonempty-face poset; accordingly, in the \(S=\varnothing\) fiber retain \(\{y_0\}\) as one critical vertex instead of attempting to pair it with the empty face. In all other fibers the toggle is a complete matching. Fibers with \(J(S)=\varnothing\) contain exactly one simplex \(F=S\), which is critical.

This matching is acyclic. Orient every matched cover relation from its lower to its higher face and every other cover downward. The map \(F\mapsto S(F)\) never increases along these arrows: a matched cover leaves \(S\) fixed, and an unmatched deletion can only remove an outer edge. A directed cycle must therefore lie in one fixed fiber. In such a fiber the toggled middle edge can only be added via matched arrows, while downward unmatched arrows remove other middle edges. The number of these other middle edges strictly decreases between upward moves, preventing a cycle. In the exceptional \(S=\varnothing\) fiber the same reasoning holds with the single critical vertex retained. Thus discrete Morse theory produces a CW model having precisely the listed critical faces.

For \(b\ge3\), any permissible \(S\) contains at most two outer edges and therefore cannot block all \(b\) middle edges. Only \(\{y_0\}\) is critical. The acyclic face matching gives an elementary simplicial collapse to that vertex.

For \(b=2\), the only outer sets blocking both middle edges are \(\{x_a,z_{a+1}\}\) and \(\{x_{a+1},z_a\}\). Thus there is one critical vertex and two critical one-cells, with no higher cells. The CW model is exactly a wedge of two circles.

For \(b=1\), the outer sets blocking the middle edge are \(\{x_a\}\), \(\{z_a\}\), their allowed pair \(\{x_a,z_a\}\), and the \(2a\) allowed pairs \(\{x_a,z_i\}\), \(\{x_i,z_a\}\) for \(0\le i<a\). There are thus three critical vertices (including \(\{y_0\}\)) and \(2a+1\) critical edges, and no higher critical cells. Since \(a\ge1\), the original matching complex is connected: \(y_0\) is adjacent in its one-skeleton to every short-arm endpoint edge, while \(x_a\) and \(z_a\) connect to a short-arm edge at the opposite terminal. The one-dimensional Morse CW model is connected and has first Betti number \((2a+1)-3+1=2a-1\). It is a wedge of that many circles.

Finally let \(b=0\). Every simplex uses at most two edges and the complex is the bipartite graph with vertices \(x_0,\ldots,x_{a-1}\) and \(z_0,\ldots,z_{a-1}\), with edge \(x_i z_j\) if and only if \(i\ne j\). When \(a=2\) this is a disjoint union of two edges, homotopy equivalent to \(S^0\). For \(a\ge3\) it is connected, with \(2a\) vertices and \(a(a-1)\) edges, hence is a wedge of \(a(a-1)-2a+1=a^2-3a+1\) circles. This proves every case over the integers.

## Verification
The self-contained `verify_mixed_theta.py` constructs graph matchings directly from graph endpoints, independently reconstructs the endpoint/middle-edge description, verifies all proposed matched pairs, builds and topologically sorts the full oriented Hasse graph to check acyclicity, counts critical cells, and independently computes reduced mod-two Betti numbers. Executing `python verify_mixed_theta.py` checks 40 distinct pairs with \(2\le a+b\le9\) and \(0\le a,b\le6\), examining 19,089 faces altogether. Its recorded output is `verification_output.txt`. These finite checks corroborate the all-parameter argument; integral homotopy and collapsibility are proved above by the explicit acyclic matching and connected graph calculations, not by the finite sample.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega, *General polygonal line tilings and their matching complexes* (first public November 22, 2022), study chains of cycles meeting along single edges, not multiple internally disjoint terminal paths. Their results do not specify the displayed mixed-path phase diagram. Their later *Matching Complexes of Outerplanar Graphs* (first public November 7, 2024) proves that ordinary matching complexes of outerplanar graphs are contractible or wedges of spheres but does not give these multiplicities or collapsibility statements. For \(a+b\ge3\), \(T_{a,b}\) contains a subdivision of \(K_{2,3}\) and is not outerplanar, so the outerplanar theorem cannot be applied to the new infinite range. The public quadrilateral-book matching-complex theorem (2026) classifies \(n\) four-cycles sharing one edge. Deleting that common edge leaves exactly \(T_{0,n}\); adding it back attaches a cone over the simplex formed by all the middle edges. As this is a contractible subcomplex, the attachment does not change homotopy type. Hence the **homotopy-type part of the \(a=0\) subfamily was already implied** by that theorem; these instances are credited rather than claimed as independent discoveries. The new result is the full classification with arbitrary positive numbers of two-edge arms, including the \(2a-1\) rank law at one long arm, the two-circle plateau at two long arms, and the uniform elementary-collapse statement. The \(b=0\) chessboard-graph case and the \(a+b=2\) cycle cases are also known boundary instances included to make the phase diagram complete. Related classifications of *perfect*-matching complexes and *directed-multipath* complexes concern different simplicial complexes and do not imply this result.

## Limitations
Only the arm lengths two and three are treated; arbitrary long arm lengths, equivariant integral homology representations, and maps induced by changing arm counts are not classified. Searches and primary-document comparisons cannot exclude all unindexed equivalent results. No independent mathematical audit is claimed.

## References
- M. Bayer, M. Jelić Milutinović and J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559, first public 2022-11-22. https://arxiv.org/abs/2211.12559
- M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, first public 2024-11-07. https://arxiv.org/abs/2411.04601
