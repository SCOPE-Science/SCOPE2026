# A quadratic-time exact next-window likelihood for random binary de Bruijn cycles

## Finding
For every integer \(n\ge2\) and every prescribed binary word \(s=s_0\cdots s_n\) of length \(n+1\), the exact probability that \(s\) occurs in a uniformly random labelled binary de Bruijn *cycle* of order \(n\), modulo rotation, is computable using at most quadratic many bit operations in \(n\) and linear auxiliary space. The algorithm needs no determinant, graph construction, or enumeration of cycles.

Here is the full closed formula. Set \(m=n-1\), and let \(u=s_0\cdots s_{m-1}\), \(v=s_1\cdots s_m\), and \(w=s_2\cdots s_{m+1}\), each of length \(m\). For \(0\le t<m\) define
\[
H_t(x,y)=\mathbf 1\{\operatorname{suf}_{m-t}(x)=\operatorname{pre}_{m-t}(y)\}.
\]
If \(s_0\cdots s_{n-1}=s_1\cdots s_n\) (equivalently, \(s\) is constant), then \(p_n(s)=0\). In all other cases,
\[
\boxed{p_n(s)=1+\sum_{t=0}^{m-1}\frac{H_t(v,u)-H_t(v,v)-H_t(w,u)+H_t(w,v)}{2^{t+1}}.}
\]
In particular, \(2^{n-1}p_n(s)\) is an integer. The exact number of de Bruijn cycles containing \(s\) is
\[
\boxed{2^{2^{n-1}-n}p_n(s)}.
\]
The novelty asserted is the **compact, matrix-free, polynomial-time evaluation specialized to binary de Bruijn cycles**, not the general existence of exact motif probabilities under constrained word-shuffling laws.

## Assumptions and scope
A binary de Bruijn cycle of order \(n\) is a cyclic binary word of length \(2^n\) in which all length-\(n\) binary factors appear exactly once. Cycles differing by cyclic rotation are identified, but the symbols \(0\) and \(1\) are fixed and not identified. All such cycles receive equal probability. The event is that \(s\) is among the cyclic length-\(n+1\) factors of the cycle; it occurs at most once, because its first length-\(n\) factor is unique. For a length-\(m\) word, \(\operatorname{pre}_r\) and \(\operatorname{suf}_r\) denote the first and last \(r\) symbols respectively, including \(r=m\).

## Proof
Let \(G\) be the order-\(n\) binary de Bruijn Euler digraph: its \(2^m\) vertices are the length-\(m\) binary words, and its \(2^n\) distinct labeled arcs are the length-\(n\) words, directed from their length-\(m\) prefix to their length-\(m\) suffix. Every vertex has indegree and outdegree two. Euler circuits with cyclic starting points suppressed correspond bijectively to the de Bruijn cycles. The BEST formula gives the number of such circuits as the number \(\tau(G)\) of spanning in-arborescences rooted at a prescribed vertex, since \(\prod_x(d_x-1)!=1\). The classical binary de Bruijn count gives \(\tau(G)=2^{2^{n-1}-n}\).

Write \(e=s_0\cdots s_{n-1}\) and \(f=s_1\cdots s_n\), the two consecutive arcs \(u\xrightarrow{e}v\xrightarrow{f}w\). If \(e=f\), these are the same labeled arc and cannot occur consecutively on an Euler circuit, so \(p_n(s)=0\). Otherwise contract the ordered two-arc path to a single distinguished shortcut arc \(u\to w\), removing arcs \(e,f\), and call the resulting balanced multigraph \(G_s\). Contracting and expanding this shortcut is a bijection between Euler circuits of \(G\) containing the adjacency \(e,f\) and Euler circuits of \(G_s\). Every vertex of \(G_s\) has outdegree two except \(v\), which has outdegree one, even if \(u\), \(v\), or \(w\) coincide. The BEST factorial remains one, including cases with disconnected \(G_s\), where the count is zero. Thus
\[
p_n(s)=\frac{\tau(G_s)}{\tau(G)}.
\]

Index the vertices, write \(e_x\) for a coordinate basis column, and set \(P_{xy}\) to the transition probability of the uniformly random shift-and-append walk: each step removes the leading bit of the current length-\(m\) word and appends an independent fair bit. The row-outdegree Laplacian of \(G\) is \(L=2(I-P)\). Directly subtracting the two deleted arc contributions and adding the shortcut contribution yields the **rank-one identity**
\[
L_s=L+(e_u-e_v)(e_v-e_w)^{\mathsf T}.
\]
Both Laplacians have zero row and column sums. Let \(N=2^m\) and \(J=N^{-1}{\bf1}{\bf1}^{\mathsf T}\). The directed Matrix-Tree theorem gives \(\det(L+J)=N\tau(G)\) and \(\det(L_s+J)=N\tau(G_s)\), including a zero in the latter if disconnected. Applying the rank-one determinant lemma therefore gives
\[
\frac{\tau(G_s)}{\tau(G)}=1+(e_v-e_w)^{\mathsf T}(L+J)^{-1}(e_u-e_v).
\]
After exactly \(m\) independent shift-and-append steps all original bits have been replaced, so \(P^m=J\). Since \(e_u-e_v\) has coordinate sum zero, the inverse of \(L+J\) acting on it is the finite Green sum
\[
(L+J)^{-1}(e_u-e_v)=\frac12\sum_{t=0}^{m-1}P^t(e_u-e_v).
\]
For \(0\le t<m\), the walk has precisely \(2^t\) equally likely choices of appended bits and
\[
P^t(x,y)=2^{-t}H_t(x,y).
\]
Substitution yields the claimed four-overlap sum exactly. This proves all quantifiers, including \(n=2\), loops, the impossible event, and the full cyclic wraparound. Because each summand has denominator dividing \(2^m\), so does the final probability.

