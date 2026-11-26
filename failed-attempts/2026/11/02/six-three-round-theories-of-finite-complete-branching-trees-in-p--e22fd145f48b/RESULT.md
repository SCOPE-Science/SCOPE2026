# Six three-round theories of finite complete branching trees in pure adjacency

## Finding

For integers \(b\ge2\) and \(h\ge0\), let \(T(b,h)\) be the finite complete rooted tree of edge-height \(h\) with exactly \(b\) children at each nonleaf vertex. Forget the root, its orientation and all levels: the structure is the ordinary simple undirected adjacency graph with equality and the sole relation \(E\).

**Theorem.** For all \(b,c\ge2\) and \(h,k\ge0\), the graphs \(T(b,h)\) and \(T(c,k)\) agree on every first-order sentence of quantifier rank at most three precisely in the following mutually exclusive cases:

\[
\begin{aligned}
& h=k=0;\\
& h=k=1\quad\text{and}\quad(b=2\iff c=2);\\
& h=k=2\quad\text{and}\quad(b=2\iff c=2);\\
& h,k\ge3.
\end{aligned}
\]

Thus there are **exactly six** rank-three theories, represented by \(T(2,0)\), \(T(2,1)\), \(T(3,1)\), \(T(2,2)\), \(T(3,2)\) and \(T(2,3)\), on respectively 1, 3, 4, 7, 13 and 15 vertices. The least possible uniform representative bound within this family is **15 vertices**. In particular, from height three onward rank-three adjacency logic detects neither the height nor whether the branching number is two or larger.

There is a sharp depth distinction: when \(h\ge3\), rank four can again distinguish binary from at-least-ternary branching, by asking for three distinct vertices with identical open neighborhoods. No full rank-four classification is asserted.

## Assumptions and scope

All structures are finite and nonempty, all branching numbers are integers at least two, all heights are nonnegative integers, and \(\equiv_3\) means agreement on all first-order sentences of quantifier rank at most three. Only equality and undirected adjacency are available. In particular, there are no names for the root or levels, no orientation, no order on children, and no transitive ancestry relation. The root is used only to describe the construction.

## Proof

**1. Three-round extension types.** For distinct vertices \(x,y\) of a simple graph, record whether \(E(x,y)\) holds and the set of attainable ordered Boolean pairs

\[
\bigl(E(x,z),E(y,z)\bigr),\qquad z\notin\{x,y\}.
\]

These data, together with the universally available responses \(z=x\) and \(z=y\), are exactly the quantifier-rank-one type of the ordered pair \((x,y)\). If \(y=x\), the corresponding type is determined by whether \(x\) has neighbors and distinct nonneighbors. The rank-two pointed type at \(x\) is the set of the rank-one pair types attained as \(y\) varies, including \(y=x\). Finally, the rank-three sentence type of the entire graph is the set of its pointed rank-two types. These are the elementary three-round Ehrenfeucht–Fraïssé extension recursions, with repeated choices retained.

**2. All distinct pairs have an outside nonneighbor in the stable range.** Put \(N=1+b+\cdots+b^h\). If \(h\ge3\), then \(N\ge1+b+b^2+b^3>2b+4\), whereas every vertex has degree at most \(b+1\). Consequently for every distinct \(x,y\) there exists \(z\notin\{x,y\}\) adjacent to neither: at most \(2(b+1)\) vertices are adjacent to either selected vertex. Thus the pattern \((0,0)\) always occurs.

In a tree, two distinct vertices have a common neighbor if and only if their graph distance is two, and such a neighbor is unique. If their distance is one or two, an additional neighbor of \(x\) that is not a neighbor of \(y\) (and is different from both selected vertices) exists precisely when \(x\) is not a leaf. At distance at least three, the same pattern exists even when \(x\) is a leaf. The analogous assertion holds with \(x,y\) interchanged. Therefore, after the first two distinct selections, every possible final-move pattern depends only on the first-two-vertex adjacency, whether their distance is two or at least three, and their leaf/nonleaf statuses. At distance at least three the leaf statuses disappear from the pair type.

**3. The four pointed types for every \(h\ge3\).** Every vertex has both a neighbor and a distinct nonneighbor. Each vertex has another vertex at distance at least three, and every nonleaf has nonleaf vertices at both distances one and two. The remaining rank-one pair signatures are controlled by the existence of leaf vertices at distances one and two from the selected vertex. For all \(b\ge2\), the pointed rank-two types are exactly:

| Position of the first vertex | Leaf at distance 1 | Leaf at distance 2 |
|---|---|---|
| Leaf, at depth \(h\) | No | Yes |
| Parent of leaves, depth \(h-1\) | Yes | No |
| Grandparent of leaves, depth \(h-2\) | No | Yes |
| Higher internal vertex, depth at most \(h-3\) | No | No |

The first row is distinguished from the other rows by whether the first vertex itself is a leaf, which is visible in its two-selected-vertex extension types. For leaf vertices there is a distance-two leaf (a sibling) and a distance-two nonleaf (a grandparent), since \(b\ge2\). For internal vertices there is always a neighboring nonleaf and a nonleaf at distance two; leaf neighbors occur exactly at depth \(h-1\), while distance-two leaves occur exactly at depth \(h-2\). The last row exists even at \(h=3\), when it contains the original root. All four rows are therefore realized for every \(b\ge2,h\ge3\), and no other pointed type occurs. Equality-response cases are identical throughout this range. By step 1, all such graphs have the same rank-three sentence type.

