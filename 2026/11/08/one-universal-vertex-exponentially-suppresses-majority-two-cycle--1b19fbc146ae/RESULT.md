# One universal vertex exponentially suppresses majority two-cycles on cocktail-party graphs

## Finding

For every integer \(n\ge2\), let \(C_n\) be the complete graph on \(2n\) labelled vertices with a perfect matching deleted, and let \(H_n\) be obtained from \(C_n\) by adjoining one vertex adjacent to every original vertex. Consider the synchronous binary strict majority map \(F\): at each vertex, take the majority of the states of its *open* neighbors, keeping the old state on a tie. Let \(P_1(G)\) and \(P_2(G)\) be the numbers of labelled configurations with least temporal period one and two, respectively, **starting at time zero**. Then

\[
\begin{aligned}
P_1(C_n)&=2+2^n, & P_2(C_n)&=\binom{2n}{n}-2^n,\\
P_1(H_n)&=2, & P_2(H_n)&=2\binom{n}{\lceil n/2\rceil}.
\end{aligned}
\]

Every configuration on \(C_n\) enters a periodic orbit by the first update; every configuration on \(H_n\) enters one by the second update. These bounds are sharp on \(C_n\) for every \(n\ge2\) and on \(H_n\) for every \(n\ge3\). No other temporal periods occur. Hence the primitive two-orbit counts are half the corresponding \(P_2\) values. If the starting state is independent uniformly random bits, its probability of immediate primitive two-periodicity satisfies

\[
\Pr_{C_n}(P_2)\sim\frac1{\sqrt{\pi n}},\qquad
\Pr_{H_n}(P_2)\sim 2^{-n}\sqrt{\frac2{\pi n}},\qquad
\frac{\Pr_{H_n}(P_2)}{\Pr_{C_n}(P_2)}\sim\sqrt2\,2^{-n}.
\]

Thus the addition of a single universal vertex reduces the immediate oscillation probability by an exponential factor while retaining symmetric majority updates.

## Assumptions and scope

The vertices of \(C_n\) are partitioned into \(n\) labelled complementary pairs \(\{a_i,b_i\}\). Each vertex sees all vertices except itself and its designated partner. The extra vertex of \(H_n\), denoted \(z\), is adjacent to the other \(2n\) vertices. The two binary opinions are encoded as \(0\) and \(1\). A strict local majority produces the majority bit; a tie does not change the vertex. The terms *periodic immediately*, *primitive two-periodic* and *first-entry time* refer to the finite deterministic map on the entire labelled bit configuration, without quotienting by graph symmetries. The first-entry time is the least \(t\ge0\) such that \(F^t(x)\) is on a periodic orbit.

## Proof

**Local count formula.** Write \(k\) for the total number of ones in a configuration and \(s_i\in\{0,1,2\}\) for the number of ones in the \(i\)-th complementary pair. A vertex in that pair has \(k-s_i\) neighbors in state one. On \(C_n\) its degree is \(2n-2\); on \(H_n\) its degree is \(2n-1\). The extra vertex of \(H_n\) has degree \(2n\) and sees \(k-c\) ones, where \(c\in\{0,1\}\) is its own state. All claims below follow from these exact formulas, including at ties.

**The even-order graph.** On \(C_n\), if \(k<n\), all vertices update to zero; if \(k>n\), all vertices update to one. At \(k=n\), each \(00\)-pair becomes \(11\), each \(11\)-pair becomes \(00\), and the two orientations of a mixed \(01\)-pair stay unchanged. Because the total number of ones is \(n\), the numbers of \(00\)- and \(11\)-pairs coincide. Hence \(k=n\) is invariant and every state in this central layer has period dividing two. The state is fixed exactly if every pair is mixed, giving \(2^n\) fixed central states. The two unanimous states are the other fixed states. All \(\binom{2n}{n}\) states in the central layer are periodic immediately, and every other state becomes unanimous after one update. This proves the first two counting identities and the sharp first-entry bound for \(C_n\).

**The odd-order graph.** On \(H_n\), if \(k<n\), the next state is unanimous zero; if \(k>n+1\), it is unanimous one. For \(k=n\), a paired block becomes \(11\) exactly when it was \(00\), and the central vertex becomes \(0\). For \(k=n+1\), a paired block becomes \(00\) exactly when it was \(11\), and the central vertex becomes \(1\). Thus after one update every pair is homogeneous, regardless of the initial state.

