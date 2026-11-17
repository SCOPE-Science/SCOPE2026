# Additive-balance resonance and exponential two-cycle multiplicity on distinct-shore majority graphs

## Finding
For every integer \(k\ge1\), let \(G_k=K_{2k,3k,4k,7k}\) be a complete four-partite graph whose vertices and four independent parts are labelled. Under synchronous strict open-neighbor binary majority dynamics with tie retention, let \(F_k\) denote the update. Then the **exact number of distinct primitive temporal two-cycle orbits** is
\[
\boxed{O_k=2^{2k}.}
\]
Every such orbit has a unique description: the part of size \(2k\) holds an arbitrary frozen binary word, the parts of sizes \(3k\) and \(4k\) synchronously switch between all zero and all one, and the part of size \(7k\) switches in the opposite phase. Each labelled word in the first part corresponds to one distinct unoriented two-cycle, including its two homogeneous words.

The number of initially fixed configurations is
\[
\boxed{P_k=2+\mathbf1_{2\mid k}\binom{2k}{k}\binom{3k}{3k/2}\binom{4k}{2k}\binom{7k}{7k/2}.}
\]
The product is omitted entirely when \(k\) is odd, so no noninteger lower binomial arguments occur. The only fixed states for odd \(k\) are the two unanimous words. Every trajectory eventually reaches a fixed configuration or a two-cycle. Consequently, for each positive integer \(t\),
\[
\#\operatorname{Fix}(F_k^t)=\begin{cases}P_k,&t\text{ odd},\\P_k+2^{2k+1},&t\text{ even},\end{cases}
\]
and the dynamical zeta function is \(\zeta_{F_k}(z)=(1-z)^{-P_k}(1-z^2)^{-2^{2k}}\) as a formal series.

For example, the respective pairs (fixed configurations, distinct two-cycle orbits) at \(k=1,2,3,4\) are \((2,4)\), \((28{,}828{,}802,16)\), \((2,64)\), and \((33{,}394{,}325{,}524{,}560{,}002,256)\). The parts are **pairwise unequal for every \(k\)**. By contrast, the established complete tripartite classification admits precisely one primitive two-cycle for three pairwise unequal part sizes. The additional part permits a balance \(3k+4k=7k\) that creates an exponentially large frozen-word degree of freedom.

## Assumptions and scope
Here \(K_{2k,3k,4k,7k}\) has four nonempty independent vertex classes; every two vertices from different classes are adjacent, and vertices within one class have no edge. Each vertex has bit \(0\) or \(1\). All updates are simultaneous: set the bit to one if strictly more than half its neighbors are one, zero if strictly fewer, and otherwise preserve its own prior bit. The labels on individual vertices matter. A primitive temporal two-cycle orbit is an unordered pair \(\{x,y\}\) with \(x\ne y=F_k(x)\) and \(F_k(y)=x\); the two configurations are counted as one orbit. A fixed state is \(x=F_k(x)\). The theorem covers every integer \(k\ge1\), including parity boundaries and nonuniform words within the first part; it does not classify transient-basin sizes or exact settling times.

## Proof
**1. Neighbor-sum equations.** Index the four parts by \(i=1,2,3,4\), with cardinalities \((n_1,n_2,n_3,n_4)=(2k,3k,4k,7k)\). In a state, let \(s_i\) denote the number of ones in part \(i\), \(N=16k\) the total number of vertices and \(S=\sum_i s_i\). Every vertex of part \(i\) has exactly \(S-s_i\) one-neighbors among its \(N-n_i\) neighbors. Accordingly, its entire part becomes all one if \(2(S-s_i)>N-n_i\), becomes all zero if this inequality is reversed, and retains its exact word if equality holds. Therefore a part that becomes homogeneous remains homogeneous at all subsequent times. A part that is mixed on a recurrent orbit is necessarily the same mixed word at every step and experiences an exact tie in every phase.

Write \(\delta_i=2s_i-n_i\) for the signed occupancy of part \(i\), and \(\Delta=\sum_i\delta_i\) for the total signed occupancy. The neighborhood signed sum at a vertex of part \(i\) is \(\Delta-\delta_i\). Any mixed part that persists through periodic updates must satisfy \(\delta_i=\Delta\). A homogeneous part with bit-sign \(\epsilon_i\in\{-1,+1\}\) has \(\delta_i=\epsilon_i n_i\); it stays homogeneous with its sign if \(\epsilon_i\Delta\ge n_i\), and flips its sign if \(\epsilon_i\Delta<n_i\) and the neighborhood signed sum has the opposite sign. The latter condition for flipping a homogeneous part is equivalently \(\epsilon_i\Delta<n_i\), because its neighbor sum is \(\Delta-\epsilon_i n_i\).

