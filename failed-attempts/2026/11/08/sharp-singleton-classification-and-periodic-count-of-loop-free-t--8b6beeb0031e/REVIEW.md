# Independent mathematical audit

## correctness

PASS

For labeled cyclic 3-letter words with no equal neighbors, balance forces p_i-m_i=t. For zero circulation, the one-reciprocal-pair and path-of-two-reciprocal-pairs cases reduce to alternating cycles and binary excursion necklaces; for nonzero circulation, the single reverse-pair case similarly reduces to two excursion types. Three-pair or multiple-reverse-pair profiles admit nonconjugate Euler tours. These establish the all-length h/u/t criterion. Direct expansion of five rational GF pieces yields coefficients (n=2..12) 3,2,6,6,11,6,15,8,9,12,11; source verify.py tests all loop-free words to n=10 and balanced directed profiles to n=29. Finite tests corroborate, not replace, the constructive classification.

## originality

FAIL

FAIL: the complete prior 2026-11-02 ternary cyclic Markov-profile classification covers ALL labeled ternary directed two-gram histograms including self-loops. Restricting its five support cases to zero self-loops exactly gives this theorem’s t=0 and t!=0 singleton criteria and rational enumerator. Its earlier published theorem is stronger on the same object and equivalence relation, not merely a similar title or count; even a distinct elementary proof does not make the final claim original.

## value

PASS

A full classification of exact cyclic reconstruction from directed digram frequencies on the natural loop-free ternary subclass has a clear information-theoretic motivation; its finite necklace-transition boundaries and periodic census are independently useful mathematically even though previously covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
