# Independent mathematical audit

## correctness

PASS

The greedy arch count equals the subsequence-universality index: an arch supplies each next requested symbol, and the successive arch-ending symbols followed by a missing suffix symbol give an absent pattern by earliest matching. With exactly k letters a, every one of the k arches must use one a; the only possibilities are ab and b^(h+1)a, followed by a b-only suffix, and the choices are unique. The first b in each later arch supplies one pair for each earlier a, giving binom(k,2). The extra weighted contributions are 1 for ab, (j−1)h for the extra b's in arch j, and k per suffix letter. Coefficient extraction therefore counts the exact histogram. The denominator is the usual Gaussian inversion-area polynomial and is positive throughout: for C=q(k+s)+r fill q rows of length k+s and one row of length r in the k-by-(k+s) rectangle, omitting a zero row. Reversal preserves universality and complements C. The total is 2^k times E binom(s+J,s) for J binomial(k,1/2); for fixed s the leading term is (k/2)^s/s!, including s=0. The composition count is asymptotic to 2^s 4^k/sqrt(pi k), giving the stated rarity. For k=3,s=1, direct coefficient extraction gives z^3(1+z)^2(1+z+z^2+z^3+z^4), agreeing with the stated histogram. Frozen verification.py and verification_output.txt were inspected, not rerun; the finite checks are supplementary.

## originality

FAIL

The all-slack refined polynomial for arbitrary k≥4, its symmetry and exact total are already equivalently covered by a distinct indexed result. Earlier entries cover s=1 and k=3 exactly. This is demonstrated coverage, not a historical-priority verdict: the general matching record has a later catalogue date. The Gaussian normalization, routine fixed-s asymptotics and omitted tiny k cases do not leave a distinct scientifically material remainder.

## value

FAIL

The exact weighted polynomial is a useful invariant in isolation, but its entire unbounded family is already given by an equivalent indexed formula. What remains is standard normalization, the elementary leading term of the existing total, and boundary values of k under the same factorization. These do not constitute a separate nonmechanically implied exact classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
