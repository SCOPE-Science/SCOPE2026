# Independent mathematical audit

## correctness

PASS

Rampersad–Wiebe 2023 Theorems 13 and 14 supply the exact original integer binomial-sum run-length transforms with seeds (1,1,1,1) and (1,2,2,3) and the common order-four recurrence. Modulo 2 the recurrence has period five with parity profiles 11110 and 10010; because the transform is a product over lengths of maximal binary one-runs, U is odd iff every length lies in residues {0,1,2,3} mod5, V iff each length lies in {0,3} mod5. A unique binary-word block decomposition gives rational enumerators (1+z+z²+z³)/(1-z-z²-z³-z⁴-z⁵) and (1+z³)/(1-z-z⁴-z⁵). Denominators have unique simple strictly positive dominant roots via triangle inequality and the degree-one term, so their coefficients grow as C_i λ_i^m with λ_U≈1.9659482, λ_V≈1.4970940, and arbitrary-X support exponents log2 λ_i. Independently computed original binomial residues using Lucas bit criterion for every n<1024 and exact dyadic counts m<=10; the all-n assertion is the recurrence/language proof, not finite enumeration.

## originality

PASS

The 2023 paper already proves both underlying run-length identities. Further, a 2026-11-02 theorem gives the entire U zero-valuation generating function, U exponent and its fixed higher 2-adic strata; OEIS A124312 independently counts the U language. Neither these nor the separately inspected V-Mersenne valuation theorem give the second V odd-support rational enumerator, its exponent, strict nested support and exponentially vanishing v_m/u_m. Originality is credited solely to that surviving V count and comparative law, not the known U component or the transform identities.

## value

PASS

The exact odd-support density of a named arithmetic binomial sum is a natural 2-adic sparsity invariant. The V formula supplies a new complete exact counting law and entropy exponent, sharply distinguishing two companion transforms with identical recurrence coefficients but different seeds; the V support is asymptotically negligible even among odd U values. The known U count and general regular-language enumeration method alone would not provide the V arithmetic conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
