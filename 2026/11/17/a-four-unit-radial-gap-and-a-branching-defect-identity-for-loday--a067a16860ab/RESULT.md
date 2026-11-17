# A four-unit radial gap and a branching-defect identity for Loday's associahedron

## Finding
For every integer \(n\ge3\), let \(\operatorname{Asso}(n)\) denote the canonical Loday associahedron with one vertex \(v(T)\) per plane full binary tree \(T\) with \(n\) internal nodes. With the inherited Euclidean metric in the affine hyperplane \(\sum_i x_i=\binom{n+1}{2}\), let \(b_n=\frac{n+1}{2}\mathbf1\) be its known vertex barycenter. At an internal tree node \(u\), write \(L_u,R_u\) for the numbers of leaves of its left and right subtrees.

The complete vertexwise radial-defect identity is
\[
\boxed{\|v(T)-b_n\|^2=\frac{n(n^2-1)}{12}+\sum_{u\in\mathrm{Int}(T)}L_uR_u(L_u-1)(R_u-1).}
\]
Every summand on the right is a nonnegative multiple of four. In particular, all vertex squared radii lie in the congruence class \(\frac{n(n^2-1)}{12}+4\mathbb Z_{\ge0}\).

The two smallest **distinct** squared vertex radii are exactly
\[
\boxed{\rho_1^2=\frac{n(n^2-1)}{12},\qquad\rho_2^2=\frac{n(n^2-1)}{12}+4.}
\]
Exactly \(2^{n-1}\) vertices attain \(\rho_1\); their trees are the *combs*, those with at least one leaf child at every internal node. Exactly \(2^{n-3}\) vertices attain \(\rho_2\); their trees consist of one balanced four-leaf subtree (three internal nodes) with a succession of \(n-3\) one-leaf attachments above it. Thus the squared separation of the first two radial shells equals four independently of dimension.

## Assumptions and scope
A plane full binary tree has either a leaf or an internal node with two ordered children. An \(n\)-internal-node tree has \(n+1\) leaves. Label its internal nodes in inorder by \(i=1,\dots,n\), and set \(v(T)_i=L_iR_i\). By Loday's standard vertex theorem these points are precisely the distinct vertices of the canonical associahedron. The metric is the ordinary inherited Euclidean metric, *not* the rotation-graph distance or an affine-invariant quantity. The theorem is about distances to the specified vertex barycenter, *not* about a minimum-enclosing sphere, a global circumcenter, or distances to the boundary.

For \(n=1,2\), the branching sum vanishes for every tree and there is only one squared-radius level; the asserted second shell therefore begins at \(n=3\).

## Proof
**Constant coordinate sum and center.** Each unordered pair of distinct leaves has exactly one lowest common ancestor; at that ancestor the two leaves belong to opposite child subtrees. Consequently, \(\sum_{u}L_uR_u=\binom{n+1}{2}\). The fact that the vertex barycenter of the standard Loday realization is \(b_n=\frac{n+1}{2}\mathbf1\) is known from the cited barycenter literature; the following radial identity can also be read simply as a distance-to-the-explicit-point statement without that prior theorem.

**Exact structural identity.** Define \(S(j)=\sum_{r=1}^{j}r^2=j(j+1)(2j+1)/6\), with \(S(0)=0\). If the root separates \(a\) left leaves and \(b\) right leaves, then \(n=a+b-1\). The root coordinate is \(ab\), while the remaining coordinates are those of its left and right subtrees. The elementary polynomial identity
\[
a^2b^2+S(a-1)+S(b-1)-S(a+b-1)=ab(a-1)(b-1)
\]
therefore gives, by induction on the number of internal nodes,
\[
\sum_{i=1}^n v(T)_i^2=S(n)+\sum_{u\in\mathrm{Int}(T)}L_uR_u(L_u-1)(R_u-1).
\]
Using \(\sum_i v(T)_i=n(n+1)/2\), subtract \(n((n+1)/2)^2\) from both sides. Since \(S(n)-n(n+1)^2/4=n(n^2-1)/12\), this is precisely the boxed radial identity, for every tree and every dimension.

