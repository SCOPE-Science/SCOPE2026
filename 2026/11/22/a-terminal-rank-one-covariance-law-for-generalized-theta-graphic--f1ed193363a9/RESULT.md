# A terminal rank-one covariance law for generalized-theta graphical zonotopes

## Finding

Let \(r\ge3\) and let \(\ell_1,\dots,\ell_r\ge2\) be integers, with at least one \(\ell_i\ge3\). Form the simple graph \(G=\Theta_{\ell_1,\dots,\ell_r}\) from \(r\) internally disjoint paths of lengths \(\ell_i\), all joining terminals \(s,t\). Let \(Z_G\subset\mathbb R^{V(G)}\) be the centered, unit-incidence graphical zonotope
\[
Z_G=\sum_{\{u,v\}\in E(G)}[-(e_u-e_v)/2,(e_u-e_v)/2].
\]
Choose \(X\) uniformly from the *distinct vertices* of \(Z_G\), not according to their normal-cone angles. For each path let \(L_i=\sum_{e\in E(P_i)}b_eb_e^{\mathsf T}\) be its ordinary incidence-Laplacian contribution (either choice of sign for each incidence column), and put \(v=e_s-e_t\).

Define the finite positive integers
\[
A_i=2^{\ell_i}-1,\quad D_i=2^{\ell_i}-2,\quad
N=2\prod_{i=1}^r A_i-\prod_{i=1}^rD_i,
\]
and the omitted-index products
\[
T_i=\prod_{j\ne i}A_j,\quad U_i=\prod_{j\ne i}D_j,
\quad T_{ij}=\prod_{k\notin\{i,j\}}A_k.
\]
Then \(\mathbb EX=0\) and the **entire Euclidean vertex covariance** is
\[
\boxed{
\operatorname{Cov}(X)=\frac14\left(
\sum_{i=1}^r\left[1+\frac{2(T_i-U_i)}N\right]L_i
+\frac2N\left[\sum_{i=1}^r(U_i-T_i)+2\sum_{i<j}T_{ij}\right]vv^{\mathsf T}
\right).
}
\]
Thus all nonlocal correction terms collapse to one matrix of rank at most one, supported on the two common terminals; the remaining terms are positive pathwise reweightings of the graph Laplacian. The displayed formulas determine all coordinate covariances, the exact inertia, and the mean squared separation of two independent uniform vertices by taking the trace.

For three equal-length paths \(\ell_i=\ell\ge3\), write \(q=2^\ell\), \(N=q^3-6q+6\), and \(L_G=\sum_iL_i\). The formula simplifies sharply to
\[
\boxed{
\operatorname{Cov}(X)=\frac14\left(1+\frac{4q-6}{N}\right)L_G
+\frac{3}{2N}vv^{\mathsf T}.
}
\]
For independent uniform vertices \(X,Y\), the exact squared Euclidean separation is
\[
\boxed{\mathbb E\|X-Y\|_2^2=3\ell+\frac{3\ell(4q-6)+6}{N}}
\]
and its excess over the independent-edge-sign benchmark \(3\ell\) is positive and asymptotic to \(12\ell\,4^{-\ell}\).

## Assumptions and scope

All graph vertices are labeled; path interiors are mutually disjoint, and no other edges are present. The paths are oriented for bookkeeping from the terminal \(s\) toward \(t\), so their incidence columns telescope to \(v\). All incidence segments have the same unit scaling, the ambient Euclidean norm is the standard coordinate norm, and the zonotope lies in the intrinsic \((|V(G)|-1)\)-dimensional subspace \(\mathbf1^\perp\). Acyclic orientations, and hence polytope vertices, are sampled uniformly without identifying graph automorphisms or orientation reversal. Empty products are one. The novel quantified domain requires at least one path of length three or more. The all-length-two graph is \(K_{2,r}\), whose uniform-vertex covariance spectrum was already evaluated; the displayed algebra also specializes to that known boundary case but no independent novelty is asserted there. No asymptotics in the number of paths are asserted.

## Proof

**1. Acyclic sign words and the vertex model.** Order each path's edges from \(s\) to \(t\). An edge orientation defines a sign \(S_e\in\{-1,1\}\) relative to that order. A directed cycle exists if and only if one entire path is all plus and some other entire path is all minus: any simple cycle must use two of the terminal paths, and the converse is immediate. Hence an acyclic sign array is one with no both-sign coherent paths. The standard graphical-zonotope normal-fan correspondence gives a bijection between distinct vertices and such arrays, with vertex coordinate
\[
X=\tfrac12\sum_{e\in E(G)}S_e b_e.
\]
Global sign reversal preserves the allowed arrays and negates \(X\), so \(\mathbb EX=0\).

**2. Count the sample space.** On path \(i\), there are \(A_i\) words excluding the all-minus word, \(A_i\) excluding the all-plus word, and \(D_i\) excluding both coherent words. Inclusion-exclusion therefore gives \(N=2\prod_iA_i-\prod_iD_i\) allowed arrays, which is strictly positive. This count is a known acyclic-orientation enumeration, not the claimed new invariant.

