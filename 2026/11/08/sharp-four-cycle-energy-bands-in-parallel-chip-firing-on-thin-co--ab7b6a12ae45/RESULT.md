# Sharp four-cycle energy bands in parallel chip-firing on thin complete bipartite graphs

## Finding

For every integer \(b\ge 3\), consider synchronous parallel chip-firing on the labelled complete bipartite graph \(K_{2,b}\). Denote by \(H_b(z)\) the polynomial whose coefficient at \(z^m\) is the number of *initially periodic configurations of least period four* with exactly \(m\) chips. Put
\[
S_b(z)=\sum_{r=1}^{b-1}\binom br(1+z+\cdots+z^{r-1})(1+z+\cdots+z^{b-r-1}).
\]
Then
\[
\boxed{H_b(z)=4z^{2b}S_b(z)+4z^{5b-2}S_b(z^{-1}),\qquad
(1-z)^2S_b(z)=2^b(1+z^b)-2(1+z)^b.}
\]
The negative exponents in the second summand cancel: the displayed expression is an ordinary polynomial. The exact set of chip totals admitting a least-period-four state is
\[
\boxed{\{2b,\ldots,3b-2\}\ \cup\ \{4b,\ldots,5b-2\}.}
\]
Each listed total occurs. In particular, the universal middle-stair boundary totals \(2|E|-|V|=3b-2\) and \(2|E|=4b\) *both* admit least-period-four configurations, exactly \(4(2^b-2)\) each; none occur at the intervening totals. Summing coefficients gives exactly \(2^{b+1}b(b-1)\) primitive-four **configurations**, hence \(2^{b-1}b(b-1)\) distinct primitive-four **orbits**. Half of the primitive-four configurations have firing activity \(1/4\), half activity \(3/4\).

## Assumptions and scope

Vertices hold nonnegative integer chips. In a simultaneous update, a vertex with at least its degree in chips sends exactly one chip to each neighbor; other vertices send none. The two vertices on one side of \(K_{2,b}\) are labelled \(L_1,L_2\), have degree \(b\), and the \(b\) individually labelled vertices on the other side have degree two. A least-period-four configuration \(\sigma\) satisfies \(U^4\sigma=\sigma\) and \(U^2\sigma\ne\sigma\). Total mass is conserved. Activity means the fraction of rounds in one period in which any specified vertex fires (the fraction is common to all vertices). The theorem counts configurations on their cycles, not configurations eventually entering those cycles, and does not classify fixed points or two-cycles.

## Proof

**1. Restrict firing words.** Jiang [1, Proposition 2.5] proves that in a periodic chip-firing trajectory on a connected graph, every vertex fires equally many times during a complete period. The non-clumpiness theorem of Jiang, Scully and Zhang [2, Theorem 6.2] says that a periodic vertex firing word cannot contain both a pair of consecutive firings and a pair of consecutive nonfirings, considered cyclically. A primitive-four state therefore has a common number \(k\in\{1,2,3\}\) of firings per four rounds. If \(k=0\) or \(k=4\), the state is fixed. For \(k=2\), non-clumpiness forces each four-letter firing word to alternate. Each vertex then fires exactly once in any two consecutive rounds, so the net two-round chip transport along each edge vanishes and \(U^2\sigma=\sigma\), contradicting primitivity. Thus \(k=1\) or \(k=3\).

**2. The possible one-firing phases.** Assume \(k=1\). Each of \(L_1,L_2\) fires once in four rounds. If they fire simultaneously, choose that time as round zero. Every right-side vertex then must fire at round one: with incoming pattern \((2,0,0,0)\), exactly one firing per period requires its starting chip number to be zero or one, and its firing occurs in round one. Both left vertices regain \(b\) chips before round two, hence must fire again, impossible. If the two left firings are adjacent, choose them at rounds zero and one. With right-side incoming pattern \((1,1,0,0)\), one firing per period requires each right vertex initially to carry zero or one chips, so no right vertex fires in round zero. The left vertex scheduled to fire at round one was below threshold at round zero and gained no chips, impossible. Interchanging labels and rotating time covers all simultaneous and adjacent cases. The two left firings must therefore occur two rounds apart.

**3. Enumerate all opposite-phase states.** Fix a phase with \(L_1\) firing in round zero and \(L_2\) in round two. Each right vertex receives one chip in rounds zero and two. It starts with zero or one chips: a right vertex initially at one fires in round one, whereas one initially at zero fires in round three. Let \(r\) be the number of right vertices initially at zero. Thus the numbers of right firings over rounds zero through three are \((0,b-r,0,r)\). Write the initial chips on the left as \(\alpha,\beta\). Directly applying their threshold inequalities and chip balances yields
\[
1\le r\le b-1,\qquad b\le\alpha\le b+r-1,\qquad r\le\beta\le b-1.
\]
Conversely these inequalities imply the required four-round firing pattern and exact return, without any other firing. Set \(\alpha=b+i\), \(\beta=r+j\), with \(0\le i<r\), \(0\le j<b-r\). Since \(b-r\) right vertices begin with one chip, the total mass equals \(2b+i+j\). For fixed \(r,i,j\), the right-side labelling has \(\binom br\) choices. Choosing the firing phase of the labelled vertex \(L_1\) gives exactly four distinct initial states. Hence all \(k=1\) primitive-four states have enumerator \(4z^{2b}S_b(z)\).

