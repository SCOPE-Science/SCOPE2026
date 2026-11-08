# Parity bifurcation of majority clocks on crown graphs

## Finding

For every integer \(n\ge3\), let \(\operatorname{Cr}_n\) be the connected crown graph obtained from the complete bipartite graph on \(\{a_1,\ldots,a_n\}\) and \(\{b_1,\ldots,b_n\}\) by deleting every matching edge \(a_i b_i\). Under simultaneous binary strict open-neighbor majority, with ties retaining the vertex's previous state, define \(T(x)\) as the least nonnegative time at which the state is periodic, and \(p(x)\) as its eventual least period. The only possible eventual periods are one and two. The following formulas count **labelled configurations** with each \((T,p)\).

**Even order parameter.** If \(n=2k\ge4\), put \(C=\binom{n}{k}\) and \(L=(2^n-C)/2\). All other temporal classes vanish, and
\[
\begin{aligned}
N_{0,1}&=C+2,&N_{0,2}&=(C+2)(C+1),\\
N_{1,1}&=2L^2-2,&N_{1,2}&=4^n-(C+2)^2-(2L^2-2).
\end{aligned}
\]
The sharp maximum of \(T\) is one.

**Odd order parameter.** If \(n=2k+1\ge3\), put \(C=\binom{n}{k}\), \(L=2^{n-1}-C\), and
\[
B=\frac{4^n}{2}-2C\bigl[(k+2)(2^{k+1}-k-1)-1\bigr].
\]
Here \(B\) is the exact population whose eventual period is two. All nonzero temporal classes are
\[
\begin{aligned}
N_{0,1}&=2+2(k+2)C, &N_{0,2}&=2,\\
N_{1,1}&=2L^2-2+4C(2^k-1)+2C[1+k(k+1)], &N_{1,2}&=2L^2-2,\\
N_{2,2}&=B-2L^2,&N_{3,1}&=4C(k+1)(2^k-k-1),\\
N_{2,1}&=4^n-N_{0,1}-N_{0,2}-N_{1,1}-N_{1,2}-N_{2,2}-N_{3,1}.
\end{aligned}
\]
There is exactly **one** primitive two-cycle, exchanging the two opposite unanimous-side configurations; it attracts exactly \(B\) initial configurations. The sharp maximum of \(T\) is two at \(n=3\), and three for all odd \(n\ge5\). Every configuration requiring all three updates converges to a fixed point.

The immediately periodic fraction undergoes a striking parity change: as \(n\to\infty\) along the respective parity subsequences,
\[
\Pr(T=0)\sim\begin{cases}2/(\pi n),&n\ \text{even},\\ \sqrt{2n/\pi}\,2^{-n},&n\ \text{odd}.\end{cases}
\]
For odd \(n\), the eventual two-cycle basin probability is \(B/4^n=1/2-O(\sqrt n\,2^{-n/2})\), while for even \(n\) the eventual two-cycle basin fraction tends to \(1/2\).

## Assumptions and scope

The graph is simple, undirected and connected; the deleted matching contains all \(n\) diagonal edges. Each vertex has degree \(n-1\). The two labelled sides have \(n\) binary coordinates each. For a configuration \((a,b)\), write \(|a|=A\), \(|b|=B_0\); the symbol \(B_0\) for the right-side weight is distinct from the eventual two-cycle basin count \(B\) in the theorem. At every update, a vertex chooses one if more than half of its neighbors are one, zero if fewer than half are one, and otherwise retains its current bit. First-entry time zero means the initial configuration itself belongs to a periodic orbit. Cycle counts, rather than periodic-state counts, are half of the corresponding period-two-state populations. All formulas apply to every integer \(n\) in the stated ranges, not merely the verified finite cases.

## Proof

**Local response.** At the paired index \(i\), the left vertex sees \(B_0-b_i\) ones; the right vertex sees \(A-a_i\) ones. This identity follows immediately because its only absent opposite-side neighbor is its matched partner.

