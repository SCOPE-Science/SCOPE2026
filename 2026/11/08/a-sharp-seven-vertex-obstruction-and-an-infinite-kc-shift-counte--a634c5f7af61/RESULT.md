# A sharp seven-vertex obstruction and an infinite KC-shift counterfamily for random greedy matching

## Finding

Let \(\mu(T)\) be the expected number of edges selected by the random greedy matching algorithm on a finite tree \(T\): repeatedly select uniformly one currently feasible edge, add it to the matching, and delete its two endpoints and all incident edges.

Write \(P_n\) for the path on \(n\) vertices and \(S(a,b,c)\) for the tree with three arms of \(a,b,c\) edges joined at a central vertex. Then **for every integer \(L\ge2\)**, a single proper Kelmans–Csikvári (KC) tree shift takes \(P_{L+5}\) to \(S(2,2,L)\), and

\[
\mu(S(2,2,L))>\mu(P_{L+5}).
\]

This strict increase cannot occur on trees of fewer than seven vertices: every proper KC shift of a tree on at most six vertices weakly decreases \(\mu\). The first example is

\[
\mu(P_7)=\frac{26}{9},\qquad \mu(S(2,2,2))=3,\qquad
\mu(S(2,2,2))-\mu(P_7)=\frac19.
\]

Conversely, a proper KC shift of \(P_4\) to the four-vertex star strictly decreases the expected greedy matching size, from \(5/3\) to \(1\). Consequently, random greedy matching expectation is **neither increasing nor decreasing** on the KC tree poset.

## Assumptions and scope

All graphs here are finite, undirected, simple and unweighted. The algorithm chooses uniformly among the presently feasible edges, equivalently processing the original edges in a uniformly random order and accepting an edge exactly when its endpoints are both currently unmatched. Edges chosen in disjoint components contribute independent, additive expectations. A proper KC shift on a tree takes a bare path between two nonleaf vertices, transfers all off-path branches at one endpoint to the other, and increases the number of leaves by one. This theorem concerns expected **edge** greedy matching cardinality, not vertex greedy independent-set cardinality.

For \(L\ge2\), label the path \(0,1,\ldots,L+4\) in order. Move edge \(\{1,2\}\) to \(\{1,4\}\), leaving all other edges unchanged. The bare path from vertex \(2\) to vertex \(4\) has internal vertex \(3\) of degree two, and both endpoints have degree two. The resulting tree has center \(4\) and arms of lengths \(2,2,L\); hence this is a proper KC shift.

## Proof

**First-edge recurrence.** For a graph \(G\) with \(m>0\) edges, selecting the first feasible edge and using additivity on components gives

\[
\mu(G)=1+\frac1m\sum_{e\in E(G)}\mu(G-V(e)),
\]

where isolated vertices contribute zero. Put \(p_n=\mu(P_n)\), with \(p_0=p_1=0\). Deleting the endpoints of an edge of \(P_n\) splits the remaining graph into paths. Thus, for every \(n\ge2\),

\[
p_n=1+\frac{2}{n-1}\sum_{j=0}^{n-2}p_j,
\qquad
p_n=\sum_{j=1}^{n-1}\frac{(-2)^{j-1}(n-j)}{j!}.
\]

The closed expression follows by induction from the recurrence (or by taking successive differences). In particular, with \(\delta_n=p_n-p_{n-1}\),

\[
\delta_n=\sum_{j=1}^{n-1}\frac{(-2)^{j-1}}{j!},
\qquad (n-1)p_n=(n-2)p_{n-1}+2p_{n-2}+1\quad(n\ge3).
\]

**Spider recurrence.** Set \(F_L=\mu(S(2,2,L))\), allowing a zero arm for the auxiliary base case. Direct first-edge counting gives \(F_0=p_5=2\) and \(F_1=p_6=37/15\). For \(L\ge1\), the spider has \(L+4\) edges. Its two outer short-arm edges each leave a path of \(L+3\) vertices, its two inner short-arm edges each leave a disjoint one-edge component and a path of \(L\) vertices, the center edge of the long arm leaves two one-edge components and a path of \(L-1\) vertices, and the other long-arm edges leave a path and a shorter spider. Therefore

\[
F_L=1+\frac{4+2p_L+2p_{L+3}+p_{L-1}
+\sum_{r=0}^{L-2}p_r+\sum_{r=0}^{L-2}F_r}{L+4},
\]

with empty sums understood as zero. Subtracting consecutive identities, for \(L\ge2\), gives

\[
(L+4)F_L=(L+3)F_{L-1}+F_{L-2}
+1+2p_L-p_{L-1}+2p_{L+3}-2p_{L+2}.
\]

