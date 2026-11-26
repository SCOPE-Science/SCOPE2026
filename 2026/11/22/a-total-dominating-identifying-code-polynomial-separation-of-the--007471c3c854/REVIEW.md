# Independent mathematical audit

## correctness

PASS

Verified the joint definition: every open-neighborhood witness must meet the chosen set, and every symmetric difference of distinct closed neighborhoods must meet it. The first condition already makes all closed signatures nonempty. Independently built each graph from translates of its generator set in Z₄² and used a Boolean subset-zeta transform to propagate failure from each witness to all complements containing it. This covers all 65,536 labeled choices per graph, including the empty set. The length-17 coefficient vectors, sums 42375 and 42459, and both full membership-bitmap hashes matched the frozen values. I checked the strongly regular common-neighbor counts and that the 64 size-six witnesses are distinct and pairwise differ in at least four positions, so their ten-vertex complements share no nine-subset. This independently explains the identical tail: all size at least 11 sets count, there are binom(16,10)−64 valid ten-sets and binom(16,9)−640 valid nine-sets. The two minima are 6; the labeled-count difference is exactly 16z⁶−64z⁷−36z⁸. The frozen scripts were inspected, not executed.

## originality

PASS

The joint code class is already known (including under the alias differentiating-total dominating set), as are related invariant values for this graph pair. The supported distinct claim is the exact joint cardinality distribution and where it distinguishes this pair. Prior minimum-size theorems, minimum ordinary-code counts, and separate total- or paired-domination distributions do not supply this joint census.

## value

PASS

The Shrikhande and 4×4 rook graphs are a natural strongly regular comparison pair with the same parameters and known identical pure total-domination distributions. The established joint code class detects a difference where even its minimum size does not, with reversed order between size six and sizes seven/eight and exact equality above them. That profile is a meaningful precise benchmark for separation criteria and stronger than exhibiting a single numerical distinction. The witness geometry accounts for the common tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
