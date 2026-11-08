# A sharp overlap threshold for permanent polarization under two-group majority dynamics

## Finding

Let a fixed hypergraph have precisely two distinct intersecting hyperedges \(E,F\) of odd sizes \(a,b\ge 3\), with \(s=|E\cap F|\), where \(1\le s<\min(a,b)\). Each vertex initially holds one of two opinions. At independent rate-one exponential clocks, an active hyperedge (containing both opinions) changes all its opinions to its strict majority. The clocks continue forever, with inactive updates having no effect.

**Theorem.** Write \(m_H(\sigma)\) for the strict majority of the initial configuration \(\sigma\) on hyperedge \(H\), \(A_H(\sigma)\) for the indicator that \(H\) is initially active, and \(m_{F\mid E}(\sigma)\) for the majority on \(F\) after overwriting every vertex in \(E\) with \(m_E(\sigma)\), retaining all other initial values. Define \(m_{E\mid F}\) analogously. If \(A_E+A_F>0\), the probability (conditional on \(\sigma\)) of never reaching global consensus is exactly

\[
\frac{\mathbf1_{\{2s<\min(a,b)\}}}{A_E+A_F}
\left(A_E\mathbf1_{\{m_{F\mid E}\ne m_E\}}+
A_F\mathbf1_{\{m_{E\mid F}\ne m_F\}}\right).
\]

When both edges are initially inactive, the probability is zero. Thus all configurations almost surely reach consensus after at most four *effective* hyperedge updates when \(2s\ge\min(a,b)\). When \(2s<\min(a,b)\), there exist initial configurations giving permanent polarization with probability one; both edges fire infinitely often in the resulting closed alternating class.

If the initial opinions are independent unbiased fair bits, define

\[
T_a(s)=2^{-(a-s)}\sum_{j=(a+1)/2}^{a-s}\binom{a-s}{j},
\qquad
T_b(s)=2^{-(b-s)}\sum_{j=(b+1)/2}^{b-s}\binom{b-s}{j},
\]

where an empty sum is zero. Then the **complete fair-initialization polarization law** is

\[
\boxed{\Pr(\text{never reaches consensus})=
\mathbf1_{\{2s<\min(a,b)\}}\frac{T_a(s)+T_b(s)}{2}.}
\]

In particular, the probabilities are \(5/16\) for \((a,b,s)=(5,5,1)\), \(1/8\) for \((5,5,2)\), and zero for \((5,5,3)\). This is a sharp overlap-driven consensus/polarization boundary for every pair of odd group sizes, not merely a finite enumeration.

## Assumptions and scope

The vertex set is exactly \(V=E\cup F\), and there are no other hyperedges or rewiring events. Both group sizes are odd and at least three, with nonempty intersection, and neither group contains the other. All opinions are binary. A majority update is simultaneous across the selected group; each group has the same rate-one Poisson clock, independent of the other. An inactive update is a no-op. The time-continuous process is equivalently the embedded chain of effective updates, which selects uniformly among currently active groups. "Permanent polarization" means that global unanimity is never reached; on this two-edge system this is equivalent to alternating forever between distinct opinions on the shared vertices while each private vertex retains its own final value. The formula is for equal clock rates; unequal rates require unequal first-event weights.

## Proof

**1. The first event and the state space.** If both groups are homogeneous at the start, their shared vertices force the homogeneous opinions to agree, so consensus already holds. Otherwise the first effective event selects each initially active group with probability \(1/(A_E+A_F)\). Suppose the first event fires \(E\) and sets its vertices to \(c=m_E(\sigma)\). The only group that can next be active is \(F\). If \(F\) has majority \(c\), then either it is already homogeneous \(c\), or its next update makes all vertices equal to \(c\). If its majority is the opposite opinion \(d\), then \(F\) is active, and its next update makes all vertices of \(F\) equal to \(d\). Thus both private parts are now monochrome, with opposing opinions \(c\) on \(E\setminus F\) and \(d\) on \(F\setminus E\).

**2. The sharp overlap obstruction.** With opposing private parts, \(E\) has \(a-s\) private \(c\)-vertices and at most \(s\) shared \(d\)-vertices. Its majority is \(c\) exactly when \(a-s>s\), equivalent to \(2s<a\). Otherwise its majority is \(d\), and the next \(E\)-update gives consensus \(d\). When \(2s<a\), the next \(E\)-update restores shared opinion \(c\). Now \(F\) has a majority \(d\) exactly when \(2s<b\); otherwise its next update creates consensus \(c\). If both strict inequalities hold, the private parts dominate their respective groups for either opinion on the shared block, so effective updates alternate on \(F\) and \(E\) indefinitely. Both exponential clocks fire infinitely often almost surely. This proves the conditional expression, the four-effective-update bound, and necessity and sufficiency of the small-overlap condition for the existence of a permanent polarized state. A witness is all private \(E\)-vertices opinion \(0\), all private \(F\)-vertices opinion \(1\), and arbitrary opinions on the overlap: each private block forces its respective group majority whenever \(2s<\min(a,b)\).

