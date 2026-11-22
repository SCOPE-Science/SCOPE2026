# Scientific assessment: multivariate Raftery total-correlation law

## Correctness — PASS

For fixed \(0<\theta<1\) and every integer \(d\ge2\), the exponential marginal Laplace transform is exactly \((1+s)^{-1}\), the common-shock likelihood factors through the minimum, and conditional independence gives \(T_d=-d\log(1-\theta)-I(W;M)\). The minimum is exactly a Bernoulli–exponential shock plus an exponential noise of mean \((1-\theta)/d\). Its derived scalar density integrates to one. Entropy-of-mixtures and the elementary nonnegative-mean entropy bound give the full three-term asymptotic. A threshold classifier controls the only nonexplicit posterior-entropy remainder by a binary-entropy error bound. The standalone checker reproduces the exact reduction and numerical cases; no finite computation is promoted into an infinite-dimensional proof.

## Originality — PASS (qualified)

The 2023 Saali–Mesfioui–Shabri article is the originating source of the homogeneous Raftery copula and of its common-shock representation, both expressly credited. Its results concern density, moments, tail dependence, concordance and inference, rather than exact total correlation or its logarithmic high-dimensional correction. The 2024 heterogeneous-parameter extension likewise addresses construction, moments and estimation; its homogeneous specialization does not state the present relative-entropy law. General total-correlation identities in Rowe–Day (2019) and copula-entropy ideas in Ma–Sun (2008) are standard ingredients rather than equivalent family-specific results. Searches for entropy, mutual information, relative entropy and the Raftery common-shock family yielded no statement that dominates the new three-term expansion. This is a supported comparison, not a claim of globally certified priority; some earlier distribution-theory literature is not fully inspected.

## Value — PASS

Rank concordance and Pearson correlation do not quantify the accumulation of dependence across a growing vector. The exact conversion of a \(d\)-dimensional relative-entropy integral into one-dimensional sample-minimum entropy is computationally and structurally useful. More importantly, the \(-\theta\log d\) correction and its exact constant quantify the cost of recovering a mixed discrete/continuous shock, distinguishing the multivariate family from what pairwise dependence measures reveal. The concrete error envelope makes the formula usable without an unspecified asymptotic onset. This is a motivated information-theoretic property of an established copula, not an arbitrary parameter slice.

## Closest literature and remaining limits

- Saali, Mesfioui and Shabri (2023), *Multivariate Extension of Raftery Copula*, DOI 10.3390/math11020414: same homogeneous law and latent construction, but no total-correlation result.
- Saali, Mesfioui and Shabri (2024), *A novel multivariate copula of Raftery type with multiple dependence parameters and its neutrosophic application in finance*, DOI 10.54216/IJNS.230224: broader nonexchangeable parameter class, not an information-theoretic asymptotic classification.
- Rowe and Day (2019), *The Sampling Distribution of the Total Correlation for Multivariate Gaussian Random Variables*, DOI 10.3390/e21100921: general definition and Gaussian sampling theory, not the shock copula.
- Raftery (1984), *A continuous multivariate exponential distribution*, DOI 10.1080/03610928408828733: historical progenitor; full original text was not inspected, leaving a bounded historical-priority risk.

The theorem is fixed-parameter interior asymptotics only. The heterogeneous extension, parameter limits and any independent validation remain outside scope.

Self-review: passed. Independent audit: not yet performed.
