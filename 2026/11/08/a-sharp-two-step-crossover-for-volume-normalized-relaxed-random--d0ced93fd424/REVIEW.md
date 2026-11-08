# Review of the two-step randomized projection crossover

## Correctness — PASS

The row norms are exactly \(1\) and \(\sqrt{1-\tau^2}\), so the 2026 volume-normalized rule gives fixed relaxations \(1\) and \(1+\tau\). For independent uniform row selections, enumerate the four two-step matrix products and form the exact quadratic-form difference \(D\). In the orthonormal second-row basis, direct multiplication yields \(\operatorname{tr}D=\tau^2(\tau^2+2s^2)/4>0\) and \(\det D=\rho^2s^2\tau^2[\tau^4+\tau(\tau+2)s^2-1]/16\). The spectral sign test for a real symmetric two-by-two matrix proves both directions of the claimed if-and-only-if, including equality and every initial error. The sign of the one-step difference follows from orthogonality of \(I-Q\) and \(Q\). All 50,904 independent exact-rational checks, including enumerated words, passed. The proof covers an infinite open parameter domain; the finite checker is supplemental.

## Originality — PASS, qualified

Entezari, Banerjee and Kalantari (arXiv:2610.12346v1, 8 October 2026) specify the row-volume-based relaxation and its one-step expected progress; their §3.3, proofs, experiments and discussion do not give the exact **two-step, all-initial-error** comparison to unit-relaxation uniform sampling. Marshall and Mickelin (arXiv:2202.12224) analyze scheduled learning rates in a noisy regime; Dong et al. (arXiv:2512.09825) analyze a distinct averaged Bregman-block update; Bai and Wu (doi:10.1016/j.laa.2018.05.009) treat unrelaxed randomized Kaczmarz. A relevant publicly indexed result on **cyclic**, asymptotically optimized two-row Kaczmarz has a different update law and finite-horizon objective, so it does not imply the independent uniformly sampled result here. Other indexed results address reverse-order cyclic underrelaxation, not this precise policy. Searches for equivalent two-step moment and noncommuting-projection formulations did not locate direct coverage. The publisher full text of Bai–Wu and the full publicly indexed cyclic result could not be inspected; historical originality against an unindexed equivalent calculation remains a concrete residual risk. The originality assessment is a reasoned comparison, not a uniqueness guarantee.

## Value — PASS

The result answers a mathematically motivated question for a newly introduced computationally cheap rule: can a relaxation that can never improve **any conditional one-step expected squared error** nevertheless produce a strictly smaller expected error after two randomly composed steps? The answer has a complete sharp angular and norm-ratio phase boundary, a matching all-initial-error impossibility region, and a simple exact rational instance. The noncommutative memory of random projection compositions is essential; a one-step spectral bound does not decide this. The result is deliberately narrow but gives a concrete diagnostic for interpreting finite-horizon performance of the proposed norm-dependent policy. It is not a theorem of worst-case or per-gradient-evaluation superiority.

## Limitations and closest literature

The system is two-dimensional, homogeneous and consistent; two rows are sampled iid with equal probabilities, the global maximum row norm is known, and only the second iterate is compared. Neither a larger-system improvement nor any longer-time advantage follows. Related prior methods and sources are identified in RESULT.md and AUDIT.json. Independent mathematical audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.
