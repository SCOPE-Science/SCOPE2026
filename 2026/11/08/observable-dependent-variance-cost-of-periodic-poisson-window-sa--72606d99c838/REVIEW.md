# Review: Observable-dependent variance cost of periodic Poisson-window sampling

## Correctness — PASS

The Poisson law at a fixed time has mean \(\lambda\) because the periodic intensity integrates to one on every unit interval. Two windows have a shared Poisson count of mean \(\lambda J_v(t)\), so multiplying the exact Poisson–Charlier generating functions gives the orthogonal cross-covariance \(r!\lambda^r J_v(t)^r\) and removes all mixed orders. Square-summable Charlier coefficients justify the infinite sum and covariance integral by monotone convergence. Periodicity gives the Jensen lower bound. A nonzero Fourier mode of the intensity makes the overlap nonconstant at almost every lag, proving the sharp strictness condition. Parseval and the explicit second-factorial-moment expansion give the Fourier penalty with the displayed constant. Unit-time block integrals are stationary, one-dependent and square integrable, proving the CLT by a standard finite-dependence theorem. Reproduction: `python3 verify.py` reports 324 exact or numerical finite diagnostics. These tests are corroborative, not proof of an infinite theorem.

## Originality — PASS, provisional

The 2026 motivating work asks for the role of oscillating baseline arrival intensities but does not derive the optimum for all \(L^2\) Poisson observables. The 2014 trawl work develops covariance structures for stationary count processes but does not state nonstationary rate-profile optimization. Veraart's 2023 periodic trawl process is stationary despite periodic lag dependence and its CLTs concern discrete-time sample means and autocovariances of stationary trawl processes, not the physically averaged count functionals under periodically modulated *arrival rates*. The statement is not a direct corollary of those reported theorems without deriving the specific Charlier-overlap formula and Jensen rigidity. Background Poisson-Charlier orthogonality and one-dependent CLTs are known and not claimed as discoveries. Remaining risk: a more general historical result for cyclostationary Poisson moving averages could subsume the formula; priority has not been independently assessed.

## Mathematical value — PASS

The source literature explicitly raises the variance consequences of a periodic baseline rate. Here a uniform rate is optimal simultaneously for every nonlinear square-integrable count observable, yet is exactly tied with every other profile for affine observables: this sharp observable-dependent boundary is not visible from the ordinary count covariance alone. The exact nonnegative \(H^{-1}\)-weighted Fourier penalty for a natural second-factorial-moment estimator quantifies how modulation frequency affects statistical efficiency. The result is a structural optimization for a natural sampling family, not merely a finite check or renamed standard limit theorem.

## Closest sources and scientific limitations

- C. A. Stewart and M. Sahani (2026), *Sampling on Discrete Spaces with Temporal Point Processes*, https://arxiv.org/html/2603.09089 (motivation and open oscillatory-intensity question).
- O. E. Barndorff-Nielsen et al. (2014), *Integer-valued trawl processes*, DOI:10.1111/sjos.12056 (stationary count covariance framework).
- A. E. D. Veraart (2023), *Periodic trawl processes*, https://arxiv.org/html/2303.04121v2 (stationary periodic-lag trawls and CLTs).

Proof applies only to the stated Poisson-window family, fixed physical-time averaging and \(L^2\) count observables; external novelty remains provisional.

Self-review: passed. Independent audit: not yet performed.
