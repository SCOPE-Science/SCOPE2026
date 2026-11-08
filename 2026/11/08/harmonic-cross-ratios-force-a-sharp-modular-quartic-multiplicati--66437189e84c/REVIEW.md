# Scientific review: harmonic quartic multiplication rank

## Correctness

**PASS.** The statement is for every field of prime characteristic at least seven, with the third power of a specified squarefree quartic, a specified square graded map, and an exact nonzero determinant polynomial. The proof derives the matrix entry \(c_{6+j-i}\) directly from the quotient monomial bases. Two opposite triangular specializations prove both the constant and leading coefficients and therefore the exact determinant degree. At the harmonic parameter, the socle pairing is block off-diagonal by parity; a square cross-block minor is a Toeplitz continuant of determinant \((-1)^m\binom{m+2}{2}\), nonzero modulo every eligible prime. This establishes *equality* of the harmonic rank \(p-7\), not merely singularity. The Frobenius identity makes the other two harmonic parameters equivalent. The \(\lambda=0\) triangular witness and graded duality give full generic multiplication rank \((p-6)^2\) by an open-condition argument. Prime-field elimination checks cover eight primes, but the infinite assertion is supplied by the proof. No assertion is made about all other roots of the determinant.

## Originality

**PASS, provisional.** The closest inspected sources are Cook's 2011 work on positive-characteristic Lefschetz properties (arXiv:1111.4979), Lundqvist–Nicklasson's 2016 classification for monomial complete intersections (arXiv:1604.06820), Glasby–Praeger–Xia's 2014 modular tensor-product Jordan partitions (arXiv:1403.4685), and Dimca–Sticlaru's 2020 treatment of the *complex Waring rank* of binary quartics with harmonic cross-ratios (arXiv:2002.05617). The first three focus on powers of linear forms and/or the algebra-wide Lefschetz property, rather than the cross-ratio-parametrized determinant of a **quartic cube**. The fourth concerns a different characteristic and invariant: apolar catalecticant/Waring rank, not multiplication on a finite characteristic truncated group algebra. None of the inspected statements directly yields the present exact determinant degree and harmonic corank calculation. Searches for close equivalent formulations and comparison with accessible prior claim summaries revealed no direct match.

The most material priority risk is an unidentified general theorem about multiplication determinants of binary forms in characteristic \(p\) that could imply this special case. A specialist's independent literature review remains necessary; search non-matches do not establish priority. The determinant is not claimed to have only three roots: additional roots occur over extensions in some small primes.

## Value

**PASS.** The setting is the regular module of \(k[C_p\times C_p]\cong k[x,y]/(x^p,y^p)\), a natural modular-representation and Artinian-Lefschetz object. The theorem exhibits a rank jump *inside the squarefree quartic moduli locus*, where all root multiplicities agree. It provides two nontrivial quantitative invariants: the exact degree \(3(p-6)\) of the middle-map jumping divisor and a universal one-dimensional rank loss at the harmonic cross-ratios for every prime \(p\ge7\). A nilpotent Jordan profile is demonstrably not constant along that family. This is a characteristic-dependent structural phenomenon, not an arbitrary numerical slice, renamed identity, or routine tiny parameter gain. It does not purport to classify the full jumping divisor or all Jordan blocks.

## Closest literature and boundaries

Cook (2011) and Lundqvist–Nicklasson (2016) concern linear Lefschetz forms; their theorems are respected. Glasby–Praeger–Xia (2014) treats tensor products of Jordan blocks and provides modular Jordan context, but does not incorporate a four-line cross-ratio. Dimca–Sticlaru (2020) finds the same harmonic locus for complex Waring rank, an important but non-implicative parallel. This result requires \(p\ge7\), and its genericity claim is geometric; exceptional nonharmonic cross-ratios have not been classified.

Self-review: passed. Independent audit: not yet performed.
