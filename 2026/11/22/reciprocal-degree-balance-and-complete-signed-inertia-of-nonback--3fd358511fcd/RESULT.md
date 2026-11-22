# Reciprocal-degree balance and complete signed inertia of nonbacktracking self-commutators

## Finding
Let \(G\) be a finite, connected, simple, undirected graph with \(n\) vertices, \(m\) edges, and minimum degree at least three. Write \(B\) for its ordinary unnormalized nonbacktracking (Hashimoto) matrix on the \(2m\) directed edges and
\[
K=B^{\mathsf T}B-BB^{\mathsf T}.
\]
The selfadjoint matrix \(K\) has equally many strictly positive and strictly negative eigenvalues. Their number \(\nu(G)\), **on each side**, is determined exactly by bipartiteness and one reciprocal-degree balance:
\[
\boxed{
\nu(G)=
\begin{cases}
n-1,&G\text{ nonbipartite};\\
n-2,&G\text{ bipartite and }\Delta_G=0;\\
n-1,&G\text{ bipartite and }\Delta_G\ne0,
\end{cases}
}
\qquad
\Delta_G=\sum_{v\in L}\frac1{d_v-2}-\sum_{v\in R}\frac1{d_v-2}
\]
where \(L,R\) are the two bipartite classes. The remaining \(2m-2\nu(G)\) eigenvalues are zero. Reversing the choice of \(L,R\) changes only the sign of \(\Delta_G\), so the classification is intrinsic.

Two quantitative consequences hold. First,
\[
\boxed{
\|K\|_{\mathcal S_2}^{2}=
2\sum_{v\in V(G)}d_v^2(d_v-2)^2
-4\sum_{\{u,v\}\in E(G)}(d_u-2)(d_v-2).
}
\]
Second, for a \(d\)-regular graph (\(d\ge3\)), if \(\lambda_1,\ldots,\lambda_n\) are the real adjacency eigenvalues, the **entire** spectrum of \(K\), with multiplicity, consists of
\[
\boxed{\pm d(d-2)\sqrt{1-(\lambda_j/d)^2}\quad(1\le j\le n)}
\]
together with \(2m-2n\) additional zeros. A zero square root contributes two zeros. This regular-graph expression is a consistency corollary; the reciprocal-degree inertia dichotomy for arbitrary irregular graphs is the central assertion.

## Assumptions and scope
The graph is undirected, connected, finite and simple; each edge has both orientations. Its vertex degrees obey \(d_v\ge3\). Set
\[
B_{(u,v),(x,y)}=\mathbf 1_{\{v=x,\ y\ne u\}},\quad
K=B^{\mathsf T}B-BB^{\mathsf T}.
\]
All eigenvalue multiplicities are algebraic, equivalently geometric because \(K\) is real symmetric. The statements concern this **unnormalized** Hashimoto operator; replacing it by a degree-normalized walk generally changes the formulas. No claim is made for graphs with vertices of degree one or two, disconnected graphs, or directed/weighted/multigraph versions.

## Proof
**1. The exact incidence identity.** Index each directed edge by its tail and head. Define \(2m\)-by-\(n\) matrices \(X\) and \(Y\) by
\[
X_{(u,v),a}=\mathbf1_{u=a},\qquad Y_{(u,v),a}=\mathbf1_{v=a},
\qquad W=\operatorname{diag}(d_a-2).
\]
For two directed edges sharing a tail \(a\), their columns in \(B\) have exactly \(d_a-2\) common predecessors when the directed edges differ, and \(d_a-1\) when they are equal. The analogous count for common successors uses the head. Therefore
\[
B^{\mathsf T}B=I_{2m}+XWX^{\mathsf T},\qquad
BB^{\mathsf T}=I_{2m}+YWY^{\mathsf T},
\]
so \(K=XWX^{\mathsf T}-YWY^{\mathsf T}\). The reversal permutation \(J(u,v)=(v,u)\) interchanges \(X\) and \(Y\) and hence satisfies \(JKJ=-K\). Thus every nonzero eigenvalue occurs with its negative, with identical multiplicity.

**2. An exact rank lemma.** Put \(Z=[X\ \ Y]\) and \(H=\operatorname{diag}(W,-W)\), so \(K=ZHZ^{\mathsf T}\). Since all degrees exceed two, \(H\) is invertible. For any real \(N\)-by-\(r\) matrix \(Z\) and invertible real symmetric \(r\)-by-\(r\) matrix \(H\), let \(L=\ker Z\), \(\ell=\dim L\), and let \(q\) be the rank of the symmetric bilinear form \((a,b)\mapsto a^{\mathsf T}H^{-1}b\) restricted to \(L\). Then
\[
\operatorname{rank}(ZHZ^{\mathsf T})=r-2\ell+q.
\]
Indeed, \(Z^{\mathsf T}\) is an isomorphism from \((\ker Z^{\mathsf T})^{\perp}\) onto \(L^{\perp}\). Its vectors giving zero under \(ZHZ^{\mathsf T}\) correspond precisely to \(a\in L^{\perp}\) with \(Ha\in L\). Under the bijection \(a\mapsto Ha\), this set is the radical of the restricted \(H^{-1}\)-form on \(L\), of dimension \(\ell-q\). Subtracting from \(\dim L^{\perp}=r-\ell\) proves the displayed identity.

