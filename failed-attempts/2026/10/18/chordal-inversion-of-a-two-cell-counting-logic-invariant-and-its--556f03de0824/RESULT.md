# Chordal inversion of a two-cell counting-logic invariant and its sharp forty-vertex collision

## Finding

**Theorem.** Let \(\mathcal C\) consist of all finite, connected, simple, chordal graphs \(G\) admitting a partition \(V(G)=H\sqcup L\), with both parts nonempty, such that each vertex of \(H\) has three neighbours in \(L\) and none in \(H\), while each vertex of \(L\) has one neighbour in each part. Equivalently, the corresponding two-cell equitable quotient (with ordered cells \(H,L\)) is
\[
Q=\begin{pmatrix}0&3\\1&1\end{pmatrix}.
\]

For each integer \(k\geq 0\), the isomorphism types of members of \(\mathcal C\) with \(8k+8\) vertices are in canonical bijection with the set \(\mathcal R_k\), where \(\mathcal R_0\) is a singleton and, for \(k\geq1\), \(\mathcal R_k\) consists of the isomorphism types of trees on \(k\) vertices of maximum degree at most three. The graph corresponding to \(R\in\mathcal R_k\) is explicitly constructed below. These graphs have \(2k+2\) degree-three vertices, \(6k+6\) degree-two vertices, and \(9k+9\) edges.

Two graphs belonging to \(\mathcal C\) satisfy exactly the same sentences of two-variable first-order logic with counting quantifiers, denoted \(C^2\), **if and only if they have the same order**. Their isomorphism types agree if and only if the corresponding auxiliary trees agree. Within \(\mathcal C\), the first order admitting two nonisomorphic \(C^2\)-equivalent graphs is **40**: exactly two isomorphism types occur at that order, indexed by \(R=P_4\) and \(R=K_{1,3}\). The number of nonisomorphic, mutually \(C^2\)-equivalent connected chordal graphs in this prescribed equitable class is unbounded.

The forty-vertex statement is **relative to the displayed quotient and chordality hypothesis**. No minimality among all chordal graphs is asserted.

## Assumptions and scope

A graph is *chordal* when it has no induced cycle of length four or more. A *block graph* is a graph whose every biconnected block is a clique. The stable one-dimensional color refinement, or \(1\)-WL, starts with one vertex color and repeatedly refines it using the multiset of neighbors' previous colors. On finite graphs, equal stable color histograms in a common refinement of their disjoint union are equivalent to indistinguishability in \(C^2\) (the classical color-refinement/counting-logic correspondence).

The degree partition is intrinsic because vertices in \(H\) have degree three and those in \(L\) degree two. Connectedness, finiteness, simplicity, both nonempty cells, and the exact full quotient \(Q\) are essential assumptions. The conclusion is about **simple undirected graphs** and does not classify arbitrary relational structures, general chordal graphs with other equitable quotients, or graphs without chordality.

For a tree \(T\) all of whose degrees are one or three, define \(B(T)\) by replacing every edge \(ab\) of \(T\) by a three-edge path \(a-u-v-b\), using two new vertices, and, independently, adding two further new vertices \(p,q\) and edges \(ap,pq,qa\) at every leaf \(a\) of \(T\). The vertices originally in \(T\) comprise \(H\); the added vertices comprise \(L\). If \(k=0\), take \(T=K_2\). If \(k\geq1\), take any tree \(R\) of order \(k\) and maximum degree at most three and attach exactly \(3-\deg_R(v)\) new leaves at each \(v\in V(R)\) to obtain \(T=T(R)\).

## Proof

**1. The matching contraction.** Let \(G\in\mathcal C\), and put \(t=|H|\). The prescribed degrees force \(G[L]\) to be a perfect matching and \(|L|=3t\). Consequently \(t\) is even, and \(t\geq2\). Each matching edge \(uv\), with unique \(H\)-neighbors \(a\) of \(u\) and \(b\) of \(v\), either has \(a=b\) or provides a three-edge path \(a-u-v-b\). Let \(F\) be the resulting multigraph on \(H\), recording the former kind as a loop and the latter kind as an ordinary edge. Deleting its loops gives a connected multigraph \(F^\circ\): all connections among distinct vertices of \(H\) in \(G\) pass through these three-edge paths.

If \(F^\circ\) contains a multigraph cycle of length \(s\geq2\), the corresponding three-edge paths in \(G\) give an induced cycle of length \(3s\geq6\). Indeed, their interior vertices have no neighbors other than the two prescribed path neighbors, and \(H\) is independent. This contradicts chordality. Thus \(F^\circ\) is a simple tree \(T\) on \(H\). If \(m_a\) denotes the number of loops at \(a\), counting the three edges from \(a\) to \(L\) yields
\[
\deg_T(a)+2m_a=3.
\]
Since \(T\) is connected on at least two vertices, \(\deg_T(a)\geq1\), so exactly one of \((\deg_T(a),m_a)=(1,1)\) and \((3,0)\) occurs. Each degree-one vertex has one attached triangle, and every other vertex has degree three. It follows, using the matching decomposition, that \(G\cong B(T)\). The recovery of \(T\) is intrinsic and respects graph isomorphisms.

