# Maximum-independent-set transversal polynomial of one-defect cycle powers

## Finding

Let \(q,k\) be any integers with \(q\ge 2\) and \(k\ge2\), put \(n=kq+1\), and let \(G=C_n^{q-1}\) be the \((q-1)\)-st **distance power** of the labelled cycle with vertices \(\mathbb Z/n\mathbb Z\). Its edges join distinct vertices with cyclic distance at most \(q-1\). A transversal is a vertex set meeting **every maximum-cardinality independent set** of \(G\), not merely every maximal independent set.

Write \(H_{q,k}(z)=\sum_{T}z^{|T|}\), where the sum ranges over all transversals of the family of maximum independent sets. Then

\[
\boxed{H_{q,k}(z)=\sum_{t=q+1}^{kq+1}\frac{kq+1}{t}\,[u^{kq+1}](u+u^2+\cdots+u^k)^t z^t.}
\]

In particular, the hitting number and the **exact number of minimum transversals** are respectively

\[
\boxed{h(G)=q+1,\qquad [z^{q+1}]H_{q,k}(z)=\frac{kq+1}{q+1}\binom{k+q-1}{q}.}
\]

All maximum independent sets admit a simultaneous structural description: there are exactly \(n\) of them, namely

\[
I_j=\{j,j+q,\ldots,j+(k-1)q\}\pmod n\qquad(j\in\mathbb Z/n\mathbb Z).
\]

Since \(\gcd(q,n)=1\), the cyclic permutation \(0,q,2q,\ldots,(n-1)q\) transforms these \(n\) maximum independent sets into exactly the \(n\) consecutive length-\(k\) arcs of an \(n\)-cycle. Accordingly a subset is a transversal if and only if each gap between successive selected vertices in **this permuted cyclic order** is at most \(k\).

For fully explicit integer coefficients, the coefficient of \(z^t\), for \(q+1\le t\le n\), also equals

\[
\frac nt\sum_{j=0}^{\lfloor(n-t)/k\rfloor}(-1)^j\binom tj\binom{n-jk-1}{t-1}.
\]

## Assumptions and scope

All graphs are finite, simple, undirected, and labelled. A distance power is different from a strong graph-product power. Quantifiers: **every** pair of integers \(q,k\ge2\); no other restrictions. Only the first nondivisible order \(n=kq+1\) is asserted. The generating polynomial counts labelled vertex subsets (not automorphism classes); coefficient \([z^t]\) counts transversals of cardinality exactly \(t\). There is no constant term.

## Proof

**Maximum independent sets.** Let \(S\) be independent with \(a\) selected vertices, listed clockwise around the original cycle. Every circular gap between consecutive selected vertices contains at least \(q\) original-cycle steps. Hence \(a q\le n=kq+1\), so \(a\le k\). Taking vertices \(0,q,\ldots,(k-1)q\) attains \(k\), so \(\alpha(G)=k\).

If \(a=k\), the \(k\) positive clockwise gaps are at least \(q\) and sum to \(kq+1\). Thus exactly one gap is \(q+1\) and all others are \(q\). Start immediately **after** the unique longer gap. This recovers precisely one of the displayed sets \(I_j\), which consequently are pairwise distinct and exhaust all maximum independent sets. This classification includes the boundary case \(k=2\).

**Cyclic-arc equivalence.** As \(\gcd(q,kq+1)=1\), repeatedly adding \(q\) visits all \(n\) vertices. In that cyclic order, the sets \(I_j\) are exactly the intervals of \(k\) consecutive vertices. A subset \(T\) meets every one of those intervals exactly when it contains no gap of \(k\) consecutive unselected vertices. Writing \(d_1,\ldots,d_t\) for the positive step distances between consecutive vertices of \(T\) in the new cyclic order, this is equivalent to \(1\le d_i\le k\) for every \(i\), with \(\sum_i d_i=n\).

**Enumeration.** Count pairs consisting of a transversal \(T\) of size \(t\) and a distinguished vertex of \(T\). There are \(n\) choices of the distinguished starting vertex and \([u^n](u+\cdots+u^k)^t\) choices of its ordered cyclic gaps. Each unmarked transversal is counted exactly \(t\) times. Dividing by \(t\) proves the polynomial formula. The gap equations have solutions only for \(t\ge\lceil n/k\rceil=q+1\), and all \(t\in[q+1,n]\) are realized; therefore \(h(G)=q+1\).

At \(t=q+1\), write \(d_i=k-e_i\). The nonnegative deficits sum to \((q+1)k-n=k-1\). Their upper bounds are automatic, and stars-and-bars gives \(\binom{k+q-1}{q}\) ordered deficit vectors. The distinguished-vertex count now yields the minimum-transversal formula. Finally, expansion of \((1-u^k)^t(1-u)^{-t}\) in the gap generating function gives the alternate binomial sum.

Every step is finite and exact; no limiting or probabilistic argument is used.

## Verification

The accompanying `verify.py` implements the original distance-power independence condition, exhaustively recovers the maximum independent sets, and directly tests every vertex subset against all maximum independent sets for 14 parameter pairs with \(2\le q\le5\), \(2\le k\le6\), and \(kq+1\le17\). These cases cover 293,152 candidate subsets. Every coefficient agrees with the displayed formula. A second dynamic program counts bounded gap compositions for four larger parameter pairs and agrees with the independent inclusion-exclusion expression. Run with `python verify.py` using only the Python standard library.

As illustrations, for \((q,k,n)=(2,3,7)\) the minimum is three with 14 minimum transversals, while for \((3,3,10)\) it is four with 25 minimum transversals. The proof, not the finite tests, establishes the universal claim.

## Relationship to prior work

Bai–Chang–Yan (2026) focus on general reduction principles and bounds for hitting all maximum independent sets. In particular their bound involving \(2\alpha(G)+\delta(G)-|V(G)|\) does not supply these exact coefficients or the one-defect cyclic-arc correspondence. Dong–Luo (2025) study resistance of the independence number to vertex deletion; their tight-stability classification includes odd cycles but does not count the transversals here. Bohman–Holzman–Natarajan (2009) use **strong graph-product powers** of odd cycles, a different graph operation from the distance power above.

The bounded-gap composition is classical, but the result identifies the entire maximum-independent-set hypergraph of a nontrivial distance-power family with circular interval hypergraphs and transfers the **complete** transversal enumerator back to the original graph. The work is motivated by the first nondivisible order, where all maximum stable configurations have exactly one surplus gap. A literature search cannot rule out an unlocated equivalent enumeration.

## Limitations

No formula is claimed for arbitrary orders \(kq+s\) with \(2\le s<q\), for arbitrary circulant graphs, or for transversals of all *maximal* independent sets. The theorem does not count equivalence classes modulo graph automorphisms. The exact formula is proved combinatorially; the experiments are finite corroborations. Historical priority remains provisional; no independent external mathematical assessment is asserted.

## References

- H. Bai, Y. Chang, and J. Yan, *Hitting Maximum Independent Sets in Dense and Highly Connected Graphs*, arXiv:2608.18963v1 (first public 2026-08-19), https://arxiv.org/abs/2608.18963.
- D. Dong and S. Luo, *Structure of Tight (k,0)-Stable Graphs*, Electronic Journal of Combinatorics 32(4) (2025), P4.45, https://doi.org/10.37236/13791.
- T. Bohman, R. Holzman, and V. Natarajan, *Maximum Independent Sets in Certain Powers of Odd Cycles*, Electronic Journal of Combinatorics 16 (2009), N26, https://doi.org/10.37236/264. This paper concerns strong graph-product powers, not the distance powers used here.