**3. Average over independent fair opinions.** Under the small-overlap condition, an \(E\)-first update can lead to polarization exactly when the private vertices of \(F\) contain at least \((b+1)/2\) opinions opposite to the initial majority on \(E\). Since those private bits are independent of the initial \(E\)-configuration and the majority of an odd fair-bit group is symmetric, this happens with probability \(T_b(s)\), conditional on any initially active \(E\). The unconditional probability that \(E\) is active and this condition holds is \((1-2^{1-a})T_b(s)\). Likewise, the corresponding \(F\)-first condition has probability \((1-2^{1-b})T_a(s)\).

If both edges are initially active, each is selected first with probability \(1/2\), whereas if only one is active, it is selected with probability one. A correction of one-half times each sole-active adverse-event probability is therefore required. The probability that \(F\) is initially homogeneous and its opinion opposes the initial majority of active \(E\) is exactly \(2^{1-b}T_a(s)\): fix either homogeneous opinion on \(F\), then the \(a-s\) private bits of \(E\) must already constitute a strict opposite majority. The analogous probability is \(2^{1-a}T_b(s)\). Therefore

\[
\begin{aligned}
\Pr(\text{polarization})
&=\frac12\Big[(1-2^{1-a})T_b(s)+(1-2^{1-b})T_a(s)\\
&\qquad\qquad+2^{1-b}T_a(s)+2^{1-a}T_b(s)\Big]\\
&=\frac{T_a(s)+T_b(s)}2.
\end{aligned}
\]

Multiplying by the sharp-overlap indicator proves the unconditional formula. The proof applies to arbitrarily large odd group sizes and uses no numerical approximation.

## Verification

The supplied standard-library `verify.py` independently follows effective hyperedge updates until consensus or repetition, and compares the resulting exact rational nonconsensus probability for each labeled initial state with the theorem's formula. It checks \(18{,}544\) initial configurations across \(27\) group-size/overlap structures, and separately compares direct exact averages to the binomial-tail formula for \(46\) structures. Execute `python3 verify.py` from the extracted package; the output ends in `PASS`. These finite checks cross-check, but do not constitute, the general proof.

## Relationship to prior work

Golovin, Mölter, and Kuehn (2023/2025) introduce adaptive hypergraph opinion propagation and rewiring, including majority propagation; this result specializes to their majority-update mechanism with no rewiring on a two-hyperedge overlap and derives an exact all-size phase boundary. Noonan and Lambiotte (2021) analyze majority updates on 3-uniform random, modular, and heterogeneous hypergraphs using density approximations, rather than this sparse two-group exact law. Papanikolaou et al. (2022) study distinct adaptive group-influence mechanisms. Lanchier and Neufer (2013) study overlapping lattice blocks, not a fixed two-edge overlap classification. The previously known triplet loose-hyperstar special case \(a=b=3\), \(s=1\), has polarization probability \(1/4\); the contribution here is **not** that special case but the complete arbitrary-odd-size, arbitrary-intersection conditional and averaged laws and sharp consensus threshold.

## Limitations

The model has precisely two overlapping groups, equal event rates, odd sizes, no rewiring and no noise. A larger collection of overlapping groups, even group sizes with tie-breaking, or persistent random opinion mutation may behave differently. The analysis gives no quantitative confidence interval for priority against unindexed or unavailable prior results. In the polarized closed class, state convergence fails although the private vertices stabilize; therefore calling polarization an absorbing single state would be incorrect. The at-most-four bound counts effective updates, not elapsed Poisson-clock time (although elapsed time to the eventual class is finite almost surely).

## References

- A. Golovin, J. Mölter, C. Kuehn, *Polyadic Opinion Formation: The Adaptive Voter Model on a Hypergraph*, arXiv:2308.03640, first version 2023-08-07, https://arxiv.org/abs/2308.03640.
- J. Noonan, R. Lambiotte, *Dynamics of Majority Rule on Hypergraphs*, Physical Review E 104, 024316 (2021), https://doi.org/10.1103/PhysRevE.104.024316, arXiv:2101.03632.
- S. Papanikolaou and collaborators, *Consensus from Group Interactions: An Adaptive Voter Model on Hypergraphs*, Physical Review E 105, 054307 (2022), arXiv:2201.06421, https://arxiv.org/abs/2201.06421.
- N. Lanchier, J. Neufer, *Stochastic Dynamics on Hypergraphs and the Spatial Majority Rule Model*, Journal of Statistical Physics 151 (2013), 21–45, https://arxiv.org/abs/1301.0151.
