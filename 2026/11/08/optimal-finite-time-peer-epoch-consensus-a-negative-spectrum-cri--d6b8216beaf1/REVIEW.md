# Review: finite-time peer-epoch controllability

## Correctness — PASS

Reversibility provides a real common spectral basis. Each finite-horizon peer update is a stochastic polynomial of the same transition matrix, and its exact scalar multiplier is derived in `RESULT.md`. The denominator is positive, nonnegative eigenvalues never vanish, even inner horizons never vanish, and odd horizons have at most one negative real root. This proves both impossibility and the optimal number of outer epochs, including for state-dependent schedules on generic inputs. Cauchy interlacing rigorously handles missing edges. The provided standalone script passed 360 spectral comparisons on 15 small connected regular graph types and an exact rational weighted example. Finite checks are corroboration, not an infinite proof.

## Originality — PASS, qualified

The 2026 predictive-loop study already derives the peer-filter multiplier; Kibangou's 2012 Laplacian result already contains the one-inner-step spectral annihilation construction. Neither of those is presented here as new. The inspected texts did not state the additional optimality assertion *across arbitrary longer finite peer horizons*, under adaptive repeated homogeneous anchor resets, or the reversible support-graph obstruction in that setting. Broader finite-time consensus theorems allow controls outside this restrictive family. Residual uncertainty: a full text of the 2019 directed spectral-factor paper was unavailable and an equivalent older nonnegative-filter theorem might be unindexed. See `AUDIT.json` for actual comparisons and inspection limits.

## Value — PASS

The sharp minimum number of outer episodes quantifies an intervention cost and rules out the intuitive but false hope that arbitrarily long inner peer averaging can produce exact consensus faster. It separates complete-support finite-time reachability from ordinary asymptotic consensus on sparse networks, and gives exact tuning choices when reachability holds. This is a specific, structural limitation of a recently studied predictive-loop opinion mechanism, not a general finite-time consensus claim.

Self-review: passed. Independent audit: not yet performed.