**3. Identify the incidence kernel.** A vector \((a,b)\in\mathbb R^n\oplus\mathbb R^n\) lies in \(L=\ker Z\) exactly when
\[
a_u+b_v=0\quad\text{for every oriented edge }(u,v).
\]
Connectivity and the existence of both orientations imply that \(a\) is constant on even-walk parity classes and \(b\) takes the opposite values on the opposite classes. If \(G\) is nonbipartite, an odd cycle merges the two parity classes: \(L\) is one-dimensional, spanned by \((\mathbf1,-\mathbf1)\). The restricted \(H^{-1}\)-form is identically zero, because its two diagonal blocks are equal and opposite; hence \(\ell=1,q=0\). The rank lemma gives \(\operatorname{rank}K=2n-2\).

If \(G\) is bipartite, choose two basis vectors for \(L\): the first has \(a=\mathbf1_L\) and \(b=-\mathbf1_R\); the second has \(a=\mathbf1_R\) and \(b=-\mathbf1_L\). In this basis the restricted form has Gram matrix \(\operatorname{diag}(\Delta_G,-\Delta_G)\). Thus \(\ell=2\), with \(q=0\) at \(\Delta_G=0\) and \(q=2\) otherwise. Consequently \(\operatorname{rank}K=2n-4\) in the balanced case and \(2n-2\) otherwise. Reversal symmetry halves each rank into equal positive and negative indices. The nullities follow by subtraction from \(2m\).

**4. Quantitative identities.** The incidence products are
\[
X^{\mathsf T}X=Y^{\mathsf T}Y=D=\operatorname{diag}(d_v),
\quad X^{\mathsf T}Y=A,
\]
where \(A\) is the adjacency matrix. Expanding \(\operatorname{tr}K^2\) and using \(\operatorname{tr}(WAWA)=2\sum_{\{u,v\}\in E}w_uw_v\) gives the stated Hilbert--Schmidt identity.

When \(G\) is \(d\)-regular, \(U=X/\sqrt d\) and \(V=Y/\sqrt d\) are isometries with \(U^{\mathsf T}V=A/d\). Then \(K=d(d-2)(UU^{\mathsf T}-VV^{\mathsf T})\). Diagonalizing the symmetric overlap \(A/d\) and using the elementary two-subspace projection formula shows that each overlap eigenvalue \(c=\lambda_j/d\) produces the two eigenvalues \(\pm\sqrt{1-c^2}\); zeros are retained when \(|c|=1\). The orthogonal complement of \(\operatorname{ran}U+\operatorname{ran}V\) supplies the additional \(2m-2n\) zeros in the displayed multiset. This proves the regular-graph formula.

## Verification
A standalone finite checker (`verify.py`) constructs the nonbacktracking matrix directly and separately constructs both incidence matrices for regular, irregular bipartite, and irregular nonbipartite examples. It verifies the exact integer-matrix factorization, reversal anticommutation, both inertia counts, nullity, the integer-valued trace-square identity, and, when regular, the full eigenvalue formula. It returned `VERIFICATION_OK 474`. Its numerical eigenspectrum tolerance is \(10^{-6}\); finite checks do not replace the rank proof, do not exhaust all graphs, and do not independently certify mathematical novelty.

For example, \(K_{3,4}\) has \(n=7\), \(\Delta_G=-5/2\), and six eigenvalues of each sign, whereas deleting one edge from \(K_{4,4}\) gives a connected irregular graph with \(\Delta_G=0\), \(n=8\), and six of each sign. The pair illustrates that irregularity alone does not determine the nullity; the signed reciprocal-degree balance does.

## Relationship to prior work
The unnormalized nonbacktracking matrix and its ordinary eigenvalue spectrum are classical. Glover and Kempton (arXiv:2011.09385v1, 18 November 2020) derive an Ihara-type block reduction and adjacency-spectrum relation. Their auxiliary matrix also uses the letter \(K\), but it is **not** the self-commutator here. Jost, Mulas and Torres (arXiv:2203.10824v1, 21 March 2022) analyze nonbacktracking Laplacian eigenvalues. Mulas, Zhang and Zucal (arXiv:2303.00373v1, 1 March 2023) study, among other topics, singular values of that Laplacian. Kwon (arXiv:2607.21294v1, 23 July 2026, Proposition 5.1) supplies a general Hashimoto incidence factorization in a distinct entropy/inverse-realization problem, which is compatible with the first identity above. None of these inspected statements provides the reciprocal-degree-balanced positive/negative inertia count of the self-commutator. An ordinary nonnormal spectrum or incidence factorization alone does not yield the signed inertia without analyzing the restricted indefinite form; that analysis is the new assertion. The regular adjacency formula is treated as a related consequence, not claimed independent of standard principal-angle or known regular nonbacktracking reductions.

## Limitations
The classification is restricted to connected simple graphs with minimum degree at least three and to the unnormalized matrix. It describes signed indices and a trace-square invariant; for irregular graphs it does not determine every eigenvalue. The result is mathematically proved here, but has not had independent external validation. Searches cannot exclude an unindexed equivalent identity in earlier spectral graph theory, signed-incidence, or Krein-space literature.

## References
1. C. Glover and M. Kempton, *Spectral properties of the non-backtracking matrix of a graph*, arXiv:2011.09385v1 (18 November 2020), https://arxiv.org/abs/2011.09385.
2. J. Jost, R. Mulas, and L. Torres, *Spectral theory of the non-backtracking Laplacian for graphs*, arXiv:2203.10824v1 (21 March 2022), https://arxiv.org/abs/2203.10824.
3. R. Mulas, D. Zhang, and G. Zucal, *There is no going back: Properties of the non-backtracking Laplacian*, arXiv:2303.00373v1 (1 March 2023), https://arxiv.org/abs/2303.00373.
4. S. Kwon, *Critical-exponent stratification and inverse realization on biregular trees*, arXiv:2607.21294v1 (23 July 2026), https://arxiv.org/abs/2607.21294, Proposition 5.1.
