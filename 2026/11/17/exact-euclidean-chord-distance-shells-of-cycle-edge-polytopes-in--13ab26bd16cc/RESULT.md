# Exact Euclidean chord-distance shells of cycle edge polytopes inside the second hypersimplex

## Finding
For an integer \(n\ge3\), use standard Euclidean coordinates \(e_0,\ldots,e_{n-1}\) in \(\mathbb R^n\), with subscripts understood modulo \(n\). Define the complete rank-two hypersimplex and the cycle edge polytope by
\[
H_n=\Delta(2,n)=\operatorname{conv}\{e_i+e_j:0\le i<j<n\},\qquad
P_n=\operatorname{conv}\{u_i=e_i+e_{i+1}:0\le i<n\}.
\]
For any distinct indices \(i,j\), write \(v_{ij}=e_i+e_j\) and \(\delta(i,j)=\min(|i-j|,n-|i-j|)\). The *complete squared-distance spectrum* from hypersimplex vertices to the cycle edge polytope is:

- For \(n=3\), all distances are zero.
- For \(n=4\), edges of the cycle have squared distance zero, while the two opposite pairs have squared distance \(1\).
- For every \(n\ge5\),
\[
\operatorname{dist}_2(v_{ij},P_n)^2=
\begin{cases}
0,&\delta(i,j)=1,\\
5/6,&\delta(i,j)=2,\\
3/4,&\delta(i,j)\ge3.
\end{cases}
\]

In particular, the *ambient Euclidean Hausdorff distance* has the exact, nonmonotone dimension dependence
\[
d_H(H_n,P_n)^2=\begin{cases}0,&n=3,\\1,&n=4,\\5/6,&n\ge5.\end{cases}
\]
For \(n=4\) the only farthest points of **the entire hypersimplex** are the two nonedge vertices \(v_{02}\) and \(v_{13}\). For each \(n\ge5\) the only farthest points are the \(n\) vertices \(v_{i,i+2}\), with the indices reduced modulo \(n\); these are the two-step chords. All nearest points of all hypersimplex vertices are unique. For \(n\ge6\), the second-largest squared vertex distance is \(3/4\), so the exact squared vertex-distance gap is \(1/12\); the three squared-distance levels \(0,5/6,3/4\) have respective multiplicities \(n,n,n(n-5)/2\).

An explicit formula describes every nearest point. If \(\delta(i,j)=1\), the projection is \(v_{ij}\) itself. For \(n=4\) and \(\delta(i,j)=2\), it is \((1/4)\sum_{k=0}^{3}u_k=(1/2)\mathbf1\). For \(n\ge5\) and \(j\equiv i+2\pmod n\), the projection is
\[
p_{i,j}=\frac13u_{i-1}+\frac16u_i+\frac16u_{i+1}+\frac13u_{i+2}.
\]
(The endpoints may be ordered in either direction to make the displayed congruence hold; the second-step orientation is unique for \(n\ge5\).) Finally, if \(n\ge6\) and \(\delta(i,j)\ge3\), the projection is
\[
p_{i,j}=\frac14(u_{i-1}+u_i+u_{j-1}+u_j).
\]

## Assumptions and scope
These are **unnormalized** incidence vectors \(e_i+e_j\), not the half-scaled barycenters. Distance is ambient Euclidean distance in \(\mathbb R^n\) with its usual dot product; it is not measured in an arbitrary affine realization of the polytopes. Since \(P_n\subseteq H_n\), the symmetric Hausdorff distance equals \(\max_{x\in H_n}\operatorname{dist}_2(x,P_n)\). In even order \(P_n\) is lower-dimensional than \(H_n\), but the same ambient metric is used. The statement concerns finite integers \(n\ge3\).

## Proof
**1. Euclidean projection certificate.** For any nonempty closed convex set \(K\), a proposed \(p\in K\) is the unique closest point to \(x\) if and only if \(\langle x-p,z-p\rangle\le0\) for all \(z\in K\). For \(P_n=\operatorname{conv}\{u_k\}\) it is enough to check the finitely many inequalities \(\langle x-p,u_k\rangle\le\langle x-p,p\rangle\). If \(p=\sum_k w_ku_k\) with \(w_k\ge0\), \(\sum_k w_k=1\), then these inequalities follow by showing that the numbers \(\langle x-p,u_k\rangle\) are bounded above by a common value attained at every \(k\) having \(w_k>0\).

**2. Adjacent endpoints and the four-cycle.** For a cycle edge \(v_{ij}=u_i\), the distance is zero. At \(n=4\), rotate the nonedge to \(x=e_0+e_2\). Take \(p=\frac14\sum_k u_k=\frac12\mathbf1\). The residual has entries \((1/2,-1/2,1/2,-1/2)\), squared norm \(1\), and dot product zero with every edge vector \(u_k\). The projection certificate applies; the opposite pair follows by rotation.

