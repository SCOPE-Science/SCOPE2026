# Scientific assessment

## Correctness — PASS

For the explicitly stated weak-deficit linear-wake model, differentiation reduces the layout derivative to the difference of a strictly decreasing and a strictly increasing positive function. The pointwise strict sign conditions use \(0<\delta<3/10\) and hold on the entire feasible interval. The derivative is positive at the midpoint and its value at the right endpoint decreases strictly with total span, crossing zero once. Those facts prove global uniqueness, endpoint-to-interior switching, and strict downstream bias. A logarithmic expansion of the exact interior stationarity equation gives the \(\delta/(6\kappa^2 L)\) asymptotic. An independent, executable Python checker reported 19,724 finite probes, including exact-rational algebraic signs and numerical comparisons; the proof, not those probes, establishes the infinite-parameter assertion. The \(\ell=0\) mathematical endpoint is covered; practical distances require \(\ell>0\).

## Originality — PASS, with priority qualifications

The searched mathematical record and the accessible primary literature have no located implication of the particular unique critical-span threshold and strict nonmidpoint optimum for a **single movable middle turbine, two fixed endpoints, full overlapping linear Jensen/Park deficits and cubic power**. Stevens, Gayme and Meneveau (2015; doi:10.1002/we.1835) use extended regular arrays and LES; Peña, Réthoré and van der Laan (2015; doi:10.1002/we.1863) analyze a quadratic wake-merging model; Stevens, Hobbs, Ramos and Meneveau (2016; doi:10.1002/we.2016) focus on large-farm fluid/economic spacing. Ma, Archer and Vasel-Be-Hagh (2022; doi:10.5194/wes-7-2407-2022) document linear superposition as an existing wake convention but not this optimization theorem. General historical numerical turbine placement and wake-layout optimization are established prior art. Earlier Grady–Hussaini–Abdullah (2005; doi:10.1016/j.renene.2004.05.007) and Lissaman (1979; doi:10.2514/3.62441) could not be inspected in full, leaving a bounded historical-priority risk. No novelty assertion beyond the stated finite-array mathematical claim is made.

## Value — PASS

Fixed endpoints and a mandated minimum spacing are natural in an already bounded wind-farm row. This exact phase change distinguishes a boundary-constrained layout from a fully interior optimum and proves that exactly symmetric spacing is never best under a specified conventional wake simplification. The proof and the \(L^{-1}\) asymptotic offer a nonnumerical benchmark for testing layout solvers and for checking what linear overlapping-wake approximations predict. In the example, the gain over midpoint at \(L=3\) is only about \(10^{-5}\) in normalized power, so no claim of large engineering improvement is made. The theorem's mathematical value is a model-specific classification and reproducible benchmark, not practical yield or a general nonlinear wake law.

## Limits and related evidence

Other wake-deficit combinations, speed-dependent thrust, atmospheric recovery, yaw control, turbulence, and changing winds can alter the result. Weak-deficit \(\delta<3/10\) is sufficient, not claimed sharp. Historical priority remains provisional, and the finite checker cannot replace independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
