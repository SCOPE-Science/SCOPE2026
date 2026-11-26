# Independent mathematical audit

## correctness

PASS

Maity's Lemma 2.2 gives exactly the stated starting values and recurrence, and Theorem 3.1 proves the baseline on the same four progressions. The independent replay recomputes the complete sparse recurrence polynomials and calculates the low coefficients directly from the Euler product, rather than by logarithmic differentiation. For the deepest lift, 1646+3125b plus 1479 is 3125(b+1); moving this factor to q^5 leaves exponent 7605+15000b. Extraction shifts q by (1479−4)/5=295, canceled by xi^295. This gives the stated intermediate E(q)-exponent 9375+15000b. The factor 1920 has valuation one, so Frobenius modulo 625 gives the claimed final dissection, with all four target progressions outside its support. The first lift works by the same two exact Frobenius steps at the indicated lower moduli. For the sharpness witnesses, F(q)^(5^t)−1 has coefficients divisible by 5^(t−1) through degree 14: after Frobenius the remaining Euler product at q^5 to exponent 24·5^(t−1) can itself be moved to q^25 modulo 5^(t−1). Thus the quadratic parameter terms vanish modulo 5^(t+1) in each of the three strata. The affine residues give exact valuations in the first two strata; 3−b and 3+b cannot both vanish modulo 5 in the last.

## originality

PASS

Credit the exact modulo-125 family to Tang/Maity and treat the modulo-625 dissection as prior as reported. The supported distinct claim is the modulo-3125 dissection on the narrower family, the paired obstruction to a further common lift, and the resulting complete depth classification. No inspected statement supplies or already implies these extra results without new arithmetic and lifting arguments.

## value

PASS

An existing uniform partition congruence motivates the optimal common modulus for every tuple order in that family. The deepest exceptional class and an all-index support identity answer that question rather than merely detecting isolated high valuations. The two small coefficients' incompatible zero classes explain why the uniform lifting stops even at tuple orders where either coefficient alone would miss the obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
