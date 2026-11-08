# Self-review of the sharp quadratic last-gap theorem

## Correctness — PASS

The theorem is about functions, not formal expressions. The CRT argument reduces global support to one nonzero prime-power component. The minimum valuation of function values divides every coefficient of the integer Newton expansion because these coefficients are integer combinations of values at the zero vector, unit vectors, doubled unit vectors, and pairs of distinct unit vectors. Dividing yields a nonzero modulo-prime Newton polynomial. At odd primes the degree-two finite-field root bound gives nonzero support at least \((p-2)/p\). At two, the binomial quadratic functions depend on independent low digit bits; every nonzero Boolean quadratic has support at least \(1/4\), and an affine one at least \(1/2\). The case of modulus two is separately reduced from an integral polynomial, so no spurious binomial quadratic is introduced. Scalar CRT witnesses attain the precise lower bound for all prime powers and mixed moduli. The companion exact verifier exhausts 450,011 coefficient arrays in sixteen configurations and checks 297 sharpness witnesses. None of these finite tests substitutes for the unrestricted argument.

## Originality — PASS, with historical-priority uncertainty

Surowka and Regan, *Polynomials Modulo Composite Numbers* (arXiv:1404.4852, first public 18 April 2014), Section 8, explicitly conjecture the last zero-count gap at powers of two; Section 5 reports data and the main theorems concern divisibility and symmetries of solution counts. The present theorem proves that conjecture and gives a closed answer for every composite modulus. Field-only Reed–Muller minimum-distance bounds do not imply the prime-power normalization and mixed-modulus sharpness steps. The quaternary Plotkin/Gray-map Reed–Muller-like codes of Pujol, Rifà and Solov'eva (arXiv:0801.3024) use a potentially different evaluated family. Targeted database and literature queries did not identify an equivalent all-residue-ring assertion, although a coding-theory reformulation may be overlooked, and the Pujol full text was not inspected.

## Mathematical value — PASS

A published paper singled out the *last gap* between the two largest polynomial zero counts as a naturally motivated unsolved problem, and recorded unusual behavior for composite moduli. The present precise all-modulus theorem settles that problem in degree two: it determines the last gap over every modulus and proves the stated power-of-two pattern in arbitrary dimension. The Newton/Boolean-digit proof explains why composite rings present a sharp parity-dependent obstruction and how CRT carries it globally. It does not claim the full zero-count spectrum or higher-degree results.

## Closest literature and limitations

The primary complete source is arXiv:1404.4852, especially §§2, 5, 8. The finite-field Reed–Muller comparison uses arXiv:1407.3433 and DOI:10.1109/FOCS.2010.71. The quaternary-code comparison uses the abstract of arXiv:0801.3024, not its full text. An independent literature and proof audit remains necessary.

Self-review: passed. Independent audit: not yet performed.
