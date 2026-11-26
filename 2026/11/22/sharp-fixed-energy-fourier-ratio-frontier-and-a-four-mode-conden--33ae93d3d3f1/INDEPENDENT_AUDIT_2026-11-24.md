# Independent mathematical audit

## correctness

PASS

Parseval for the stated counting norms makes the normalized energy ∑λₖpₖ on the nonzero-frequency probability simplex. The four ground modes are (±1,0),(0,±1); summing sine-squares yields the stated mean. The two endpoint maxima and equality profiles follow from Cauchy–Schwarz. In the interior, for any t<Λ_N, weighted Cauchy–Schwarz bounds (∑√pₖ)² by (E−t)∑(λₖ−t)⁻¹. Equality requires full use of the budget and pₖ proportional to (λₖ−t)⁻². For this profile the derivative of its energy with respect to t is 2 Cov(λ,(λ−t)⁻¹)<0, with the stated limiting budgets. Thus the exact formula and all equality profiles follow; real phases may be chosen in conjugate pairs. This direct argument avoids needing the frozen proof's suggestion that two positive coordinates of an arbitrary candidate can always preserve both constraints. If using strict positivity instead, mix with the positive feasible distribution already given in the record: a zero entry gains order √η, while changes on positive entries cost at most order η. The uniform gap ≥8|k|², Taylor expansion of the sine multiplier and comparison of lattice squares with a planar annulus give S_N=log(N)/(2π)+O(1) and summable domination for T_N. Splitting the four minimal modes from the rest, weighted Cauchy–Schwarz and the trial inverse-gap profile give the exact two-sided bracket; its discrepancy is O_E(1/log N). Writing t_N=Λ_N−ε_N, the gap energy at fixed positive ε tends to infinity, forcing ε_N→0. The exact gap equation then yields Q_N=Δ_N A_N/B_N with A_N→T∞ and B_N=S_N+o(1), proving the condensate rate and ℓ¹ convergence of the normalized tail by domination. Independent bounded numerical replay at N=8,24,72,216 and E=60 checks the bracket and the energy equation (`python3 /workspace/review_checks.py 5`); the limits follow from the analytic argument, not those sizes.

## originality

PASS

The ratio itself, reciprocal spectral weights and weighted Cauchy–Schwarz are known ingredients. The strongest inspected sources give broad energy upper bounds, critical logarithmic order, or an exact resolvent extremizer under a different energy constraint. They do not cover the square-grid fixed-energy optimizer and its sharp additive term and conditional tail together. No stronger inspected statement giving these conclusions was found.

## value

PASS

The canonical first-difference budget quantifies how spectrally diffuse a mean-zero signal can be at a specified energy. Beyond the routine weighted bound, the two-scale law identifies an exact excess-energy factor, the additive term forced by bottom multiplicity, and the distribution of the small high-frequency mass that contributes the growing part of the objective. These clarify sharpness of the logarithmic regime and distinguish spectra with the same leading order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
