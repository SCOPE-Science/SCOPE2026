# A sharp refinability criterion for cycle barbell graphs

## Finding

Let \(B(m,n,d)\), for integers \(m,n\ge3\) and \(d\ge1\), be the finite simple graph obtained from vertex-disjoint cycles of lengths \(m,n\) by joining one designated vertex of each cycle with a new path of \(d\) edges (and \(d-1\) new interior vertices). All vertices are initially uncolored. A graph is **refinable** if its stable one-dimensional Weisfeiler--Leman (1-WL, or color-refinement) vertex partition equals its automorphism-orbit partition.

**Theorem.** The graph \(B(m,n,d)\) is refinable if and only if the three lengths are *not all equal*:
\[
 B(m,n,d)\text{ is not refinable}\quad\Longleftrightarrow\quad m=n=d.
\]
More precisely, the number of distinct stable 1-WL colors is
\[
 c(m,n,d)=
 \begin{cases}
 d+1+\lfloor m/2\rfloor+\lfloor n/2\rfloor,&m\ne n,\\
 1+\lfloor m/2\rfloor+\lfloor d/2\rfloor,&m=n\ne d,\\
 1+\lfloor m/2\rfloor,&m=n=d.
 \end{cases}
\]
In the final case the number of automorphism orbits is \(1+2\lfloor m/2\rfloor\); thus the stable partition merges exactly \(\lfloor m/2\rfloor\) pairs of *distinct automorphism-orbit classes*. Specifically, a vertex at distance \(j\) from the designated vertex on either cycle has the same stable color as an interior bridge-path vertex at distance \(j\) from its nearer endpoint whenever \(1\le j\le\lfloor m/2\rfloor\), although these vertices are never automorphic.

The result is relative to the family of cycle barbells and concerns color classes of *vertices of one graph*, not the identification of that graph among all graphs, not higher-dimensional WL, and not a formula for stabilization time.

## Assumptions and scope

All graphs are finite, simple, undirected and uncolored. The two cycles meet neither each other nor the interior of the connecting path. If \(d=1\), the connector is a single bridge edge. The two vertices of degree three are the *hubs*. Every other vertex has degree two. The path length \(d\) and both cycle lengths count edges. The graph has \(m+n+d-1\) vertices and \(m+n+d\) edges.

Color refinement starts with the indiscrete partition \(\chi_0\), then assigns \(\chi_{t+1}(v)=(\chi_t(v),\left\{\!\left\{\chi_t(w):w\sim v\right\}\!\right\})\), up to injective renaming of color symbols. Its stable partition is the first partition after which no class splits. In formulas below, all distances along a cycle are measured from that cycle's hub, and bridge-path positions are numbered \(1,\ldots,d-1\) from the first hub.

## Proof

**Step 1: stable colors as rooted universal-cover types.** In any finite graph, vertices have the same stable 1-WL color exactly when their rooted infinite universal covering trees are isomorphic. One can see this directly by induction: the color at round \(t\) is the isomorphism type of the rooted depth-\(t\) universal-cover truncation, since the recursive color records the rooted type and the multiset of neighboring rooted types. In a finite graph, color refinement stabilizes after finitely many rounds; equality at stability is therefore equality at every depth. Conversely, isomorphic infinite rooted covers give equality at every finite depth. This is also Lemma 2.6 of Krebs--Verbitsky [KV14]. Crucially, the universal cover *does not retain identifications of two distinct walks that end at the same original vertex*.

**Step 2: the weighted branching skeleton.** Unfolding \(B(m,n,d)\) into its universal cover produces an infinite tree with vertices of degrees two and three. Suppress every maximal chain of degree-two vertices between consecutive degree-three vertices, but retain as an edge label the original chain length. The result is an infinite trivalent tree \(S\) with each edge carrying a positive integer length. It is the tree covering of the two-hub pseudograph with one loop of length \(m\) at the first hub, one loop of length \(n\) at the second, and one connector of length \(d\). Each degree-three node lying above the left hub has three incident segment lengths \(\{m,m,d\}\); each lying above the right hub has \(\{n,n,d\}\). These lengths can be recovered *intrinsically* from the uncolored universal cover by moving along each branch to the next degree-three node and counting traversed edges.

For a root of degree two, its two non-backtracking directions meet their first degree-three nodes in finite numbers \(j\) and \(L-j\) of edges, where \(L\) is the segment's length. Beyond those nodes one sees the remaining incident segment types. Thus the infinite rooted cover records the edge length, the two endpoint branch types, and the position along that segment (up to reversing it when the endpoint types are interchangeable). A root of degree three records its hub type. These data are also *sufficient*: if they match for two roots, recursively pair the incident branches, continuing at every degree-three node by the same multiset of outgoing segment types. All resulting matching branches are infinite and have identical labeled local degrees. This back-and-forth gives an isomorphism of the uncolored infinite rooted covering trees. The sufficiency can alternatively be seen by lifting the obvious symmetries of the infinite trivalent universal cover of the two-loop-and-link pseudograph. No cyclic closing relation in the finite graph survives in this tree.

