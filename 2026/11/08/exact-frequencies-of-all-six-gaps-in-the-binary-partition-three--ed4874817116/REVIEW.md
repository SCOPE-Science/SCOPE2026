# Scientific review

## Correctness — PASS

The claim is the six-component frequency vector for consecutive exceptional indices, each with an absolute \(O(\log(J+2))\) discrepancy, for every integer \(J\ge1\). The proof derives four exhaustive length-16 block types from the cited exact exceptional-index criterion, proves logarithmic-error Thue–Morse adjacent-pair frequencies from the explicit correlation recurrence, enumerates all eight nonzero allowed type transitions, and counts internal and cross-block gaps. Their rates sum to \(4/3\) gaps per block and normalize to the stated vector. The exact-count Python checker independently tested 4,097 binary-partition evaluations, 65,538 full 16-blocks and 87,381 consecutive gaps. These experiments do not substitute for the infinite argument.

## Originality — PASS within inspected sources

Sobolewski and Ulas [1] explicitly list all six possible gap lengths in Proposition 3.4 and prove a sharp total exceptional-set counting estimate in Theorem 6.1. They do not state any componentwise gap-frequency law. The law is not a restatement of the gap spectrum or total exceptional density, since neither determines relative frequencies. The article's exact block indicator does supply the underlying objects, and the present proof adds the two-point Thue–Morse correlation and complete transition accounting. OEIS A363769 gives sample positions and the indicator, without the vector. Targeted literature searches found no explicit covering result; hidden or unindexed equivalent consequences are an acknowledged risk.

## Value — PASS

The six-gap spectrum was a conspicuous exact invariant of the exceptional binary-partition sequence, and its authors separately investigated the complexity of the ordered gaps. The new result gives the full natural law of those gaps and quantitative logarithmic discrepancy, not a finite sample or a restatement of the known total density. It may inform analysis of derived sequences and statistical structure without claiming to resolve automaticity.

## Closest literature and limitations

[1] B. Sobolewski and M. Ulas, *Values of Binary Partition Function Represented by a Sum of Three Squares*, arXiv:2211.16622; *Results in Mathematics* 78, 188 (2023), DOI:10.1007/s00025-023-01966-8 (Corollary 3.3; Proposition 3.4; Theorem 6.1; Section 7). [2] OEIS A363769, https://oeis.org/A363769. No result is asserted about colored partitions or automaticity of the ordered gap sequence. An independently verified priority determination is still needed.

Self-review: passed. Independent audit: not yet performed.
