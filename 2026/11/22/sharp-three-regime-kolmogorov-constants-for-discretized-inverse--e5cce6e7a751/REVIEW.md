# Scientific review

## Correctness (C): PASS

For all fixed positive shape and scale parameters, the inverse-gamma tail expansion follows from the lower incomplete-gamma integral with a remainder uniformly controlled at large arguments. Expanding the logarithm of the smooth sample-maximum CDF gives the separate \(n^{-1}\) and \(a_n^{-1}\) effects. The proof explicitly controls the two tails, verifies uniform derivative convergence, translates the continuous CDF by the exact integer-floor displacement, and optimizes the limiting envelopes. At shape one, the continuous CDF is exactly max-stable, eliminating both smooth terms. At each lattice point the displacement is precisely one, attaining the constants. The included numerical sanity checker was executed successfully but is not treated as a proof.

## Originality (O): PASS, with historical limitations

The 2017 full-text *Discrete Extremes* paper contains the same floor inverse-gamma model (Section 3.1), making that paper essential prior art; the author's established domain-of-attraction and threshold-exceedance results do not imply the three sharp uniform maxima constants. The 2023 PLOS ONE full text describes the discrete inverse-gamma model, analytical survival, fitting, and simulation; it does not classify the uniform normalized-max error. Shimura's earlier discretization theorem and general extreme-value convergence-rate theory cover broad first-order/rate frameworks. No retrieved exact formula or stronger theorem implies the concrete three constants, and the canonical nonlinear model correction is distinctly affected by floor rounding. The original Shimura full text and parts of early 1982 rate literature were inaccessible; the literature comparison is qualified, not a proof of priority.

## Value (V): PASS

Normalized maxima are central to high-quantile risk prediction under discretized heavy-tailed sampling. The result identifies the correct sample-size rate and a computable sharp constant (not simply a big-O bound), distinguishes sampling error from recording-resolution effects, and reveals the surprising exact cancellation at shape one. These are natural features of the full two-parameter distribution and offer a concrete basis for assessing Fréchet approximations for discretized insurance/severity data.

## Scope and unproved questions

The result is fixed-parameter and distributional only; it does not control parameters approaching shape one with sample size, account for estimation error, or certify historical priority against inaccessible full texts. The numerical sample is finite and not a proof.

Self-review: passed. Independent audit: not yet performed.
