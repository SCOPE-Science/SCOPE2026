# Scientific review: heavy-tailed run durations and harmonic-trap support edges

## Correctness — PASS

The claimed equivalent is reconstructed from the equilibrium alternating-renewal age law, the exact deterministic deficit evolution within each orientation run, and a two-sided estimate that suppresses exceptionally short intervening runs. The latter requires \(\Pr(T\le u)=O(u^\beta)\). Karamata's tail theorem yields the constant \(1/[2m(\alpha-1)]\) for regularly varying waiting tails. For the half-\(t\) density, the survivor and integrated survivor have elementary primitives, giving the coefficient \(\kappa\tau/4\) and an explicit logarithmic relative-error bound. The numerical checker validates the special-case algebra and provides independent stochastic diagnostics, not the proof of the general statement.

## Originality — PASS, with residual priority risk

The original non-Markovian model and its half-\(t\) numerical case belong to Farago and Smith (arXiv:2401.01576). Their accessible primary full text reports a vanishing edge effective switching rate in the half-\(t\) example (with a force different from the harmonic one) and explains that the associated nonzero-rate large-deviation approximation fails; it does not provide an exact boundary-mass coefficient for a harmonic trap. The earlier Markovian harmonic-trap solution (arXiv:1811.03808) produces algebraic rather than logarithmic edge laws. General heavy-tailed on/off fluid literature may contain an abstract framework yielding this statement, and that publication-priority risk remains. No independence or exhaustive originality certification is claimed.

## Value — PASS

The shape of the support-edge stationary probability is a natural observable for confined active transport. The theorem determines its exact accumulation coefficient under a family of non-Markovian tumbling clocks, demonstrates a singular change from Markovian algebraic to heavy-tailed logarithmic behavior, and recovers the hidden power-tail index from position measurements in principle. These address a specific unresolved edge regime in the motivating non-Markovian analysis, rather than an arbitrary parameter slice.

## Closest literature and limitations

- Farago and Smith, arXiv:2401.01576: general non-Markovian stationary framework, half-\(t\) numerical edge behavior, but no quoted inverse-logarithmic boundary-mass equivalent.
- Dhar et al., arXiv:1811.03808: exact Markovian run-and-tumble trapping and algebraic stationary edge transitions.
- Heath, Resnick and Samorodnitsky (1998), DOI 10.1287/moor.23.1.145: heavy-tailed on/off fluid models; related renewal mechanism, but the retrieved source description does not establish the harmonic-filter endpoint formula.
- Sun, Ye and Podgornik, arXiv:2409.00578: finite tumble-time harmonic-trap moments, distinct from a general regularly varying law; the complete text was not accessible in this review.

The result assumes independent identical positive run times, finite mean, a quantitative near-zero time bound, a harmonic trap and exact stationary probabilities. No finite-data stability theorem, general nonlinear-force theorem or full density-edge asymptotic is asserted.

Self-review: passed. Independent audit: not yet performed.
