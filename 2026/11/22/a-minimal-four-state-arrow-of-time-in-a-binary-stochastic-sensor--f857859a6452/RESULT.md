# A minimal four-state arrow of time in a binary stochastic sensor

## Finding

A stationary deterministic binary readout of an irreducible continuous-time Markov chain with at most three microstates is reversible as a complete process. Four microstates suffice for irreversibility. In the clockwise ring with positive rates \(1\to2\to3\to4\to1\) equal to \(a,b,c,d\), respectively, a nonconstant binary coloring produces an irreversible stationary process **if and only if** its two color classes are \(\{1,3\}\) and \(\{2,4\}\), **in either label order**, and \((a-c)(b-d)\ne0\). Every singleton/triple and every adjacent-pair/adjacent-pair partition is reversible.

Label \(\{1,3\}\) by 1 and \(\{2,4\}\) by 0, and let \(p_h(w)\) be the stationary probability of word \(w\) at times \(0,h,2h,3h\). Then
\[
p_h(1100)-p_h(0011)=\frac{abcd(a-c)(b-d)}{abc+abd+acd+bcd}\,h^3+O(h^4),\qquad h\downarrow0.
\]
Complementing the labels negates this witness without affecting reversibility. Whenever both opposite contrasts are nonzero, the witness is nonzero at all sufficiently small positive sampling intervals. For such rates, at a fixed suitably short sampling interval it remains nonzero after adding a sufficiently small positive reverse rate on every edge; the perturbed chain has finite strictly positive entropy production.

## Assumptions and scope

The hidden model is a finite-state continuous-time Markov chain with row generator \(Q\), exponential holding times, and its unique invariant initial distribution \(\pi\). The binary sensor is a deterministic function of the state; its labels do not change under time reversal. Reversibility means equality in law of \((Y_{t_1},\ldots,Y_{t_k})\) and \((Y_{-t_1},\ldots,Y_{-t_k})\) for every finite collection of times, allowing unequal gaps. The obstruction up to three states applies to every irreducible generator with at most three states. The classification with four states is for the specified one-way ring only, with all four rates strictly positive.

## Proof

**1. Singleton color and adjacent pairs.** In any nonconstant binary coloring with at most three states, one class is a singleton. Each visit to that state has an exponential duration independent of the next microstate and subsequent excursion. The strong Markov property at successive entries and exits makes the two sequences of alternating color durations independent, with each sequence i.i.d. in its own color. A stationary alternating renewal law with these properties is reversible: conditional on the color covering the origin, its covering interval has the corresponding length-biased duration and the origin is uniform in it; the intervals on either side are independent and alternate with the same respective duration laws. Reflection about the origin exchanges the sides and replaces the uniform offset by its complement. The same reasoning applies to singleton partitions of the four-cycle. For adjacent-pair/adjacent-pair partitions of the one-way ring, every entrance to a color is at a fixed microstate and each color duration is a sum of its two independent exponential holding times. Successive such sums are independent, so the observed path is again stationary alternating renewal and reversible. Constant colorings are trivial.

**2. Opposite pairs.** Write \(Z=abc+abd+acd+bcd\) and \(J=abcd/Z\). The stationary weights of the ring are
\[
\pi=(bcd,acd,abd,abc)/Z,
\]
because the four oriented edge traffics are equal to \(J\). At a typical entry to color 1 the hidden entry is 1 or 3 with equal probability. Let \(U\) be the duration of that 1-run and \(V_+,V_-\) the next and previous 0-run durations. Conditional on the hidden phase at the 1-run, the exponential holding times are independent. Choosing a typical 1-run by its entry weights it once, not by duration. Thus
\[
\mathbb E[UV_+]-\mathbb E[UV_-]
=\tfrac12\left(\tfrac1a-\tfrac1c\right)\left(\tfrac1b-\tfrac1d\right).
\]
Under reversal the marked statistic for a typical 1-run exchanges the next and previous 0-runs. In stationarity the rate-normalized distribution on these marks is the same whether a run is counted at its entry or exit: each complete run is counted once in either convention, with at most two boundary runs in a finite window. Consequently a nonzero difference implies time irreversibility. Equivalently, the finite-dimensional distributions determine the law of the piecewise-constant binary path and hence these run statistics.

Conversely, in the time-reversed hidden generator the only jump from site \(i\) is to its predecessor, at rate \(r_i\), where \((r_1,r_2,r_3,r_4)=(a,b,c,d)\). Indeed \(\pi_{i-1}r_{i-1}/\pi_i=r_i\). If \(a=c\), reflection of the square exchanging sites 1 and 3 and fixing 2 and 4 sends this reverse generator to the forward one without changing either color, stationary weights, or holding rates. If \(b=d\), use the reflection exchanging 2 and 4 and fixing 1 and 3. The observed path laws are therefore equal under reversal in either case. Both arguments are invariant under swapping the two binary labels.

