# Scientific self-review

## Correctness: PASS

The claim is restricted to fixed \(c\in(0,1)\), \(0<p<(3+\sqrt{1-c})/4\), and compact time horizons. The source gives the exact innovation recursion and compact-log-time deterministic coefficient convergence. The additional proof supplies an independent square-summable, sub-square-root coefficient envelope through a positive renewal comparison for positive reinforcement (and a convex-combination bound for negative reinforcement); it obtains the required almost-sure vanishing local bias from exponential martingale concentration. Riemann-sum Gram limits, the martingale-array CLT, and a uniform fourth-moment increment estimate yield finite-dimensional convergence and path tightness. The covariance derivative follows by a justified integration by parts. Exact finite-path enumeration gives 4,196 passing rational assertions and tests the innovation Gram identities, without being misrepresented as an infinite proof.

The proof is conditional on the precise compact-log-time coefficient convergence established in Hu--Xue's Lemma 3.6, but it independently rederives the coefficient envelope needed for functional tightness. There is no assertion about rates or the phase boundary.

## Originality: PASS relative to inspected evidence

Hu and Xue prove a one-time central limit theorem, not a functional one: their Theorem 1.2 identifies only \(S_n/\sqrt n\). The fixed-recent-memory functional theorem of Vázquez-Guevara and González-Navarrete has memory length independent of time, while Tokumitsu's dynamic elephant walk conditions on the cumulative past rather than a sliding window. The smoothly amnesic step-reinforced walks of Bertenghi and Laulin, and of Coletti, dos Santos and Valle, use strictly positive sampling weights over old times rather than a hard proportional recent cutoff. The new kernel is therefore not an immediate change of parameters in any of those inspected theorems. An earlier general martingale-array principle could conceivably imply this specialization; no exhaustive historical priority assertion is made.

## Value: PASS

The one-time Gaussian limit does not determine path-level dependence. The functional theorem supplies a full stochastic-process limit suitable for path observables, and reveals a sharp structural distinction between positive reinforcement, negative reinforcement and neutral memory through the sign of a covariance derivative. It distinguishes Brownian diffusive scaling from Brownian independent-increment behavior in the very model where a proportional recent window first yielded a scalar phase transition.

## Closest literature and residual risks

- Hu and Xue, arXiv:2611.17664v1, Theorem 1.2 and Lemmas 2.1 and 3.6: exact model and scalar theorem, credited input.
- Vázquez-Guevara and González-Navarrete, arXiv:2506.12145v1, model (1.2) and Section 3: fixed-width dependence, not a proportional-width theorem.
- Tokumitsu, arXiv:2507.01708v1, equation (1.1) and Theorem 1.1: cumulative-past drift, not sliding-window drift.
- Bertenghi and Laulin, arXiv:2402.09202: globally weighted amnesia model.
- Coletti, dos Santos and Valle, arXiv:2609.14871: globally weighted amnesia with random step sizes.

Mathematical priority risk remains around broad deterministic-kernel martingale functional limit theorems that may have implicit special cases. Critical and superdiffusive regimes, parameter sequences and convergence rates are outside the result. Independent scientific review has not been performed.

Self-review: passed. Independent audit: not yet performed.
