# Flip-activity interpolation for strict majority on cliques with deleted matchings

## Finding

For integers \(m\ge2\) and \(0\le k\le m\), let \(G_{m,k}\) be the graph obtained from the labelled \(K_{2m}\) by deleting a fixed matching of size \(k\). Use synchronous binary open-neighbor strict majority, retaining each incumbent bit on a tie. The result below describes the **activity distribution on the balanced layer**, not a new classification of the periods or of the transient.

For a configuration with exactly \(m\) ones, let \(J\) be the number of deleted edges whose endpoints have different bits. The state is periodic of period dividing two, with \(2(m-J)\) flips each update. For each \(0\le j\le k\), the number of labelled balanced states with \(J=j\) is
\[
A_{m,k,j}=\binom{k}{j}2^j\sum_{r=0}^{k-j}\binom{k-j}{r}\binom{2m-2k}{m-j-2r}.
\]
An inadmissible lower binomial argument contributes zero. The balanced activity polynomial is
\[
\mathcal A_{m,k}(z)=\sum_{j=0}^{k}A_{m,k,j}z^{2(m-j)},\qquad
\mathcal A_{m,k}(1)=\binom{2m}{m}.
\]
For a uniformly chosen balanced state,
\[
\mathbb E[J]=\frac{km}{2m-1},\qquad
\operatorname{Var}(J)=\frac{km(m-1)}{(2m-1)^2}+\frac{k(k-1)m}{(2m-1)^2(2m-3)}.
\]
Along any sequence with \(m\to\infty\) and \(k/m\to\alpha\in[0,1]\), the fraction of vertices changing at every step converges in probability to \(1-\alpha/2\). This conditional limit does not assume independent pair indicators.

**Period census for context (existing result).** All unbalanced initial states become unanimous after one update. The number of fixed configurations is \(2+2^m\mathbf 1_{k=m}\); the number of primitive two-orbits is \(\tfrac12[\binom{2m}{m}-2^m\mathbf 1_{k=m}]\). Thus the primitive two-orbit total stays the same for \(k<m\), even though the distribution of flips changes. Only the last matching deletion changes that total and makes \(2^m\) balanced states fixed. These transition and period-census facts, including the final-edge threshold, are covered for \(k\ge1\) by the even-universal-vertex case of [1]; the undamaged clique \(k=0\) is immediate from the same local rule.

## Assumptions and scope

The graph is simple, the removed edges are vertex-disjoint, and all configurations are labelled without a graph-symmetry quotient. Each update uses only the previous step's bits. Activity is the Hamming distance between consecutive phases of an initially periodic state, not a sum of flips in an attraction basin. A fixed balanced configuration contributes at activity zero; the two unanimous states are outside the balanced polynomial. A primitive two-orbit consists of two configurations.

## Proof

**Local rule, recalled for the activity calculation.** At weight \(w\), an unmatched vertex with bit \(x\) sees \(w-x\) ones among \(2m-1\) neighbors. The vertices of a deleted pair with bit sum \(s\) each see \(w-s\) ones among \(2m-2\) neighbors. If \(w<m\), the unmatched vertices go to zero and the matched vertices do also: a tie is possible only at \(w=m-1\), \(s=0\), where incumbents are already zero. By the complementary argument \(w>m\) gives all ones. At \(w=m\), unmatched vertices flip. Among the deleted pairs, \(00\) goes to \(11\), \(11\) goes to \(00\), and mixed pairs tie and stay unchanged. The mixed pairs contain \(J\) ones and \(J\) zeros, so the remaining \(2m-2J\) complemented bits are balanced. Hence weight and mixed pairs are preserved and the next step undoes the first. This both proves the activity formula and recovers the period census: no balanced fixed state is possible unless \(J=m=k\), when the fixed states are the \(2^m\) orientations of the mixed pairs. The two unanimous states are fixed.

**Exact stratification.** To count states with \(J=j\), choose and orient the \(j\) mixed deleted pairs. Of the other \(k-j\) pairs, choose \(r\) to be \(11\) and give the rest \(00\). The \(2m-2k\) unmatched vertices must contain \(m-j-2r\) ones. This gives the claimed sum, counting each balanced state once. For \(k=0\) all balanced states have activity \(2m\). When \(k=m\), the binomial term on the unmatched vertices permits only \(m-j=2r\), including the fixed stratum \(j=m\).

