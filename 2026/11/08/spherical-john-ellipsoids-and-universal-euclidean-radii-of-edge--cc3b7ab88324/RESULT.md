# Spherical John ellipsoids and universal Euclidean radii of edge-transitive bipartite perfect-matching polytopes

## Finding
Let \(G=(L\sqcup R,E)\) be any **finite, simple, connected, edge-transitive, \(d\)-regular bipartite graph**, with \(|L|=|R|=n\) and \(d\ge2\). Write \(m=nd\) and \(D=m-2n+1>0\). In its usual edge-coordinate Euclidean space, its perfect-matching polytope is
\[
P_G=\operatorname{conv}\{\mathbf1_M:M\text{ a perfect matching of }G\}\subset\mathbb R^E.
\]
Write \(u_e=1/d\) on every edge and let \(H=u+T\), where
\[
T=\{z\in\mathbb R^E:\sum_{e\ni v}z_e=0\text{ for all vertices }v\}.
\]
Then \(\dim H=D\), and **both** the largest inscribed Euclidean ball and the smallest enclosing Euclidean ball have \(u\) as their unique center. Their exact intrinsic radii are
\[
\boxed{\quad r_G=\sqrt{\frac{n}{d(nd-2n+1)}},\qquad R_G=\sqrt{\frac{n(d-1)}d},\qquad\frac{R_G}{r_G}=\sqrt{(d-1)(nd-2n+1)}.\quad}
\]
More strongly, the inball \(u+r_G B_T\) is the **unique maximum-volume inscribed ellipsoid** (John ellipsoid) of \(P_G\). Every edge-coordinate supporting hyperplane \(x_e=0\) touches this ball and provides an equal-weight John contact. Every perfect-matching incidence vector touches the enclosing sphere, and no nonvertex does.

For the zero-diagonal doubly stochastic (World Cup/derangement) polytope, \(G=K_{n,n}\) with the diagonal matching deleted, so for \(n\ge3\)
\[
\boxed{\quad r_G^2=\frac{n}{(n-1)(n^2-3n+1)},\quad R_G^2=\frac{n(n-2)}{n-1},\quad (R_G/r_G)^2=(n-2)(n^2-3n+1).\quad}
\]
The formulas hold for all indicated orders, not just the orders covered by currently available Ehrhart tables.

## Assumptions and scope
All norms and ellipsoid volumes are **intrinsic**, using the standard Euclidean inner product on \(\mathbb R^E\) restricted to the affine hull \(H\). The graph is finite, simple, connected and edge-transitive, and the two bipartition classes have \(n\) vertices each. Each vertex has degree \(d\ge2\), so \(2\le d\le n\); \(G\) is allowed to be a cycle and \(D=1\). An ellipsoid means a full-\(D\)-dimensional Euclidean ellipsoid in \(H\). The centroid and external Euclidean geometry in \(\mathbb R^{2n}\) are not involved. A spherical John ellipsoid need not be a spherical Löwner ellipsoid; **no** outer Löwner-ellipsoid formula is claimed.

The proof in fact needs only the weaker hypothesis that the \(m\) diagonal entries of the orthogonal projector onto \(T\) are equal; edge transitivity is a transparent sufficient condition. The universal enclosing-ball formula alone holds for **every** connected \(d\)-regular bipartite graph on \(2n\) vertices, without edge transitivity.

## Proof
**1. Affine hull and matching vertices.** Let \(A\) be the unsigned vertex-edge incidence matrix. Its rank is \(2n-1\): multiplying the equations on one bipartition by \(-1\) makes \(A\) an oriented incidence matrix, whose rank for a connected graph is \(2n-1\). Thus \(T=\ker A\) has dimension \(D=m-2n+1\). The uniform vector \(u_e=1/d\) satisfies \(Au=\mathbf1\). Every \(d\)-regular bipartite graph is a union of \(d\) edge-disjoint perfect matchings, by Hall's theorem applied successively. A standard Hall/support-subtraction argument shows
\[
P_G=\{x\in\mathbb R^E:x_e\ge0,\ Ax=\mathbf1\}.
\]
Indeed, every feasible nonnegative \(x\) has a perfect matching in its positive support: for a set \(S\) of left vertices, \(|S|\) units leave \(S\), and at most \(|N(S)|\) units can enter its right neighbors. Choose a supported matching and subtract its smallest matching-edge entry; renormalizing gives a smaller-support feasible matrix. Repetition yields a convex combination of matching vectors.

**2. Equal projected coordinate lengths.** Let \(\Pi\) denote orthogonal projection from \(\mathbb R^E\) onto \(T\), and set \(a_e=\Pi\mathbf e_e\) for each edge coordinate vector. A graph automorphism permutes coordinates, preserves \(T\), and commutes with \(\Pi\). Edge transitivity therefore makes \(\|a_e\|^2\) independent of \(e\). Since \(\sum_e\|a_e\|^2=\operatorname{tr}\Pi=D\), every edge satisfies
\[
\|a_e\|^2=D/m=:s^2>0,\qquad\sum_e a_e=\Pi\mathbf1_E=0,\qquad\sum_e a_ea_e^{\mathsf T}=I_T.
\]
The second equality holds because \(\mathbf1_E\) is orthogonal to \(T\) (every left-vertex tangent sum is zero). The third is the orthogonal resolution of identity on \(T\).

