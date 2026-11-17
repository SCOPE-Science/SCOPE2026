# A five-edge saturation law for Hausdorff approximation of complete root polytopes by paths

## Finding

For every integer \(n\ge3\), equip the zero-sum Euclidean subspace \(H_n=\{x\in\mathbb R^n:\sum_{k=1}^n x_k=0\}\) with the ordinary inherited Euclidean metric. Define the complete type-A symmetric root polytope and its path subpolytope by
\[
Q_n=\operatorname{conv}\{\pm(e_i-e_j):1\le i<j\le n\},\qquad
P_n=\operatorname{conv}\{\pm(e_i-e_{i+1}):1\le i<n\}.
\]
Then \(P_n\subset Q_n\), and their exact Euclidean Hausdorff distance is
\[
\boxed{d_H(Q_n,P_n)^2=\begin{cases}
\frac12,&n=3,\\
\frac45,&n=4,\\
\frac9{10},&n=5,\\
\frac{11}{12},&n\ge6.
\end{cases}}
\]
The only farthest points in the *whole* convex body \(Q_n\) are \(\pm(e_1-e_n)\), the antipodal longest path roots. In particular, the Hausdorff distance becomes independent of the number of path vertices as soon as the path has six vertices.

There is also an exact localization law for the distances of all long roots. If \(1\le i<j\le n\) and \(j-i\ge5\), then
\[
\boxed{\operatorname{dist}(e_i-e_j,P_n)^2=
\begin{cases}
\frac{11}{12},&i=1\text{ and }j=n,\\
\frac56,&\text{exactly one of }i=1\text{ and }j=n\text{ holds},\\
\frac34,&i>1\text{ and }j<n.
\end{cases}}
\]
Thus, once the path separation reaches five edges, the distance depends only on whether either root endpoint is a graph endpoint, and not on the separation. For every \(n\ge7\), the second-largest squared distance **among the root vertices of \(Q_n\)** equals \(5/6\), attained at exactly \(4(n-6)\) oriented roots, namely the positive and negative roots having exactly one graph endpoint and path separation at least five. The resulting sharp vertex-distance squared gap is \(1/12\). This second-level assertion does not concern arbitrary nonvertex points of \(Q_n\).

## Assumptions and scope

Every graph edge \(\{i,j\}\) contributes both vectors \(\pm(e_i-e_j)\), without any rescaling by graph distance. All Euclidean distances are computed in the inherited standard-coordinate metric of \(\mathbb R^n\), or equivalently in the intrinsic Euclidean metric of \(H_n\). The result concerns the exact metric approximation of the complete-graph symmetric edge polytope by the path's symmetric edge polytope, not the covering radius of a discrete set and not the inradius of either polytope.

Put \(b_k=e_k-e_{k+1}\) for \(1\le k<n\), and let \(B\) be the matrix with these \(n-1\) columns. They are a basis of \(H_n\); consequently
\[
P_n=\{Ba:a\in\mathbb R^{n-1},\ \|a\|_1\le1\}.
\]
Let \(v_{ij}=e_i-e_j\). Because distance to a closed convex set is convex, its maximum over \(Q_n\) is achieved at a signed root \(\pm v_{ij}\). Central symmetry permits consideration of \(i<j\) alone.

## Proof

**Projection certificate.** For a proposed coefficient vector \(a\) with \(\|a\|_1=1\), set \(r=v_{ij}-Ba\), and \(g_k=\langle b_k,r\rangle=r_k-r_{k+1}\). The vector \(Ba\) is the unique Euclidean projection of \(v_{ij}\) onto \(P_n\) if, for some \(\lambda\ge0\),
\[
g_k=\lambda\operatorname{sgn}(a_k)\quad(a_k\ne0),\qquad
|g_k|\le\lambda\quad(a_k=0).
\tag{1}
\]
Indeed, these are exactly the subgradient optimality conditions for minimizing the strictly convex objective \(\|v_{ij}-Ba\|_2^2/2\) subject to \(\|a\|_1\le1\); strict convexity holds since \(B\) is injective. We use these inequalities both as verifiable lower-bound certificates and to construct the optimal projections explicitly.