Take a configuration with homogeneous pairs and put \(b\) for the number of \(11\)-pairs and \(c\) for the central bit. Its number of ones is \(k=2b+c\). A non-unanimous state with such pairs is on a two-cycle **exactly when** \(k\in\{n,n+1\}\): at either of these two weights all pairs flip, while the central bit changes from \(c\) to \(0\) at weight \(n\), and to \(1\) at weight \(n+1\). The new total is \(n+c\), which again lies in \(\{n,n+1\}\), and the next update restores each pair and the central bit. In the case \(k=n\), the parity condition forces \(c\equiv n\pmod2\), and in the case \(k=n+1\) it forces \(c\equiv n+1\pmod2\); the two cycle phases are distinct. If instead \(k\notin\{n,n+1\}\), the state becomes unanimous at the next update. Consequently every orbit has entered a fixed point or two-cycle by time two. A state of period one or two must already have homogeneous pairs, since applying \(F\) makes every pair homogeneous. The only fixed states are the two unanimous ones, because each homogeneous middle-weight configuration flips all its pairs. When \(n\) is even, the two periodic middle-weight layers have respectively central bit zero or one and exactly \(n/2\) pairs of type \(11\). When \(n\) is odd, the layers have central bit one with \((n-1)/2\) pairs of type \(11\), or central bit zero with \((n+1)/2\) such pairs. In both parity cases their total number is \(2\binom{n}{\lceil n/2\rceil}\). All these states have primitive period two for \(n\ge2\).

For sharpness of the second-update bound at every \(n\ge3\), choose an initial \(H_n\)-configuration with central bit zero, one pair \(00\), one pair \(11\), and the other \(n-2\) pairs mixed. Its initial weight is \(n\); after one update it has exactly one pair \(11\), total weight two, and all other vertices zero. It is not periodic then, and the next update makes it unanimously zero. For \(n=2\), the bound two remains valid but not sharp.

**Probability asymptotics.** There are \(2^{2n}\) equally likely states on \(C_n\) and \(2^{2n+1}\) on \(H_n\). Divide the respective primitive-two populations by these numbers. The central-binomial estimates \(\binom{2n}{n}\sim4^n/\sqrt{\pi n}\) and \(\binom{n}{\lceil n/2\rceil}\sim2^n\sqrt{2/(\pi n)}\) give the three displayed asymptotics. The subtractive term \(2^n\) in \(P_2(C_n)\) is exponentially negligible compared with \(\binom{2n}{n}\). No probabilistic convergence assumption other than uniform independent initial bits is used.

## Verification

Two self-contained Python 3 scripts, using only the standard library, reproduce the finite checks. Run `python3 verify_direct.py` to enumerate every bit vector on both graph families for \(2\le n\le8\), construct the true open-neighbor majority update vertex by vertex, and verify primitive-period populations and the stated entrance-time bounds. It processes exactly \(262128\) labelled states. Run `python3 verify_weighted_types.py` for an independent multinomial-weighted enumeration of the four possible binary pair types, both values of the central bit, and the compressed update for \(2\le n\le60\). It verifies both counting identities and the global iterate relations \(F^3=F\) on \(C_n\), \(F^4=F^2\) on \(H_n\), at the pair-type level. Captured standard output accompanies both scripts. These are finite tests; the all-size theorem is proved above by the update cases.

## Relationship to prior work

Goles and Olivos (1980) established the general eventual period-at-most-two property of symmetric threshold systems. The full available texts of Tamuz and Tessler (2013 preprint, revised 2014) and Benjamini et al. (2014 preprint, journal 2016) treat majority dynamics, convergence, stability or information retention, but do not supply the fixed- and primitive-two-population formulas for these complementary-pair graphs, nor their exponential contrast after adding one universal vertex. The first family is the classical cocktail-party graph, equivalently the complete \(n\)-partite graph with every part of size two. The second has the additional singleton part. Results about majority colorings of multipartite graphs and about binary *parity* updates concern different invariants or different local dynamics. The formulas here are specific to the strict synchronous **majority** rule with tie retention, not general consequences of the eventual-period-two theorem.

## Limitations

The analysis concerns only these two explicitly defined families, exactly binary opinions, synchronous updates and the specified tie rule. It counts immediate primitive periods and gives sharp upper bounds on transient length; it does not claim the mass-resolved sizes of all eventual two-cycle basins. The earliest dated, electronically verified preprint used as an archival anchor is July 15, 2013. A foundational 1980 journal result has a verified publication year but no day-resolved earliest public release date in the inspected material. The possibility of an unindexed equivalent exact census remains a bibliographic limitation; mathematical correctness does not establish historical priority.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI 10.1016/0012-365X(80)90121-1. Journal abstract available at https://pure.uai.cl/en/publications/periodic-behaviour-of-generalized-threshold-functions/.
2. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, first submitted July 15, 2013, arXiv:1307.4035, https://arxiv.org/html/1307.4035v2 (full text).
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, May 11, 2014, https://arxiv.org/abs/1405.2486 (full mathematical text accessible).
4. Wolfram MathWorld, *Cocktail Party Graph*, https://mathworld.wolfram.com/CocktailPartyGraph.html (graph nomenclature only).