**Even case.** When \(n=2k\), the degree is odd, so there are no ties. Define \(R(w)=0^n\) for \(|w|<k\), \(R(w)=\bar w\) for \(|w|=k\), and \(R(w)=1^n\) for \(|w|>k\). The full update is \(F(a,b)=(R(b),R(a))\). Its image is \(S^2\), where \(S=\{0^n,1^n\}\cup\{w:|w|=k\}\). On \(S\), \(R\) is an involution; hence \(F^2\) is the identity on \(S^2\), proving the exact one-step bound. Every point of \(S^2\) is periodic, so there are \((C+2)^2\) such points. A fixed point has \(b=R(a)\) with arbitrary \(a\in S\), giving \(C+2\) fixed points; all other periodic points form two-cycles. To count all states whose **first image** is fixed, the initial words must both have weight less than \(k\), both have weight greater than \(k\), or be balanced complements of one another. There are \(2L^2+C\) such states. Subtract \(C+2\) initially fixed states for \(N_{1,1}\), and subtract the remaining initially periodic and first-step fixed populations from \(4^n\) for \(N_{1,2}\). Positive \(N_{1,1}\) establishes sharpness for \(n\ge4\).

**Odd case: a complete four-band transition analysis.** Let \(n=2k+1\). Partition possible weights into \(\mathrm L=\{0,\ldots,k-1\}\), \(\mathrm M=\{k\}\), \(\mathrm P=\{k+1\}\), and \(\mathrm H=\{k+2,\ldots,n\}\). The left-side response, with current pair \((a,b)\), is
\[
 a'=\begin{cases}0^n,&|b|\in\mathrm L,\\ a\land\bar b,&|b|=k,\\a\lor\bar b,&|b|=k+1,\\1^n,&|b|\in\mathrm H.\end{cases}
\]
The right response is the same formula with the two sides exchanged. Let \(z=|a\land b|\). The following case analysis, with the cases obtained by swapping sides or complementing all bits included, is exhaustive:

* Both side weights low (or both high) yield the corresponding unanimous fixed point after one update. A low/high pair yields the alternating unanimous-side two-cycle after at most one update.
* Low/middle (or high/upper-middle) yields a fixed point within two steps; its first image is fixed precisely when the low-side ones are contained in the middle-side ones (or the complementary inclusion).
* Low/upper-middle yields first-image weight \(k+z\) on the low side and zero on the other. If \(z=0\), it becomes zero at step two; if \(z=1\), at step three; if \(z\ge2\), it reaches the unanimous-side two-cycle at step two. The complemented case is middle/high.
* Middle/middle yields a fixed point immediately when \(z=0\); otherwise it reaches zero by step two. Upper-middle/upper-middle is the complementary case, fixed immediately when \(z=1\), and otherwise reaches one by step two.
* Middle/upper-middle yields complementary sides after one step, with weights \(k+z\) and \(k+1-z\). It is fixed initially for \(z=0\), fixed after one step for \(z=1\), and enters the unanimous-side two-cycle after two steps for \(z\ge2\). The swapped case is symmetric.

For the low/upper-middle case, the first image's low-side weight is \(k+z\) because \(|\bar b|=k\) and the added overlap is \(z\). For the middle/high case, the first image is \((1^n,b\land\bar a)\); writing \(t=|b\land\bar a|\), it goes to the two-cycle at time two for \(t<k\), to the all-ones fixed point at time three for \(t=k\), and to it at time two for \(t>k\). This verifies the complement of the preceding statement, including every boundary. The case partition proves directly that there are no eventual periods beyond one and two, and that every entry time is at most three.

**Odd case: counting periodic states.** Fixed points comprise the two globally unanimous states; \(\mathrm M/\mathrm M\) states with disjoint side supports; \(\mathrm P/\mathrm P\) states with union all \(n\) matched positions; and complementary \(\mathrm M/\mathrm P\) or \(\mathrm P/\mathrm M\) states. Put \(C=\binom nk\). The respective populations are \(2\), \((k+1)C\), \((k+1)C\), \(C\), \(C\); thus \(N_{0,1}=2+2(k+2)C\). The only primitive two-cycle alternates \((0^n,1^n)\) and \((1^n,0^n)\), so \(N_{0,2}=2\).

**Odd case: entry-time populations.** The number of words of low weight is \(L=\sum_{j=0}^{k-1}\binom nj=2^{n-1}-C\); there are also \(L\) of high weight. The low/high and high/low bands give \(2L^2-2\) noninitial, one-step entries to the two-cycle. The first-update-fixed population beyond the two already fixed unanimous states is the disjoint sum of: \(2L^2-2\) from the low/low and high/high bands; \(4C(2^k-1)\) from the low/middle and upper-middle/high inclusion cases and their swaps; \(2C\) from coincident middle/middle or upper-middle/upper-middle supports; and \(2Ck(k+1)\) from middle/upper-middle overlap of size one and its swap. This proves \(N_{1,1}\).