**Longest roots.** Fix \(i=1,j=n\). For \(n=3,4,5\), the respective coefficient vectors in the ordered path-root basis are
\[
\left(\frac12,\frac12\right),\qquad
\left(\frac25,\frac15,\frac25\right),\qquad
\left(\frac25,\frac1{10},\frac1{10},\frac25\right).
\]
Each has \(\ell_1\)-norm one. Direct substitution in (1) gives a common nonnegative multiplier in each case, proving squared residual norms \(1/2\), \(4/5\), and \(9/10\).

For every \(n\ge6\), choose
\[
a_1=a_{n-1}=\frac5{12},\qquad a_2=a_{n-2}=\frac1{12},\qquad a_k=0\text{ otherwise}.
\]
Here the four indicated positions are distinct. The residual has first three entries \((7/12,1/3,1/12)\), last three entries \((-1/12,-1/3,-7/12)\), and all other entries zero. Its adjacent differences are \(1/4\) on the four active edges, and have absolute value at most \(1/4\) elsewhere. Therefore (1) holds with \(\lambda=1/4\). The squared norm is
\[
2\left[\left(\frac7{12}\right)^2+\left(\frac13\right)^2+\left(\frac1{12}\right)^2\right]=\frac{11}{12}.
\tag{2}
\]
This establishes the *exact* distance from each antipodal longest root to \(P_n\), rather than an upper bound.

**All roots with separation at least five.** Consider \(v_{ij}\) with \(j-i\ge5\). Define a coefficient vector by prescribing two disjoint local blocks:
\[
\begin{array}{ll}
\text{left block if }i=1:& a_1=5/12,\ a_2=1/12,\\
\text{left block if }i>1:& a_{i-1}=-1/4,\ a_i=1/4;\\
\text{right block if }j=n:&a_{n-2}=1/12,\ a_{n-1}=5/12,\\
\text{right block if }j<n:&a_{j-1}=1/4,\ a_j=-1/4.
\end{array}
\]
All unlisted coefficients vanish. In every case the total absolute coefficient sum is one. A graph endpoint contributes a residual block of squared norm \(11/24\), with coefficients \((7/12,1/3,1/12)\) up to reflection and sign. An interior endpoint contributes a residual block of squared norm \(3/8\), with coefficients \((1/4,1/2,1/4)\) up to reflection and sign. Because the endpoint separation is at least five, the blocks have disjoint supports. Every active-edge residual difference is \(\operatorname{sgn}(a_k)/4\), and every inactive-edge difference has modulus at most \(1/4\). Thus (1) applies with \(\lambda=1/4\). The possible squared norms are
\[
\frac{11}{24}+\frac{11}{24}=\frac{11}{12},\qquad
\frac{11}{24}+\frac38=\frac56,\qquad
\frac38+\frac38=\frac34.
\]
This proves the full stated localization law.

**Remaining shorter roots.** For any \(v_{ij}\) of path separation one, take the single corresponding edge coefficient equal to one; the error vanishes. For separation two, take coefficients \(1/2,1/2\) along the two-edge interval; the squared error is \(1/2\). For separation three, take coefficients \(2/5,1/5,2/5\) along its three-edge interval; the squared error is \(4/5\). These are feasible upper bounds, sufficient to prove that these roots are never farther than the longest root.

For separation four, unless the pair is the two graph endpoints (the already handled \(n=5\) case), use the same endpoint-local coefficient assignments as in the preceding paragraph: a graph-endpoint block \((5/12,1/12)\) or an interior-endpoint block \((-1/4,1/4)\) on the left and the corresponding reflected block on the right. All blocks have disjoint residual supports. This feasible point has squared error \(5/6\) if exactly one graph endpoint occurs, and \(3/4\) if neither occurs. Both are strictly less than the longest-root squared distance \(11/12\) for \(n\ge6\). The same upper-bound construction handles the separation-four pairs in \(n=5\) only when they are not the endpoint pair, so there is no conflict with the separate \(n=5\) exact certificate. Therefore all nonlongest vertices have strictly smaller distance than \(\pm v_{1n}\), and the Hausdorff formula follows.

**Farthest-point uniqueness in the entire convex polytope.** The continuous function \(x\mapsto\operatorname{dist}(x,P_n)\) is convex. Express any \(x\in Q_n\) as a convex combination of its signed root vertices. If its distance attains the maximum, every vertex in such a combination must be maximizing, hence only the pair \(\pm v_{1n}\) can occur. Thus \(x=t v_{1n}\) for some \(|t|\le1\). Since \(0\in P_n\), scaling a nearest point to \(v_{1n}\) shows
\[
\operatorname{dist}(t v_{1n},P_n)\le|t|\operatorname{dist}(v_{1n},P_n).
\]
Equality with the positive maximum demands \(|t|=1\). Hence precisely the two claimed points are farthest.

