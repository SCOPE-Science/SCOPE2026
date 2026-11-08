# Parity and block-size thresholds for the Euclidean circumspheres of path block polytopes
## Finding
Fix integers \(m\ge2\) and \(a\ge1\). For \(x=(x_{ij})\in\mathbb R^{ma}\), with \(1\le i\le m\) and \(1\le j\le a\), put \(s_i=\sum_{j=1}^{a}x_{ij}\). Define the path block polytope
\[
P_{m,a}=\{x:x_{ij}\ge0,\ s_i+s_{i+1}\le1\ (1\le i<m)\}.
\]
The metric is the standard Euclidean metric in these coordinates. The **unique smallest enclosing Euclidean ball** of \(P_{m,a}\) has an explicit center and squared radius, and its complete contact set undergoes a sharp parity-and-block-size transition.

For even \(m=2k\), the center has **every coordinate equal to** \(1/(2a)\), and
\[
\boxed{R_{m,a}^{2}=\frac{m(2a-1)}{4a}.}
\]
If \(a=1\), every vertex contacts the sphere. If \(a\ge2\), exactly the vertices selecting one coordinate in each block of a maximum independent set of the length-\(m\) path contact it. There are
\[
\boxed{(k+1)a^k}
\]
such contacts when \(a\ge2\).

For odd \(m=2k+1\), put
\[
h=\min\left\{1,\frac{m+a-1}{2m}\right\},\qquad \ell=1-h.
\]
The center has coordinate \(h/a\) in each **odd-indexed** block and \(\ell/a\) in each **even-indexed** block. The squared radius is
\[
\boxed{R_{m,a}^{2}=\begin{cases}
\displaystyle\frac{m(2a-1)}{4a}+\frac{(a-1)^2}{4ma},&1\le a\le m+1,\\[3pt]
\displaystyle\frac{(m+1)(a-1)}{2a},&a\ge m+1.
\end{cases}}
\]
The formulas coincide at \(a=m+1\). If \(a=1\), every vertex contacts. If \(2\le a\le m+1\), the contacts are precisely the vertices occupying all odd-indexed blocks or all even-indexed blocks, choosing one coordinate in each occupied block; their number is
\[
\boxed{a^{k+1}+a^k.}
\]
If \(a>m+1\), precisely the vertices occupying every odd-indexed block contact; their number is
\[
\boxed{a^{k+1}.}
\]
In the exceptional case \(a=1\), the total number of contacts is \(F_{m+2}\), with \(F_0=0\), \(F_1=1\) the Fibonacci numbers. In every case **no nonvertex point is a contact**.

For instance, \(P_{5,3}\) has a center with entries \(7/30\) in the odd blocks and \(1/10\) in the even blocks, squared radius \(43/20\), and \(36\) contact vertices. At \(m=5,a=6\) there are \(252\) contacts, whereas \(m=5,a=7\) has \(343\) contacts, all from the odd-support family (the block-size change also changes the raw counts).

## Assumptions and scope
All statements quantify over integer \(m\ge2\), integer \(a\ge1\), and the **unweighted** Euclidean metric of \(\mathbb R^{ma}\). A contact is a point of the entire convex polytope lying on the unique minimum enclosing sphere. The polytope is bounded because \(s_i\le1\) for each block, and full-dimensional because small positive coordinates satisfy all inequalities strictly.

Its vertices are precisely the \(0/1\) vectors obtained by selecting at most one coordinate in each block and occupying a set of nonadjacent blocks. To justify this, the feasible aggregate vector \(s\) lies in the stable-set polytope of a path: \(s\ge0\) and \(s_i+s_{i+1}\le1\) form an integral polytope because the edge-node incidence matrix of a bipartite path is totally unimodular. Decompose \(s\) into binary independent-set indicators. For any block with \(s_i>0\), choose its coordinate independently using probabilities \(x_{ij}/s_i\), conditional on occupancy; this expresses \(x\) as a convex combination of the asserted \(0/1\) vectors. All asserted \(0/1\) vectors are extreme because they are vertices of the ambient unit cube.

## Proof
Write \(I\subseteq\{1,\ldots,m\}\) for an independent block support, and let \(v\) select one standard basis coordinate in each occupied block. If a prospective center has each coordinate of block \(i\) equal to \(p_i/a\), its exact squared distance to \(v\) is
\[
\|v-c\|_2^2=B+\sum_{i\in I}w_i,\qquad
B=\frac1a\sum_{i=1}^mp_i^2,\quad w_i=1-\frac{2p_i}{a}.
\tag{1}
\]
The identity follows by expanding \(\|v\|^2-2\langle c,v\rangle+\|c\|^2\). Thus classification of vertex contacts amounts to a maximum-weight independent-set problem on a path.

