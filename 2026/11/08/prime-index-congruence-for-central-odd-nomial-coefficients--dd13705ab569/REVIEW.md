# Scientific assessment

## Correctness — PASS
The coefficient extraction is performed in the localized formal power-series ring \(\mathbb Z_{(p)}[[x]]\). The binomial expansion of \((1-x)^p\) modulo \(p^2\), geometric-series inversion, and harmonic-sum calculation each follow from explicit integer or modular identities. The exceptional index range is exactly \(1\le j\le(p-1)/2\), regardless of the quotient \((2d+1)/p\). The standalone checker compares two independent exact integer coefficient algorithms for 319 parameter pairs. Boundary cases \(d=0\), \(p=3\), and arbitrarily large \(d\) are included in the proof.

## Originality — PASS, with residual historical priority risk
Searches for central odd-nomial, pentanomial, multinomial, Fermat-quotient, and prime-square congruences, plus semantic research-index searches using the complete two-branch formula and aliases, did not identify a theorem covering this statement. Sun (arXiv:1008.3887, full text) proves weaker \(\pmod p\) prime-index statements for trinomial coefficients. Rudolph-Lilith and Muller (arXiv:1403.5942, full HTML) give central odd-nomial trace and trigonometric formulas, not this congruence. Mellit–Vlasenko (arXiv:1306.5811, full PDF) impose a Newton-polytope hypothesis inapplicable for \(d\ge2\). OEIS A005191 lists the pentanomial sequence and other congruences but not this two-parameter classification. As with any elementary identity, the possibility of an earlier equivalent statement cannot be excluded by searches alone.

## Mathematical value — PASS
This is a complete sharp prime-square congruence for the prime-index return-to-origin count of a symmetric random walk with every step from \(-d\) to \(d\), simultaneously for all odd primes and all step radii. A single arithmetic relation, \(p\mid (2d+1)\), produces an exact universal jump to \(2^p-1\), a Fermat-quotient correction independent of the quotient \((2d+1)/p\). The result naturally generalizes the classical trinomial and pentanomial coefficient families and gives a reusable coefficient-extraction method at the first nontrivial prime-power modulus. It does not classify higher powers of \(p\) or general exponents.

Self-review: passed. Independent audit: not yet performed.
