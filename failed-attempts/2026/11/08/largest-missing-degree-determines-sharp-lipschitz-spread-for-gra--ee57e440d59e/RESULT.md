# Largest missing degree determines sharp Lipschitz spread for graphs with square-free complements

## Finding
Let \(G\) be a simple graph on \(n\ge5\) vertices with graph-metric diameter at most \(2\). Assume its complement \(H=\overline G\) has no (not necessarily induced) four-cycle, equivalently, no complete bipartite subgraph \(K_{2,2}\). Write \(\Delta=\max_{v\in V(H)}\deg_H(v)\), and set
\[
B_n=\left\lfloor\frac{n^2}{4}\right\rfloor,\qquad F_n(k)=n(k+1)-(k-1)^2.
\]
For the uniform probability measure on vertices and the unit-edge shortest-path metric, define the sharp Lipschitz variance (the squared norm of the centering embedding from real Lipschitz functions to mean-zero \(L^2\)) by
\[
\operatorname{spr}(G)=\sup_{|f(u)-f(v)|\le d_G(u,v)}\frac1n\sum_{v\in V(G)}\bigl(f(v)-\overline f\bigr)^2,\qquad \overline f=\frac1n\sum_v f(v).
\]
Then the norm depends **only on \(n\) and \(\Delta\)**, not on the isomorphism type or the number of missing edges:
\[
\boxed{\operatorname{spr}(G)=\frac1{n^2}\max\!\left\{B_n,\max_{1\le k\le\Delta}F_n(k)\right\}.}
\]
The inner maximum is understood as absent when \(\Delta=0\). For \(\Delta\ge1\), it equals \(F_n(q)\) with \(q=\min\{\Delta,\lfloor n/2\rfloor+1\}\). Every maximizer, modulo addition of a constant, is exactly one of the following forms (including ties):

1. A balanced two-valued function, equal to \(1\) on \(\lfloor n/2\rfloor\) or \(\lceil n/2\rceil\) vertices and to \(0\) on the others, if \(B_n\) attains the displayed maximum.
2. A three-valued missing-star function: for a vertex \(v\in V(H)\), select \(k\) of its \(H\)-neighbors, assign \(-1\) to \(v\), \(+1\) to the selected neighbors, and \(0\) elsewhere, or reverse all signs, if \(F_n(k)\) attains the displayed maximum.

The sharp graph-independent improvement over the complete-graph baseline is
\[
0\le\operatorname{spr}(G)-\frac{B_n}{n^2}\le\frac2n.
\]
Equality on the right is attained for every \(n\ge5\) by taking \(H\) to be a star on \(\lfloor n/2\rfloor+2\) vertices together with isolates. For the complementary-cycle family \(G=\overline {C_n}\), \(n\ge5\), this yields the exact phase transition
\[
\operatorname{spr}(\overline {C_n})=\frac1{n^2}\max\{B_n,3n-1\};
\]
three-valued missing-star optimizers strictly win for \(5\le n\le11\), and balanced binary optimizers strictly win for all \(n\ge12\).

## Assumptions and scope
The four-cycle exclusion concerns subgraphs of \(H\), not only induced four-cycles. In particular it prohibits two distinct vertices of \(H\) from having two common neighbors. The diameter assumption is **separate**: the condition on \(H\) alone does not guarantee diameter \(2\) for \(G\). A complete graph has diameter \(1\) and is included. The measure is uniform, functions are real-valued, and edge lengths are one. The stated variance is the sharp square of the operator norm from \(\operatorname{Lip}_0(G)\), with the Lipschitz seminorm, into centered \(L^2(G)\); choosing the anchored vertex does not affect the answer.

## Proof
**1. Integer maximizers.** Fix a root \(o\) and impose \(f(o)=0\). The Lipschitz feasible set is a bounded convex polytope determined by \(|f(u)-f(v)|\le1\) for graph edges. Its vertices have a connected spanning subgraph of **tight edges** satisfying \(|f(u)-f(v)|=1\): otherwise the connected component of the tight-edge graph not containing \(o\) can be raised and lowered by sufficiently small equal amounts without breaking any inequality, contradicting extremality. Along a tight spanning tree, all differences are \(\pm1\), hence every vertex potential is an integer. The variance functional is strictly convex on the anchored space, because the kernel of the centering map consists only of constants. Therefore no nonvertex of the polytope can attain its maximum (a nontrivial convex combination has strictly smaller variance than the corresponding endpoint average). Every maximizing function consequently has integer values.

