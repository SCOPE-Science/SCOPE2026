# Flip-activity interpolation for strict majority on cliques with deleted matchings

## Finding

For every integer \(m\ge2\) and \(0\le k\le m\), delete a fixed matching of \(k\) edges from the labelled complete graph \(K_{2m}\), obtaining \(G_{m,k}\). Under synchronous strict binary open-neighbor majority with incumbent tie retention, let \(F\) be the state update. All configurations with exactly \(m\) ones are immediately periodic with period dividing two. All others become unanimous, hence fixed, after one update. This is an exact all-size transient classification.

For a balanced configuration, let \(J\) count deleted edges whose endpoints initially have *different* bits. Exactly \(2(m-J)\) vertices switch bit at every update, and the number of labelled balanced configurations in the stratum \(J=j\) is

\[
A_{m,k,j}=\binom{k}{j}2^j\sum_{r=0}^{k-j}\binom{k-j}{r}\binom{2m-2k}{m-j-2r},\qquad 0\le j\le k.
\]

Every binomial coefficient with an inadmissible lower argument is zero. The all-parameter activity generating polynomial is \(\mathcal A_{m,k}(z)=\sum_{j=0}^{k}A_{m,k,j}z^{2(m-j)}\), and its coefficient sum is \(\binom{2m}{m}\).

The fixed-state and primitive-two-orbit counts are, respectively,

\[
P_1(G_{m,k})=2+2^m\mathbf 1_{k=m},\qquad
O_2(G_{m,k})=\tfrac12\left(\binom{2m}{m}-2^m\mathbf 1_{k=m}\right).
\]

Thus deleting the final edge of a perfect matching converts exactly \(2^m\) balanced configurations from two-periodic to fixed, whereas for all preceding deletion counts the number of primitive-two orbits is unchanged; the intermediate deletion counts nevertheless shift the exact distribution of switching activity.

Conditional on a uniformly chosen balanced configuration, \(J\) satisfies

\[
\mathbb E[J]=\frac{km}{2m-1},\qquad
\operatorname{Var}(J)=\frac{km(m-1)}{(2m-1)^2}+\frac{k(k-1)m}{(2m-1)^2(2m-3)}.
\]

For any integer sequence \(m\to\infty\), \(k=k(m)\) with \(0\le k\le m\) and \(k/m\to\alpha\in[0,1]\), the fraction of vertices changing at every step converges *in probability* to \(1-\alpha/2\) under the uniform balanced-state distribution. This is an activity law, not an assertion of independence of the matched-pair indicators.

## Assumptions and scope

The deleted edges are vertex-disjoint and marked; all remaining possible distinct-vertex edges are present. All \(2^{2m}\) binary configurations are labelled, without graph-symmetry quotienting. Each vertex simultaneously compares the counts of the two bits among its *open* neighbors. A tie leaves its own state unchanged. A state has first periodic-entry time \(t\) if \(t\) is the least nonnegative update number at which it lies on an exact periodic orbit. The activity of an immediately periodic state is the Hamming distance between consecutive phases, not the number of vertices that ever change in its attraction basin. Fixed states have activity zero. The terms “primitive-two configurations” and “primitive-two orbits” differ by the standard factor of two. Unbalanced initial states that collapse to a fixed point are not counted as initially periodic.

## Proof

Write \(w=|x|\) for the initial number of ones. An unmatched vertex has degree \(2m-1\) and sees \(w-x_v\) ones. If \(w<m\) every unmatched vertex updates to zero; if \(w>m\) every unmatched vertex updates to one. For a deleted matched pair \(e=\{a,b\}\), let \(s=x_a+x_b\in\{0,1,2\}\). Both endpoints see \(w-s\) ones, among \(2m-2\) neighbors, so the strict-majority threshold is \(m-1\). If \(w\le m-1\), then \(w-s\le m-1\); equality can occur only when \(s=0\) at the boundary, in which case both incumbent bits are zero and tie retention still gives zero. Thus both endpoints update to zero. Similarly, if \(w\ge m+1\), then \(w-s\ge m-1\); equality can occur only when \(s=2\) at the boundary, where both incumbent bits are one. Thus both endpoints update to one. Consequently all unbalanced states enter the appropriate unanimous fixed state after one update.

Suppose \(w=m\). Each unmatched vertex strictly adopts the opposite bit because its odd degree yields a majority against itself. A deleted pair of type \(00\) sees \(m\) ones and becomes \(11\); a type \(11\) pair sees \(m-2\) ones and becomes \(00\). A mixed pair has exactly \(m-1\) neighbors of each color and remains *unchanged* by tie retention. Thus \(F(x)\) complements precisely the vertices outside the \(J\) mixed deleted pairs, for exactly \(2m-2J\) flips. The mixed pairs contain exactly \(J\) ones and \(J\) zeroes. Among the remaining \(2m-2J\) vertices, there are exactly \(m-J\) ones and as many zeroes. Complementing them therefore preserves total weight \(m\), preserves the locations of mixed pairs, and reverses the complemented bits a second time. Thus \(F^2(x)=x\) on every balanced state, with constant activity \(2(m-J)\) in both phases.

