# Scientific audit — 2026-10-01

## Final claim

No universal differential Santaló inversion for the projective Finsler X-ray on RP^2

## Correctness — PASS

The round RP2 reduction to the even Funk transform is correct. On H_{2k}, the Funk multiplier is a nonzero constant times P_{2k}(0)=(-1)^k binom(2k,k)/4^k, so the normal multiplier is asymptotic to c/k. If a finite-order D satisfied DN=Id, averaging over SO(3) preserves differential order and the identity, producing an invariant differential operator P(Delta). Its multiplier is polynomial in 2k(2k+1), hence either bounded or grows with even polynomial degree in k; it cannot equal the reciprocal normal multiplier, which grows linearly in k. Thus the claimed obstruction is mathematically sound.

## Originality — FAIL

The argument is a short mechanical corollary of classical Funk harmonic multipliers together with the standard classification of SO(3)-invariant differential operators. Published Funk literature already gives exact inversion on even functions and modern Rubin papers explicitly formulate inversion via fractional/integral constructions and polynomial-in-Laplacian weighted differential operators. Once the standard multiplier P_{2k}(0) is inserted, the impossibility of a bare finite-order D(F*F)=Id follows immediately from growth. Under the audit rule that unstated corollaries of stronger prior theory count as covered, this does not clear originality.

## Scientific value — PASS

Testing a proposed universal differential Santaló inversion on the symmetric round metric is a natural and decisive boundary test. A correct obstruction would be useful because it separates differential inversion from the known nonlocal/fractional inversion mechanisms. The rejection is prior implication, not scientific motivation.

## Sources inspected

- **Boris Rubin, On the Funk-Radon-Helgason Inversion Method in Integral Geometry** (https://arxiv.org/abs/1207.5178): STRONG_PRIOR_FRAMEWORK. The paper develops established nonlocal/fractional Funk-Radon inversion, placing the round inversion problem in prior theory.
- **Boris Rubin, The Fourier Transform Approach to Inversion of lambda-Cosine and Funk Transforms on the Unit Sphere** (https://arxiv.org/abs/2005.03607): STRONG_PRIOR_FRAMEWORK. It explicitly introduces weighted differential operators that are polynomial functions of the Beltrami-Laplace operator and derives Funk inversion formulas.
- **Bailey, Eastwood, Gover, Mason, The Funk transform as a Penrose transform** (https://doi.org/10.1017/S0305004198002527): BACKGROUND_COVERAGE. Bijectivity of the classical even Funk transform is long established.

## Residual risks

- The artifact's numerical loop is not needed for the proof; the audit rests on exact multiplier identities.
- The originality failure is by mechanical implication from standard prior theory, not an assertion that a prior paper uses the same headline wording.

## Disposition

**failed** — at least one required scientific axis does not pass. The original scientific files are preserved unchanged as evidence.
