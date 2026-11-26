# Independent mathematical audit

## correctness

PASS

A self-inverse map is exactly an automorphism of its domain of order dividing two. On a proper nonempty domain the graph of strict comparabilities is a disjoint union of alternating paths. Path reversal exchanges endpoint parities for even length and preserves them for odd length, giving the stated path types and internal automorphism counts; the two isolated-vertex parities are one poset type. An involution on a type class matches exchanged components (the isomorphism back is forced) and makes independent internal choices on fixed components, giving W. The trace counts all run-marked subsets once per mark, including periodic patterns; N/2 choices of starting position for each parity and division by the number of marks therefore give A_N. Full-domain parity-preserving rotations have just the identity and, when m is even, the half-turn as involutions, and the m parity-preserving reflections fix exactly two vertices. For corank two a deleted pair has N choices below antipodal separation and m at that separation. The per-domain weights below antipodal separation are 1 for odd d, 2 for d=2, and 4 for even d>=4. At the antipodal separation the two identical paths give 2 involutions if even paths, or 6 if odd paths (four in place and two swaps); this gives the two coefficients and agrees with the separate N=4 rank-two case. The antichain and component bounds with classical symmetric-group involution counts prove the logarithmic exponent; the rank substitution is U=Z, V=Z^2. An independent enumeration by extending each partial involution to fix all omitted vertices computed the rank spectra through N=12, confirming the total and boundary coefficients, without using cyclic runs or a transfer matrix. Replay: python3 /workspace/reproductions/frozen_checks.py 5.

## originality

FAIL

The exact stated crown polynomial need not have appeared verbatim: the earlier crown transfer result gives precisely A_N and all proper-domain path types; the earlier fence involution theorem gives precisely W for those same path types. W depends only on the disjoint union of paths and not its ambient embedding. Their product-sum therefore gives every proper-domain cycle coefficient by direct substitution. The known parity-preserving dihedral action on the full crown supplies the elementary identity/reflections/half-turn correction, and the empty term is forced. The advertised additional results do not establish a distinct claim beyond this mechanical synthesis. The earlier crown proof already partitions two-hole subsets by separation and identifies the equal-length odd-path swap at the even antipode; substituting W for the all-isomorphism weight in that partition gives the stated parity count. For growth, the earlier crown antichain and at-most-m-component bounds are exactly the bounds needed: replace m! permutations by I_m involutive permutations, count at most 2^m internal choices, and sum over the 2^N domains instead of domain-image pairs. The standard involution estimate immediately gives the quarter coefficient and the known denominator gives the ratio. This is a finding of mechanical implication from inspected prior statements, not an assertion that the exact crown polynomial or exponent was printed elsewhere.

## value

FAIL

Self-inverse cycle type is a natural and useful statistic, but the frozen contribution does not clear the threshold for a new exact invariant: the prior exact profile formula and local involution evaluator already yield it by direct composition. The explicit corank-two coefficient reweights a preclassified boundary case, and the claimed logarithmic precision retains exactly the elementary exponent obtained by replacing factorial permutation counts with involution counts in the prior sandwich. No separate supported, nonmechanically implied crown-specific result survives these comparisons in the frozen Finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
