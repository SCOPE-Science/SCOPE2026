# Exact intrinsic inradius of odd-cycle edge-midpoint simplices

## Finding

Let \(n\ge3\) be odd. Let \(u_i=\sqrt{n/(n-1)}(e_i-\mathbf1/n)\) be the vertices of the regular simplex of circumradius one, indexed by \(i\) modulo \(n\), and put \(v_i=(u_i+u_{i+1})/2\). In its intrinsic Euclidean metric the convex hull \(P_n=\operatorname{conv}\{v_i\}\) has inradius
\[
r_n=\frac{1}{(n-1)\sqrt{n+1}}.
\]
Its centroid \(0\) is the unique center of a largest inscribed ball, and all \(n\) facets are tangent. Equivalently, the standard odd-cycle graph-edge polytope \(\operatorname{conv}\{e_i+e_{i+1}\}\) has intrinsic Euclidean inradius \(2/\sqrt{n(n^2-1)}\); in the simplex normalization \(r_n\sim n^{-3/2}\).

## Proof

Put \(\alpha=\sqrt{n/(n-1)}\) and let \((Sz)_i=z_{i+1}\). The matrix of uncentered edge incidence columns is \(I+S^\mathsf T\). For odd \(n\), its kernel is zero: iterating \(z_{i+1}=-z_i\) around the cycle gives \(z_i=-z_i\). Hence the edge incidence columns, and therefore the midpoint vertices, are affinely independent. Their affine span is \(E=\mathbf1^\perp\), and their sum is zero, so the centroid is interior.

For a facet opposite \(v_i\), let \(w\in E\) be the oriented normal normalized by \(\langle w,v_j\rangle=1\) for \(j\ne i\). The omitted height is \(1-n\) by the sum of the vertices. Set \(z=(\alpha/2)w\); then \(z_j+z_{j+1}=1\) for \(j\ne i\) and \(z_i+z_{i+1}=1-n\). By cyclic relabeling let \(i=n-1\). The first \(n-1\) equations make the entries alternate between \(z_0\) and \(1-z_0\); the last reads \(2z_0=1-n\). Thus \((n+1)/2\) entries equal \(-(n-1)/2\), and \((n-1)/2\) equal \((n+1)/2\). Therefore \(\|z\|^2=n(n^2-1)/4\), giving \(\|w\|^2=(n-1)^2(n+1)\) and the same distance from \(0\) to every facet.

The center constraints at radius \(r\) are \(\langle w_i,c\rangle+r\|w_i\|\le1\) for all facets. The normals sum to zero by cyclic symmetry (their sum is cyclically invariant and in \(E\)). Summing bounds \(r\) by \(r_n\), which is attained at \(0\). At this radius every inequality is tight. The normals span \(E\), since a common orthogonal direction would make the intersection of their halfspaces unbounded. Thus \(c=0\). The formula for the ordinary graph-edge polytope follows by undoing the translation and the factor \(\alpha/2\).

## Relationship to prior work

Tran–Ziegler, *Extremal Edge Polytopes*, [arXiv:1307.6708](https://arxiv.org/abs/1307.6708), Example 3, gives the odd-cycle simplex and the even-cycle combinatorial description. That combinatorial result does not fix the intrinsic Euclidean inradius. Yi, [arXiv:2611.05421v2](https://arxiv.org/abs/2611.05421v2), concerns the complete regular-simplex midpoint configuration, not this cycle subhull. The catalogue result [*Exact Euclidean chord-distance shells of cycle edge polytopes inside the second hypersimplex*](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-exact-euclidean-chord-distance-shells-of-cycle-edge-polytopes-in--13ab26bd16cc) computes distances from external hypersimplex vertices, rather than from the centroid to supporting facets.

Even cycles are not claimed. Their midpoint hull is similar to the standard bipartite-cycle root polytope: change the signs of coordinates in one bipartition to send every root from the other part to that part to an edge incidence vector, then apply the simplex translation and uniform scaling. The prior [bipartite-cycle root-polytope result](https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-euclidean-support-plane-shells-and-an-incenter-parity-law-for-bi--2c6fea9ced07) gives the corresponding even-cycle inradius and center-dimension transition. No bipartition sign change is possible on an odd cycle. The odd formula quantifies the roundness of a natural, non-bipartite family in its canonical Euclidean embedding.

## Verification and limitations

The odd cases in the accompanying `verify.py` solve the rational facet-normal recurrence for odd \(3\le n\le25\) and compare the squared norms. The proof, not the finite check, establishes every odd order. The formulas are for the indicated metric and Hamiltonian-cycle selection, not all edge selections, the convex hull of signed edge roots, or arbitrary affine normalizations. Literature comparisons do not certify historical priority.
