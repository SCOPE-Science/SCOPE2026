# Scientific review

## Correctness
**PASS.** The resolvent partial fraction and jump equation yield the stated two-sided decaying kernel with the stated normalization. The first difference commutes with convolution; Young's inequality gives the upper variation bound and a single Heaviside jump gives equality. Every smoothing parameter has a negative impulse coefficient because the complex-root phase advances through a negative-sine interval. The small-parameter expansion is an \(\ell^1\) Neumann expansion; the large-parameter limit is an exponentially dominated Riemann sum with a directly integrated sign-alternating continuum Green function. A standalone exact rational finite-section/residual argument certifies the strict nonmonotone comparison.

## Originality
**PASS (with residual historical risk).** The closest source is McElroy's 2006 full-text report, which explicitly supplies the signed exponentially decaying weights, but does not state their absolute-sum sharp variation norm, the step extremizer, the nonmonotone rational comparison or the continuum-limit constant. Its weight formula cannot by itself be reported as novel. The full-text 2009 \(\ell^1\) trend-filtering paper studies a different nonsmooth optimization penalty and finite data. Finite-path Whittaker–Henderson variation results and periodic biharmonic positivity theorems do not cover the bilateral exact gain and its strong-smoothing limit. Relevant keywords and formulas were also compared against indexed mathematical records. The finite-sample HP source was available at abstract level only; an older unindexed exact-norm treatment remains possible.

## Mathematical value
**PASS.** The problem asks a natural stability question about a widely used regularized low-pass estimator: does it reduce total signal variation, and how does the worst-case amplification depend on regularization? The theorem completely determines the gain by a rapidly convergent formula, gives exact extremizing inputs, proves persistent failure of variation contraction, exhibits a rigorously certified *decrease* under stronger smoothing, and evaluates an unexpected nontrivial universal saturation constant. These are relevant when controlling artificial oscillation around discontinuities rather than only mean-square or frequency response.

## Scope and risks
The operator is bilateral and the input is a bounded real sequence with finite adjacent variation. Endpoints, other dimensions and general penalty orders are excluded. The 2006 weight formula is established prior art; the specific norm and phase behavior require additional arguments. No independent mathematical or historical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
