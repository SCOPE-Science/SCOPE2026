# Exact-block queries on set partitions: shattering, facets, and online dimension

## Finding

Let \(\mathcal C_n\) consist of all set partitions \(\pi\) of \([n]\). A query is a nonempty subset \(B\subseteq[n]\), and its binary answer is one precisely when \(B\) is **an entire block** of \(\pi\). For every integer \(n\ge1\) and every family \(S\) of distinct queries, the following are equivalent:

1. \(S\) is VC-shattered by \(\mathcal C_n\).
2. Distinct members of \(S\) are disjoint, and either \(\bigcup_{B\in S} B\ne[n]\) or every \(B\in S\) has at least two elements.

All inclusion-maximal shattered families are precisely (i) pairwise-disjoint query families covering exactly \(n-1\) elements and (ii) set partitions of \([n]\) with no singleton block. In case (i), the uncovered element is unique.

Let \(\left\{\begin{smallmatrix}m\\k\end{smallmatrix}\right\}\) denote a Stirling number of the second kind, including \(\left\{\begin{smallmatrix}0\\0\end{smallmatrix}\right\}=1\), and let \(S_{\ge2}(n,k)\) count set partitions of \([n]\) into exactly \(k\) blocks, each having at least two elements (including \(S_{\ge2}(0,0)=1\)). If \(\Phi_n(z)\) enumerates **all** shattered query supports by cardinality and \(F_n(z)\) enumerates inclusion-maximal ones, then

\[
\Phi_n(z)=\sum_{k=0}^{n-1}\left[\sum_{m=k}^{n-1}\binom nm\left\{\begin{smallmatrix}m\\k\end{smallmatrix}\right\}+S_{\ge2}(n,k)\right]z^k,
\]

\[
F_n(z)=\sum_{k=0}^{n-1}\left[n\left\{\begin{smallmatrix}n-1\\k\end{smallmatrix}\right\}+S_{\ge2}(n,k)\right]z^k.
\]

The associated exponential generating functions, extending the convention to \(n=0\) by \(\Phi_0(z)=F_0(z)=1\), are

\[
\sum_{n\ge0}\Phi_n(z)\frac{x^n}{n!}=(e^x-1)e^{z(e^x-1)}+e^{z(e^x-1-x)},
\]

\[
\sum_{n\ge0}F_n(z)\frac{x^n}{n!}=xe^{z(e^x-1)}+e^{z(e^x-1-x)}.
\]

The exact static and online dimensions are

\[
\operatorname{VCdim}(\mathcal C_n)=\operatorname{Ldim}(\mathcal C_n)=n-1\qquad(n\ge1).
\]

## Assumptions and scope

The blocks of a set partition are nonempty, disjoint, and cover every element of \([n]\); their number and sizes are unrestricted. A positive answer requires exact equality \(B=C\) with some block \(C\), not merely containment in a block, intersection with one, or equality of the clusters of two points. The query domain consists of all \(2^n-1\) nonempty subsets. The empty query support is shattered vacuously. Littlestone dimension uses adaptive complete binary mistake trees over these same queries.

## Proof

**Shattering, necessity.** To realize the labeling in which every member of \(S\) is positive, all queried subsets must occur simultaneously as distinct blocks. Therefore they must be pairwise disjoint. If they cover \([n]\) and one of them is a singleton, label every other member positive and that singleton negative. The positive blocks cover all other elements, leaving the singleton's element necessarily as its own block; it must also be positive, a contradiction.

**Shattering, sufficiency.** Assume the stated condition. Fix any desired positive subfamily \(T\subseteq S\). Make the members of \(T\) blocks. Break each \(B\in S\setminus T\) with \(|B|\ge2\) into singleton blocks. If the support contains one or more singleton queries and an element \(u\notin\bigcup S\) exists, form one additional block consisting of \(u\) and all vertices from singleton queries in \(S\setminus T\). When none of those singleton queries is negative, leave \(u\) alone. Make every remaining vertex a singleton. All positive queries are unchanged as entire blocks; each negative query of size at least two is split; each negative singleton is merged with \(u\). If no query is a singleton, no auxiliary block is necessary. Every \(0/1\)-labeling is therefore realized by some partition.

**Facets.** Suppose a shattered family leaves at least two vertices unused. Adding one of these vertices as a new singleton query preserves disjointness and leaves another unused vertex, so it is not maximal. If a shattered family leaves exactly one vertex unused, the only nonoverlapping query that could be adjoined is that singleton, which would make the enlarged family cover all vertices and contain a singleton; it is not shattered. If the family covers all vertices, the criterion forces every block size to be at least two, and no nonoverlapping nonempty query remains. These are exactly the asserted facets.

