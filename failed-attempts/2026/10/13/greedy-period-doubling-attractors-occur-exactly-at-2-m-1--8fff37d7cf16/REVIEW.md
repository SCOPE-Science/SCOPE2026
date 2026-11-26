# Independent mathematical audit

## correctness

PASS

The prefix-window induction is valid: for length 2^m through 2^(m+1)−1 the word is P_m followed by a prefix of H_m. Occurrences avoiding position 2^m−1 are represented in the leading H_m, which is attracted by the previous positions. For the forcing direction an occurrence of P_r with r≥1 begins 10, so it is aligned at an even index and desubstitutes to one of the positions at the preceding level; the three starts at r=0 are 0,2,3. In the next complete prefix only the occurrence at 3·2^(k−2) has the correct predecessor for the forcing factor, whose start exceeds every previously chosen point. The length-one and length-two cases start the induction. A least-failing endpoint repairs all newly unhit factors, as each must be a suffix of that prefix. Linear recurrence follows also from primitivity of the substitution, and the optimum and ratio follow from the cited published prefix theorem. Independent check `python3 /workspace/branches/independent_examples.py 2` reproduced the first 128 symbols' greedy selections from the independent one-based v2-parity word formula; this finite replay is not the proof.

## originality

FAIL

A distinct indexed Resultary finding states the identical fixed point, greedy rule, exact positions, prefix count, optimum and logarithmic separation. The alternative forcing suffix is a proof device and not a distinct substantive conclusion. This is mathematical coverage, not a claim of dependence or of a particular historical derivation.

## value

PASS

The objective is scientifically motivated: an exact logarithmic separation on a canonical linearly recurrent automatic word demonstrates tight greedy behavior even with a constant optimum. That fact is substantive, but this record does not contribute a distinct instance or result beyond the identified coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
