# Independent mathematical audit

## correctness

PASS

The secant coefficients a and b in the difference system are continuous and bounded by A and B; at a zero of the observed difference u, the hidden difference v is nonzero by uniqueness, and a>0 by strict inhibition. With U=√B exp(γt)u, V=√A exp(γt)v the angular speed is [b√(A/B)U²+a√(B/A)V²]/(U²+V²), between 0 and √(AB). Transverse departure from the vertical axis and monotone angle imply that the next observed equality requires a full half-turn; the sign before it is as stated. Bounded derivatives, rather than bounded response values alone, supply global Lipschitzness. For the symmetric logistic example, the equilibrium variational difference is −exp(−t/10) sin(t/4); its first positive zero is simple. Smooth dependence plus a uniform sign change around 4π and the universal lower bound give convergence of the first nonlinear return times. The saturation example has positive slopes matching at the joins; the exact decaying oscillator stays inside the affine core for every t≥0 and all allowed amplitudes, so its sampled x is identically 5 at kπ. The proof concerns equalities of two distinct trajectories, not periods of individual orbits. Inspected frozen VERIFICATION.md and CHECK.py without running the uploaded numerical script.

## originality

FAIL

Distinct indexed coverage of the core theorem and exact endpoint witness is demonstrable. The crossing theorem in a28f39575ba9 allows equal decay and yields the same bound, and its bounded affine-core attainment family reproduces the exact all-sample alias, even the specified response pair after a state rescaling. The logistic sharpness calculation is a distinct illustration, not coverage of an additional universal threshold. This is a statement-coverage judgment; it does not determine which of the two same-day entries appeared first or imply misconduct.

## value

FAIL

The sharp sampling boundary and permanent aliasing are worthwhile scientific questions, but the frozen contribution adds no distinct invariant once the broader crossing result and its affine-core family are taken into account. The logistic example illustrates the covered constant by a simple near-equilibrium limiting return, weaker than exact attainment as a general sharpness claim. It does not supply a separate characterization of logistic sampling that would justify accepting this package as a new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
