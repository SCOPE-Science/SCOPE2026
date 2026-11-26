# Independent mathematical audit

## correctness

PASS

For each independent draw stream, order the forbidden labels and telescope its conditional avoidance factors. Independence of the k streams yields (1), including the deterministic last label and, separately, the excluded root. Each factor is bounded by its one-label counterpart, giving all-order domination and pairwise nonpositive covariance. At fixed k the power sums are Riemann sums at (n-1)^{k/(k+1)}, the weights vanish pointwise uniformly on compacts, and the joint-to-product ratio tends uniformly to one away from an initial window of arbitrarily small mass. For k/log n tending to positive finite c, power sums in (9) have relative discretization error O(k/b_n), the relevant labels are of order n, and the fixed-order ratio has error O(k/n). Thus the bounded factorial coefficients give the Laplace functional by dominated summation. The left log-tail has expected count asymptotic to e^{-M}, making the minimum a legitimate reversed-Gumbel limit; the location ratio follows from tightness. For the sublogarithmic regime, the mean diverges and variance is at most the mean. In the superlogarithmic proof the displayed bound using 1-epsilon has a harmless denominator slip: since the actual denominator is n-1, use n(1-epsilon/2)^{k_n} for all sufficiently large n, which suffices without any upper bound on k_n. The theorem is unchanged. Replay via RESULT.md (1), (7)–(9) and the corrected cutoff inequality. VERIFICATION.md and verify.py were inspected, not executed; the 497 is the script's bookkeeping total, not 497 literal assertions or evidence for the infinite-size theorem.

## originality

PASS

The one-stream joint law is already explicit for recursive-tree leaves, and the exact k-stream law is its direct kth power, not a separate novelty. The supported distinct claims are the early-label Poisson law at fixed fan-in k≥2 and the log-fan-in Poisson/reversed-Gumbel window and macroscopic crossover. The exact one-stream antecedent also provides product domination, but its k=1 limiting statement does not establish those regimes; the new analysis requires different label scales and uniform control with varying k. The checked circuit literature does not establish such coverage; inaccessible papers remain priority risks rather than evidence of novelty.

## value

PASS

The first circuit output by birth is not a total-output statistic. The theorem identifies a nontrivial fan-in scale where it first occupies a macroscopic portion of the sequence, and describes its extreme fluctuations and neighboring outputs there. The change from a polynomial-origin intensity to an exponential log-window intensity is a structural result worth retaining beyond the mechanically inherited finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
