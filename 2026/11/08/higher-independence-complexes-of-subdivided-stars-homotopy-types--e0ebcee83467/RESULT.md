# Higher independence complexes of subdivided stars: homotopy types and integral symmetry

## Finding

Let \(k\ge 3\). Form the once-subdivided \(k\)-star \(T_k\) with center \(c\), inner vertices \(a_1,\ldots,a_k\), outer leaves \(b_1,\ldots,b_k\), and edges \(ca_i,a_ib_i\) for \(1\le i\le k\). For an integer \(r\ge1\), let \(X_{k,r}=\operatorname{Ind}_r(T_k)\) consist of vertex subsets whose induced connected components contain at most \(r\) vertices.

For all the indicated integer parameters, there is an **ordinary (not asserted equivariant) homotopy equivalence**

\[
|X_{k,r}|\simeq
\begin{cases}
S^{k-1},&r=1,\\
\mathrm{point},&2\le r\le k,\\
\displaystyle\bigvee^{\binom{k-1}{r-k-1}} S^{r-1},&k+1\le r\le 2k,\\
\mathrm{point},&r\ge 2k+1.
\end{cases}
\]

In particular, the reduced integral homology is free abelian and is concentrated in the dimension of the displayed spheres. This exhibits a **contractibility window** followed by a binomial sequence of nonzero homology ranks.

There is also an **integral equivariant refinement**. Let \(S_k\) permute arms simultaneously, let \(\varepsilon:\mathbb Z^k\to\mathbb Z\) sum coordinates, let \(U_k=\ker\varepsilon\) be the integral augmentation lattice with this action, and let \(\mathrm{sgn}\) be the one-dimensional integral sign representation. Then

\[
\widetilde H_{k-1}(X_{k,1};\mathbb Z)\cong_{\mathbb Z[S_k]}\mathrm{sgn},
\]
\[
\widetilde H_{r-1}(X_{k,r};\mathbb Z)
\cong_{\mathbb Z[S_k]}
\mathrm{sgn}\otimes_{\mathbb Z}\bigwedge^{r-k-1}U_k
\quad (k+1\le r\le2k).
\]

All remaining reduced integral homology representations vanish. The endpoints are informative: at \(r=k+1\) the rank-one class transforms by sign; at \(r=2k\) the rank-one class is invariant, since \(\bigwedge^{k-1}U_k\cong\mathrm{sgn}\).

## Assumptions and scope

The simplicial complex is based on **induced** connected components, not a matching complex, path complex, or a complex of edge subsets. All vertices are distinct, the tree is unweighted and undirected, and the dimension convention is \(\dim \sigma=|\sigma|-1\). The \(S_k\)-action permutes both \(a_i\) and \(b_i\) with the same index permutation, fixing \(c\). Empty reduced homology means the zero group, not absence of a nonempty space.

## Proof

**1. Deletion of the center.** For \(r\ge2\), removing \(c\) leaves \(k\) disjoint graph edges, so every vertex subset in the deletion satisfies the size bound. Thus the simplicial deletion of \(c\) is a full simplex \(D\). Write \(L=\operatorname{lk}_{X_{k,r}}(c)\). The standard decomposition \(X_{k,r}=D\cup(c*L)\), with intersection \(L\), identifies \(|X_{k,r}|\) with the homotopy cofiber of \(|L|\hookrightarrow |D|\). Since \(D\) is contractible, \(|X_{k,r}|\simeq\Sigma |L|\). The connecting homomorphism in its long exact sequence is naturally \(S_k\)-equivariant:
\[
\widetilde H_j(X_{k,r};\mathbb Z)\cong\widetilde H_{j-1}(L;\mathbb Z).
\]

**2. Exact link condition.** A face of \(L\) is uniquely specified by \(I,J\subseteq[k]\), where \(a_i\) is selected precisely for \(i\in I\) and \(b_i\) for \(i\in J\). The component containing \(c\) in the enlarged face has exactly \(1+|I|+|I\cap J|\) vertices; all the remaining selected leaves are isolated. Therefore
\[
L=\{(I,J):1+|I|+|I\cap J|\le r\}.
\]
This identity supplies the entire face poset, including all boundary cases.

**3. Acyclic matching and homotopy.** Project the face poset of \(L\) monotonically to the Boolean poset of subsets \(I\). In each fiber with \(I\ne[k]\), choose its least missing index \(i\); toggle \(b_i\), which never changes the defining inequality. This gives a perfect elementary matching in that fiber. In the fiber \(I=[k]\), put \(h=r-k-1\). This fiber is empty for \(h<0\), and otherwise consists of \(J\) with \(|J|\le h\). Toggle \(b_1\) whenever both faces lie in the fiber. If \(0\le h\le k-1\), precisely the faces with \(1\notin J\) and \(|J|=h\) remain unpaired. There are \(\binom{k-1}{h}\) of them, all of dimension \(k+h-1=r-2\). If \(h\ge k\), every face is paired. The patchwork lemma for acyclic matchings on fibers of an order-preserving map proves acyclicity of their union. The empty face is paired in a nonempty lower fiber; the corresponding ordinary Morse CW complex has an additional base vertex. Hence \(L\) is contractible for \(h<0\) or \(h\ge k\), and is homotopy equivalent to \(\binom{k-1}{h}\) spheres of dimension \(r-2\) for \(0\le h\le k-1\). Suspending gives the claimed formula for \(r\ge2\). (At \(r\ge2k+1\), one can also see directly that \(X_{k,r}\) is a full simplex.)

