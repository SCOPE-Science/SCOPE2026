# A sharp temporal sorting law for fragmentation under size-selective marine loss

## Finding

Let the expected mass of a single marine-plastic batch occupy fragment-generation classes \(0,1,\ldots,J\), with \(J\ge1\). In each observation interval, every class except \(J\) transfers a fraction \(p\in[0,1]\) of its mass to the next (finer) class and retains the rest, while class \(J\) cannot fragment further. After this transition, fractions \(s_j\in(0,1]\) survive in class \(j\). The total input batch and the multiset of interval fragmentation fractions are fixed; no new plastic is introduced during the intervals.

**Universal temporal-rearrangement theorem.** For every finite collection of fragmentation fractions, every nonnegative initial size-class mass vector, and every final size class simultaneously, arranging the fragmentation fractions in *nondecreasing* chronological order maximizes final surviving mass over all permutations if and only if
\[
s_0\ge s_1\ge\cdots\ge s_J.
\]
Arranging the fractions in nonincreasing chronological order similarly maximizes every final class for all such inputs if and only if the survival fractions are nondecreasing. If every survival fraction is equal, every order is exactly equivalent. If the survival profile has both a strict rise and a strict fall, neither sorted orientation is universally best across all possible initial batch profiles; two intervals already witness opposing preferences. These conditions are sharp and include equal fractions, zero fragmentation, and arbitrary terminal-class accumulation.

In particular, **when finer fragments suffer more loss, later (rather than earlier) high fragmentation maximizes surviving mass in every size bin at once**. This is a size-resolved result, stronger than a claim about total retained mass alone.

## Assumptions and scope

The class index counts *equal-mass halving generations*, not necessarily physical sieve diameters: a fragmentation event turns one parent into two daughters whose combined mass equals the parent's mass. The state variables below are expected *mass*. If generation-zero particles have a common mass \(m_0>0\), every generation-\(j\) particle has mass \(m_0 2^{-j}\), and the corresponding expected count is \(2^j x_j/m_0\). This fixed positive classwise rescaling preserves the entire componentwise theorem. There are \(J+1\) classes with a hard lower fragmentation cutoff at \(J\). All classes use the same interval fragmentation probability \(p\) except the absorbing smallest class; the probability may differ between intervals. Survival is multiplicative and stationary across intervals, and occurs **after** fragmentation in each interval. There is no aggregation, immigration, exchange between ocean regions, or size-dependent variation in the fragmentation probability within a given interval. Surviving mass fractions \(s_j\) are strictly positive. The theorem concerns the algebraic model, not a claim that oceanic size-selective loss is universally monotone.

For a column vector \(x\in\mathbb R_{\ge0}^{J+1}\), define the capped forward shift by \(Ue_j=e_{j+1}\) for \(0\le j<J\), and \(Ue_J=e_J\). Set \(B=U-I\), \(D=\operatorname{diag}(s_0,\ldots,s_J)\), and
\[
T(p)=D(I+pB).
\]
For chronological fractions \(p_1,\ldots,p_N\), surviving class masses are \(x_N=T(p_N)\cdots T(p_1)x_0\). Coordinatewise comparison is the usual componentwise order in \(\mathbb R^{J+1}\).

## Proof

Every \(T(p)\) is entrywise nonnegative: for \(j<J\), its only possibly nonzero entries in column \(j\) are \(s_j(1-p)\) in row \(j\), and \(s_{j+1}p\) in row \(j+1\); the final column has \(s_J\) at row \(J\). Thus multiplying a coordinatewise inequality by a common prefix or suffix of such matrices preserves its direction.

Fix \(p>q\). Since \(T(p)=D+pDB\), exact multiplication gives
\[
T(p)T(q)-T(q)T(p)=(p-q)(DBD-D^2B).
\]
The matrix on the right has no nonzero entries except possibly on the first subdiagonal, with
\[
[DBD-D^2B]_{j+1,j}=s_{j+1}(s_j-s_{j+1}),\qquad 0\le j<J.
\]
Indeed, its diagonal cancels because diagonal matrices commute with the diagonal of \(B\), and the cap gives no subdiagonal entry beyond \(J\). Consequently
\[
T(p)T(q)\ge_{\rm cw}T(q)T(p)\quad\Longleftrightarrow\quad s_j\ge s_{j+1}\text{ for every }j<J.
\]
Here \(T(p)T(q)\) means **the smaller fragmentation fraction \(q\) first and the larger \(p\) second**. For \(s_0\ge\cdots\ge s_J\), any inversion in a chronological schedule can be removed by swapping an adjacent larger-then-smaller pair. The displayed nonnegative difference, multiplied by the common pre- and post-swap transition products and initial nonnegative vector, preserves coordinatewise order. Repeated adjacent swaps produce the nondecreasing schedule, establishing its simultaneous maximality for all bins. Reversing the swap argument gives the nonincreasing schedule as a simultaneous minimum.

