# Independent mathematical audit

## correctness

PASS

For OPT=k+d, any one occurrence per class in an optimum has three distinct start positions spanning at most d, so at least one adjacent start gap is at most floor(d/2). Its overlap lower-bounds the first greedy overlap (with zero also allowed). The resulting length is at most 2k+floor(d/2). Dividing by k+d gives a nonincreasing bound for d≥3: the upward numerator step at d=2j is offset by the denominator step because j≤k. At d=3 the resulting ratio is strictly below 2k/(k+2) for k≥3. For d=2 the three windows exhaust all k-factors of the host. The optimal first overlap is k−1. The binary endpoint obstruction is exact: the oriented last-letter and first-letter sets can be disjoint only if each is a singleton; doing this in both orders requires identical complementary endpoint pairs. The eight-case reduction is exhaustive because reverse-complementing the host reflects the window indices and toggles orientations, and reverse-complementing the candidate merge exchanges its ordered inputs and toggles both orientations. Independently checking the equalities, the adjacent pairs give respectively a direct overlap, a self-invariant first read reducing to that case, W₀=rc(W₂), or period two with impossible opposite endpoints. The nonadjacent pairs give respectively equal endpoints on W₁, W₁=rc(W₂), W₁=rc(W₀), or period three with h₁=h₂ while both hₖ₋₁ and hₖ must differ from h₁; at least one of those indices has residue 1 or 2. Thus every first tie leaves a positive second overlap. For sharpness 10^k1 realizes OPT=k+2, and the bad tie 01^{k−1}0 versus the remaining constant-word orbit has maximum overlap exactly one, since its endpoints are equal and its next letters have the opposite bit. The proof covers every k rather than extrapolating the finite counts.

## originality

PASS

The k=4 slice, including the same sharp triple, is explicitly covered by the distinct four-mer catalogue record. Scope-specific originality is the all-length three-class theorem and the structural k+2 obstruction, neither supplied by that census or by the inspected general half-compression or modified-greedy results. This is a bounded literature judgment and does not assert priority within the day shared by the records.

## value

PASS

The smallest nontrivial tie-sensitive instance size already exhibits a ratio approaching two. The theorem gives its exact dependence on length, explains the exceptional near-minimum host where the generic compression bound is insufficient, and does so by a structural binary obstruction plus a matching family, not by enlarging a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
