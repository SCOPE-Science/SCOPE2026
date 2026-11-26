# Independent mathematical audit

## correctness

PASS

The completed repair replaces the unordered set in the frozen boxed sum by three indexed gaps, preserving their multiplicities. Literally summing over the set {a,b,c} was false when gaps coincide: (2,2,2) gives Phi=3 but the literal display gives 2; the frozen proof already used the three separate contributions. The corrected formula agrees with that proof and preserves all other claims. A one-bearing factor has at most two alignments, so only 1 qualifies; the three zero runs and strict cutoff give the sharp endpoints with the stated witnesses including N=0 and N=1. The discrete sign test perturbs the continuous root by at most 3/N and discretization adds at most one grid cell. The uniform compositions converge to simplex area. Independently, taking the maximum over subsets in the root test gives 1-3t <= x_i <= 2t and t >= 1/4; area after translation and exclusion of disjoint caps gives the exact CDF, with the jump at 1/4 and no other jump. This derivation is in the repaired result. Reproduction: python3 /workspace/branches/reproductions/combinatorics.py verified 2925 literal words, the cutoff and extrema, and exact rational integration giving mass 1, mean 187/576, second moment 1499/13824 and variance 1007/331776. Weak convergence on a common bounded interval gives moment convergence. The reproduction does not prove the asymptotic step or describe other marker weights.

## originality

PASS

For the repaired indexed-gap statement, the scope and random statistic are the same as the intended frozen result. Prior sources establish either a coarser unrestricted bound or distinguishable fixed-marker observables. The sharp weight-two endpoints together with the mixed limiting law are supported as a distinct scoped claim on the available evidence.

## value

PASS

The predicate arises from the selection of precomputed frequency counts in text indexing. On a natural fixed-content source the exact sharp bounds and full limiting law characterize typical as well as extremal demand. The positive mass at the lower endpoint and two density pieces are new structure beyond a trivial finite test or the linear worst-case bound. Indexing the equal-sized gaps correctly is necessary to state the finite theorem, not an added research claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
