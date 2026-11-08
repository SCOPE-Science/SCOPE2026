# Exact Ehrhart polynomial and a strict deletion-clustering effect for star-deleted complete graphs

## Finding

Let \(n\ge4\) and \(2\le k\le n-2\) be integers. Obtain \(G_{n,k}\) from the complete graph \(K_n\) by deleting exactly \(k\) edges incident to one distinguished vertex. Write \(P_{n,k}=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(G_{n,k})\}\) in the zero-sum Euclidean hyperplane \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), and let \(Q_{n,k}=P_{n,k}^{\circ}\subset H\) be its polar. Count lattice points in \(mQ_{n,k}\) using the dual root lattice \(A_{n-1}^{*}=\{x\in H:x_i-x_j\in\mathbb Z\ \forall i,j\}\).

**Exact Ehrhart and volume theorem.** For every integer \(m\ge0\), putting \(r=n-k-1\),

\[
L_{n,k}(m)=\#(mQ_{n,k}\cap A_{n-1}^{*})=(m+1)^n-m^n+2\bigl((m+1)^k-m^k\bigr)\sum_{s=1}^{m}s^r.
\]

The intrinsic Euclidean volume, measured with the metric inherited from \(H\), is

\[
\operatorname{vol}_{n-1}(Q_{n,k})=\frac{1}{\sqrt n}\left(n+\frac{2k}{n-k}\right).
\]

This provides the full Ehrhart polynomial, hence all Ehrhart coefficients and the complete Ehrhart series, for the entire two-parameter family.

**Strict effect of clustering the deleted edges.** If also \(2\le k\le\lfloor n/2\rfloor\), let \(R_{n,k}\) be the analogous polar for a graph obtained from \(K_n\) by deleting \(k\) pairwise disjoint edges. Then, for every integer \(m\ge1\),

\[
\#(mQ_{n,k}\cap A_{n-1}^{*})>\#(mR_{n,k}\cap A_{n-1}^{*}),
\]

and the intrinsic Euclidean volumes satisfy

\[
\operatorname{vol}_{n-1}(Q_{n,k})-\operatorname{vol}_{n-1}(R_{n,k})
=\frac{2k(k-1)}{(n-k)(n-1)\sqrt n}>0.
\]

Thus the position, not merely the number, of missing edges affects the entire polar Ehrhart count. Concentrating missing edges at one vertex strictly enlarges these counts relative to disjoint missing edges.
In particular, for every \(n\ge4\), every two-edge deletion of \(K_n\) is isomorphic to either a deleted two-edge star or a deleted two-edge matching. The strict comparison therefore gives the **complete geometric ordering of all two-edge deletions** at every positive Ehrhart dilation and for intrinsic volume.

## Assumptions and scope

The graph is simple, connected, and undirected. The condition \(r\ge1\) makes the distinguished vertex adjacent to at least one other vertex and hence makes the polar bounded. The common coordinates of the remaining \(n-1\) vertices form a clique. The deleted edges comprise a star, not a matching. The dimension is \(n-1\); the polar is defined relative to \(H\), not to the whole ambient space. The dual lattice is the coordinate-difference lattice, not the integer zero-sum lattice.

A rooted coordinate representative of each coset modulo global translation is obtained by setting the distinguished coordinate to zero. Translating this representative by its mean gives the corresponding point of \(H\). In this gauge, all remaining coordinates are integral if and only if the point lies in \(A_{n-1}^{*}\).

## Proof

Label the distinguished vertex \(0\), its \(k\) non-neighbors \(1,\ldots,k\), and the \(r=n-k-1\) remaining vertices \(k+1,\ldots,n-1\). The last group is called the core. The graph has all edges except \(\{0,j\}\) for \(1\le j\le k\). By polarity, a rooted integer potential \(x\) with \(x_0=0\) lies in \(mQ_{n,k}\) exactly when \(\lvert x_u-x_v\rvert\le m\) on every edge.

First count integer potentials whose **total range**, maximum minus minimum over all \(n\) coordinates, does not exceed \(m\). This count is the complete-graph baseline

\[
B_n(m)=(m+1)^n-m^n.
\]

To see this, quotient integral assignments by global translation, take the unique representative whose minimum equals zero, and count assignments in \(\{0,\ldots,m\}^n\) with at least one zero. This is a bijection with the rooted representatives \(x_0=0\).

Every feasible potential outside this baseline has total range greater than \(m\). The pair of vertices attaining the global minimum and maximum cannot be an edge. Since the only nonedges are \(\{0,j\}\), the distinguished vertex is an extreme vertex of the potential, and the opposite extreme occurs among its \(k\) non-neighbors. Negating the potential exchanges the two cases, so it suffices to enumerate the case in which \(x_0=0\) is the minimum and some non-neighbor exceeds \(m\).

Write the maximum value as \(m+h\), with unique integer \(h\in\{1,\ldots,m\}\). Every core coordinate lies in \(\{h,\ldots,m\}\): the distinguished vertex is adjacent to the core, so these coordinates are at most \(m\); the vertex realizing \(m+h\) is adjacent to every core vertex, so these coordinates are at least \(h\). Conversely, arbitrary choices in that interval are allowed; there are \((m-h+1)^r\) such choices.

