# Scientific review: restricted cyclic Rule 150 predecessor spectra

## Correctness — PASS

The exact three-term XOR collision recurrence has nonzero cyclic solutions precisely for multiples of three, with the three nonzero length-three blocks `110`, `101`, `011`. For each such shift the no-adjacent-one constraint forces exactly two choices in every disjoint triple; the resulting pair-edge count is \(3\cdot2^{k-1}\). The three pair-sets have only the one all-one-output triple fiber in common, so \(A_{n,2}+3=3\cdot2^{k-1}\), and the Lucas cardinality \(|X_n|=L_n\) fixes the singleton count. Both small-ring repeated-neighbor cases are included explicitly. Independent exhaustive enumeration of the defining source and observation maps agrees at every size \(1\le n\le21\). Finite enumeration is not used as the all-size proof.

## Originality — PASS, with limits

The 2024 paper on networks of elementary-rule necklaces and the public all-length Rule 150 necklace inverse-degree classification treat the *full binary source* and rotation quotient, not the hard-core restricted indexed source. The 2020 algebraic theory of additive cellular automata covers basic linear structure and decidability, not the required constrained-coset intersections. An article on von Neumann regularity considers golden-mean shift endomorphisms but does not derive this target-inverse count. The closest underlying four-element full-shift kernel is properly credited; novelty is restricted to its exact hard-core pair-intersection census and all-length restricted-fiber law. Unindexed coding and constrained symbolic dynamics are meaningful priority risks. The older 1984 polynomial-CA paper was not fully inspected in this run.

## Value — PASS

The no-`11` language is a canonical run-length-limited or Fibonacci constraint, and Rule 150 is a canonical three-local parity observation. The theorem gives a natural exact reconstruction invariant for every cyclic blocklength: the full list-size distribution, unique exceptional triple ambiguity, maximum ambiguity and codebook capacity. It is not a small numerical improvement or a computed isolated table. The exact probability of ambiguity under a uniform admissible input vanishes exponentially at rate \(2^{1/3}/\varphi\) along the divisible-by-three subsequence. Results do not address noisy reads, other restrictions or higher iterates.

Self-review: passed. Independent audit: not yet performed.