**3. Exact edge-sign second moments.** The diagonal entries of \(\mathbb E SS^{\mathsf T}\) are one. Fix distinct edges on path \(i\). Their sign product sums to \(2\) over the two coherent words and to \(-2\) over the mixed words, because the sum over the full binary cube is zero. Given a coherent word of either sign on path \(i\), each other path can independently use only its mixed words or the same coherent sign, yielding \(T_i\) possibilities. Given a mixed word, the other paths have \(2T_i-U_i\) legal assignments. The off-diagonal within-path sign correlation is consequently
\[
\alpha_i=\frac{2T_i-2(2T_i-U_i)}N=\frac{2(U_i-T_i)}N.
\]
For edges on *different* paths \(i,j\), any case where either path is mixed contributes zero after summing that path's edge sign over its mixed words. The only nonzero cases are the two choices in which both paths are coherent with the same direction. The other paths each exclude the opposite coherent direction, giving
\[
\beta_{ij}=\frac{2T_{ij}}N.
\]
These computations are exact for any \(r\ge3\) and all permitted path lengths.

**4. Push the covariance through the incidence map.** Write \(B_i\) for the matrix of incidence columns on path \(i\) and \(\mathbf1_i\) for the vector of ones of length \(\ell_i\). Then \(B_i\mathbf1_i=v\), by telescoping. The within-path sign correlation matrix is \((1-\alpha_i)I+\alpha_i\mathbf1_i\mathbf1_i^{\mathsf T}\); between paths \(i,j\) it is \(\beta_{ij}\mathbf1_i\mathbf1_j^{\mathsf T}\). Therefore
\[
4\operatorname{Cov}(X)=\sum_i(1-\alpha_i)L_i+
\left(\sum_i\alpha_i+2\sum_{i<j}\beta_{ij}\right)vv^{\mathsf T}.
\]
Substituting the moments from step 3 gives exactly the stated formula. Since \(T_i>U_i\), every path's Laplacian multiplier is strictly greater than one. No covariance sign assumptions or independence between distinct paths were imposed.

**5. Three equal paths and distances.** For \(r=3\) and common \(q\), \(T_i=(q-1)^2\), \(U_i=(q-2)^2\), and \(T_{ij}=q-1\). Thus \(\alpha_i=(6-4q)/N\) and \(\sum_i\alpha_i+2\sum_{i<j}\beta_{ij}=6/N\). This gives the simplified rank-one formula. Finally \(\operatorname{tr}L_G=2|E(G)|=6\ell\), \(\operatorname{tr}(vv^{\mathsf T})=2\), and for independent centered copies \(\mathbb E\|X-Y\|^2=2\operatorname{tr}\operatorname{Cov}(X)\). The exact distance identity follows. As \(q\to\infty\), \(N/q^3\to1\), so the positive excess has the asserted sharp asymptotic.

## Verification

The self-contained Python 3 program `verify_theta_covariance.py` enumerates *all* binary edge orientations for eight nontrivial parameter tuples, discards exactly the cyclic ones, independently accumulates the integer matrices \(\sum(2X)(2X)^{\mathsf T}\), and compares them entrywise with the integer-scaled analytic covariance formula. It tests unequal lengths, three through six terminal paths, the precise vertex counts, and full off-diagonal matrices. It prints `THETA_MULTIARM_COVARIANCE_EXACT_PASS` on success. Those finite tests support the implementation and normalization; the proof above establishes every integer parameter choice.

## Relationship to prior work

Padrol, Pilaud and Poullot establish the graphical-zonotope and acyclic-orientation framework and investigate deformation cones, not the uniform *vertex-coordinate covariance* considered here. Earlier general theta-graph results give the exact number of acyclic orientations and full local one-skeleton degrees; those are inputs or different statistics. The uniform-vertex covariance spectrum of \(K_{2,r}=\Theta_{2,\dots,2}\) was already obtained separately, so that full all-length-two specialization is expressly excluded from the novelty domain. Its symmetry and eigenvalue formulas do not determine the covariance of unequal subdivided theta arms. Published cactus graphical-zonotope covariance laws treat graphs whose cycles are edge-disjoint, unlike this family of overlapping terminal-to-terminal cycles. Their Laplacian-only block decomposition does not apply here; the explicit terminal rank-one term is the new feature.

## Limitations

This is a theorem for the canonical, uniformly weighted incidence realization and uniform distribution on distinct **vertices**. It is not a formula for uniform *volume* inside the polytope or for Gaussian objective exposure, both of which have different laws. It does not classify the eigenvalues of the resulting covariance matrix, extend to arbitrary edge weights, or establish that the result is absent from every unindexed source. Earlier exact orientation counts are not claimed as new; complete prior-art priority remains open to independent checking.

## References

1. A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first posted 24 November 2021, especially Section 1.3 and the introduction, https://arxiv.org/abs/2111.12422 and https://arxiv.org/html/2111.12422v2.
2. *Local flip degrees and simple graphical-zonotope vertices of generalized theta graphs*, published-finding corpus research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-local-flip-degrees-and-simple-graphical-zonotope-vertices-of-gen--23a76ec8b64b.
3. *Acyclic orientation counts within parity classes of multi-theta graphs*, published-finding corpus research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-acyclic-orientation-counts-within-parity-classes-of-multi-theta--c0aa7bda86b4.
4. *A sharp vertex–volume covariance sandwich for cactus graphical zonotopes*, published-finding corpus research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-vertex-volume-covariance-sandwich-for-cactus-graphical-z--b39706fc7ceb.
