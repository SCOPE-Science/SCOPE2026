# Endpoint-conditioned rooted geodesic complexity of mixed Hamming products

## Finding

Let \(G=K_{q_1}\square\cdots\square K_{q_d}\), where \(d\ge2\), every \(q_i\ge2\), at least one \(q_i=2\), and at least one \(q_i\ge3\). Write \(b=|\{i:q_i=2\}|\) and \(t=|\{i:q_i\ge3\}|\), so \(b,t\ge1\) and \(b+t=d\). Define \(\operatorname{ipco}(G)\) as the smallest integer \(k\) for which some vertex \(r\) has the following property: the vertices of every single shortest path in \(G\) can be covered by at most \(k\) shortest paths, each having \(r\) as an endpoint. Then

\[
\boxed{\operatorname{ipco}(G)=1+t+\left\lfloor b/2\right\rfloor.}
\]

More precisely, fix *any* root \(r\) and endpoints \(u,v\). For each coordinate in which \(u\) and \(v\) differ, classify the change from \(u\) to \(v\) as an **erasure** when \(u_i\ne r_i=v_i\), an **addition** when \(u_i=r_i\ne v_i\), and a **replacement** when \(u_i,v_i,r_i\) are pairwise distinct. Let \(e,a,h\) be the respective numbers of these changes. Among all shortest \(u\)-to-\(v\) paths \(P\), the largest possible minimum number of \(r\)-rooted shortest paths covering \(V(P)\) is exactly

\[
\boxed{1+h+\min(e,a).}
\]

The second identity is terminal-conditioned and distinguishes different coordinate-change orders between the same endpoints. Both identities refer to vertex covers of a **single geodesic** by rooted geodesics, not a shortest-path cover of the entire graph.

## Assumptions and scope

All graphs are finite, simple, unweighted, and undirected. Each factor \(K_{q_i}\) is a complete graph with at least two vertices. Vertices of \(G\) are words \(x=(x_1,\ldots,x_d)\) with \(x_i\in\{0,\ldots,q_i-1\}\); adjacent words differ in exactly one coordinate. The distance is the Hamming distance, \(\mathrm d(x,y)=|\{i:x_i\ne y_i\}|\). An isometric path means a shortest path between its endpoints; a one-vertex path is permitted. A covering rooted path may contain vertices not in the path being covered. \(\operatorname{ipco}_r(G)\) fixes the root, whereas \(\operatorname{ipco}(G)=\min_r\operatorname{ipco}_r(G)\).

The genuinely mixed condition \(b,t\ge1\) is part of the theorem's novelty scope. Equal-alphabet special cases were previously studied and are not asserted to be new here.

## Proof

**1. Rooted reachability order.** For a fixed root \(r\), define \(x\preceq_r y\) if a shortest \(r\)-to-\(y\) path contains \(x\). Equivalently, \(\mathrm d(r,x)+\mathrm d(x,y)=\mathrm d(r,y)\). Coordinatewise Hamming distances give the exact criterion

\[
x\preceq_r y\quad\Longleftrightarrow\quad
(\forall i)\ [x_i=r_i\ \text{or}\ x_i=y_i].
\]

This relation is a partial order. Any chain \(x^{(1)}\preceq_r\cdots\preceq_r x^{(m)}\) lies on one \(r\)-rooted shortest path: its successive coordinate activations can be concatenated, because an activated coordinate never changes again. Conversely, vertices on any \(r\)-rooted shortest path form a chain. Thus Dilworth's theorem shows that, for a given path \(P\), the minimum number of \(r\)-rooted shortest paths covering \(V(P)\) equals the width of the restricted order \((V(P),\preceq_r)\). This equality uses arbitrary rooted paths in the graph, not paths constrained to lie in \(P\).

**2. Comparability along an arbitrary geodesic.** A shortest path from \(u\) to \(v\) changes every coordinate with \(u_i\ne v_i\) exactly once, and no other coordinate; every permutation of these changes gives a shortest path. Relative to \(r\), its changes have the three types stated above. Take path vertices \(x\) before \(y\). By the criterion in Step 1, they are incomparable precisely when the intervening path segment contains a replacement, or contains both an addition and an erasure. Indeed, a replacement leaves two different nonroot symbols in one coordinate and prevents reachability in both directions. Without replacements, additions alone give \(x\preceq_r y\), erasures alone give \(y\preceq_r x\), and the presence of both gives neither relation.

**3. Exact endpoint maximum.** Consider \(m\) vertices of one shortest \(u\)-to-\(v\) path that form an antichain, ordered by appearance. Their \(m-1\) successive intervening segments are disjoint. Each segment must contain either a replacement or at least one addition and one erasure. At most \(h\) segments can be charged to distinct replacements; the others can be charged to distinct addition-erasure pairs, of which there are at most \(\min(e,a)\). Hence

\[m\le 1+h+\min(e,a).\]

