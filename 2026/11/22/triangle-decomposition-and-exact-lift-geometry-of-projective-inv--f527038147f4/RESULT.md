# Triangle decomposition and exact lift geometry of projective involutions over dual numbers

## Finding
Let \(q\) be any odd prime power, \(k=\mathbb F_q\), \(R=k[\varepsilon]/(\varepsilon^2)\), and \(P=\operatorname{PGL}_2(R)\). Define the simple **involution commuting graph** \(\Gamma(P)\) whose vertices are elements of exact order two in \(P\), with an edge between distinct commuting vertices. Denote by \(\pi:P\to\operatorname{PGL}_2(k)\) reduction modulo \(\varepsilon\).

**Theorem.** The graph \(\Gamma(P)\) has exactly \(q^4\) vertices. It has precisely two degrees:

\[
\begin{array}{c|c}
\text{degree}&\text{number of vertices}\\ \hline
q(q-1)&q^3(q+1)/2\\
q(q+1)&q^3(q-1)/2
\end{array}
\]

Each reduction fiber over a residue-field involution contains \(q^2\) vertices and is independent. Between fibers above two *different commuting* residue-field involutions, the induced bipartite graph is exactly a disjoint union of \(q\) copies of \(K_{q,q}\); above noncommuting residue-field involutions there are no edges. Every edge of \(\Gamma(P)\) belongs to exactly one triangle, and all maximal cliques are triangles. Consequently

\[
|E(\Gamma(P))|=\frac{q^4(q^2-1)}2,\qquad
\#\{\text{triangles}\}=\frac{q^4(q^2-1)}6.
\]

In particular there are \(q^6\) ordered commuting pairs of exact-order-two elements, including equal pairs, and \(q^4(q^2-1)/6\) embedded Klein four subgroups in \(P\). The reduction of each Klein four subgroup is injective, and exactly \(q^3\) Klein four subgroups lift each Klein four subgroup of \(\operatorname{PGL}_2(k)\).

## Assumptions and scope
The ring is the *split dual-number ring* of length two, not a Witt-vector ring or \(\mathbb Z/p^2\mathbb Z\). The field has odd characteristic, including \(q=3\), and may be a nonprime prime power. The graph excludes the identity and excludes loops. An involution is an element of exact order two, not an arbitrary element whose square is the identity. The counts are for actual elements and embedded subgroups, not conjugacy classes.

## Proof
**1. The reduction kernel.** The inclusion of constants splits the reduction homomorphism. Every element of the kernel has a representative \(I+\varepsilon X\), \(X\in M_2(k)\), unique modulo scalar matrices. Because \(2\in k^\times\), each class has a unique trace-zero representative, giving an isomorphism of groups
\[
P\cong V\rtimes H,\quad V=(\mathfrak{sl}_2(k),+),\quad H=\operatorname{PGL}_2(k),
\]
where \(H\) acts on \(V\) by conjugation and \(\dim_k V=3\). Thus the kernel has odd order \(q^3\). Any order-two element of \(P\) reduces to a nonidentity involution of \(H\). If \(t\in H\) is an involution, its lifts of exact order two are precisely \((x,t)\) with \((1+t)x=0\) in the adjoint representation.

**2. Involutions of the residue field group.** Each \(t\in H\) of order two has a nonsingular trace-zero matrix representative \(A\) with \(A^2=aI\). The adjoint action has a one-dimensional \(+1\)-space \(kA\) and a two-dimensional \(-1\)-space \(V_t^-\). Hence every \(t\) has \(q^2\) involutive lifts. The split residue-field involutions (those with two fixed points on \(\mathbb P^1(k)\)) are indexed by unordered pairs of distinct points: there are \(q(q+1)/2\). All other residue-field involutions are nonsplit, and their number is \(q(q-1)/2\), since the total is \(q^2\). The centralizer of a split involution is the normalizer of a split torus, a dihedral group of order \(2(q-1)\); that of a nonsplit involution is the normalizer of a nonsplit torus, of order \(2(q+1)\). Each is dihedral with the original involution as central half-turn. Since \(q\pm1\) are even, the centralizer has respectively \(q-1\) or \(q+1\) other involutions.

**3. Exact lifting of edges.** If \(s,t\in H\) do not commute, no pair of their lifts commutes. If \(s=t\), then \((x,t)\) and \((y,t)\), with \(x,y\in V_t^-\), commute exactly when \(x=y\), as \((1-t)(x-y)=2(x-y)\). Thus each fiber is independent.

