# Independent mathematical audit

## correctness

PASS

The leftmost greedy embedding bijects distinct outputs with canonical deletion pairs: a skipped block before a retained letter cannot contain that letter, and trailing deletions are unrestricted. The explicit pair cases in the proof give B=1+M(M+1)/2-T_m+sum(A_i-C_i). An invertible uniform increment representation gives independent Bernoulli(p) transition indicators T_i. Independently, conditional on T, each return indicator C_i on an adjacent nonzero pair has probability r=h/p, and the active return tests are jointly independent: any selected tests form a union of paths and each constraint fixes one additional independent nonzero increment. The conditional variance averages to (m-1)h(p-h). In the conditional mean, the orthogonal terms in T_i-p have common linear coefficient (m-1)p and quadratic coefficients 1-1/p on adjacent pairs and 1 otherwise. Adding their squared contributions to the expected conditional variance yields the displayed bracket. The conditional mean or the source identity gives the claimed expectation; for n=2 both moments reduce to mean 1 and variance 0, and the leading variance term is p^3 h n^3. An independent exact replay counted distinct retained tuples and verified the rational moments for all 13,652 words in its bounded ranges, without relying on the deterministic identity: /workspace/replay_two_deletion_moments.py and /workspace/replay_two_deletion_moments.txt. This check is supplementary to the all-q, all-n argument. The separate frozen checker and check_output.txt were inspected as evidence, not executed. The stated theorem concerns a single uniform word, not intersections or nonuniform sources.

## originality

FAIL

A distinct inspected catalogue result gives the identical all-alphabet expectation and variance under the same model, and adds a growing-alphabet Poisson limit; other distinct catalogue results report exact distributional refinements. The October 25 label for the closest match is later than the frozen label; these comparisons establish equivalent mathematical coverage, not earlier publication, dependence or provenance. The binary precedent alone would not cover the nonbinary result. The cited distinct-subsequence arXiv identifier also needs correction from 1704.08643 to 1704.08661, but that is not the reason for the failed verdict.

## value

FAIL

Quantifying fluctuations in the size of a random two-deletion ambiguity set is naturally motivated; an unknown exact nonbinary variance would be a useful addition. This submission offers neither a new observable nor a stronger law after the exact same moment formula and distributional refinements are accounted for. The binary specialization, leading coefficient and standard-deviation formula are direct consequences, not a distinct valuable remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
