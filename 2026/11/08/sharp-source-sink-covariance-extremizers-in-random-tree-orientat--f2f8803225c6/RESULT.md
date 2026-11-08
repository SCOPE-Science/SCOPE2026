# Sharp source–sink covariance extremizers in random tree orientations

## Finding

Let \(T\) be a fixed finite simple tree with \(n\ge4\) vertices. Orient its \(n-1\) edges independently and uniformly, and let \(S(T)\) and \(K(T)\) be respectively the numbers of sources (indegree zero) and sinks (outdegree zero). For \(d_v=\deg_T(v)\),
\[
\operatorname{Cov}(S(T),K(T))
=2\sum_{uv\in E(T)}2^{-d_u-d_v}-\sum_{v\in V(T)}4^{-d_v}.
\]
Among all such trees on \(n\) vertices, this covariance is **uniquely maximized**, up to tree isomorphism, by the path \(P_n\), and **uniquely minimized** by the star \(K_{1,n-1}\). The sharp bounds are
\[
\boxed{
\frac{n-1}{2^{n-1}}-\frac{n-1}{4}-4^{-(n-1)}
\ \le\ \operatorname{Cov}(S(T),K(T))\ \le\ \frac{n-4}{16}.
}
\]
Equality on the left holds exactly for stars and equality on the right exactly for paths. For \(n\ge5\), the two extremal covariances have opposite signs: the star value is negative and the path value is positive. At \(n=4\), the path covariance is zero.

## Assumptions and scope

A *source* is a vertex all of whose incident edges point outward, and a *sink* is a vertex all of whose incident edges point inward. The underlying tree is deterministic and has no loops, multiple edges, or isolated vertices. All \(2^{n-1}\) orientations are equally likely; neither the underlying tree nor its vertex labels are sampled randomly. Covariance is taken over orientations of that fixed tree. The extremal inequalities concern all nonisomorphic unlabeled tree shapes, equivalently all labeled trees, for each integer \(n\ge4\).

## Proof

**Step 1: Exact local covariance identity.** Let \(I_v\) and \(J_v\) indicate that \(v\) is respectively a source and a sink. Then \(\mathbb E I_v=\mathbb E J_v=2^{-d_v}\). For \(u=v\), the two events are incompatible because \(d_v\ge1\), so \(\operatorname{Cov}(I_v,J_v)=-4^{-d_v}\). For distinct nonadjacent vertices, the events involve disjoint edge directions and are independent. For adjacent distinct \(u,v\), the direction \(u\to v\) is compatible simultaneously with \(I_u=1\) and \(J_v=1\), so
\[
\mathbb P(I_u=J_v=1)=2^{-(d_u+d_v-1)},
\qquad \operatorname{Cov}(I_u,J_v)=2^{-(d_u+d_v)}.
\]
The swapped ordered pair contributes the same quantity. Summing these exhaustive cases proves the first formula.

**Step 2: Energy identity and the unique maximum.** Put \(x_v=2^{-d_v}\). The first formula rearranges into
\[
C(T):=\operatorname{Cov}(S(T),K(T))
=\sum_v(d_v-1)4^{-d_v}
-\sum_{uv\in E(T)}(x_u-x_v)^2.
\]
As \(\sum_v(d_v-1)=n-2\), subtracting from the claimed path value gives
\[
\frac{n-4}{16}-C(T)
=\sum_v(d_v-1)\left(\frac1{16}-4^{-d_v}\right)
+\sum_{uv\in E(T)}(x_u-x_v)^2-\frac18.
\tag{1}
\]
For the path, each of the two leaf–degree-two edges has squared difference \(1/16\); all other differences vanish. The first sum in (1) vanishes, giving equality. For a nonpath, some vertex has degree at least three. Each degree-three vertex contributes \(3/32\) to the first sum in (1), and a vertex of degree at least four contributes at least \(45/256\). If there are at least two vertices of degree at least three, the first sum alone is at least \(3/16>1/8\). If exactly one vertex has degree at least four, its contribution alone is at least \(45/256>1/8\). In the remaining case exactly one vertex has degree three and all others have degree one or two: the three edges incident to that vertex each have squared difference at least \(1/64\), so the two sums total at least \(3/32+3/64=9/64>1/8\). Thus (1) is strictly positive for every nonpath, proving uniqueness.

