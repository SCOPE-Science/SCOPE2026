# Scientific review

## Correctness — PASS

The claim specifies independent uniform-endpoint chords, a sampling-label distinguished chord, and both normalizations. The crossing kernel is an exact opposite-side endpoint test; the first Hoeffding variance is \(1/45\). The key mixed projection is proved by an explicit arc-translation integral, giving \(q(t)^2/6\). A degenerate order-two remainder has \(O(n^2)\) variance; the conditional bounded-vector CLT then proves the mixed-normal limit. Exact rational finite checks passed 142 assertions. The finite test does not substitute for the limit proof.

## Originality — PASS (historical-priority qualification)

The previously published marginal crossing CLT (Flajolet–Noy), macroscopic chord-degree law (Acan), and improved marginal CLT rate (Paguyo) do not contain the conditional two-scale joint fluctuation law. Particularly close published findings on marked-degree regression, conditional crossing variance, and global span–crossing covariance were read: none gives the conditional mixed-normal covariance kernel. Generic U-statistic CLTs supply methodology, but obtaining the chord-specific mixed covariance and a joint deletion-noise law requires an extra specialization and calculation. A broader previously published conditioned-U-statistic result or refined enumerator could imply it; independent historical validation remains warranted.

## Value — PASS

Deleting one chord removes its entire crossing degree, a natural edge-count influence diagnostic in a random circle graph. The \(n\)-scale deletion response is geometry-driven, while its \(\sqrt n\)-scale centered error is random; the explicit joint Gaussian mixture tells whether global crossing fluctuations predict that error. The distinction between asymptotic independence at the macroscopic scale and positive covariance at the finer scale is useful in sampling and leave-one-out uncertainty calibration, beyond a rederivation of either marginal CLT.

## Evidence and limitations

Evidence consists of the explicit kernel calculation, Hoeffding decomposition, standard conditional multivariate CLT, exact finite identity, exhaustive small matching enumeration, and inspected primary literature. Scope is independent uniform-endpoint chords; no quantitative convergence rate or uniqueness claim is made.

Self-review: passed. Independent audit: not yet performed.
