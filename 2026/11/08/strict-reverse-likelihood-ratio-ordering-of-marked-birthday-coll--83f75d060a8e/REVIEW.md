# Self-review

## Correctness (C): PASS

The event \(\{C=i,T=t\}\) has precisely \((t-1)!\) arrangements for any fixed set of \(t-2\) other distinct initial labels, yielding the joint formula with \(p_i^2\) and an elementary symmetric polynomial. For \(p_i>p_j\), separating both compared probabilities reduces adjacent likelihood-ratio differences to \((p_i-p_j)(E_k^2-E_{k-1}E_{k+1})\), strictly positive by Newton's inequalities and the checked zero-index boundary conventions. The two-label case is included. Positive joint entries ensure conditional likelihood-ratio and stochastic order, and nonproportionality proves nonindependence unless all probabilities agree. An executable exact-rational check independently enumerates several small cases and tests 201,721 assertions; it is supplementary to the proof. No unsupported infinite extrapolation is used.

## Originality (O): PASS, subject to stated historical risks

The nearest fully inspected paper is Camarri–Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities*, whose Section 3.1 formulas (1), (2), and (13) describe unmarked first-repeat times and sampled sets, not the family of conditional laws indexed by the first repeated label. The accessible Flajolet–Gardy–Thimonier report, Section 3, gives symmetric-polynomial expectations of unmarked birthday waiting times; the present strict pairwise reverse likelihood-ratio ordering is not stated there. The Fadnavis paper concerns no-collision probability/majorization, rather than conditional collision-type ordering. The closest accessible results provide counting ingredients, but the all-pairs sign of the two-by-two joint minors and the conditional stochastic-order statement are not direct prior assertions. Searches for equivalent terms (marked first collision, reverse total positivity, conditioned repeated species, elementary symmetric likelihood ratios), broader results, and exact tables produced no decisive coverage. The full text of Holst (1995), on general unequal birthday problems, was not accessible, so unrecognized coverage remains a substantive risk. This is a self-review of originality, not independent priority certification.

## Value (V): PASS

The repeated category identifies which high-frequency item caused a collision in nonuniform hashing, rare-event detection, occupancy sampling and classical birthday models. A smaller *unconditional* expected first-repeat time under more concentrated weights does not answer the conditional question: how the time changes when the identity of the first repeated type is observed. Strict likelihood-ratio ordering provides simultaneous comparisons for **every** increasing loss of elapsed time and is stronger than a comparison of conditional means. The result also supplies an exact structural characterization of when repeat time and repeat type are independent. These are natural properties of the complete marked waiting-time distribution rather than isolated, arbitrarily chosen finite examples.

## Closest literature and limitations

Camarri–Pitman (1998 report; 2000 article), Flajolet–Gardy–Thimonier (1987 report; 1992 article), Holst (1995), and Fadnavis (2011) are the principal comparisons; see RESULT.md and AUDIT.json for exact identifiers and material assessed. The historical claim that no previous source implies the result is not certified. Strict positivity, finiteness, and iid sampling are necessary hypotheses of the stated theorem; no extension to later repeats or unequal-time distributions is proved.

Self-review: passed. Independent audit: not yet performed.
