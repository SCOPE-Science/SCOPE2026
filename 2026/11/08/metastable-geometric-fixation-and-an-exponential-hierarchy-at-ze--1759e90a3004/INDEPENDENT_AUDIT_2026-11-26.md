# Independent mathematical audit

## correctness

PASS

Counting maps from the n ballots onto j of k active labels yields the stated Stirling kernel; first-step conditioning gives the PGF. Each visited k has one geometric holding block with exit probability a_k at least ((k-1)/k)^n. At entry into {1,2}, the conditional ratio P(k,2)/P(k,1)=(k-1)(2^n-2)/2 gives the shortcut bound uniformly, and the post-entry time from 2 is an independent positive geometric. A deterministic shift u costs exactly 1-(1-q_n)^u in total variation, giving the displayed bound after averaging the entrance delay, including the empty delay for k=2. For fixed k, at first entry into {1,...,k}, the ratio of probabilities below and at k is O_k(((k-1)/k)^n) uniformly over the preceding state, by surjection count bounds. The resulting missing-visit probability changes h_k/a_k by O_k(1). The two-empty-bin term in a_k is O_k(((k-2)/k)^n); the reciprocal correction is bounded since k(k-2)/(k-1)^2<1 (and is zero at k=2). The tail above fixed r is bounded by the first remaining hold-time bound plus n times the next, giving the claimed exponential remainder. These analytic arguments do not rely on extrapolating the checker.

## originality

PASS

Credit is for the quantitative full-process comparison and especially the complete subleading fixed-level expectation hierarchy, not the Stirling kernel, binary metastable mechanism, leading expectation, or scaled exponential limit. The strongest matching indexed theorem explicitly includes the same zero-reinforcement endpoint and those leading conclusions. Its initial-contraction and two-label estimates are close predecessors (and readily recover a geometric comparison in this specialization); they do not give the frozen explicit uniform bound or the hierarchy of contributions from all fixed higher survivor levels.

## value

PASS

A leading metastable clock does not determine the transient contribution to the mean. Here each fixed survivor level has a distinct exponential contribution with a controlled remainder at the next rate. The first correction, (3/2)^n/3, is exponentially large in absolute terms and identifies a separate three-survivor timescale; the complete hierarchy makes this quantitative beyond the leading overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