**The sharp second vertex shell.** If \(n\ge7\), long roots with exactly one graph endpoint have squared distance \(5/6\), and there are \(2(n-6)\) such unordered pairs, hence \(4(n-6)\) signed root vertices. Every other long root outside the maximizing pair has squared distance \(3/4\). Roots of separation at most three have squared distance at most \(4/5<5/6\); interior separation-four roots have squared distance at most \(3/4\). For a separation-four root with exactly one graph endpoint, the above feasible point has squared error \(5/6\), but it is **not** its nearest point: at the unique inactive edge joining the endpoint residual blocks the absolute residual difference is \(1/3\), whereas each active coefficient forces the multiplier in (1) to be \(1/4\). The necessary condition (1) fails; the actual minimum is therefore strictly smaller than \(5/6\). Consequently only the counted long roots attain the second level, completing the proof.

## Verification

The accompanying `verify_path_hausdorff.py` constructs exact rational projection coefficients and checks every active and inactive subgradient inequality (1) in every order \(3\le n\le40\), examining 10,659 unordered root pairs. It checks 7,770 long-root certificates and 2,886 short-root upper bounds, in addition to the longest-root cases. Independent constrained numerical quadratic programming reproduces the exact projections in 38 cases across orders three through ten with maximum squared-distance discrepancy below \(3\times10^{-14}\). The finite calculations corroborate the arbitrary-order analytical proof but do not replace it. Run `python3 verify_path_hausdorff.py` with Python 3, NumPy and SciPy to replay both stages.

## Relationship to prior work

D'Alì, Delucchi and Michałek introduce and investigate the same symmetric edge polytopes, including complete graphs, paths, and the finite-metric Kantorovich–Rubinstein realization. Their metric identification describes the vertices and convex body, but it does **not** determine the inherited Euclidean nearest-point projection of a long root to the path subpolytope. Chen, Davis and Korchevskaia characterize facets and facet subgraphs; D'Alì, Juhnke-Kubitzke, Köhne and Venturello study the \(\gamma\)-vector and \(h^*\)-theory. These results do not imply the present Euclidean Hausdorff saturation or root-distance shells.

A related published exact inball theorem for the *path* symmetric edge polytope determines the inradius, circumradius and incenter locus of \(P_n\), not the directed distance from \(Q_n\) to \(P_n\). Knowing the individual radii of two convex bodies cannot by itself determine the distance of each omitted complete-graph root to the smaller body; the certificates above give that missing information. Other published metric results for cross-polytopes and crown-graph root polytopes involve different convex bodies and do not imply the path-specific projection shells. The term *Hausdorff distance* is always used for the standard ambient Euclidean metric, not the graph shortest-path metric.

## Limitations

No classification is asserted for the exact projection distance of the roots with separation four, aside from sufficient sharp upper bounds and the strict exclusion from the second vertex shell. The second-largest-distance statement applies to the *finite root-vertex set*, not to arbitrary nonvertex points, whose distances can approach the maximum continuously. Weighted paths, other spanning trees, and other Euclidean normalizations are not covered. The result is a proved formula under the specified hypotheses; its historical priority remains provisional because some geometric optimization results may be indexed under related root-system, normed-space, or least-squares projection terminology.

## References

1. Alessio D'Alì, Emanuele Delucchi and Mateusz Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first posted 2019-10-11), *Electronic Journal of Combinatorics* 29 (2022), P3.24, DOI 10.37236/10387. https://arxiv.org/abs/1910.05193
2. Tianran Chen, Robert Davis and Evgeniia Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first posted 2021-07-26). https://arxiv.org/abs/2107.12315
3. Alessio D'Alì, Martina Juhnke-Kubitzke, Daniel Köhne and Lorenzo Venturello, *On the gamma-vector of symmetric edge polytopes*, arXiv:2201.09835 (first posted 2022-01-24). https://arxiv.org/abs/2201.09835
4. *Path symmetric edge polytopes have an exact inradius and a codimension-one incenter family*, publicly accessible mathematical research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-path-symmetric-edge-polytopes-have-an-exact-inradius-and-a-codim--4fbd84888e21
