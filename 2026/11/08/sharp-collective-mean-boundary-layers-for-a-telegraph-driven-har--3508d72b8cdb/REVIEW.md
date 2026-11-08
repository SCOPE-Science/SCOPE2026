# Scientific review

## Correctness — PASS

The stationary equations in arXiv:2404.02480v1 give an exact conditional-Gaussian position decomposition. Independence of the thermal OU terms yields the exact mean representation, and the source's telegraph-filter beta law yields the displayed endpoint density. The proof then checks both nonuniform limits: \(w=\sqrt Ny\) for the boundary layer, and \(t=N\delta_N y/\sigma^2\) with normal Mills bounds for exterior or moderate offsets. The conditional hidden-center law follows from normalizing the same integrable measure. This covers every fixed positive \(\nu\), including integrably divergent beta endpoint densities, and both sign-reflected edges. The standalone numerical checker passed 46 diagnostic assertions, including direct finite-\(N\) quadrature; the limit is proved analytically rather than inferred from numerics.

## Originality — PASS, qualified

The closest exact sources are arXiv:2404.02480v1 (the particular driven gas and the full stationary Gaussian-beta mixture), arXiv:2307.15351v1 (general conditional-i.i.d. sum formulas, especially Eqs. (127)–(133)), and arXiv:2312.02570v1 (a physically distinct switching-stiffness gas). The first two already yield the finite-\(N\) integral and weak macroscopic limit and thus substantially limit the new scope. Primary-text and research-record comparisons did not identify the asserted sharp edge, endpoint selection, and exterior prefactor in this model. The mathematical tools are standard endpoint asymptotics, and an unindexed general Gaussian-smoothing theorem may subsume the resulting estimates. Originality is claimed only for the present explicit sharp classification, not the known starting distribution.

## Mathematical value — PASS

The limiting ensemble mean cannot leave \([-B,B]\), but its finite-\(N\) Gaussian component can. The theorem locates the exact width separating polynomial and exponentially rare escape, calculates the prefactors, and identifies the hidden-state selection responsible for an escape. The power \(\gamma/(2\mu)\) is a direct dynamic signature in a measurable collective quantity despite the unbounded marginal position densities. This answers a physically natural rare-collective-fluctuation question not resolved by the leading conditional-i.i.d. limit, without asserting a general downstream theorem.

## Closest literature and residual risks

The full finite-\(N\) Gaussian-beta mixture is available by specializing the older equations, so a characterization of this result as a straightforward but unstated asymptotic consequence is a plausible priority and value risk. Searches cannot exclude equivalent unindexed presentations. The theory does not address thermal-noise/particle-number joint limits or finite-sample statistical stability.

Self-review: passed. Independent audit: not yet performed.
