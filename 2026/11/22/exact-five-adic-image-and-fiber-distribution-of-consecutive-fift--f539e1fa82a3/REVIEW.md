# Independent mathematical audit

## correctness

PASS

Expansion with t=2x+1 gives 16F+4=5U, U=(t^2+1)^2. For each t=±1 mod 5 the derivative of U is a unit and Hensel lifting gives exactly one branch onto 4+5 Z_5. On t=5v, U=1+50(vS(v))^2 with S(v)^2=1+(25/2)v^2, S(v)=1 mod 5. The difference S(v)-S(w) equals (25/2)(v-w)(v+w)/(S(v)+S(w)), so vS(v)-wS(w) is v-w times a unit congruent to 1 mod 5. This proves bijectivity on each finite reduction (thus also on Z_5). For each t=±2 mod 5, lifting t^2=5z-1 produces the bijection z=(t^2+1)/5, so U=25z^2 on both outer branches. The output branches reduce to 4,1,0 mod 5 and are disjoint. For k>=3, regular lifts contribute 2*5=10 per image residue. In a critical ball the normalized variable runs independently modulo 5^(k-1), whereas the square is specified modulo 5^(k-3); this gives 25 times the square-root count per ball. At k=1 all five inputs map to 1; at k=2 residues 1,11,6 have counts 10,5,10. A nonzero square of valuation 2h<j has two nonsingular unit roots modulo 5^(j-2h), with 5^h extra lifts each; the zero equation requires valuation at least ceil(j/2). Thus Q(j) and R_k follow by counting two of four unit classes at each permissible even valuation, plus zero. The square set has measure (2/5)/(1-1/25)=5/12; scaling the regular and two square components yields (1/5+1/60+1/60)/5=7/150. Independent replay compared complete fibers via the valuation formula to direct modular evaluations on all 488280 inputs through k=8, giving 1,3,7,31,147,731,3647,18231 image sizes. Replay: python3 /workspace/independent_replays.py 5.

## originality

PASS

The inspected statements establish independent-variable power-sum image counts and related but different prime-power classifications, not the adjacent fifth-power image or its full fibers. There is a substantive equivalence to a precision-shifted quartic Dickson value-set/fiber problem, so the inaccessible directly relevant 1991 article remains a material priority risk, without verified coverage.

## value

PASS

The polynomial is the natural fixed-unit-step fifth-power difference, and 5 is the prime dividing its exponent. Knowing its targetwise multiplicities solves local representability for this constrained expression, rather than merely reporting a density or sample of values. The two inequivalent critical ball mechanisms, together with the regular two-sheet lifting, explain the exact finite distribution and remain useful at all depths. The result is narrow but its solution uses the geometry of the singular balls, not a substitution in an identified prior count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