For each \(t\), computing four suffix-prefix equalities of at most \(m\) bits using a direct comparison needs \(O(m)\) bit operations. There are \(m\) terms. The dyadic accumulator needs only \(O(m)\) bits; hence the total exact computation uses \(O(n^2)\) bit operations and \(O(n)\) space. The bit-operation bound includes parsing the \(n+1\) input symbols, without treating exponentially sized integers as constant-time objects. \(\square\)

## Verification
The standalone `verify.py` runs three independent checks. First, it enumerates *all* local successor bijections at the \(2^{n-1}\) vertices for every order \(2\le n\le5\), retains exactly those giving a single Euler circuit, and independently counts the frequencies of all \(2^{n+1}\) prescribed windows. The cycle totals are \(1,2,16,2048\), and every exact rational frequency agrees with the formula. Second, it tests all binary prescribed windows for \(2\le n\le11\), checking the probability interval, denominators, the identity \(\sum_s p_n(s)=2^n\), and the four known impossible motifs. Third, a separate direct integer Laplacian-cofactor calculation was performed for every nonconstant prescribed word at orders two through five and matched the overlap formula. Finite experiments verify the calculation, while the proof above establishes it for every order.

For example, at order four, the motif `00100` has probability \(1/4\); at order five, `001011` has probability \(3/8\). To reproduce the standalone checks, run `python3 verify.py` with Python 3 standard library only.

## Relationship to prior work
Rødland (2006), Theorem 1 and Appendix B, gives **a general exact path-contraction/tree-determinant method for motif frequencies** under fixed \(k\)-word compositions. In particular, it **already implies the scalar probability** of any prescribed next-order factor of a de Bruijn cycle. The general exact formula and its underlying BEST or Matrix-Tree arguments are therefore not claimed new. However, applying that general method to a binary de Bruijn graph appears to require handling a Laplacian with \(2^{n-1}\) vertices; the present result eliminates the entire matrix by using the shift-register mixing identity \(P^m=J\) and gives an explicit \(O(n^2)\)-bit algorithm. The computational complexity reduction, not merely pointwise existence, is the scope of the claimed contribution.

Lin, Ward, Jain and Skiena (2011) motivate controlling next-order motifs to construct orthogonal de Bruijn cycles, but focus on existence and construction rather than an input-linear or quadratic exact motif likelihood. Sawada and Gabrić (2025) establish practical uniform samplers, not this closed per-motif evaluation. The published *Exact next-order factor support across de Bruijn cycles* identifies which motifs can occur in at least one cycle; its source theorem explicitly leaves their exact probabilities uncomputed. Its support classification is not asserted as new here.

## Limitations
This is an exact **single-motif** likelihood for binary, unconstrained, uniformly sampled de Bruijn cycles of order at least two. The formula does not characterize simultaneous events, motif covariances, nonbinary alphabets, weight-restricted universal cycles, or joint optimization across several motifs. Generic exact motif-frequency formulas were already known, and the new contribution is their polynomial-time explicit evaluation for this highly structured family. A general prior identity could conceivably be specialized to the same computational bound in an unlocated source; the literature comparison is not proof of uniqueness. No independent scientific audit has been performed.

## References
1. E. A. Rødland, *Exact distribution of word counts in shuffled sequences*, Advances in Applied Probability 38 (2006), 116–133, Theorem 1 and Appendix B. https://doi.org/10.1239/aap/1143936143
2. Y.-L. Lin, C. Ward, B. Jain and S. Skiena, *Constructing orthogonal de Bruijn sequences*, WADS 2011, 595–606. First verified dated publication 2011-08-12. https://doi.org/10.1007/978-3-642-22300-6_50
3. J. Sawada and D. Gabrić, *Random generation of universal cycles and de Bruijn sequences*, arXiv:2510.16545, first posted 2025-10-18. https://arxiv.org/abs/2510.16545
4. *Exact next-order factor support across de Bruijn cycles* (2026), publicly archived research result. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-next-order-factor-support-across-de-bruijn-cycles--02203ca2da50
