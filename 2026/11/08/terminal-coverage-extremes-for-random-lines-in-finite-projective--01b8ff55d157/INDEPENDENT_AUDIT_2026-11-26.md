# Independent mathematical audit

## correctness

PASS

For any fixed active set A of distinct points, incidence and pair uniqueness give |A|k−binom(|A|,2)≤H(A)≤|A|k, hence log avoidance is −|A|/s+O(|q|^−2) for bounded |A|. The full-subset hypergeometric product gives the same uniform bound. For different deadlines, the sum of the active-set sizes across rounds is the sum of the individual deadlines; the log error across O(q log v) rounds is O(log v/q). This yields the mixed labelled survival asymptotics, with rounding error O(1/s). By interval inclusion–exclusion they give all mixed factorial moments of disjoint bounded interval counts, and bounded expected compact counts give vague point-process tightness. Counts above any fixed threshold also have the Poisson limit, with the expected number above an increasing upper threshold tending to zero, so the highest finitely many points converge jointly. The map x↦exp(−x) turns the limit into rate-one Poisson arrivals, giving the stated ranks and the Gumbel maximum. For the moments, both samplers have pair avoidance 1−(2k−1)/v: for the full sampler this uses k(k−1)=v−1. It is less than the square of the one-point avoidance probability by q/v². Thus Var(U_t)≤E(U_t), and 1/E(U_t) bounds early complete coverage, while E(U_t) bounds the late tail. At the early threshold up to s log v, log(1−1/s)=−1/s+O(1/s²) gives E(U_t) bounded below by a constant times exp(x); negative round thresholds give zero probability of early completion. Both centered tails are bounded by Ce^(−x), yielding the two Gumbel moments and both little-o differences since s is asymptotic to q. The argument needs only the plane axioms; the finite checks in CHECK.py were read, not executed, and do not prove any asymptotic conclusion. The detailed replay is RESULT.md §§1–4.

## originality

PASS

The supported distinct contribution is the multitime first-hit limit for restricted line draws along arbitrary existing plane sequences, with joint fixed terminal ranks and the first two cover-time moment asymptotics compared with uniform full subsets. No first claim is credited for one-time Poisson uncovered counts, a coupon-collector Gumbel law in a different model, or finite-order mean comparisons. The strongest checked design and coupon-collection results do not state the combination or imply the multitime estimates on their retrieved assumptions. Historical priority remains provisional, especially for broader random-covering results.

## value

PASS

Equality of block size and pair incidences does not make the samplers identical. The result explains why the same extreme process and the same leading cover-time fluctuations nonetheless hold despite different higher joint laws, for all projective planes without coordinates. The marked limit distinguishes higher waiting times from a single completion-time estimate, and the quantitative moment asymptotics explain what the limiting law does and does not resolve about the comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
