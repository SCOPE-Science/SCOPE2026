# A parity law for antipodal pairs and the antipodal defect of regular antiprisms

## Finding
Let \(P_n\) be a right regular \(n\)-gonal antiprism with \(n\ge3\), any circumradius \(R>0\), and any separation \(2h>0\) between its parallel base planes. Two distinct vertices, respectively two distinct edge midpoints, form an *antipodal pair* when they lie on two parallel supporting planes of \(P_n\). Write \(A_n\) and \(B_n\) for these unordered pair counts and define the antipodal defect \(\delta_n=(2n-1)-A_n+B_n\).

Then the complete counts are
\[
 A_n=\begin{cases}n^2+2n,&n\text{ odd},\\n^2+n,&n\text{ even},\end{cases}\qquad
 B_n=\begin{cases}n^2+7n,&n\text{ odd},\\n^2+n,&n\text{ even},\end{cases}
\]
and
\[
 \boxed{\delta_n=\begin{cases}7n-1,&n\text{ odd},\\2n-1,&n\text{ even}.\end{cases}}
\]
All three are independent of the height-to-radius ratio. By the previously established antipodal-square-complex homology theorem of Phat, \(H_2(X(P_n);\mathbb Z)\cong\mathbb Z^{\delta_n}\). This homology implication uses an existing general theorem and is not an additional independent theorem.

## Assumptions and scope
The coordinates, with \(\theta=\pi/n\), are
\[
 b_j=(R\cos(2j\theta),R\sin(2j\theta),-h),\qquad
 t_j=(R\cos((2j+1)\theta),R\sin((2j+1)\theta),h)
\]
for \(j\in\{0,\ldots,n-1\}\), with indices taken modulo \(n\). The polyhedron \(P_n=\operatorname{conv}\{b_j,t_j\}\) has two \(n\)-gonal cap facets, \(2n\) triangular lateral facets, \(2n\) vertices and \(4n\) edges. The term 'antipodal' means opposite *supporting hyperplanes*, not necessarily centrally opposite positions, Euclidean diameter pairs, or unique support points. All counts concern distinct unordered pairs.

## Proof
**1. Vertex pairs.** The caps give every pair \(\{b_i,t_j\}\) as antipodal, contributing \(n^2\). If both points lie in one cap, the horizontal component of a supporting-plane normal must make them an opposite-support pair in the projected regular \(n\)-gon. A projected regular odd \(n\)-gon has precisely the two candidates \(\{b_j,b_{j+(n-1)/2}\}\) and \(\{b_j,b_{j+(n+1)/2}\}\) for each \(j\), which give \(n\) unordered pairs in each layer. They are genuinely supported by the whole antiprism: take a horizontal normal through \(b_j\) and adjust its vertical component so that the opposite-layer projected support interval, \([-R,R\cos\theta]\), is shifted onto the bottom interval \([-R\cos\theta,R]\). The required shift is exactly \(R(1-\cos\theta)\), achievable since \(h>0\).

For even \(n\), projected regular-polygon opposite-support pairs comprise diametric vertex pairs and the pairs from opposite parallel edges. The diametric pairs persist: choosing a radial horizontal normal produces a bottom interval \([-R,R]\) containing the other layer's interval \([-R\cos\theta,R\cos\theta]\). For a non-diametric pair from opposite parallel edges, the only horizontal exposing normal is an edge normal; the cap width in that normal is \(2R\cos\theta\), whereas the rotated opposite cap has width \(2R\). No vertical translation can put the larger interval inside the smaller one. Thus exactly \(n/2\) same-layer pairs remain in each layer. Together these prove \(A_n\).

**2. Opposite facial pairs and the defect.** We invoke Phat's established local normal-fan identity for a convex three-polytope:
\[
\delta(P)=\sum_{\{F,G\}\text{ exact opposite faces}}\bigl(e(F)e(G)-(v(F)-1)(v(G)-1)\bigr),
\]
where \(v(F)\) is the number of face vertices and \(e(F)\) its number of edges. In dimension three, only opposite facet-facet and edge-facet pairs contribute nonzero terms; for a pair of \(a\)- and \(b\)-gons the contribution is \(a+b-1\), and for a triangle opposite a single edge it is \(1\).

