# A positive partition formula for the sphere ranks of partition-graph clique complexes

## Finding

For every integer \(n\geq1\), let \(G_n\) have the integer partitions of \(n\) as vertices; two vertices are adjacent when a unit is transferred between distinct rows, possibly introducing a new row, and the resulting parts are reordered. Write \(K_n=\operatorname{Cl}(G_n)\). For each partition \(\lambda\vdash n\), let \(h_1>\cdots>h_s>0\) be the **distinct positive part values** of the conjugate partition \(\lambda'\), and set \(g_i=h_i-h_{i+1}\) for \(1\leq i<s\) and \(g_s=h_s\). Define the nonnegative integer

\[
 w(\lambda)=\begin{cases}0,&s\leq3,\\\binom{s-2}{2},&s\geq4\end{cases}
   +\sum_{i=2}^{s-1}\mathbf 1_{\{g_i\geq2\}},
\]

where an empty sum is zero. Then

\[
\boxed{K_n\simeq\bigvee^{b_n}S^2,\qquad b_n=\sum_{\lambda\vdash n}w(\lambda).}
\]

In particular, \(b_n\) is given by an explicit **positive partition statistic**, rather than an alternating count of cliques or an unevaluated Euler characteristic. The first nonzero value is \(b_8=1\). For \(n=26,27,28,29,30\), the formula gives respectively \(4480,5975,7927,10429,13653\).

The ordinary generating function has the following exact product–sum form in formal power series \(\mathbb Z[[q]]\). Let \(P=\prod_{a\geq1}(1-q^a)^{-1}\), \(P_{<m}=\prod_{1\leq a<m}(1-q^a)^{-1}\), \(P_{>m}=\prod_{a>m}(1-q^a)^{-1}\), \(Q=q/(1-q)\), \(R=q^2/(1-q^2)\), and \(D=\sum_{a\geq1}q^a/(1-q^a)\). Then

\[
\boxed{\sum_{n\geq1}b_nq^n=P\left(3-2Q+\frac{Q^2-R}{2}\right)-3-D+
\sum_{m\geq1}\frac{q^{2m}}{1-q^m}(P_{<m}-1)(P_{>m}-1).}
\]

Despite the displayed rational coefficients, its formal coefficients are nonnegative integers by the partition-statistic interpretation.

## Assumptions and scope

There are no asymptotic or genericity assumptions: \(n\) is an arbitrary positive integer. Integer partitions are unlabelled, weakly decreasing sequences of positive parts. The graph is the **one-cell row-transfer** partition graph, not the Hamming-word partition graph. The symbol \(\simeq\) denotes ordinary homotopy equivalence. For \(b_n=0\), the empty wedge denotes a point. The primary mathematical object is the homotopy type of the flag simplicial complex \(K_n\); no equivariant splitting is asserted.

## Proof

**1. Lexicographic filtration.** Represent each partition by its conjugate, padded with zeroes. Order vertices increasingly by lexicographic order of these conjugates. The first vertex is \((n)\), whose conjugate has \(n\) entries equal to one. Let \(L_\lambda\) be the simplicial link of a newly inserted vertex within the complex induced by all preceding vertices. A simplex introduced at this stage is exactly the cone on \(L_\lambda\), so the Euler-characteristic increment is \(1-\chi(L_\lambda)\).

**2. Lower-link graph.** Suppose the distinct entries of \(\lambda'\) are \(h_1>\cdots>h_s>0\), with multiplicities \(a_1,\ldots,a_s\); put \(d_i=a_1+\cdots+a_i\). A neighbor earlier in the order arises by decreasing the last occurrence at position \(d_i\) of value \(h_i\) and increasing the first occurrence at position \(d_j+1\) of the next lower value \(h_{j+1}\) (or zero if \(j=s\)). These two positions have the required earlier lexicographic order exactly when \(i\leq j\). If \(i=j\), adjacency of the positions requires the gap \(g_i\geq2\); if \(i<j\), the move is always allowed. Hence the earlier neighbors are indexed by the edges of the simple bipartite graph \(B_\lambda\) with vertices \(D_1,\dots,D_s\) and \(R_1,\dots,R_s\), where

\[
D_iR_j\in E(B_\lambda)\quad\Longleftrightarrow\quad
(i<j)\ \text{or}\ (i=j\ \text{and}\ g_i\geq2).
\]

Isolated vertices in this bipartite graph are discarded. Two earlier neighbors are adjacent in the partition graph exactly when their transfers share the decreased coordinate or the increased coordinate. Indeed, the difference between distinct transfer vectors \(-e_{d_i}+e_{d_j+1}\) and \(-e_{d_{i'}}+e_{d_{j'}+1}\) is a root vector only if the two donors or two recipients coincide; otherwise it has four nonzero coordinates or a coefficient of magnitude two. Thus the graph of earlier neighbors is precisely the line graph \(L(B_\lambda)\), and

\[
L_\lambda=\operatorname{Cl}(L(B_\lambda)).
\]

**3. Homotopy type of the link.** The clique complex of the line graph of a simple bipartite graph is covered by simplices indexed by its original nonisolated vertices: each cover simplex consists of edges incident to that vertex. Every clique of edges shares a vertex because the original graph has no triangles. Two such simplices intersect in one vertex precisely when their original endpoints are adjacent; threefold intersections are empty. The nerve lemma therefore gives \(L_\lambda\simeq B_\lambda\) whenever \(B_\lambda\) is nonempty. For \(s\geq2\), the edges \(D_iR_j\) with \(i<j\) span a connected component containing all \(D_1,\ldots,D_{s-1}\) and \(R_2,\ldots,R_s\); optional diagonal edges add loops or pendant vertices, so \(B_\lambda\) is connected. When \(s=1\), this graph is empty precisely for \(g_1=1\), which is \(\lambda=(n)\); otherwise it is one edge. Consequently **every noninitial lower link is nonempty, connected, and homotopy equivalent to a graph**.

**4. Cell dimension and fundamental group.** Start at the single initial vertex. Adding a new vertex attaches a cone on its connected lower link. Replacing the prior space and the link by homotopy-equivalent CW models in the corresponding homotopy pushout constructs, by induction, a CW model with cells of dimension at most two. By van Kampen, coning off a connected link cannot create a new fundamental-group generator, so every stage is simply connected. The eventual \(K_n\) is therefore simply connected and of CW homotopy dimension at most two. Its second integral homology is free abelian. Choosing spherical representatives of a basis (Hurewicz) and applying the simply connected homological Whitehead theorem gives a wedge of \(2\)-spheres of rank \(\chi(K_n)-1\). These steps independently establish the needed topological reduction rather than assuming the rank formula from prior work.

**5. The local Euler increment.** For \(s\geq2\), the nonisolated vertex count and edge count of \(B_\lambda\) are

\[
V=2(s-1)+\mathbf1_{\{g_1\geq2\}}+\mathbf1_{\{g_s\geq2\}},\qquad
E=\binom{s}{2}+\sum_{i=1}^s\mathbf1_{\{g_i\geq2\}}.
\]

Thus \(1-\chi(L_\lambda)=1-V+E=\binom{s-2}{2}+\sum_{i=2}^{s-1}\mathbf1_{\{g_i\geq2\}}\), where the binomial expression is interpreted as zero when \(s=2\) or \(3\). For \(s=1\), the increment is one at \(\lambda=(n)\), otherwise zero. Summation of the increments over all partitions yields \(\chi(K_n)=1+\sum_{\lambda\vdash n}w(\lambda)\). Combining with step 4 proves the claimed sphere count.

**6. Generating function.** Every conjugate partition is uniquely encoded by an increasing sequence of positive integers \(A_1<\cdots<A_s\) (cumulative multiplicities of its distinct heights) and positive gaps \(g_1,\ldots,g_s\), with \(n=\sum_i A_i g_i\). Therefore

\[
E(t,q)=\prod_{a\geq1}\left(1+t\frac{q^a}{1-q^a}\right)
\]

counts these partitions by \(n\) and the number \(s\) of distinct heights. The \(\binom{s-2}{2}\) part, set to zero for \(s\leq3\), has generating series \(P[3-2Q+(Q^2-R)/2]-3-D\): apply \(E(1,q)=P\), \(\partial_t E(1,q)=PQ\), and \(\partial_t^2E(1,q)=P(Q^2-R)\), then subtract the unwanted contributions at \(s=0,1\). An internal marked gap \(g_j\geq2\) requires at least one selected cumulative multiplicity on each side of \(A_j=m\), contributes \(q^{2m}/(1-q^m)\) at the marked position, and contributes \((P_{<m}-1)(P_{>m}-1)\) on the two sides. Summing over \(m\) yields the stated product–sum identity. All operations are well-defined coefficientwise in formal power series.

## Verification

`verify.py` uses only the Python standard library and may be run with `python3 verify.py`. Its two calculation paths are independent: one builds row-transfer graph neighborhoods and cliques to calculate lexicographic lower-link Euler increments; the other builds a formal-power-series state machine for the explicit positive statistic and marks internal gaps. Direct partition enumeration also supplies a comparison path. Results: 1,211 local lower-link checks for all partitions through \(n=17\), 81,155 direct partition-vs-generating-function checks through \(n=35\), agreement with the published first 25 ranks, and new coefficients through \(n=50\). Recorded output is `verify_output.txt`; the terminal marker is `ALL_VERIFY_OK`. The proof, not finite verification, establishes the unrestricted statement.

## Relationship to prior work

Lyudogovskiy [1] established \(K_n\simeq\bigvee^{\chi(K_n)-1}S^2\), but left the Euler characteristics unevaluated. Lyudogovskiy [2, §6, Problem 6.1] explicitly asked for exact formulas or structural reductions for the rank and listed numerical values through \(n=25\). Lyudogovskiy [3, §8, Problem 8.2] asked for a direct partition-theoretic meaning of the sphere rank and examined full neighborhoods; it did not produce this positive gap statistic. The contribution here is the explicit positive partition sum, its exact generating function, and a lower-link derivation which also yields a short, independent topological proof. The previously known qualitative sphere-wedge theorem and previously tabulated values are not claimed as new.

## Limitations

This is an ordinary homotopy-equivalence result for the specific one-cell transfer graph. It does not determine equivariant homotopy types, individual canonical sphere generators, or asymptotic growth of the coefficients. Searches of accessible literature cannot exclude an equivalent unindexed formulation; independent validation of the mathematical proof has not been performed.

## References

[1] F. B. Lyudogovskiy, *The homotopy type of the clique complex of the partition graph*, arXiv:2603.14370 (first public 2026-03-15), https://arxiv.org/html/2603.14370v1.

[2] F. B. Lyudogovskiy, *Numerical topology of the clique complex of the partition graph: Euler characteristic, clique counts, and sequence data*, arXiv:2603.26656 (first public 2026-03-27), https://arxiv.org/html/2603.26656v1.

[3] F. B. Lyudogovskiy, *Local Complexity, Overlap Control, and Global Simplicity in Partition Graphs*, arXiv:2606.20773 (first public 2026-06-18), https://arxiv.org/abs/2606.20773.

[4] F. B. Lyudogovskiy, *Local Morphology of the Partition Graph*, arXiv:2603.18696 (first public 2026-03-19), https://arxiv.org/html/2603.18696v1.
