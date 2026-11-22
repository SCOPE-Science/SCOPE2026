# Self-review

## Correctness: PASS

The claim is a finite, exhaustively verifiable theorem: the Fourier fourth moment equals the sum of squared integer aperiodic autocorrelations. Up to an irrelevant global sign, all \(2^{18}=262144\) assignments are enumerated, not sampled. Two different algorithms (integer Gray-code update and direct vectorized pair-product summation) verify the exact minimum \(467\), the \(72\) fixed-center minimizers, the next attainable value \(475\), and the full symmetry orbit decomposition \(24+24+24\). Explicit witnesses have squared one-sided sidelobe sum \(53\). Source code and observed outputs are included. The conclusion does not extend to arbitrary array sizes or complex phases.

## Originality: PASS (best knowledge)

The 2019 Balister et al. result is a one-variable asymptotic Littlewood existence theorem; the 2015 Ding–Noshad–Tarokh paper explicitly includes **this same 19-site hexagonal geometry** but constructs multiple jointly complementary arrays after removing the central site. The published 7-site continuous-phase exact fourth moment treats a smaller support. Neither result implies the exact single-array binary 19-site optimum and orbit classification. Search comparisons covered fourth moments, autocorrelation sidelobe energy, hexagonal phase arrays, merit factor and equivalent terms. The 2005 Ramakrishna–Mow work treats peak rather than integrated sidelobe optimization, but its complete tabulations were not accessed; historical priority is provisional. The precise evidence and implication comparisons are provided in `AUDIT.json`.

## Value: PASS

The completed radius-two hexagon is the first natural 19-point step beyond the familiar 7-point seed. The exact spectral-flatness defect \(106\), all equality classes, and the sharp \(8\)-unit next-value separation answer a natural discrete harmonic-analysis and array-autocorrelation design question, not a named single random slice. The result is a finite benchmark, not a general asymptotic theorem or a certified improvement for physical instruments.

## Limitations

The method is exact finite verification, with source and full configuration coverage, not a human closed-form universal inequality. Some historic specialized tables are accessible only as abstracts. No independent mathematical or bibliographic audit has been performed.

Self-review: passed. Independent audit: not yet performed.
