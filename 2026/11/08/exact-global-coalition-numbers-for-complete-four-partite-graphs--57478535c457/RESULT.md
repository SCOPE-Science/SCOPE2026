# Exact global coalition numbers for complete four-partite graphs

## Finding

**Theorem.** Let \(G=K_{a,b,c,d}\) be a finite simple complete four-partite graph, where \(a\ge b\ge c\ge d\ge1\). A *global coalition partition* is a vertex partition into nonempty classes, none of which dominates both \(G\) and its complement, such that every class has a **distinct** partner class whose union dominates both graphs. Let \(GC(G)\) denote the maximum number of classes in such a partition. Then

\[
\boxed{
GC(K_{a,b,c,d})=
\begin{cases}
a+1,&d=1,\\
a+b,&d=2,\\
a+b+c-3,&3\le d\le5,\\
a+b+c+d-8,&d\ge6.
\end{cases}}
\]

The formula is valid for every positive integer quadruple, including all unequal and boundary profiles; none of the part sizes is assumed large. As an illustrative specialization, for four equal parts of size \(m\), the values are \(2,4,6,9\) for \(m=1,2,3,4\), respectively, and \(4m-8\) for every \(m\ge5\).

Equivalently, take the maximum over the feasible members of the four lower-bound templates \(a+1\), \(a+b\), \(a+b+c-3\), and \(a+b+c+d-8\), available at smallest-part sizes at least one, two, three, and four, respectively. The proof below shows that no other pattern exceeds them and then simplifies this maximum to the displayed four regimes.

## Assumptions and scope

All graphs are finite, simple, undirected. Write the four specified independent partite classes as \(V_1,V_2,V_3,V_4\) and their sizes as \(n_1,n_2,n_3,n_4\). A set dominates a graph if each vertex outside the set has a neighbour in it; vertices in the set are considered dominated. For \(A\subseteq V(G)\), write \(\operatorname{supp}(A)=\{i:A\cap V_i\ne\varnothing\}\).

Since the complement of \(G\) is the disjoint union of the four cliques induced by the parts, \(A\) globally dominates if and only if its support is the complete index set \(\{1,2,3,4\}\). Accordingly, every partition block has a nonempty **proper** support, and two distinct blocks are coalition partners precisely when the union of their supports is the full index set. A *one-part block* below means a block supported on one part, not necessarily a one-vertex block.

## Proof

**Construction of the four lower bounds.** For any \(t\in\{1,2,3,4\}\), suppose each of the four parts has at least \(t\) vertices when \(t<4\), or at least four vertices when \(t=4\). Choose \(t\) special blocks \(H_i\), indexed by the first \(t\) parts. Each \(H_i\) meets every part other than \(V_i\), and avoids \(V_i\). For \(t<4\), distribute all vertices in the remaining \(4-t\) parts among these \(t\) special blocks, retaining at least one from each relevant part in each \(H_i\). For \(j\le t\), give one vertex of \(V_j\) to each special block \(H_i\) with \(i\ne j\), and put the remaining \(n_j-(t-1)\) vertices into one-vertex blocks. Every one-vertex block from \(V_j\) partners with \(H_j\); if \(t\ge2\), distinct special blocks also partner one another. For \(t=1\), the special block partners all one-vertex blocks. The resulting numbers of blocks are \(n_1+1\) for \(t=1\), \(n_1+n_2\) for \(t=2\), \(n_1+n_2+n_3-3\) for \(t=3\), and \(N-8\) for \(t=4\), where \(N=a+b+c+d\). The \(t=2,3,4\) constructions require respectively \(d\ge2,3,4\). This establishes the lower bound in the theorem.

**Upper bound if a part has one vertex.** Suppose \(d=1\). The unique block \(H\) containing the vertex of the smallest part misses at least one other part, say \(V_j\), since no block may be a global dominating set. Every other block omits the singleton part, and hence can have no coalition partner except \(H\). Thus every other block meets \(V_j\), and there are at most \(n_j\le a\) such blocks. Therefore \(GC(G)\le a+1\), matching the first construction.

