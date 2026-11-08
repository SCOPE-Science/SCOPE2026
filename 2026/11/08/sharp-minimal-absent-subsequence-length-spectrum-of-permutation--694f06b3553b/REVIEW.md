# Scientific review

## Correctness

**PASS.** Greedy matching in a repeated permutation yields the exact criterion \(D(v)\le k-1\). The first/last deletion constraints force \(D(v)=k\) and descending endpoints, and interior deletions give the necessary and sufficient three-letter identity. Every ascent imposes two strict two-step increases, one per parity track; all other two-step comparisons are nonincreasing. A \(q\)-letter track has at most \(q-1\) rises per increasing run. This proves the sharp inequality on the ascent count. Concatenated doubled staircases, with additional leading zero repetitions, attain each allowed count. Direct literal tests (14 host configurations and 65,958 candidate strings) and separately implemented finite-state tests (136 configurations) agreed. The tests alone are not an infinite proof.

## Originality

**PASS with residual bibliographic risk.** The closest primary source [1], which was inspected in its pertinent Section 3, uses the *same* host family and constructs an exponentially large subset of its minimal absent subsequences (Proposition 3.8); it does not determine the longest possible length or show that all intermediate lengths occur. The subsequent general longest-minimal-absent-subsequence algorithm [2] solves arbitrary fixed inputs, not this symbolic full parameter and length-support classification. Earlier two- and three-symbol special cases are already recorded and are not claimed again. No equivalent result appeared in the searches of the relevant published records or the local accessible prior claims, but unindexed equivalences remain possible.

## Mathematical value

**PASS.** Rather than merely constructing long absent words or applying a general algorithm to an instance, this provides the exact extremal cutoff and the full uninterrupted length support for every power of every permutation of arbitrary size \(q\ge4\). The parity-track obstruction and sharp doubled-staircase family identify a structural mechanism and yield the nontrivial asymptotic slope \(2q/(q+1)\). It supplies a natural infinite-family benchmark for the longest-minimal-absent-subsequence problem.

## Closest sources and limitations

[1] M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, https://arxiv.org/abs/2108.13968 (2021), Section 3, Proposition 3.8.

[2] F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, https://arxiv.org/abs/2504.21471 (2025), longest-minimal-absent-subsequence algorithm.

The claim is limited to the full permutation-power host alphabet and length support, not exact multiplicities, arbitrary hosts, or independent validation. An unindexed equivalent is the principal originality risk.

Self-review: passed. Independent audit: not yet performed.