**Step 3: The unique minimum for \(n\ge7\).** The star has \(n-1\) degree-one vertices and a single degree-\(n-1\) vertex. Substitution into the local formula gives
\[
C(K_{1,n-1})=-\frac{n-1}{4}+h_n,
\qquad h_n=\frac{n-1}{2^{n-1}}-4^{-(n-1)}.
\]
For \(n\ge7\), \(0<h_n<(n-1)/2^{n-1}\le 3/32<1/8\). Every nonstar tree has at least two nonleaves. Since degree-one vertices contribute \(1/4\) and vertices of degree at least two contribute at most \(1/16\) to \(\sum_v4^{-d_v}\), writing \(r\ge2\) for the number of nonleaves yields
\[
\sum_v4^{-d_v}\le\frac{n-r}{4}+\frac r{16}
\le\frac{n-1}{4}-\frac18.
\]
The positive edge term in the first covariance identity then gives
\[
C(T)>-\frac{n-1}{4}+\frac18
>C(K_{1,n-1}).
\]
This proves the lower extremum and its uniqueness for every \(n\ge7\).

**Step 4: The remaining small orders.** For \(n=4,5,6\), the distinct sorted degree sequences and all possible covariance values (one value per tree isomorphism class) are:

| \(n\) | Sorted vertex degrees | Possible covariance values |
|---|---|---|
| 4 | \((1,1,1,3)\) | \(-25/64\) |
| 4 | \((1,1,2,2)\) | \(0\) |
| 5 | \((1,1,1,1,4)\) | \(-193/256\) |
| 5 | \((1,1,1,2,3)\) | \(-17/64\) |
| 5 | \((1,1,2,2,2)\) | \(1/16\) |
| 6 | \((1,1,1,1,1,5)\) | \(-1121/1024\) |
| 6 | \((1,1,1,1,2,4)\) | \(-153/256\) |
| 6 | \((1,1,1,1,3,3)\) | \(-1/2\) |
| 6 | \((1,1,1,2,2,3)\) | \(-13/64,-9/64\) |
| 6 | \((1,1,2,2,2,2)\) | \(1/8\) |

These rows are exhaustive: a tree's degrees are positive with sum \(2n-2\), and for the listed orders the degree sequences and degree-adjacency possibilities determine precisely the cases shown. Direct substitution of each case into the local identity establishes the displayed values. The star is the strict minimum at all three orders; the path is the strict maximum. Together with Steps 2–3 this proves the theorem for all \(n\ge4\).

## Verification

A self-contained exact-arithmetic Python script, `verify.py`, checks the formula and both equality characterizations for every Prüfer-coded labeled tree of each order \(4\le n\le8\) (\(280388\) trees in total). For every labeled tree with \(4\le n\le6\), it also independently enumerates every edge orientation, calculates the original sample covariance from orientation counts, and checks agreement with the local formula. Running `python verify.py` using Python 3 and its standard library prints `PASS`. These finite tests support error detection; the complete all-order proof is Steps 1–4 above.

## Relationship to prior work

Linusson, *A note on correlations in randomly oriented graphs* (arXiv:0905.2881, first submitted 18 May 2009), proves correlation inequalities for **directed reachability** events in the same independent-edge orientation model, rather than optimizing the covariance of the aggregate source and sink counts over tree shape. Alm, Janson and Linusson, *Correlations for paths in random orientations of \(G(n,p)\) and \(G(n,m)\)* (arXiv:0906.0720, first submitted 3 June 2009), study pairs of directed-path events in random underlying graphs, not these two aggregate counts on a fixed tree. Engström, *Random acyclic orientations of graphs* (KTH thesis, 2013), discusses the mean source count and unique-source probability, but the inspected Section 5.3 does not state the sharp covariance extrema. Okoth and Wagner, *Locally oriented noncrossing trees* (2015), enumerate sources and sinks for **noncrossing tree shapes oriented deterministically by vertex labels**, a different probability space. The extremal statement here is neither a consequence of a directed-reachability correlation inequality nor an extremal comparison in the label-induced noncrossing-tree model.

## Limitations

This result concerns fair, independent edge directions and fixed tree shapes; it does not address biased orientations, random underlying trees, directed reachability counts, or non-tree graphs. The source–sink covariance identity itself is elementary local counting; the all-tree-shape extremal theorem is the asserted additional contribution. Historical implicit coverage by broader orientation enumerators or uninspected older work remains a priority risk. The numerical checks do not certify the infinite family independently. No independent mathematical audit has been performed.

## References

1. S. Linusson, *A note on correlations in randomly oriented graphs*, arXiv:0905.2881, first submitted 2009-05-18, https://arxiv.org/abs/0905.2881 .
2. S. E. Alm, S. Janson, and S. Linusson, *Correlations for paths in random orientations of G(n,p) and G(n,m)*, arXiv:0906.0720, first submitted 2009-06-03, https://arxiv.org/abs/0906.0720 .
3. S. Engström, *Random acyclic orientations of graphs*, KTH thesis (2013), https://www.diva-portal.org/smash/get/diva2%3A590036/FULLTEXT01.pdf .
4. I. O. Okoth and S. Wagner, *Locally Oriented Noncrossing Trees*, Electronic Journal of Combinatorics 22(3) (2015), P3.36, https://doi.org/10.37236/5164 .
