# Scientific review: three-time self-return onset

## Correctness — PASS

The reduction from original times \(t,2t,3t\) to multipliers \(1,a+1,a^2+a+1\) preserves Haar measure because multiplication by the integer \(a-1\) maps Haar measure to Haar measure. The signed-coordinate interval argument leaves only the common central interval for \(r\le\rho_a\), and shows the first additional pair of intervals for \(\rho_a<r\le\rho_a+\eta_a\). The relevant integer-center inequalities are explicitly checked in the proof, including the critical \(a=2\) boundary. The exact-rational checker enumerates all possible endpoint crossings for \(1,3,7\), making its eleven finite breakpoint checks a proof of the complete six-branch base-two identity; 174 additional exact checks sample but do not prove the uniform-in-parameter assertion. Boundary sets have measure zero. No Monte Carlo observations or unproved asymptotic extrapolations are used as the theorem's basis.

## Originality — PASS within inspected evidence

Kirsebom–Kunde–Persson (arXiv:2003.01361, Sections 6 and 8) introduce the relevant self-return events, compute their pairwise Fourier correlations, and investigate eventually-always hitting. Their pairwise expressions do not supply the three-frequency geometry, first new triple-overlap threshold, slope jump, or the complete \(1,3,7\) probability diagram. He–Liao (arXiv:2302.05149) treats quantitative recurrence and overlap bounds for more general maps, rather than these exact finite triple-event identities. The closest examined prior record, the circle-endomorphism conditional later-phase law indexed `6cc0a523-4f88-433c-babc-0850400828d0`, gives full two-time conditional phase distributions, not the dependence on three simultaneous return times. The published expanding-map pair-correlation variance record `2026/10/11/SCOPE-sharp-second-moment-inflation-for-expanding-circle-map-pair-corr--d5c688b954c6` treats a different orbit-pair statistic and no triple self-return onset. Exact endpoint enumeration is a standard method and not claimed as a methodological discovery. Search results cannot establish absolute uniqueness; unindexed equivalent triple laws remain a residual risk.

## Mathematical value — PASS

Third-order recurrence is the first joint statistic not fixed by single-event frequencies and pairwise correlations; for the count of the three indicated return events, its third factorial moment is exactly six times the computed triple overlap. The sharp arithmetic threshold identifies where the joint event stops being supported solely by neighborhoods of common resonant phases. Distinguishing its onset from the already-present pairwise onset requires genuine three-frequency compatibility, not renaming a pair result. The full six-phase first-three-return law gives a benchmark for higher-order self-return clustering and finite-time recurrence-count moment calculations, which are natural in shrinking-target dynamics. The general result concerns every integer expansion factor and every equally spaced triple, not a handpicked isolated parameter. This is an exact but limited finite-time classification; no new global limit theorem is asserted.

## Closest sources and limitations

- Kirsebom, Kunde, Persson, *On shrinking targets and self-returning points*, arXiv:2003.01361, Sections 6 and 8: same self-return events and pairwise analysis, not the stated triple threshold.
- He, Liao, *Quantitative recurrence properties for piecewise expanding maps on [0,1]^d*, arXiv:2302.05149, Introduction and recurrence-correlation estimates: broader map class, but different conclusions.
- Existing two-time conditional circle-phase law `6cc0a523-4f88-433c-babc-0850400828d0`: exact two-event law, without an implication to three-event conditional intersections.

The claim is for Haar initial data, the circle distance, shared radii, and times equally spaced. A complete large-radius phase diagram is derived only for the first three doubling-map times. Publication priority cannot be established against all inaccessible or unindexed mathematical work. The review is not independent.

Self-review: passed. Independent audit: not yet performed.
