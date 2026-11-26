# Independent mathematical audit

## correctness

PASS

The Finding is correct by reconstruction; the frozen proof has a false intermediate congruence at RESULT.md:27. Both children are congruent modulo four to (1+2n)T_n, not to T_n in general (T_2=T_3=3 while T_1=1). This is immediate from the preceding exact recurrences and oddness; it still implies T_{n-1}=T_n mod 4 for odd n, which is the only needed step. For the recurrences, put Q=P(z^2) and use P^2=Q+2P; the even Laurent parts of P, P^2, P^3 are respectively 1, Q+2, 3Q+4. Truncating the binomial expansions at two factors of 2P gives both stated recurrences, with the n=0 case direct. The corrected sibling equality gives the stated mod-eight transitions. Independently replayed exact finite checks confirm the 24-state communication, stationary weights, annihilator identity on every basis state, and three count anchors. The simple Perron eigenvalue and the remaining nonzero simple roots of modulus at most sqrt(2), with nilpotents at zero killed after three steps, yield O(sqrt(N)) after dyadic block decomposition. Eighth powers of the nonzero roots are 256,16,1; the three anchors uniquely force the claimed marginal count for all m>=1, and at least one of four joint discrepancies is at least sqrt(N)/8 infinitely often. Replay: python3 /workspace/review_replay.py 1. This independently verifies the finite prerequisites, not by testing an infinite set of N. No source checker was executed.

## originality

FAIL

A distinct Resultary finding demonstrably covers the same main theorem, including simultaneous square-root discrepancy and optimality. This is a comparison of statements, not a claim of chronological priority. The additional selected dyadic marginal count is not stated there verbatim, but follows by direct Walsh evaluation from the same digit transfer already written there; it does not distinguish the original finding or supply a substantial remainder to repair.

## value

PASS

As mathematics, the full joint law and optimal all-prefix exponent are useful explicit correlation and discrepancy information not supplied by uniform marginals. This does not make the covered result original. Once the joint law is removed there is no worthwhile repair based solely on the direct Walsh specialization at r divisible by eight.

The dated certificate retains the supplied scientific assessment, sources and limitations.
