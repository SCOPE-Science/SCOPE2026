# Independent mathematical audit

## correctness

PASS

The exact inverse DFT of each full unnormalized intensity is the weighted cyclic autocorrelation. In odd n, the two nonzero cross-lags +/-h differ; the positive geometric-mask autocorrelation ratio determines ordinary integer sum u+v, and sum plus difference modulo odd n uniquely determines unordered support by invertibility of 2. Two zero-lag equations then solve the squared magnitudes and one cross-lag solves relative phase; zero and one-sparse cases are separate. An arbitrary single mask cannot distinguish two scaled impulses, while even n real masks have explicit conjugate antipodal two-site ambiguity. Inspected CHECK.py demonstrates 905 finite support signatures and recovery/counterexample sampling; unrestricted correctness rests on the analytic proof.

## originality

PASS

Unlike full-signal random-mask PhaseLift, Sidon-support phase-only masks, unmasked sparse Fourier recovery or complete translated-window Gabor measurements, the claim gives exactly two deterministic strictly positive bounded-contrast unoversampled masks for ALL odd-cycle complex two-sparse vectors, with a sharp one-mask lower bound. Li–Li 2021 is highly relevant but its full text was unavailable despite OA/preprint and authorized Oxford attempts; its accessible abstract gives a randomized-mask setting rather than this exact deterministic sparse theorem. Best-of-knowledge PASS with explicit high-priority residual risk and no invented full-text exclusion.

## value

PASS

Exact universal support/amplitude/relative-phase recovery of a nontrivial sparse complex class with two elementary positive masks and explicit decoder identifies a minimal measurement-design threshold; parity obstruction gives a genuine acquisition boundary. This is meaningful beyond a generic phase-retrieval algorithm or finite experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