To attain this bound, choose a shortest path whose coordinate changes occur in this order: \(\min(e,a)\) successive erasure-addition pairs (each pair using different coordinates), then the \(h\) replacement changes, and finally all remaining one-sided changes. Select the initial path vertex, the vertex following each complete pair, and the vertex following each replacement. There are \(1+\min(e,a)+h\) selected vertices. Between any two selected vertices the path has a replacement or has both an erasure and an addition, so they are pairwise incomparable by Step 2. The width bound is attained. Step 1 converts it to the minimum number of rooted covering paths, proving the terminal-conditioned formula, including all zero-count boundary cases.

**4. Global upper bound.** For any endpoints, replacement changes require a nonbinary factor, so \(h\le t\). The other changed coordinates number at most \(b+t-h\), so \(e+a\le b+t-h\). Consequently

\[
h+\min(e,a)\le h+\left\lfloor\frac{b+t-h}{2}\right\rfloor
=\left\lfloor\frac{b+t+h}{2}\right\rfloor
\le t+\left\lfloor\frac b2\right\rfloor.
\]

The terminal-conditioned identity gives \(\operatorname{ipco}_r(G)\le1+t+\lfloor b/2\rfloor\) for every root \(r\).

**5. Sharpness for every root.** Fix any \(r\) and put \(k=\lfloor b/2\rfloor\). In every nonbinary coordinate choose distinct nonroot symbols for \(u_i\) and \(v_i\), making all \(t\) such coordinates replacements. In \(k\) binary coordinates choose an erasure, in \(k\) other binary coordinates choose an addition, and leave any remaining binary coordinate unchanged at the root. Then \(h=t\) and \(e=a=k\). The terminal-conditioned formula supplies a shortest path requiring \(1+t+k\) rooted paths. Since \(r\) was arbitrary, \(\operatorname{ipco}_r(G)=1+t+\lfloor b/2\rfloor\) for *every* root. In particular the minimum over roots has the announced value. \(\square\)

## Verification

Two standalone Python 3 programs accompany the result, without third-party dependencies.

- `check_ipco.py` enumerates all paths for twelve small Hamming products, computes antichain widths directly from coordinatewise comparability, checks the global formula, and independently solves the exact rooted-path set-cover problem on extremal short paths.
- `check_endpoint.py` enumerates every endpoint pair and every shortest path for five mixed/binary/nonbinary products, then compares the observed maximum width against \(1+h+\min(e,a)\).

Reproduce from the directory containing the files with `python check_ipco.py` and `python check_endpoint.py`. The recorded output is in `verification_output.txt`. Computations corroborate only the listed finite cases; the unrestricted theorem follows from the proof above. No randomized tests or unproved computer algebra are used.

## Relationship to prior work

The *isometric path antichain cover number* was introduced in Chakraborty et al. (ISAAC 2022, Definition 9); the subsequent study of isometric path complexity (MFCS 2023, Definition 1 and Lemma 7) identifies it with rooted geodesic covering by a Dilworth argument. Those papers establish structural bounds and approximation applications, not the terminal-conditioned mixed-factor formula above. Their known general statements are used only for context: Step 1 also gives a self-contained equivalence in the present graph class.

An earlier computation of \(\operatorname{ipco}(K_q^{\square d})\) for homogeneous alphabet size \(q\) already gives \(\lceil(d+1)/2\rceil\) for \(q=2\) and \(d+1\) for \(q\ge3\). These homogeneous cases are deliberately excluded from the asserted novelty scope. That separate calculation does not supply the fixed-endpoint extremal formula or the mixed-factor law; in mixed products the two types of coordinate contribute differently, with nonbinary replacements contributing individually and binary erasure/addition pairs jointly. The familiar *whole-graph* isometric path cover numbers of hypercubes or products of cliques concern different quantifiers and do not imply this theorem.

Published exact priority is not claimed beyond the documented comparisons. Search limitations and the closest scientific comparisons are recorded in the accompanying review.

## Limitations

The global exact formula is asserted for products having both binary and nonbinary complete-graph factors. It does not determine isometric path complexity of arbitrary Cartesian products of noncomplete graphs, and does not enumerate every path attaining maximum width. The endpoint-conditioned identity maximizes over shortest paths with fixed endpoints; it does **not** claim that every choice of coordinate-change order has that same covering number. The small-instance tests are not substitutes for the infinite proof. Independent mathematical audit and exhaustive historical priority verification are not included.

## References

1. D. Chakraborty, A. Dailly, S. Das, F. Foucaud, H. Gahlawat, and S. K. Ghosh, *Complexity and Algorithms for ISOMETRIC PATH COVER on Chordal Graphs and Beyond*, ISAAC 2022, DOI: https://doi.org/10.4230/LIPIcs.ISAAC.2022.12 (online 2022-12-14).
2. D. Chakraborty, J. Chalopin, F. Foucaud, and Y. Vaxès, *Isometric Path Complexity of Graphs*, MFCS 2023, DOI: https://doi.org/10.4230/LIPIcs.MFCS.2023.32; preprint https://arxiv.org/abs/2301.00278 (first posted 2022-12-31).
3. S. L. Fitzpatrick, R. J. Nowakowski, D. A. Holton, and I. Caines, *Covering hypercubes by isometric paths*, Discrete Mathematics 240 (2001), 253–260. This reference concerns global path covers, not the rooted single-path parameter.
