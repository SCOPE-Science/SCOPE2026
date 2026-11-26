# Independent mathematical audit

## correctness

FAIL

The frozen mixed-space bounded-perturbation proof is invalid. Free transport is not strongly continuous on the stated space with L∞ in x: for a spatial step times a nonzero velocity factor supported at positive first velocity, the essential-supremum difference across the transported step does not vanish as t→0. Also the full K is not E→E bounded. For homogeneous data the two hard-sphere gains have a positive kernel proportional to r⁻¹ exp(−(r+w·ω)²/2), where v=w+rω. On a fixed angular band −w·ω∈[|w|/3,|w|/2], integrate r from −w·ω to −w·ω+1. There |v| is comparable to |w| and the weighted gain column has mass at least c|w|¹³, while the nonlocal loss column has weighted mass O(⟨w⟩). Nonnegative smooth inputs localized near large w contradict an E→E bound. In addition, the projection formula needs a spatial average in the coefficients if dx is the unnormalized measure used for H. These are errors in the frozen definitions and the premises of its Duhamel estimate, not counterexamples to the negative bound. In fact, the obstruction on smooth homogeneous data is true: in Y=L²(μ⁻¹dv), after conjugation by μ⁻¹/² the gain kernel is bounded by C r⁻¹ exp(−r²/8), and the nonlocal loss has Gaussian factors. Schur's bound gives K bounded on Y, and the corresponding column L² bounds give K:L¹(B₁)→Y. Reverse Duhamel, ∫₀ᵗ S(t−s)K e^(−sν)ψ ds, is uniformly bounded in Y for unit-mass smooth bumps supported in Bε. The bare term has L² norm ≥c(t) ε⁻³/², and the true hydrodynamic projection is stationary with bounded norm on these inputs. Thus no evolution agreeing with the conventional homogeneous solution on smooth data can satisfy the conjectured estimate. This does not validate the claimed C₀ realization or the proof on E.

## originality

FAIL

No distinct source read states the exact mixed-space inequality with its target constants. But the scientifically valid obstruction is a routine consequence of the classical hard-sphere kernel and Duhamel formula, and survival of unsmoothed initial data is explicitly established as the cutoff mechanism in prior work. The erroneous full-space bounded-perturbation assertions are not distinct valid content.

## value

FAIL

The valid obstruction is the standard non-diffusive cutoff term tested on a velocity concentration. It is a useful caution in reading factorization estimates, but it does not isolate a new boundary for enlargement, establish a sharp estimate for the regularizing remainder, or identify a velocity weight at which the known mechanism changes. The constants 60, 5/2 and weight exponent 12 play no scientific role in the obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
