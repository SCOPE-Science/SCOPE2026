# Independent mathematical audit

## correctness

PASS

The finite reset identity follows by first-hit splitting of the product-chain resolvent, followed by renewal at the independent reset clock. With u=dt and r=cd, the two kernels, after multiplying by d and d^(k+1), tend respectively to exp(-(1+c)u) and u^k exp(-(1+c)u); the same dominating functions using the minimum c in a compact positive interval give uniformity. The scaled objective tends to (1+c)^k/(k!c), whose log derivative has only the zero c=1/(k-1). Rechecking the boundary estimates: on t<=1/minimum scale as used in the proof (t<=1/d for r<=d, t<=1/r for r>=d) the numerator kernel is bounded below by an absolute positive number. For the low-rate denominator, use q(t)<=exp(-t/2) on [0,1], tanh(t)<=t, and q^d<=q(1)^d thereafter. This yields divergence of the normalized mean when r/d tends to zero; the high-rate bound from the kth power t^k gives divergence when r/d tends to infinity. The lower bounds and a fixed positive scaled trial value prove compactness of every sequence of optimizers, not just local stationarity. An independent zero-rate check is to set Δ_j=M_{d,j}(0)-M_{d,j-1}(0). Its backward equation gives jΔ_j-(d-j)Δ_{j+1}=1 and thus Δ_j=sum_{i=j}^d binom(d,i)/(j binom(d,j)); Δ_1 dominates the fixed-k sum. Finite irreducibility gives the zero-rate renewal limit, and the large-r bound implies existence by continuity. Replay: frozen RESULT.md lines 26–94 and verify.py (read, not executed); the script's two numerical finite methods are not a proof of asymptotic optimality. No claim for growing k or non-Poisson policies.

## originality

PASS

Reset renewal and Ehrenfest dynamics are prior, but the checked time/distance normalizations and theorem scopes did not cover the fixed-distance corner mean and all-minimizer limits.

## value

PASS

A natural local-start/rare-target benchmark for resetting: the optimal clock and exact leading mean quantify an exponential-to-polynomial change. Two-sided rate control makes this a global optimization result, not just a tuned heuristic. Both constants depend on the stated coordinate clock and on fixed Hamming distance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
