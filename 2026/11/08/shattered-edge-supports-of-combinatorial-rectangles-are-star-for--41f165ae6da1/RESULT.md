# Shattered edge supports of combinatorial rectangles are star forests

## Finding
Fix integers \(p,q\geq1\). On the query domain \([p]\times[q]\), let \(\mathcal R_{p,q}\) be the family of all Cartesian rectangles \(A\times B\), with \(A\subseteq[p]\) and \(B\subseteq[q]\), including the empty rectangle (only once). Interpret a query set \(S\subseteq[p]\times[q]\) as the edge set of a bipartite graph \(G_S\) with left vertex set \([p]\) and right vertex set \([q]\).

**Complete shattering theorem.** The support \(S\) is shattered by \(\mathcal R_{p,q}\) if and only if every nontrivial connected component of \(G_S\) is a star. Equivalently, \(G_S\) contains no (not necessarily induced) simple path of three edges. Isolated graph vertices are permitted. The empty support is shattered.

Writing \(\Phi_{p,q}(z)=\sum_{S\text{ shattered}}z^{|S|}\), the complete two-sort labeled exponential generating function is
\[
\sum_{p,q\geq0}\Phi_{p,q}(z)\frac{u^p v^q}{p!q!}
=\exp\!\left(u+v+uvz+u(e^{vz}-1-vz)+v(e^{uz}-1-uz)\right).
\]
Here the summands with \(p=0\) or \(q=0\) are defined by the unique empty concept; consequently \(\Phi_{p,0}=\Phi_{0,q}=1\).

The exact two learning dimensions, for every \(p,q\geq1\), are
\[
\operatorname{Ldim}(\mathcal R_{p,q})=p+q-1,
\qquad
\operatorname{VCdim}(\mathcal R_{p,q})=
\begin{cases}
\max\{p,q\}, &\min\{p,q\}=1,\\
p+q-2,&p,q\geq2.
\end{cases}
\]
Thus the online dimension exceeds the static VC dimension by exactly one when both sides have at least two vertices, and the two dimensions agree on a one-row or one-column domain.

A sharp one-parameter specialization is
\[
\Phi_{2,q}(z)=(1+2z)^q+qz^2\qquad(q\geq1).
\]
In particular, the complete cardinality distribution is available without enumerating the \(2^{2q}\) query supports.

## Assumptions and scope
A binary concept is the indicator function of a rectangle. A support \(S\) is shattered if for every assignment \(\sigma:S\to\{0,1\}\), some \(A\times B\) agrees with \(\sigma\) on \(S\). The Littlestone dimension is the largest depth of a complete binary query tree whose root-to-leaf label paths can all be realized by the concept class; the depth of a singleton class is zero. All vertex labels are distinct and all edges in a support are distinct. A path of three edges means four distinct alternating vertices, regardless of whether an additional closing edge is present. These definitions are important: forbidding induced paths would instead allow four-cycles, which are not shattered.

## Proof
**1. Necessity.** Suppose \(G_S\) contains a path with successive edges \((i,j)\), \((i',j)\), \((i',j')\), where \(i\ne i'\), \(j\ne j'\). The labeling that makes the first and third edges positive and the middle edge negative is impossible: the positive labels force \(i,i'\in A\) and \(j,j'\in B\), so \((i',j)\in A\times B\). Thus a shattered graph has no three-edge path. A finite graph without such a path has every nontrivial connected component a star: if a component is not a star, either it contains a cycle (giving a three-edge simple path in a bipartite graph), or, as a tree, it has diameter at least three. The same conclusion follows directly from the criterion that no edge has both endpoints of degree at least two.

**2. Sufficiency.** Suppose \(G_S\) is a star forest. For an arbitrary binary labeling, let \(A\) be the left endpoints of positively labeled edges and let \(B\) be their right endpoints. Every positive edge belongs to \(A\times B\). If a negative edge \((i,j)\) also belonged to the rectangle, then both its endpoints would be incident to some positive edge. Yet in a star forest at least one endpoint of every edge is a leaf of degree one. That endpoint's only queried edge is the negative one, so it cannot be incident to a positive edge. This contradiction establishes the required trace; the all-negative trace is realized with \(A=B=\varnothing\).

**3. Enumerating all shattered supports.** A labeled bipartite star forest decomposes uniquely into connected components, each being one isolated left vertex, one isolated right vertex, one single edge, a star centered at a left vertex with at least two right leaves, or a star centered at a right vertex with at least two left leaves. Assigning weights \(u\) per left vertex, \(v\) per right vertex and \(z\) per edge, the connected component exponential generating series is
\[
u+v+uvz+u\sum_{j\geq2}\frac{(vz)^j}{j!}
+v\sum_{i\geq2}\frac{(uz)^i}{i!}.
\]
The labeled exponential formula gives the stated generating function. For exactly two left vertices, supports not using both left vertices have polynomial \(2(1+z)^q-1\). Supports using both and having disjoint nonempty neighborhoods contribute \((1+2z)^q-2(1+z)^q+1\). The only remaining star forests consist of one two-edge star centered at a right vertex, contributing \(qz^2\). Adding gives \(\Phi_{2,q}(z)=(1+2z)^q+qz^2\).