**2. All constructions and counts.** Conversely, for any tree \(T\) with degrees one or three, \(B(T)\) is connected and has the prescribed \(H,L\) adjacency counts. Every biconnected block is either an edge or a pendant triangle, so \(B(T)\) is a block graph and hence chordal. If \(k\) is the number of degree-three vertices of \(T\) and \(a\) the number of leaves, the tree handshake identity gives \(a=k+2\). Hence \(|H|=a+k=2k+2\), \(|L|=3|H|=6k+6\), \(|G|=8k+8\), and \(|E(G)|=(3|H|+2|L|)/2=9k+9\). In particular there are \(k+2\) pendant triangles.

For \(k\geq1\), the induced subtree of \(T\) on its degree-three vertices is connected (a path between such vertices cannot have a degree-one vertex internally), has \(k\) vertices and maximum degree at most three, and is precisely \(R\). Restoring \(3-\deg_R(v)\) leaves at each core vertex recovers \(T\). Conversely, every such \(R\) produces exactly one \(T\). For \(k=0\), the only connected tree with no degree-three vertices and all degrees one is \(K_2\). This establishes the isomorphism-type bijection and all counts.

**3. Exact counting-logic indistinguishability.** Starting color refinement from the uniform coloring immediately separates degree-two and degree-three vertices. Because every vertex in each of \(H,L\) has the same number of neighbors in each of those two cells, the partition stabilizes there. All graphs in \(\mathcal C\) with equal \(k\) have the same stable two-cell quotient \(Q\) and the same cell sizes \((2k+2,6k+6)\); running refinement on their disjoint union leaves identical color histograms on both summands. By the \(1\)-WL/\(C^2\) correspondence, they are \(C^2\)-equivalent. Conversely, different \(k\) give different total orders, detected by a counting sentence. The isomorphism criterion follows from the intrinsic recovery of \(R\).

**4. Sharp forty-vertex onset and unbounded multiplicity.** A tree on \(k\leq3\) vertices is unique up to isomorphism. On four vertices the only two trees have degree sequences \((2,2,1,1)\) and \((3,1,1,1)\): \(P_4\) and \(K_{1,3}\). Both are subcubic, so the first nontrivial multiplicity in the restricted class occurs at \(8(4)+8=40\), and that multiplicity is exactly two. For each positive integer \(m\), put \(k=3m+1\). For \(j=0,1,\ldots,m-1\), take \(R_j\) to be a three-arm spider whose arm lengths in edges are \((m-j,m,m+j)\). These are \(m\) pairwise nonisomorphic subcubic trees of the same order \(k\), since their unique degree-three centers have different unordered arm-length multisets. Their associated graphs all have \(8k+8\) vertices, are chordal, and are \(C^2\)-equivalent. Thus the multiplicities grow without bound.

## Verification

A standard-library-only accompanying program, `verify.py`, constructs the examples, explicitly recovers the contracted tree, tests the prescribed neighborhood counts and graph sizes, verifies by biconnected-block decomposition that all blocks are cliques, and runs ordinary color refinement on each graph and on the disjoint union of the forty-vertex pair. Run `python3 verify.py`. It checks the core trees of orders one through four, both nonisomorphic four-vertex cores, and thirty further path-core instances.

An additional separate experiment generated and checked 46 nonisomorphic subcubic core trees through order nine, with identical structural and color-refinement outcomes. These computations are finite consistency checks; the universal bijection, sharp threshold, and unboundedness are justified by the proof above rather than by extrapolation.

## Relationship to prior work

Arvind, Köbler, Rattan, and Verbitsky establish the standard graph-isomorphism/color-refinement framework, the connection to two-variable counting logic and fractional isomorphism, and structural criteria for globally color-refinement-amenable graphs. In particular their local equitable-cell results allow both a matching cell and a star-forest bipartite cell. The theorem here instead inverts a **specified two-cell quotient within the connected chordal class**. It determines every restricted isomorphism type, a sharp restricted collision order, and an unbounded restricted class multiplicity. None of those three conclusions follows merely from the general correspondence between color refinement and counting logic.

Kiefer, Schweitzer, and Selman describe a general complete \(C^2\) invariant based on stable cell sizes and inter-cell degrees, give unconstrained inversion constructions, and classify graphs globally identified by that logic. Their results explain why equal quotients entail \(C^2\) equivalence, but do not themselves classify the chordal realizations of this particular quotient. The present matching-contraction/tree-bijection supplies the extra chordality-specific information. It does **not** contradict their general global classification: there can also be nonchordal realizations with the same quotient.

## Limitations

The forty-vertex cutoff is relative to exactly the quotient \(Q\), connectedness, and chordality; it is not a global minimum for failure of color refinement on chordal graphs. The theorem concerns unlabeled graph isomorphism types, not labeled counts or asymptotic enumeration. Numerical experiments do not establish the general theorem or exclude unindexed equivalent formulas. The literature comparison supports originality relative to the inspected primary results, with residual risk of an equivalent unpublished or unindexed characterization. No independent mathematical audit has been performed.

## References

1. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, preprint publicly available 2015-02-04, arXiv:1502.01255, particularly Sections 2–4 and the introduction. https://arxiv.org/abs/1502.01255
2. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, preprint publicly available 2015-03-30, arXiv:1503.08792, particularly Sections 3 and 4. https://arxiv.org/abs/1503.08792