Assume henceforth \(d\ge2\), and let \(\pi\) be any global coalition partition. Let \(J\) be the set of part indices occurring as the support of at least one **one-part block**. Put \(q=|J|\). For each \(i\in J\), any coalition partner of such a block must have support exactly \(\{1,2,3,4\}\setminus\{i\}\), a three-part support. These \(q\) compulsory blocks are distinct. Let \(c_i\) be the number of blocks meeting \(V_i\); since blocks are disjoint, \(c_i\le n_i\). We distinguish five cases.

**Case \(q=0\).** Every block meets at least two parts, so \(2|\pi|\le\sum_i c_i\le N\). Because \(a+b\ge c+d\), this gives \(|\pi|\le a+b\).

**Case \(q=4\).** Four compulsory three-part blocks each contribute two extra part incidences relative to one incidence per block. Hence \(\sum_i c_i\ge|\pi|+8\) and \(|\pi|\le N-8\). Moreover, each part must supply three vertices to these compulsory blocks and at least one vertex to its own one-part block, so \(d\ge4\).

**Case \(q=3\).** Let \(J=\{i,j,k\}\) and let \(\ell\) denote the remaining part. Every block meets at least one part indexed by \(J\), since otherwise it would be a one-part block in \(V_\ell\). Each of the three compulsory complementary supports meets exactly two of the parts in \(J\), so
\[
|\pi|+3\le c_i+c_j+c_k\le n_i+n_j+n_k\le a+b+c.
\]
The compulsory blocks need three distinct vertices of \(V_\ell\), and each part in \(J\) needs two such vertices plus a one-part block. Thus \(d\ge3\), and \(|\pi|\le a+b+c-3\), an available lower-bound candidate.

**Case \(q=2\).** Write \(J=\{i,j\}\) and let \(h,\ell\) be the remaining two indices. The two compulsory triples use one vertex from each of \(V_i,V_j\), and two from each of \(V_h,V_\ell\). Every block either meets \(V_i\cup V_j\), or has support exactly \(\{h,\ell\}\). Let \(x\) count blocks of the latter type. Necessarily \(0\le x\le\min(n_h,n_\ell)-2\). If \(x=0\), then \(|\pi|\le c_i+c_j\le n_i+n_j\le a+b\). If \(x>0\), at least one of these \(x\) blocks needs a partner meeting **both** \(V_i\) and \(V_j\). Such a partner is counted twice in \(c_i+c_j\), so
\[
|\pi|\le c_i+c_j-1+x\le n_i+n_j+\min(n_h,n_\ell)-3.\tag{1}
\]
If \(d\ge3\), the last expression is at most \(a+b+c-3\), since it is the sum of three distinct part sizes minus three. If \(d=2\) and \(\min(n_h,n_\ell)=2\), then \(x=0\), already handled. If \(d=2\) and \(\min(n_h,n_\ell)\ge3\), at least one part in \(J\) has size two, and the last expression in (1) is at most the sum of two distinct part sizes minus one, hence at most \(a+b\). Therefore this case never beats an available candidate.

