# Scientific review

## Correctness — PASS

The proof is an all-dimension argument: four cubic corner derivatives establish individual-input variation equality; all finite minmod selector chambers reduce first-difference perturbations to unit steps, and the two adjoining derivative humps each have exactly \(8/27\) variation per unit derivative. The explicit positive-secant pairs attain the bound with a finite perturbation. The condition \(0\le\lambda\le3\) is shown sharp by an actual monotone input whose cubic reverses direction for outside scales. The standalone checker supplies exact symbolic identities and finite stress tests, not an infinite proof by enumeration.

## Originality — PASS (best-knowledge, with residual risks)

The full available archival Hermite/minmod technical sections provide monotonicity and continuity statements, not the exact two-input variation coefficient. The earlier Fritsch–Carlson and Fritsch–Butland publications introduce monotonicity criteria and derivative constructions; their full publisher texts were not accessible. Compared published analyses of Catmull–Rom, Akima and cubic Lagrange address different operators or range loss; a closer affine-minmod comparison measures discontinuous reconstruction and therefore has a different variation norm. Incomplete early full-text access and unindexed equivalent formulations remain priority risks; absence of search hits does not constitute proof of global novelty.

## Mathematical value — PASS

The exact amplification quantifies why TV preservation of every individual smooth Hermite reconstruction does not imply pairwise BV nonexpansivity. It reveals the four-knot threshold, computes the sharp cubically scaled correction, and identifies the largest admissible slope scale, all for a natural commonly used limiter and a stability seminorm relevant to interpolation errors.

## Limitations

No nonuniform-grid, periodic, harmonic-mean-limiter, vector-valued or time-discretization extension is claimed. Historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
