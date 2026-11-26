# Independent mathematical audit

## correctness

PASS

Every allowable word has a terminal descendant in the finite prefix order; incomparable words have disjoint descendant sets, so choosing one leaf for each injects any code into the set of all leaves. For m≤N/2 a palindrome can be doubled and is never a leaf. For m>N/2 an extension by t≤N−m must have its original palindrome as both prefix and suffix and hence must overlap consistently at offset t. Conversely, gluing two copies with this overlap gives a unique compatible word; reversal interchanges the covering copies and fixes the word. Thus the exclusions are precisely periods 1 through N−m. The connected components of the reflected/shifted position graph are the exact equality classes for simultaneous periods, so inclusion–exclusion gives the count including N=1. For each period t, reflection on residue classes has at most two fixed points and hence at most floor(t/2)+1 orbits. Summing the resulting geometric upper bound for exclusions over t and m costs O_q(h q^(h/2+1)). Summing all candidate palindrome counts q^ceil(m/2) gives the displayed leading constants, including the unpaired final layer for odd N. Independent `python3 /workspace/reproduce_reviews.py` deletes word-prefix ancestors directly and compares to graph counting through N=18,11,9 for q=2,3,4 respectively. Its finite agreement is supplementary; the suffix-overlap equivalence and group count prove the arbitrary-N result.

## originality

PASS

The distinct claim is the all-q,N exact period-exclusion count and its sharp parity gains for cardinality under a maximum length, not the already known bidirectionally decodable palindrome constraint, prefix tree, or feasibility of prescribed lengths. The strongest available comparisons either use prescribed lengths and an average-length-style optimization or impose genuinely different combinatorial constraints. A generic existence algorithm might be iterated to compute particular finite optima, but does not supply this exact expression or asymptotic.

## value

PASS

With a hard maximum decoding length this gives the entire allowable noiseless dictionary size and a canonical maximizing codebook, as well as actual sharp relative gains versus using only the maximum length (binary four versus three). The result uses the overlap structure of palindromes and is not a Kraft-bound restatement. It does not promise efficient arbitrary-size computation, unique optimal codes, or noise correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