To count two-step entries to the two-cycle, first use the low/upper-middle region with overlap at least two. Choosing the upper-middle side first gives \(C\) possibilities and, for each, the admissible low-side subsets number
\[
H=L-(2^k-1)-(k+1)(2^k-k-1)
  =L-(k+2)2^k+1+(k+1)^2.
\]
Its complemented and swapped regions contribute altogether \(4CH\). In the middle/upper-middle region, overlap at least two gives
\[
C\sum_{z=2}^{k}\binom{k}{z}\binom{k+1}{z}=C\bigl[C-1-k(k+1)\bigr]
\]
by Vandermonde's identity; its swapped region doubles this. Thus \(N_{2,2}=4CH+2C[C-1-k(k+1)]\). Adding \(2L^2\) initially or first-step period-two states and substituting \(L=2^{n-1}-C\) simplifies the eventual period-two basin count to exactly \(B\) above.

Three-step entries occur precisely in the low/upper-middle region with overlap one, the middle/high region with exactly \(k\) unpaired right-side ones, and their side swaps. Each of the four regions contributes
\[
C(k+1)\sum_{j=0}^{k-2}\binom kj=C(k+1)(2^k-k-1).
\]
This proves \(N_{3,1}\) and, because there are no three-step two-cycle entries, the remaining \(N_{2,1}\) follows by subtracting from all \(4^n\) labelled states. At \(k=1\), \(N_{3,1}=0\) but \(N_{2,1}>0\). At \(k\ge2\), \(N_{3,1}>0\), proving the claimed sharp first-entry bounds.

**Asymptotics.** The central binomial estimate \(\binom{2k}{k}\sim4^k/\sqrt{\pi k}\) yields both immediately periodic probabilities. In the odd case the displayed closed formula for \(B\) gives \(B/4^n=1/2-O(\sqrt n\,2^{-n/2})\); in the even case the eventual fixed basin has size \(2L^2+C\), yielding a period-two basin fraction tending to \(1/2\). No probabilistic independence of updates is assumed.

## Verification

Two independent implementations test the formulas. `verify_exhaustive.cpp` directly enumerates all \(4^n\) labelled initial states for every \(3\le n\le10\), applies neighbor majority at each vertex, and determines the minimal periodic-entry time and eventual period. This covers \(1,398,080\) starting states across the eight sizes. `verify_pair_classes.py` instead enumerates the \(\binom{n+3}{3}\) classes of matched-pair patterns (00, 10, 01, 11), follows one representative in each, and weights by the exact multinomial orbit cardinality; it verifies the formulas for every \(3\le n\le26\). The outputs are saved as `exhaustive.out` and `pair_classes.out`. The finite tests corroborate but do not replace the preceding general proof.

To reproduce: compile `verify_exhaustive.cpp` with a C++17 compiler using `-O3`, then run it; invoke `python3 verify_pair_classes.py` with standard-library Python 3. Both terminate with a nonzero exception or return status on mismatch. The graph's order parameter is \(n\), not the number \(2n\) of vertices.

## Relationship to prior work

Goles and Olivos (1980) established the period-at-most-two theorem for symmetric binary threshold networks. The present period bound is also proved directly rather than represented as new in isolation. Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1, August 14, 2015) developed general and symmetry-sensitive voting-time bounds and hardness results, but do not give the exact crown-graph parity dichotomy or any of the joint populations above; their full manuscript was accessed and its definitions, main bounds, family reductions and relevant appendix statements were inspected. Agur, Fraenkel and Klein (1988) counted fixed points for one-dimensional cyclic three-neighbor majority, a different graph and local rule; their complete accessible paper was inspected. Available mathematical searches did not identify an earlier statement implying the present classification. Separate graph-theoretic results concerning crown-graph colorings and domination do not address this majority dynamical map.

## Limitations

The conclusions require the complete bipartite graph with all matched cross-edges deleted, exactly synchronous open-neighbor majority, and tie retention; they do not automatically extend to partial matchings, asynchronous updates, stochastic voting, or other thresholds. Published earlier work may contain an equivalent but unindexed special-case calculation. The historical Goles--Olivos full text was not accessible in the available reading environment; its established general period bound is fully credited. No independent audit has been performed. Finite computations are checks, not an infinite proof.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, DOI 10.1016/0012-365X(80)90121-1 (historical result; only bibliographic/abstract material was accessible).
2. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1, August 14, 2015, https://arxiv.org/pdf/1508.03519 (full manuscript inspected).
3. Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics **70** (1988), 295–302, https://u.cs.biu.ac.il/~tomi/Postscripts/majority.pdf (full text inspected; cyclic one-dimensional majority).
