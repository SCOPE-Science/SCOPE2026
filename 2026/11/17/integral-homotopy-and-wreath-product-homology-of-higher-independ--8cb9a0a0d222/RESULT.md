# Integral homotopy and wreath-product homology of higher-independence windmill complexes

## Finding

Let \(n\ge 2\) and \(q\ge 3\) be integers. The **generalized windmill graph** \(W_{n,q}=K_1\vee(\bigsqcup_{i=1}^n K_q)\) has a universal center \(c\) and \(n\) pairwise nonadjacent clique blades, each containing \(q\) vertices. Put \(N=nq\). For an integer \(r\ge 1\), the higher-independence complex \(X_r=\operatorname{Ind}_r(W_{n,q})\) consists of all vertex subsets whose induced connected components each have at most \(r\) vertices.

For **every** \(2\le r\le N\), the following integral homotopy classification holds:

\[
X_r\simeq
\begin{cases}
\displaystyle\bigvee^{\binom{N-1}{r-1}} S^{r-1}\;\vee\;\bigvee^{\binom{q-1}{r}^{n}} S^{nr-1}, & 2\le r<q,\\[3pt]
\displaystyle\bigvee^{\binom{N-1}{r-1}} S^{r-1}, & q\le r\le N.
\end{cases}
\]

For \(r\ge N+1\), the complex is a simplex and is contractible. Thus, when \(2\le r<q\), its reduced integral homology is free, nonzero in **exactly two distinct degrees**, and has the displayed multiplicities.

Write \(V_m=\ker(\mathbb Z^m\xrightarrow{\mathrm{sum}}\mathbb Z)\), with its natural permutation action. The full graph-automorphism group is \(G=\mathfrak S_q\wr\mathfrak S_n\). Under this action, for \(2\le r\le N\),

\[
\widetilde H_{r-1}(X_r;\mathbb Z)\cong\bigwedge^{r-1}V_N.
\]

When \(2\le r<q\), the other nonzero integral homology module is

\[
\widetilde H_{nr-1}(X_r;\mathbb Z)\cong
\bigotimes_{i=1}^n\bigwedge^r V_q^{(i)},
\]

where each blade's symmetric group acts on its own factor and a permutation \(\sigma\) of the blades permutes the tensor factors with the **Koszul sign** \((\operatorname{sgn}\sigma)^r\). For \(q\le r\le N\), no second module occurs. These are integral homology-module statements, not claims of an equivariant wedge decomposition.

All positive-degree reduced rational homology invariants under \(G\) vanish. In particular, for all \(2\le r\le N\),

\[
\widetilde H_*(|X_r|/G;\mathbb Q)=0.
\]

Here the last assertion is rational acyclicity of the geometric quotient, not contractibility.

## Assumptions and scope

All graphs are finite, simple and undirected; joins of graphs and simplicial complexes are different operations. The wedge and suspension statements are for geometric realizations. Binomial coefficients have their usual integer meaning in the stated ranges. The integers \(n\ge2\), \(q\ge3\), and \(r\ge2\) are unrestricted beyond the displayed inequalities; no finite-parameter inference is used in proving the unrestricted result. The automorphism group fixes the unique universal vertex and acts on the blades by within-blade and blade permutations.

## Proof

**1. Center deletion, center link, and the cofiber.** Let \(B_{m,k}\) denote the complex of subsets of a fixed \(m\)-element set of size at most \(k\). Every selected noncenter vertex belongs to one of \(n\) disjoint cliques, so the deletion of the center in \(X_r\) is

\[
A=\operatorname{del}_{X_r}(c)=\bigast_{i=1}^n B_{q,\min(r,q)}.
\]

If the center is selected, all other selected vertices lie in its single connected induced component. Hence the link of the center is exactly \(L=\operatorname{lk}_{X_r}(c)=B_{N,r-1}\) when \(2\le r\le N\). Therefore \(X_r=A\cup_L(c*L)\), the mapping cone (homotopy cofiber) of the simplicial inclusion \(L\hookrightarrow A\).

