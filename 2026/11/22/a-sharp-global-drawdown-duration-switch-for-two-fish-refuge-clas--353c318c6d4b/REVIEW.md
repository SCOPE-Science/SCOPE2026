# Scientific review

## Correctness — PASS

The claim specifies all positive rates, the full decision domain \(T\ge0\), two strictly ordered fixed travel requirements and the independent, whole-event mortality assumption. Direct independence gives the survival probability. Separating the two smooth domains at the slow-class travel time reduces each to a difference of exponentials with one strict maximum; the comparison uses valid unrestricted upper bounds and separately proves that both relevant maxima are inside their actual branches at the tie. Strict convexity of the power functions establishes feasibility and the critical strict inequalities. The resulting global argmax trichotomy includes equality, the joining time and all admissible boundaries. A rational witness has exactly two co-global maxima of height \(1/24\), separated by a lower joining value \(1/32\). A Python standard-library checker passed 5,000 seeded parameter trials with 1,505,000 time-grid evaluations and 5,000 nonsmooth-join checks, plus 20 exact-threshold numerical identities. These finite tests are not treated as infinite proofs.

## Originality — PASS on inspected evidence, subject to historical priority

The nearest prior mathematical result is *A sharp reentrant two-peak window for delayed unequal Bateman inputs* (2026; full RESULT text inspected), which already proves mode counts, turning-point formulas and a reentrant two-peak regime for delayed response mixtures. The present survival curve is algebraically a *special constrained shifted-Bateman mixture*, so these published mathematical facts are explicitly prior, not re-claimed. In contrast, the published result does not supply global dominance of the two peaks along the biologically constrained amplitude-delay path, the single sharp maximizing-duration switch, the complete co-global equality set, or the exact finite jump formula. These are proved separately here. The ecological sources (Hedger et al. 2023, Hayes et al. 2019, Le Coarer et al. 2022/2023) discuss hydropeaking stranding and ramping but not the stated two-class optimal-duration theorem. Actual published-finding corpus semantic searches of aliases, mode/maximum comparison, refuge and heterogeneous mortality were made, and relevant published mathematical claims were compared by content rather than only titles. Absence from inspected results is not a uniqueness proof; a more general exponential-mixture maximum-dominance theorem could subsume it, and some relevant environmental articles were not fully accessible.

## Value — PASS

The newly resolved question is the global design choice rather than the mere existence of two peaks: stage heterogeneity can make a single mathematically optimum drawdown duration jump between widely separated alternatives, whereas a homogeneous response model always has one continuously varying optimum. The exact boundary, universal positive jump and full classification identify a testable mechanism for sensitivity and offer a benchmark for more realistic fish-passage simulations. It is not merely a normalization or numerical gain. The decisive physical limitation is that refuges do not stop the modeled exposure-mortality clock early; field design requires validation of this premise and of the latency distribution.

## Closest sources and limits

- Hedger et al. (2023), *Exploring sensitivities to hydropeaking in Atlantic salmon parr using individual-based modelling*, doi:10.1002/eco.2553, first online 2023-04-24. Accessible full study inspected; ecological motivation rather than mathematical coverage.
- Hayes et al. (2019), *Life Stage-Specific Hydropeaking Flow Rules*, doi:10.3390/su11061547. Full accessible article inspected; stage-specific field-design background.
- Le Coarer et al. (2023), *Horizontal ramping rate framework to quantify hydropeaking stranding risk for fish*, doi:10.1002/rra.4087, first online 2022-12-05. Abstract and accessible partial text; full article not confirmed read.
- *A sharp reentrant two-peak window for delayed unequal Bateman inputs* (2026), full published RESULT inspected, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-reentrant-two-peak-window-for-delayed-unequal-bateman-in--2eb46436a2c9. Directly related mathematics, but global winner/crossover not the published claim.

Independent field or scientific audit has not been performed. A published-finding corpus search, even accompanied by full inspection of the nearest source, is not a complete mathematical priority certification.

Self-review: passed. Independent audit: not yet performed.
