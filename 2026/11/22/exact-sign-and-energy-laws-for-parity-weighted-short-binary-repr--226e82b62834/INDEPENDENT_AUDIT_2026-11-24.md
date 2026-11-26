# Independent mathematical audit

## correctness

PASS

The least-significant-digit split preserves the forbidden leading pair for m≥1 in the odd recurrence and reverses parity on the −1 branch. The exceptional short strings at 1 and 2 each contribute +1; the recurrence is not applied at odd n=1. The resulting (a,b)→(a,a−b),(a−b,b) transitions preserve the eight reachable state classes from (1,1). Solving their count equations gives (1−z)/(1−2z) for positive words with z counting digits after the leading 1, which sums to 2^(L−1) through length L. The zero class series z/(1−z−z²) yields F_(L+1)−1 positive zero indices below 2^L; subtraction gives the stated negative count. At the moment boundaries g(1)=g(2)=g(2^L)=1. The adjacent-product recurrence telescopes the difference g(m)²−g(m+1)² to zero across m=1,…,2^L−1, leaving T_L=1. The first sum adds 1 each level and the second satisfies S_(L+1)=3S_L−1 with S_1=1. Variance follows by normalization. The squared total grows as 3^L; the per-integer second moment instead decays as (3/4)^L. If limiting density is taken at arbitrary cutoffs, the automaton also proves it: the closed four N/R states form an aperiodic irreducible class with equal total stationary mass on each sign, all other states are transient, and the uniform suffix transition converges exponentially from every state. Partitioning [0,X) into aligned binary-prefix blocks of distinct sizes sums the exponentially sublinear block errors to o(X), proving natural densities without claiming exact half-count at arbitrary cutoffs.

## originality

PASS

The dyadic positive-sign census and evaluated energy law for the known recurrence are supported as distinct to the best of current knowledge. The recurrence, short-representation definition, unweighted count and zero-language result are prior. The first moment follows by a short telescoping identity and is not the principal novelty on its own.

## value

PASS

Parity-weighted counts are a natural signed evaluation on a standard representation system, and powers of two are the canonical complete levels of its binary recursion. Knowing which values vanish did not determine the split of the remaining signs or the sharp scale of their magnitudes. The exact positive census and second moment resolve distinct parts of that distribution; the first moment gives the contrasting scale of net cancellation. Neither the seed values nor the Fibonacci zero count alone supplies this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
