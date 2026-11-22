# Scientific review of the two-phase central-binomial summatory residue law

## Correctness — PASS
Lucas's digitwise congruence gives the stated exact five-digit multiplier vector, and summing complete blocks yields the affine transition on the summatory residue and current binomial residue. The proof handles leading zeros, all residue classes and all positive depths. Two forbidden digits cause absorption with probability \(2/5\) at every live digit, proving a uniform \((3/5)^r\) error after parity correction. The displayed twenty-entry rational vector satisfies the defining exact integer system, and the resulting two probability vectors are computed exactly, not estimated. The packaged Python checker reproduces the certificate and verifies direct finite cases. Risk: the proof assumes standard Lucas congruences, stated explicitly, and does not establish optimality of the error exponent.

## Originality — PASS, with historical priority risk
Sun–Tauraso's prime-power endpoint congruences, Mattarei's finite-block polynomial identity, and Chen–Hou–Zeilberger's general endpoint-summation method were compared with the actual claim. These results determine selected sums or their coefficients, but they do not report the running-sum residue-frequency law for variable endpoints or the two subsequential vectors. A published central-binomial quadratic-character classification was read fully and addresses individual coefficient characters, not cumulative sums. Broad distribution theory of Barat–Grabner was available only through its abstract and could conceivably include a more general apparatus that implies this result; no equivalent numerical specialization was found. Novelty is asserted at best knowledge, not certified historical uniqueness.

## Mathematical value — PASS
The underlying central-binomial partial sums have a longstanding modular-congruence literature. Rather than providing another endpoint congruence, this theorem identifies the failure of residue frequencies to exist at four of five classes, quantifies a persistent oscillation of order equal to the full population, and supplies the exact rational pair of competing distributions. This is a structural boundary for summatory congruences that cannot be inferred from the distribution of the summands alone. The fixed modulus is natural because its digit factors \((1,2,1,0,0)\) produce a nontrivial signed absorption mechanism.

## Scope and uncertainty
The result is restricted to residues modulo five; higher powers and other primes are not addressed. The limiting behavior of residue zero at arbitrary cutoffs is not settled. The central-binomial digit-product, endpoint congruences, and generic finite automata are not claimed as new. Full historical literature screening and independent mathematical verification remain open.

Self-review: passed. Independent audit: not yet performed.