**Even case.** Choose \(p_i=1/2\) in all blocks. If \(a>1\), every weight in (1) is \(1-1/a>0\). The largest independent-set cardinality of a path of \(m=2k\) vertices is \(k\), so (1) has maximum
\[
\frac{m}{4a}+k\left(1-\frac1a\right)
=\frac{m(2a-1)}{4a},
\]
and equality means that the support has size \(k\). Exactly \(k+1\) maximum independent supports exist: the compression \(i_1<\cdots<i_k\mapsto(i_1,i_2-1,\ldots,i_k-k+1)\) bijects them with the \(k\)-subsets of \(\{1,\ldots,k+1\}\). There are \(a^k\) coordinate choices for each support. When \(a=1\), all weights vanish, so all binary independent-set vertices are contacts, of which there are \(F_{m+2}\).

**Odd case: the two-family regime.** Let \(m=2k+1\) and \(1<a\le m+1\), and put
\[
h=\frac{m+a-1}{2m},\quad \ell=1-h,\quad p_{2j-1}=h,\quad p_{2j}=\ell.
\tag{2}
\]
The odd-block and even-block weights \(w_o=1-2h/a\), \(w_e=1-2\ell/a\) are positive and satisfy
\[
(k+1)w_o=k w_e.
\]
Set \(\theta=w_o/k=w_e/(k+1)>0\), and assign to the path edge indexed \(2j-1\) the positive weight \((k-j+1)\theta\) and to edge \(2j\) the positive weight \(j\theta\), for \(1\le j\le k\). The sum of the two incident edge weights at each odd path vertex is \(w_o\); at each even vertex it is \(w_e\). Therefore, for any independent set \(I\),
\[
\sum_{i\in I}w_i
=\sum_{e=\{i,i+1\}}\lambda_e(\mathbf1_I(i)+\mathbf1_I(i+1))
\le\sum_e\lambda_e.
\tag{3}
\]
All edge weights are strictly positive, so equality in (3) forces every edge to have exactly one occupied endpoint. There are **exactly two** such independent sets: all odd indices and all even indices. The two families therefore give all contact vertices, including at \(a=m+1\). Counting colors gives \(a^{k+1}+a^k\).

**Odd case: the one-family regime.** When \(a>m+1\), choose \(p_i=1\) on odd indices and \(p_i=0\) on even indices. Now \(w_o=1-2/a>k/(k+1)\) and \(w_e=1\). Put \(\theta=w_o/k\) and use the same positive edge coefficients as above. The incident-edge sum is exactly \(w_o\) at each odd vertex and is \((k+1)w_o/k>1=w_e\) at each even vertex. Hence the weighted independence objective is strictly below \(\sum_e\lambda_e=(k+1)w_o\) for any independent set using an even index; equality elsewhere forces every edge tight and therefore **only the odd support**. Equation (1) now gives
\[
R^2=\frac{k+1}{a}+(k+1)\left(1-\frac2a\right)
=(k+1)\left(1-\frac1a\right).
\tag{4}
\]
There are \(a^{k+1}\) contacts.

**Odd case at \(a=1\).** Set \(p_i=1/2\) for all blocks. Again every \(w_i=0\), so all vertices are equidistant, with squared radius \(m/4\). This equals the first branch of the stated formula.

**Closed radius formula in the two-family regime.** In (2), the center is the barycenter of the following contact distribution: choose the all-odd block support with probability \(h\), or the all-even support with probability \(\ell\), then choose one of the \(a\) block coordinates uniformly and independently wherever occupied. The block occupancy probability is \(p_i\). The expected squared norm of a contact is \((k+1)h+k\ell\), and the squared norm of the barycenter is \(((k+1)h^2+k\ell^2)/a\). Since the two support classes tie in distance, their common squared distance equals their expected squared distance from the barycenter:
\[
R^2=(k+1)h+k\ell-\frac{(k+1)h^2+k\ell^2}{a}
=\frac{m(2a-1)}{4a}+\frac{(a-1)^2}{4ma}.
\tag{5}
\]
This also works at \(a=1\) and \(a=m+1\), by the same barycentric identity.