**2. Classification by missing bicliques.** Because \(G\) has diameter at most \(2\), an integral Lipschitz potential takes either one, two, or three consecutive integer values. A nonconstant two-valued potential can be shifted to an indicator with \(k\) ones and \(n-k\) zeros; its variance is \(k(n-k)/n^2\), maximized precisely by the balanced binary choices with numerator \(B_n\). In the three-valued case shift to levels \(-1,0,+1\), and write \(A=\{f=-1\}\), \(B=\{f=+1\}\). Both extreme sets are nonempty, and no edge of \(G\) joins them (such an edge would carry a forbidden difference \(2\)). Thus \(H\) contains every edge between \(A\) and \(B\). If both sets had size at least two, these edges would contain a \(K_{2,2}\), contrary to the hypothesis. Therefore at least one extreme set is a singleton; multiplying by \(-1\) if needed, write \(A=\{v\}\), \(|B|=k\), where \(B\) is a subset of the \(H\)-neighbors of \(v\). The centered variance numerator is exactly
\[
n\sum_{x\in V(G)}f(x)^2-\left(\sum_x f(x)\right)^2=n(k+1)-(k-1)^2=F_n(k).
\]
Conversely every such potential is Lipschitz on \(G\): there are no graph edges joining its opposite extreme sets, while every other potential difference is at most one. The binary potentials are always Lipschitz. The full formula and equality classification follow; the constant potential cannot maximize because binary potentials have positive variance.

**3. Optimizing the single integer parameter.** Completing the square gives
\[
F_n(k)=\frac{n^2}{4}+2n-\left(k-\frac{n+2}{2}\right)^2.
\]
The sequence increases until the closest integer to \((n+2)/2\) and then decreases. Hence its maximum over \(1\le k\le\Delta\) is attained at \(q=\min\{\Delta,\lfloor n/2\rfloor+1\}\), with the additional tied integer \(q+1\) possible for odd \(n\) if the degree permits it. For even \(n\) the unrestricted maximum is \(n^2/4+2n\). For odd \(n\), the half-integer peak produces an integer unrestricted maximum of \(B_n+2n\). Therefore \(F_n(k)\le B_n+2n\), proving the sharp increase bound. A missing star with \(\lfloor n/2\rfloor+1\) leaves has no four-cycle; its complement has diameter two for \(n\ge5\) (the star's center has at least one neighbor in the complement, and any nonedge has a common neighbor). It realizes the bound with the prescribed three-valued potential.

**4. Exact cycle threshold.** For \(n\ge5\), the complement of an \(n\)-cycle has diameter two, since each pair adjacent in the cycle has a third vertex not adjacent in the cycle to either. Its missing-degree maximum is two, and \(F_n(2)=3n-1\), which exceeds \(F_n(1)=2n\). The identity \(3n-1>B_n\) holds for integers \(5\le n\le11\), and the reverse strict inequality holds for \(n\ge12\). Substituting into the norm formula proves the threshold and equality types.

## Verification
The accompanying standalone `verify.py` performs exact-integer enumeration of all anchored integral one-Lipschitz potentials on every qualifying labeled graph with four or five vertices. It also checks 900 reproducibly sampled qualifying six-vertex graphs and 70 qualifying seven-vertex graphs, confirming both the formula and the equality shapes. Further checks verify the cycle threshold for \(5\le n\le50\) and quadratic maximization identities for \(5\le n\le1000\). The final emitted marker is `ALL_C4_FREE_SPREAD_CHECKS_OK`. The finite checks are corroboration only; the preceding proof applies for all \(n\ge5\).

## Relationship to prior work
Graph spread was introduced as the maximum variance of a graph-Lipschitz function by Alon, Boppana and Spencer; Addario-Berry, Janson and McDiarmid study random-graph spread (their available abstract was inspected; full text remained inaccessible). Yancey develops geometric and structural properties of variance-optimal Lipschitz functions, including families far from the present complement condition. Lancien and Pernecká give the underlying framework of \(\operatorname{Lip}_0(M)\) and Lipschitz-free spaces but do not compute this embedding norm for missing-four-cycle graph metrics. The new statement concerns a **per-graph universality principle**: within the entire forbidden-subgraph class, only the order and largest missing degree matter, with complete equality classification. Bounds on maximum spread among graphs with a deletion budget do not automatically yield this per-graph identity or its full optimizer geometry. No assertion of originality is made for basic integrality or the established definition of graph spread.

## Limitations
The result does not apply when \(G\) has diameter greater than two, when the missing-edge graph contains a four-cycle, or with nonuniform measures, weighted distances, or higher centered moments. It does not characterize arbitrary graphs merely from their missing-degree maxima. Although targeted primary-literature and mathematical-database comparisons (with one relevant abstract-only source) did not find the exact forbidden-four-cycle universality statement, equivalent results under different terminology remain a possibility; independent literature verification is still warranted.

## References
1. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156v1 (first publicly posted 2009-02-06).
2. G. Lancien and E. Pernecká, *Approximation properties and Schauder decompositions in Lipschitz-free spaces*, arXiv:1207.1583v1 (first publicly posted 2012-07-06), primary MSC 46B20.
3. M. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, arXiv:1705.09725v1 (first publicly posted 2017-05-26).
