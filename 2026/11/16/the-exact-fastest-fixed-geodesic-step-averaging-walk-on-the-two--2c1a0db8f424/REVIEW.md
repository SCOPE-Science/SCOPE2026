# Scientific review

## Correctness — PASS

The model is the normalized spherical-circle averaging Markov operator on \(L^2_0(S^2)\), not an arbitrary group walk. Funk–Hecke diagonalization gives its exact multipliers \(P_\ell(\cos\theta)\). Degrees one, two and three prove a global lower bound and uniqueness of the candidate. The exact fourth- and fifth-degree evaluations are strictly smaller. Laplace's Legendre integral and a closed third binomial moment give \(\sup_{\ell\ge6}|P_\ell(a)|\le B_6<r\) for all remaining degrees. The attached code verifies crucial exact expressions and rational comparisons, with finite tests explicitly distinguished from the infinite proof. The endpoint angles and all positive iterate counts are included in the proof.

## Originality — PASS, with historical-priority risk

The closest same-object primary analysis is Su (2001), whose inspected Section 5 gives exactly the Legendre multipliers but seeks discrepancy mixing order, not minimizing the spectral radius over the fixed step angle. Mangoubi–Smith (2016) use the fixed-time geodesic algorithm but prove curvature-based Wasserstein mixing bounds; the inspected Algorithm 1 and Theorem 5 do not supply this exact minimax. Schär–Stier (2023) concern a distinct geodesic-slice sampling kernel with a uniformly sampled arc angle and a Wasserstein guarantee. Searches for the exact radical, the spectral norm, alternative circle-average names, and the degrees-two/three balancing condition identified no statement subsuming the exact classification. This is a reasoned novelty comparison rather than a claim that unsuccessful searches prove uniqueness in the literature; a hidden earlier extremal Legendre result remains possible.

## Value — PASS

The question is intrinsic to designing isotropic fixed-length random moves on the sphere: a single angle must damp every nonconstant harmonic degree. The answer is a sharp global, infinite-frequency minimax with exactly two complementary optimizer angles, a twelve-dimensional worst-case harmonic subspace, and an exact exponential rate for every number of steps. It improves the equatorial choice's worst-case factor \(1/2\) to \((2+3\sqrt6)/25\) and separates spectral design from discrepancy/Wasserstein estimates. No stronger claim about point-mass total variation is made.

## Scope and remaining risks

A specialized Legendre supremum optimization from historical approximation or spherical random-walk literature may predate this calculation; independent audit and priority verification are outstanding. No optimization over angle mixtures or other sphere dimensions has been proved.

Self-review: passed. Independent audit: not yet performed.
