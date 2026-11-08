# Self-review

## Correctness — PASS

The root-clock and non-root transitions were reconstructed from the literal growth rule. In particular, root doubling maps vertex size and leaf imbalance by \((s,i)\mapsto(2s+1,2i-1)\), with total non-root birth rate \(s-1\); this normalization is crucial. Generator calculations for \(i\), \(i^2\), \(d\), and \(iz^d\) give a closed pair of scalar evolution equations. Their exact solutions yield the claimed generating transform, variance, and covariance. Standard moment bounds justify unbounded-observable Dynkin identities. The standalone exact-rational checker passed 10,263 checks, including eight-order generator Taylor tests. No finite check is presented as an infinite proof.

## Originality — PASS (best-knowledge, with residual risk)

The inspected full arXiv text of Björnberg–Mailler (arXiv:2501.18466) establishes the root-doubling model, size moments, degree proportions and Poisson root-clock embedding, but does not state the mixed leaf-imbalance generating transform or its finite-time covariance and variance. Classical outdegree CLTs for ordinary random recursive trees omit root doubling. The closest accessible related claim concerns the size scaling limit of this same model, not the joint leaf-imbalance and root-clock moments. Actual published-finding corpus and literature searches looked for exact and equivalent formulations. Priority remains provisional: a broad unlocated Markov-generator identity could imply the formula.

## Value — PASS

The precise invariant is motivated by separating shape fluctuations from random total size: \(2L-N\) vanishes at first order relative to size, yet its continuous-time second moment grows at a computable exponential rate. The Poisson-tilted transform resolves conditional mean imbalance across every doubling-count stratum, with the exact negative covariance \(-t^2\) exposing a dependence unmeasured by the source paper's degree-frequency theorem. These are nontrivial joint finite-time identities for the natural root-doubling model, rather than an arbitrary parameter slice or a restatement of limiting frequencies.

## Limits and closest literature

The result is confined to the natural three-vertex post-first-doubling state in continuous time; it does not assert a Gaussian limit or a complete conditional law. Closest sources are Björnberg–Mailler (arXiv:2501.18466, accessible full HTML) and Mahmoud–Smythe (1992, bibliographic/abstract-level coverage for classical outdegrees). Historical completeness cannot be certified by these searches.

Self-review: passed. Independent audit: not yet performed.
