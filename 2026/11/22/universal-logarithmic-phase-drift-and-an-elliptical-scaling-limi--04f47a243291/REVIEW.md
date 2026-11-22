# Scientific review: critical business-cycle phase and scaling ellipse

## Correctness — PASS

The claimed parameter interval, punctured local domain, normalization and limiting quantifiers follow from the explicit real-to-complex linear conjugacy and a locally invertible cubic nonresonant transformation. The resonant coefficient is computed from the **original exact polynomial** as \(C=-3\alpha(1+i c)/(2(1+\alpha))\); its rotated real and imaginary parts are respectively \(-a_\alpha\) and \(a_\alpha c\). Since \(a_\alpha>0\), the local normal form strictly contracts radii. Reciprocal-radius summation gives \(n|u_n|^2\to (1+\alpha)/(3\alpha)\), and summability of the angular remainder proves the finite renormalized phase with coefficient \(c/2\). The distinction between rational and irrational linear rotation is handled independently: Weyl summation for the latter, slow unbounded logarithmic drift on a residue class for the former. There is no need to assume all initial states belong to a global basin. Finite checks from the accompanying script passed; they do not replace the proof.

## Originality — PASS within checked sources

The closest primary paper, Grushkovskaya (2024), fully treats this precise neutral map but proves local decay estimates and prints a radial normal form, without proving its nonzero logarithmic phase drift or describing the full ellipse of **rescaled** limit points for all rational and irrational angles. Puu and Sushko (2004) study attracting sets, fixed-point stability and post-bifurcation invariant circles, which cannot imply the asymptotic rotation phase at the critical fixed point without further analysis. The nonresonant cubic normal-form technique is classical background, not a new method; the new mathematical content is the model-specific strict angular drift and its all-angle elliptical accumulation consequence. Relevant indexed results on cubic Liénard weak foci, cubic stable flows and neutral maps use other flows or maps and do not cover this recurrence. An unindexed equivalent derivation remains possible.

## Mathematical value — PASS

At a nonhyperbolic fixed point, a decay bound does not identify how signed observables oscillate, whether a scaled state converges, or what its limit set is. This theorem gives the exact complex amplitude and logarithmic phase in the model's original coordinates, with a parameter-explicit ellipse describing every scaled subsequential limit. The rational-angle conclusion is not implied by ordinary irrational linear-rotation density: the nonlinear, unbounded logarithmic phase creates the complete limit set even at rational rotation numbers. The model is naturally defined by an established stability boundary, rather than an arbitrary numerical slice. The result neither claims a general theorem for all neutral maps nor an invariant unscaled attractor.

## Closest literature and limitations

- Grushkovskaya, *Asymptotic behavior of solutions of nonlinear discrete systems in critical cases*, first published 16 October 2024, https://doi.org/10.1007/s11071-024-10295-6 , especially Sections 3 and 4.1.
- Puu and Sushko, *A business cycle model with cubic nonlinearity* (2004), https://doi.org/10.1016/S0960-0779(03)00132-2 , especially Section 2.1.
- Generic cubic Neimark--Sacker normal forms are established background. No independent novelty certification is claimed. The local constants need not be uniform near the endpoints, and no global-basin statement is proved.

Self-review: passed. Independent audit: not yet performed.
