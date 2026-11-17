# Component-size shattering of cardinality-constrained graph cuts

## Finding

Let \(n\ge2\), \(1\le k\le n-1\), and \(r=\min\{k,n-k\}\). On the edge set \(E(K_n)\), let \(\mathcal C_{n,k}\) be the Boolean concept family \(\{\delta(A): A\subseteq[n],\ |A|=k\}\), where an edge has positive label if and only if its endpoints lie on opposite sides of the cut. For each query support \(S\subseteq E(K_n)\), write \(H_S=([n],S)\).

**Exact all-support criterion.** The support \(S\) is shattered if and only if \(H_S\) is a forest and the following component-size test succeeds. Let its nontrivial components (orders at least two) have orders \(t_1,\ldots,t_c\), and let \(m=n-\sum_{i=1}^c t_i\) be its number of isolated vertices. For every choice \(a_i\in\{0,\ldots,\lfloor t_i/2\rfloor\}\), there must exist \(\varepsilon_i\in\{0,1\}\) and \(h\in\{0,\ldots,m\}\) satisfying
\[
 k=h+\sum_{i=1}^c\bigl(\varepsilon_i a_i+(1-\varepsilon_i)(t_i-a_i)\bigr).
\]
When \(c=0\), the test is interpreted as \(0\le k\le m=n\). In particular, for forests the shattering decision depends **only on the multiset of component orders**, not on the component tree shapes.

**Full face polynomial.** Define \(\tau_1=1\), \(\tau_j=j^{j-2}\) for integers \(j\ge2\). For a partition \(\lambda\vdash n\), write \(m_j(\lambda)\) for the multiplicity of part \(j\), \(\ell(\lambda)\) for its length, and \(G_k(\lambda)\in\{0,1\}\) for the component-size test above (including singleton parts). Then the entire shattered-support polynomial is exactly
\[
 \Phi_{n,k}(z)=\sum_{\lambda\vdash n}G_k(\lambda)
 \frac{n!\prod_{j\ge1}\tau_j^{m_j(\lambda)}}{\prod_{j\ge1}(j!)^{m_j(\lambda)}m_j(\lambda)!}
 z^{\,n-\ell(\lambda)}.
\]
This is a finite integer-partition computation for all \(n,k\), including any intermediate parameter values for which no simpler VC-dimension formula is asserted.

**Dimension bounds and exact stable range.** Every shattered support has at most \(2r\) edges. If \(n\ge3r+1\), this bound is attained by a star with \(2r\) edges and therefore
\[
 \operatorname{VCdim}(\mathcal C_{n,k})=2r\qquad(n\ge3r+1).
\]
More generally, every forest having \(s\) edges is shattered whenever \(s\le r\) and \(n\ge2s+1\). These are sufficient conditions, not a claim that other supports cannot be shattered. For example, for \(n=9,k=4\), the component test admits some five-edge forests, although \(r=4\).

## Assumptions and scope

All graphs are finite, simple and labeled. The ambient query domain is the full edge set of the complete graph, not the vertices and not a graph-neighborhood system. Both shores of a cut are nonempty because \(1\le k<n\). Distinct shores may yield identical cut vectors when \(n=2k\); this has no effect on shattering. The graph \(H_S\) retains all \(n\) ambient vertices, including isolates. The parameter \(k\) is the cardinality of one shore, not the number of edges cut. The empty support is always shattered.

## Proof

**1. Cycles are forbidden.** Encode a shore \(A\) by bits \(x_v=\mathbf1\{v\in A\}\). On an edge \(uv\), its cut label is \(x_u\oplus x_v\). The XOR of cut labels around every cycle is zero. A support containing a cycle cannot realize a labeling of that cycle with odd XOR and hence cannot be shattered.

**2. The exact forest test.** Let \(H_S\) be a forest. On any nontrivial tree component, a prescribed assignment of edge labels uniquely determines the vertex bits once one root bit is fixed. Its only two solutions are complementary, with numbers of ones \(a_i\) and \(t_i-a_i\). Each isolated vertex is free, contributing either zero or one. Therefore a prescribed edge labeling extends to a shore of size exactly \(k\) if and only if an integer \(h\in[0,m]\) and a choice of one of these two sizes for every nontrivial component sum to \(k\). Conversely, every integer \(a_i\) from zero to \(t_i\) occurs as the number of ones in some vertex-bit assignment on that tree, and this assignment induces an edge labeling. Replacing \(a_i\) by \(t_i-a_i\) does not alter the two available counts. Thus testing \(0\le a_i\le\lfloor t_i/2\rfloor\) for every component is both necessary and sufficient for shattering. This also proves tree-shape independence.

**3. Counting all supports.** By Cayley's labeled-tree formula, a prescribed vertex block of order \(j\) admits exactly \(\tau_j\) trees. A set partition of \([n]\) into blocks of sizes \(\lambda\) has \(n!/\prod_j(j!)^{m_j}m_j!\) realizations. The disjoint union of its chosen trees is a unique labeled forest and has \(n-\ell(\lambda)\) edges. Step 2 shows all forests with those component sizes are either all shattered or all unshattered according to \(G_k(\lambda)\). Summing their counts gives the polynomial, without overcounting.

