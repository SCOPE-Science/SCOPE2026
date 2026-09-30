# Exact prescribed-coloring feasibility at maximum degree two

## Statement

Let \(n\ge 1\), write
\[
n=3s+m,\qquad m\in\{0,1,2\},
\]
and let \(\vec n=(n_1,\ldots,n_d)\) be a vector of positive integers with \(\sum_i n_i=n\). Call \(\vec n\) *universally feasible at degree two* if every \(n\)-vertex graph \(G\) with \(\Delta(G)\le 2\) has a proper coloring whose color-class sizes are exactly \(n_1,\ldots,n_d\).

Then \(\vec n\) is universally feasible at degree two if and only if
\[
n_i\le s+1\quad\text{for every }i,
\qquad
\#\{i:n_i=s+1\}\le m.
\tag{1}
\]
Equivalently, at most \(m\) color classes may have size \(s+1\), and every other class has size at most \(s\).

For \(m\in\{1,2\}\), this proves Conjecture 5 of Birken's *A Hajnal--Szemerédi theorem for skewed colorings* in the full case \(r=2\). The cases \(n=1,2\) are included in the statement and are immediate.

## Context

Birken defines an \(\vec n\)-coloring to be a proper coloring with prescribed color-class sizes and proves that every \(n\)-vertex graph of maximum degree at most \(r\) has such a coloring whenever every prescribed size is at most \(\lfloor n/(r+1)\rfloor\). He then conjectures the sharper remainder-sensitive condition: if \(n=s(r+1)+m\), then at most \(m\) classes may have size \(s+1\), with all remaining classes of size at most \(s\). The graph
\[
sK_{r+1}\sqcup K_m
\]
is identified there as the extremal obstruction showing that this condition is best possible.

The theorem above establishes that sharper conjecture exactly when \(r=2\), the first degree bound at which odd cycles occur.

## Proof

We use two elementary lemmas.

### Lemma 1: an independent feedback set of size \(\lceil n/3\rceil\)

If \(G\) has \(\Delta(G)\le 2\), then \(G\) has an independent set \(S\) of size \(\lceil n/3\rceil\) meeting every cycle of \(G\). Consequently, \(G-S\) is a linear forest.

**Proof.** Every component of \(G\) is a path or a cycle. Choose one vertex from every cycle component, and let \(X\) be the set of chosen vertices. The set \(X\) is independent because its vertices lie in distinct components. If \(c\) is the number of cycle components, then \(3c\le n\), so \(c\le\lfloor n/3\rfloor\).

For a path on \(\ell\) vertices there is an independent set of size \(\lceil\ell/2\rceil\). For a cycle on \(\ell\) vertices, any specified vertex belongs to an independent set of size \(\lfloor\ell/2\rfloor\). Choosing such independent sets componentwise, with the specified vertex from \(X\) included in each cycle component, gives an independent set \(I\supseteq X\) satisfying
\[
|I|\ge \left\lceil\frac n3\right\rceil.
\]
Because \(|X|\le\lfloor n/3\rfloor\), one may choose
\[
X\subseteq S\subseteq I,
\qquad
|S|=\left\lceil\frac n3\right\rceil.
\]
Then \(S\) is independent and intersects every cycle component, so \(G-S\) is acyclic and still has maximum degree at most two. Hence \(G-S\) is a linear forest. \(\square\)

### Lemma 2: prescribed colorings of linear forests

Let \(H\) be a linear forest on \(N\) vertices, and let \(a_1,\ldots,a_t\) be positive integers summing to \(N\). If
\[
\max_i a_i\le \left\lceil\frac N2\right\rceil,
\tag{2}
\]
then \(H\) has a proper coloring with color-class sizes \(a_1,\ldots,a_t\).

**Proof.** Join endpoints of the path components of \(H\) to obtain a spanning path \(P_N\) containing \(H\) as a subgraph. Thus it is enough to arrange a multiset containing \(a_i\) copies of symbol \(i\) in a sequence with no equal adjacent symbols. The standard multiset-arrangement criterion says that such a sequence exists exactly when the largest multiplicity is at most the number of all other symbols plus one, which is precisely (2). One explicit construction sorts symbols by decreasing multiplicity and places their copies successively in positions
\[
1,3,5,\ldots,2,4,6,\ldots;
\]
condition (2) ensures that equal copies are never consecutive. Coloring the vertices of \(P_N\) in this order gives the desired coloring, and restriction to \(H\) remains proper. \(\square\)

We now prove sufficiency of (1). If \(m=0\), or more generally if every \(n_i\le s\), Birken's Theorem 1 applies directly with \(r=2\), because \(s=\lfloor n/3\rfloor\).

