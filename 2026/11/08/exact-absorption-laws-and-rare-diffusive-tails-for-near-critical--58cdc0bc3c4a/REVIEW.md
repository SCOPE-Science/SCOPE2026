# Scientific review

## Correctness — PASS

The claim is about the exact specific simple sticky walk of [1], not all generalized war models. Two first-step conditioning branches and their second-step continuations exhaust the state space; on the nonabsorbing outcomes exactly two active players remain and evolve as ordinary unbiased gambler’s ruin. The exact generating function solves the correct boundary-value equation and reproduces the exact expected-time formula, with the \(k=0\), \(k=1\), and \(k=m\) edge cases treated separately. The dense-excess limit follows by explicit Laplace-transform convergence with fixed Brownian diffusion normalization. The sparse-excess theta tail follows from the full killed-walk sine spectrum; negative eigenvalue modes are controlled, rather than dropped. An elementary reflection bound proves the collapse in probability despite the mean scaling. A completely independent, unreduced finite Markov-chain checker passed 2,205 exact-rational survival, transform and expectation comparisons. The infinite theorems rest on the mathematical proof, not on these tests.

## Originality — PASS, with residual priority risk

The closest paper is Adjei–Krishnan–Mossel [1], which *already* supplies the model and the qualitative two-round gambler’s ruin argument in Remark 3.4, and predicts an \(mk\)-order duration when \(k=o(m)\). That overlap is substantive, explicitly credited and not presented as new. Its actual statements and relevant later-version full text do not state the exact full finite absorption law, the arbitrary positive-density Brownian scaling theorem, or the explicit sparse-excess \(m^2\)-tail theta profile that isolates rare-event domination. The classical two-player ruin law [2] is an ingredient, not the claimed novel result. Relevant mathematical-record queries and previous accessible claims yielded no identical or stronger implication. A complete priority guarantee is not available; related preprints or unpublished general hitting-time results may be overlooked.

## Value — PASS

The source explicitly highlights the transition between immediate absorption when the number of cards equals the number of players and quadratic duration at positive excess density. Exact first and second-round probabilities distinguish typical and mean duration and provide a complete law rather than an order estimate. The surprising \(\tau_{m,k}/(mk)\to0\) in probability together with \(\mathbb E\tau_{m,k}\sim mk\) and the explicit \(\Phi(t)\) identifies precisely how rare long paths control the expectation. The object and scaling are source-motivated, not arbitrary parameters added to a known formula.

## Scientific limitations

Only uniform winner selection and one/two-card initial configurations are covered. The limiting theta profile concerns fixed positive diffusive times and not the full distribution on all scales; no uniform error rate is asserted. Historical priority still warrants independent expert literature checking.

## References

[1] Adjei, Krishnan and Mossel, *Multiplayer Games of War*, https://arxiv.org/abs/2409.05201 (first public version 2024-09-08; relevant updated complete text pp. 3–5, 13–14).

[2] Bhatia, Chin, Mani and Mossel, *When Will (Game) Wars End?*, https://arxiv.org/abs/2302.03535.

Self-review: passed. Independent audit: not yet performed.
