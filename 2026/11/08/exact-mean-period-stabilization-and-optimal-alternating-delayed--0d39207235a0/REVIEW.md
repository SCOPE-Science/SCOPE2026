# Scientific review: exact two-periodic delayed-sample stabilization

## Correctness — PASS

The precise controller uses a previous-sample hold on an integrator, giving \(x_{k+1}=x_k-h_kx_{k-1}\). Direct multiplication gives Floquet trace \(1-a-b\) and determinant \(ab\). The strict degree-two Jury test produces \(ab<1\) and \(ab>a+b-2\), without missing boundary cases. At fixed mean \(m=(a+b)/2\), all admissible products cover \(0<ab\le m^2\). These observations establish the complete stability regime, including the strict, unattained upper mean \(3/2\). The eigenvalue-sum inequality \(\rho(F)\ge m-1/2\) for \(m\ge1\) has equality only at a negative double root, which yields the unique positive unordered interval pair and verifies its asymptotic optimality. A nontrivial Jordan block is explicitly disclosed. The standalone symbolic verifier passed 2,809 assertions and confirms the exact rational illustration. The mathematical continuum proof is independent of the finite numerical checks.

## Originality — PASS, with explicit precedence risk

A fixed-delay, equally spaced sampled-data model and its companion-matrix analysis are present in García–Aguirre–Suárez (2008). Aperiodic sample-and-hold stability under current-sample feedback and robust upper sampling bounds are present in Berberich et al. (2020), Wildhagen et al. (2021), and Vallarella–Haimovich (2022). Jin–Wang–Wang (2022) already study mixed short/long sampling intervals and improved mean sampling intervals, so the qualitative improvement from mixing sampling intervals is not novel. In contrast, the claim here is an exact necessary-and-sufficient two-periodic **one-index-lagged** stability classification, a sharp universal mean limit, and a uniquely minimizing two-interval Floquet schedule. Those statements were not found in the inspected accessible material or indexed overlapping claims. The last cited article's full text was inaccessible, and unindexed equivalent work cannot be excluded. Search absence is not used as a proof of novelty.

## Value — PASS

The exact complete classification answers a natural scheduling question in digital feedback with one outstanding measurement: whether a controller may safely reduce the *average* sampling frequency beyond the uniform stability limit. It shows a sharp fifty-percent improvement in the supremal mean and gives the unique fastest two-periodic design, while identifying a stability window between too little and too much imbalance. These are nontrivial design boundaries for a standard delayed measurement model, rather than isolated numerical examples. The result does not claim robustness for arbitrary jitter or that the spectral-rate optimizer minimizes finite-horizon transient amplification.

## Closest literature and limitations

- García, Aguirre and Suárez (2008), DOI 10.1155/2008/270518: a closely related scalar delayed-feedback model with a *fixed physical delay and equal spacing*, not the present variable one-index delay.
- Berberich et al. (2020), arXiv:2011.09221: general robust aperiodic sampling, with control using the current sampled state; a different optimization objective.
- Wildhagen et al. (2021), arXiv:2103.14353: model/data-based sufficient stability conditions under varying discrete sampling, not a sharp fixed-average two-periodic delayed law.
- Vallarella and Haimovich (2022), arXiv:2202.10549: stability transfer to continuous-time limits under varying intervals, not the exact repeated two-step lagged model.
- Jin, Wang and Wang (2022), DOI 10.1080/00207179.2022.2069051: abstract directly documents mixed-interval stabilization; full-text comparison remains incomplete due to access restrictions.

The claim applies only to an exact scalar integrator with one-index lag, deterministic periodic spacing and noiseless fixed-gain held feedback. The unique optimizer is defined in asymptotic Floquet spectral radius, not peak or worst-case finite-time gain. An external independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
