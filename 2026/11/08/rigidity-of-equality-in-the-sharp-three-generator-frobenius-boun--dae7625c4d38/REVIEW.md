# Independent mathematical audit

## correctness

PASS

Kneser's inequality forces k{0,a,b} to fill Z/cZ if the stabilizer is trivial; if it is nontrivial, the generating set reaches every vertex in the quotient in at most c/|H|-1 steps and periodicity lifts this to the same conclusion. The Apéry minimum in an equality residue is kb-1; its at-most-k-coin representative is at least kb-1, at most kb, and congruent to kb-1, forcing that exact coin value. The deficit identity then forces one copy of a, k-1 of b and b=a+1. For 2≤a<k the proposed gap is at least a(a-1) for either parity and thus is already in <a,a+1> (its quotient on division by a is at least its remainder). For odd c, the remaining a≥k give quotient k-1 and remainder a-k≤k-3; for even c, a≥k+1 gives quotient k-1 and remainder a-k-1≤k-3. The case a=1 gives equality exactly at b=2 and even c by the stated F=-1 convention. For a=k and c=2k, the candidate k²-k-1 is a gap modulo k: at least k-1 copies of k+1 would be needed and already exceed the candidate. The sharp upper bound makes that gap maximal. Independently, `python3 /workspace/branches/independent_math_replay.py 5` verified 14,665 triples through c=48 by direct integer reachability, finding 46 equalities and certifying the upper tail with c consecutive representable values per triple. This is finite corroboration only.

## originality

PASS

The bound and nonunit equality family are prior. The distinct assertion is the complete equality locus, including the necessity of consecutive smaller generators and the exclusion of odd c. Neither the sharpness construction nor the older fixed-largest-generator extremal theorem supplies those restrictions.

## value

PASS

A sharp general inequality with a known attaining family leaves a natural inverse question. The classification shows that no odd largest generator attains the bound and that with even largest generator there is exactly one nonunit triple, beyond the elementary generator-one convention case. This is structural information about sharpness rather than another construction or tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