**Case \(q=1\).** Let \(J=\{i\}\), and let \(a'\ge b'\ge c'\) be the sizes of the other three parts. Denote by \(u\) the number of blocks avoiding \(V_i\), and let \(H\) be the set of other part indices met by **some** block that also meets \(V_i\). The unique required support type complementary to \(\{i\}\) ensures that at least one block avoiding \(V_i\) meets all three other parts. Any other block avoiding \(V_i\) has support of size at least two, since \(J\) contains only \(i\). Thus
\[
u\le\left\lfloor\frac{a'+b'+c'-1}{2}\right\rfloor,\qquad |\pi|\le n_i+u.\tag{2}
\]
If \(|H|=0\), every block avoiding \(V_i\) must meet all three other parts (a two-part support would have no possible partner), so \(u\le c'\le a'\). If \(|H|=1\), any two-part support avoiding \(V_i\) must omit the single index in \(H\); therefore every such block meets both other indices and \(u\le a'\). If \(|H|=2\), any block avoiding \(V_i\) must meet the sole index outside \(H\), again giving \(u\le a'\).

Suppose \(|H|=3\). Every other part supplies at least one vertex to a block meeting \(V_i\), and a distinct vertex to the compulsory complementary three-part block. The remaining \(u-1\) blocks avoiding \(V_i\) require at least two vertices each. Therefore
\[
u\le 1+\left\lfloor\frac{a'+b'+c'-6}{2}\right\rfloor.\tag{3}
\]
If \(c'\le5\), then \(u\le a'\), using \(b'\le a'\) and \(c'\le5\). In all four subcases \(q=1\) with \(c'\le5\), we obtain \(|\pi|\le n_i+a'\le a+b\).

It remains to treat \(c'\ge6\). If \(d\le4\), the selected part \(V_i\) must be a smallest part, so \(n_i=d\le4\). Put \(T=a'+b'\ge12\). Since \(c'\le T/2\), inequality (2) gives
\[
|\pi|\le4+\left\lfloor\frac{3T-2}{4}\right\rfloor\le T=a+b.
\]
The final elementary inequality holds for integers \(T\ge12\) (directly at \(12,13\), and algebraically for \(T\ge14\)). If \(d=5\), then \(n_i=5\) and \(S=a'+b'+c'\ge18\), so (2) gives
\[
|\pi|\le5+\left\lfloor\frac{S-1}{2}\right\rfloor\le S-3=a+b+c-3.
\]
Finally, if \(d\ge6\), all three other parts have sizes at least six, so \(S=a'+b'+c'\ge18\). Inequality (2) directly gives
\[
N-|\pi|\ge S-\left\lfloor\frac{S-1}{2}\right\rfloor\ge10>8,
\]
so \(|\pi|\le N-8\), the available fourth construction.

All five cases give the asserted upper bound. Combined with the constructions, this proves the theorem.

## Verification

The standalone standard-library `verify.py` checks the formula by a second exhaustive support-multiplicity enumeration on all 70 sorted size profiles with entries from one through five and seven additional unbalanced profiles. The search considers every multiplicity of all 14 proper nonempty four-part supports up to part capacities and checks the coalition-partner condition independently. It also checks seven small graphs by enumerating all unordered vertex partitions directly and testing **both original graph and complement domination conditions**, without appealing to support reduction. The verifier reports `VERIFY_OK` on success. Finite tests corroborate the proof; they do not prove its unbounded quantifiers.

## Relationship to prior work

Anholcer, Besharati, Mojdeh and Samadzadeh, *Global coalitions in graphs* (arXiv:2509.15386, earliest submission September 18, 2025; expanded version October 25, 2026), define global coalitions, establish multipartite lower-bound constructions (Proposition 6), and determine exact values for at most three parts (Theorem 7). Their Conjecture 54 asks for sharpness across all complete multipartite graphs. The present result settles the complete four-part case, including unequal and small parts. It uses their near-transversal lower-bound templates but adds an upper-bound proof that also resolves mixed two-support configurations and the one-part boundary. Their equivalence with ordinary coalition numbers of complementary disjoint unions of cliques provides another formulation.

An earlier large-minimum-part theorem establishes \(GC(K_{n_1,\ldots,n_r})=N-r(r-2)\) whenever \(r\ge4\) and \(\min_i n_i\ge3r-6\). Accordingly, the large-size fourth-part regime in the present statement is **not claimed as new**; the contribution is the **complete determination at every smaller part profile** for exactly four parts, including discontinuous boundaries, as well as the resulting exact all-profile theorem. Both sources are compared by implication, not merely by parameter names.

## Limitations

The theorem determines the maximum number of classes only, not the number of maximizing partitions. It applies to graphs with exactly four nonempty independent parts; it does not resolve all larger multipartite cases of Conjecture 54. The small-part conditions are essential to the piecewise proof, not assumptions restricting the theorem's domain. The finite verifier provides no independent audit or guarantee of historical priority. Possible unindexed equivalent results for disjoint unions of four cliques remain a residual literature risk.

## References

1. M. Anholcer, N. Besharati, D. A. Mojdeh, and M. R. Samadzadeh, *Global coalitions in graphs*, arXiv:2509.15386 (first submitted 18 September 2025; version 4 dated 25 October 2026), https://arxiv.org/abs/2509.15386. See Definitions 1–2, Proposition 6, Theorem 7, Corollary 18 and Conjecture 54.
2. T. W. Haynes, J. T. Hedetniemi, S. T. Hedetniemi, A. A. McRae, and R. Mohan, *Introduction to coalitions in graphs*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 653–659, https://doi.org/10.1080/09728600.2020.1832874.
3. *Eventual exactness and rigidity of multipartite global coalition partitions*, earlier mathematical research record; threshold statement for \(r\ge4\), \(\min_i n_i\ge3r-6\).
