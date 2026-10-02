# Independent mathematical audit — SCOPE-20260909-073

Outcome: **FAILED**.

## Correctness
**PASS** — The quotient (x,y)->(y,x^2) maps y^3=x^4-1 to Y^2=X^3+1. Using E(Q)=Z/6, the only possible y-coordinates are -1,0,2; the corresponding equations x^4=0,1,9 give x=0, x=+/-1, and no rational solution respectively. Together with the unique point at infinity this gives exactly four rational points. The direct mod-7 projective count of 12 points makes both stated p=7 bounds non-sharp.

## Originality
**FAIL** — A 2024 paper by Fall-Sarr states that its family y^(3n)=x^(4n)-1 extends Debarre-Klassen, who had already determined the algebraic points of degree at most two on the n=1 curve y^3=x^4-1. That prior result strictly contains the rational-point census in this record.

## Value
**FAIL** — The alternate elliptic-quotient proof is clean, but the exact rational census is already contained in stronger prior low-degree-point work, and the Stoll/Coleman non-sharpness at p=7 is then an elementary comparison rather than an independent substantive gap.

## Source inspections
- **Fall-Sarr, Determination of Algebraic Points of Low Degree on a Family Curves, Balkan Journal of Applied Mathematics and Informatics 7(2), 2024** — Full 14-page PDF inspected. Its abstract/introduction states that the work extends Debarre and Klassen, who determined the degree-at-most-two points on C1: y^3=x^4-1; reference [4] identifies Debarre-Klassen, J. Reine Angew. Math. 446 (1994), 81-87. Consequence: stronger prior coverage contains the rational-point census
- **Debarre-Klassen, Points of low degree on smooth plane curves, J. Reine Angew. Math. 446 (1994), 81-87** — Identified through the full-text 2024 paper as the prior source for C1 low-degree points. Consequence: prior result subsumes degree-one points

## Residual risk
See the accompanying JSON audit for the explicit residual-risk record.
