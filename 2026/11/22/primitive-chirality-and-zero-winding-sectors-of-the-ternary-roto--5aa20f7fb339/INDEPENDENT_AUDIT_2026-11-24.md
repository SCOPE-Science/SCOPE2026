# Independent mathematical audit

## correctness

PASS

The transfer matrix J−I has eigenvalues 2,−1,−1; inversion over least periods followed by division by n gives T_n. Choosing the initial symbol and the indexed steps determines the walk. An integer sum zero, rather than merely zero modulo 3, gives the factor 3 times the central binomial coefficient, and repetition multiplies this sum, so inversion in the zero sector is legitimate. For a specified reflection i↦−i, passing to any divisor period preserves the reflection; odd divisor periods have a swapped adjacent pair (or the impossible length-one loop). At even period d, the vertex axis fixes 3·2^{d/2} words, by the half-path count. Edge axes fix none. The fixed-point sets of distinct axes are disjoint on primitive indexed words since two axes compose to a nonidentity rotation. Counting over n/2 vertex axes and dividing by n gives A_n, including n=2 where the vertex reflection acts as the identity on positions. Reversal negates the sum, so the achiral census is contained in the zero sector. Exact substitution at n=2,4,6,8 gives (3,3,3),(3,3,3),(9,9,9),(30,24,18). Proper divisors are ≤n/2, making the lower terms exponentially smaller than the leading binomial and 2^{n/2} terms. Stirling gives the claimed constant and decay along even n. Independent n≤12 enumeration confirms the counts without proving the all-length statements.

## originality

PASS

Total proper-cycle coloring and period inversion are classical. In particular the zero-winding count is an exact translation of the balanced binary primitive necklace count, not a new standalone enumeration. The supported distinct part is the joint comparison with literal reversal in the proper ternary shift, including the first nonempty chiral zero sector and its asymptotic dominance. Neither the rotor grammar nor the unrestricted symmetric-bracelet comparison supplies that combined proper-coloring result on the statements inspected.

## value

PASS

A closed symbolic walk can have zero net orientation either by retracing under an orbit symmetry or without any reversal symmetry. Distinguishing these two natural properties is useful in the abstract no-repeat surrogate: the theorem identifies the exact first counterexamples and shows the nonsymmetric part is asymptotically typical, rather than offering only an instance. The value is confined to the combinatorial grammar, not claimed as a result about real rotor trajectories.

The dated certificate retains the supplied scientific assessment, sources and limitations.
