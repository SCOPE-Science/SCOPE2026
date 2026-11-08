# Scientific review of the Gaussian–first-Hermite exposure-allocation theorem

## Correctness

PASS. The centered Gaussian and first-Hermite ambiguity integrals give the exact squared multiplier \(e^{-s}(1+a(s^2-2s))\). Its derivative has at most two critical points on the nonnegative axis, and the radius-two boundary separates the regimes. For \(T>2\), an increasing outer-boundary branch and a strictly decreasing interior-minimum branch cross exactly once, giving both uniqueness and the explicit root equation. Taylor expansion at the endpoint \(a=1\) proves the stated large-radius asymptotics. A direct-integral and global-parameter grid checker provides supporting numerical evidence. The proof, not the numerical grid, establishes the continuum result.

## Originality

PASS under currently inspected evidence, with historical-priority qualifications. Alaifari–Yang's Hermite multi-window construction supplies the ambiguity/Laguerre formula, disjoint annular coverage algorithm and noise bounds but not a disk-wide optimal fixed exposure split for a jointly prewhitened \(L^2\) multiplier. Grohs–Liehr–Rathmair's Gaussian/first-Hermite constructions concern uniqueness from lattice samples, not this sharp multiplier lower norm. The older Cakrak–Loughlin optimized weights minimize discrepancy with a target Wigner spectrum, a different objective; its accessible extracted text was inspected, but the complete source could not be visually assessed. These comparisons do not constitute an exhaustive historical priority search. An equivalent result hidden in signal-design literature remains possible.

## Mathematical value

PASS. A choice of how to divide a fixed measurement budget between two prescribed Hermite windows is a natural design question in ambiguity-based inversion. The theorem identifies precisely when the first-Hermite channel becomes beneficial, classifies every optimizer including a threshold interval, supplies a one-dimensional reproducible rule for every larger aperture, and quantifies a polynomial large-aperture stability gain. This is a sharp finite-window model fact, not a claim of a full phase-retrieval algorithm or broad optimality among all windows.

## Scientific limitations

Only constant exposure fractions, these two unit-norm windows, ideal disk restriction and prewhitened L2 errors are treated. The construction does not optimize nonlinear recovery, arbitrary windows, sampled data or correlated spectrogram noise. Direct external independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