**3. Four-snapshot coefficient.** Compare the words \(1100\) and \(0011\) by summing over initial states \(i\) of odd and even index, respectively, with the latter terms subtracted. Indices on the rates are modulo four. Each true jump changes color. For one jump, it must be in the middle gap; writing its time as \(h(1+s)\) gives an exact contribution from initial state \(i\), including its stationary weight, of
\[
J h\int_0^1\exp\{-h[r_i(1+s)+r_{i+1}(2-s)]\}\,ds.
\]
The order \(h\) and \(h^2\) differences cancel: there are two initial states of each parity, and each parity counts every rate once in the linear sum \(r_i+r_{i+1}\). In the cubic term the squared-rate sums cancel as well. The cross term has multiplier \(\int_0^1(1+s)(2-s)\,ds=13/6\), and the signed sum of \(r_i r_{i+1}\) equals \((a-c)(b-d)\).

For three jumps the counts per gap must be \((2,1,0),(0,1,2)\), or \((0,3,0)\). To cubic order each probability is its product of rates times the ordered jump-time volume, with no survival correction at that order. Across the three counts the volume factor is \(1/2+1/2+1/6=7/6\), and the stationary rate product is \(J r_{i+1}r_{i+2}\). Its signed rate sum is the negative of the preceding one. There are no even jump totals for these words, and five or more jumps have probability \(O(h^5)\) for fixed rates. The net cubic coefficient is \(J(13/6-7/6)(a-c)(b-d)\), as asserted.

In a stationary, equally spaced binary series the pairs \(01,10\) have equal probabilities. For triples the only nonpalindromic reversal pairs are \(001,100\) and \(011,110\), which are equal by the identical first/last two-symbol marginals. Four consecutive equally spaced snapshots are therefore the shortest window that can witness this asymmetry in any stationary binary process. This does not rule out three snapshots with unequal gaps.

**4. Positive reverse edges.** Fix positive rates with \((a-c)(b-d)\ne0\) and then choose a positive \(h\) at which the one-way witness is nonzero. Stationary probabilities of an irreducible finite generator and its transition matrix at that lag are continuous in the rates. Hence the same nonzero witness persists when a common counterclockwise rate \(\varepsilon>0\) is sufficiently small. All edges then have finite forward and backward rates. The cycle affinity \(\log(abcd/\varepsilon^4)\) is nonzero for sufficiently small \(\varepsilon\), so detailed balance fails; the stationary entropy production is finite and strictly positive. This is a persistence statement, not an exact rate classification of all bidirectional rings.

## Verification

The preceding proof is analytic. The associated `checker.py` uses Python, SymPy, NumPy and SciPy and checks the four-word coefficient by a different route: expanding the stationary matrix product with three factors of \(e^{hQ}\) interspersed with binary diagonal masks. It also contains finite-lag numerical diagnostics on illustrative reversible and irreversible cases, including an example with positive reverse rates. Those examples do not replace the analytic argument about all rates and times. Label complementation interchanges the two tested words exactly.

## Relationship to prior work and limitations

Chen's Proposition 3.8 gives reversibility for a three-state hidden Markov observation when two emission rows are identical, which covers a deterministic binary observation of three states. Lucente et al., §V, describe the singleton-class renewal mechanism, and Arola-Fernandez and Lacasa, §III, establish the binary short-word obstruction. Neither lower bound is claimed as new. Flomenbom, Klafter and Szabo use pairs of successive on/off dwell times to diagnose correlations and analyze a four-substate bidirectional path; correlated dwells need not be time asymmetric. Martínez et al. develop general waiting-time approaches to hidden irreversibility. The specific contribution here is the complete one-way four-cycle partition and rate-contrast classification, the two signed witnesses at run and snapshot scales, and finite-affinity persistence. The separately studied homogeneous ring threshold restricts all clockwise rates and all counterclockwise rates to be equal across sites within their directions, and therefore does not cover the heterogeneous four-rate witness.

The theorem concerns stationary paths with noiseless deterministic readout. It does not classify arbitrary four-state graphs, estimate entropy production from the binary data, or establish finite-sample detection power. Small-lag asymmetry has cubic magnitude and may be hard to resolve statistically. More general hidden-state methods may contain related results; historical priority is not certified.

## References

1. Y. Chen, *On the reversibility of the observed process of three-state hidden Markov model*, arXiv:1101.5482, Proposition 3.8. https://arxiv.org/abs/1101.5482
2. D. Lucente et al., *Inference of time irreversibility from incomplete information: Linear systems and its pitfalls*, Phys. Rev. Research 4 (2022), 043103. https://doi.org/10.1103/PhysRevResearch.4.043103
3. L. Arola-Fernandez and L. Lacasa, *Irreversibility of symbolic time series: a cautionary tale*, arXiv:2303.11868. https://arxiv.org/abs/2303.11868
4. O. Flomenbom, J. Klafter and A. Szabo, *What Can One Learn from Two-State Single-Molecule Trajectories?*, Biophys. J. 88 (2005), 3780–3783. https://arxiv.org/abs/q-bio/0502006
5. I. A. Martínez et al., *Inferring broken detailed balance in the absence of observable currents*, Nature Communications 10 (2019), 3542. https://doi.org/10.1038/s41467-019-11051-w
6. *A six-state visibility threshold for binary observation of irreversible Markov circulation*, Resultary. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-six-state-visibility-threshold-for-binary-observation-of-irrev--741ee1f18a68
