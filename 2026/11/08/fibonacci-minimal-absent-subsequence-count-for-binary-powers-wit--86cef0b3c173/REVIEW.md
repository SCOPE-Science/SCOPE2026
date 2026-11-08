# Self-review

## Correctness: PASS

The one-letter-deletion bridge characterization is necessary and sufficient for minimal absence. Reconstructing greedy embeddings in the two-run power shows that every reachable ready run-start state has two disjoint continuations, advancing by one or two runs, and that the last two ready states admit respectively two and three completions. A word starting in zero is forced through the first zero run before reaching the third run (or terminating), while one starting in one is ready at the second run. This gives \(F_{2k+2}\) for every \(a,b\ge2\) and \(k\ge1\). Explicit endpoint and initial-run cases are included. Literal finite checks corroborate but do not replace the proof.

## Originality: PASS, with residual risk

The closest direct predecessor is Kosche–Koß–Manea–Siemer, *Absent Subsequences in Words* (arXiv:2108.13968), especially Theorem 3.1 and Proposition 3.8. That work proves the general greedy bridge criterion and a different exponential family, not this exact closed binary two-run count in the inspected statements. Manea–Ringleb–Siemer–Winkler (arXiv:2504.21471) give general optimal enumeration algorithms but no inspected family-specific Fibonacci result. The specific new content is the reduction to two ready-run jumps and the resulting exact count independent of both non-singleton run weights. An unindexed equivalent is possible; generic computability is not mistaken for a reported formula.

## Value: PASS

This counts the entire antichain of minimal absent scattered subsequences—not only the shortest absences—in an infinite natural repetition family. The sharp threshold at run length two exposes a different growth mechanism from singleton-run sources. The computation-free exact Fibonacci law and run-length invariance are mathematically motivated structural facts useful as benchmarks for compressed subsequence languages and antichain enumeration.

## Verification and limits

The standalone verifier passed direct versus greedy-bridge equality on 25 finite instances and an additional 4,056 graph-count comparisons, including boundary \(k=1\). The proof does not address length-refined counts, other alphabets or singleton-run cases, and bibliographic exhaustiveness is not established. The independent scientific audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
