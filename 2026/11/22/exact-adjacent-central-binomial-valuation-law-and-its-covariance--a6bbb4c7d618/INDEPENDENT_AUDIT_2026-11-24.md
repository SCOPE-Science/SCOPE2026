# Independent mathematical audit

## correctness

PASS

The digit update for the three carries (doubling n, incrementing n, doubling n+1), split at a=m−1,m,2m for p=2m+1 and with separate incoming states, gives the stated weighted rows on the five reachable states. If a terminal increment remains, the terminal state is A or B and the doubling carry for n+1 is zero, so the additional leading 1 contributes no weight even at p=3. The other leading-zero cases also add no carry. The recurrence B_(n+1)/B_n=2(2n+1)/(n+1) expresses the jump as a difference of valuations on disjoint residue classes. There are exactly (p−1)p^(k−j−1) representatives on each signed level j<k and exactly one on each signed level k; p≥3 prevents higher levels. The one-carry expectations and covariances follow from the Bernoulli chain with conditional-expectation contraction 1/p. Summing gives the stated mean and W_k−W_(k−1)=(p+1)(1−p^(−k))²/[4(p−1)], hence the closed W_k. The endpoints have equal zero valuation, so equal marginals and the jump tail give K_k=W_k−∑(2j−1)p^(−j). For k≥1 the increase in W strictly exceeds (2k+1)p^(−k−1): lower and upper bounds are 32/81 versus 1/3 at p=3 and 144/625 versus 3/25 at p≥5. The k=1 sign, K_(3,2)=−4/81 and K_(3,3)=167/729 then establish the phase. The infinite jump correction (p+1)/(p−1)² and W_k's linear coefficient give the Pearson expansion. An independently written integer/rational reproduction, `python /workspace/branches/audit_arithmetic_reproduction.py 3`, matched joint counts, jumps and moments on eight prime-depth pairs including both negative cases and the sign transition. Submitted verification code was inspected, not executed; finite checks do not establish the unrestricted statement.

## originality

PASS

The known one-index Kummer valuation and elementary coefficient recurrence are not counted as new. The checked sources do not state or mechanically supply the complete finite-block pair distribution for adjacent central coefficients across odd primes, nor its exact covariance sign phase.

## value

PASS

The pair is the natural unit shift of a classical valuation word, and its ordered joint counts are not recovered from the known single-index histogram. The law isolates a bounded jump discrepancy even as the variance grows, and exhibits an exact finite-depth change of covariance sign with two exceptional blocks. Those are usable structural invariants beyond the routine carry formula or a claim of asymptotic correlation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
