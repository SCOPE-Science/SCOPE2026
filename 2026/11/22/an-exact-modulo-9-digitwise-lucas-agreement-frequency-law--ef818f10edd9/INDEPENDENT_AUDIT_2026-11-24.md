# Independent mathematical audit

## correctness

PASS

Rowland's harmonic congruence iterated on the no-borrow digits gives the sum of adjacent corrections with the stated A and B; division by the digit Lucas product is legitimate there. A separate analytic certificate for the universal recurrence uses the nontrivial-character transfer. Group digits as A={(0,0),(2,0),(2,2)}, E={(1,0),(1,1)}, and F={(2,1)}; for a cube root x!=1, summing each row into these groups preserves functions constant on each group. The reduced matrix K is [[3,2,1],[2+x^2,1+x,x],[1+2x,2x^2,x]]. The group-count row (3,2,1) is the first row of K, so the filtered D_L equals the first coordinate of K^L times the all-ones column, plus its conjugate, also at L=0. The two characteristic cubics are conjugates of t^3-(4+2x)t^2+(6x-3)t+18+9x. Their product is the stated sixth-degree polynomial. The first six first coordinates are 1, 6, 21+3x, 78+3x, 279+9x, 999-81x; taking twice the real parts gives the stated initial values and the generating function. On the original six states all entries have modulus one. Equality in the eigenvalue bound 6 would force all components to have the same modulus and all diagonal phases to equal the eigenvalue phase, inconsistent with diagonal entries 1 and x. The nontrivial characters thus contribute o(6^L). Kummer's borrow count yields a single adjacent start/termination pair with 3 choices at each end and 6 at other digits; all positions with at least two borrows agree with the zero Lucas product. This proves the all-position formula, with the two boundary cases checked directly. A separately written program confirms the first six nonempty blocks, including W_6=18162 and E_6=179271 over 299481 cumulative comparisons, and verifies the 20 exact recurrence residuals used by the source's alternative Cayley–Hamilton certificate.

## originality

PASS

Best-of-knowledge pass for the global coincidence recurrence, limiting proportion, and consequent all-position count. The local congruence and Kummer valuation are established inputs; generic automata and prime-power Pascal counts are not novelty claims.

## value

PASS

Digitwise Lucas congruence is a natural approximation to the unit entries modulo nine. The theorem quantifies where it remains exact, including cancellations that the universally safe digits cannot capture. The compact recurrence and a limiting one-third agreement fraction give exact finite calibration and an asymptotic law, not merely first-block counts or a new notation for absolute residues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