All \(k\) non-neighbor coordinates must lie in \(\{h,\ldots,m+h\}\), because they form a clique and have maximum \(m+h\). At least one coordinate must attain that maximum. Hence there are exactly \((m+1)^k-m^k\) choices. These choices also satisfy every cross edge to the core: their minimum is at least \(h\), and their maximum exceeds the smallest core coordinate by at most \(m\). The number of high-range potentials with fixed \(h\) is therefore

\[
\bigl((m+1)^k-m^k\bigr)(m-h+1)^r.
\]

Summing over \(h\), multiplying by two for negation, and adding the baseline proves the Ehrhart formula. The argument includes \(m=0\), where the correction is empty.

For the volume, the rooted gauge map into \(H\) has Gram matrix \(I_{n-1}-\frac1n\mathbf1\mathbf1^{\mathsf T}\) and determinant \(1/n\). Thus rooted-coordinate volume must be divided by \(\sqrt n\) to obtain intrinsic Euclidean volume. Since the Ehrhart polynomial has degree \(n-1\), its leading coefficient is the rooted-coordinate volume. The baseline has leading coefficient \(n\). Moreover,

\[
(m+1)^k-m^k=km^{k-1}+O(m^{k-2}),\qquad
\sum_{s=1}^{m}s^r=\frac{m^{r+1}}{r+1}+O(m^r).
\]

Because \(r+k=n-1\), the correction contributes \(2k/(r+1)=2k/(n-k)\) to the leading coefficient. This gives the stated intrinsic volume.

For comparison, suppose the \(k\) missing edges form a matching. In a potential of range greater than \(m\), its maximum and minimum must be the two endpoints of one missing edge. After translating the minimum to zero, choose that edge in \(k\) ways, its direction in two ways, and the range \(m+h\), with \(1\le h\le m\). Every other coordinate is adjacent to both extrema and so lies in \(\{h,\ldots,m\}\). Consequently its full Ehrhart polynomial is independently counted as

\[
L_{\mathrm{match}}(m)=(m+1)^n-m^n+2k\sum_{s=1}^{m}s^{n-2}.
\]

For \(m\ge1\) and \(k\ge2\), the binomial theorem gives \((m+1)^k-m^k>km^{k-1}\). Also, since \(1\le s\le m\), one has \(s^r\ge s^{n-2}/m^{k-1}\). Multiplication and summation yield the strict Ehrhart inequality. Comparing the two leading coefficients and applying the same Gram factor gives the stated positive volume difference. This completes the proof.

## Verification

Run `python3 artifacts/verify.py`. The standalone program enumerates integer solutions to the original edge-difference inequalities independently of the closed formula, checks the Ehrhart numerator and leading coefficient algebraically for finite parameter profiles, verifies strict matching comparisons, and (when SciPy is installed) constructs the polar from its halfspaces and computes its coordinate volume using independent convex-hull routines. All integer checks use exact arithmetic.

The verification run completed with:

`DELETED_STAR_POLAR_EHRHART_CHECKS_PASSED independent_counts=32 numerator_and_lead=45 strict_matching_comparisons=175 independent_hulls=6`

Finite checks are not the proof of the infinite-parameter result; the proof above supplies the general bijection and exact inequalities.

## Relationship to prior work

Higashitani, Jochemko, and Michałek (2018) describe facets and Ehrhart theory for symmetric edge polytopes, including an evaluated formula for **primal** polytopes of complete bipartite graphs. D'Alì, Delucchi, and Michałek (2019) connect symmetric edge polytopes and Lipschitz polytopes and study general graph classes and polar enumerators. D'Alì, Juhnke-Kubitzke, and Koch (2023) identify general polar lattice points with bounded integer cuts. These results justify the objects and the integer-potential interpretation but do not themselves display the star-deleted complete-graph count, its evaluated Euclidean volume, or the strict same-budget comparison with a deleted matching.

The matching enumeration, which is also known separately, is re-derived in the proof rather than assumed. The claim here is specifically the evaluated formula for a **star of missing edges** and its strict all-dilation and volume comparison. A generic bounded-cut description is not equated with the evaluated formula.

## Limitations

The theorem is restricted to deleted stars and compares with matching deletions only where a matching of the same size fits. It does not claim an extremum among all edge-deletion patterns. The Ehrhart identity determines but does not explicitly factor the numerator of the Ehrhart series; no new real-rootedness or \(\gamma\)-positivity property is asserted. A logically equivalent earlier enumeration of integer graph height functions or clique-amalgamated metric polytopes may exist; the literature review does not establish universal historical priority. The finite verification profiles do not certify every parameter.

## References

- A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, first public version 2018-07-20, https://arxiv.org/abs/1807.07678.
- A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first public version 2019-10-11, https://arxiv.org/abs/1910.05193.
- A. D'Alì, M. Juhnke-Kubitzke, M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933, first public version 2023-07-10, https://arxiv.org/abs/2307.04933.
