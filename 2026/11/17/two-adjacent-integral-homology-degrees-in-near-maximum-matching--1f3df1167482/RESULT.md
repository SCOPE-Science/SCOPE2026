# Two adjacent integral homology degrees in near-maximum matching avoidance on two cycles

## Finding
For integers \(n,m\geq 6\), let \(G=C_n\sqcup C_m\), \(a=\lfloor n/2\rfloor\), \(b=\lfloor m/2\rfloor\), and \(q=a+b-1\). Let \(\operatorname{NM}_{q}(G)\) be the simplicial complex on the **edges** of \(G\) whose faces are edge sets with matching number strictly less than \(q\). Put \(s=a+b\). The complete reduced **integral** homology is
\[
\widetilde H_j(\operatorname{NM}_{s-1}(C_n\sqcup C_m);\mathbb Z)\cong
\begin{cases}\mathbb Z^2,&j=2s-6,\\\mathbb Z,&j=2s-5,\\0,&\text{otherwise}.\end{cases}
\]
In particular, the groups are torsion-free. The assertion includes odd and even cycles independently, with no restriction on their relative lengths. It is **not** a claim of a wedge-of-spheres homotopy equivalence.

## Assumptions and scope
The graphs are finite simple cycles on disjoint vertex sets, and all homology is reduced simplicial homology with integral coefficients. The threshold is exactly one below the maximum matching number of their disjoint union: \(q=s-1\). The length bound ensures \(a,b\ge3\), so every auxiliary non-matching complex below is a nonempty positive-dimensional sphere.

## Proof
Write \(E_1=E(C_n)\), \(E_2=E(C_m)\). Let \(\Delta_1\), \(\Delta_2\) be the full simplices on these edge sets, and put
\[
A=\operatorname{NM}_{a-1}(C_n),\quad C=\operatorname{NM}_{a}(C_n),\quad
B=\operatorname{NM}_{b-1}(C_m),\quad D=\operatorname{NM}_{b}(C_m).
\]
Here \(A\subset C\subset\Delta_1\) and \(B\subset D\subset\Delta_2\). The cycle/cyclic-polytope theorem, as restated with proof in Shan--Wang, Lemma 2.2, gives the **integral homotopy types**
\[
A\simeq S^{2a-5},\quad C\simeq S^{2a-3},\quad
B\simeq S^{2b-5},\quad D\simeq S^{2b-3}.
\]
The inclusions \(A\hookrightarrow C\) and \(B\hookrightarrow D\) are nullhomotopic: each domain is a sphere up to homotopy, two dimensions lower than its sphere target, whose homotopy groups below the target dimension vanish.

For edge subsets with matching numbers \(x\in[0,a]\), \(y\in[0,b]\), the face condition \(x+y\le a+b-2\) is equivalent to at least one of \(x\le a-2\), \(y\le b-2\), or \((x\le a-1\text{ and }y\le b-1)\). Consequently the desired complex \(K\) is **exactly**
\[
K=(A*\Delta_2)\cup(C*D)\cup(\Delta_1*B).
\]
The asterisk is simplicial join on the disjoint vertex sets. Define
\[
P=(A*\Delta_2)\cup(\Delta_1*B),\quad Q=C*D,\quad
R=P\cap Q=(A*D)\cup(C*B).
\]
The two terms of \(P\) are contractible and meet in \(A*B\simeq S^{2s-9}\). Mayer--Vietoris therefore gives \(\widetilde H_{2s-8}(P;\mathbb Z)=\mathbb Z\) and no other reduced homology. Furthermore \(Q\simeq S^{2s-5}\).

For \(R\), its two terms are \(A*D\simeq S^{2s-7}\) and \(C*B\simeq S^{2s-7}\); their intersection is \(A*B\simeq S^{2s-9}\). Both maps from this intersection into those two terms are nullhomotopic, since they are joins of the null maps \(B\to D\) or \(A\to C\) with an identity. The resulting Mayer--Vietoris calculation yields
\[
\widetilde H_j(R;\mathbb Z)=\begin{cases}\mathbb Z^2,&j=2s-7,\\\mathbb Z,&j=2s-8,\\0,&\text{otherwise}.\end{cases}
\]
The inclusion \(R\hookrightarrow P\) induces an **isomorphism** in reduced degree \(2s-8\). Indeed, the connecting maps in the two Mayer--Vietoris sequences for the unions defining \(R\) and \(P\) are both isomorphisms from this group onto \(\widetilde H_{2s-9}(A*B;\mathbb Z)\), and the naturality square commutes with the identity on \(A*B\). This verifies the crucial potentially nonzero map, rather than assuming it vanishes.

Apply the integral Mayer--Vietoris exact sequence to \(K=P\cup Q\), with \(R=P\cap Q\). The established isomorphism cancels the degree-\(2s-8\) groups, the two generators in degree \(2s-7\) of \(R\) give \(\widetilde H_{2s-6}(K)\cong\mathbb Z^2\), and the degree-\(2s-5\) generator of \(Q\) gives \(\widetilde H_{2s-5}(K)\cong\mathbb Z\). Exactness eliminates every other degree and any possible integral extension ambiguity. This proves the claim for **all** stated cycle lengths.

## Verification
The standalone standard-library Python program `verify_homology.py` enumerates forbidden matchings directly, builds every allowed simplex, and independently computes signed-incidence boundary ranks over \(\mathbb F_2\) (signs disappear in this field) for the five pairs \((n,m)=(6,6),(6,7),(7,7),(6,8),(8,8)\). The resulting reduced Betti ranks are \((2,1)\) in the two predicted consecutive degrees, with none elsewhere. Exact numbers of nonempty faces are \(2790,4444,6750,12882,56638\), respectively. The finite-field tests **cannot** establish the infinite family or the absence of integral torsion; both follow from the preceding integral proof.

## Relationship to prior work
Shan and Wang (first publicly posted 2026-09-02), Lemma 2.2, restate the earlier identification of a **single-cycle** non-matching complex with a cyclic-polytope boundary and prove edge-addition results for bipartite graphs. The present result credits that single-cycle input and instead determines two nonzero **integral** homology degrees for the **two-component** graph at the near-maximum matching threshold. Holmsen--Lee's general Leray vanishing bounds do not determine the lower-degree rank \(2\). Linusson--Shareshian--Welker treat complete and complete-bipartite graph families, not these disconnected cycles. Published mathematical research records for non-matching complexes, their cycle equivariance, and graph-family classifications were searched using both direct and equivalent terminology; no statement implying these exact two-component groups was located. This is evidence of nonoverlap, not proof of universal novelty.

## Limitations
The result determines integral homology but not the homotopy type, cup products, persistence maps, or automorphism representation. The cycles must each have at least six edges and the threshold is exactly \(a+b-1\). A previously unindexed computation or a general theorem with an implicit two-cycle corollary remains possible. Finite experiments cannot rule out such prior work or replace the integral argument.

## References
- J. Shan and Z. Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley-Reisner ideals*, arXiv:2609.02621 (first version 2026-09-02), especially Lemma 2.2 and Theorems 2.1 and 2.3. https://arxiv.org/abs/2609.02621
- A. F. Holmsen and S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270 (first version 2020-03-25). https://arxiv.org/abs/2003.11270
- S. Linusson, J. Shareshian and V. Welker, *Complexes of graphs with bounded matching size*, Journal of Algebraic Combinatorics (2008). The complete-graph and complete-bipartite cases are distinct from the present family.