**2. Fixed states.** A fixed configuration with at least one mixed part has \(m\ge1\) mixed parts, all with \(\delta_i=\Delta\). Every homogeneous part that remains fixed must have \(\epsilon_i\Delta\ge n_i>0\), so if any such part exists then \(\Delta\ne0\) and all homogeneous signs equal the sign of \(\Delta\). Summing signed occupancies yields
\[
(1-m)\Delta=\sum_{\text{homogeneous }i}\epsilon_i n_i.
\]
For \(m=1\), the left side is zero but the right side is nonzero; for \(m>1\), the left side has the opposite sign to the right side. Both are contradictions. Hence any fixed state with a mixed part has **all four** parts mixed. The tie conditions force \(\Delta=4\Delta\), hence \(\Delta=0\) and \(\delta_i=0\) in all four parts. This requires each \(n_i\) even, equivalently \(k\) even, and permits exactly \(\prod_i\binom{n_i}{n_i/2}\) labelled configurations. If no part is mixed but the homogeneous signs are not unanimous, at least one all-one and one all-zero part must remain fixed. Their respective stability inequalities require \(\Delta\ge n_i>0\) and \(-\Delta\ge n_j>0\), impossible. Only the two unanimous homogeneous states remain fixed.

**3. Two-cycles with mixed parts.** On a genuine two-cycle every mixed part retains its word through both phases. Let \(m\ge1\) be their count and \(d\) the common signed occupancy of each. In both phases \(\Delta=d\). Any homogeneous part that stays frozen over both phases would need \(\epsilon_i d\ge n_i>0\). Thus all such frozen homogeneous signs would match the sign of \(d\). Summing the signed occupancies over the two phases gives
\[
(1-m)d=\sum_{\text{frozen homogeneous }i}\epsilon_i n_i,
\]
because all flipping homogeneous parts cancel upon taking the phase average. If any frozen homogeneous part existed, the equation would contradict signs when \(m>1\), or contradict zero versus nonzero when \(m=1\). Thus every homogeneous part flips in a genuine two-cycle containing a mixed part. The total signed occupancy must stay equal to \(d\), so the sizes of the positively and negatively flipping homogeneous parts must sum to the same value. The four sizes \(2k,3k,4k,7k\) are distinct, and the only equality between nonempty disjoint subsets of these numbers with at least two members overall is
\[
3k+4k=7k.
\]
Therefore the only possibility is one mixed part of size \(2k\), with the three other parts oscillating as the two groups \(\{3k,4k\}\) and \(\{7k\}\), in opposite phase. The mixed part has any signed occupancy \(d\in[-2k,2k]\). Since \(|d|\le2k<3k\), each of the three pure parts sees a strict opposite-majority vote and switches every phase. Thus **every labelled binary word on the \(2k\)-vertex part** works, and each determines precisely one unoriented orbit. There are \(2^{2k}\) such words.

**4. All-homogeneous cycles.** We must also exclude any other two-cycle with no mixed parts. Encode a homogeneous configuration by four bits ordered by part size \(2k,3k,4k,7k\). The update depends only on the size ratios \((2,3,4,7)\) and not on \(k\). A direct evaluation of the four strict-neighbor majority tests gives the following complete one-step transition table, with inputs written as four-bit words:

| Input | Output | Input | Output |
|---|---|---|---|
| 0000 | 0000 | 1000 | 0000 |
| 0001 | 0110 | 1001 | 1110 |
| 0010 | 0000 | 1010 | 0001 |
| 0011 | 1110 | 1011 | 1111 |
| 0100 | 0000 | 1100 | 0001 |
| 0101 | 1110 | 1101 | 1111 |
| 0110 | 0001 | 1110 | 1001 |
| 0111 | 1111 | 1111 | 1111 |

The only genuine two-cycle pairs in this table are \(\{0001,0110\}\) and \(\{1001,1110\}\). These are already included in the family from Step 3, corresponding respectively to the all-zero and all-one words in the first part. (The state classification from Step 3 assumed a mixed first part; here we explicitly add its homogeneous endpoints.) Therefore the precise orbit count is \(2^{2k}\) and there are no additional classes.

