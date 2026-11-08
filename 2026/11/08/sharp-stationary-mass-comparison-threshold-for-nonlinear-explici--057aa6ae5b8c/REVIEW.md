# Self-review

## Correctness
PASS. The exact EIN representation follows by multiplying by the Markov resolvent. The weighted generator dissipation identity uses both row-sum conservation and stationarity and does not assume reversibility. The energy Taylor estimate proves the bound \(\alpha\ge A/2\), and a centered linear-flux witness establishes necessity. The nonreversible return lemma follows from a resolvent quadratic form with nonpositive weighted generator pairing; ergodicity makes its stationary lower bound sharp as the step grows. The nonlinear Jacobian is entrywise nonnegative precisely under the universal sufficient comparison threshold, and the same linear flux produces a negative component below it. The standalone checker supplied 976 supplementary assertions. The proof does not substitute finite sampling for universal quantifiers.

## Originality
PASS, with residual literature risk. The motivating EIN papers already supply the half-diffusivity energy principle, which is expressly excluded from the new contribution. The closest published Markov-chain result gives the Cayley/Crank–Nicolson diagonal-resolvent test, including the \(\alpha=A/2\) linear subcase, but not the adjustable nonlinear EIN all-flux comparison frontier controlled by \(\pi_{\min}\). Literature on bound-preserving sweeping and Fokker–Planck penalization changes the algorithm. Searches across the named aliases, available prior claims, and published mathematical records did not locate a statement implying the full threshold. Some plausible source appendices and older literature were not available in full; a previously known equivalent formulation cannot be excluded categorically.

## Value
PASS. The result resolves a natural tension between energy decay and invariant-domain preservation for the standard split used on finite-volume and graph diffusion discretizations. It provides the exact scale-free stabilization parameter for all directed, irreducible conservative generators and monotone fluxes with bounded slope. The three-cycle example proves that the energy-safe parameter can still create negative states, and the sharp frontier gives a replacement without an extra projection step. The result is intentionally limited to the first-order fixed-generator setting.

## Closest literature and limitations
Wu–Shu (2026) and Wang–Zhang–Wang–Shu (2019) develop EIN energy analysis; the published Crank–Nicolson resolvent-return law addresses a different fixed rational map with an acknowledged overlapping linear subcase. Papers on extra correction/sweeping procedures do not imply the stated unmodified-map threshold. The theorem does not apply automatically to variable-mobility spatial discretizations, higher-order methods, or non-Metzler generators; independent corroboration is still absent.

Self-review: passed. Independent audit: not yet performed.
