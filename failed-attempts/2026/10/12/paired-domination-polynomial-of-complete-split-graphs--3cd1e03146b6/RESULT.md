# Paired-domination polynomial of complete split graphs
## Finding
For integers \(r,n\ge 1\), let \(S_{r,n}=K_r\vee \overline{K_n}\) be the complete split graph with clique part \(C\) of size \(r\) and independent part \(I\) of size \(n\). For \(X\subseteq V(S_{r,n})\), put \(a=|X\cap C|\) and \(b=|X\cap I|\). Then \(X\) is paired-dominating if and only if
\[
a\ge 1,\qquad b\le a,\qquad a+b\equiv 0\pmod 2.
\]
Equivalently, the bivariate enumerator by clique and independent occupancy is
\[
F_{r,n}(u,v)=\sum_{a=1}^{r}\binom{r}{a}u^a
\sum_{\substack{0\le b\le \min(a,n)\\ b\equiv a\, (\mathrm{mod}\,2)}}\binom{n}{b}v^b,
\]
and the paired-domination polynomial is
\[
D_{\mathrm{pr}}(S_{r,n};x)=F_{r,n}(x,x).
\]
Consequently,
\[
\gamma_{\mathrm{pr}}(S_{r,n})=2,
\qquad
 d_{\mathrm{pr}}(S_{r,n},2)=\binom{r}{2}+rn,
\]
and every inclusion-minimal paired-dominating set has size \(2\). Thus the upper paired-domination number also satisfies \(\Gamma_{\mathrm{pr}}(S_{r,n})=2\).

## Assumptions and scope
Graphs are finite, simple, and undirected. A paired-dominating set is a dominating set whose induced subgraph contains a perfect matching. The theorem covers every complete split graph in the join form \(K_r\vee\overline{K_n}\) with both parts nonempty. The bivariate variable \(u\) records selected clique vertices and \(v\) records selected independent vertices.

## Proof
Let \(X\subseteq V(S_{r,n})\), and write \(a=|X\cap C|\), \(b=|X\cap I|\).

If \(a=0\), then domination forces \(X=I\): any unselected independent vertex has no neighbor in \(I\). But \(S_{r,n}[I]\) is edgeless, so a nonempty \(X=I\) has no perfect matching. Hence a paired-dominating set must satisfy \(a\ge 1\).

Assume now that \(a\ge1\). A selected clique vertex is adjacent to every other vertex of \(S_{r,n}\), so \(X\) is automatically dominating. The induced graph on \(X\) is
\[
S_{r,n}[X]\cong K_a\vee\overline{K_b}.
\]
In every perfect matching of this graph, each selected independent vertex must be matched to a distinct selected clique vertex. Therefore \(b\le a\) is necessary. A perfect matching also requires \(a+b\) to be even.

Conversely, suppose \(b\le a\) and \(a+b\) is even. Match the \(b\) selected independent vertices injectively to \(b\) distinct selected clique vertices. The remaining \(a-b\) clique vertices form a clique, and
\[
a-b\equiv a+b\equiv0\pmod 2,
\]
so they can be paired among themselves. Thus \(S_{r,n}[X]\) has a perfect matching. This proves the stated criterion.

For fixed \(a,b\), there are \(\binom{r}{a}\binom{n}{b}\) choices, yielding the bivariate enumerator and, after substituting \(u=v=x\), the ordinary paired-domination polynomial.

The minimum possible cardinality is \(2\). Every edge of a complete split graph is itself a paired-dominating set: every edge has a clique endpoint, and that endpoint dominates the whole graph. The number of such edges is
\[
\binom{r}{2}+rn.
\]
Finally, any paired-dominating set \(X\) contains an edge from a perfect matching of \(S_{r,n}[X]\); that edge alone is already paired-dominating. Hence no paired-dominating set of size greater than \(2\) is inclusion-minimal. Therefore all minimal paired-dominating sets are exactly the edges and \(\Gamma_{\mathrm{pr}}(S_{r,n})=2\).

## Verification
The standalone checker `verify.py` constructs \(S_{r,n}\) directly and exhausts all subsets for every \(1\le r,n\le7\). It checks the paired-domination predicate using an independent recursive perfect-matching test, compares it with the criterion above, compares every coefficient with the formula, checks the minimum count, and verifies that every larger paired-dominating set contains a paired-dominating two-set. Its packaged replay result is:

`VERIFY_OK r_range=1..7 n_range=1..7 subset_checks=64516 criterion_checks=64516 coefficient_checks=162 paired_set_minimality_checks=22507 max_order=14`

This finite computation is a stress test only; the proof above establishes the theorem for all \(r,n\ge1\).

## Relationship to prior work
Haynes and Slater introduced paired domination in 1998. Chen, Lu, and Zeng later proved that the paired-domination problem is NP-complete even on split graphs, making exact tractable subclasses structurally relevant. Puttaswamy, Alwardi, and Nayaka introduced the paired-domination polynomial and reported computations for some standard graph families. The publicly retrievable abstract does not identify complete split graphs among those families, and targeted searches under the join, split, threshold, and complete-split aliases did not locate the criterion or polynomial above.

The closest indexed semantic results found for all-set paired-domination polynomials concern complete multipartite graphs and chain graphs. Neither covers \(K_r\vee\overline{K_n}\) in general: for \(r\ge2\) and \(n\ge2\), a complete split graph contains both a clique edge and a nonedge inside the independent part, so it is not complete multipartite; and it is not a chain graph unless restricted to special small cases. A separate result on all \(k\)-tuple total dominating sets of threshold graphs concerns open-neighborhood multiplicity, not perfect matchings, and does not imply the paired-domination criterion.

## Limitations
The theorem is restricted to complete split graphs, not arbitrary split graphs. The 2016 paired-domination-polynomial proceedings item is publicly available only as an abstract/one-page proceedings record in the sources inspected here; because it says that several standard families were computed without naming all of them, unindexed overlap with a fuller version remains a residual originality risk. The searches and source comparisons support noncoverage of the inspected material but do not constitute a proof of global novelty.

## References
- T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
- L. Chen, C. Lu, and Z. Zeng, “Labelling algorithms for paired-domination problems in block and interval graphs,” *Journal of Combinatorial Optimization* 19 (2010), 457–470. DOI: 10.1007/s10878-008-9177-6.
- P. Puttaswamy, A. Alwardi, and S. R. Nayaka, “Introduction to Paired Domination Polynomial of a Graph,” ICMAGT 2016 proceedings record, conference dates September 26–27, 2016.
- W. Ulatowski, “All graphs with paired-domination number two less than their order,” *Opuscula Mathematica* 33 (2013), 763–783. DOI: 10.7494/OpMath.2013.33.4.763.
