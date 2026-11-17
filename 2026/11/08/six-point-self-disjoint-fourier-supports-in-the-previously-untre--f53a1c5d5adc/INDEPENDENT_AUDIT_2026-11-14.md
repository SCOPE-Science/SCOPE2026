# Independent mathematical audit

## correctness

PASS

For p≡7 mod24, the Legendre symbol of -3 is +1, so t^2=-3 exists. Six indicated nonzero Fourier coefficients have unnormalized transform (z-zeta)(z-zeta^2)(zeta^(at+b)-1), which vanishes at each point in the six-site support, including (t,3) since t^2+3=0. For p=7 a support size<=5 would make a principal character minor singular; simultaneous translation and row/column phase factors permit assuming origin is included, reducing to exactly 1+48+1128+17296+194580=213053 cases. The inspected finite-field checker certifies prime 1000000093 and primitive 7th root 993004909, computes each determinant by exact modular elimination, and reports all 213053 nonsingular. A zero cyclotomic integer determinant would necessarily reduce to zero modulo this prime; therefore no complex minor of order<=5 is singular, yielding sigma_7=6. The frozen C++ source was inspected and independently compiled/executed, reproducing exact counts; it does not prove minimality for p>7.

## originality

PASS

Primary Zhou (2026) explicitly studies the same p-square support-disjointness but gives a p-dependent weaker 2p-2 construction and leaves the exact minimum difficult. An earlier four-point solution is restricted to p≡3 mod8; these primes are p≡7 mod8. Cyclic Fourier minor results apply to nonisomorphic cyclic groups rather than Fp^2. The six-support construction for all p≡7 mod24 and exact natural p=7 minimum survive these comparisons.

## value

PASS

The minimum self-disjoint support on the first prime square of a previously untreated anisotropic residue class is a natural exact Fourier uncertainty invariant. A concise six-point construction valid for an infinite congruence family and a fully exhaustive small-prime sharp certificate give usable nontrivial bounds and a reference case. Computation is necessary but not the sole value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