**Strict sign for all sizes.** Define \(d_L=F_L-p_{L+5}\). The path recurrence and the preceding identity imply

\[
(L+4)d_L=(L+3)d_{L-1}+d_{L-2}+b_L,\qquad d_0=d_1=0,
\]

where

\[
\begin{aligned}
b_L&=p_{L+3}-2p_{L+2}+2p_L-p_{L-1}\\
&=\delta_{L+3}-\delta_{L+2}-\delta_{L+1}+\delta_L\\
&=\frac{2(-2)^{L-2}(L^2+3L-2)}{L!(L+1)(L+2)}.
\end{aligned}
\]

For \(L\ge2\), let \(h_L=|b_L|\). Then \(b_L\) has sign \((-1)^L\), and

\[
\frac{h_{L+1}}{h_L}=
\frac{2(L^2+5L+2)}{(L+3)(L^2+3L-2)}<1,
\]

because the denominator minus the numerator equals \((L-2)(L+3)^2+8>0\). At \(L=2\), \(6d_2=b_2=2/3\), hence \(d_2=1/9>0\). Inductively, when \(L\) is even, the recurrence has positive forcing \(b_L=h_L\) and nonnegative earlier differences, so \(d_L>0\). When \(L\) is odd, the immediately preceding even recurrence yields \((L+3)d_{L-1}\ge h_{L-1}>h_L\); therefore the negative forcing \(-h_L\) is more than compensated and \(d_L>0\). This proves the infinite strict family.

**Sharpness below seven vertices.** Every labeled tree on \(n\ge2\) vertices is generated exactly once by a Prüfer word in \(\{0,\ldots,n-1\}^{n-2}\). The standalone checker exhaustively enumerates all such words for \(n=4,5,6\), every ordered pair of nonleaf vertices with a bare connecting path, and the corresponding proper KC shift. It computes both expected matching sizes as exact fractions using the first-edge recurrence, not simulation. The exhaustive comparison totals are: \(24\) negative and no zero/positive shifts at order \(4\); \(480\) negative and no zero/positive at order \(5\); and \(6180\) negative, \(2160\) zero, and no positive at order \(6\). At orders at most three there is no proper shift. Thus the seven-vertex positive example is minimal. Finally, \(P_4\) has \(p_4=5/3\), whereas every greedy matching in the star has size one, proving failure of monotonicity in the opposite direction too.

## Verification

The standalone stdlib-only file `checker.py` evaluates expected greedy matching sizes by exact rational edge-subset recurrence, independently enumerates all edge orders for the two seven-vertex witnesses and for the eight-vertex analogues, and verifies the spider/path identities for \(2\le L\le11\). It independently enumerates all \(16\), \(125\), and \(1296\) labeled trees on respectively \(4\), \(5\), and \(6\) vertices by Prüfer words and all proper KC shifts. Execution: `python3 checker.py`. The finite computations support the exact small-order certificate and spot-check the infinite proof; finite tests are not offered as proof of the infinite sign.

## Relationship to prior work

Krivelevich, Mészáros, Michaeli, and Shikhelman develop random-order greedy independent sets and KC transformations on trees, proving a global path-minimization result for **vertex** greedy independent sets and discussing their putative monotonicity under individual shifts. Their vertex statistic is not the present edge-matching statistic; the line graph of a tree need not be a tree. Dyer and Frieze investigate the same random-feasible-edge matching algorithm and give worst-case approximation guarantees for forests, but that guarantee does not determine the direction of one KC shift. Dyer, Frieze and Pittel study the same algorithm mainly on random sparse input graphs and random labeled trees, not fixed path-to-spider shifts. These distinctions do not establish historical uniqueness of the present result.

## Limitations

The infinite inequality applies only to the three-arm family \(S(2,2,L)\) and its specified path precursor. The finite sharpness result covers all trees of order at most six, but the work does not classify all larger positive shifts or the globally extremal tree at any given size. The 1991 Dyer–Frieze article was available in publisher abstract form but not in full, leaving some historical-priority uncertainty. No independent mathematical audit has been performed.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216 (first public 2019-07-16), https://arxiv.org/abs/1907.07216 ; doi:10.1002/rsa.21200.
2. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45, https://doi.org/10.1002/rsa.3240020104.
3. M. Dyer, A. Frieze and B. Pittel, *The average performance of the greedy matching algorithm*, Annals of Applied Probability 3 (1993), 526–552, https://doi.org/10.1214/aoap/1177005436.
4. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: exact results and finite girth corrections*, Combinatorics, Probability and Computing 19 (2010), 61–85, https://dspace.mit.edu/entities/publication/36eae796-81ba-4fbd-980d-445c69cd9f2a.
