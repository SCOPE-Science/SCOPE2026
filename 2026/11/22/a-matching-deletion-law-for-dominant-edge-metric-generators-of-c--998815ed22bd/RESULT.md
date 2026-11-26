# A matching-deletion law for dominant edge-metric generators of complete bipartite graphs

Let \(G=K_{m,n}-\{a_ib_i:1\le i\le t\}\), where \(m,n\ge3\), \(0\le t\le\min(m,n)\), and the deleted edges are a matching. Put \(N=m+n\), \(u=m-t\), \(v=n-t\). A dominant edge-metric generator is a vertex cover \(S\) whose distances \(d(w,xy)=\min(d(w,x),d(w,y))\), \(w\in S\), distinguish all present edges. Counts refer to subsets of the labeled graph.

The polynomial by omitted cardinality is
\[
H(z)=(1+z)^t(2+(u+v)z)-1+tz^2.
\]
The polynomial by selected cardinality is \(z^NH(1/z)\). The polynomial for inclusion-minimal generators by selected cardinality is
\[
M(z)=(u+v)z^{N-t-1}+tz^{N-2}+(\mathbf 1_{u=0}+\mathbf 1_{v=0})z^{N-t}.
\]
In particular, the minimum cardinality is \(N-t-1\) if \(u+v>0\) and \(t\) in the balanced crown case \(u=v=0\). The respective minimum multiplicities by case are \(N\) for \(t=0\), \(N-1\) for \(t=1\), \(N-2t\) for \(t\ge2\) and \(u+v>0\), and 2 for the balanced crown.

There are three distinct inclusion-minimal cardinalities exactly when one shore is saturated by the deleted matching and the other is not. Then \(t\ge3\), and the sizes are \(N-t-1,N-t,N-2\). For instance, \((m,n,t)=(3,4,3)\) gives \(M(z)=z^3+z^4+3z^5\). There are two distinct cardinalities when \(t\ge2\) leaves unmatched vertices on both shores, or in the balanced crown case. There is one cardinality when \(t=0\) or \(t=1\). Where more than one size occurs, the overall gap is \(t-1\) in the cases with \(u+v>0\), and \(t-2\) in the balanced crown.

## Proof

The omitted set \(U\) must be independent. It therefore lies in one shore (possibly empty) or is a single deleted pair: if it contains vertices on both shores, each cross-pair must be among the deleted edges, so neither shore can supply a second vertex. Two vertices on the same shore always have distance two, since at most two possible common neighbors are lost. A deleted pair has distance three: besides the other endpoint, choose a neighbor of each endpoint from the opposite shore with distinct indices, which is possible with both shores of size at least three. All present cross-pairs have distance one.

Suppose \(U\subseteq B\). Two omitted unmatched vertices \(b_j,b_k\) give the present edges \(a_i b_j,a_i b_k\) for any fixed \(i\), with identical distances from all selected vertices: on \(A\) both give zero at \(a_i\) and one elsewhere, and on selected \(b_h\) both give \(\min(d(b_h,a_i),2)\). Conversely if there is at most one unmatched omission, two present edges with different \(A\)-endpoints are distinguished by one of those endpoints. For distinct edges in row \(i\), a selected \(B\)-endpoint distinguishes them if available. Otherwise one omitted endpoint, say \(b_j\), is matched. Since \(j\ne i\), the selected \(a_j\) gives distance two to \(a_i b_j\) and one to \(a_i b_k\). The argument for \(U\subseteq A\) is symmetric. For a mixed deleted pair \(\{a_i,b_i\}\), selected-endpoint intersections distinguish all edges: a singleton intersection determines the unselected endpoint as the unique omitted vertex on the opposite shore, and a two-element intersection specifies the edge itself.

For one-shore omissions choose any of the matched vertices and at most one unmatched vertex. The two resulting terms double-count the empty omission; subtract it and add the \(t\) mixed pairs to obtain \(H\). Inclusion-minimal selected sets are complements of inclusion-maximal omissions. Every mixed pair is maximal. A maximal omission confined to one shore includes all its matched vertices and one unmatched vertex if available, or the whole shore if no unmatched vertex exists. These omissions are indeed globally maximal: they contain at least two vertices if \(t>0\) under the stated shore-size assumptions; if \(t=0\) no mixed pair is available. This proves \(M\), and inspecting the exponents and leading coefficient of \(H\) gives the claimed minima. In \(M\), \(N-t-1=N-2\) for \(t=1\); a saturated shore requires \(t\ge3\), for which all three displayed exponents are distinct. This gives the cardinality classification.

## Verification and scope

Exact BFS-based edge-distance enumeration across all 199 graphs with \(3\le m,n\le8\) and all admissible \(t\) matched the admissible and maximal omission sets mask by mask (14,171 admissible and 1,850 maximal sets). The general statement follows from the proof, not this bound. Neither smaller shores nor nonmatching deletion patterns are included.

## Prior work

Tavakoli, Korivand, Erfanian, Abrishami and Baskoro, *The dominant edge metric dimension of graphs* (2023), DOI [10.5614/ejgta.2023.11.1.16](https://doi.org/10.5614/ejgta.2023.11.1.16), give the known complete-bipartite scalar \(N-1\) at \(t=0\). Ordinary edge-metric resolution (Kelenc–Tratnik–Yero, [arXiv:1602.00291](https://arxiv.org/abs/1602.00291)) does not require a cover; vertex-edge dominating resolution (Ikhlaq–Hayat–Siddiqui, [arXiv:2211.09327](https://arxiv.org/abs/2211.09327)) has a weaker domination condition. The prior matching-deleted vertex-resolving polynomials and the prior ordinary crown edge-metric bases address different classes of subsets. These comparisons do not certify historical priority.