**Enumeration.** A disjoint queried family of \(k\) blocks covering exactly \(m<n\) vertices is obtained by choosing those \(m\) vertices and partitioning them into \(k\) nonempty unordered blocks: \(\binom nm\left\{\begin{smallmatrix}m\\k\end{smallmatrix}\right\}\) possibilities. A fully covering shattered family must have all block sizes at least two, contributing \(S_{\ge2}(n,k)\). For maximal families, choose the unique unused vertex in \(n\) ways and partition its \(n-1\) neighbors, or use a no-singleton partition of all vertices. Standard exponential formulas for labeled set partitions supply the two generating functions; the factor \(e^x-1\) encodes a nonempty unqueried vertex set, and \(e^x-1-x\) encodes blocks of size at least two.

**Static dimension.** The \(n-1\) singleton queries on any \(n-1\) elements are shattered by the unused vertex, so \(\operatorname{VCdim}\ge n-1\). No shattered family can have \(n\) queries: a support with an unused vertex has at most \(n-1\) pairwise-disjoint nonempty members; a fully covering support has only blocks of size at least two and hence at most \(\lfloor n/2\rfloor\) members. For \(n=1\), the concept class is a singleton and both dimensions are zero.

**Online dimension.** Let \(d_n=\operatorname{Ldim}(\mathcal C_n)\), with \(d_0=d_1=0\). At the root of any nontrivial mistake tree, let \(B\ne\varnothing\) be the query. On the positive branch the block \(B\) is fixed, and the remaining partition can vary freely over \([n]\setminus B\). Every other query is then either a constant or an exact-block query on the remaining vertices. Thus the positive-branch Littlestone dimension is exactly \(d_{n-|B|}\). A complete depth-\(d\) tree requires both root branches to have depth at least \(d-1\), giving \(d_n\le1+\max_{1\le b\le n}d_{n-b}\). Induction gives \(d_n\le n-1\) for \(n\ge2\), including the singleton residual cases. The general inequality \(\operatorname{VCdim}\le\operatorname{Ldim}\), together with the lower bound above, forces \(d_n=n-1\).

## Verification

Run `python3 verify.py` using Python's standard library. The script constructs all set partitions independently via restricted-growth recursion, enumerates every query support through \(n=4\), and enumerates supports through cardinality four for \(n=5\). It tests every binary trace against the theorem, checks face and facet counts for the complete small cases, and computes exact online dimensions through \(n=4\) via version-space recursion. The recorded run examined 69,363 supports and printed `PARTITION_EXACT_BLOCK_PASS`.

For example, the respective face coefficient vectors for \(n=3,4,5\) are \((1,7,3)\), \((1,15,21,4)\), and \((1,31,85,40,5)\). The experiments are not a proof for unbounded \(n\); the preceding constructive and inductive arguments provide that proof.

## Relationship to prior work

DePavia, Medrano Martín del Campo, and Tani (first public 2023-05-22, arXiv:2305.13402) study learning finite set partitions mainly through **pairwise same-cluster** queries and develop general worst-case binary-oracle bounds. Their Section 4.4 also discusses other subset oracles, including existential containment questions. Such an answer is not equivalent to testing whether the queried set is exactly one block. Their results do not state the shattered-support criterion, maximal-face formula, or exact online dimension for the exact-block query class. Standard Stirling and associated Stirling enumerations count partitions once the shattering criterion is supplied; those counting identities themselves are classical.

## Limitations

These formulas depend on unrestricted set partitions and exact-block membership questions. They do not apply as stated to fixed-number-of-blocks, size-constrained or noncrossing partitions, or to pairwise same-cluster oracles. They give VC and Littlestone dimensions, not the number of oracle queries needed for exact identification, robustness to errors, or a computationally optimal learning algorithm. Historical priority under alternative terminology remains possible; the available literature and database comparisons are not an exhaustive proof of novelty.

## References

1. A. F. DePavia, O. Medrano Martín del Campo, and E. Tani, *Error-Tolerant Exact Query Learning of Finite Set Partitions with Same-Cluster Oracle*, arXiv:2305.13402, first public 2023-05-22. https://arxiv.org/abs/2305.13402.
2. Classical Stirling-number and exponential-formula identities are used only as enumerative tools, not claimed as new results.
