# Scientific review

**Correctness: PASS.** Each prime-local deficit is bounded above by \(\lfloor\log_p k\rfloor\). Above \(\sqrt k\), these deficits are independent Bernoulli variables under uniform sampling over a full period. The smaller primes contribute at most \(O(\sqrt k)\) deterministically, so they cannot alter the leading mean, variance or Gaussian limit. Weighted prime-number-theorem sums reduce the constants to two explicit integrals; Stirling's formula evaluates the variance constant, and Lindeberg–Feller proves the Gaussian limit. Independent finite checks confirm the exact reduction and moment formulas on small windows.

**Originality: PASS, qualified.** The 2026 least-period theorem establishes periods rather than the growing-\(k\) law. The strongest related published result gives exact carry-matrix value frequencies and finite moments for every fixed window. That is a relevant precursor and could provide an alternative starting point, but it does not give the prime-weighted large-window limits, their constants, or this central limit theorem. Indexed and accessible prior-claim searches showed no equivalent asymptotic statement. Unindexed sources or implicit deductions remain residual risks.

**Mathematical value: PASS.** The random quotient is a classical arithmetic object with known periodicity and finite-frequency descriptions. The theorem identifies its asymptotic *scale of fluctuations*, a nontrivial Gaussian law, and two universal constants, including \(2-\log(2\pi)\). It answers a natural statistical question not resolved by merely tabulating values at each window size.

**Closest literature and limits.** Huang–Yang, arXiv:2611.15379v1; Hong–Qian, arXiv:0903.0530; and *Exact value-frequency law for consecutive arithmetic-progression LCM quotients* (2026-10-26). No local limit theorem or quantitative normal approximation is claimed. The use of the exact finite-\(k\) mean is essential.

Self-review: passed. Independent audit: not yet performed.