Suppose now that \(s\ne t\) are commuting involutions in \(H\). Choose trace-zero nonsingular matrix representatives \(A,B\) for \(t,s\). Projective commutation gives \(AB=\lambda BA\) with \(\lambda^2=1\). If \(\lambda=1\), the trace-zero part of the matrix centralizer of \(A\) is \(kA\), contradicting \(s\ne t\); therefore \(AB=-BA\). The matrices \(A,B,AB\) are a basis of \(V\), and the simultaneous adjoint eigenspaces give
\[
V_t^-=kB\oplus kAB,\qquad V_s^-=kA\oplus kAB.
\]
For the two involutive lifts, the semidirect product multiplication says that they commute precisely when
\[
(1-s)x=(1-t)y.
\]
Writing \(x=\beta B+\gamma AB\) and \(y=\alpha A+\delta AB\), this equality is \(\gamma=\delta\), while \(\alpha,\beta\) are arbitrary. The bipartite edges therefore partition into \(q\) separate complete bipartite graphs with \(q\) vertices on each side. This proves the fiber statement, and supplies exactly \(q^3\) ordered lift pairs for every *ordered* distinct commuting residue-field pair.

**4. Degrees and total counts.** A lift above a split residue-field involution meets \(q\) neighbors in each of the \(q-1\) other commuting residue involution fibers, so it has degree \(q(q-1)\). A nonsplit lift similarly has degree \(q(q+1)\). Multiplying the two base-type multiplicities by \(q^2\) gives the listed vertex counts. The number of ordered, distinct, commuting base involution pairs is
\[
\frac{q(q+1)}2(q-1)+\frac{q(q-1)}2(q+1)=q(q^2-1).
\]
Therefore the ordered commuting lift count including equal pairs is
\[
q^2\,q^2+q(q^2-1)q^3=q^6.
\]
The number of graph edges is one half of the number of ordered distinct commuting lift pairs.

**5. Unique triangles and subgroup lifts.** Whenever distinct involutions \(u,v\) commute, \(uv\) is a third nonidentity involution commuting with both. The reduction kernel has odd order, so reduction injects on any elementary abelian two-subgroup. No subgroup \(C_2^3\) embeds in \(H\): fixing any nontrivial involution, its centralizer is dihedral and has elementary abelian two-rank at most two. Thus \(u,v\) have no additional common involution neighbor; every edge lies in its unique triangle, and no larger clique exists. Dividing the number of ordered distinct commuting pairs by six counts these triangles and Klein four subgroups. For each Klein four subgroup of \(H\), one ordered generating pair has \(q^3\) commuting lift pairs, yielding exactly \(q^3\) subgroup lifts. This completes the proof.

## Verification
The standalone program `pgl2_dual_check.py` directly enumerates normalized projective matrices over the prime fields of orders three and five, then enumerates the trace-zero reduction kernel and all involutive lifts. It tests exact projective commutation, every degree, all ordered commuting pairs, and uniqueness of a common neighbor for every edge. On \(q=3\): \(81\) vertices, degree multiplicities \(54\) of degree \(6\) and \(27\) of degree \(12\), \(324\) edges and \(108\) triangles. On \(q=5\): \(625\) vertices, degree multiplicities \(375\) of degree \(20\) and \(250\) of degree \(30\), \(7,500\) edges and \(2,500\) triangles. These finite checks corroborate but do not replace the general argument for all odd prime powers.

## Relationship to prior work
The finite-field commuting-involution graph literature investigates linear groups and, notably, graph diameter (Baek–Han, arXiv:1610.07938). The work on centralizers of reductive group schemes studies purity and geometric flatness, including complications for nonreduced Artin bases (Cotner, arXiv:2203.15133), but not the finite graph and fiber incidence just proved. Work on representations of matrix groups over finite commutative rings (Crisp–Meir–Onn, arXiv:1704.05575) and on power-map images over length-two local rings (Panja–Roy–Singh, arXiv:2508.18952) concerns different invariants. Prior computations for characteristic-two \(\mathrm{SL}_2\) and a particular degree-two matrix-group product-order spectrum do not cover the all-odd-field projective graph. The classical dihedral centralizers in \(\mathrm{PGL}_2(k)\) are standard ingredients rather than claimed as new. No claim of proven global historical uniqueness is made.

## Limitations
The theorem requires odd characteristic and the split square-zero ring; it does not automatically extend to mixed-characteristic length-two local rings or to \(\operatorname{PSL}_2\). The full isomorphism type of the global graph is not claimed beyond its proven reduction-fiber adjacency description. The finite checker treats \(q=3,5\) and does not certify other fields. Historical-priority comparisons depend on accessible indexed literature and may miss a differently titled or unindexed equivalent statement.

## References
- S. Cotner, *Centralizers of sections of a reductive group scheme*, arXiv:2203.15133, first public 2022-03-28, https://arxiv.org/abs/2203.15133.
- S. Baek and C. Han, *Commuting involution graphs of linear groups*, arXiv:1610.07938, first public 2016-10-25, https://arxiv.org/abs/1610.07938.
- T. Crisp, E. Meir, and U. Onn, *Principal series for general linear groups over finite commutative rings*, arXiv:1704.05575, first public 2017-04-19, https://arxiv.org/abs/1704.05575.
- S. Panja, A. Roy, and A. Singh, *Power maps on General Linear groups over finite principal ideal local rings of length two*, arXiv:2508.18952, first public 2025-08-26, https://arxiv.org/html/2508.18952v1.
