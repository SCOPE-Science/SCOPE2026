# Independent mathematical audit

## correctness

PASS

For M=[[6,−1],[1,0]], M³ is [[204,−35],[35,−6]]=−I modulo 5. Fifth powering inductively gives M^(3·5^r)=−I+5^(r+1)A_r with A_r integral. For the five offsets j=0,…,4, the even power eliminates the sign, the quadratic errors vanish modulo 5^(r+2) even for r=0, and the linear term disappears on summation since ∑j=10. Thus each 3·5^(r+1) block is five times the preceding block modulo 5^(r+2). Its base residue is 2 from the word (0,1,1), so concatenation gives 2k/3 modulo 5^(ν₅(k)+1) on every start, without dividing by the exponent. For k=1 or 2 modulo 3 the possible window residues differ by one; at least one is a unit. These arguments cover the entire positive-even exponent domain and the infinite gcd, only at prime five. The supporting recurrence order follows by conjugation-invariance of the monic product over the d+1 algebraic-integer Binet roots. Independent rolling-modular replay: /workspace/review-evidence/replay.py 2, output 2.txt; 22,981 windows, including large powers of five in the length and exponents divisible by five. This corroborates but does not prove the all-parameter statement.

## originality

FAIL

The square gcd specialization is known, and the asserted all-even-power increment follows mechanically from the principal-unit block-sum argument and the same Binet parameters explicitly developed in the distinct quartic Lucas-balancing record 15fb03885e39. The latter's stated quartic gcd theorem alone is not the claim. Its exposed general geometric-sum calculation plus the binomial expansion of the already displayed B_n gives the full assigned statement, without a further lifting estimate. Both records carry the same date; this is an implication assessment, not an assertion of their relative chronology or of textual copying.

## value

FAIL

The per-window residue is a natural invariant and the matrix derivation is valid and convenient. As a distinct finding, however, it supplies the value obtained immediately by applying the available principal-unit block computation to the same recurrence's other Binet polynomial. The complement uses the same period obstruction, and the square global gcd was already determined. No separate structural extension, new obstruction or application survives beyond that evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
