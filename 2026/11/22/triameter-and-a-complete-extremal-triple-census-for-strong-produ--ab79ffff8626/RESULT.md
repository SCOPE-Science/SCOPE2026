# Triameter and a complete extremal-triple census for strong products of paths

## Finding

Let \(d\ge 2\), let \(q_1,\ldots,q_d\ge 2\) be integers, and let
\[G=P_{q_1}\boxtimes\cdots\boxtimes P_{q_d},\]
where \(P_q\) is the path with vertices \(0,1,\ldots,q-1\), and \(\boxtimes\) denotes the strong graph product. Put \(a=\max_i q_i\) and let \(k\) be the number of factors of order \(a\). Denote by \(T(G)\) the number of unordered triples of *distinct* vertices whose sum of three graph distances equals the triameter \(\operatorname{tr}(G)\).

**Case I: at least two largest factors (\(k\ge2\)).** Put \(R=\prod_{i:q_i<a}q_i\), with an empty product equal to one. Then
\[\operatorname{tr}(G)=3(a-1),\]
and
\[
T(G)=\frac{R^3}{6}\left[a^{3k}-3(a^3-2a)^k+3(a^3-4a+2)^k-(a^3-6a+6)^k\right].
\]

**Case II: a unique largest factor (\(k=1\)).** Among the other factors, let \(b\) be their largest order and \(r\ge1\) its multiplicity, and put \(S=\prod_{i:q_i<b}q_i\). Then, with \(R=b^r S\),
\[\operatorname{tr}(G)=2(a-1)+(b-1),\qquad
T(G)=R\bigl[R^2-S^2(b^2-2)^r\bigr].\]

Thus for a rectangular king graph \(P_m\boxtimes P_n\), \(m\ge n\ge2\),
\[\operatorname{tr}(G)=2m+n-3,\qquad T(G)=\begin{cases}2n,&m>n,\\4(n-1),&m=n.\end{cases}\]
In particular the largest-perimeter triples on a non-square king board are only \(2n\) in number, regardless of the longer dimension.

**Quadratic-dimensional transition.** For \(G_{q,d}=P_q^{\boxtimes d}\), with \(q\ge2,d\ge2\), the preceding formula gives the *entire* count of maximum-perimeter triples. If \(q\to\infty\) and \(d/q^2\to\lambda\in[0,\infty)\), the proportion of unordered three-vertex subsets that are triametral converges to
\[\bigl(1-e^{-2\lambda}\bigr)^3.\]
More precisely, for a uniformly chosen unordered triple, the number of its three pairs that fail to attain graph distance \(q-1\) converges in distribution to \(\operatorname{Binomial}(3,e^{-2\lambda})\). In particular, the triametral proportion tends to zero when \(d/q^2\to0\), and tends to one when \(d/q^2\to\infty\).

## Assumptions and scope

Graphs are finite, simple, undirected, and labelled by their coordinate vectors. Every \(q_i\) is at least two, and at least two factors are present. The graph distance in a strong product of paths is the Chebyshev distance
\[d_G(x,y)=\max_{1\le i\le d}|x_i-y_i|.\]
The triameter is \(\max_{x,y,z}\bigl(d_G(x,y)+d_G(x,z)+d_G(y,z)\bigr)\). A triametral triple has three distinct vertices. In the asymptotic statements, the path order \(q\) and the dimension \(d\) are integers; when \(\lambda=0\) we retain \(d\ge2\). The statement does not concern arbitrary graphs or other graph products.

## Proof

**1. A sharp three-distance upper bound.** Order the coordinate side lengths as \(A=q_{(1)}-1\ge B=q_{(2)}-1\ge\cdots\ge1\). For each of the three unordered pairs among \(x,y,z\), select a coordinate where its Chebyshev distance is attained. If all three pairs select one coordinate, their distance sum is at most twice that coordinate's range, hence at most \(2A\): for any real \(u,v,w\), \(|u-v|+|u-w|+|v-w|=2(\max\{u,v,w\}-\min\{u,v,w\})\). If two pairs select one coordinate and the third a distinct coordinate, their total is at most \(2a_i+a_j\), with \(a_i,a_j\) the two coordinate ranges, and hence at most \(2A+B\). If all three pairs select distinct coordinates, the sum is at most \(A+B+C\le 2A+B\). Consequently
\[\operatorname{tr}(G)\le2A+B.\]
Equality is realized using only the first two coordinates: take three vertices whose first two coordinates are respectively \((0,0)\), \((A,0)\), \((0,B)\), setting all remaining coordinates to zero. Their distances are \(A,A,B\). Thus \(\operatorname{tr}(G)=2A+B\), which gives both asserted triameter formulas.

**2. Unique longest side.** Suppose \(A>B\). Any triple of perimeter \(2A+B\) must have two pair-distances equal to \(A\), witnessed in the unique coordinate of range \(A\); the remaining pair-distance must equal \(B\). To see necessity without assuming it, use the coordinate assignment in step 1: assigning at most one pair to the longest coordinate bounds the total by \(A+2B<2A+B\); assigning all three pairs to that coordinate bounds it by \(2A\). Therefore two pairs must be assigned to that coordinate, their sum must be \(2A\), and the remaining selected coordinate must have range \(B\). Two coordinate differences with the same endpoint sum to \(2A\) only when the outlier has endpoint value zero or \(A\) and the other two vertices have the opposite endpoint value. Hence the repeated-endpoint pair must be at distance exactly \(B\) in the remaining \(d-1\) coordinates. Conversely all such triples attain the triameter.

