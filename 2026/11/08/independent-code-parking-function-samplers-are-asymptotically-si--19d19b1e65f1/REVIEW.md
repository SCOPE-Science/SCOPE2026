# Review of independent-code parking-function singularity

## Correctness

**PASS.** The proof has one decisive statistic: the surplus of preferences at \(\lfloor n/2\rfloor\). Under independent bounded codes it is exactly a Poisson--binomial sum with variance at most its mean. Under the uniform parking-function law it has a non-atomic Brownian-excursion limit after division by \(\sqrt n\), using Diaconis--Hicks Theorem 15 (via Chassaing--Marckert). A two-case Chebyshev argument treats all possible means uniformly and establishes total-variation distance tending to one. The non-atomic weak-limit lemma is proved in RESULT.md. Every quantifier includes arbitrary row-dependent marginal laws. Exact rational finite checks agree with the independent-code formula; they are not used to justify the infinite conclusion.

## Originality

**PASS, with historical-priority qualification.** Pinsky's full arXiv manuscript arXiv:2509.24452v2 contains an explicit open question about whether a Mallows parameter regime can have limiting full-law total-variation distance below one. His marginal and occupancy-count limits do not entail the answer. Diaconis--Hicks and Chassaing--Marckert establish the Brownian-excursion limit, not the separation against arbitrary independent bounded codes. Bellin treats small-coordinate projections and does not imply the global comparison. Targeted literature and mathematical-record searches did not identify the uniform independent-code impossibility theorem. A previously unnoticed combination of the classical excursion theorem with the code independence is the main residual priority risk; novelty is not certified independently.

## Mathematical value

**PASS.** The claim resolves the explicit approximation question for *every* parameter sequence rather than a handpicked regime, and establishes the structural reason: independent factorial-code coordinates cannot generate the order-\(\sqrt n\) nondegenerate bulk-surplus fluctuations of a uniform parking function. The broad theorem rules out an entire natural family of exchangeable approximate samplers in full-law total variation while remaining compatible with weak agreement of finitely many coordinates. The result is not merely a computation or a restatement of the excursion theorem.

## Closest literature and scope limits

The code independence and the motivating open question come from Pinsky (2025), the input excursion process from Chassaing--Marckert (2001) and Diaconis--Hicks (2017), and related finite-projection results from Bellin (2023). This theorem does not cover dependent-code sampling, nor does it compute an optimal finite-size variation distance. Its conclusion applies to the entire parking-function law and does not contradict matching low-dimensional marginal limits.

Self-review: passed. Independent audit: not yet performed.
