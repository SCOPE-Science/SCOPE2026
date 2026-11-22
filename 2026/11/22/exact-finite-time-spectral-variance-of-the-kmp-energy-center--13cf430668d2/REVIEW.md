# Review of exact finite-time KMP center variance

## Correctness — PASS

The normalized center is a martingale. Its conditional quadratic variation is determined by local KMP exchanges, and the translation-summed second moments solve an explicit bounded half-line difference system. Resolvent inversion produces a strictly positive density, without additional poles. The spectral endpoints give both time expansions, including the finite additive offset. The standalone checker reproduces five Laplace resolvents, two spectral sum rules and three independent event-driven simulations. Its finite tests are only corroboration, not a proof of infinite time or lattice size.

## Originality — PASS, qualified

Schorlepp–Meerson–Sasorov, arXiv:2611.15739 (2026), §IV and §IX, derive leading long-time spatial-moment variances in macroscopic fluctuation theory. The leading coefficient here is the same known coefficient after adjusting microscopic bond rate. The new claim is the exact microscopic finite-time spectral measure, strict full-time concavity, and constant \(1/4\) correction. Earlier Bettelheim–Smith–Meerson heat-transfer and Bettelheim–Meerson interval-energy results concern different observables. Indexed comparisons and accessible earlier research claims identified no equivalent statement, but an unindexed two-particle resolvent may implicitly cover this finding; that is a publication-priority risk. The closest 2026 source was inspected in detail in full HTML and PDF; older source comparisons were limited to their abstracts and known scopes.

## Value — PASS

An explicit positive spectral density gives a finite-time microscopic benchmark where the motivating long-time MFT theory provides only the leading variance. Strict concavity shows how the instantaneous spreading of center uncertainty slows at every time; the exact additive finite-lattice correction quantifies the deviation from continuum prediction. The result is fully self-contained and concerns the exact physically motivated observable rather than an arbitrary parameter slice.

## Limitations

Only the second moment for uniform KMP exchange, one initially loaded site, and symmetric bonds on the infinite line is covered. No full finite-time probability law or higher cumulants are derived. Independent verification is not claimed.

Self-review: passed. Independent audit: not yet performed.
