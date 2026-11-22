# Scientific review

## Correctness — PASS
The model specifies independent nonnegative exponential passage/mortality clocks and an Erlang-2 alternative, both with identical passage means. Integrating passage density times mortality survival gives the two closed forms. Their derivative difference is \(e^{-(2+a)x}(4x-e^x)\), so precisely two stationary locations occur for every mortality rate. Multiplying the interior maximum by \(e^{ax_-}\) proves strict monotonicity in the mortality parameter and yields one critical rate. Endpoint signs prove zero, one, or two crossings in each exact regime. The independent standard-library checker covers numerical integration, threshold roots, sign patterns and endpoints; finite checks complement rather than establish the proof.

## Originality — PASS, subject to historical-priority risk
Castro-Santos and Haro (2003) provide time-to-event methodology for fish passage, but their inspected article material does not show an equal-mean exponential/Erlang-2 deadline comparison with constant independent mortality. Castro-Santos and Perry (2012) discuss time-to-event and competing-risk passage analysis. Silva et al. (2018) discuss fishway performance and timing. Kochar and Xu (2010) study a different spread order for sums of exponentials. Searches for equal-mean Erlang/exponential discounted finite-deadline success and published indexed mathematical findings identified no matching complete threshold theorem. A standard stochastic-ordering theorem or less-visible competing-risk treatment could imply this classification; historical priority is not definitively established.

## Mathematical and applied value — PASS
The comparison isolates a concrete modeling ambiguity in migration performance: matching mean passage time does not fix the probability of surviving and completing passage by a management deadline. For a positive but not-too-strong mortality hazard, the same designs exchange ranking twice as the deadline changes; increasing mortality removes that finite window at an exactly characterized cutoff. This gives a reusable sharp benchmark for choosing or evaluating waiting-time assumptions, not a claim that a real fishway can realize either waiting-time law.

## Limits and sources
The result concerns one isolated passage operation with independent, stationary mortality, exactly equal mean passage time, and exact model probabilities; no field calibration or estimation uncertainty is addressed. Principal motivating sources are Castro-Santos and Haro (2003), https://doi.org/10.1139/f03-086; Castro-Santos and Perry (2012), https://www.usgs.gov/publications/time-event-analysis-a-framework-quantifying-fish-passage-performance; Silva et al. (2018), https://doi.org/10.1111/faf.12258; and Kochar and Xu (2010), https://doi.org/10.1016/j.jmva.2009.07.001.

Self-review: passed. Independent audit: not yet performed.
