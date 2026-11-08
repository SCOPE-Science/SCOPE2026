# Two-degree sphere-wedge classification for higher independence complexes of once-subdivided double stars

## Finding
For integers \(a,b\geq1\), let \(T_{a,b}\) be the tree with a three-vertex central path \(u-w-v\), with \(a\) pendant leaves incident to \(u\) and \(b\) pendant leaves incident to \(v\), and no other edges. Put \(t=a+b\). Let \(\operatorname{Ind}_r(T)\) comprise the vertex subsets for which every connected component of the induced subgraph has at most \(r\) vertices. For binomial coefficients, use \(\binom{n}{k}=0\) if \(k<0\) or \(k>n\) (with \(n\geq0\)); an empty wedge denotes a contractible point.

**Theorem.** For every \(r\geq1\), the exact integral homotopy type is
\[
\operatorname{Ind}_r(T_{a,b})\simeq
\begin{cases}
S^1,&r=1,\\[2pt]
\displaystyle\left(\bigvee^{\binom{t-1}{r-3}} S^{r-1}\right)
\vee\left(\bigvee^{\binom{a-1}{r-1}\binom{b-1}{r-1}} S^{2r-1}\right),
&2\leq r\leq t+2,\\[5pt]
\{\mathrm{point}\},&r\geq t+3.
\end{cases}
\]
In particular, the complete reduced integral homology is torsion-free. For \(3\leq r\leq\min(a,b)\), both sphere families occur in distinct degrees \(r-1\) and \(2r-1\). For example, \(\operatorname{Ind}_3(T_{3,3})\simeq S^2\vee S^5\), and \(\operatorname{Ind}_3(T_{4,4})\simeq S^2\vee\bigvee^{9} S^5\).

## Assumptions and scope
Every graph is finite, simple, and undirected. The leaves on the two hubs are distinct, with at least one on each. A higher independent face may have several induced components, each separately bounded in order. All homotopy equivalences concern the geometric realizations of simplicial complexes, and the wedge is an ordinary, generally non-equivariant wedge. The theorem includes all boundary cases, including \(r=1\), values for which one multiplicity vanishes, and the full-simplex range \(r\geq t+3\).

## Proof
**1. The single-star calculation.** Write \(H_a=K_{1,a}\) with leaf set \(U\), and let \(K_a(r)=\operatorname{Ind}_r(H_a)\). For \(1\leq r\leq a\), every face either omits the hub or contains it with at most \(r-1\) leaves. Consequently
\[
K_a(r)=\Delta_U\cup\bigl(u*\operatorname{skel}_{r-2}\Delta_U\bigr),
\qquad \Delta_U\cap(u*\operatorname{skel}_{r-2}\Delta_U)=\operatorname{skel}_{r-2}\Delta_U.
\]
Here \(\operatorname{skel}_{-1}\Delta_U=\{\varnothing\}\) and its realization is interpreted as the formal \((-1)\)-sphere for augmented join/suspension calculations. Coning off this skeleton inside the contractible full leaf simplex gives the suspension of that skeleton. The \((r-2)\)-skeleton of an \((a-1)\)-simplex is a wedge of \(\binom{a-1}{r-1}\) spheres of dimension \(r-2\), with the standard \((-1)\)-sphere convention at \(r=1\). It follows that
\[
K_a(r)\simeq\bigvee^{\binom{a-1}{r-1}} S^{r-1}\quad(1\leq r\leq a),
\]
while \(K_a(r)\) is a full simplex for \(r\geq a+1\). The skeleton statement follows, for instance, by the usual simplex-face matching or by induction on vertices using deletion and link; it is a homotopy statement, not merely a homology computation.

**2. The ordinary double-star calculation.** Let \(D_{a,b}\) have adjacent hubs \(u,v\) and respective disjoint leaf sets \(U,V\), with \(|U|=a\), \(|V|=b\). Put \(t=a+b\). For \(s\geq2\) define \(C=\Delta_{U\sqcup V}\), \(A_u=\operatorname{skel}_{s-2}\Delta_U*\Delta_V\), \(A_v=\Delta_U*\operatorname{skel}_{s-2}\Delta_V\), and \(B=\operatorname{skel}_{s-3}\Delta_{U\sqcup V}\). Consider
\[
E=C\cup(u*A_u)\cup(v*A_v).
\]
Both \(A_u\) and \(A_v\) are nonempty contractible because their opposite leaf-simplex factors are nonempty. The intersections used in consecutively adjoining these two cones to \(C\) are exactly \(A_u\) and \(A_v\), respectively. Thus \(E\) is contractible and connected. The full complex has the exact decomposition
\[
\operatorname{Ind}_s(D_{a,b})=E\cup\bigl((uv)*B\bigr),\qquad
E\cap((uv)*B)=\partial(uv)*B.
\]
Indeed, a face containing both hubs uses at most \(s-2\) leaves; those containing at most one hub are already in \(E\). The second term is a cone and its attaching complex is the suspension of \(B\); attaching this cone to contractible \(E\) yields \(\Sigma^2 B\). If \(2\leq s\leq t+1\), the leaf skeleton \(B\) is a wedge of \(\binom{t-1}{s-2}\) spheres in dimension \(s-3\). This includes \(s=2\), for which \(B=\{\varnothing\}\), the attaching intersection is two points, and the result is a circle. Hence
\[
\operatorname{Ind}_s(D_{a,b})\simeq
\bigvee^{\binom{t-1}{s-2}}S^{s-1}\quad(2\leq s\leq t+1).
\]
For \(s\geq t+2\) the complex is the full simplex. For \(s=1\), the analogous decomposition omitting the edge \(uv\) shows it is contractible: the all-leaves simplex is successively enlarged by cones on the nonempty contractible opposite leaf simplices.