**4. VC dimension.** If \(\min\{p,q\}=1\), every subset of the single row or column is itself a rectangle, so all \(\max\{p,q\}\) available queries are shattered. For \(p,q\geq2\), let a shattered support have \(c\) nontrivial components and \(w\) nonisolated vertices. Since it is a forest, \(|S|=w-c\). With at least two nontrivial components, \(|S|\leq p+q-2\). With exactly one, it is a star with at most \(\max\{p,q\}\leq p+q-2\) edges. The bound is attained by the disjoint union of the star from the first left vertex to all right vertices except the first, and the star from the first right vertex to all left vertices except the first. It has \(p+q-2\) edges. This proves the VC formula.

**5. Littlestone dimension.** The number of distinct rectangles is exactly
\[
H=1+(2^p-1)(2^q-1)=2^{p+q}-2^p-2^q+2<2^{p+q}.
\]
Any complete mistake tree of depth \(d\) requires at least \(2^d\) distinct concepts, since different leaves have incompatible answer paths. Thus \(\operatorname{Ldim}\leq p+q-1\).

For the reverse inequality, use induction on \(p+q\). The case \((p,q)=(1,1)\) has two concepts and Littlestone dimension one. Query the cell \((1,1)\). Conditional on a positive answer, the first left vertex and first right vertex are included in the rectangle, while membership of the other \(p-1\) left vertices and \(q-1\) right vertices can be queried independently via cells \((i,1)\) and \((1,j)\). Therefore the positive branch contains a complete mistake tree of depth \(p+q-2\). If \(p\geq2\), the negative branch contains all rectangles avoiding the first left vertex, an isomorphic copy of \(\mathcal R_{p-1,q}\) on the other rows; by induction it supports depth \(p+q-2\). If \(p=1\), the negative branch contains every subset of cells in the remaining \(q-1\) columns, also supporting depth \(q-1=p+q-2\). Joining the two branch trees below the root query gives depth \(p+q-1\). This completes the induction and the proof.

## Verification
The standalone checker `verify.py` enumerates every support of \([p]\times[q]\) for \(1\leq p,q\leq4\), and independently compares direct shattering by all distinct rectangles against the star-forest criterion. It also compares the resulting shattering polynomials to a separate labeled-component recurrence and verifies the closed two-row formula. For ten small shape parameters it computes Littlestone dimension directly from its defining recursive minimax formula. The recorded run checked 74,954 query supports and ten online-depth instances, producing the marker `CARTESIAN_RECTANGLES_PASS 74954 supports 10 online_ranks`. These finite checks are corroboration; the preceding proof establishes the unrestricted theorem.

## Relationship to prior work
Block, Brânzei, Maji, Mehta, Mukherjee and Nguyen (Cryptology ePrint 2020/1605; ITC 2021) study combinatorial rectangles and partitions and covers of bipartite graphs by *induced*-\(P_4\)-free components. In that setting complete bipartite components, including a four-cycle, are permitted. The present shattered-support criterion forbids three-edge paths as arbitrary subgraphs and excludes four-cycles; it characterizes a different property, not an implication of their covering theorems. The paper's established definitions and graph-theoretic context are used, but its partition-number bounds are not claimed here.

General VC and Littlestone counting principles give basic upper bounds but not, by themselves, this support-by-support graph characterization or its two-parameter exponential enumerator. The online rank proof is a separate exact argument. The available literature comparisons did not disclose this combined full statement. No claim is made to settle historical priority across all possible terminology.

## Limitations
The theorem assumes every Cartesian factor subset is available, including empty factors; fixed-cardinality factors or restrictions to a prescribed host bipartite graph require different arguments. It is specifically two-dimensional; no claim is made about arbitrary products of three or more factors. The finite verifier does not constitute an infinite proof. Exhaustive bibliographic coverage is not claimed, and an earlier equivalent presentation under the terminology of Boolean rank-one incidence families remains possible.

## References
- A. R. Block, S. Brânzei, H. K. Maji, H. Mehta, T. Mukherjee and H. H. Nguyen, *P4-free Partition and Cover Numbers and Application*, Cryptology ePrint Archive, Paper 2020/1605 (first public version received 2020-12-27), https://eprint.iacr.org/2020/1605.
- A. R. Block, S. Brânzei, H. K. Maji, H. Mehta, T. Mukherjee and H. H. Nguyen, *P4-free Partition and Cover Numbers & Applications*, ITC 2021, LIPIcs 199, article 16, https://doi.org/10.4230/LIPIcs.ITC.2021.16.
