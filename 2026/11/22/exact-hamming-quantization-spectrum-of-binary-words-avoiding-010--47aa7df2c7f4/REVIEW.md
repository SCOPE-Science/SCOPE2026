# Independent mathematical audit

## correctness

PASS

An original 010 can overlap another only at shift two; the runs of overlaps therefore form paths, whose disjoint packing numbers are the ceilings of half their numbers of occurrences. Any correction must hit every disjoint occurrence. Pair consecutive occurrences in each run and flip their shared zero; for an unpaired final occurrence flip its middle one. Flips are nonadjacent. A shared zero turned to one has unchanged adjacent ones and cannot center a new 010; a middle one turned to zero has unchanged adjacent zeros and cannot be an endpoint of a new 010. Thus every original occurrence is destroyed and no new one is created, proving Hamming distance equals maximum disjoint packing. Earliest-ending intervals give a maximum packing; the scan must reset to the empty prefix at a hit. For the three states empty, 0 and 01, the continuation series A,B,C obey A=1+z(A+B), B=1+z(B+C), C=1+z(1+u)A. Solving gives the stated rational function for A. The word (010)^k with any suffix of length below three attains the obvious packing limit k=⌊n/3⌋. Expanding in u gives [u^k]A=z^{3k}(1+z²)/(1−2z+z²−z³)^{k+1}; the first three coefficients after removing z^{3k} are exactly 1, 2k+2 and 2k²+5k+4, including k=0. At z=t/2 the u-derivatives at one are t³/[8(1−t)²(1+t²/4)] and t⁶/[32(1−t)³(1+t²/4)²]. The poles at ±2i contribute only exponentially decaying terms times polynomials in n. The principal parts at t=1 give mean n/10−4/25+o(1), second factorial moment n²/100−37n/500+O(1), and variance 29n/500+O(1). Chebyshev gives convergence of D_n/n. An independent exhaustive check through n=9 directly minimized the mismatch count over all avoiding words for each input and checked each distance, optimum flip construction, histogram and deep-hole count; this finite check is corroboration only.

## originality

PASS

The supported distinct claim is the exact distance-to-language characterization and safe optimal repair for 010, together with the resulting quantization distribution as an application. The unmarked avoidance series is already indexed, and the same marked enumerator as a distribution of greedy disjoint hits is determined by the known first-hit/avoidance law and renewal decomposition. The algebra and asymptotic constants should not be credited as an independent new theorem about occurrence processes. The inspected sources do not prove the Hamming repair identity.

## value

PASS

For this short bordered mixed constraint, a lower bound by disjoint violations does not automatically give an avoiding repair because a substitution can create a new violation. The exact matching edit construction is a useful structural result: it gives an optimal linear-time quantizer and turns known pattern enumeration into an exact test case for constrained-code quantization, including the separation of typical cost 1/10 from worst cost 1/3. The pass is not based on recomputing known occurrence polynomials.

The dated certificate retains the supplied scientific assessment, sources and limitations.
