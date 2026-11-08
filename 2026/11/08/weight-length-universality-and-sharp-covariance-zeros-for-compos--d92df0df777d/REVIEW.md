# Scientific review

## Correctness — PASS

For every exact consecutive word of length \(r\ge2\) and total weight \(w\), marking one occurrence decomposes a uniform composition into two unconstrained sides. The bivariate rational series \(u^r z^w/(1-u z/(1-z))^2\) then yields all first mixed moments. The coefficient identities and binomial mean of the part count prove the exact covariance, and the sign cases are exhaustive because \(2r-w\) is integral. The events at the two zero boundaries are shown dependent by their deterministic conditional part counts. The standalone exhaustive checker passed 24,558 finite exact assertions for sizes through 12. The all-size proof does not rely on those finite checks.

## Originality — PASS (provisional historical assessment)

Closest primary literature: Heubach–Kitaev (arXiv:0903.5135) and Wilf (arXiv:0906.5196) derive weight/length generating functions for *avoiding* prescribed words or equal-part runs; Gafni (arXiv:0907.5553) studies longest equal runs; Bender–Canfield (DOI 10.37236/197) treats general local-event asymptotics; Shabani–Gjergji (DOI 10.46298/dmtcs.2156) studies occurrence statistics of order-isomorphic short patterns. The inspected results do not supply the all-exact-word mixed covariance or universal sign/zero classification. Closest previously recorded composition findings cover part-size covariance matrices, the part-count/maximum relation, and an endpoint/bulk variation covariance, not occurrence counts of arbitrary fixed exact words. The excluded one-part special case is elementary and not presented as a new contribution. General pattern generating-function technology might make the identity recoverable, and a historical source not located here could contain the explicit classification.

## Value — PASS

The problem concerns a natural dependence statistic in uniform random compositions: how the total number of parts biases the local frequency of a prescribed block. Self-overlap strongly influences the *distribution* of a pattern count, yet remarkably does not influence this mixed covariance at fixed word length and total weight. The complete sharp sign diagram, the two dependent zero-covariance cases, and the sample-size-constant covariance family distinguish structural phenomena from a routine expectation formula. The result is an exact finite-sample characterization; no downstream theorem or independent validation is asserted.

## Scope and residual risks

The sampling law is unrestricted uniform composition; the word is exact and consecutive, not a relative-order pattern. No statement is made for other composition distributions or higher moments. Historic implicit coverage and the possibility of an equivalent unstated corollary of general generating-function machinery remain the main originality risks.

Self-review: passed. Independent audit: not yet performed.
