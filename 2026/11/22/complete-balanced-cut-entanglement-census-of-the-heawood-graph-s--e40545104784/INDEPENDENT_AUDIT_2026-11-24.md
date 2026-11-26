# Independent mathematical audit

## correctness

PASS

The frozen marginal, mean, composition table and crossing-edge refinement are numerically correct. I constructed the Fano graph from cyclic difference set {0,1,3}, traversed all 3432 labeled seven-subsets, and computed each binary rank from the size of the XOR span of the cut rows. Results include rank counts (100,980,1680,672) and exactly 336 rank-seven cuts at each of 11 and 13 crossing edges. The repaired contribution is the conditional edge profile, with a separate analytic proof. Character orthogonality yields a flat reduced spectrum of rank 2^r. Fano incidence rank four forces block sizes 3 and 4 for r=7; the four-block factors through the four augmented coordinates and is invertible exactly when the two complementary triples are bases. For any of the 28 point bases, 72 of the 168 ordered line bases pass det(N+J)≠0, by uniformity of N^−1 times the all-ones vector and its three even-weight values. Since both N and N+J are invertible, their row weights exclude total incidence counts other than 4 or 5, and complementation exchanges them. This leaves 6 unordered line bases per point basis per case; total cross edges are 3+2e. Hence there are 168 unordered cuts per edge count, or 336 oriented. At the all-edge cut the incidence rank is four. These checks support exactly the repaired finite theorem.

## originality

PASS

Applied to the repaired edge profile only. The original marginal cannot be treated as distinct from the associated same-day qudit record: although that Finding targets odd primes, the complete Smith table mechanically recovers the binary marginal and the companion source asserts it explicitly. That record treats the binary marginal as prior, so this overlap is not evidence that the same-day qudit record appeared first. The repair credits the overlap, makes no within-day priority inference, and retains the joint count of crossing edges within the binary rank-seven class, now with an analytic proof. None of the examined comparisons gives or mechanically determines that joint count.

## value

PASS

The surviving result answers how many preparation edges can cross a balanced cut once maximal entanglement is imposed, for a canonical incidence graph. The complete two-class answer and short Fano-basis mechanism expose why the largest edge boundary need not be the best entanglement partition. It is a distinct and useful finite statistic, not a recomputation of the associated marginal histogram or a claim about practical gate cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
