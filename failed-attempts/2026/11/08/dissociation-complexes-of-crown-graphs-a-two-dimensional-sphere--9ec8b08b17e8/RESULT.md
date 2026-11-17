# Dissociation complexes of crown graphs: a two-dimensional sphere wedge

## Finding

Let \(n\ge3\) be an integer. Let \(C_n=K_{n,n}-M_n\) be the crown graph with parts \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), in which \(a_i b_j\) is an edge exactly when \(i\ne j\). A **dissociation set** is a set \(S\) inducing maximum degree at most one. Let \(\mathcal D_n\) denote the simplicial complex of dissociation sets, equivalently the \(2\)-independence complex \(\operatorname{Ind}_2(C_n)\) in the convention that every induced connected component has at most two vertices.

**Theorem.** The complete face polynomial and inclusion-maximal face polynomial are, respectively,
\[
D_n(z)=2(1+z)^n-1+n^2z^2+2n(n-1)z^3+\binom n2z^4,
\]
\[
M_n(z)=2z^n+\binom n2z^4.
\]
Here the empty face contributes \(1\) to \(D_n\), and equal exponents in \(M_n\) are combined. More strongly, the **integral homotopy type** is
\[
\boxed{\mathcal D_n\simeq\bigvee^{\binom{n-1}{2}}S^2.}
\]
Thus all reduced integral homology vanishes except for \(\widetilde H_2(\mathcal D_n;\mathbb Z)\cong\mathbb Z^{\binom{n-1}{2}}\). The inclusion-maximal dissociation sets are precisely the two complete shores \(A,B\) and the \(\binom n2\) four-vertex sets \(\{a_i,b_i,a_j,b_j\}\), for \(i<j\). Their sizes are \(\{n,4\}\), so the complex is pure exactly when \(n=4\) within the stated domain.

The topology exhibits a sharp contrast with complete bipartite graphs: the published complete-multipartite theorem gives \(\operatorname{Ind}_2(K_{n,n})\simeq\bigvee^{n^2-1}S^1\), whereas deleting the perfect matching yields the two-dimensional wedge above.

## Assumptions and scope

All graphs are finite, labeled, undirected and simple. The parameter \(n\) is any integer at least three. A maximal dissociation set is inclusion-maximal, not merely of largest cardinality. The wedge symbol denotes the topological wedge (one-point union) and the homotopy equivalence is for geometric realizations of simplicial complexes, with **integral** consequences. For \(n=2\), the graph is two disjoint edges and its dissociation complex is a simplex; this excluded boundary has a different facet census.

## Proof

**Step 1: classify every face.** Put \(I=\{i:a_i\in S\}\) and \(J=\{j:b_j\in S\}\). For a selected \(a_i\), its degree in the induced subgraph is \(|J|-\mathbf 1_{i\in J}\), and for a selected \(b_j\) it is \(|I|-\mathbf 1_{j\in I}\). If \(J\ne\varnothing\), a selected \(b_j\) forces \(|I|\le2\), and symmetrically \(I\ne\varnothing\) forces \(|J|\le2\). If \(|I|=2\) and \(|J|=1\), the unique element of \(J\) must lie in \(I\); analogously for the transposed case. If \(|I|=|J|=2\), each side's degree inequalities force \(I=J\). Consequently, a mixed dissociation set is **exactly** a subset of \(\{a_i,b_i,a_j,b_j\}\) for some distinct indices \(i,j\); conversely any such subset induces at most two independent edges and is dissociating. All subsets contained entirely in one shore are also dissociating. This proves the face classification without any computational assumption.

**Step 2: face and maximal-face counts.** The subsets lying entirely in the two shores contribute \(2(1+z)^n-1\). The mixed faces have shore counts \((|I|,|J|)=(1,1),(2,1),(1,2),(2,2)\), with respective totals \(n^2,\ n(n-1),\ n(n-1),\ \binom n2\). Thus the claimed \(D_n\) follows. Every mixed face extends to the full four-vertex face on two indices; all such four-vertex faces are maximal, because a vertex at a third index would give some selected vertex induced degree at least two. Both entire shores are maximal since adding any opposite-shore vertex yields degree \(n-1\ge2\) at that new vertex. Any proper single-shore subset extends within its shore. These are all facets and give \(M_n\). The only possible facet sizes are \(n\) and \(4\), establishing purity exactly at \(n=4\).

**Step 3: a contractible intermediate complex.** Let \(T\) be the subcomplex consisting of all faces supported on at most two matched index pairs \(\{a_i,b_i\}\). Equivalently,
\[
T=\bigcup_{1\le i<j\le n}\operatorname{Simplex}\bigl(\{a_i,b_i,a_j,b_j\}\bigr).
\]
Let \(L_A\) be the one-skeleton of the full simplex on \(A\). Define a simplicial map \(p:T\to L_A\) by \(p(a_i)=a_i\) and \(p(b_i)=a_i\). Because each simplex of \(T\) uses at most two indices, its union with its image under \(p\) lies inside a single displayed four-vertex simplex. Hence the identity on \(T\) and \(p\) are contiguous simplicial maps, and the straight-line simplicial homotopy fixes \(L_A\) pointwise. It follows that \(|T|\) strongly deformation retracts onto \(|L_A|\).

