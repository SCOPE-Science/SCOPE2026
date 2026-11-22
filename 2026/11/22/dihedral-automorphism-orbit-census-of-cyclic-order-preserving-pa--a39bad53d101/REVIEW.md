# Self-review of a rank-refined dihedral orbit census

## Correctness: PASS

For the exact domain of all injective cyclic-order-preserving partial maps on \(n\ge3\) points, each rotation-fixed map is determined by two invariant \(k\)-subsets and one of \(k\) cyclic shifts; each reflection-fixed map is determined by matching numbers of fixed vertices on two invariant subsets and \(\gcd(2,k)\) compatible cyclic shifts. These disjoint cases account for every automorphism, so rank-wise Burnside counts are exact. The divisor-sum total follows from Vandermonde identities. The equalities for the two boundary ranks and the rank immediately below full rank follow by direct evaluation. The embedded code checks the fixed counts against actual maps, and constructs actual orbit partitions in small degrees; finite checks corroborate the proof, not the reverse.

## Originality: PASS, relative to inspected evidence

Li and Fernandes (arXiv:2207.12823) and the earlier automorphism-group theorem provide the group action; Umar (2011) provides raw rank counts but not its orbit quotient. The published parity-and-totient classification addresses only longest nilpotent maps at rank \(n-1\), whereas this theorem classifies **all** ranks. The published involution count for the dihedral inverse monoid concerns a different monoid and does not imply the present result. The numerical divisor sum is not claimed as a general new Burnside theorem. An earlier universal cycle-index formula could subsume the statement. The initial 2000 presentation paper was available only through bibliographic and abstract material, leaving a residual priority risk.

## Value: PASS

The rank-wise quotient is a natural complete symmetry census of a well-established inverse monoid, not merely an evaluation of its known raw cardinality. Explicit reflection corrections and nontrivial stabilizers make the orbit distribution genuinely different from naïve division by the automorphism-group order. The sharp \(\binom n2+1\) next-to-full-rank law and asymptotic generic freeness quantify structural features across every degree.

Self-review: passed. Independent audit: not yet performed.
