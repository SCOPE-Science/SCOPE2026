# The complete Euclidean vertex-shell spectrum of cyclic cross-polytope sums

## Finding
For every integer \(n\ge5\), let
\[
P_n=\sum_{i=1}^{n}\operatorname{conv}\{e_i,-e_i,e_{i+1},-e_{i+1}\}\subset\mathbb R^n,
\qquad e_{n+1}=e_1.
\]
The vertices of \(P_n\) occupy exactly \(\lfloor n/2\rfloor\) distinct spheres centered at the origin. For every \(1\le k\le\lfloor n/2\rfloor\), the squared radius and number of vertices on the corresponding sphere are
\[
\rho_{n,k}^{2}=n+2k,
\qquad N_{n,k}=2^{n-k+1}\binom{n}{2k}.
\]
Thus the complete radial vertex enumerator is
\[
\sum_{v\in\operatorname{Vert}(P_n)}z^{\|v\|_2^2}
=\sum_{k=1}^{\lfloor n/2\rfloor}2^{n-k+1}\binom n{2k}z^{n+2k}.
\]
The unique minimum enclosing Euclidean ball has center \(0\) and squared radius
\[
R_n^2=n+2\lfloor n/2\rfloor=
\begin{cases}2n&n\text{ even},\\2n-1&n\text{ odd}.\end{cases}
\]
Its contact points are exactly the outer-shell vertices, numbering \(2^{n/2+1}\) for even \(n\), and \(n2^{(n+3)/2}\) for odd \(n\). The diameter is \(2R_n\); all diameter-attaining pairs, and no others, are antipodal pairs of outer-shell vertices.

## Assumptions and scope
All coordinates use the standard Euclidean inner product. The sum is a Minkowski sum of \(n\) genuine two-dimensional coordinate cross-polytopes (diamonds); there is no rescaling or recentering. The integer restriction \(n\ge5\) excludes the already separately analyzed complete-multipartite instances \(C_3\) and \(C_4\). An edge index \(i\) denotes the cycle edge joining coordinates \(i\) and \(i+1\) modulo \(n\). The claims concern **polytope vertices** and the convex body, not all lattice points of the body.

## Proof
**Exposed vertices and orientations.** For generic \(u\in\mathbb R^n\), choose its coordinates nonzero with pairwise distinct neighboring absolute values. The unique maximizer of the functional \(x\mapsto\langle u,x\rangle\) on the \(i\)-th diamond is \(\operatorname{sgn}(u_j)e_j\), where \(j\) is the endpoint of edge \(\{i,i+1\}\) with larger \(|u_j|\). Direct every cycle edge toward that endpoint. Along each directed edge the magnitude \(|u_j|\) strictly increases, so the resulting cycle orientation is acyclic. Conversely, every acyclic orientation admits a topological ordering with strictly increasing positive magnitudes along directed edges; assigning arbitrary independent signs to the coordinates gives a generic linear functional uniquely exposing the corresponding signed indegree vector. Every vertex can be exposed by some generic functional (choose a functional in the interior of its full-dimensional normal cone and perturb away from finitely many hyperplanes). Hence these are *all* vertices.

**Binary cycle words.** Encode the choice of winning endpoint for edge \(i\) by \(b_i\in\{0,1\}\), where \(b_i=1\) means the edge points to coordinate \(i\), while \(b_i=0\) means it points to coordinate \(i+1\). The resulting unsigned coordinate multiplicity is
\[
t_i=1+b_i-b_{i-1}\in\{0,1,2\},
\]
with indices read cyclically. The only directed cycles are the two uniform words, so the acyclic orientations are exactly the nonconstant binary words. Their number of transitions is even; write it as \(2k\), necessarily \(1\le k\le\lfloor n/2\rfloor\). Each such word has \(k\) entries of indegree zero, \(k\) entries of indegree two, and \(n-2k\) entries of indegree one.

