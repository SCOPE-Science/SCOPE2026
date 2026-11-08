# Sharp Euclidean outer spheres and contact multiplicities for complete-multipartite edge-diamond sums

## Finding
For a finite complete multipartite graph \(G=K_{a_1,\ldots,a_r}\) with \(r\ge2\), \(a_j\ge1\), and \(N=\sum_j a_j\), consider its **edge-diamond Minkowski sum**
\[
P_G=\sum_{\{u,v\}\in E(G)}\operatorname{conv}\{e_u,-e_u,e_v,-e_v\}\subset\mathbb R^N.
\]
This is a natural unweighted edge-indexed member of the cross-polytope Minkowski-sum family studied by Wang et al. (2026). Its ambient Euclidean minimum enclosing ball has **unique center \(0\)**. Let \(b_1\ge\cdots\ge b_r\) be the part sizes in decreasing order, \(S_0=0\), \(S_{j-1}=\sum_{i<j}b_i\), \(A=b_1\), and let \(m_s\) denote the number of multipartite classes of size \(s\). Then
\[
\boxed{R(P_G)^2=\sum_{j=1}^r b_jS_{j-1}^2,\qquad \operatorname{diam}_2(P_G)=2\sqrt{\sum_{j=1}^r b_jS_{j-1}^2}.}
\]
The contact points are **exactly** these: select a total ordering of the *labeled* multipartite classes in nonincreasing class size; for each vertex \(v\) of the \(j\)-th class set \(|x_v|=S_{j-1}\); choose the signs of all nonzero coordinates arbitrarily. This procedure lists each contact vertex once: signs are chosen only for nonzero entries and distinct admissible labeled class orders have different coordinate-absolute-value vectors. There are precisely
\[
\boxed{C(P_G)=2^{N-A}\prod_s m_s!}
\]
contact points and precisely \(C(P_G)/2\) unordered diametral pairs, namely antipodal pairs of contacts. For unequal bipartite class sizes \(p>q\), the radius is \(R^2=p^2q\) and there are \(2^q\) contacts; for \(p=q\), \(R^2=p^3\) and there are \(2^{p+1}\) contacts.

## Assumptions and scope
Every part is nonempty, there are at least two parts, all edges of the complete multipartite graph appear once with coefficient one, the standard coordinate vectors are orthonormal, and distances are the ambient Euclidean distances. Distinct part labels are retained even when sizes tie. The quantities \(R\) and \(\operatorname{diam}_2\) refer to the whole convex polytope, not solely to its displayed summand vertices. No arbitrary affine or anisotropic re-embedding is covered.

## Proof
**1. Center and reduction to orientations.** Each diamond is centrally symmetric, hence \(P_G=-P_G\). Let \(R_0=\max_{x\in P_G}\|x\|_2\). Any ball of center \(z\) containing both \(x\) and \(-x\), for a point \(x\) attaining \(R_0\), has squared radius at least
\[
\tfrac12\bigl(\|x-z\|_2^2+\|-x-z\|_2^2\bigr)=R_0^2+\|z\|_2^2.
\]
The origin-centered ball of radius \(R_0\) contains the polytope, so it is uniquely optimal.

Each point of the Minkowski sum is a convex combination of endpoint sums obtained by choosing for every edge \(\{u,v\}\) one of \(\pm e_u,\pm e_v\). The strictly convex function \(x\mapsto\|x\|_2^2\) attains its maximum only at vertices. For any fixed assignment of endpoints (ignoring signs), the largest squared norm is realized when every contribution to a given coordinate uses a common sign. If the chosen endpoint counts are \(d_v\), this maximum equals \(\sum_v d_v^2\), with signs freely chosen independently for coordinates with \(d_v>0\). An endpoint assignment is equivalent to orienting each graph edge toward its chosen endpoint, so
\[
R_0^2=\max_{\omega\text{ an orientation of }G}\Phi(\omega),\qquad \Phi(\omega)=\sum_{v\in V(G)}\bigl(\deg^-_\omega(v)\bigr)^2.
\]
Conversely every maximizing signed endpoint sum is exposed as a vertex, since a nonvertex on a line segment would have strictly smaller squared norm than the maximum. We now classify all maximizing orientations.

