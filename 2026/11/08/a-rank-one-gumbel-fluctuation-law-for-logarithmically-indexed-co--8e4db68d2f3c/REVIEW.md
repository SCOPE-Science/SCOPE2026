# Scientific review: logarithmic-index sibling fluctuations

## Correctness — PASS

The precise, compact-uniform mean-square approximation is supported by an analytic proof: independent rate-one Poisson processes recover the discrete stopped coupon counts; the Dvoretzky–Kiefer–Wolfowitz inequality controls uniformly the empirical Gamma survival functions over \(O(\sqrt{\log N})\) indices and all times; an exact Poisson-CDF derivative plus uniform local Poisson approximation gives the random time shift; the exponential-spacing representation supplies uniform fourth moments; and a stopped Poisson martingale transfers continuous completion time to discrete draw count in \(L^2\). Standard arguments then yield the Gumbel functional limit and limiting means and covariances. Exact-finite/numerical cross-checks passed 87 assertions but do not replace the infinite proof. Limits: the result is not extended to nonuniform weights or expanding index windows.

## Originality — PASS, with historical limitations

In arXiv:2606.29635, the source model and notation match, but Theorem 5 restricts the joint theorem to \(j\le J\) for fixed \(J\), and Remark 3 explicitly excludes growing indices. Ilienko (2026, DOI:10.15559/26-VMSTA306) proves an infinite-dimensional fixed-coordinate theorem in the **product topology**, which, unlike a uniform theorem on a moving index window, does not control ranks increasing as \(\log N\). The companion arXiv:2606.31391 proves finite-size transform extremality for any fixed parameters, not a growing-index functional Gumbel law. The older arXiv:1412.4346 studies fixed-index expectations, and arXiv:2005.05270 treats the first sibling. Searches comparing the exact first-cover stopping time, logarithmic sibling index, empirical Poisson centering, rank-one Gumbel process, and covariance did not reveal a directly covering statement. This is **best-knowledge** originality, not a claim of exhaustive priority; a sufficiently broad other occupancy empirical-process theorem could cover the result by specialization and remains a residual risk.

## Mathematical value — PASS

The motivating paper explicitly identifies the growing-album-index question as outside the known fixed-index theorem. Near \(j\simeq\log N\), the missing-album fraction changes from microscopic fixed-index size to macroscopic Gaussian-CDF shape. The theorem identifies its fluctuation scale, non-Gaussian limiting driver, compact-uniform dependence, and exact leading covariance profile. In particular, it identifies a natural phase of the sibling problem which fixed-index asymptotics cannot extrapolate to, and provides a starting point for second-order and nonuniform generalizations. It is more than a standalone Poisson-tail estimate because it controls the *stopped, jointly indexed random occupancy profile*.

## Closest literature and residual risks

- Long (2026), arXiv:2606.29635, Theorem 5, Remark 3: same object, fixed-index regime only.
- Ilienko (2026), DOI:10.15559/26-VMSTA306: an important same-model infinite-dimensional limit theorem in the product topology, meaning convergence of fixed coordinate blocks, not the growing index window.
- Long (2026), arXiv:2606.31391: fixed-size generating-function and extremality comparisons rather than joint growing-index asymptotics.
- Mahmoud–Smythe (2012), DOI:10.1239/aap/1339878719: fully inspected earlier general occupancy paper; Theorems 1–2 concern fixed frequency categories at deterministic growing sampling times, not a moving log-frequency threshold at first collection completion.
- Doumas–Papanicolaou (2014/2018), arXiv:1412.4346: classic sibling expectation estimates, not this functional fluctuation.
- Papanicolaou–Doumas (2020), arXiv:2005.05270: first-sibling distribution limit, not growing sibling index.
- Classical stopped occupancy and empirical-process literature: broad theoretical ingredients could offer an equivalent or dominating general statement not yet located. This uncertainty must be distinguished from a proven priority claim.

Self-review: passed. Independent audit: not yet performed.
