# Review: Globally optimal two-time worst-direction observation of a damped planar rotation

## Correctness — PASS
For every damping and frequency pair, the two-row Fisher matrix reduces by a common rotation and positive attenuation to first time zero. The smaller eigenvalue solves a quadratic with trace \(1+q\) and determinant \(q\sin^2 z\). Its derivative is positive or negative according to a scalar \(F\); every zero of \(F\) has \(F' < 0\), establishing one strict maximizer on \((0,\pi/2)\), while all later lobes lie below the first half-period endpoint. E/D timing separation and both asymptotic expansions follow from that exact stationarity relation and a localized nondegenerate limiting maximizer. The Python verifier reconstructs Gramians independently as a supplementary numerical check; no finite grid is used as an infinite-domain proof.

## Originality — PASS (qualified)
Inspected primary full text on randomized observability Gramian sensor selection, finite-horizon Kalman prediction-budget allocation, and first-order trigonometric-regression E-optimal design. Unlike the present two fixed equal-noise observation-time design of a normal damped oscillator, these sources respectively treat spatial randomized sampling, different averaged prediction objectives, and undamped trigonometric approximate-design settings. A diffusion-timing parameter-estimation source was only partially accessible. Actual semantic published-finding corpus queries retrieve related three-time determinant-optimal oscillator observations and jittered-time conditioning, but no equivalent two-time exact E-optimal classification. No exhaustive novelty claim or independence claim is made; older damped sinusoidal design formulations may exist.

## Value — PASS
Two observations are the minimal budget for observing two unknown planar coordinates with a fixed scalar sensor. The exact E-optimal delay, its strict separation from the D-optimal delay, and asymptotically sharp weak/strong damping laws characterize a natural minimax initial-state sensing problem with an explicit usable timing prescription. The result does not imply a broader arbitrary-dynamics theorem or a physical sensing speedup.

## Closest literature and scientific limits
- S. D. Bopardikar, *Sensor Selection via Randomized Sampling*, arXiv:1712.06511 (2017-12-18): full preprint inspected including theorem on Gramian and sampled subsets; its random spatial sensor-selection setup does not entail the optimal two continuous observation times here.
- A. Aspeel and collaborators, *Optimal measurement budget allocation for Kalman prediction over a finite time horizon by genetic algorithms* (2021), DOI 10.1186/s13634-021-00732-8: inspected full open-access article; different mean prediction error and genetic search objective.
- H. Wu, *Optimal designs for first-order trigonometric regression on a partial cycle*, *Statistica Sinica* **12** (2002): inspected full paper, including its E-optimal and approximate-design arguments; undamped harmonic regression with freely weighted design measures, not this exponential-amplitude fixed two-point restriction. Older equivalent weighted-design formulations are a real residual originality risk.
- A. Javeed and G. Hooker, *Timing observations of diffusions* (2019): accessible abstract and some appendix; complete text unavailable; parameter estimation of diffusions is not direct proof of coverage, but residual priority risk remains.
- Related published-finding corpus records include three-time oscillator D-optimality, jittered-time conditioning, and four phaseless sample designs. Their indexed claims do not imply the current exact two-time E-optimal theorem; their full source was not materially inspected.

All correctness, originality, and value assessments are limited to the specified domain and examined material. The finite cross-checks do not prove the infinite-domain claim. Independent review and priority validation have not occurred.

Self-review: passed. Independent audit: not yet performed.