**Moments and limit.** View a uniform balanced configuration as a uniform \(m\)-subset of \(2m\) labels. Let \(I_i\) indicate that deleted pair \(i\) is mixed. Its one- and two-pair probabilities for distinct \(i,h\) are
\[
p=\Pr(I_i=1)=\frac{2\binom{2m-2}{m-1}}{\binom{2m}{m}}=\frac m{2m-1},\qquad
\Pr(I_i=I_h=1)=\frac{4\binom{2m-4}{m-2}}{\binom{2m}{m}}=\frac{m(m-1)}{(2m-1)(2m-3)}.
\]
The covariance is \(m/[(2m-1)^2(2m-3)]\). In \(J=\sum_{i=1}^k I_i\) this gives \(kp\) for the mean and \(kp(1-p)+k(k-1)\operatorname{Cov}(I_i,I_h)\) for the variance, with absent pair terms interpreted as zero. Since \(k\le m\), the variance is \(O(m)\) uniformly and Chebyshev's inequality gives \((J-\mathbb E[J])/m\to0\) in probability. The mean divided by \(m\) tends to \(\alpha/2\). The changing fraction is \(1-J/m\), proving the limit.

## Verification

The source package contains two Python 3 standard-library checkers. `verify_direct.py` explicitly updates the open-neighbor majority state for every labelled configuration at \(2\le m\le7\), \(0\le k\le m\), testing transitions, activity strata and periods; this range contains 167472 initial states. `verify_weighted.py` independently counts by the occupation types of the labelled pairs and checks the activity coefficients, normalization and moments for 1888 parameter choices at \(2\le m\le60\), \(0\le k\le m\). The original verification notes report successful runs. The finite checks are sample corroboration of the all-parameter counting and probability proof, not its substitute.

## Relationship to prior work

The matching-deleted-clique theorem of [1] treats \(K_{2r+u}\) with \(r\ge1\) deleted pairs and \(u\) universal vertices. Taking \(r=k\), \(u=2(m-k)\) gives exactly the even-order family here for \(k\ge1\). Its even-\(u\) rule leaves mixed pairs unchanged and flips every other bit on the balanced layer. Thus the underlying dynamics, aggregate fixed and two-orbit counts, threshold at completion of a matching, and the identification of flipping vertices follow from that prior result. The earlier cocktail-party calculation [2] also gives the \(k=m\) aggregate census. More generally \(G_{m,k}=T(2m,2m-k)\) in the convention that Turán parts are as equal as possible; the voting-time bound of [5] is a different kind of result. The general period-at-most-two theorem for symmetric threshold dynamics is due to Goles and Olivos [3]; see also [4] for majority dynamics background.

The contribution here is the **activity refinement**: the exact labelled multiplicity distribution and its moments under balance throughout the partial-matching interpolation, and the matching-density limit. The prior transition rule is an input for the refinement. Aggregate period counts and activity distributions answer different questions: before the final deletion, the primitive two-orbit counts cannot distinguish matching sizes, but the changing fraction can.

## Limitations

This covers labelled even-order matching-deleted cliques and deterministic synchronous open-neighbor majority with incumbent tie retention. It does not determine the basin of each cycle, nonmatching edge deletions, odd order, or other update rules. The limit is conditional on initial balance, not a statement about an unconditioned uniform state. Historical coverage of exact activity refinements may be incomplete.

## References

1. [*Parity-gated majority oscillations on matching-deleted complete graphs*](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-parity-gated-majority-oscillations-on-matching-deleted-complete--e054374efd08), 2026-11-17, Finding and even-\(u\) proof.
2. [*One universal vertex exponentially suppresses majority two-cycles on cocktail-party graphs*](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-one-universal-vertex-exponentially-suppresses-majority-two-cycle--1b19fbc146ae), 2026-11-08.
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
4. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, https://arxiv.org/abs/1307.4035.
5. D. Kaaser, F. Mallmann-Trenn, and E. Natale, *On the Voting Time of the Deterministic Majority Process*, https://arxiv.org/abs/1508.03519.
