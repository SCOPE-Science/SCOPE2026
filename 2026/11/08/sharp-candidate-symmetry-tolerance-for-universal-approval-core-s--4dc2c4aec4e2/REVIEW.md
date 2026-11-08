# Scientific review

## Correctness

**PASS.** The integral Hare-core definition is equivalent to requiring that every nonempty proposal of size \(t\le k\) has strictly fewer than \(nt/k\) voters whose approved-candidate count improves. Exchangeability proves the block-comparison lemma without candidate independence, the sharp integer gap is \(1/[k(k+1)]\), total variation controls the aggregate drift, and the nonidentical Bernoulli Chernoff bound yields simultaneous stability. The one-hot multinomial construction verifies exact sharpness and the binomial large-deviation rate. Exact finite verification checks 446,363 candidate-symmetric comparisons, 6,678 direct core profiles and 14 rational boundary identities. The general theorem and asymptotics rely on the written proof, not finite enumeration.

## Originality

**PASS, with residual bibliographic risk.** The closest primary work is Becker–Greger–Peters (arXiv:2609.11912), which guarantees existence of at least one Hare-core committee in every approval election, not simultaneous stability of all committees under nearly symmetric random ballots. Peters (arXiv:2501.18304) proves restricted deterministic existence. Goel–Jiang–Zhou (arXiv:2609.00486) investigate fractional Nash-core and small voter populations. Chen–Hatschka (arXiv:2605.22528) establish the equivalent NTU-AV/PAV/SAV core formulation, but study structural membership/existence rather than random-population symmetry. Han and colleagues (arXiv:2510.18718) study stochastic **average justified representation**, explicitly distinct from core. Source comparisons considered equivalent core definitions, broader existence results, and distributional aliases; no dominating theorem was identified. An unindexed equivalent result cannot be ruled out.

## Mathematical value

**PASS.** The theorem shows that a celebrated coalitional fairness axiom may become non-discriminating on large neutral electorates because *all* candidate committees satisfy it, even when the ballots are correlated within voter. The sharp \(1/[k(k+1)]\) total-variation radius quantifies the first asymmetry at which that statistical conclusion can fail. This offers a concrete benchmark for comparing core-based decision rules and tests the practical selectivity of the criterion.

## Scope and limitations

Only the integral Hare core and independent voters are covered. No claim is made for core+, fractional or Droop blocking, arbitrary dependence across voters, or convergence without controlling growing dimensions. The sharpness construction addresses a uniform threshold across approval distributions; it is not a necessary test for every distribution. The result is not a substitute for independent scientific review.

Self-review: passed. Independent audit: not yet performed.