**3. Two-step chords for \(n\ge5\).** Rotate to \(x=e_0+e_2\) and take
\[
p=\tfrac13u_{n-1}+\tfrac16u_0+\tfrac16u_1+\tfrac13u_2.
\]
Its coordinate values are \(1/2\) at \(0,2\), \(1/3\) at \(n-1,1,3\), and zero elsewhere; the three off-target coordinates are distinct because \(n\ge5\). Thus \(r=x-p\) is \(1/2\) at the two target coordinates, \(-1/3\) at the three indicated other coordinates, and zero elsewhere. Consequently \(\|r\|_2^2=2(1/2)^2+3(1/3)^2=5/6\). Each of the four edge vectors in the displayed combination has \(\langle r,u_k\rangle=1/6\); every other cycle edge has both endpoints outside \(\{0,2\}\) and therefore satisfies \(\langle r,u_k\rangle\le0\). The projection criterion proves optimality and uniqueness.

**4. Long chords for \(n\ge6\).** If \(\delta(i,j)\ge3\), the two target vertices and their four cyclic neighbors are pairwise distinct where required (the two sets of neighbors are disjoint). Set \(p=\frac14(u_{i-1}+u_i+u_{j-1}+u_j)\). The residual \(r=v_{ij}-p\) equals \(1/2\) at \(i,j\), \(-1/4\) at their four distinct neighbors, and zero elsewhere. Therefore \(\|r\|_2^2=2(1/2)^2+4(1/4)^2=3/4\). All four active edges have \(\langle r,u_k\rangle=1/4\). Any other edge is incident to neither target and has \(\langle r,u_k\rangle\le0\); hence the projection criterion applies. There are no other cyclic distances.

**5. Hausdorff extremizers and rigidity.** The function \(x\mapsto\operatorname{dist}_2(x,P_n)\) is convex. Thus its maximum on \(H_n\) is already attained at some vertex. This establishes the formula for the Hausdorff distance. To exclude nonvertex maximizers, write any \(x\in H_n\) as \(\sum_a\lambda_av_a\), and let \(p_a\) be each vertex's unique projection, with residual \(r_a=v_a-p_a\). The point \(\sum_a\lambda_ap_a\) is in \(P_n\), so
\[
\operatorname{dist}_2(x,P_n)^2\le\left\|\sum_a\lambda_ar_a\right\|_2^2\le\sum_a\lambda_a\|r_a\|_2^2\le d_H(H_n,P_n)^2.
\]
The second inequality is strict whenever the representation puts positive weight on two different residual vectors. Equality in the last inequality requires every used vertex to be farthest. The two opposite four-cycle residuals are distinct; for \(n\ge5\), the two positive entries of a farthest residual identify its two-step-chord vertex uniquely. Thus no genuine mixture of distinct farthest vertices attains the maximum. The counts of each vertex shell follow by counting unordered pairs at cyclic distances \(1\), \(2\) and at least \(3\).

## Verification
The reproducible standalone program `checks/cycle_hypersimplex.py` verifies rational weight positivity, normalization, the projection variational inequalities for **every** unordered pair in every order \(3\le n\le40\), and the complete exact squared-distance level multiplicities. It checks 10,659 vertex pairs. For \(3\le n\le11\), it also solves 219 independent constrained quadratic programs using SciPy and compares their optima with the formulas; the largest squared-distance discrepancy in that run was approximately \(1.01\times10^{-14}\). All-dimensional conclusions are proved in the preceding argument, not inferred from these finite tests.

## Relationship to prior work
Tran and Ziegler defined edge polytopes as the hypersimplex's graph-induced subpolytopes, explicitly identified the complete-graph edge polytope with the rank-two hypersimplex, and described the cycle edge polytopes' dimensions and affine types (2013 preprint, 2014 publication, Example 3). Nagaoka and Tsuchiya developed reflexive completions and normality criteria for graph edge polytopes (first posted 17 December 2017). Martínez-Sandoval and Padrol analyzed convex dimensions and skeleton-preserving projections of hypersimplices (first posted 3 September 2019). These distinguishable structural questions do not in the inspected statements provide the present explicit *Euclidean nearest-point maps*, complete chord-distance spectrum, all-point farthest locus or dimension-four exception. The classical graph-edge-polytope model and standard convex-projection characterization are not new claims.

## Limitations
The distance values depend on the precise unnormalized embedding and Euclidean metric; abstract affine equivalence of edge polytopes does not preserve them. The second-largest gap is **only** a gap among hypersimplex vertices, since nonvertex points can approach a farthest vertex continuously. The four-cycle is a complete bipartite graph and is included to state the entire cycle family, not as a separately asserted new structural discovery. Historical priority cannot be guaranteed by nonexhaustive literature/database searches. No independent mathematical review or validation has been performed.

## References
1. T. Tran and G. M. Ziegler, *Extremal Edge Polytopes*, 2013 preprint, 2014 publication, arXiv:1307.6708, https://arxiv.org/abs/1307.6708.
2. T. Nagaoka and A. Tsuchiya, *Reflexive polytopes arising from edge polytopes*, first posted 2017-12-17, arXiv:1712.06078, https://arxiv.org/abs/1712.06078.
3. L. Martínez-Sandoval and A. Padrol, *The convex dimension of hypergraphs and the hypersimplicial Van Kampen–Flores Theorem*, first posted 2019-09-03, arXiv:1909.01189, https://arxiv.org/abs/1909.01189.
