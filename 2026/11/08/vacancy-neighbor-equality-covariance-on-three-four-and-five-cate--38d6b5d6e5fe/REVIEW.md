# Self-review

## Correctness — PASS
The exact covariance follows from the number of weak compositions with one fixed zero, a prescribed equal pair, and the two possible incidences between a vacancy coordinate and a cyclic edge. The identity in `RESULT.md` is proved for every integer total; the six signs follow from explicit parity-dependent binomial sums. The included `verify.py` passed 3060 exact arithmetic and independent enumeration assertions. Finite tests supplement, but do not replace, the infinite proof.

## Originality — PASS (historical priority qualified)
Bender and Canfield (2005, 2010) treat locally constrained random compositions and asymptotics, whereas these claims concern uniformly sampled fixed-category *weak* compositions and a closed cyclic neighbor count. The nearest located occupancy-frequency and fixed-content run-correlation results do not imply the exact parity phase boundary. A wider historical multivariate generating function may implicitly cover the formulas; no independent historical survey certifies priority.

## Value — PASS
The statistic pair naturally contrasts unobserved categories and neighbors with identical abundance under a symmetric Pólya sampling null. Exact zero covariances alternate with strict opposite signs at three and four categories; at five categories the covariance is positive for all nontrivial totals. This is a complete structural finite-category boundary over arbitrarily large sample sizes. The classification does not claim what happens for six or more categories.

## Limitations and related literature
Theorem 1(c) of Bender and Canfield (2005) describes a different asymptotic model; their 2010 periodic inequalities also do not state the present fixed-category exact calculation. General stars-and-bars methods are classical. Scope excludes higher moments, non-unit Pólya reinforcement, and larger cycles.

Self-review: passed. Independent audit: not yet performed.