For the sharp converse, if \(s_j<s_{j+1}\) at any index, choose \(x_0=e_j\) and two intervals \(q<p\). Then the \((j+1)\)-st coordinate of \(T(p)T(q)x_0-T(q)T(p)x_0\) is exactly \((p-q)s_{j+1}(s_j-s_{j+1})<0\). Hence nondecreasing chronology is not universally maximizing. Conversely, if \(s_j>s_{j+1}\), the same witness disproves universal optimality of nonincreasing chronology. Constant survival makes every commutator zero, so adjacent swaps leave the entire vector unchanged. A profile with both a strict rise and fall supplies two incompatible two-interval witnesses. This completes the necessary-and-sufficient classification.

## Verification

The standalone `verify.py` uses only Python's standard-library `fractions` and `itertools` for the exact rational arithmetic and permutation tests. It checks the exact commutator coefficient for \(J+1=2,\ldots,7\), sampled rational inputs, and all distinct permutations of sampled four-interval schedules, with explicit examples for both survival directions. These finite checks corroborate, but do not replace, the all-parameter symbolic proof above.

For an exact illustration, take \(J=3\), \((s_0,s_1,s_2,s_3)=(1,3/4,1/2,1/4)\), \((q,p)=(1/4,3/4)\), and \(x_0=e_0\). Small-then-large fragmentation yields surviving masses
\[
(3/16,\,117/256,\,9/128,\,0),
\]
whereas large-then-small yields
\[
(3/16,\,93/256,\,9/128,\,0).
\]
The precise gain in class one is \(3/32\), with all other classes unchanged after these two intervals.

## Relationship to prior work

George, Nallet and Fabre (arXiv:2307.04162, initially public July 9, 2023) investigate deterministic and stochastic fragmentation, a small-size cutoff and growing environmental plastic input. Their preprint includes size-class recurrences and discusses sinking as an alternative explanation for small-particle depletion, but its inspected model does not derive a temporal ordering theorem for a fixed batch subject to both fragmentation and class-dependent survival. Kaandorp and colleagues (2022) model marine fragmentation together with size-dependent transport; Lobelle and colleagues (2021) study the size-dependent sinking context.

The algebraic adjacent-swap method is related to general rearrangement and stochastic scheduling ideas (Chang and Yao, 1993). Hsiau, Chen and Yao (2021), Theorems 1–2, give stochastic ordering of the killing time with respect to the initial state in birth–death processes, not ordering of chronological transition schedules for a common initial state. The specific if-and-only-if size-resolved capped-cascade theorem is the narrow contribution, not a claim of inventing interchange proofs or fragmentation matrices. Historical priority is not certified.

## Limitations

The result is conditional on an idealized stationary *survival-by-fragment-class* profile, the same fragmentation fraction at every nonterminal class per interval, one-step generation transitions, strictly positive survival, and a batch with no further source input. Real sinking can depend nonmonotonically on size, density, biofouling, turbulence, geography and time; separate sources may enter in different years. The count conversion requires a fixed particle mass per bin as specified above; it does not justify an inference about counts in sieve bins with variable mass per particle. The theorem compares final retained mass by generation, not ecological harm, toxicity or real-world management objectives. No field-data calibration or experimental confirmation is claimed.

## References

1. M. George, F. Nallet and P. Fabre, *A threshold model of plastic waste fragmentation: New insights into the distribution of microplastics in the ocean and its evolution over time*, arXiv:2307.04162, first posted 2023-07-09. https://arxiv.org/abs/2307.04162
2. M. L. A. Kaandorp et al., *Influence of Particle Size and Fragmentation on Large-Scale Microplastic Transport in the Mediterranean Sea*, Environmental Science & Technology 56 (2022), 15528–15540. https://doi.org/10.1021/acs.est.2c03363
3. D. Lobelle et al., *Global Modeled Sinking Characteristics of Biofouled Microplastic*, Journal of Geophysical Research: Oceans 126 (2021), e2020JC017098. https://doi.org/10.1029/2020JC017098
4. C.-S. Chang and D. D. Yao, *Rearrangement, Majorization and Stochastic Scheduling*, Mathematics of Operations Research 18 (1993), 658–684. https://doi.org/10.1287/moor.18.3.658
5. S.-R. Hsiau, M.-R. Chen and Y.-C. Yao, *Stochastic ordering for birth–death processes with killing*, Journal of Applied Probability 58 (2021), 708–720. https://doi.org/10.1017/jpr.2021.1