**4. Complementary three-firing states.** The confined-state complement from Jiang [1, Lemma 2.3], \(\sigma^c(v)=2\deg(v)-1-\sigma(v)\), conjugates the update on periodic states and exchanges firing with nonfiring. Every nonfixed periodic state is confined by Jiang [1, Lemmas 2.1–2.2], hence \(0\le\sigma(v)\le 2\deg(v)-1\). This confinement result is essential: a large chip count at one time by itself does not imply perpetual firing. The total capacity \(\sum_v(2\deg(v)-1)\) is \(7b-2\), so complementary mass is \(7b-2-m\). Complementation bijects all \(k=1\) and \(k=3\) states. This proves the first polynomial identity.

**5. Polynomial simplification and sharp support.** Writing each short geometric sum as \((1-z^r)/(1-z)\) and using the binomial theorem gives
\[
(1-z)^2S_b(z)=\sum_{r=1}^{b-1}\binom br(1-z^r)(1-z^{b-r})=2^b(1+z^b)-2(1+z)^b.
\]
Every coefficient of \(S_b\) in degrees zero through \(b-2\) is positive: already \(r=1\) supplies all those degrees. Its first and last coefficients each equal \(\sum_{r=1}^{b-1}\binom br=2^b-2\). Thus low masses are all integers from \(2b\) to \(3b-2\) and high masses all integers from \(4b\) to \(5b-2\), with the claimed exact endpoint counts. Finally
\[
S_b(1)=\sum_{r=1}^{b-1}\binom br r(b-r)=b(b-1)2^{b-2}.
\]
Multiplication by the two four-phase contributions gives \(H_b(1)=2^{b+1}b(b-1)\). Each primitive orbit has four states, giving the orbit count. The firing totals \(k=1,3\) supply the two equal activity classes. This completes the proof.

## Verification

Three standalone Python 3 programs included with this result run without external libraries. `verification/verify_bruteforce.py` directly iterates all bounded labelled configurations for \(2\le b\le7\), checks exact four-step return and failure of two-step return, and compares every mass coefficient. It examines \(3,211,264\) configurations at \(b=7\). `verification/verify_histogram.py` independently enumerates right-side chip histograms with exact multinomial weights through \(b=12\). `verification/verify_formula.py` checks the polynomial coefficient identity, boundary counts, support and orbit total for all \(2\le b\le50\). All three succeeded when executed from the included code; their captured outputs are included. These finite checks supplement, rather than replace, the all-parameter proof.

## Relationship to prior work

Jiang [1] classified possible period lengths on complete bipartite graphs; in particular, period four is possible on \(K_{2,b}\). That work supplies a firing-count lemma and a complement lemma but does not supply the distribution of primitive-four states by total chips. Jiang, Scully and Zhang [2] proved the non-clumpiness restriction used to exclude two firings per four rounds. Ji, Li and Wang [3] excluded periods three and four in the *open* universal middle-stair interval; Jung [4] proved period two in that open interval for all complete bipartite graphs. These statements do not determine whether period four occurs at either boundary, its exact multiplicities, or its full mass-generating function. The present theorem determines both endpoints and the complete distribution. Levine [5] studied the activity staircase on complete graphs, not the enumerator for \(K_{2,b}\). Relevant database and literature comparisons revealed no equivalent primitive-four energy census, but that absence is not proof of historical novelty.

## Limitations

The result concerns the labelled family \(K_{2,b}\) with \(b\ge3\), not arbitrary complete bipartite or general graphs; it counts periodic configurations, not transient basin sizes. It assumes deterministic synchronous threshold chip-firing with no dissipation. The principal source provides earlier period-existence results; the originality assessment concerns precisely the new energy-refined counts and boundary attainments. The possibility of earlier unindexed equivalent counting work remains open, and the complete 1992 Bitar–Goles article was not available for comparison. No independent mathematical audit has been conducted.

## References

[1] T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game* (first posted March 4, 2010), arXiv:1003.0943, https://arxiv.org/abs/1003.0943.

[2] T.-Y. Jiang, Z. Scully, Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game* (first posted November 29, 2012), arXiv:1211.6786, https://arxiv.org/abs/1211.6786.

[3] D. Ji, M. Li, D. Wang, *Non-Stabilizing Parallel Chip-Firing Games* (first posted August 20, 2024), arXiv:2408.10508, https://arxiv.org/abs/2408.10508.

[4] M. Jung, *The Middle Stair for Complete Bipartite Parallel Chip-Firing* (first posted August 2, 2026), arXiv:2608.01350, https://arxiv.org/abs/2608.01350.

[5] L. Levine, *Parallel Chip-Firing on the Complete Graph: Devil's Staircase and Poincaré Rotation Number* (first posted November 17, 2008), arXiv:0811.2800, https://arxiv.org/abs/0811.2800.
