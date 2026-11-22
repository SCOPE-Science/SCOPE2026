# Scientific assessment

## Correctness — PASS

The model's sample miss probability is obtained by conditioning on DNA availability, and independence multiplies it over samples. The strict concavity of the per-sample negative log failure probability produces a single continuous maximum; strictly increasing adjacent-efficiency ratios produce exactly one switch for each integer count above the initial optimum. Strict single-peakedness prevents skipped counts, while expansion at fixed scaled failure \(1-p=k(1-q)^m/m\) yields the sharp asymptotic coefficient. The relaxed logarithmic and log-log terms are independently obtained from the unique stationary equation. The standalone checker reproduced the specified numerical threshold examples and broader finite diagnostics. Numerical checks are not used as proof of universal assertions.

## Originality — PASS with provisional historical priority

Schmidt et al. (2013), DOI 10.1111/2041-210X.12052, and Willoughby et al. (2016), DOI 10.1111/1755-0998.12531, provide the motivating hierarchical field-capture/PCR model; the inspected full articles do not give an optimized cost-normalized PCR-replication staircase. Moore et al. (2014), DOI 10.1371/journal.pone.0115345, and Smart et al. (2016), DOI 10.1111/2041-210X.12598, optimize field visits/samples under different time-varying detection models, rather than the present nested Bernoulli laboratory replicate count. Lugg et al. (2018), DOI 10.1111/2041-210X.12951, fit a three-level model with a fixed number of PCRs; they optimize the field/site design rather than the PCR count. The closest accessible published-finding corpus occupancy findings concern coarsened detection or Fisher-information allocation, not this target and objective. No inspected primary source establishes the ordered no-skip switching probabilities or the exact asymptotic \(1-p_m\sim (a/b)c(1-q)^{m+1}/[qm]\). The 2014 work on eDNA replicate levels was available as abstract rather than complete full text, so this remains an explicitly limited originality review, not a historical uniqueness certification.

## Value — PASS

Field capture and laboratory amplification are different kinds of imperfect detection with different costs. The theorem resolves the exact direction and sequence of PCR-replication changes, and the geometric-over-linear threshold tells how close to certain field DNA capture must become before an additional PCR count is cost-optimal. It refines the qualitative claim that extra PCRs have diminishing returns with a natural, model-specific, experimentally parameterizable phase diagram; the log-log correction identifies the boundary of the high-capture regime. It does not claim instrument realism or a model-independent field recommendation.

## Closest literature and residual limits

The three-level observation model predates this analysis, and optimization frameworks for survey effort predate it as well. This result is confined to cost-normalized negative log missed-detection, independently repeated PCRs within each captured sample, and no false positives. Other cost models or posterior-estimation objectives need fresh optimization. Possible earlier analytic treatments of a mathematically equivalent nested Bernoulli efficiency objective were not exhaustively ruled out. The abstract-only Ficetola et al. (2014) replication analysis is a residual literature-access risk.

Self-review: passed. Independent audit: not yet performed.