**3. Delete the middle vertex.** For \(X_r=\operatorname{Ind}_r(T_{a,b})\), deleting the middle vertex \(w\) yields a disjoint union of two stars. By the disjoint-union join law,
\[
D_r:=\operatorname{del}_{X_r}(w)=K_a(r)*K_b(r).
\]
For \(r\geq2\), the link is exactly
\[
L_r:=\operatorname{lk}_{X_r}(w)=\operatorname{Ind}_{r-1}(D_{a,b}).
\]
To see this face-by-face, adding \(w\) to any subset of \(V(T_{a,b})\setminus\{w\}\) joins the two hub components if both hubs are selected, or enlarges the unique selected hub component if only one is selected; both requirements amount to the corresponding component having at most \(r-1\) vertices in \(D_{a,b}\). If neither hub is selected, all leaves are isolated and the same formula holds. No other connected components can violate the bound. Therefore
\[
X_r=D_r\cup_{L_r}(w*L_r),
\]
i.e. \(X_r\) is a homotopy cofiber of the link inclusion \(L_r\longrightarrow D_r\).

**4. The attaching map vanishes.** By Step 1, for \(r\geq2\), the deletion \(D_r\) is either contractible or homotopy equivalent to a wedge of
\(\binom{a-1}{r-1}\binom{b-1}{r-1}\) spheres in dimension \(2r-1\); in particular it is \((2r-2)\)-connected. By Step 2, \(L_2\) is contractible, while for \(3\leq r\leq t+2\), \(L_r\) is a wedge of \(\binom{t-1}{r-3}\) spheres in dimension \(r-2\). Its dimension is strictly below the connectivity range of \(D_r\), so every map \(L_r\to D_r\) is nullhomotopic. For the zero-multiplicity boundary cases, the same conclusion holds because either the source or target is contractible. The cofiber of a null map therefore splits:
\[
X_r\simeq D_r\vee\Sigma L_r,
\]
which gives the claimed two multiplicities and dimensions. Finally, \(X_1\) has a contractible link at \(w\) (the simplex on all leaves), and its deletion is the join of two disjoint zero-spheres, hence \(X_1\simeq S^1\). If \(r\geq t+3\), every vertex subset of the tree is permitted and \(X_r\) is a simplex. This proves all cases. \(\square\)

## Verification
The accompanying standalone `verify_subdivided_stars.py` constructs each labeled tree directly. Independently of the homotopy decomposition, it enumerates all vertex subsets, tests the sizes of every connected component of each induced graph, builds complete augmented simplicial boundary matrices over \(\mathbb F_2\), and computes reduced Betti numbers by exact bitset Gaussian elimination. In its supplied bounded parameter test, \(1\leq a,b\leq4\), \(a+b\leq7\), and every \(1\leq r\leq a+b+3\), it checked 117 parameter triples and 36,352 nonempty faces counted across instances. The recorded execution returned `ALL_VERIFY_OK cases=117 total_face_instances=36352`. The unrestricted integral homotopy and torsion-freeness statements follow from the preceding construction, not from finite-field computations; no assertion about integral symmetry actions is made.

## Relationship to prior work
R. Sawant (arXiv:2605.25150v1, public 2026-05-24) proved vertex decomposability of \(\operatorname{Ind}_r(T)\) for every finite tree. F. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh (arXiv:2106.10863) had established vertex decomposability for all caterpillar graphs, including this tree, but without a two-dimensional family-specific sphere count. P. Deshpande and A. Singh (arXiv:2001.05448) determined exact homotopy types of complete multipartite graphs, fully whiskered graphs, cycles, paths, and perfect \(m\)-ary trees, but not this once-subdivided double-star family: its middle non-leaf vertex has no pendant neighbor, so it is not fully whiskered. Thus the known general shellability/vertex-decomposability statements already imply existence of a wedge decomposition, but not this explicit mixed-dimensional formula. A published result on bidirected double-star *multipath* complexes concerns different simplicial vertices (arcs rather than graph vertices) and a different compatibility condition. No claim is made that the standard star skeleton or the auxiliary adjacent-double-star lemma alone is novel.

## Limitations
The theorem treats a three-vertex core path with leaves only at its ends; it does not classify arbitrary caterpillars or their automorphism representations. Its homotopy equivalence is not asserted to be equivariant. The literature comparison cannot rule out an unindexed equivalent closed formula; independent review is not performed. The computations confirm only the stated finite parameter region and mod-two homology, while the proof handles all integer parameters and integral homotopy.

## References
1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1, first public 2026-05-24; Theorem 3.6.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v3; Theorem 3.12 (original preprint 2021-06-21).
3. P. Deshpande, A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v2; Theorems 3.8 and 3.10 (original preprint 2020-01-15).
