# Independent mathematical audit

## correctness

PASS

For the two-row scalar objective φ(x)=(x²+1)/2, the one-row correction, after the sampled line scale, gives signed unit displacement b. With independent fair with-replacement validation signs B_i and Y=b mean(B_i), a trial of magnitude α gives sampled change α²/2−αY and directional term −αY. Both tests hold exactly when Y≥α/[2(1−c)]>0, including equality at the Armijo threshold. Reuse of the validation batch makes these events nested across the grid: acceptance is precisely the tail at α=2^−J, which is zero if the threshold exceeds one. Every nonzero step increases φ by α²/2. An independent integer Pascal-row calculation at s=64 yielded the exact numerator 8307059966383480541 over 18446744073709551616, with binomial cutoff 33. Di supplies c=10^−4 and J=5; the 64-row choice is an evaluated example, not established as his implementation's batch size. The CLT and Hoeffding bound give the finite and infinite scaling limits, and solving the Gaussian tail gives the budget ratio. The largest eligible dyadic α satisfies q/2<α≤q for q=2(1−c)Y on acceptance (also under saturation, as q<2). Symmetry gives s times the positive-side second moment exactly 1/2, and discarding values between zero and the minimum acceptance threshold loses at most s t_J²→0 in the deep regime. This proves the two normalized damage bounds without asserting an exact constant. Frozen checker.py and VERIFICATION.md were inspected, not executed; the checker covers finite exact-rational scenarios and CLT spot checks, not all s or a multistep convergence claim.

## originality

PASS

The assessed distinct claim is the exact finite-grid false-acceptance and sample-to-depth frontier for a specific independently validated Armijo rule at its true minimizer, plus the damage order. The algorithm, the qualitative possibility of uphill false acceptance, and the binomial and Gaussian tools are prior. The compared stronger-looking oracle-complexity results do not give this validation statistic, finite-grid decision or coupling.

## value

PASS

The minimal least-squares example isolates a flaw that independence alone does not fix in an actual uncorrected validation rule. The exact frontier quantifies how c, the finite grid depth and batch size interact, and separates the probability of a wrong decision from the O(1/s) expected size of its damage. This is a motivated calibration benchmark, not a general stochastic convergence or error-control result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
