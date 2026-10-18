# Badawi annihilator graphs determine finite reduced nonfield rings

## Finding

Let
\[
R=\prod_{i=1}^{r}\mathbb F_{q_i},\qquad r\ge2,
\]
be a finite reduced commutative nonfield, and let \(G=AG(R)\) be Badawi's annihilator graph on the nonzero zero-divisors. For a vertex \(x\), write \(S(x)=\{i:x_i\ne0\}\). For every nonempty proper \(S\subset[r]\), define
\[
C_S=\{x:S(x)=S\},\qquad w_S=|C_S|=\prod_{i\in S}(q_i-1).
\]
Then the sets \(C_S\) are exactly the false-twin classes of \(G\), and the false-twin quotient is the incomparability graph \(H_r\) of the nonempty proper subsets of \([r]\).

It follows that the full annihilator graph is a complete invariant of the ring inside this class:
\[
AG(R)\cong AG(R')\quad\Longleftrightarrow\quad R\cong R'
\]
for finite reduced commutative nonfields \(R,R'\).

For \(r\ge3\), put \(a_i=q_i-1\). Then
\[
\operatorname{Aut}(G)\cong
\left(\prod_{\varnothing\ne S\subsetneq[r]}\mathfrak S_{w_S}\right)\rtimes B,
\]
where \(B\) is the subgroup of \(\operatorname{Aut}(H_r)\) preserving the cell sizes. Explicitly, \(B\) contains exactly the coordinate permutations \(\pi\in S_r\) satisfying \(a_{\pi(i)}=a_i\) for all \(i\), and it contains the support-complementing coset only when \(q_1=\cdots=q_r=2\). For \(r=2\), one has \(G=K_{q_1-1,q_2-1}\); its quotient symmetry is trivial if \(q_1\ne q_2\) and is \(C_2\) if \(q_1=q_2\).

## Assumptions and scope

The theorem concerns Badawi's annihilator graph, whose vertices are nonzero zero-divisors and where distinct vertices \(x,y\) are adjacent when \(\operatorname{ann}(xy)\ne\operatorname{ann}(x)\cup\operatorname{ann}(y)\). The ring is assumed finite, commutative, reduced, and not a field; equivalently it is a product of at least two finite fields. Finite fields of a given order are unique up to isomorphism, so recovering the unordered list of field orders recovers the ring.

A false-twin class means a maximal set of distinct vertices having the same open neighborhood. The quotient used below collapses each such class to one vertex.

## Proof

For \(x\in R\), the annihilator is the coordinate ideal supported on \(S(x)^c\). Hence, if \(S=S(x)\) and \(T=S(y)\), then
\[
\operatorname{ann}(xy)=I_{(S\cap T)^c}=I_{S^c\cup T^c}=\operatorname{ann}(x)+\operatorname{ann}(y).
\]
For two ideals, their set-theoretic union equals their sum exactly when one contains the other. Thus
\[
x\sim y\quad\Longleftrightarrow\quad S(x)\text{ and }S(y)\text{ are incomparable under inclusion}.
\]
All vertices in one support cell therefore have the same open neighborhood.

These are the only false twins. Suppose \(S\ne T\). If \(S,T\) are incomparable, then a vertex from \(C_T\) is adjacent to every vertex of \(C_S\), while no vertex is adjacent to itself or to another vertex with the same support \(T\); hence the neighborhoods differ. If \(S\subsetneq T\), choose \(a\in T\setminus S\). The singleton support \(\{a\}\) is incomparable with the nonempty set \(S\), but is contained in \(T\), so it distinguishes the two neighborhoods. The case \(T\subsetneq S\) is symmetric. Therefore the false-twin quotient is precisely \(H_r\).

Assume now \(r\ge3\). A quotient vertex of support size \(k\) has degree
\[
d_k=2^r+1-2^k-2^{r-k}.
\]
The minimum degree occurs exactly at \(k=1\) and \(k=r-1\). The induced subgraph on these \(2r\) minimum-degree vertices consists of two \(r\)-cliques, one on the singleton supports and one on the co-singletons, together with the matching \(\{\{i\},[r]\setminus\{i\}\}\). Its automorphism group is \(S_r\times C_2\): the first factor permutes coordinates and the second exchanges the two cliques by complementation. Every other support \(S\) is determined by which singleton vertices are comparable with it, so an automorphism of the minimum-degree subgraph extends to at most one automorphism of \(H_r\). Coordinate permutations and complementation do extend, hence
\[
\operatorname{Aut}(H_r)\cong S_r\times C_2.
\]

Because false-twin classes are canonical, every automorphism of \(G\) first permutes vertices arbitrarily inside each \(C_S\), and its induced quotient automorphism must preserve the sizes \(w_S\). Conversely every size-preserving quotient automorphism lifts after arbitrary internal permutations. This gives the semidirect product above.

For a coordinate permutation, size preservation on singleton cells is exactly \(a_{\pi(i)}=a_i\). For a complement-type quotient automorphism, let \(A=\prod_i a_i\). Size preservation of singleton cells would require
\[
a_i=\frac{A}{a_{\pi(i)}}
\]
for every \(i\). Multiplying over \(i\) gives \(A^2=A^r\). Since \(r\ge3\) and \(A\) is a positive integer, this forces \(A=1\), hence every \(a_i=1\), equivalently every field is \(\mathbb F_2\). Thus complementation survives exactly in the Boolean case.

Finally consider an isomorphism \(AG(R)\cong AG(R')\). The number of false-twin classes is \(2^r-2\), so the numbers of field factors agree. If \(r=2\), the graph is \(K_{q_1-1,q_2-1}\), which recovers the unordered pair \(\{q_1,q_2\}\). If \(r\ge3\), the quotient isomorphism is either coordinate type or complement type. In the coordinate case, singleton-cell sizes recover the unordered list \(\{q_i-1\}\). In the complement case, write \(b_j=q'_j-1\), \(A=\prod_i a_i\), and \(B=\prod_j b_j\). Matching a singleton cell to a complementary cell and a co-singleton cell to the corresponding singleton gives
\[
a_i=\frac{B}{b_{\pi(i)}},\qquad \frac{A}{a_i}=b_{\pi(i)}.
\]
Hence \(A=B=a_i b_{\pi(i)}\) for all \(i\), and multiplying again gives \(A^2=A^r\). Thus \(A=1\), so both rings are products of \(r\) copies of \(\mathbb F_2\). In every case the unordered field-order lists agree, proving \(R\cong R'\).

## Verification

The proof is symbolic and covers the boundary \(r=2\) separately. The included standard-library checker constructs the quotient incomparability graphs and expanded annihilator graphs, verifies the exact false-twin partition, exhaustively counts quotient automorphisms for \(r=2,3,4\), exhaustively counts full graph automorphisms for several small products, checks the semidirect-product order formula, and tests graph-isomorphism reconstruction on a bounded collection of small parameter tuples. These finite checks are consistency tests, not substitutes for the general proof.

## Relationship to prior work

Badawi introduced the annihilator graph and established its foundational structural properties. Visweswaran and Sarman studied the complement for reduced rings; in the finite-product-of-fields case their full text develops annihilator-equivalence classes and exact clique/chromatic information. A later inclusion-graph paper identifies, for reduced rings, the inclusion graph of annihilators with the complement of Badawi's graph. Those results supply closely related support and comparability structure but do not state the automorphism decomposition or the if-and-only-if ring-reconstruction theorem above.

A public published-finding corpus finding gives the weighted support-incomparability model for finite semisimple annihilator graphs and exact distance enumerators. That statement is a direct structural input but does not imply the present symmetry or reconstruction classification. A 2026 paper on a weak zero-divisor difference graph advertises reconstruction of finite reduced rings for its different graph; no reduction showing that graph is determined by Badawi's annihilator graph was available in the inspected material.

## Limitations

The result does not cover finite rings with nilpotents, infinite reduced rings, or fields. The reconstruction statement is only for the full labeled-size blow-up graph, not for the unweighted quotient \(H_r\), which remembers only the number of factors. The complete text of the 2026 weak zero-divisor difference-graph paper was not accessible in the inspection path, so it remains a bibliographic residual risk; its accessible abstract concerns a different graph and does not supply the implication needed to cover this theorem. An equivalent theorem could also exist in unindexed literature under another name for the same incomparability blow-up.

## References

1. A. Badawi, “On the Annihilator Graph of a Commutative Ring,” *Communications in Algebra* 42 (2014), DOI 10.1080/00927872.2012.707262.
2. S. Visweswaran and S. Sarman, “Some properties of the complement of the annihilator graph of a commutative reduced ring,” *Palestine Journal of Mathematics* 6(2) (2017), 455–462.
3. M. Safari, F. Shaveisi, and R. Nikandish, “Inclusion graph of annihilators in a commutative ring,” arXiv:2606.15498 (2026).
4. A. Wani, “The Weak Zero-Divisor Difference Graph of a Finite Commutative Ring,” arXiv:2607.17677 (2026).
5. Public published-finding corpus record `24d777b2eb6c`, “Exact distance enumerator for annihilator graphs of finite semisimple rings.”
