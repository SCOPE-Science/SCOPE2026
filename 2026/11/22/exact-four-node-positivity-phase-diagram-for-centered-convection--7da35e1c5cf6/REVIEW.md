# Independent mathematical audit

## correctness

PASS

For four sites S^4=I. Independently inverting 1+2κt−(κ+1)tS−(κ−1)tS^3 modulo S^4−I recovers the claimed diagonal and the potentially negative off-diagonal tPκ(t)/[(1+4κt)Fκ(t)]; the other off-diagonals have strictly positive numerators for κ,t>0. Pκ has positive leading and negative constant coefficients for 0<κ<1, so its only positive root is t*. The identity M=θ^(-1)(Q−(1−θ)I) leaves the off-diagonal signs unchanged and imposes exactly Rκ(t)≥1−θ. Rκ decreases strictly from 1 to 1/4, not attaining 1/4 at a finite step; this proves the four regimes, with their endpoints. For θ=0 the negative explicit neighbor persists. At t*, substituting κFκ=1+4κt gives Rκ≥1/2 iff t*≤1/[2(1−κ)]; Pκ at that bound has sign κ²+2κ−1. Direct substitution also gives the quoted critical kernel and unique step. As κ tends to zero, t*∼1/(2√κ), κt* tends to zero and Rκ(t*) tends to 1/2. At κ=0 the bad coefficient is −t/(1+4t²) and the explicit step still fails. The theorem pertains to nonnegative completed updates, not intermediate stages, stability, or accuracy on general grids.

## originality

PASS

The same frozen finding indexed in Resultary is not independent prior coverage. The closest inspected primary result gives the obstruction only at zero diffusion. Neither the shared circulant technique nor the known endpoint implies positive-diffusion reentry at t*, the finite diagonal ceiling, or the sharp Crank–Nicolson ratio. Pass applies to the four-site positive-diffusion phase diagram, not the general theta method or the zero-diffusion obstruction.

## value

PASS

Four sites are the first even periodic grid for which the two centered neighbors are distinct. On this canonical case the negative spatial coefficient does not preclude nonnegative fully discrete evolution: the methods can regain positivity only above a nonzero time and can lose it again at a finite upper time. The exact second-order threshold and singleton identify which mechanism limits the admissible steps and provide a test case for general periodic positivity analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
