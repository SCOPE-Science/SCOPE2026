# Scientific review

## Correctness: PASS

Homogeneous fraction reduction is well-defined because the two child maps preserve coprimality. All four-state and six-state transitions are written out explicitly and reduce, by inversion symmetry, to the displayed three- and four-dimensional integer matrices. Their characteristic polynomials give the claimed rational generating functions for **every** depth. Exact partial fractions exhibit the leading oscillatory coefficients; an algebraic-integer argument proves irrational phase and sharp limsup/liminf, without extrapolating from finite data. A separate direct-tree implementation agrees with the formulas to depth \(15\); exact generating-function checks run through depth \(80\).

## Originality: PASS within inspected evidence

Lynch–Mackey's publicly available 2022/2024 full text studies three parity classes modulo two, not projective reductions modulo three or five. Stanley's public 2019 text supplies general recurrence machinery for power sums, not an evaluation of the present modular projective statistics. Closest public research records on triple and quadruple Stern residues concern asymptotic densities over the overall sequence and do not state the **exact per-depth** spectra or the sharp constants. The separate previously recorded modulo-five Stern-character result counts numerator characters only; it does not imply the joint numerator/denominator classes. Exact statements, not just title similarity, were compared. There remains a risk that an earlier projective random-walk computation implicitly contains the special cases; two relevant research-record full texts could not be fetched.

## Value: PASS

This supplies the first two odd-prime cases naturally suggested by the established modulo-two Calkin–Wilf parity theorem. It gives a complete all-depth classification, a sharp universal mixing exponent, explicit irrational oscillatory phases, and different nonzero sharp constants at the first two odd primes. These are exact arithmetic statistics of a canonical enumeration of all positive rationals, rather than arbitrary parameter choices or a finite table lookup. The result is not a general theorem for all primes.

## Closest literature and limits

P. Lynch and M. Mackey, arXiv:2205.00565 (2022), compare parity and general rational partition; R. Stanley, arXiv:1901.04647 (2019), gives Stern-array moment recurrences; related 2026 three- and four-residue Stern records provide asymptotic data at a different normalization. No surveyed source was found that implies the displayed exact \(p=3,5\) projective formula and amplitudes. The ability to inspect all older notes and the two fetched-unavailable research-record full texts is limited. No independent verification is claimed.

Self-review: passed. Independent audit: not yet performed.
