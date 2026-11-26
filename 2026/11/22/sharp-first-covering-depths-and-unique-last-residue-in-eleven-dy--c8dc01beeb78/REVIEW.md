# Independent mathematical audit

## correctness

PASS

The Stern recurrence gives S(2n)=(a,a+b), S(2n+1)=(a+b,b) for S(n)=(a,b). Each move is invertible modulo 2^k and preserves the condition that at least one coordinate is odd. The start (0,1) is fixed by the zero move, so fixed-length binary words with leading zeros give exactly the stipulated half-open prefix, and the first distance and least numerical index are correctly identified by breadth-first order and binary tie order. Independently computed via a synchronous predecessor recurrence: at each pair (a,b), take the minimum of twice the previous least index at (a,b-a) and twice that at (a-b,b) plus one, with infinity marking absence. This is exact by splitting indices into even and odd. The whole primitive grid was counted and the complete distance histograms, extreme layers and least indices agreed for all eleven k. The radii are (2,5,8,11,14,18,20,23,26,30,33); each final layer has size one, with (1,0) at k=1 and (-1,-1) thereafter. In particular the last index at k=11 is 4,920,978,067, between 2^32 and 2^33.

## originality

PASS

The ordered pair graph and its eventual coverage are known. The extra claim is the exact rooted out-eccentricity, last-layer uniqueness and earliest binary index at every exponent in the stated range. The closest inspected exact and asymptotic results do not give this combined statement or imply the finite values without an additional exhaustive calculation.

## value

PASS

For a canonical integer sequence and a natural family of nested moduli, the rooted depth is exactly the minimum binary index budget needed to realize all allowed consecutive residues. The census resolves the sharp cutoffs, identifies the obstruction and its exact occurrence, and reaches far enough to exhibit two four-step increases rather than giving only tiny examples of eventual coverage. These are useful finite benchmarks distinct from a new asymptotic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