**Global minimality and uniqueness.** For even \(m\), take the equal-probability mixture of the two alternating supports (odd and even), with uniform coordinate selection in each occupied block. Its barycenter is the candidate center \(c\), and both alternating support families are contacts. For odd \(a>m+1\), take the uniform-color all-odd support distribution; its barycenter is again the proposed center. Otherwise use the \(h,\ell\) mixture just described. Every mixture component of positive probability is a sphere contact. For any other proposed center \(z\), the variance identity gives
\[
\mathbb E\|V-z\|^2=R^2+\|z-c\|^2.
\]
Consequently any ball enclosing all vertices has squared radius at least \(R^2+\|z-c\|^2\); it cannot improve on \(R^2\), and equality forces \(z=c\). This certifies the unique global minimum without assuming block symmetry. Finally, strict convexity of squared Euclidean norm shows that a nontrivial convex combination of distinct vertices cannot contact a ball on which all vertices lie, completing the contact classification.

## Verification
The included standalone `verify.py` independently enumerates all binary independent block supports and evaluates their squared distances using **exact rational arithmetic**. It checks enclosure, equality classes, the complete contact counts, the explicit contact barycenter, and the equality of the barycentric variance and the claimed radius. The exhaustive bounded parameter sweep covers \(274\) pairs \((m,a)\), including all \(2\le m\le18\) with a range of block sizes on both sides of the odd transition, and \(351{,}604\) independent-support distance comparisons, yielding \(707{,}576\) exact assertions. A separately formulated numerical quadratic projection problem agrees with the proposed center in another \(70\) small parameter instances. These finite computations are **not** used as an infinite proof; the preceding argument is valid for all allowed integer parameters.

To reproduce: save `verify.py` next to this document and run `python verify.py` using Python 3; SciPy and NumPy are optional and are needed only for the supplementary numerical quadratic program.

## Relationship to prior work
Jiang, Yang, and Zhong introduced path and cyclic block polytopes and developed transfer-matrix and Ehrhart results, including the stable-set interpretation of the path family. The present claim concerns the **unique Euclidean minimum enclosing ball**, its **exact coordinates**, and its **complete contact-vertex transitions**, not the lattice-point generating function. Their 2026 manuscript was available in abstract but its full text could not be retrieved for a direct statement-level audit; priority with respect to that manuscript is therefore provisional.

The earlier sharp Euclidean-diameter theorem for **cyclic** block polytopes treats a different metric invariant on cycle constraints, where odd cycles can have half-integral vertices. Neither its diameter statement nor its vertex-count formulas imply the path-family circumsphere and contact thresholds here. The published complete-multipartite stable-set sphere theorem concerns graphs whose independent sets lie in one independent vertex class; in our clique-expanded path, a stable set can occupy multiple nonadjacent clique blocks. No graph or parameter specialization of that theorem covers this case. The published cycle fractional-stable-set sphere theorem treats a single coordinate per cycle vertex and a cyclic closure rather than the colored path family; it does not imply the present block-size transition.

Elzinga and Hearn give a general algorithm for covering a convex polyhedron by a minimum sphere, but no closed parity/parameter/contact classification for this family. Published literature searches under the synonymous terms *Euclidean circumradius*, *Chebyshev center*, *smallest enclosing sphere*, *stable-set polytope*, and *clique-blown path* did not identify a covering theorem. A missing full primary manuscript and possible differently named metric results remain priority risks.

## Limitations
The construction requires equal block sizes, path (not cycle or arbitrary graph) adjacency, nonnegative coordinates, and the specified standard Euclidean metric. No John ellipsoid, affine-invariant radius, or cyclic-family analogue is asserted. The result concerns a family already known to be a stable-set polytope; the new content is its explicit Euclidean sphere and support geometry. Search failures do not prove historical novelty, and the original full 2026 preprint was not accessible for complete comparison.

## References
1. Xinru Jiang, Shuai Yang, Yueming Zhong, *Transfer Matrices and Ehrhart Theory for Path and Cyclic Block Polytopes*, arXiv:2607.22008, first posted 2026-07-24, DOI 10.48550/arXiv.2607.22008.
2. Jack Elzinga and Donald Hearn, *The minimum sphere covering a convex polyhedron*, *Naval Research Logistics Quarterly* 21 (1974), 715–718, DOI 10.1002/nav.3800210414.
3. *Large-part screening in minimum spheres of complete multipartite stable-set polytopes*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-large-part-screening-in-minimum-spheres-of-complete-multipartite--2a7050b5d350.
4. *Cycle fractional stable-set polytopes have a parity-split minimum sphere*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cycle-fractional-stable-set-polytopes-have-a-parity-split-minimu--0b914e4f06d2.
