# Independent mathematical audit

## correctness

PASS

The rate-(n−i)α exponential log-gaps give independent Beta((n−i)α,1) ratios. A violation is the event R_(i+1)(1+R_i)>1. The zero event detects every triangular triple, since the two immediate predecessors of any possible largest stick dominate any other pair below it; the count itself is only of consecutive triples. Conditioning yields q_i=a∫x^(a−1)[1−(1+x)^(−b)]dx. Expanding the exponential and x^a with one-sided remainders gives 0≤(π²/12)ab−q_i≤(3ζ(3)/4)a²b+(π²log(2)/24)ab². The adjacent joint probability is at most q_i β_(i+2) log 2. For an independent check of the process approximation: write F for the indicators through i−2 and J for I_(i−1). I_i is independent of F. The conditional deviation from q_i, averaged over J given F, equals 2|E[I_i J|F]−q_i E[J|F]|. Summing the expected deviations while replacing the conditional laws by independent Bernoulli(q_i) laws bounds process TV by 2Σ(P(I_i I_(i−1)=1)+q_i q_(i−1)); Poissonizing the independent coordinates costs O(Σq_i²). Coupling intensities adds at most their summed absolute difference. These give the claimed two error orders and apply even outside the critical regime (where the bound can be vacuous). Riemann sums give the stated density and mean π²λ/36, including the empty limit at λ=0. For supercritical n³α²→∞ with nα→0, the relative variance is O(1/(n³α²)+1/(n²α)); both denominators diverge. Capping α by n^(−4/3) preserves this regime and monotonicity of the uniform-ratio construction extends the conclusion. An independent algebraic recomputation confirmed the constants. CHECK.py was inspected, not executed; its frozen finite diagnostics are not a limit proof.

## originality

PASS

The closest fixed-n endpoint already contains the same leading local coefficient, triangle criterion and adjacent-event mechanism. The defended contribution is the uniform-in-n process approximation with a growing sample, the limiting spatial intensity, and the threshold including the out-of-window avoidance limit; not the local coefficient, finite exact integral, or rare-event approximation theorem by itself.

## value

PASS

This identifies a natural noncommuting-limits problem: the window α on the scale n^(−3/2) determines when a first triangle can occur and whether complete avoidance is likely. The explicit rank intensity says where the consecutive-order violations concentrate, beyond a scalar avoidance probability, and the grid approximation supplies a quantitative finite-size law. It does not count all triangular subsets and its quantitative bound can be uninformative outside the sparse regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