**Quantization and equality.** Both \(L_u(L_u-1)\) and \(R_u(R_u-1)\) are even integers, so every local penalty is a multiple of four. It vanishes exactly when at least one child is a leaf. Thus total penalty zero occurs precisely for a comb; from the bottom cherry, each of the remaining \(n-1\) internal nodes can attach a new leaf on the left or on the right, giving exactly \(2^{n-1}\) trees.

If the total penalty is positive, it is at least four. Equality forces exactly one positive local term, which must have \(L_u=R_u=2\): indeed for integers \(a,b\ge2\), the smallest value of \(ab(a-1)(b-1)\) is four, attained only at \((a,b)=(2,2)\). Its two child subtrees are necessarily cherries. Every ancestor must have a leaf as its other child, and there can be no other internal node elsewhere. Conversely this construction has penalty exactly four. There is one balanced four-leaf base tree, followed by \(n-3\) independently left/right one-leaf extensions, giving \(2^{n-3}\) trees. This proves both the strict first gap and all equality cases.

## Verification
The standalone `verify.py` enumerates all plane full binary trees with \(1\le n\le11\), directly builds their Loday vertex coordinates, and independently accumulates their local branching penalties. It verifies the coordinate sum, exact identity, divisibility by four, the minimum-shell counts and the sharp second gap for every tree in that range (82,499 profiles). It also checks the root polynomial identity on 2,401 integer pairs. The check prints `LODAY_RADIAL_QUANTIZATION_CHECKS_PASSED profiles=82499 dimensions=11 algebraic_pairs=2401`. These finite computations corroborate the algebraic proof and are not a substitute for the arbitrary-dimensional induction.

## Relationship to prior work
Pilaud, Santos and Ziegler (first public version 15 May 2023) survey the canonical coordinates, associahedral realization and existing vertex-barycenter theorem. Hohlweg, Lortie and Raymond prove the barycenter coincidence, but a barycenter identity does not determine radial shells or tree-dependent quadratic defects. Padrol, Palu, Pilaud and Plamondon study the realization cone and the Loday construction; the inspected work does not state the present squared-radius decomposition. A published note on the exact **inradius** of Loday's three canonical polytopes studies distances to supporting *facets*, not distances from the barycenter to *vertices*: neither those contact facets nor its inradius imply the present defect or multiplicities.

The new result is a vertexwise identity and exact first two radial levels, not a restatement of the inradius, barycenter or rotation-graph diameter. Specific phrase and formula searches found no published claim covering it, but absence from located sources does not establish complete historical priority.

## Limitations
This is a canonical-realization-dependent result, not a metric invariant of an abstract associahedron. The formula classifies the two innermost **vertex** shells and constrains all others to a four-spaced arithmetic lattice; it does not claim every possible higher shell occurs. Older work on binary-tree imbalance statistics or an unpublished identity could imply the same result under other terminology. No independent mathematical audit has been performed.

## References
1. V. Pilaud, F. Santos and G. M. Ziegler, *Celebrating Loday's Associahedron*, arXiv:2305.08471v1, first posted 2023-05-15; *Archiv der Mathematik* 121 (2023), 559–601, https://arxiv.org/html/2305.08471v1 .
2. C. Hohlweg, J. Lortie and A. Raymond, *The Centers of Gravity of the Associahedron and of the Permutahedron are the Same*, *Electronic Journal of Combinatorics* 17 (2010), R72, DOI: 10.37236/344.
3. A. Padrol, Y. Palu, V. Pilaud and P.-G. Plamondon, *Associahedra for finite-type cluster algebras and minimal relations between g-vectors*, *Proceedings of the London Mathematical Society* 127 (2023), 513–588, DOI: 10.1112/plms.12543.
4. J.-L. Loday, *Realization of the Stasheff Polytope*, *Archiv der Mathematik* 83 (2004), 267–278.