Let \(R\) be the number of vertices in those remaining coordinates. Their number of **ordered** pairs at distance \(B\) is
\[R^2-S^2(b^2-2)^r,\]
since such a pair fails to have distance \(B\) exactly when, in each of the \(r\) coordinates of order \(b=B+1\), it avoids the two ordered opposite-endpoint pairs, while other coordinate pairs are unrestricted. To form an **ordered** triametral triple, choose which of the three points is the outlier (three options), its endpoint orientation (two options), its remaining-coordinate vector (\(R\) options), and an ordered pair of remaining-coordinate vectors at distance \(B\). Dividing by the six permutations of three distinct vertices proves the Case II formula.

**3. Tied longest sides.** Suppose \(A=B=a-1\), with \(k\ge2\) coordinates of order \(a\). The triameter is \(3A\), so a triple is triametral if and only if *each of its three pairs* differs by \(A\) in at least one of these \(k\) coordinates. For a single coordinate, there are \(a^3\) ordered triples of symbols. Given a specified pair of point labels, exactly \(2a\) triples place that pair at opposite endpoints; for any two specified pairs, their two events intersect in exactly two ordered symbol triples; all three events have empty intersection. Therefore the numbers of allowed symbol triples when one, two, or all three specified pair-events are forbidden are respectively
\[a^3-2a,\quad a^3-4a+2,\quad a^3-6a+6.\]
Independence between the \(k\) coordinates and inclusion-exclusion over the three pairs give the bracketed expression in Case I as the count of ordered \(k\)-coordinate triples in which all three pairs attain the diameter. Each shorter coordinate contributes an unconstrained ordered triple, giving a factor \(R^3\). All counted triples are necessarily distinct. Division by six establishes Case I.

**4. Limiting law.** Choose three independent uniformly distributed vertices of \(G_{q,d}\). For any specified set of \(j\in\{1,2,3\}\) pairs, the probability that none of these pairs is at distance \(q-1\) is, respectively for \(j=1,2,3\),
\[\left(1-\frac2{q^2}\right)^d,\quad
\left(1-\frac4{q^2}+\frac2{q^3}\right)^d,\quad
\left(1-\frac6{q^2}+\frac6{q^3}\right)^d.\]
When \(q\to\infty\) and \(d/q^2\to\lambda<\infty\), these converge to \(e^{-2j\lambda}\). These are all joint probabilities that any chosen subset of the three diameter events fails; inclusion-exclusion (or Möbius inversion on the three-event Boolean lattice) therefore gives joint convergence to three independent failure indicators of probability \(e^{-2\lambda}\). Their sum converges to the stated binomial law. The probability that the independent vertices are distinct tends to one, because \(q^d\ge q^2\to\infty\), so conditioning on distinctness gives the same limit for uniformly chosen unordered triples. If instead \(d/q^2\to\infty\), the probability of any missing diametral pair is at most \(3(1-2/q^2)^d\to0\), giving the remaining assertion.

## Verification

The included standalone Python 3 script `verify.py` reconstructs the vertex sets and directly computes the maximum three-point perimeter and the number of unordered maximizers, using the Chebyshev graph distance rather than relying on any coefficient formulas. It compares these with both closed formulas on twelve mixed-size instances and on further uniform powers. It checked \(676739\) unordered triples and returned `VERIFY_OK`. These finite checks are corroboration, not proofs of the quantified formulas or the limiting distribution.

## Relationship to prior work

Hak and Kozerenko's 2026 triameter paper supplies the motivating graph invariant and general sharp bounds in terms of packing and connectivity, with extremal graph characterizations for those constraints. It does not compute the triameter or triametral-triple census in strong products of paths. Bujtás, Iršič Chenoweth, Klavžar and Zhang's paper studies distance packing domination on strong products of paths, cycles and other graphs; it states the standard Chebyshev distance identity but its results concern a different invariant. Neither article supplies the extremal-triple counts or the dimension-to-alphabet threshold here. The exact formulas use standard inclusion-exclusion and the known strong-product distance identity; novelty is asserted only for their application to the complete triameter extremizer census and transition. Priority remains provisional until broader independent literature verification.

## Limitations

The result applies to strong products of at least two finite paths, not to arbitrary strong products, graph powers, or arbitrary lattice subsets. The quadratic-dimensional limit considers uniformly sampled triples with the stated joint scaling of side length and dimension, not arbitrary nonuniform sampling. The proof is self-contained apart from the standard distance identity, which is also immediate from simultaneous coordinate moves. Independent validation or external priority certification is not claimed.

## References

1. A. Hak and S. Kozerenko, *Triameter, distance packings, and vertex connectivity*, arXiv:2611.17259v1, first posted 2026-11-12. https://arxiv.org/abs/2611.17259
2. C. Bujtás, V. Iršič Chenoweth, S. Klavžar and G. Zhang, *On \(d\)-distance \(p\)-packing domination number in strong products*, arXiv:2510.02749, first posted 2025-10-03; *Annals of Combinatorics*, published 2026-03-26. https://doi.org/10.1007/s00026-026-00814-0
3. A. Das, *Triameter of graphs*, *Discussiones Mathematicae Graph Theory* 41 (2021), 601–616. https://arxiv.org/abs/1804.01088