There is no duplication among these unsigned vectors: if two binary words \(b,b'\) give the same \(t\), the differences \(b_i-b'_i\) are constant around the cycle. Any nonzero constant forces one word to be identically zero and the other identically one, which are both excluded. For each orientation, its \(n-k\) nonzero coordinates admit arbitrary independent signs, and distinct sign choices give distinct exposed vertices. The transition set is an arbitrary even-sized subset of the \(n\) cyclic boundaries; its size \(2k\) and one initial bit determine the entire word. There are therefore exactly \(2\binom n{2k}\) orientations with \(2k\) transitions, giving
\[
N_{n,k}=2\binom n{2k}\,2^{n-k}=2^{n-k+1}\binom n{2k}.
\]
Every vertex on this layer has
\[
\|v\|_2^2=k\cdot 2^2+(n-2k)\cdot1^2=n+2k.
\]
All these values are distinct and all layers occur, finishing the shell classification.

**Ball, contacts and diameter.** The body is centrally symmetric. Its largest vertex norm is \(R_n=\sqrt{n+2\lfloor n/2\rfloor}\); convexity of the Euclidean ball ensures that the radius-\(R_n\) ball centered at zero contains the entire body. If a ball centered at \(c\) contains antipodal outer vertices \(v\) and \(-v\), then
\[
\max\{\|v-c\|_2^2,\|-v-c\|_2^2\}\ge R_n^2+\|c\|_2^2.
\]
Thus no smaller ball exists, and equality for a minimum ball forces \(c=0\). Strict convexity of squared norm excludes any nonvertex convex combination of distinct vertices from the sphere; contacts are precisely the outer-shell vertices. Substituting \(k=\lfloor n/2\rfloor\) into the multiplicity formula yields the two parity-sensitive counts. Finally, \(P_n\) is contained in that ball, so any pair has distance at most \(2R_n\); equality in the triangle inequality for points in the ball forces an antipodal outer-shell pair, and all such pairs belong to the body.

## Verification
The accompanying standalone `verify.py` independently enumerates every one of the \(4^n\) sums of one signed endpoint from each diamond for \(3\le n\le7\), comparing squared outer radius and outer-contact count to the formulas. For \(3\le n\le5\), it further computes the convex hull of these endpoint sums and checks *every* predicted radial vertex-shell multiplicity against the numerical convex-hull vertex list. These are bounded corroborative tests; completeness in arbitrary dimension follows from the orientation and counting proof above, not the computation. The verifier requires Python, NumPy and SciPy and exits on any disagreement.

For instance, \(n=5\) has exactly \(320\) vertices on squared radius \(7\), and \(80\) on squared radius \(9\); the unique outer radius is \(3\), giving \(40\) diametral antipodal pairs. For \(n=6\), the squared shells are \(8,10,12\) with multiplicities \(960,480,16\).

## Relationship to prior work
Wang, Hou, Thawinrak, Liu and Dai introduced the graph-indexed Minkowski sums of coordinate cross-polytopes and studied lattice-point enumeration, support-enumerators, Ehrhart positivity and volume (arXiv:2608.16037v1, publicly available August 17, 2026). Their general graph-based formulation contains the present cycle-incidence instance, and their Proposition 3.5 provides general supporting inequalities; those facts are credited and **not** claimed as novel. The present conclusion instead classifies all Euclidean vertex radii, shell multiplicities, minimal enclosing sphere and its exact contacts for cycle-incidence sums. Comparisons with other public findings on graphical zonotopes, cycle symmetric-edge polytopes and complete-multipartite edge-diamond sums establish differences in the objects or exclude the non-complete-multipartite cycles \(n\ge5\). An unindexed equivalent metric enumeration remains possible; historical priority is not independently established.

## Limitations
The theorem is restricted to equal unit weights and the cycle-incidence family with \(n\ge5\); it does not determine analogous spectra for arbitrary graphs, arbitrary weights, or the whole lattice-point set. The numerical verifier tests only dimensions at most seven, with exact convex-hull shell lists through dimension five. This is a mathematical proof with finite corroboration, not an external independent audit or a claim of historical priority.

## References
Wang, H., Hou, Q., Thawinrak, W., Liu, Z., Dai, Z. *Counting Lattice Points in Minkowski Sums of Cross Polytopes*. arXiv:2608.16037v1 (first posted 2026-08-17). https://arxiv.org/abs/2608.16037.

Bastidas, J. A. *The polytope algebra of generalized permutahedra*. arXiv:2009.05876 (2020). https://arxiv.org/abs/2009.05876.
