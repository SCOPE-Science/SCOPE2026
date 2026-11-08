# Review: near-uniform cyclic moment classes

## Correctness

**PASS.** The marking map has exactly three preimages per indexed word, independently of rotational symmetry, since each word contains three distinct marked positions. The checksum identity \(S\equiv3i+2a+b\pmod n\) follows directly. The bijective case of multiplication by three proves uniformity. In the divisible case, three solutions of the starting-position congruence cancel the three markings, and the cube-root generating function gives the \(1,0,0\) Fourier coefficient at each degree divisible by three. These steps verify all quantifiers and the degenerate \(n=3h\) boundary. The actual extracted `verify.py` directly enumerates all admissible triples through \(n=42\) and passes 247 parameter pairs. Finite enumeration does not substitute for the proof.

## Originality

**PASS within searched evidence, with residual historical risk.** Cheng–Ferreira–Broere (2010) establishes first-order moment-balancing methods for run-length-constrained sequences, not exact indexed circular weight-three checksum populations. Kulkarni–Kiyavash (2012) gives deletion-code bounds rather than the exact vector of checksum-bucket sizes. Chan (2018) treats unrestricted modular subset sums; the unrestricted \(h=1\) boundary is deliberately excluded from the novelty claim. The equivalent independent-set language was searched alongside cyclic checksum and run-length-limited language. Relevant prior work on circular three-marker *palindromic complexity* counts another invariant and cannot imply this formula. Query and source comparisons found no known theorem subsuming this constraint-dependent expression, but incompletely indexed older cycle subset-sum literature may exist.

## Value

**PASS.** First-order moment syndromes are a standard tool for constrained code design. The smallest nontrivial cyclic sparse family with three marked sites and a genuine minimum run length has a non-obvious arithmetic transition at divisibility by three; the theorem shows all \(n\) buckets are as balanced as integers permit, at every feasible length and spacing parameter. It is an exact infinite-family structural result, not a table or an arbitrary unmotivated small slice. The limited coding consequence is an exact balanced partition count; no error-correction promise is inferred.

## Closest literature and limitations

Cheng, Ferreira and Broere, DOI 10.1109/ISIT.2010.5513415, full author text examined; Kulkarni and Kiyavash, arXiv:1211.3128, run-length-limited code-size discussion examined; Chan, arXiv:1802.03507, unrestricted cyclic subset-sum formulation examined. The proof assumes exactly three ones, circular uniform minimum gap and checksum modulus \(n\). Independent specialist priority verification remains desirable.

Self-review: passed. Independent audit: not yet performed.