**4. Integral symmetry, independently of the non-equivariant matching.** Let \(A\subseteq L\) be the subcomplex of faces with \(I\ne[k]\). The perfect matching from Step 3, applied to \(A\) alone, shows that \(A\) is contractible; importantly, \(A\) itself is \(S_k\)-invariant even though the chosen matching need not be. For \(0\le h\le k-1\), the relative chain group \(C_{k+j-1}(L,A;\mathbb Z)\), for \(0\le j\le h\), is freely generated by the oriented simplices containing all \(a_i\) and exactly \(j\) of the \(b_i\). Put every \(a\)-vertex first in the orientation. There is a natural \(\mathbb Z[S_k]\)-isomorphism
\[
C_{k+j-1}(L,A;\mathbb Z)\cong\mathrm{sgn}\otimes\bigwedge^{j}\mathbb Z^k.
\]
The relative boundary, up to the uniform sign \((-1)^k\), is contraction with the coordinate-sum functional \(\varepsilon\). The finite complex for \(j=0,\ldots,h\) is the truncated augmented chain complex of a simplex. Its only homology is the kernel of the top contraction, namely \(\bigwedge^{h}U_k\), with the convention \(\bigwedge^0U_k=\mathbb Z\). Indeed \(\mathbb Z^k=U_k\oplus\mathbb Z e_1\), and contraction maps \(e_1\wedge\bigwedge^{j-1}U_k\) isomorphically onto \(\bigwedge^{j-1}U_k\), annihilating \(\bigwedge^jU_k\). As \(A\) is contractible, reduced homology of \(L\) equals relative homology of \((L,A)\), equivariantly. The connecting isomorphism from Step 1 finishes the integral representation claim and proves torsion-freeness.

**5. The classical parameter \(r=1\).** Now the deletion of \(c\) is \(\operatorname{Ind}_1(kK_2)=(S^0)^{*k}\cong S^{k-1}\). The link of \(c\) is the full simplex on \(b_1,\ldots,b_k\), so coning it off does not change this homotopy type. Interchanging two arms exchanges two \(S^0\) join factors and acts by \(-1\) on their top orientation; the resulting integral homology action is \(\mathrm{sgn}\).

## Verification

Run `python3 verify.py` with Python 3 and no external packages. It independently enumerates all induced-component-bounded faces for every \(2\le k\le5\), \(1\le r\le2k+1\), computes reduced homology over \(\mathbb F_2\) by full boundary-matrix rank, and verifies the predicted Betti tables. It also checks the acyclic link matching by constructing and topologically sorting its directed Hasse graph, and checks signed simplicial Lefschetz traces of every arm permutation against the proposed integral characters. The recorded executable result is in `verify_output.txt`. These finite tests are corroboration, not a substitute for Steps 1–5.

## Relationship to prior work

Sawant (arXiv:2605.25150, first public 2026-05-24) proves vertex decomposability for higher independence complexes of **all** trees, hence a general qualitative sphere-wedge property; it does not identify sphere counts, their dimensions for this family, or integral arm-permutation modules. Deshpande and Singh (arXiv:2001.05448, first public 2020-01-15) give exact formulas for fully whiskered graphs, graphs with a leaf at **every** non-leaf vertex, and perfect regular-branching trees. In \(T_k\) the center \(c\) is a non-leaf without a leaf neighbor, so the relevant whiskering hypotheses fail, and regular perfect-branching at depth two also fails. Ghosh and Selvaraja (arXiv:2505.06614, first public 2025-05-10) give shellability criteria for trees and whiskering operations, not this integral equivariant calculation. This result uses related elementary-matching methods but supplies the distinct explicit partially whiskered classification. The two-arm path is excluded from the parameter range because its higher independence homotopy type is already a special case of the known path formulas.

## Limitations

The theorem does not classify arbitrary spiders with unequal arm lengths, higher independence complexes of all trees, geometric fixed-point spaces, or equivariant homotopy equivalences. The displayed sphere splittings are ordinary homotopy equivalences; only the homology-module statements are equivariant. The cited comparisons cannot rule out an equivalent unindexed or unpublished result.

## References

1. Rutuja Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150 (first submitted 2026-05-24), https://arxiv.org/abs/2605.25150.
2. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first submitted 2020-01-15), https://arxiv.org/abs/2001.05448, published 2021.
3. Arka Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614 (first submitted 2025-05-10), https://arxiv.org/abs/2505.06614.
4. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145; the acyclic matching/patchwork lemma is also described in Deshpande–Singh, Section 2.
