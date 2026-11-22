# Scientific review: exact Markov-generator RK2 positivity

## Correctness — PASS

The claim is for every finite row-generator \(Q\), with all offdiagonal rates \(a_{ij}\ge0\). The exact identity \((Q^2)_{ij}=-\Delta_{ij}\) gives one linear-in-\(h\) sign factor after removing \(h\), while each diagonal stays at least \(1/2\); hence every offending edge can cross zero only once. A maximal-exit-rate diagonal exceeds one after \(2/M\), proving a finite offending edge exists. The formula and the if-and-only-if SSP equality criterion follow from these explicit exact inequalities; no limiting or spectral assumptions intervene. The packaged `verify.py` passed 39,240 supplemental exact-rational assertion groups, including heterogeneous directed examples, zero rates, endpoint equality, negative entries past the endpoint, and stars through 50 leaves. It does not establish the infinite result by enumeration.

## Originality — PASS on available comparisons, with priority risk

The 2014 full-text SSP treatment establishes the sufficient bound at one forward-Euler step, not a generator-dependent exact positivity interval. The 2013 absolute-monotonicity treatment optimizes stability functions, not directed graph-local sharp thresholds. Two close public technical results were read in full. The regular-graph two-stage Euler-superstep theorem allows real nonnegative substeps; its quadratic coefficient is at most one quarter the squared total time, whereas the present RK2 coefficient is one half. Its regular graph formula provides related algebra but not the directed nonregular all-generator theorem. The other result gives only a sufficient walk-gap criterion for sharpness on constant-rate graphs; it does not give the necessary and sufficient maximal-exit/two-hop criterion. The accessible historical claims were checked for the same RK2 formula and motif, with no match found. A plausible 2005 positivity-threshold paper was accessible only in abstract, so equivalent generator-wise results there remain a priority risk. Failure to locate a paper is not evidence of absolute priority.

## Value — PASS

The class is the complete finite-dimensional family of conservative positive linear ODE systems, rather than a chosen small graph slice. The theorem gives an exact computable positivity step limit using only one-hop rates and two-hop bypasses. It identifies a necessary and sufficient support/rate motif for when the generic SSP limit is the true bound, shows that all other generators admit a strict improvement, and quantifies a sharp possible near-doubling on a natural growing family of stars. The local criterion supplies a concrete positivity-preserving implementation rule and a structural explanation for the improvement, beyond a stand-alone matrix multiplication check.

## Limits

This is a completed-step rather than stagewise positivity theorem. It makes no claim for nonlinear problems or for higher-order Runge–Kutta and does not certify small truncation error at the maximal safe step. Older general positivity literature may contain equivalent specialized results. The independent scientific review channel has not been conducted.

Self-review: passed. Independent audit: not yet performed.
