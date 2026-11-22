# Scientific review

## Correctness — PASS

The error model explicitly allows zero or one downward flip, and all received words remain in the source. For distinct inputs the coordinatewise intersection is a common received word if and only if the two one-sided support differences are each at most one. This gives an exact compatibility graph. Complete Bron–Kerbosch maximal-clique enumeration over all 34 length-seven words proves that the maximum size is eight, with exactly ten optima and no omitted larger cliques. A separate C++ bitmask implementation confirms these finite results. Exact rational primal/dual shadow-packing certificates, checked against every constraint for every length one through seven, prove the fractional values, including nine at length seven. The complete all-length limitation is explicit: only lengths one to seven are claimed. Risk: the computational exhaustiveness rests on the correctness of two executable search implementations, not formal proof-assistant certification.

## Originality — PASS, qualified

The 1965 asymmetric-error coding work is for the unrestricted binary alphabet, while the present classification restricts to the Fibonacci source. The 2011 Fibonacci-cube 2-packing census is a Hamming graph-distance problem, which forbids additional pairs and has value six at length seven, not eight. The 2012 Fibonacci cube work addresses maximal induced subcubes. The 2015 Fibonacci perfect-code work addresses two-sided Hamming neighborhoods. An indexed result for Fibonacci-constrained single-deletion codes uses length-shortening rather than one downward bit flip. Full-text comparisons did not imply the exact current integer/fractional pair or equality classification. Risk: an unindexed earlier finite case or inaccessible specialised code table might cover the result; no uniqueness proof of historical priority is claimed.

## Mathematical value — PASS

The Fibonacci constraint is standard in graph models and forbidden-adjacency constrained coding, and the Z-channel is a classical asymmetric-error channel. Their interaction produces a natural output-shadow packing LP. The first strict gap is stronger than a merely fractional objective: the LP optimum is the integer nine while the true capacity is eight. The ten-optimum census and common six-word core give rigidity information beyond an isolated number. The fact is finite and does not promise an asymptotic theorem or all-length capacity.

Self-review: passed. Independent audit: not yet performed.