Let \(\Sigma_A\) and \(\Sigma_B\) be the full simplices on \(A\) and \(B\), respectively. The face classification says \(\mathcal D_n=T\cup\Sigma_A\cup\Sigma_B\), and \(T\cap\Sigma_A=L_A\), \(T\cap\Sigma_B=L_B\), where \(L_B\) is the one-skeleton of \(\Sigma_B\). The deformation retract of \(T\) onto \(L_A\) extends by the identity over \(\Sigma_A\) (the homotopy fixes the intersection), so \(X=T\cup\Sigma_A\) deformation retracts onto the simplex \(\Sigma_A\). Thus \(X\) is contractible.

**Step 4: the integral homotopy type.** Now \(\mathcal D_n=X\cup\Sigma_B\), both pieces are contractible, and their intersection is exactly \(L_B\). These are simplicial subcomplexes, so their union is an ordinary homotopy pushout. The suspension lemma for a union of two contractible subcomplexes gives \(\mathcal D_n\simeq\Sigma |L_B|\). Since \(L_B\) is the complete graph on \(n\) vertices, it is a connected graph with cycle rank \(\binom n2-n+1=\binom{n-1}{2}\) and therefore \(|L_B|\simeq\bigvee^{\binom{n-1}{2}}S^1\). Suspending gives \(\mathcal D_n\simeq\bigvee^{\binom{n-1}{2}}S^2\). This is an integral homotopy equivalence, not merely a calculation of mod-two Betti numbers.

## Verification

The standalone file `verify.py` independently generates all adjacency matrices from the original graph definition, enumerates all vertex masks, and checks induced degrees, the exact mixed-face criterion, both generating functions, and all inclusion-maximal faces. It exhaustively checks \(3\le n\le8\), amounting to \(87{,}360\) masks. It separately computes ranks of simplicial boundary maps over \(\mathbb F_2\) for \(3\le n\le8\); every computed Betti vector is consistent with the theorem. The actual output of a successful run is `VERIFY_OK orders=3..8 subsets=87360 face_enumerator=PASS facet_enumerator=PASS all_feasible_sets=PASS homology_mod2_n3..8=PASS`. To reproduce: `python3 verify.py` with Python 3.8 or newer. These finite checks do not establish the infinite-family or integral homotopy assertions; Steps 1–4 do.

## Relationship to prior work

The concept of dissociation sets and their extremal enumeration is classical. Tu, Li and Du (2021, arXiv:2103.01402v1, Theorems 1.1–1.2) give universal bounds for maximal dissociation sets and identify extremizing graph classes; they do not provide this crown-graph face polynomial or complex homotopy type. Deshpande and Singh (arXiv:2001.05448v1, Theorem 3.5) compute higher-independence-complex homotopy for **complete multipartite graphs**: the result for \(K_{n,n}\) involves \(n^2-1\) circles and does not apply unchanged after deleting a perfect matching. Goyal, Shukla and Singh (arXiv:1905.06926v1, Proposition 3.2) compute the **ordinary** independence complex of the categorical product \(K_2\times K_n\), which is the crown graph; their answer is a wedge of \(n-1\) circles, for a different face condition. In particular, neither prior homotopy formula implies the present \(2\)-independence result.

Related published results on dissociation polynomials for complete multipartite graphs and generalized windmills concern different graph families and do not supply the crown classification. Other established crown-graph resolving, domination, fort and geodesic results concern different invariants. The present result has been compared at the level of statements and implications, not merely titles; see the accompanying scientific review for the scope of the search.

## Limitations

No claim is made for arbitrary matching-deleted complete bipartite graphs with unequal shores, arbitrary deletion sizes, or higher independence parameters beyond \(2\). The result concerns the entire finite family \(n\ge3\), not numerical extrapolation. Exhaustive checks cover only the declared finite range. Although no directly covering work was found in the inspected sources and database records, publication priority cannot be certified by finite search, and independent mathematical audit has not been performed.

## References

1. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1, first posted 2019-05-16, Proposition 3.2. https://arxiv.org/abs/1905.06926
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1, first posted 2020-01-15, Theorem 3.5. https://arxiv.org/abs/2001.05448
3. J. Tu, Y. Li and J. Du, *Maximal and Maximum Dissociation Sets in General and Triangle-Free Graphs*, arXiv:2103.01402v1, first posted 2021-03-02, Theorems 1.1–1.2. https://arxiv.org/abs/2103.01402
