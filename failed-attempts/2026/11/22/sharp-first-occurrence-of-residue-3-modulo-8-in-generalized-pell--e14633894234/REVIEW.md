# Independent mathematical audit

## correctness

PASS

For the specified impulse initial conditions, multiplying the recurrence denominator by 1-z gives B+z^(k+1), with B=1-3z+z², and the generating numerator is z(1-z). Two terms of the formal geometric expansion leave a remainder of valuation 2k+3. Thus through index 2k+2 the sequence equals the odd-index Fibonacci values less the first shifted correction E=z(1-z)/B². The odd-index residues (1,2,5,5,2,1) cycle by their second-order recurrence, so all indices through k+1 avoid residue 3. I independently divided z(1-z) by B² modulo 8 using its coefficients (1,-6,11,-6,1), obtaining E's degrees 0 through 15 as (0,1,5,3,1,2,6,1,7,1,1,4,4,1,1,7). For r=k mod 6 and offsets h=1,...,16, subtract degree h-1 from entry 1+((r+h-1) mod 6) of the Fibonacci cycle. These six rows give first-hit offsets (7,16,9,6,6,7); k>=14 ensures the whole window is inside the exact coefficient range. Directly adding the preceding k terms with weight 2 on the most recent and reducing modulo 8 from initial values 0,1 reproduces the complete exceptional table for k=3,...,13. For k=2 the starting consecutive pair (0,1) repeats after eight steps with no residue 3. This proves the infinite and finite cases separately. The frozen checker was inspected, not executed. The result concerns this single residue and not the full periods or a new prime-exclusion theorem.

## originality

FAIL

No inspected source prints the complete first-hit table as such, but the entire parameter-uniform correction on the decisive window is already explicit in Bravo–Herrera–Luca, equation (1.3), attributed to Kılıç. Combined with the established early exclusion and the modulo-8 odd-Fibonacci cycle, the six-class formula is mechanically determined by a fixed sixteen-column substitution and scan, with only direct recurrence iteration for the remaining eleven orders. This is coverage by implication, not a claim that the older sources printed these numerical offsets or that the frozen result is false.

## value

FAIL

The residue and least index are naturally motivated by the initial obstruction to odd-exponent Wagstaff-type terms, and the displayed table is a convenient reference. But the substantive all-order structure reduces to evaluating the existing parameter-separated convolution on six residue classes and scanning a fixed short window, plus direct iteration of eleven orders. The record adds no nonmechanical exact invariant beyond those evaluations, and its exclusion before the first hit is the immediate residue test, not a further Diophantine result. It therefore does not meet the value criterion for a narrow exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
