# Scientific review

## Correctness — PASS

The state space and continuous-time rates are explicit, and positive immigration makes the birth–death chain irreducible. The stationary adjacent-ratio identity follows from detailed balance. The polynomial has degree no greater than the largest permitted infected-source group size plus one; its values at zero and the population endpoint are strictly negative. Each nonzero strict stationary mode consumes a distinct bracketed positive polynomial component and therefore two real roots. The mode ceiling is rigorous even when other adjacent masses tie. For every population size at least four, the displayed positive parameter construction makes the adjacent ratios negative, positive, negative, then positive relative to one, giving exactly three peaks at 0, 2 and full infection. A separate four-person rational instance was checked exactly. `verify.py` reproduced finite stationary and microstate-balance checks. No simulation is used as an infinite proof.

## Originality — PASS, with priority uncertainty

The closest prior scientific source is Kiss et al., arXiv:2309.12752v1, which derives the full higher-order finite Markov rates and proves a limiting mean-field multistability statement. Their stationary solutions are deterministic mean-field fixed points, not strict peaks of the irreducible finite stationary infection-count law after spontaneous infection. Their polynomial degree discussion is antecedent motivation but does not supply this stationary root-bracketing theorem or the exact all-population strictly positive transmission construction. The older epsilon-SIS results concern pairwise infection; Matamalas et al. study pair/triadic spreading via approximation. An earlier finite triadic-only stationary-mode threshold also cannot imply the four-person sharpness example, and its exact threshold is not being claimed again. Broader general birth–death stationary formulas imply the ratios used here but do not themselves specify this sharp simplicial order boundary. No exact covering assertion was found in targeted research searches; this is not proof of priority.

## Value — PASS

The mathematically motivated issue is how increasing contagion group size changes the possible *shape of a finite stochastic equilibrium*, a distinct observable from the deterministic steady-state count. The result identifies a sharp structural interaction-order boundary (two peaks up to three-person groups versus three peaks available at four-person groups), proves the ceiling for every finite population, and shows that the sharpness is not confined to a single small example. All infection mechanisms can be strictly positive and the three-peak region is open. The result provides a finite benchmark for interpreting higher-order epidemic multistability. It does not assert that such parameters are common empirically.

## Closest literature and limitations

Primary sources: Kiss, Iacopini, Simon & Georgiou (2023), arXiv:2309.12752v1, Sections II.B–C and III.B; Matamalas, Gómez & Arenas (2019), arXiv:1910.03069; Van Mieghem & Cator (2012), DOI 10.1103/PhysRevE.86.016116 (abstract available; complete text not accessible in the material inspected). Exact general birth–death balance is standard. The new strict-mode theorem assumes complete mixing, weak positive immigration and nonnegative interactions; zero-importation quasi-stationary laws and noncomplete structures are not covered. Search incompleteness leaves a residual priority risk.

Self-review: passed. Independent audit: not yet performed.