**4. Separating the five smaller classes.** The following are first-order sentences of quantifier rank at most three (variables range over graph vertices):

* \(\forall x\,\forall y\;(x=y)\) detects the one-vertex case.
* \(\exists x\,\forall y\;(x=y\lor E(x,y))\) holds exactly when the height is at most one.
* \(\exists x\,\forall y\;[x=y\lor E(x,y)\lor\exists z\,(E(x,z)\land E(z,y))]\) holds exactly when the height is at most two, because the radius of the graph is its construction height.
* \(\exists x\,\exists y\,\exists z\) asserting that the three vertices are pairwise distinct and pairwise nonadjacent distinguishes the star of branching two from stars of branching at least three.
* \(\exists x\,\exists y\,\forall z\;(z=x\lor z=y\lor E(x,z)\lor E(y,z))\) holds for \(T(2,2)\) and fails for \(T(b,2)\) when \(b\ge3\). Indeed the two first-level children dominate the binary height-two tree. In the latter case two closed neighborhoods cannot cover the leaves in all \(b\ge3\) first-level branches.

Together these sentences separate all six proposed classes. For height one, every \(b\ge3\) gives a star: its center is universal and two distinct leaves have a third spare leaf, so the center and the leaves have two fixed pointed types independent of the exact value of \(b\). For height two with \(b\ge3\), the graph order \(1+b+b^2\) exceeds \(2b+4\), hence the \((0,0)\) pair-extension pattern is universally available exactly as in step 2. Now a root has internal vertices at distance one and leaf vertices at distance two, but none farther away. A first-level internal vertex has internal and leaf neighbors, other internal vertices at distance two, and distant vertices at distance at least three. A leaf has an internal neighbor, both a sibling leaf and the root at distance two, and distant vertices. For pairs at distance at least three the second vertex's leaf status is invisible to the last move, so these are exactly three pointed rank-two types, independent of \(b\ge3\). The height-two binary tree has a different three-round type, as the explicit two-vertex domination sentence proves. This completes both directions.

**5. Sharp representative bound and a rank-four boundary.** The class with height at least three has smallest possible member \(T(2,3)\), with \(1+2+4+8=15\) vertices, while all other classes have the smaller representatives listed above. Finally, the rank-four sentence

\[
\exists x\,\exists y\,\exists z\,\forall w\;\Bigl(
(x\ne y\land y\ne z\land x\ne z)\land
(E(w,x)\leftrightarrow E(w,y))\land
(E(w,y)\leftrightarrow E(w,z))\Bigr)
\]

holds in \(T(b,h)\) for \(h\ge1\) exactly when \(b\ge3\): three sibling leaves share an open neighborhood precisely in that range. A tree cannot have two distinct common neighbors of any two vertices without a cycle, so three open-neighborhood twins must be sibling leaves. This confirms that the depth-three collapse of branching information is sharp.

## Verification

The included `verify_full_tree_rank3.py` computes complete rank-three types directly from all permitted equality and adjacency responses for all finite vertices. It distinguishes the six representatives and confirms the stable theory for all eligible instances with branching 2–5 and heights 3–5 up to 390 vertices. The separate `check_tree_pair_profiles.py` uses shortest-path distances to corroborate the analytic one-point extension patterns and the four pointed categories on six representative larger trees. Neither finite computation substitutes for the all-parameter proof in steps 2–4.

Run with Python 3 from the directory containing the files:

```
python3 verify_full_tree_rank3.py
python3 check_tree_pair_profiles.py
```

Expected outputs are recorded in the two matching `.out` files. No external libraries or datasets are needed.

## Relationship to prior work

Bohman, Frieze, Łuczak, Pikhurko, Smyth, Spencer and Verbitsky study first-order definability depth and Ehrenfeucht–Fraïssé games for general finite trees and random trees, but do not state the six-class, sharp rank-three classification for complete branching trees in the pure undirected adjacency signature in the inspected material [1]. Benedikt and Segoufin study first-order definability of regular labeled tree languages, with successor relations and a distinguished rooted-tree representation; their general characterization likewise does not give this exact unoriented, unlabeled rank-three partition [2].

The signature matters: a three-round classification of the same full rooted-tree family with strict ancestry is not an implication-equivalent classification for pure adjacency. The present result is a precise benchmark for information lost when the root, direction and transitive ancestor relation are forgotten. No claim is made that general finite-model-theoretic methods or all bounded-depth tree classifications are new.

## Limitations

Only rank three in the undirected, uncolored adjacency signature is classified. The four-round sentence above is merely a separating witness, not a complete rank-four classification. The result is not about arbitrary finite trees, trees with named roots, directed child edges or ancestry signatures. The finite checks are corroborative. Exhaustive historical-priority verification and an independent mathematical audit have not been carried out.

## References

[1] T. Bohman, A. Frieze, T. Łuczak, O. Pikhurko, C. Smyth, J. Spencer and O. Verbitsky, *First Order Definability of Trees and Sparse Random Graphs*, arXiv:math/0506288v1 (public 2005-06-15); *Combinatorics, Probability and Computing* 16 (2007), 375–400. https://arxiv.org/abs/math/0506288

[2] M. Benedikt and L. Segoufin, *Regular Tree Languages Definable in FO and in FOmod*, *ACM Transactions on Computational Logic* 11(1) (2009), doi:10.1145/1614431.1614435. Author-hosted full text: https://www.cs.ox.ac.uk/michael.benedikt/papers/revise.pdf