**2. Identical-part cloning is forced.** Take distinct vertices \(u,v\) in the same multipartite class; they are nonadjacent and have exactly the same neighbor set. For each common neighbor \(w\), write \(x_w=1\) if \(w\to u\), otherwise \(0\), and \(y_w=1\) if \(w\to v\), otherwise \(0\). Let \(c_w\) be the number of edges into \(w\) from vertices other than \(u,v\). Denote by \(\omega_{xx}\) the orientation replacing the incidences at \(v\) by the same pattern as at \(u\), and by \(\omega_{yy}\) the orientation replacing the incidences at \(u\) by the pattern at \(v\); all other edges stay fixed. The combined squared indegrees of \(u,v\), averaged across these two clones, equal twice their old combined contribution. At each common neighbor \(w\), the exact change obeys
\[
(c_w+2-2x_w)^2+(c_w+2-2y_w)^2-2(c_w+2-x_w-y_w)^2=2(x_w-y_w)^2.
\]
Consequently
\[
\Phi(\omega_{xx})+\Phi(\omega_{yy})-2\Phi(\omega)
=2\sum_{w\sim u}(x_w-y_w)^2.
\]
If one incidence differs, one clone strictly improves upon \(\omega\). Thus every maximizing orientation forces all vertices within any one multipartite class to have the same incidence pattern, which implies all cross-edges between any two classes point uniformly in a single direction. Every maximizing orientation therefore induces a tournament on the multipartite classes.

**3. The class tournament is transitive.** Consider any oriented edge \(u\to v\) and let \(d_u,d_v\) be the indegrees before reversal. Reversing this edge changes the objective by
\[
(d_u+1)^2+(d_v-1)^2-d_u^2-d_v^2=2(d_u-d_v+1).
\]
At a global maximum this quantity must be nonpositive. Hence \(d_v\ge d_u+1\) along every directed edge. A directed cycle is impossible. The tournament on the classes is therefore acyclic and admits a total order, with all edges pointing from an earlier class to a later class.

**4. Class-size ordering and value.** For a class order \((b_1,\ldots,b_r)\), every vertex in position \(j\) has indegree \(S_{j-1}\), giving \(\Phi=\sum_j b_j S_{j-1}^2\). For adjacent class sizes \(a,b\) with earlier class size sum \(S\), the objective of the arrangement \((a,b)\) minus that of \((b,a)\) is
\[
aS^2+b(S+a)^2-\bigl[bS^2+a(S+b)^2\bigr]=ab(a-b).
\]
Thus a global maximizing class order must be nonincreasing in size; and every such order achieves the displayed maximum. This proves the radius formula and gives **all** maximizing orientations, not only one witness.

**5. Contact points, counts and diameter.** In the maximizing class orders, the indegree pattern has one zero-coordinate class of size \(A\) and all remaining \(N-A\) coordinates strictly positive. Since the \(m_s\) labeled classes of each size \(s\) can be permuted independently, there are \(\prod_s m_s!\) maximizing class orders. Different orders produce distinct nonnegative indegree vectors because the zero class, and subsequently the next unique prefix class, can be recovered from the distinct increasing coordinate values. For each vector, all \(2^{N-A}\) sign patterns on its positive coordinates are distinct. Two such signed points corresponding to different class orders have different absolute-value vectors, so do not coincide. Their count is \(C(P_G)\) as claimed. Every contact point is a vertex by strict convexity as above, and no others exist because every maximizing endpoint selection has been classified.

If \(x,y\in P_G\), the enclosing-ball bound gives \(\|x-y\|_2\le\|x\|_2+\|y\|_2\le2R_0\). Equality forces \(\|x\|_2=\|y\|_2=R_0\) and \(y=-x\). Each contact has its negative as another contact and none is zero, giving exactly \(C(P_G)/2\) diametral pairs and diameter \(2R_0\).

