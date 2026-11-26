# Independent mathematical audit

## correctness

PASS

The difference coding lifts exactly: a finite difference block occurring in the Sturmian shift is realized at a regular rotation intercept, and an integer translate gives the required initial letter modulo m. On each unit cell the length-n floor vector is componentwise nondecreasing with each coordinate varying by at most one, so distinct intervals give distinct words even modulo m≥2; the first letter separates different cells. The endpoint limits add no words. Uniform irrational-rotation frequencies for these intervals give unique invariant cylinder frequencies. A singular orbit may meet several of the n-block cuts but at most once per cut; the endpoint convention therefore changes counts by a bounded amount. The normalized Kesten condition is length in αZ+mZ; for sufficiency, the half-open indicator minus its mean is a difference of shifted fractional-part functions with shifts separated by an integer rotation iterate, hence its counts telescope uniformly. Reversing orientation and lifting a unit gap whose successor displacement is d gives length {dα}; irrationality makes its membership equivalent to m dividing floor(dα). The three successor candidates follow by comparing to the closest positive and negative returns: a+b≥n (otherwise the return at a+b improves one of the two extremes); in the middle strip n−a≤i<b a shorter positive displacement d<a would give a return at a−d closer on the negative side, and a shorter negative displacement −d with d<b would improve the positive return at b−d. The outer strips give the same exclusions using the respective one-sided minimum; their sizes and the middle size are n−a, n−b, a+b−n. At n=2 the middle is empty, while at n=1 length one cannot satisfy the criterion. For the Fibonacci step, the two pairs (F_{r-1},F_{r-2}) and (F_{r-2},F_{r-3}) form a unimodular basis of integer (index, numerator) pairs, with opposite signed errors by the Fibonacci identity. A closer return at 0<d<F_r cannot take two positive basis coefficients (index at least F_r), two nonpositive ones (nonpositive index), or one positive and one nonpositive (error at least the corresponding extremal error). The signed displacement (−1)^{j−1}F_j has floor (−1)^{j−1}F_{j−1}; Fibonacci parity then gives exactly the three phases and their density limits. I also independently sorted all m n actual lifted cuts using exact integer comparisons of quadratic irrationals, reproducing 3,072 direct counts and 15 Fibonacci cases; replay python3 /workspace/reproductions/sturmian1.py. The uploaded checker was inspected, not executed.

## originality

PASS

The finite lift and interval criterion are anteceded, and the rotation-gap machinery is classical. The exact same Resultary record is not independent evidence. What survives comparison is the mod-m weighted, all-length cylinder count and the explicit zero/positive three-phase law at golden Fibonacci lengths. The latter and the arithmetic count are not stated in the matching accessible formulations; no priority claim is made for either ingredient or for the successor machinery.

## value

PASS

Bounded discrepancy is a stronger property than uniform word frequency. An explicit census for the natural finite cyclic extension reduces m n words to three modular tests with known multiplicities, and shows genuine oscillation of the fraction of bounded-remainder cylinders: in the simplest Fibonacci binary lift entire lengths have none while other phases have positive limiting fractions. This supplies quantitative symbolic information not provided by strict ergodicity or the mere existence of at most three gap sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