**4. Upper bound.** In a tree of order \(t_i\), choose a bit assignment having \(\lfloor t_i/2\rfloor\) ones and prescribe its induced edge labels. Under any completion the component then has at least \(\lfloor t_i/2\rfloor\) ones. Thus a shattered forest must satisfy \(k\ge\sum_i\lfloor t_i/2\rfloor\). Since \(\lfloor t_i/2\rfloor\ge(t_i-1)/2\), we obtain \(k\ge|S|/2\). Complementing all vertex bits leaves every edge label unchanged and replaces the cardinality \(k\) by \(n-k\), so also \(n-k\ge |S|/2\). Consequently \(|S|\le2r\).

**5. Attainment for \(n\ge3r+1\).** By shore complementation it suffices to treat \(k=r\). Put a star with \(2r\) edges on \(2r+1\) vertices; there are at least \(r\) unused vertices. Given any labeling of its edges, let \(t\) be the number of positive edges. If \(t\le r\), put the center outside the shore and the \(t\) positive-edge leaves inside it. If \(t\ge r+1\), put the center inside and the \(2r-t\) negative-edge leaves inside, for a total of \(1+2r-t\le r\) selected vertices. Fill the shore to size \(r\) using unused vertices. All desired edge labels are realized and the star is shattered. Step 4 supplies the matching upper bound.

**6. Uniform small-forest guarantee.** Suppose a forest has \(s\ge1\) edges, nontrivial component orders \(t_i\), \(c\ge1\) such components, and \(m=n-s-c\) isolates. For any edge labeling define \(b_i=\min\{a_i,t_i-a_i\}\), \(d_i=t_i-2b_i\ge0\), and \(L=\sum_i b_i\). The attainable shore sizes are precisely \(L+\sum_{i\in I}d_i+h\), for \(I\subseteq[c]\) and \(0\le h\le m\). Because each nontrivial tree has \(t_i-1\) edges, \(L\le\sum_i(t_i-1)=s\). If \(d_{\max}=\max_i d_i\), consecutive *distinct* subset sums of the \(d_i\) differ by at most \(d_{\max}\): given any nonzero subset sum, remove one positive summand to obtain a smaller subset sum at distance at most \(d_{\max}\). Furthermore \(t_i-1\le s-(c-1)\), so \(d_{\max}\le\max t_i\le s-c+2\). From \(n\ge2s+1\) follows \(m=n-s-c\ge s+1-c\ge d_{\max}-1\). Hence the intervals contributed by the \(m\) isolates bridge every gap in the subset sums. Every integer from \(L\) to \(n-L\) is attainable. If \(s\le k,n-k\), this includes \(k\). The case \(s=0\) is immediate.

## Verification

The standalone Python 3 program `verify.py` compares the component-size test directly against all cut trace vectors, independently enumerated by choosing shores of cardinality \(k\). It exhaustively checks every subset of \(E(K_n)\) for \(2\le n\le6\) and all \(1\le k<n\). It separately computes polynomial coefficients from integer partitions and Cayley's tree counts and checks them against the independently enumerated shattered supports. It performs 168146 support-cardinality comparisons. The exhaustive range is finite; no extrapolation from it is used in Steps 1–6.

Reproduce with `python3 verify.py` (standard library only).

## Relationship to prior work

Classical unrestricted cuts yield edge XOR labelings and hence a familiar forest obstruction; this elementary observation is not claimed as new. An earlier exact enumeration for the special case of shores of cardinality two is also not claimed as new. The contribution here is the uniform **all-cardinalities** component-size equivalence, integer-partition face enumerator, and sharp \(2\min\{k,n-k\}\) capacity in the stated infinite stable region, with a uniform small-forest shattering guarantee.

Lee, Li, Santha and Zhang (2020/2021) study linear spans of **minimum cut** incidence vectors of weighted graphs, not VC shattering of all cardinality-constrained cuts. Coudert, Csikós, Ducoffe and Viennot (2024) study VC dimension of **vertex-neighborhood** systems of graphs, rather than cut incidence on edges. These are neighboring motivations but do not imply the present criterion. No general historical-priority guarantee is claimed.

## Limitations

The partition formula is finite and exact but can be computationally expensive for large \(n\); it is not an efficient polynomial-time algorithm. The explicit dimension equality is stated only under \(n\ge3r+1\); this condition is sufficient, and it need not be the smallest possible threshold for every \(r\). All finite verification is supplementary and does not certify originality.

## References

- T. Lee, T. Li, M. Santha, S. Zhang, *On the Cut Dimension of a Graph*, arXiv:2011.05085, first posted 2020-11-10; CCC 2021, DOI 10.4230/LIPIcs.CCC.2021.15.
- D. Coudert, M. Csikós, G. Ducoffe, L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588, first posted 2024-05-13; SEA 2024, DOI 10.4230/LIPIcs.SEA.2024.8.
- Cayley's formula for the number of labeled trees (classical counting result).