**2. Skeleton lemma, including integral normalization.** For \(1\le k<m\), the complex \(B_{m,k}\) is homotopy equivalent to \(\binom{m-1}{k}\) copies of \(S^{k-1}\). Match each face not containing a fixed distinguished vertex and of size below \(k\) with the face formed by inserting that vertex; this is an acyclic element matching. The only unmatched nonempty faces after pairing the empty face are the \(k\)-subsets avoiding the distinguished vertex. The Morse model has one base point and exactly \(\binom{m-1}{k}\) cells of dimension \(k-1\), with no possible nonzero cellular differentials. For \(k=1\), this is the usual \(m\)-point space, a wedge of \(m-1\) zero-spheres.

More canonically, identify the augmented chain group in degree \(k-1\) with \(\bigwedge^k\mathbb Z^m\). Its simplicial boundary is contraction by the augmentation functional sending each standard basis vector to \(1\). Since \(\mathbb Z^m=V_m\oplus\mathbb Ze_m\) as abelian groups, the boundary kernel is \(\bigwedge^k V_m\). No higher chains occur in \(B_{m,k}\), whence the **natural integral permutation-module isomorphism**

\[
\widetilde H_{k-1}(B_{m,k};\mathbb Z)\cong\bigwedge^k V_m.
\]

**3. Homotopy splitting in every range.** If \(2\le r<q\), each blade complex \(B_{q,r}\) is a bouquet of \(\binom{q-1}{r}\) spheres of dimension \(r-1\). The join of all \(n\) such complexes is a bouquet of \(\binom{q-1}{r}^{n}\) spheres of dimension \(nr-1\), and in particular is \((nr-2)\)-connected. The link \(L=B_{N,r-1}\) has dimension \(r-2\), strictly below this connectivity bound. Thus every map \(L\to A\), including the actual inclusion, is nullhomotopic. Its mapping cone is therefore \(A\vee\Sigma L\). Applying the skeleton lemma to \(L\) yields the first line of the claimed homotopy classification.

If \(q\le r\le N\), each blade complex \(B_{q,q}\) is a full simplex, so \(A\) is contractible. The same cofiber description gives \(X_r\simeq\Sigma L\), yielding the second line. If \(r\ge N+1\), every induced connected component has at most \(N+1\) vertices, so every subset is a simplex.

**4. Integral symmetry modules.** All constructions above are natural under \(G\). The long exact homology sequence of the cofiber \(L\to A\to X_r\), together with the strict separation \(nr-1>r-1\) for \(n,r\ge2\), identifies the low-degree module with \(\widetilde H_{r-2}(L;\mathbb Z)=\bigwedge^{r-1}V_N\). In the range \(r<q\), the high-degree module is \(\widetilde H_{nr-1}(A;\mathbb Z)\). The integral Künneth isomorphism for joins, which has no \(\operatorname{Tor}\) terms here, identifies it with the tensor product of the blade modules. Swapping two join factors of dimension \(r-1\) contributes \((-1)^{r^2}=(-1)^r\), precisely the stated Koszul sign. The cases \(r\ge q\) have no high-degree homology.

**5. Rational quotient.** Over \(\mathbb Q\), the augmentation representation on all \(N\) outer vertices decomposes, as a module for the normal subgroup \((\mathfrak S_q)^n\), into the blade augmentation representations plus the standard augmentation representation of block labels:

\[
V_N\otimes\mathbb Q\cong
\left(\bigoplus_{i=1}^n V_q^{(i)}\otimes\mathbb Q\right)
\oplus\left(V_n\otimes\mathbb Q\right).
\]