**5. No recurrent periods longer than two.** For general finite undirected graphs, represent bits as spins \(\sigma\in\{-1,+1\}^N\) and let \(A\) be the symmetric adjacency matrix. Set \(W=A+\frac12I\). Every coordinate of \(W\sigma\) is a nonzero half-integer; its sign implements neighbor-majority with tie retention. The new spin vector \(\sigma'\) is the unique coordinatewise maximizer of \(\tau^T W\sigma\) over all spin vectors \(\tau\). Consequently, along any trajectory, \(Q_t=\sigma(t+1)^TW\sigma(t)\) satisfies
\[
Q_t=\sigma(t)^TW\sigma(t+1)\ge \sigma(t-1)^TW\sigma(t+1)=Q_{t-1},
\]
with strict inequality whenever \(\sigma(t+1)\ne\sigma(t-1)\). Since \(Q_t\) takes finitely many values, eventually \(\sigma(t+1)=\sigma(t-1)\). All eventual orbits therefore have period at most two. Every fixed point contributes to every iterate's fixed set, and every primitive two-cycle contributes two points for even iterates. The periodic-point and zeta formulas follow.

## Verification
The reproducible standard-library script `verify.py` gives two independent finite checks. First it applies the full part-population update to all \(\prod_i(n_i+1)\) possible part-count vectors, weighting them by the multinomial number of labelled words, for each \(1\le k\le7\); the measured fixed-state and primitive-two-orbit populations agree with the formulas. Second it builds the actual 16-vertex neighbor graph for \(k=1\) and exhaustively iterates all \(65{,}536\) labelled binary configurations, reproducing exactly two fixed states and four primitive two-cycle orbits. It also checks directly that the proposed oscillation family satisfies the two-cycle relation through \(k=4\), for all possible frozen occupancy counts. Run `python3 verify.py` and compare with `verify-output.txt`. These finite checks corroborate but do not prove the all-parameter classification; the exhaustive sign and subset-balance arguments above establish it.

## Relationship to prior work
The general eventual-period-at-most-two fact for finite symmetric threshold dynamics goes back to Goles and Olivos [1,8]; it is used here only as a dynamical restriction. Adams, Brass, Stokes and Troxell [2] study irreversible conversion thresholds on complete multipartite graphs, not the reversible time-periodic orbit counts of tie-preserving majority. Benjamini and colleagues [3] address convergence and disagreement on unimodular and random graphs. Turau [4] studies synchronous dynamic colorings on trees. None directly provides the present distinct-size four-part census.

The closest accessible complete tripartite periodic-state result [5] already shows that three **pairwise distinct** part sizes have precisely one primitive temporal two-cycle; it is not claimed new. A balanced complete multipartite counting theorem [6] and a separate all-balanced recurrence theorem [7] both require **equal part sizes**, and explicitly do not establish counts for arbitrary unequal parts. The present four-part family is unequal for every scale and exhibits an additive-balance mechanism unavailable with three distinct parts. The first member \(K_{2,3,4,7}\) is the smallest strictly increasing integer four-part tuple with a nontrivially mixed smallest part and a disjoint balance of the other three with smallest flipping part larger than the frozen part; scaling preserves the mechanism and makes its orbit count exponential. The contribution is not a general arbitrary-four-part classification, a rephrasing of [5]–[7], or an enumeration of attraction basins.

## Limitations
The theorem concerns the explicit graph family \(K_{2k,3k,4k,7k}\) under synchronous binary strict-neighbor majority with incumbent tie retention, and counts only initially periodic states/orbits, not transient basins or exact transient depths. The general period-two property is classical, not newly claimed. A broader historical threshold-network classification might imply this special exact count, and independent priority certification is not available. The full original 1980 article [1] was not accessible during source inspection, although the article abstract and subsequent expositions establish its general periodicity result. Numerical checking through \(k=7\) is not a substitute for the infinite proof.

## References
[1] E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* 30 (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.

[2] N. Adams, P. Brass, C. Stokes and D. Troxell, “Irreversible k-threshold and majority conversion processes on complete multipartite graphs and graph products,” arXiv:1102.5361v1, first publicly posted 2011-02-25. https://arxiv.org/abs/1102.5361.

[3] I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486v1, first publicly posted 2014-05-11. https://arxiv.org/abs/1405.2486.

[4] V. Turau, “Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees,” arXiv:2202.01580v1. https://arxiv.org/abs/2202.01580.

[5] “Exact periodic-orbit census for tie-retaining majority on complete tripartite graphs,” published research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-periodic-orbit-census-for-tie-retaining-majority-on-comple--131a77706642.

[6] “Parity-controlled fixed points and two-cycles in balanced multipartite majority dynamics,” published research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parity-controlled-fixed-points-and-two-cycles-in-balanced-multip--5eb2f6d50308.

[7] “Parity-selective recurrent majority dynamics on balanced complete multipartite graphs,” published research record, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-parity-selective-recurrent-majority-dynamics-on-balanced-complet--6279dfb842f9.

[8] E. Goles and J. Olivos, “Comportement périodique des fonctions à seuil binaires et applications,” *Discrete Applied Mathematics* 3 (1981), 93–105. DOI: 10.1016/0166-218X(81)90034-2.
