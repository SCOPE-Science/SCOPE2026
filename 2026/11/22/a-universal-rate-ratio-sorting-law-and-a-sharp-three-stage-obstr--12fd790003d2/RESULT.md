# A universal rate-ratio sorting law and a sharp three-stage obstruction in sequential development

## Finding

For a fixed, finite multiset of positive-duration environments, a two-transition, memoryless development process has an exact universal schedule: **sort environments in nonincreasing order of the ratio of first-stage to second-stage transition rates**. Every optimum has this ordering up to interchanges of tied ratios. The rule is independent of the durations of individual environments, though the optimal completion probability is not.

The rule ceases to be context-free at the next stage count: an explicit three-transition process has two environments whose preferred adjacent order **reverses when the same pair is preceded by a third environment**. Thus two sequential transitions are the last stage count at which the stated adjacent-swap rule can hold universally for arbitrary stage-dependent rates.

## Assumptions and scope

Let \(n\ge 1\) be finite. Each environment \(i\) has duration \(t_i>0\) and strictly positive rates \(p_i,q_i\) for the irreversible chain \(0\to1\to2\). State \(2\) is absorbing. The process begins in state \(0\), and all environment durations are mandatory and used once, without overlap or downtime. Within each block the rates are constant, all transitions are exponential/memoryless, and a transition rate changes instantly between blocks. Maximize the probability of reaching state \(2\) by \(H=\sum_i t_i\) over all permutations.

Define
\[
a_i=e^{-p_it_i},\quad b_i=e^{-q_it_i},\quad
J_i=\int_0^{t_i}e^{-p_i u-q_i(t_i-u)}\,du>0.
\]
For unequal rates, \(J_i=(a_i-b_i)/(q_i-p_i)\); for equal rates, \(J_i=t_i a_i\). All formulae below include that continuous equal-rate case.

## Proof

**Two-stage propagation.** The column of transient state probabilities evolves through block \(i\) by the lower-triangular matrix
\[
R_i=\begin{pmatrix}a_i&0\\p_i J_i&b_i\end{pmatrix}.
\]
The initial transient vector is \((1,0)^{\mathsf T}\). If blocks \(i,j\) are consecutive, the transient propagators in their two orders differ only in the lower-left entry:
\[
R_jR_i-R_iR_j=\begin{pmatrix}0&0\\ (p_jq_i-p_iq_j)J_iJ_j&0\end{pmatrix}.
\]
Indeed, subtracting the lower-left entries yields
\[
p_jJ_j(a_i-b_i)-p_iJ_i(a_j-b_j)
=(p_jq_i-p_iq_j)J_iJ_j.
\]
Let a prefix and suffix each be an arbitrary fixed sequence of the remaining blocks. A difference with only its lower-left entry nonzero, applied to the initial state after the prefix, is multiplied by \(\prod_{k\in\mathrm{prefix}}a_k\) through its upper input and by \(\prod_{k\in\mathrm{suffix}}b_k\) through its lower output. The completed probability is one minus the sum of the two remaining transient coordinates. Consequently
\[
\begin{split}
&F(\mathrm{prefix},i,j,\mathrm{suffix})
-F(\mathrm{prefix},j,i,\mathrm{suffix})\\
&=(p_iq_j-p_jq_i)J_iJ_j
\prod_{k\in\mathrm{prefix}}a_k
\prod_{k\in\mathrm{suffix}}b_k.
\end{split}
\]
Each factor outside the rate determinant is strictly positive. Hence an adjacent pair \(i,j\) is strictly better in that order if and only if \(p_i/q_i>p_j/q_j\), and is indifferent exactly for equal ratios. Repeatedly swapping any inverted adjacent pair therefore strictly improves completion until the ratios are nonincreasing. Conversely, a permutation containing an inversion of unequal ratios has an improving adjacent swap (possibly after commuting ties), and cannot be globally optimal. This proves the exact complete characterization, including all ties, for every positive duration and rate choice. A process with only one transition has completion probability \(1-e^{-\sum_i p_i t_i}\), independent of order.

**First stage-count obstruction.** For three transitions, consider states \(0\to1\to2\to3\), with state \(3\) absorbing. All three environments have duration \(\log 2\). Their ordered stage-specific rate triples are
\[
A=(4,1,2),\qquad B=(1,4,3),\qquad C=(8,1,2).
\]
Write \(F_3\) for the probability of reaching state \(3\) by the final time. Exact transition-matrix evaluation gives
\[
F_3(A,B)-F_3(B,A)=\frac{245}{768}>0,
\]
but
\[
F_3(C,A,B)-F_3(C,B,A)=-\frac{59245}{1376256}<0.
\]
Therefore no index based solely on the two adjacent environments can reproduce all strict local adjacent-swap preferences in the three-transition class: the same pair has opposing strict preferences in two lawful contexts. This conclusion **does not assert** the absence of every conceivable global algorithm or state-dependent control rule.

