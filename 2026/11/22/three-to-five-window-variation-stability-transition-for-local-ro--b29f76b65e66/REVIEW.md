# Scientific review — local ROF window-size variation transition

## Correctness — PASS

The three-window argument is a complete analytical norm bound: every generic center-row Jacobian is the average over a contiguous fused block, the four possible probability rows each send a unit step to a spatially nondecreasing response, and the step decomposition of arbitrary input differences yields variation nonexpansivity. Integrating affine-region derivatives extends the bound to all pairs, including degeneracies. A strictly monotone large-gap construction attains the coefficient one. The five-window counterexample is proved by exact primal-dual KKT calculations for twelve prox problems at a specified rational pair, not a floating-point search. The gain is exactly \(7/3\); scaling and extension supply all claimed positive penalties and lengths.

## Originality — PASS, with historical limitations

Louchet–Moisan's local ROF analysis gives pointwise order/range and asymptotic statements; these do not imply the new two-input variation threshold. Tibshirani–Taylor's generalized-lasso results supply fused-block methods. Little–Jones prove one-input three-point median variation diminution. The published graph-TV perturbation-modulus theorem is about **one global proximal map**, not an assembly of different local proximal center rows; the published sliding-median theorem is for an order-statistic selector on a cycle. The closest statements, rather than merely title matches, were compared in the source inspections and exact checks in `AUDIT.json`. A historical equivalent in less searchable nonlinear filter literature remains possible and requires independent review.

## Value — PASS

The result provides a natural operator-stability boundary: a three-sample local TV smoother cannot amplify the adjacent variation of differences, whereas the next odd window already amplifies it by more than a factor two. It separates local range/Euclidean stability of denoising from nonlinear perturbation stability in BV, a mathematically and practically motivated issue for choosing spatial denoising windows.

## Limitations

There is no claimed exact sharp five-window constant, and no classification of five-window lengths five through nine, longer windows, unequal weights, or padded/cyclic boundary conventions. The verified five-window gain is a lower bound, not a universal maximum. Historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
