# Self-review

## Correctness — PASS

The one-step first-arrival decomposition is exhaustive, and the residual graphs in all four cases are identified explicitly. The resulting rational probability laws normalize to one; their two upper-tail crossings and strictly positive expectation difference follow by exact subtraction. All connected original graphs on at most three vertices are \(K_1\), \(K_2\), \(P_3\), or \(K_3\); each pendant attachment has the stochastic-order direction shown in the proof. An exact independent recurrence checker reproduced the formulas and minimality checks (179 assertions). Computation tests do not substitute for the infinite-family algebraic proof.

## Originality — PASS, with historical-priority risk

The closest inspected full-text source, Krivelevich–Mészáros–Michaeli–Shikhelman, https://onlinelibrary.wiley.com/doi/10.1002/rsa.21200 , introduces the process and treats expectations and tree extremizers; it discusses a different failure of expected-value monotonicity under edge deletion. It does not assert this exact two-threshold comparison under *pendant extension*. AofA 2020 DOI:10.4230/LIPIcs.AofA.2020.20 also describes expectation and tree results. Separate mathematical-record searches for pendant-extension stochastic ordering and greedy independent sets returned no covering theorem. Existing private matching-augmentation and decorated-path results concern different random variables/graph classes and imply neither crossing. Literature searches cannot prove uniqueness; historical priority remains a risk.

## Value — PASS

The natural question “does a locally enlarged tree produce a stochastically larger greedy independent set?” has a sharp negative answer already at four original vertices. The infinite star family shows two opposite tail movements while the mean moves upward, separating stochastic-order claims from expectation-level intuition. An exact order cutoff and full probability laws make this a structural boundary rather than an isolated numerical counterexample.

## Limits

No universal monotonicity claim for expected size is made; there is no theorem classifying all connected graph families. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
