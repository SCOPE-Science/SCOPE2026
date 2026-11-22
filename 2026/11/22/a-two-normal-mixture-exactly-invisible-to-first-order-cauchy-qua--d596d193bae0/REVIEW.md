# Scientific review: two-normal Cauchy-quantile mimicry

## Correctness — PASS

For the exact eight-decimal outer quantile probability, the published scalar interquantile-ratio statistic has a standard joint-quantile central limit theorem. The delta-method variance is reconstructed from the nested Brownian-bridge increment covariance. The Cauchy variance formula follows algebraically from its four population quantiles and two relevant densities. The monotonicity identity for the Gaussian mixture quantile ratio yields a unique continuous scale along which the target Cauchy ratio holds. An exact-rational interval checker then proves **opposite strict variance signs** at mixing weights \(0.08\) and \(0.20\), forcing an exact variance-matching point by continuity. The checker is part of the package, was run successfully on the packaged code, and does not rely on floating-point signs. An approximate numerical solution is not the theorem's certificate.

Risk/limits: the result is a first-order weak-limit assertion for sample quantiles with the usual Bahadur law; it does not assert equality of finite-sample distributions or validity for exotic non-quantile-convergent estimators. The proof assumes iid observations and positive densities at the fixed quantiles.

## Originality — PASS, with historical uncertainty

The primary Cauchy four-quantile test (Pekgör, 2023, DOI 10.1155/2023/9200213) provides the index, asymptotic null normal law and a numerical comparison with single Gaussian and other alternatives. In the inspected full article, its empirical discussion says power can be low near the Cauchy index, but no two-normal construction matching *both the index and its asymptotic fluctuation variance* was found. The closest older quantile test (Rublík, 2001) uses a different fitted-parameter quadratic statistic and moving extreme ranks. The Ebner–Eid–Klar Cauchy test (2022) uses a different Fourier–Stein characterization. A related earlier Cauchy quantile-ratio extreme-tail calculation concerns fixed-sample Cauchy-null tail exponents, not the present asymptotic normal-limit equality under a non-Cauchy mixture. There is no implication from any of those statements to the exact two-equation Gaussian-mixture matching theorem.

Risk/limits: absence from inspected texts and mathematical searches does not certify absolute priority. The publisher's HTML conversion omitted some rendered equations; the ratio and four quantile levels were independently triangulated with the article's stated numerical Cauchy index and asymptotic discussion. A separately available PDF rendering of the original article was not obtained.

## Value — PASS

The published procedure selects outer quantiles specifically to separate Cauchy data from a single Gaussian alternative. This theorem shows that the very same scalar test is asymptotically unable to distinguish a smooth, strictly unimodal, all-moments-finite two-Gaussian mixture from Cauchy **even at the fluctuation-law level**, not merely in its population index. It gives an explicit structural minimality statement within the natural Gaussian scale-mixture class and an exact rational crossing certificate. That is a statistically meaningful limitation on claimed omnibus use: nominal asymptotic power instead of consistency for an elementary, well-behaved alternative.

Risk/limits: it pertains only to the fixed-four-quantile scalar statistic and Gaussian or asymptotically equivalent null-critical calibration; other, richer goodness-of-fit procedures can detect this alternative.

Self-review: passed. Independent audit: not yet performed.
