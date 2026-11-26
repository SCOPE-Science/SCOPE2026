# Independent mathematical audit

## correctness

PASS

There is an independent direct proof of the balancing step: put v_d=[(m−1)d+c]_p and e_d=[md+c]_p. The carry bit 1_{v_d+d≥p} equals (v_d+d−e_d)/p and is the indicator of e_d<d. Both v_d and e_d are permutations of the residues by the two hypotheses on m, so summing this bit over d gives (p−1)/2, for any integer carry c. Lucas's test then gives exactly (p+1)/2 possible next digits from each state. Prescribed lower digits are unaffected by an extension, hence an illegal suffix remains illegal. A finite word's high zero digits never violate Lucas even if its carry has not ended; this also treats the zero-length endpoints. The closure is exactly the infinite legal tree since every finite legal prefix extends by zeros. There are a_p^r occupied cylinders at level r, each of mass a_p⁻ʳ under the consistent uniform branch measure. Covering bounds, the mass distribution principle and a_p<p give the two dimensions, Ahlfors regularity and Haar-nullness. Bounding arbitrary X between consecutive powers of p proves the stated Θ bound uniformly in the eligible m. If p|m the first nonzero digit fails the test, while m=p+1 makes all p one-digit indices pass. The frozen finite verifier was inspected, not executed; it is not needed for any universal step.

## originality

PASS

The m=2 specialization is covered: the classical central-binomial digit restriction already mechanically gives those exact counts, and a catalogue index–value result covers the same admissible suffixes. The supported distinct content is the universal affine carry-state balance for every nonexceptional slope, and its resulting exact arbitrary-suffix law. General row/spatial counts and path-set dimension theory do not calculate these carry-state row sums. Known consequences of the branching mechanism, such as the dimensional formula once that mechanism is known, are not separate originality claims.

## value

PASS

The index support of proportional binomial coefficients is a natural arithmetic set. Exact constant branching despite carry-dependent digit sets gives directly usable counts with an arbitrary prescribed low-digit suffix and a canonical regular measure, rather than only a density or dimensional bound. Its universality contrasts with the nearby exceptional slopes, and the proof exposes a structural balancing mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
