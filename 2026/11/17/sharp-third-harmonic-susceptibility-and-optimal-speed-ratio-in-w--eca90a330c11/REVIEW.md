# Scientific review

## Correctness — PASS

The exact co-rotating-frame pursuit law has a smooth circle equilibrium at separation \(\sqrt{1-n^2}>0\). Its variational matrix has strictly negative trace and positive determinant for each fixed \(0<n<1\); the periodic implicit-function theorem therefore supplies a unique smooth local response. A direct differentiated normalized-direction formula gives the two-frequency forced system, whose nonresonant complex solution yields \(\widehat P_3\). The squared susceptibility has derivative with sign \((5n^2-3)(n^2-3)\), proving a unique maximum of \(1/10\). All fixed-parameter limits and the non-uniformity at endpoints are explicit. The complete proof is in RESULT.md, with corroborative symbolic and ODE checks in verify.py.

## Originality — PASS, subject to historical priority risk

The closest primary paper [1], inspected across its equations, theorem, periodic-solution construction, simulation section and conclusions, establishes orbit existence/attraction and a Floquet product but does not provide first-order weak-ellipticity harmonic coefficients or their extremizing speed ratio. Its related 2024 extended paper [2] develops the circular Jacobian and reports the shape problem numerically, with no Fourier expansion. The complete seven-page conference chapter [3] proves reparametrization invariance of the geometric image rather than the anomaly-clock Fourier law. Search of related mathematical records found harmonics of unrelated oscillator and geometric models, not a stronger statement about the same pursuit ODE. This is evidence of noncoverage by inspected sources, not exhaustive novelty certification; unindexed older pursuit calculations remain a risk.

## Mathematical value — PASS

A prior qualitative observation was that the attracting pursuer's curve is not merely the shrunken evader ellipse. The precise third-harmonic response supplies a directly computable phase-resolved deformation observable in that model, with an unexpected speed tradeoff: it vanishes at both extreme subunit speed ratios and peaks uniquely at an intermediate algebraic ratio. This closes a natural local shape-response question rather than selecting arbitrary discrete parameters, and can calibrate near-circular numerical or perturbative studies. A time-Fourier mode is deliberately not misrepresented as a parameter-free geometric invariant.

## Relationship and limits

The source [1] is stronger on global existence, but it neither states nor implies a numerical value for this first-order susceptibility without additional variational analysis. Both [2] and [3] address the same pursuit rule and are counted as related prior work. All coefficients are at fixed subunit speed ratio and canonical anomaly time; unindexed literature and alternative invariant geometric measurements are residual research limitations.

Self-review: passed. Independent audit: not yet performed.
