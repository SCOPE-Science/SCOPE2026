# Scientific review: Brownian first-passage crossover

## Correctness — PASS

The claim concerns static random \(D>0\) with finite mean, without hidden integrability hypotheses. The reflection-principle CDF, strict early-time dominance, and the late-time limit (including the infinite-negative-moment case via Fatou) yield opposite endpoint signs. Exact differentiation reduces the derivative sign to a strict-convexity problem for the exponentially tilted inverse-diffusivity moment. This proves exactly two nondegenerate stationary points and one CDF crossing. Direct second differentiation and strict Jensen yield the stated bounded-support bracket. The full quantified proof is in RESULT.md, with independent symbolic and high-precision test examples in checker.py. Numerical examples alone do not certify the infinite family.

## Originality — PASS, qualified

The CDF mixture, Jensen-based characteristic-time comparison and an implicit crossover equation are already in Sposini et al. (arXiv:2403.10138v1, equations (31),(34)–(39)); these are **not new**. The paper calls the crossing typical and does not provide a general theorem guaranteeing the one-crossing and two-extrema counts for every static positive finite-mean distribution. Sposini, Chechkin and Metzler (arXiv:1809.09186v1) describe a crossover in a time-varying diffusivity model, with independence from initial position in their scaling formulation; that is not a general static-mixture uniqueness theorem. The 2024 companion concerns extreme searches; Grebenkov et al. (arXiv:2007.05765v1) treat time-varying diffusivity examples. No matching stronger implication was identified in the examined records. An equivalent application of an earlier general variation-diminishing principle remains possible, and one directly related 2024 review chapter could not be fully inspected.

## Mathematical value — PASS

The unique threshold makes the preexisting implicit criterion operational for all admissible quenched mixtures and rules out reentrant early/late targeting efficiency. Counting the exactly two extrema gives a complete qualitative phase portrait of the CDF difference. The strict support-only bracket provides a useful prior range for a crossover search, and the theorem remains valid when the negative half-moment diverges, covering a natural nonuniform-diffusivity boundary that cannot be handled by a finite-coefficient long-time expansion. This is a motivated structural result rather than a table lookup or arbitrary parameter slice.

## Limits and risks

Applicability is to independent Brownian trajectories with static diffusivity draws and one absorbing half-line target. It does not cover dynamically fluctuating diffusivity, finite domains, noise in empirical estimates, or an explicit universal closed-form time. The originality comparison is not independent publication certification; unindexed variants or broad total-positivity theorems may overlap. The 2024 handbook chapter listed in RESULT.md was inaccessible for full-text inspection.

Self-review: passed. Independent audit: not yet performed.