It remains to consider \(m\in\{1,2\}\) when at least one prescribed class has size \(s+1\). By Lemma 1 choose an independent feedback set \(S\) with
\[
|S|=s+1.
\]
Assign one size-\(s+1\) color to \(S\). The remaining graph
\[
H=G-S
\]
is a linear forest on
\[
N=n-(s+1)=2s+m-1
\]
vertices.

If \(m=1\), condition (1) permits no second class of size \(s+1\), so every remaining prescribed size is at most
\[
s=\left\lceil\frac{2s}{2}\right\rceil=\left\lceil\frac N2\right\rceil.
\]
If \(m=2\), at most one remaining class has size \(s+1\), and
\[
s+1=\left\lceil\frac{2s+1}{2}\right\rceil=\left\lceil\frac N2\right\rceil.
\]
In either case Lemma 2 colors \(H\) with exactly the remaining prescribed sizes. Together with the color on \(S\), this gives the desired \(\vec n\)-coloring of \(G\).

For necessity, consider
\[
E_{s,m}=sK_3\sqcup K_m,
\]
with the last summand omitted when \(m=0\). This graph has maximum degree at most two. A color can occur at most once in each triangle and at most once in \(K_m\), so every color class has size at most \(s+1\), and when \(m=0\) at most \(s\). Moreover, a class of size \(s+1\) must use one vertex from every triangle and one vertex from \(K_m\). Since \(K_m\) is a clique, distinct size-\(s+1\) color classes require distinct vertices of \(K_m\). Hence there can be at most \(m\) such classes. Thus every universally feasible vector must satisfy (1). \(\square\)

## Consequences

The extremal graph from Birken's conjecture is not merely a witness to sharpness at \(r=2\): it characterizes all universally feasible prescribed size vectors. In particular, the universal feasibility problem for maximum-degree-two graphs depends only on \(n\bmod 3\), not on the arrangement of path and cycle components.

The proof separates the obstruction into two structural ingredients. One large class of size \(\lceil n/3\rceil\) can always be realized as an independent feedback set, after which the remaining graph is a linear forest. On a linear forest, the only obstruction to prescribed class sizes is the one-dimensional multiplicity bound \(\max a_i\le\lceil N/2\rceil\).

## Verification

The accompanying verifier independently generates every isomorphism type of graph of maximum degree at most two through order 12 as a multiset of path and cycle components. For every integer partition of the order, it solves the exact prescribed-coloring feasibility problem by backtracking from the adjacency relation and compares universality across all graph types with condition (1). It reports no discrepancy.

This finite computation is supporting evidence only; the theorem is proved above for all orders.

## Originality and limitations

The principal source inspected is Birken, arXiv:2609.18629v1 (16 September 2026). Its Theorem 1 establishes the smaller-class range \(n_i\le\lfloor n/(r+1)\rfloor\), while its Conjecture 5 states the remainder-sensitive larger-class condition proved here for \(r=2\). The paper explicitly identifies \(sK_{r+1}\sqcup K_m\) as the sharp obstruction, but does not state a proof for maximum degree two.

Kuchukova--Perkins--Povill, arXiv:2603.08259, introduced the fixed-class-size coloring setting used by Birken and described the existence theory beyond the equitable case as sparse; its prescribed-coloring conjecture is the smaller-class theorem now proved by Birken. Searches using the terms *prescribed coloring*, *fixed color class sizes*, *given color class sizes*, *color class cardinalities*, *maximum degree two*, *paths and cycles*, and *skewed coloring* did not locate an earlier exact degree-two characterization or the independent-feedback reduction above.

No specific inaccessible paper was identified that plausibly states this exact theorem. Residual originality risk remains because older coloring literature uses varied terminology for colorings with prescribed multiplicities, so an equivalent special-case statement may exist under different language. Originality is therefore asserted only **to the best of our knowledge**.

No claim is made here for \(r\ge3\), where Birken's Conjecture 5 remains open in the inspected source. Computational verification is finite and does not replace the proof.

## References

1. M. Birken, *A Hajnal--Szemerédi theorem for skewed colorings*, arXiv:2609.18629v1, 16 September 2026. https://arxiv.org/abs/2609.18629
2. A. Kuchukova, W. Perkins, X. Povill, *Sampling Colorings with Fixed Color Class Sizes*, arXiv:2603.08259; ICALP 2026. https://arxiv.org/abs/2603.08259
3. H. A. Kierstead, A. V. Kostochka, *A Short Proof of the Hajnal--Szemerédi Theorem on Equitable Colouring*, Combinatorics, Probability and Computing 17 (2008), 265--270. https://doi.org/10.1017/S0963548307008511
