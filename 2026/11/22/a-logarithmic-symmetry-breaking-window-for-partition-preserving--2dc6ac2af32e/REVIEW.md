# Scientific review: logarithmic asymmetry of partition-preserving retractions

## Correctness — PASS

The proof works for every fixed integer \(m\ge2\), every real perturbation vector, and all sufficiently large \(n\). It starts from a verified rooted-fiber product count, proves a uniform saddle at image-point count \(tn/\log n\), derives the strict entropy gap for multiple target blocks, and then obtains the critical softmax law from the logarithmic one-point sensitivity of the rooted count. The sensitivity formula explicitly includes the extra endpoint term that arises when the target block size increases. The uniform large-size extension retains the total source size \(N\) in the leading formula, avoiding a potentially invalid \(o(n)\) replacement. Finite direct enumeration passes for six small block profiles; all thirty tested binomial increment identities pass. Finite experiments are corroboration, not proof of the limiting statement.

## Originality — PASS, subject to priority risk

The exact idempotent census for all nonuniform partitions is already established by Dolinka, East and Mitchell (2015), Proposition 3.1–3.2. The uniform case is covered by Dolinka and East (2014), and earlier equal-block entropy laws already show that multiple image blocks are exponentially rare. Nothing in those specific statements supplies the limiting selection weights after block sizes are perturbed by \(\lfloor\beta_j\log n\rfloor\), nor the exact threshold between uniform and deterministic target selection. The new mathematical step is the uniform one-unit root-capacity sensitivity, whose cumulative effect appears precisely on the logarithmic size scale. The published exact enumeration algebraically determines all finite probabilities, so this is a nontrivial asymptotic consequence of prior counts rather than a new finite enumeration. Independent priority checking against any broad older asymptotic saddle analysis remains advisable.

## Value — PASS

This fills a natural stability gap in the symmetry of random retractions of uniform partitions: equal blocks give an exactly symmetric target selection, while an additive perturbation of order only \(\log n\) produces arbitrary nondegenerate softmax selection laws. Pairwise smaller perturbations disappear in the limit and superlogarithmic gaps yield a deterministic winner. The exact scale and continuous crossover describe how strongly a finite transformation monoid amplifies small changes in block cardinality, beyond the first-order condensation entropy rate.

## Scope, related results, and limits

The statement is for fixed \(m\) and asymptotically equal block sizes; it does not cover growing \(m\), unequal macroscopic block proportions, or arbitrary transformation distributions. The rooted enumeration and its finite recurrence are antecedents. Relevant primary sources are arXiv:1407.3312 and arXiv:1504.02520, inspected in their available full-text HTML versions. No independent audit or external expert validation has been performed.

Self-review: passed. Independent audit: not yet performed.