For completeness, the exact fractions can be reconstructed without floating-point arithmetic. Given a single environment with pairwise-distinct nonnegative integer rates \(r_0,r_1,r_2,r_3=0\), its transition probability over \(\log2\), from stage \(a\) to stage \(b\ge a\), equals
\[
M_{b,a}=\Bigl(\prod_{k=a}^{b-1}r_k\Bigr)
\sum_{k=a}^{b}
\frac{2^{-r_k}}{\prod_{\substack{\ell=a\\\ell\ne k}}^{b}(r_\ell-r_k)}.
\]
Empty products equal one and entries below the diagonal are zero. The formula follows by partial fractions from the Laplace transform \(\prod_{k=a}^{b-1}r_k/\prod_{k=a}^b(s+r_k)\) of the pure-birth transition kernel. In each of the three specified environments all four rates, including zero, are distinct, so the expression applies directly. Multiplying the exact matrices in chronological order and taking the final-state entry reproduces both signed fractions.

## Verification

Run the supplied standard-library-only program with `python verify.py`. It checks all exact rational transitions for the stated examples, the two signed three-transition differences, a two-transition numeric example, exhaustive permutations of randomly sampled small two-transition instances, and 1,000 independent numerical tests of the prefix/suffix interchange formula. It reports 46,171 successful assertions with its deterministic seed. The general all-parameter proof is the exact matrix interchange above; sampling is not substituted for an infinite proof.

For a simple two-transition illustration, let \(A=(p,q)=(3,1)\), \(B=(1,3)\), and let both last \(\log2\). Then
\[
F(A,B)=\frac{27}{32},\qquad F(B,A)=\frac9{16},\qquad
F(A,B)-F(B,A)=\frac9{32}.
\]
Although the integrated hazards at each of the two stages are identical under both orders, chronological exposure changes completion by \(28.125\) percentage points.

## Relationship to prior work

The underlying irreversible first-order chain and phase-type representation are classical. Bak, Salamon and Andresen (2002) optimize the terminal abundance of an *intermediate* species in a reversible three-species chemical system with continuously chosen temperature. Their full four-page paper was inspected; it neither supplies the fixed-multiset irreversible *absorbed-product* permutation law nor the three-stage prefix reversal. Yin (2008) uses reciprocal temperature transfers to estimate stage-dependent deterministic plant-development durations, rather than the probability of completing stochastic sequential transitions under permutations. Carrington and colleagues (2013) investigate development under daily temperature variation, rather than this scheduling theorem.

The new mathematical content claimed here is limited to the explicit universal ratio classification with all its quantifiers and strict ties, together with the smallest-stage context-dependence obstruction. This should not be confused with a claim that matrix exponentials, the interchange proof technique, first-order kinetic chains, or environmental sensitivity are themselves new.

## Limitations

The rates are assumed known, positive and constant within each block; transitions are memoryless and irreversible; all blocks must occur exactly once; no individual-specific variation, mortality, feedback, nonlinear thermal responses or restriction on switching beyond discrete fixed blocks is modeled. Physical temperature profiles might restrict the admissible rate triples and can make the three-stage counterexample unattainable. The explicit three-stage example proves failure of a context-free *adjacent comparison*, not a universal impossibility of optimization. The historical literature on serial reaction control and general matrix rearrangements is broad; independent priority checking, especially older optimal-control treatises, remains warranted. This is a mathematical scheduling benchmark, not a calibrated biological intervention.

## References

1. Bak, T. A., Salamon, P., and Andresen, B. (2002), *Optimal Behavior of Consecutive Chemical Reactions A↔B↔C*, Journal of Physical Chemistry A 106, 10961–10964. Published online September 19, 2002. DOI: https://doi.org/10.1021/jp021800u. Author-hosted full text: https://www.fys.ku.dk/~andresen/BAhome/ownpapers/ABC.pdf.
2. Yin, X. (2008), *Analysis of Reciprocal-transfer Experiments to Estimate the Length of Phases having Different Responses to Temperature*, Annals of Botany 101, 603–611. Published online January 17, 2008. DOI: https://doi.org/10.1093/aob/mcm319.
3. Carrington, L. B. et al. (2013), *Large Diurnal Temperature Fluctuations Negatively Influence Aedes aegypti Life-History Traits*, Journal of Medical Entomology 50, 43–51. DOI: https://doi.org/10.1603/ME11242.
