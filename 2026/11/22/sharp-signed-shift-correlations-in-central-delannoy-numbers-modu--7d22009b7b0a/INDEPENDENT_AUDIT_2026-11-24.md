# Independent mathematical audit

## correctness

PASS

Lucas' theorem splits the binomial sum digitwise, including the 2^j factor since 2^(7^i) is 2 modulo 7. The seven character weights are (1,-1,-1,0,-1,-1,1), so the support size is 6^r. Reconstructing the two-state ordinary-addition transfer gives the displayed matrices. The zero shift digits contribute diag(6,1), and the final extra digit has weight -1, not +1, for carry one. This proves the exact noncyclic formula for r at least the length of h and the limit after division by 6^r. Divide each matrix by 6: after the first nonzero digit the row has infinity norm at most 1/3. Any later digit 1 through 5 contracts by at least a factor of two; if there are only later digits 0 or 6, a 6 strictly attenuates the coordinate that enters the answer. The first coordinate has magnitude 1/3 precisely for first nonzero digits 3 and 5, with opposite signs, giving both and only the claimed equality classes. Zero shift has normalized value one and is excluded from the inequality. An independently written standard-library replay, /tmp/opencode/frozen-digit-correlations.py, computed actual Delannoy characters via constant terms of (3+x+2/x)^n mod 7 and matched all 396 noncyclic blocks tested at lengths 7, 49 and 343. The universal proof is the carry and contraction argument, not finite enumeration.

## originality

PASS

The distinct supported result is the evaluated mod-seven signed noncyclic block law together with the sharp all-lag range and complete signed extremizers. The one-point Lucas congruence and the use of a finite-state carry computation are not credited as new. No stronger matching statement was established in the evidence examined.

## value

PASS

The central Delannoy numbers are a natural digit-factorable sequence. The signed two-point statistic on the natural sparse support scale answers a different question from nondivisibility or density. Exact noncyclic correction and full positive/negative extremal families distinguish both boundary effects and the structure of long-lag agreement or anticorrelation. These precise results are useful for comparison with other residue-character correlations; the strict equality analysis is not supplied by writing down a transfer alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
