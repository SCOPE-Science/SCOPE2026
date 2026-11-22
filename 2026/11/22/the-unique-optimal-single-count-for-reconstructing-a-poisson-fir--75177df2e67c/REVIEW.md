# Scientific review

## Correctness (PASS)

The claim is restricted to a homogeneous known-rate Poisson process, one deterministic cumulative count, its unbounded first-arrival time, and squared error. Given zero observed events the residual first-arrival time is exponential; given a positive count the first event is the minimum of independent conditional uniform locations. Those conditional expectations establish the exact Bayes rule. The entire factorial series reduces the Bayes risk to an exponential-integral expression. Differentiating twice yields a strictly concave critical-point function whose derivative vanishes at zero and is thereafter negative. It crosses zero exactly once, establishing a global minimizer rather than a local numerical guess. Independent Poisson-series and symbolic checks replayed from the packaged source support the calculations; finite tests are not the infinite proof.

## Originality (PASS, provisional historical priority)

The strongest directly relevant inspected primary result, Przybyłowicz (2017), concerns asymptotic global error and optimal multiple-time sampling of jump-diffusion paths, not a one-count finite-information first-arrival estimator. Przybyłowicz, Sobieraj and Stępień (2021) concern Euler schemes and complexity. Hornberger (2025) treats periodic arrival observations and parameter/mixing behavior, not optimization of a single count time for first-arrival squared risk. Comparisons with related published work on Poisson count sampling and event-time detection concern different observation models or target functionals. No equivalent or dominating result was located in the inspected sources. Standard conditional-uniform and exponential facts are not claimed new. Risk: historical prior art outside searchable or inspected sources may exist, including textbooks and older experimental-design treatments.

## Value (PASS)

A one-query event counter must be queried at a time chosen in advance when only the first-event timing matters. The theorem supplies the exact intensity-scaled observation time, a unique numerical design root, and an absolute minimum risk with no timestep or large-sample approximation. Recording the complete count instead of only the event-presence bit reduces even the best binary-sensor risk by about 8.70%; the exact optimal risk is about 32.17% of the no-query risk. The specific event-time target, one-query information constraint and comparison make this a substantive sampling decision rather than an arbitrary special-function evaluation. It does not imply optimality for unknown rate, multiple queries or other targets.

## Literature risk and limitations

The source comparison is about claims and quantifiers: global-path asymptotics, jump-SDE pointwise complexity and periodically observed rate/mixing results do not imply the claimed all-rate exact single-count first-event optimum. A historical-priority risk remains because the literature search is not exhaustive. No external independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