## Verification
`verify.py` uses exact integer arithmetic and the standard Python library. It enumerates all multipartite part-size integer partitions with total order \(2\le N\le6\) and at least two parts (23 instances), exhaustively tests all 71,030 edge-orientation bit assignments for the squared-indegree maximum, and compares the complete maximizing indegree and signed-contact sets to the theorem. It also explicitly constructs all signed endpoint sums of the diamonds and checks their Euclidean maximum and exact contact set for seven graphs with \(N\le4\). Finally, six larger sample tuples check the predicted contacts and their squared norms, without claiming exhaustive verification in those higher dimensions. The unbounded result follows from the symbolic proof, not these finite checks. Run `python3 verify.py` from the extracted package directory; it prints an `OK` summary and raises an assertion if a check fails.

## Relationship to prior work
Wang, Hou, Thawinrak, Liu and Dai (2026) introduce the broader cross-polytope Minkowski-sum construction and prove lattice-point, Ehrhart, volume and boundary-enumeration statements, but their inspected full text does not supply an outer Euclidean ball, a contact count, or the present multipartite class-ordering criterion.

An accessible earlier classification of the same edge-diamond construction for cycle graphs proves the Löwner radius and contacts for \(C_n\). The present family intersects that scope at \(K_{1,1,1}=C_3\) and \(K_{2,2}=C_4\), and the formulas agree: respectively squared radii \(5,8\) and contact counts \(24,8\). That cycle theorem does not imply the classification for the infinite complete multipartite family (for example \(K_{3,2}\), \(K_{2,2,2}\), or general complete graphs). Its overlapping instances are credited rather than claimed as new.

A mathematically close published result, *Complete multipartite graphical zonotopes have cubic-moment circumspheres* (2026), treats the **different** standard graphical zonotope \(Z_G=\sum_{\{u,v\}}[e_u,e_v]\). Its squared circumradius is \((N^3-\sum_j a_j^3)/12\) and every total order of multipartite classes gives a farthest vertex. The present summands are four-vertex coordinate diamonds, not segments. For \(K_{3,2}\) the present squared radius is \(18\), whereas the standard graphical-zonotope squared radius is \(15/2\); its two class orders are both farthest, while only the size-3-first order is maximizing here. No affine-identification claim is made.

Borsik and Madarasi (2025/2026) study separable convex optimization over indegree polytopes, focusing on **minimizing** squared indegrees over acyclic orientations and algorithmic complexity, rather than the explicit **maximum** and all maximizers for multipartite graphs or the geometry of edge-diamond sums. Eur, Fink, Larson and Spink (2024) develop volume and lattice-point theory for type-B generalized permutohedra, not a Euclidean circumradius and complete contact classification. The equality classification here depends on a cloning inequality and a strict adjacent-class interchange not supplied by those treatments.

## Limitations
The theorem concerns unit-weight edge diamonds for complete multipartite simple graphs in their standard Euclidean coordinates. The classification can fail or need modification for nonmultipartite graphs, weighted edges, or arbitrary linear images. The present work does not prove a full Euclidean-radius theorem for all Minkowski sums of cross polytopes. Although the inspected primary sources and queried mathematical-result records provide no implication covering the theorem, a hidden equivalent statement in graph-orientation or type-B polymatroid terminology remains possible; historical priority is not independently certified.

## References
1. Hongyu Wang, Qilin Hou, Warut Thawinrak, Zhiyuan Liu, Ziyi Dai, *Counting Lattice Points in Minkowski Sums of Cross Polytopes*, arXiv:2608.16037, first publicly available 2026-08-17, https://arxiv.org/abs/2608.16037.
2. *Complete multipartite graphical zonotopes have cubic-moment circumspheres*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-multipartite-graphical-zonotopes-have-cubic-moment-circ--2fc427ff213b.
3. *Exact John and Löwner balls of edge-diamond sums over cycles*, accessible prior mathematical record, finding identifier 7a831878-29d7-40df-b377-b3ec627ecf07, arXiv:2608.16037 as motivating source (2026).
4. Nóra A. Borsik and Péter Madarasi, *Separable convex optimization over indegree polytopes*, arXiv:2509.06182, first public 2025-09-07, https://arxiv.org/abs/2509.06182.
5. Christopher Eur, Alex Fink, Matt Larson, Hunter Spink, *Signed permutohedra, delta-matroids, and beyond*, Proceedings of the London Mathematical Society 128 (2024), e12592, DOI 10.1112/plms.12592.
