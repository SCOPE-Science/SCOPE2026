# Scientific review

## Correctness — PASS

The positive off-band spectrum is reconstructed from a Jacobi recurrence and an exact decaying-tail matching condition. A finite Schur complement with its strictly monotone parameter-scaled diagonal proves the number and simplicity of threshold crossings. Taylor expansion of the matching equation is uniform near each fixed noncritical or critical root, giving the explicit \(m^{-3}\) correction and the critical \(m^{-4}\) law. The finite diagnostics in `check.py` passed 104 assertions, but numerical experiments do not substitute for the infinite-dimensional proof.

## Originality — PASS, qualified

The 2015 weighted-shift point-spectrum paper covers arbitrary *fixed-length* prefixes and supplies the already-known finite secular framework. The 2014 two-bond paper and a related indexed two-bond classification also cover the smallest fixed-prefix special cases. The 2026 geometric-modulation paper addresses a different decay regime. None of the inspected scientific claims states the growing-prefix weak-contrast limit together with the all-bound-state \(m^{-3}\) correction and the critical \(m^{-4}\) edge scale. The leading continuum half-line square-well equation is classical and is not claimed as a novel spectral object. A potential stronger uniform lattice-to-continuum theorem outside the reviewed sources remains the principal novelty risk.

## Mathematical value — PASS

The number of enhanced links tends to infinity while their contrast vanishes at the exact scale that competes with the essential band edge. The result predicts the number, spacing, and localization rates of every emerging bound state, separates the generic quadratic edge scale from a quartic critical scale, and quantifies the leading finite-lattice correction. Those are natural spectral-stability quantities not obtained by holding the number of links fixed. The result is limited to a natural piecewise-constant profile; no generalization to arbitrary smooth profiles is asserted.

## Closest prior work and limitations

Undrakh–Nakazato–Vandanjav–Chien (2015) is mathematically the strongest comparator, because its arbitrary finite-prefix polynomial characterization contains the starting spectral recurrence. The sharp asymptotics for a *simultaneously growing* prefix were separately derived and checked, rather than credited as a new recurrence. The 2014 article specializes to two raised links, and the 2026 article to geometric weighted modulation. A theorem containing a uniform continuum expansion could supersede the new assertion; no such matching result was identified in the actual comparisons. No independent audit was conducted.

Self-review: passed. Independent audit: not yet performed.
