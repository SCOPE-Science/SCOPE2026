# Review of the exponential-lottery fairness threshold

## Correctness

PASS. The claim follows from the independence factorization \(P_{\mathrm{EF}}=p(1-p)\), exact exponential survival/Laplace identities, a strict three-good comparison, stochastic dominance reducing four-good partitions to two, and a rational difference factorization with a unique positive cubic root. The all-parameter conclusion is analytic; the standalone checker completed 2,427 exact allocation comparisons and the rational four-good witness. Computational tests alone do not certify unbounded parameter ranges.

## Originality

PASS, with residual publication-priority risk. Igarashi–Oh (arXiv:2610.34906) prove the common convolution-power case and a universal log-concave approximation ratio, and give a different general log-concave four-good counterexample (Theorem 4.2, Proposition 5.5, Appendix A.4). These are not the claimed exact all-exponential four-good phase classification or its three-good minimality. A pre-existing extremal pairing observation already handles ordering *within* the pair partitions; the new sign boundary is the comparison of the best pair with a singleton-triple ex-ante fair partition. Search comparisons found no exact covering statement; unindexed equivalent results remain possible.

## Value

PASS. The minimum size and sharp switching threshold are a motivated boundary for whether expected-value fairness maximizes realized fairness under one of the standard continuous positive value laws. The robust positive large-\(t\) coefficient shows this is not an isolated rational example. The result is a small-market exact structural theorem, not a general optimal-algorithm claim.

## Limits and closest work

The two-agent independent exponential model is essential; the four-good phase curve is restricted to means \((1,2,t,t+3)\) with \(t\ge2\). The earlier general counterexample means the novelty claim is not that arbitrary log-concave laws first fail at four goods. Sources: Igarashi–Oh, https://arxiv.org/abs/2610.34906 ; Aloisio et al., https://iris.gssi.it/handle/20.500.12571/30247 .

Self-review: passed. Independent audit: not yet performed.