For \(1\le a\le q-1\), \(\bigwedge^a(V_q\otimes\mathbb Q)\) is the nontrivial irreducible hook representation of \(\mathfrak S_q\) and has no invariant vector. Thus invariants of \(\bigwedge^{r-1}(V_N\otimes\mathbb Q)\) under the blade-wise subgroup lie in \(\bigwedge^{r-1}(V_n\otimes\mathbb Q)\). The latter has no \(\mathfrak S_n\)-invariants for \(r-1\ge1\), being either zero or a nontrivial exterior power of the standard representation. The high-degree tensor product also has no blade-wise invariants because each factor \(\bigwedge^r(V_q\otimes\mathbb Q)\) is nontrivial for \(r<q\). Therefore every positive-degree invariant is zero. Since \(X_r\) is connected for \(r\ge2\), the finite-group transfer theorem (or equivariant barycentric subdivision) gives \(\widetilde H_*(|X_r|/G;\mathbb Q)=0\).

## Verification

The standalone standard-library program `verify.py` independently verifies all 7,552 potential vertex subsets using induced-graph connected components for nine parameter choices, then enumerates all faces and computes the **reduced** simplicial boundary ranks over \(\mathbb F_2\), compares all nonzero Betti numbers with the theorem, and checks signed reduced Lefschetz traces against the stated two integral module characters. It checks **3,519 faces and 528 direct character instances**. For three additional full automorphism-group sweeps (altogether **2,520** group elements), it verifies the exact zero character averages of both proposed modules. Run `python3 verify.py` from the extracted package root. The recorded output is `verification_output.txt`, ending with `WINDMILL_HIGHER_INDEPENDENCE_FINITE_CHECKS_PASS`.

These finite tests check the normalization, boundary conventions, and symmetry signs; the unrestricted theorem is proved by the cofiber and skeleton arguments above, not by extrapolation. Independent mathematical validation has not been performed.

## Relationship to prior work

Deshpande and Singh study higher-independence complexes of complete multipartite graphs, fully whiskered graphs, paths, cycles and regular rooted trees, but not this clique-bouquet family. Abdelmalek, Deshpande, Goyal, Roy and Singh prove structural chordal results, including caterpillar vertex decomposability and chordal counterexamples, not the explicit windmill homology modules. Sawant's 2026 theorem proves vertex decomposability for **trees**, whereas a windmill with \(q\ge3\) has triangles and is not a tree. These general structural results do not imply the exact two-degree multiplicities or wreath-product actions without further argument.

A publicly indexed calculation of the **dissociation polynomial** and maximal dissociation sets of generalized windmills covers face counts for the special case \(r=2\). That enumeration is not asserted here as novel; it neither gives the integral homotopy and representation classification nor covers the new range \(r\ge3\). Another indexed result treats Lovász **neighborhood complexes** for the same graph construction, which are different simplicial complexes. No equivalent full statement was identified in the searched literature and indexed records. Inaccessible or unindexed relevant work remains a residual originality risk.

## Limitations

The result assumes \(n\ge2\), \(q\ge3\), and the standard higher-independence definition; it does not classify the ordinary \(r=1\) case. The wedge equivalence is nonequivariant, although the integral homology modules are equivariantly identified. Rational acyclicity of the quotient does not imply integral acyclicity or contractibility. Finite computations alone do not establish the unrestricted theorem, and the literature search cannot exclude unindexed equivalent work.

## References

1. R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150, first submitted 2026-05-24, https://arxiv.org/abs/2605.25150.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first submitted 2020-01-15, https://arxiv.org/abs/2001.05448.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first submitted 2021-06-21, https://arxiv.org/abs/2106.10863.
4. *Dissociation polynomial and all maximal dissociation sets of generalized windmills*, public indexed research record (2026-10-04), identifier `2026/10/4/SCOPE-dissociation-polynomial-and-all-maximal-dissociation-sets-of-gen--2c55298c97bc`.
5. *Clique joins suspend Lovász neighborhood complexes*, public indexed research record (2026-10-11), identifier `2026/10/11/SCOPE-clique-joins-suspend-lov-sz-neighborhood-complexes--46728c3e0714`.