There is always one opposite pair of cap facets, contributing \(n^2-(n-1)^2=2n-1\). To classify lateral facets, set \(q=R(1-\cos\theta)/(2h)>0\). The \(n\) upper-edge triangular facets have outward supporting normals proportional to
\[
 U_j=(\cos(2j\theta),\sin(2j\theta),q),
\]
and the \(n\) lower-edge triangular facets have outward normals proportional to
\[
 L_j=(\cos((2j+1)\theta),\sin((2j+1)\theta),-q).
\]
Every such normal strictly exposes the indicated triangle: for \(U_j\) the vertices are \(b_j,t_{j-1},t_j\); for \(L_j\) they are \(t_j,b_j,b_{j+1}\). All other vertices have smaller dot product, because adjacent vertices are precisely the maximizers on each circular layer. The cap normals expose the opposite cap as a whole.

For odd \(n\), \(-U_j=L_{j+(n-1)/2}\), so the \(2n\) lateral facets form exactly \(n\) opposite triangle-triangle pairs. Each contributes \(3\cdot3-(3-1)^2=5\). For even \(n\), the negative of every lateral facet normal exposes a *single vertex* on the opposite layer: its horizontal direction lies halfway between none of that layer's vertices, but is exactly radial to one of them. Consequently no lateral facet is opposite any edge or facet, and no edge-facet contributions arise. The same is true for odd \(n\) except that lateral facets are opposite triangles. Thus there are no further terms, and the defect equals \(2n-1+5n\) for odd \(n\), or \(2n-1\) for even \(n\).

**3. Edge-midpoint pairs.** Rearranging the defining identity \(\delta_n=2n-1-A_n+B_n\) yields \(B_n=\delta_n-(2n-1)+A_n\), giving the stated formulas. No double-counting occurs because the definition and local theorem both concern unordered pairs.

**4. Height independence.** Positive changes of radius or height are invertible linear transformations of this standard realization. They preserve incidences of parallel supporting planes and hence all three counts.

## Verification
The accompanying `verify_antiprism.py` reconstructs the \(2n\) vertices and \(4n\) edges for \(n=3,\ldots,15\). For vertex pairs it solves a support-normal linear feasibility problem. For edge-midpoint pairs it tests normal directions perpendicular to both edge directions (or incident normal-cone generators for parallel edges). It independently obtains the values \((A_n,B_n,\delta_n)\) and checks all \(39\) resulting exact *integer count equalities* against the theorem's formulas. The geometric feasibility computations use numerical tolerances, and their finite sample is not a proof for arbitrary \(n\) or arbitrary real \(h,R\); the proof above supplies the universal conclusion.

## Relationship to prior work
Phat, *The Antipodal Defect of a Convex Polyhedron* (arXiv:2606.14599, publicly available from 2026-06-12), introduced the defect, the antipodal square complex and the local face-pair formula used here. The present calculation is the antipodal vertex/edge/defect census for the nonprismatic antiprism family, not a new construction of the general invariant. A separately indexed result, *Exact antipodal defect of every convex polygonal prism* (2026-11-08), deals with prisms, whose parallel lateral quadrilaterals have different opposite-face structure. A regular antiprism is not an affine prism; in particular, the parity-dependent presence of centrally opposite triangular lateral facets is absent in that prism comparison.

## Limitations
The formulas apply to right regular (not arbitrary skew or irregular) antiprisms with positive height. The new component is their exact pair census and parity transition. The general homological correspondence and local normal-fan formula are established earlier results. The complete 45-page primary preprint could not be inspected through the available routes, so the possibility of an earlier antiprism-specific example in that manuscript remains an explicit historical-priority risk. The finite checker is not an exhaustive proof or independent mathematical audit.

## References
1. Kieu Gia Thinh Phat, *The Antipodal Defect of a Convex Polyhedron*, arXiv:2606.14599, v1 (June 12, 2026). https://arxiv.org/abs/2606.14599
2. *Exact antipodal defect of every convex polygonal prism*, publicly indexed mathematical result (November 8, 2026), https://github.com/published-finding corpus/2026