For exactly \(j\) mixed deleted pairs, choose the pairs in \(\binom{k}{j}\) ways and orient each in two ways. Of the \(k-j\) remaining deleted pairs choose \(r\) to be \(11\), with the rest \(00\); then the unpaired \(2m-2k\) vertices must contain \(m-j-2r\) ones. The elementary product count gives \(A_{m,k,j}\), including boundary cases. Summation over \(j\) counts each balanced state exactly once and therefore equals \(\binom{2m}{m}\).

The activity vanishes precisely when \(J=m\). Since \(J\le k\le m\), this requires \(k=m\) and all \(m\) deleted pairs mixed. They have \(2^m\) orientations. The two unanimous configurations are the other fixed points; every other balanced state is primitive two-periodic, proving the fixed and orbit counts and the exact final-edge threshold.

For the moments, condition on choosing uniformly one of the \(\binom{2m}{m}\) subsets of size \(m\). Let \(I_i\) indicate whether the endpoints of deleted pair \(i\) have different bits, and put \(J=\sum_i I_i\). Exchangeability gives

\[
\Pr(I_i=1)=\frac{2\binom{2m-2}{m-1}}{\binom{2m}{m}}=\frac m{2m-1}=:p.
\]

For distinct \(i,h\),
\[
\Pr(I_i=I_h=1)=\frac{4\binom{2m-4}{m-2}}{\binom{2m}{m}}=\frac{m(m-1)}{(2m-1)(2m-3)},
\quad \operatorname{Cov}(I_i,I_h)=\frac m{(2m-1)^2(2m-3)}.
\]

Consequently \(\mathbb E[J]=kp\) and \(\operatorname{Var}(J)=kp(1-p)+k(k-1)\operatorname{Cov}(I_i,I_h)\), which are the displayed formulas. Since \(k\le m\), the variance is \(O(m)\) uniformly in \(k\). Chebyshev's inequality gives \((J-\mathbb E[J])/m\to0\) in probability. As \(\mathbb E[J]/m=k/(2m-1)\to\alpha/2\), the activity fraction \((2m-2J)/(2m)=1-J/m\) converges to \(1-\alpha/2\). This completes every all-parameter claim.

## Verification

The standalone script `verify_direct.py` enumerates every labelled bit configuration on each \(G_{m,k}\) for \(2\le m\le7\), \(0\le k\le m\), applying strict open-neighbor majority explicitly at each vertex. It verifies the full transition on balanced and unbalanced states, the two-step identity on the balanced layer, the exact activity profile, and fixed/primitive-two populations. A total of 167472 initial states passed, with captured output `direct_output.txt`. A separately implemented multinomial pair-type calculator `verify_weighted.py` verifies the exact generating coefficients, their central-binomial normalization, and both moments for 1888 parameter pairs with \(2\le m\le60\) and \(0\le k\le m\), with captured output `weighted_output.txt`. Both are pure Python 3 standard-library scripts, runnable as `python3 verify_direct.py` and `python3 verify_weighted.py`. These computations check finite examples; they are not the proof of the infinite-parameter statements, which is the preceding local-rule and exchangeability argument.

## Relationship to prior work

The general eventual period-at-most-two theorem for symmetric threshold dynamics is due to Goles and Olivos (1980), and is not a new assertion here. Tamuz and Tessler (2013) discuss majority dynamics and information retention; Kaaser, Mallmann-Trenn and Natale (2015) analyze general convergence/voting time including complete and multipartite networks. Neither inspected manuscript provides the full deleted-matching activity distribution for all partial matching sizes. A published exact analysis of a *full* deleted matching (the cocktail-party graph) already establishes the \(k=m\) fixed and primitive-two census, together with the behavior after adjoining one universal vertex. An activity-resolved analysis of *equal-size* Turán graphs also includes the full-matching family, but not the mixed block sizes present for \(0<k<m\). Those endpoint or balanced-part results do not imply the intermediate \(A_{m,k,j}\) coefficients or the continuous matching-density activity interpolation. The new contribution is precisely that partial-matching interpolation and its sharp final-edge fixed-state threshold; no originality is attributed to the general two-cycle bound or to previously known full-matching counts.

## Limitations

This is a classification for labelled, even-order, matching-defected cliques under synchronous two-color open-neighbor strict majority with tie retention. It does not determine separate attraction-basin sizes of individual two-cycles, odd graph orders, nonmatching edge deletions or random/asynchronous updates. The conditional limit refers only to a uniformly sampled *balanced initial configuration*, not to arbitrary initial states; under the unrestricted uniform initial distribution, most states are unbalanced and become unanimous after one update. General historical coverage cannot be ruled out entirely from indexed searches, especially for unpublished mixed-multipartite activity enumerations. No external independent mathematical audit has been performed.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 (general threshold-period theorem).
2. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, first arXiv submission 2013-07-15, https://arxiv.org/abs/1307.4035 (majority dynamics, information retention and period background).
3. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, first arXiv submission 2015-08-14, https://arxiv.org/abs/1508.03519 (general convergence and voting time).
4. *One universal vertex exponentially suppresses majority two-cycles on cocktail-party graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-one-universal-vertex-exponentially-suppresses-majority-two-cycle--1b19fbc146ae (full-matching endpoint and one-added-vertex comparison).
5. *Activity-resolved majority two-cycles on equal-part Turán graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-activity-resolved-majority-two-cycles-on-equal-part-tur-n-graphs--0086189051c3 (all-equal-part activity, not partial matching case).
