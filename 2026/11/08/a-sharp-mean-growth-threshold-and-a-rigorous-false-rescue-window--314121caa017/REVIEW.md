# Mathematical review

## Correctness: PASS

The moment exponent follows from the irreducible four-state positive generator and its involution symmetry. The strict threshold is a determinant identity, and the almost-sure gap is obtained by an exact positive-eigenvector martingale identity with a nonnegative entropy integrand. Invariance and eventual entry of the Riccati ratio into a compact interval, together with the exponential renewal strong law, yield a strict positive time-average entropy loss. The rational witness is proved using explicit rational inequalities, with no dependence on floating-point sampling. The accompanying standard-library verifier replays 942 finite checks, including a separate four-state eigenvalue comparison. Universal claims are derived analytically, not inferred from these finite tests. Main dependencies: exponential-renewal and bounded-jump-martingale strong laws.

## Originality: PASS within inspected evidence; historical priority provisional

The generic distinction between stochastic and average growth already appears explicitly in Tuljapurkar, Horvitz and Pascarella (2003), whose available author-uploaded original text was inspected. The general moment-generator methodology falls under existing Markov switching results, including Ogura and Preciado (2015), whose original nine-page arXiv preprint was inspected. Neither establishes the particular symmetric transpose-recruitment two-patch threshold \(\kappa_*=(a^2-bc)/(b+c-2a)\), the strict all-parameter interval of positive mean growth with almost-sure collapse, or its quantitative exact rational certificate. Bao and Shao (2016) is nearby in population switching but concerns nonlinear predator–prey dynamics and was accessible here only through its abstract. Searches of published mathematical research records for aliases and claimed implications did not surface the same result; absence in search is not proof of novelty. The precise restricted theorem, not the underlying general moment/path distinction, is the proposed new claim.

## Value: PASS

A sharp and nonempty false-rescue parameter region gives an exact limitation of first-moment risk assessment in an interpretable two-habitat low-density model even when both static regimes decline. The rational bound distinguishes a mathematical strict sign reversal from Monte Carlo observations or a generic Jensen inequality. The structural mechanism and sharp switching-rate threshold can be used as benchmarks in environmental demographic models. The example does not prove robustness under nonlinear feedback or demographic noise.

## Closest sources, caveats and remaining risks

Tuljapurkar et al. (2003), doi:10.1086/378648, is the closest conceptual predecessor and establishes the generic growth-rate split in a distinct discrete-time setting. Ogura and Preciado (2015), arXiv:1501.03474, provide a general mathematical framework that could in principle be specialized, but no inspected theorem states the exact claimed family. Bao and Shao (2016), doi:10.1137/15M1024512, was checked at abstract level only; an uninspected full text could contain further related inequalities. Broad switching-system literature is extensive, so an unlocated exact specialization remains an originality risk. The model is linear and uses off-diagonal recruitment, not conservative migration; no ecological field validation is claimed.

Self-review: passed. Independent audit: not yet performed.
