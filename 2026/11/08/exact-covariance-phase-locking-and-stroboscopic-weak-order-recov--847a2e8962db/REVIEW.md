# Scientific review: Exact covariance phase locking and stroboscopic weak-order recovery

## Correctness — PASS

The exact Cayley rotation, tensor covariance sum, finite geometric series, and eigenvalue split prove the complete finite-N covariance and isotropy classification. A smooth right-endpoint quadrature expansion at modified frequency proves the fixed-terminal-time first-order tensor, the sharp nonzero half-period second-order tensor, and O(h²) mean accuracy. The large-step rank-one limit is independent of finite tests. The included `verify.py` passed 1042 arithmetic and asymptotic checks, as recorded in `verification_output.txt`. Those tests do not replace the universal analytic proof.

## Originality — PASS, with explicit residual risk

Chen, Cohen, D'Ambrosio and Lang (2019 preprint; 2020 journal) originated the integrator, proved exact expected-energy drift and generic weak order one, and displayed second-moment convergence at T=1. Neither result implies the present full covariance spectrum, exact numerical isotropy set, iff physical half-period weak-order transition or large-step anisotropy. Strømmen Melbø and Higham (2004) treat other oscillator discretizations and the energy/oscillation behavior. Senosiain and Tocino (2014/2015), in the inspected public appendix, work out partitioned Euler--Maruyama trigonometric moment formulas. Hong, Scherer and Wang (2006) treat a closely related midpoint method, but their primary full text could not be obtained; its detailed covariance content remains unknown. Those limitations make historical precedence a genuine, documented risk rather than a resolved negative comparison. Scientific claims are not independently audited.

## Value — PASS

The finding establishes a complete numerical phase-locking classification and an exact accuracy boundary at physical half-periods in a canonical noise-driven Hamiltonian test problem. It shows why exact energy drift can conceal a substantial failure to represent statewise Gaussian covariance, especially at extreme stepsizes. The stated tensor coefficients provide reproducible benchmarks for covariance and weak-order diagnostics.

## Claim-to-evidence and limitations

The object is the precise published noise-then-implicit-quadrature update on a scalar undamped harmonic oscillator with additive momentum Brownian noise. The proof is analytic for all positive frequency, noise amplitude and stepsize, and positive integer step counts. It does not establish higher weak order for arbitrary smooth observables or nonlinear Hamiltonians. The checker supplies only finite exact identities and asymptotic examples. Related older midpoint full text, subscription-only review body and independent scientific validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