**Step 3: unequal cycle lengths.** Assume \(m\ne n\). The multisets \(\{m,m,d\}\) and \(\{n,n,d\}\) differ, so the two kinds of degree-three nodes in the cover can be intrinsically distinguished. A path segment has a recoverable type among: left-to-left length \(m\); right-to-right length \(n\); left-to-right length \(d\). Even if two numeric lengths coincide, their endpoint types distinguish them. Accordingly, two degree-two vertices have isomorphic rooted covers exactly when they lie in the *same segment type* and at the same distance to the nearest endpoint, allowing the reversal of left-to-left or right-to-right segments but not that of the left-to-right connector. This is exactly the finite automorphism-orbit partition: each cycle has one reflection fixing its hub, and both hubs and all bridge-path vertices are fixed. The two cycle flips generate the full automorphism group since cycle lengths are unequal. Counting one hub-orbit for each hub, \(\lfloor m/2\rfloor\) nonhub orbits on the first cycle, \(\lfloor n/2\rfloor\) on the second, and \(d-1\) singletons on the path yields \(d+1+\lfloor m/2\rfloor+\lfloor n/2\rfloor\) colors and orbits.

**Step 4: equal cycles, unequal connector length.** Assume \(m=n\ne d\). Now both kinds of degree-three nodes have the same intrinsic type, with incident segment-length multiset \(\{m,m,d\}\). However, the connector segments of length \(d\) are distinguishable from the cycle segments of length \(m\), and all degree-three nodes are equivalent in the infinite covering tree. Hence nonhub stable colors are classified by (a) belonging to an \(m\)-segment and having unordered distances \(\{j,m-j\}\) from its endpoints, or (b) belonging to a \(d\)-segment and having unordered distances \(\{j,d-j\}\). In the finite graph these are exactly the orbits generated by independent cycle reflections and the symmetry exchanging the two cycles while reversing the connector. There is one hub orbit, \(\lfloor m/2\rfloor\) cycle-position orbits, and \(\lfloor d/2\rfloor\) bridge-position orbits, totaling \(1+\lfloor m/2\rfloor+\lfloor d/2\rfloor\).

**Step 5: equal cycle and connector lengths.** Assume \(m=n=d=L\ge3\). Every degree-three node of the universal cover has three incident segments of length \(L\); after suppression of degree-two chains its rooted tree is simply the homogeneous infinite cubic tree with each edge uniformly subdivided into \(L\) edges. Its rooted types consist of (i) degree-three nodes, all equivalent, and (ii) degree-two nodes at unordered distances \(\{j,L-j\}\) from the adjacent degree-three nodes, for \(1\le j\le\lfloor L/2\rfloor\). Therefore there are exactly \(1+\lfloor L/2\rfloor\) stable colors. By contrast, every automorphism of the finite graph preserves its set of bridges, so it cannot map an interior connector vertex to a cycle vertex. The orbit partition has one hub orbit, \(\lfloor L/2\rfloor\) cycle-position orbits and \(\lfloor L/2\rfloor\) connector-position orbits, giving \(1+2\lfloor L/2\rfloor\). The two distinct kinds of orbit at each distance \(j\) are merged by refinement, proving the failure and its exact extent.

These three exhaustive cases prove the theorem. \(\square\)

## Verification

A standalone standard-library Python script, `verify_barbell.py`, directly constructs each \(B(m,n,d)\), computes its 1-WL fixed point by iterated neighbor-color multisets, compares its entire stable partition to the theorem's explicit predictions, and checks the predicted orbit-count formulas. It explores all ordered-by-size parameters \(3\le m\le n\le17\) and \(1\le d\le23\): 2,760 cases. The only nonrefinable cases are \((m,n,d)=(L,L,L)\) for \(3\le L\le17\). Its reproducible recorded output is `verification_output.txt`. A separate direct enumeration of exact automorphisms for 70 cases with \(3\le m\le n\le6\) and \(1\le d\le7\) confirmed the orbit prediction. The finite checks are corroboration; the proof establishes all parameter values.

## Relationship to prior work

Krebs and Verbitsky [KV14, §2.3, Lemma 2.6] proved the universal-cover/color-refinement correspondence used in Step 1, and studied *general lower bounds on depth*, not this barbell orbit classification. Arvind, Köbler, Rattan and Verbitsky [AKRV15, pp. 3--4, §8] define `refinable`, prove general inclusions between graph classes, and discuss generic separations; their inspected text does not state this exact cycle-barbell criterion. Kiefer, Schweitzer and Selman [KSS15, introduction and classification sections] classify graphs *identified among all graphs* by two-variable counting logic; this is distinct from recovering automorphism orbits of the specific graph.

The special case \(B(3,3,3)\) is a previously identified small graph whose stable 1-WL partition does not equal its automorphism-orbit partition. The present result does *not* claim that finite example as new: it classifies every member of a natural infinite three-parameter family and proves that **only** the diagonal \(m=n=d\) fails refinability, including the exact class-merger count for each diagonal member. A broader theorem giving this entire equivalence is not established by the inspected results, but historical priority remains provisional.

## Limitations

This statement does not determine exact stabilization rounds, decide absolute \(C^2\)-identifiability of each barbell relative to all graphs, classify all cactus or bicyclic graphs, or address vertex-colored refinement. It uses a standard universal-cover correspondence as a starting lemma; originality is claimed only for the parameter-complete barbell classification. A general published or unpublished cactus theorem could imply it, and independent historical-priority verification has not been performed. Computational checks are finite and are not an infinite proof. The result is not independently audited.

## References

[KV14] A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, first arXiv posting 2014-07-11, arXiv:1407.3175, especially §2.3 Lemma 2.6. https://arxiv.org/abs/1407.3175

[AKRV15] V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, first arXiv posting 2015-02-04, arXiv:1502.01255, especially pp. 3--4 and §8. https://arxiv.org/abs/1502.01255

[KSS15] S. Kiefer, P. Schweitzer, and E. Selman, *Graphs Identified by Logics with Counting*, first arXiv posting 2015-03-30, arXiv:1503.08792, especially introduction and graph-identification classification. https://arxiv.org/abs/1503.08792