**3. Exact inball and unique incenter.** For \(x=u+z\in H\), the coordinate inequality \(x_e\ge0\) has intrinsic normal \(a_e\). Its supporting hyperplane is at distance \(x_e/s\) from \(x\). Hence \(u+rB_T\subset P_G\) exactly when \(r\le1/(ds)\). Conversely, any inscribed ball with center \(x\) and radius \(\rho\) requires \(x_e\ge\rho s\) for every \(e\). Summing over edges gives \(n=\sum_e x_e\ge m\rho s\), whence \(\rho\le n/(ms)=1/(ds)\). At equality, the nonnegative edgewise slacks all vanish: \(x_e=1/d\) for every edge. This proves both optimality and uniqueness, and
\[
r_G^2=1/(d^2s^2)=m/(d^2D)=n/(dD).
\]
For each edge, \(u-r_G a_e/s\) is a point of \(P_G\) on \(x_e=0\), because it is a boundary point of the contained ball.

**4. John-ellipsoid optimality.** Normalize the inball to the unit ball in \(T\). Its contact directions are \(v_e=-a_e/s\), all unit vectors. Choose positive weights \(c_e=D/m=s^2\). From step 2,
\[
\sum_e c_ev_e=0,\qquad\sum_e c_ev_ev_e^{\mathsf T}=I_T.
\]
The nonsymmetric version of John's contact characterization (John; see Gruber--Schuster, Theorem 2) now proves that the inball is the unique maximum-volume ellipsoid in \(P_G\). This conclusion does **not** require the edge-coordinate symmetry representation to be irreducible.

**5. Exact outer ball.** Each perfect-matching vector \(\mathbf1_M\) has precisely \(n\) entries equal to \(1\), and \(m-n\) zero entries. Consequently
\[
\|\mathbf1_M-u\|^2=n(1-1/d)^2+(m-n)/d^2=n(d-1)/d=:R_G^2,
\]
independently of \(M\). By step 1, every point of \(P_G\) is a convex combination of matching vertices, so \(P_G\subset u+R_GB_T\). The edge-disjoint matching factorization \(M_1,\ldots,M_d\) gives \(u=d^{-1}\sum_j\mathbf1_{M_j}\). For any candidate center \(y\in H\),
\[
\frac1d\sum_{j=1}^d\|\mathbf1_{M_j}-y\|^2=R_G^2+\|y-u\|^2.
\]
Thus no center other than \(u\) can have enclosing radius at most \(R_G\), proving uniqueness. Strict convexity of squared distance shows no nontrivial convex combination of distinct matching vertices lies on the circumsphere; only matching vertices contact it. Dividing the two radius formulas gives the stated aspect ratio.

**6. Deleted-diagonal specialization.** Deleting a perfect matching from \(K_{n,n}\) gives the connected crown graph, whose \(n(n-1)\) off-diagonal edges form one orbit under simultaneous permutation of row and column labels. Set \(d=n-1\), \(D=n^2-3n+1\) in the general formulas. The case \(n=3\) is a line segment; its unique inball and circumball coincide. The case \(n=2\) is a single point and is excluded from the positive-dimensional formula.

## Verification
The accompanying `verify.py` uses Python's standard library and exact rational arithmetic. Run `python3 verify.py`. It independently constructs row/column-incidence constraint matrices and orthogonal projectors through rational matrix inversion, checks projection rank/diagonal/idempotence and the moment identities, explicitly factorizes each tested regular graph into perfect matchings, and evaluates squared vertex radii. It passes for 15 graph instances: \(K_{n,n}\) for \(2\le n\le5\), crown graphs for \(3\le n\le6\), even cycles for \(4\le2n\le12\), and Boolean-cube graphs of dimensions \(3\) and \(4\). The code is supplementary finite verification; the proof above establishes all graph orders. No numerical optimizer or external mathematical certification is used.

## Relationship to prior work
Jiang--Xin--Zhang--Zhong (first public preprint September 22, 2026) study the Ehrhart series of Birkhoff polytopes and the deleted-diagonal World Cup model, providing a recent natural impetus to seek Euclidean geometric invariants of that same polytope. Their full relevant introduction and World Cup section address integer-point counts, not intrinsic ball or John-ellipsoid radii. Gruber--Schuster establish the general John contact characterization; the present explicit equal-leverage computation and universal graph-dependent radii are additional steps. Earlier exact inradius results for **unrestricted** positive-margin transportation polytopes cover the full Birkhoff special case, not the deleted-diagonal polytope. Results on **fractional matching polytopes** allow row and column sums at most one and therefore address a different, full-dimensional matching relaxation rather than this degree-equality section. The general fact that regular bipartite graphs admit perfect matching factorizations is classical and is not claimed as new.

## Limitations
The John-ellipsoid formula is proved for the intrinsic metric, not the ambient metric across additional zero coordinates. For arbitrary regular bipartite graphs without uniform projected coordinate norms, only the circumball assertion is proved. No exact Löwner ellipsoid, volume or Ehrhart polynomial is derived. Finite checks do not establish the infinite graph statement, and literature searches cannot prove historical novelty. Public abstracts of some related geometry results were available without their complete full texts; priority remains a genuine risk pending independent audit.

## References
1. X. Jiang, G. Xin, C. Zhang, and Y. Zhong, *Exact Ehrhart Series of Birkhoff Polytopes via Constant Terms and Finite-Field Evaluation*, arXiv:2609.25863, first posted 2026-09-22, https://arxiv.org/abs/2609.25863 .
2. P. M. Gruber and F. E. Schuster, *An Arithmetic Proof of John's Ellipsoid Theorem*, arXiv:1207.7246 (2012), Theorem 2, https://arxiv.org/abs/1207.7246 .
3. J. Edmonds, *Maximum matching and a polyhedron with 0,1-vertices* (1965), classical matching-polytope context; the bipartite equality description used above is also proved directly.
