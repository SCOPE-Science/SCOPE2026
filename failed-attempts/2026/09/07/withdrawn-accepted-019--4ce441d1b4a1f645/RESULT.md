# Fixed-seed finite-N GOE edge audit at N=10,20,50: calibrated KS proximity to TW1 via Dumitriu–Edelman sampling with replay log

## Context
The Gaussian Orthogonal Ensemble (GOE) largest eigenvalue, after edge scaling, converges to the Tracy–Widom GOE law (TW1) as N→∞. Textbook treatments give the limit; practitioners at small N need a citable, replayable quantification of how far classical scaling is from TW1 and how much a fitted finite-size centering/scaling correction helps, plus a sampler correctness check.

## Definitions
- GOE sampler (Dumitriu–Edelman beta=1 tridiagonal): per sample, `d = sqrt(2)*N(0,1)^N` (diag ~ N(0,2)), `c_k = sqrt(chi^2_{k})` for k=N-1..1 (off-diag ~ chi_k), `A = diag(d)+diag(c,1)+diag(c,-1)`, `lambda_max = max(eigvalsh(A))`.
- Classical edge scaling: `mu_N = 2*sqrt(N)`, `sigma_N = N^{-1/6}`, `s = (lambda_max - mu_N)/sigma_N`.
- TW1 reference CDF `F1(s)`: Hastings–McLeod Painlevé-II `q'' = s*q + 2*q^3`, `q(s)~Ai(s)` as s→∞, `F1(s) = exp(-0.5*∫_s^∞ q - 0.5*∫_s^∞ (x-s)q^2)`.
- KS distance: for sorted scaled `x_(1)≤…≤x_(n)`, `Ft = F1(x)`, `D = max(max|i/n - Ft|, max|(i-1)/n - Ft|)`.
- DKW 95% uniform epsilon: `eps = sqrt(ln(2/0.05)/(2n))`.
- Seeds: master `SeedSequence(500020).spawn(3)[0→N10, 1→N20, 2→N50]`, `numpy.default_rng(child)`; bootstrap seed 500021. Environment: numpy 1.26.4, mpmath 1.2.1, Python 3.12.3, Linux x86_64.

## Result (empirical, not a theorem)
With fixed seeds:

| N | n | mu_cl | sig_cl | KS_cl | mu* | sig* | KS_cal | DKW95 |
|---|---|---|---|---|---|---|---|---|
| 10 | 5000 | 6.32455532 | 0.68129207 | 0.089543 | 6.18455532 | 0.70854375 | 0.007335 | 0.019206 |
| 20 | 20000 | 8.94427191 | 0.60696223 | 0.070261 | 8.82427191 | 0.61303185 | 0.003677 | 0.009603 |
| 50 | 5000 | 14.14213562 | 0.52100073 | 0.046639 | 14.07213562 | 0.52360573 | 0.008268 | 0.019206 |

- Primary stratum N=20, n=20000: calibrated `(mu*_20=8.82427191, sigma*_20=0.61303185)` from two-stage grid minimizing KS achieves `D*=0.00368 < 0.025` vs classical `D=0.07026`.
- Classical gaps exceed DKW epsilon by 2–7×; calibrated gaps lie inside epsilon.
- Offsets mu*−mu_cl = −0.14/−0.12/−0.07 and factors sig*/sig_cl = 1.040/1.010/1.005 shrink with N.
- Classical-scaled moments (bootstrap B=1000 percentile 95% CIs): N10 mean −1.467678 [−1.503249,−1.430912], var 1.680764 [1.613219,1.749834], skew 0.232064 [0.162257,0.303870]; N20 −1.417773 [−1.436138,−1.399719], 1.630087 [1.599681,1.664882], 0.263985 [0.227299,0.296973]; N50 −1.363955 [−1.398242,−1.324492], 1.609008 [1.544351,1.674536], 0.196255 [0.127177,0.268877]; TW1 −1.20653357/1.60778103/0.29346452. Calibrated-scaled means −1.21364/−1.20799/−1.22348 (skew invariant to affine rescaling).
- 50-bin histogram on [−6,4]: e.g. N=20 peak bin [−1.6,−1.4) 1327 observed vs 1270.8 TW1-expected; 2/20000 N=20 samples fall above 4.0 and outside bins.
- 500-sample N=20 prefix exact-diagonalization replay: max abs diff 0.0 < 1e-10, PASS.

No new random-matrix law is claimed. Contribution is the replayable benchmark.

## Proof / Evidence (computed, audited)
- TW1 CDF vendored via RK4 fixed step h=−0.001 from s_max=8 (mpmath Airy init dps=50, q=4.69e-08, q′=−1.34e-07) to s_min=−8 (16000 steps), reverse-cumsum trapezoid integrals, tails beyond ±8 ignored (<1e-12). Convergence h=0.001 vs 0.002 max |ΔF|=1.04e-07 (0.001 vs 0.0005: 6.1e-09). Moments via gradient pdf: −1.20653365/1.60778073/0.293461/0.165220 match literature. Quantiles 10% −2.782, 50% −1.269, 90% 0.450.
- Sampler run exactly as in `run_audit.py`: 30000 draws total; CSVs store idx,lambda_max to 12 decimals; means 5.32464/8.08374/13.43151. Independent audit recomputed KS from stored CSVs + vendored CDF to 6 decimals, verified DKW formula, classical scales, moments, and replay determinism (CSV-roundtrip 5e-13 < 1e-10). Split-half N=20 calibrated KS ~0.010–0.012 vs classical ~0.065 confirms qualitative conclusion despite in-sample optimism.
- Grid: coarse dmu∈[−1,0.6] 33 pts × factor∈[0.85,1.20] 15 pts, refine ±0.06/±0.03 (13×13).

## Limitations
- Calibrated D* is in-sample minimized (optimistic, no split-sample correction); read as lower bound; honest out-of-sample gap marginally larger (~0.01) but still far below classical.
- Only N=10,20,50, one seed family, one documented variance convention (√2 convention yields identical scaled s to 6e-14).
- No analytic rate proof; histogram range truncates far tails; bit-replay version-pinned (allow 1e-10 across BLAS); TW numerical error 1e-07 negligible vs KS 1e-03.

## Reproducibility
`python3 output/artifacts/run_audit.py` (stdlib+numpy+mpmath only) regenerates `tw1_cdf.csv`, `lmax_N*.csv`, `ks_table.csv`, `moments_table.csv`, `histogram_all.csv`, `histogram_N20.svg`, `replay_log.json`, `provenance.json`. Deterministic; second run bit-identical (KS to 6 decimals, replay 0.0). Timed ~1.4 s sampling + ~0.3 s TW + seconds grids/bootstrap on single core (<2 min).

## References
- Dumitriu & Edelman, Matrix models for beta ensembles, J. Math. Phys. 2002 (sampler; arXiv:math-ph/0206043).
- Tracy & Widom, On orthogonal and symplectic matrix ensembles, Commun. Math. Phys. 1996 (TW1 law; DOI 10.1007/BF02099545).
- Johnstone & Ma, Fast approach to the Tracy–Widom law at the edge of GOE and GUE, Ann. Appl. Probab. 2012 (improved centering theory; DOI 10.1214/11-AAP819).
- Bornemann, Asymptotic Expansions of the Limit Laws of Gaussian and Laguerre Ensembles at the Soft Edge, arXiv:2403.07628 (analytic finite-size counterpart).
- Bornemann, On the numerical evaluation of Fredholm determinants (TW numerics concept; reimplemented here with documented RK4, not Bornemann code).
