# Review of the fair Peres residual bound

## Correctness (C): PASS

The statement fixes the input distribution, the exhaustive pair transformation, the meaning of residual length, and the exceptional cases \(N=0\) and \(N=1\). The conditional-uniformity argument yields the exact binomial recurrence. The proof establishes a global quadratic minorant for powers with exponent \(0<\alpha<1\), bounds the Jensen deficit by a nonzero-binomial probability, then completes the even/odd strong induction. The odd-step upper inequality is proved for every integer by comparison with square roots. The standard-library checker independently exhausts all binary words through length twelve and uses rational recurrence values through length 150; no finite test substitutes for an infinite proof.

## Originality (O): PASS against inspected literature

The closest primary publication is Lim, Liao and Yao, *Asymptotic Analysis of Peres' Algorithm for Random Number Generation* (2020; DOI: https://doi.org/10.1017/S0269964820000510). Their full manuscript proves a logarithmic exponent limit for the same mean cost but not its two-sided \(\Theta(N^\alpha)\) envelope. They explicitly identify stronger asymptotic information as unresolved. Garivier, *The Exhaustive Peres Transform: Extraction and Universal Coding* (2026; https://arxiv.org/abs/2610.26396), §8, records the identical recurrence and the exponent heuristic for the mean, while his main pointwise bounds are for residual one counts, a different invariant. The 2018 paper by Prasitsupparote, Konno and Shikata (https://doi.org/10.3390/e20100729) discusses finite-iteration or heuristic maximal redundancy. The available indexed mathematical results and the inspected documents did not cover the explicit uniform bounds.

Residual risks: priority cannot be proven by a finite search; an overlooked equivalent recurrence theorem or a stronger unindexed estimate is possible. The full 2018 document was not locally available, though relevant primary indexed sections were examined. The exponent and recurrence are known, so only the global constant-factor strengthening is claimed as new.

## Value (V): PASS

Uniform constants at the exact golden-ratio power give a strictly stronger efficiency guarantee than a logarithmic exponent. They rule out all divergent slowly varying multipliers and establish the all-length residual order, a natural coding and randomness-extraction invariant studied in both cited papers. The work does not claim to settle normalized convergence, worst-case residual-one growth or biased sources.

Self-review: passed. Independent audit: not yet performed.
