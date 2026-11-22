# Scientific review: midpoint-riffle inversion law

## Correctness

PASS. Conditional on any cut, reflection of pairs of packet-midpoint keys exchanges earlier and later relations for every strictly ordered cross-packet pair. Exactly half of the non-tied pairs are inverted, and independent fair tie coins produce the conditional binomial term. The proof derives the exact mean and variance using the second and fourth centered moments of a symmetric binomial, and derives the limiting reflected chi-square distribution via the binomial CLT with an explicit negligible tie-noise bound. The GSR comparison follows from an exact independent-binary-label decomposition into a weighted linear term and a centered quadratic term, which are uncorrelated and have exactly evaluated variances. Lindeberg and a second-moment bound give its Gaussian limit. The embedded checker corroborates finite distributions and moments through stated sizes but is not used to infer the all-size theorem.

## Originality

PASS under the examined literature, with residual historical-priority risk. Jiang's arXiv:2611.02092v1 develops the same midpoint shuffle and computes the tie count, but its inspected model, inversion-related, bounds and limitations passages do not state the complete one-step inversion law, its reflected-chi-square limit, or the exact GSR variance-suppression comparison. The prior tie-count result is credited. Classic GSR inversion enumeration and fluctuation calculations concern the uniformly random interleaver, not midpoint sorting; that comparator is not claimed as newly discovered. A related published midpoint-riffle group-generation result concerns odd-deck irreducibility rather than the inversion statistic. A published correlated-label inverse-riffle inversion regime concerns a different shuffle. The inaccessible full text of the group-generation result leaves a bounded risk that it contains additional inversion computations not described in its indexed summary. The explicit novelty is confined to the midpoint law and scale contrast; searches alone do not certify priority.

## Value

PASS. The two shuffling mechanisms have exactly the same binomial distribution of cuts and the same mean inversion count, yet midpoint sorting cancels essentially all within-cut inversion noise. It changes the variance order from cubic to quadratic in deck size, with an exact sharp ratio on odd decks, and changes the limit from a Gaussian to a one-sided, reflected chi-square distribution. This is a natural quantitative diagnostic of the interleaving mechanism in a recently introduced shuffle, not an arbitrary parameter slice or a minor numerical improvement. The precise finite distribution is meaningful independently of a mixing theorem.

## Closest literature and limitations

The motivating source is Jiang, *Adhesive riffle shuffles*, arXiv:2611.02092v1, §§2--4 and 13. Classical GSR benchmarks are documented by Bayer--Diaconis (1992), Diaconis--Fulman (2023) and Sellke--Shi--Wang (arXiv:2510.22783). The published-finding corpus record titled *Odd-deck midpoint riffles generate the full symmetric group* concerns group support and convergence, and the record *Three-scale inversion laws for correlated-label inverse riffle shuffles* concerns a distinct stochastic interleaver. The findings are only about one step from the ordered deck; no total-variation mixing rate, cutoff, positive-adhesion law, or independent mathematical validation is asserted.

Self-review: passed. Independent audit: not yet performed.
