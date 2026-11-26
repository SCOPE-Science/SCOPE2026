# Independent mathematical audit

## correctness

PASS

In binary gap coordinates the recursive tortoise map merges the first two zero gaps and appends a one, with all later zero gaps retained. Thus k passes merge k+1 initial gaps unless the word has fewer ones and is already sorted. In the suffix-1^k output family, splitting h leading zeros across k+1 ordered gaps gives binom(h+k,k) preimages, with 2^(n−k−h−1) such outputs if h<n−k and one if h=n−k. Lower weights 0≤r<k each have one sorted output with binom(n,r) preimages. This yields the count, histogram and maximum by monotonicity and binomial unimodality, including k=n; k=0 is the identity. For a fair source, the (k+1)st one appears at position G_k+k+1, where G_k is a sum of k+1 mean-one variance-two geometric zero counts. On arrival by time n the gap fiber formula applies; otherwise the fiber is binom(n,B_n) for B_n the source weight. In the subcritical regime arrival has probability tending to one and the log gap fiber is 2k+(G_k−k)+O_P(log k+1) by uniform Stirling and the geometric CLT. At k=floor(n/2), (G_k−k)/sqrt(n) tends to Z, the arrival threshold differs from k by at most one, and the nonarrival deficit is O_P(log n+1), so the scaled deficit is the positive part of the negative Gaussian up to o_P(1). In the supercritical regime the binomial branch dominates; Stirling's central quadratic term is −2(B_n−n/2)^2/(n ln 2), which gives the stated constant and limit. For arbitrary critical proportions the LLNs/continuous entropy estimates work on both branches; for k=o(n) the arrival branch is bounded by G_k+k=o_P(n) and nonarrival has vanishing probability. Bounded normalized log sizes give convergence of expectations, and H(Y)=n−E log₂ F since fibers are conditionally uniform. The recorded runs agree with the stated finite ranges and were inspected without replay. No finite check is used for a limit.

## originality

PASS

Pass for the full-cube random-source information-loss and combined three-regime fluctuation theorem. Credit the prior exact deterministic action: the fiber census, extremum and support size are an immediate combinatorial aggregation of Campbell–Rampersad's rule, not independent originality here. The strongest checked restricted-language and single-pass sources do not supply the stopped-source asymptotic or its critical atom under a uniform input at growing iteration depth. The three laws use standard CLTs and Stirling but require tracking the two distinct branches on their different scales.

## value

PASS

The uniform full alphabet cube and linear pass depth are natural baselines for quantifying how much reversible identification is lost under iteration. The result distinguishes exponentially many possible outputs from their actual Shannon concentration, and the critical mixed atom exposes how stopping versus sorting changes the scale of typical uncertainty. It gives explicit fluctuation laws rather than only finite entropy numerics or a restatement of the known deterministic relocation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
