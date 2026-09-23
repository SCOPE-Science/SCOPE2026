# Murnaghan stabilization census for padded triples from cores of weight <= 4 at n = 6..10, with maximal-delay witness (3,1)^3

## Context

For partitions lambda, mu, nu of n, let g(lambda,mu,nu) be the symmetric-group Kronecker coefficient. Murnaghan's theorem states that if alpha, beta, gamma are fixed partitions (reduced cores) and lambda[n]=(n-|alpha|,alpha) (and analogously mu[n], nu[n]) are the padded partitions, then the sequence g_n=g(lambda[n],mu[n],nu[n]) is eventually constant (and nondecreasing). Its limit is the reduced (Murnaghan) coefficient bar-g(alpha,beta,gamma). Exact stabilization points govern the reduced-vs-ordinary dictionary used in geometric complexity theory and in work of Briand-Orellana-Rosas, Sam-Snowden, Vallejo, and Ikenmeyer-Panova.

## Definitions

- Reduced core: a partition alpha with |alpha| <= 4. There are 12: (), (1), (2), (1,1), (3), (2,1), (1,1,1), (4), (3,1), (2,2), (2,1,1), (1,1,1,1).
- Padding: lambda[n]=(n-|alpha|,alpha), valid when n-|alpha| >= alpha_1 (with the convention that the empty core always pads to (n)).
- Trajectory: for a reduced triple (alpha,beta,gamma), the values g_n at each n in 6..10 where all three paddings are valid.
- stab: first n0 such that the trajectory is constant on [n0, max valid n in window]. gbar: last observed value.
- Statuses: `stabilized-in-window` (suffix constant through the last valid n, and constant at n=9..10 when n=10 is valid); `increasing-at-10` (n=10 valid and g9 < g10, so no exact threshold is claimed, only stab > 10 and bar-g >= g10).

## Result

Complete recomputed census over all 12^3 = 1728 ordered reduced triples, observed at S_n for n = 6..10 by exact character inner products:

- 1000 triples valid at every n = 6..10; all 1728 have >= 1 valid n.
- 1669 stabilized-in-window; 59 certified increasing-at-10 (each with g9 < g10).
- All 1728 trajectories monotone nondecreasing; zero strict decreases anywhere.
- Threshold histogram (stabilized): stab=6: 689, stab=7: 353, stab=8: 465, stab=9: 162.
- Relative-delay histogram (stab minus first-valid-n, all 1728): 0: 1115, 1: 371, 2: 217, 3: 25.
- Stable-value histogram (stabilized): 0: 663, 1: 479, 2: 224, 3: 126, 4: 57, 5: 42, 6: 18, 7: 16, 8: 12, 9: 7, 11: 6, 12: 6, 13: 9, 18: 4.
- Weight-<=3 sub-cube (7^3 = 343 triples): all stabilized in-window.

Maximal-delay witness: alpha = beta = gamma = (3,1), paddings (3,3,1), (4,3,1), (5,3,1), (6,3,1), trajectory g7 = 1 < g8 = 8 < g9 = 15 < g10 = 19. Hence stab > 10 and reduced value bar-g((3,1)^3) >= 19. The in-window range 18 is tied-maximal over all triples (tied only with stabilized (2,1,1)^3 trajectory 0,8,17,18,18), and 19 is the largest g10 among the 59 delayed triples (next-largest 17). The triple is diagonal hence S_3-symmetric; the neighboring orbit ((3,1),(3,1),(2,1,1)) and permutations give 3,11,16,17. 24 triples have 3 strict increases, of which 10 are still unstable at 10.

## Proof / evidence

- S_n character tables for n = 6..10 (11, 15, 22, 30, 42 classes) built from scratch by two Murnaghan-Nakayama beta-set implementations with entrywise agreement; verified by full row and column orthogonality, dimension positivity, and sum-dim^2 = n!.
- Every Kronecker number by the exact class-algebra inner product g = sum_C chi_lambda(C) chi_mu(C) chi_nu(C)/z_C in exact rational arithmetic with integrality and nonnegativity asserted.
- Global cross-checks: dimension identity sum_nu g(lambda,mu,nu) dim nu = dim lambda dim mu for all 3494 ordered pairs; sum-of-squares spot checks 3603 for (6,3,1)^2 and 96237 for (4,3,2,1)^2 at n=10; dimension check 99225 = 315^2.
- Each of the four witness inner products is committed as per-class exact summands (chi, z, chi^3/z) summing exactly to 1, 8, 15, 19.
- The auditor independently re-verified row orthogonality, hook-length dimensions, all 1728 CSV rows from the committed tables (zero mismatches), all witness class sums, and the witness values via an independent rim-hook-path Murnaghan-Nakayama implementation.

## Limitations

- For the 59 increasing-at-10 triples, no exact stab and no exact reduced value is claimed; only g9 < g10, stab > 10, bar-g >= g10.
- stab/gbar for stabilized triples mean constancy through n = 10 combined with Murnaghan's eventual-constancy theorem, not an independent proof of stabilization theory.
- Scope is exactly cores of weight <= 4 at n = 6..10; extrapolation beyond n = 10 or to heavier cores is not claimed.

## Reproducibility

Stdlib Python only. `output/artifacts/verify_tables.py` rebuilds all five tables and checks dual-implementation agreement plus orthogonality. `output/artifacts/verify_census.py` (run beside committed `chartables.json`) re-derives all 1728 trajectories and the witness. `output/artifacts/threshold_table.csv` (parse with csv.DictReader; core tuples contain commas), `summary_stats.json`, `chartables.json`, `witness_class_sums.json` are committed.

## References

- E. Briand, R. Orellana, M. Rosas, The stability of the Kronecker products of Schur functions, arXiv:0907.4652.
- S. V. Sam, A. Snowden, Proof of Stembridge's conjecture on stability of Kronecker coefficients, arXiv:1501.00333.
- C. Ikenmeyer, G. Panova, All Kronecker coefficients are reduced Kronecker coefficients, arXiv:2305.03003.
