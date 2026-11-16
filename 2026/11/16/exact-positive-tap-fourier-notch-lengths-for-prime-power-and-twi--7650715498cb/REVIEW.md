# Self-review

## Correctness — PASS

The proof reduces primitive-character nulling to cyclotomic polynomial divisibility; monic substitution admits a residue-by-residue decomposition. For prime powers the last residue forces an entire \(p\)-coefficient block. For \(2^sp^k\), reduction modulo \(Y^p+1\) makes two adjacent positive coefficients contradict the required alternating cyclotomic pattern below degree \(2p-2\). The explicit construction is positive at every tap and divisible by the target polynomial; geometric-sum multiplication fills every greater length. Exact SymPy construction tests on 20 periods and a separate LP boundary stress test on nine periods corroborate the argument. No untested computational extrapolation is part of the proof.

## Originality — PASS relative to checked evidence

Tan–Zhang (2026) and Steinberger (2012) solve the nonnegative-multiple optimization that permits sparse zeros. Their statements do not impose strict positivity at every intermediate exponent or yield the new length formula as a stated result. Reddy (2011) concerns sparse binary multiples. Brunotte's 2012 and 2013 works explicitly study positive multiples of real factors; the quadratic base cases may already be covered, but accessible abstracts do not identify this full mixed-prime-power length theorem. The complete Brunotte texts were inaccessible through available institutional access; exact priority cannot be certified. No comparable claim was identified among indexed harmonic-analysis and cyclotomic results, including the narrower dyadic-antipodal rigidity theorem. Search absence alone is not a proof of originality.

## Value — PASS

Exact primitive-mode rejection with no zero taps is a natural dense positive FIR design constraint distinct from unconstrained sparse positive measures. The theorem gives all feasible lengths for two infinite arithmetic families, explains their sharp arithmetic discontinuity, and provides reproducible positive-integer constructions of every allowed length. It is not a single numerical example or a restatement of the sparse diameter theorem.

## Closest literature and limits

The main closest direct prior article is Tan–Zhang, arXiv:2609.07646, which is about nonnegative and possibly sparse multiples. Steinberger provides an earlier two-prime nonnegative decomposition. Brunotte's positive-multiple methods represent a bibliographic risk (complete texts inaccessible). Scope excludes periods with two different odd prime divisors, coefficient-range optimization, and robustness optimization.

Self-review: passed. Independent audit: not yet performed.
