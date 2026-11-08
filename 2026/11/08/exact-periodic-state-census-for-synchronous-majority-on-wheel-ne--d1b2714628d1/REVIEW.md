# Scientific review

## Correctness

**PASS.** The theorem fixes the graph and tie rule, distinguishes labeled periodic configurations from unordered orbits, and splits states according to whether the hub changes. In the constant-hub case, the two-step identity forces all-ones or all-zeros on each distance-two component; the hub majority condition excludes the all-one rim and leaves precisely two consensus states and four additional even-rim states. In the changing-hub case, the two-step identity enforces no isolated ones along distance-two edges, while the two strict hub-majority conditions are exactly the coefficient inequalities. Cyclic run compositions give the stated integer coefficients, including the doubled-edge convention at length two. The standard symmetric-threshold period bound establishes exhaustiveness. Independent full-state enumeration, transfer calculations, and exact coefficient arithmetic pass the packaged verifier. Finite tests corroborate, but do not establish, the all-size proof.

## Originality

**PASS, subject to priority uncertainty.** Goles–Olivos (1980) already establishes the period-one-or-two restriction, not the graph-specific count. Zehmakan (arXiv:2302.06760; 2024 journal article) treats this majority rule with detailed ordinary-cycle results, but no wheel periodic census in the inspected full-text portions. Turau (arXiv:2202.01580 and arXiv:2312.13769) covers trees, not the wheel family. The closest previously stored majority census concerns the cubic prism, and a wheel anti-coordination equilibrium classification concerns a different update rule; neither implies the present wheel count. Public mathematical-record searches returned parity automata on other graphs and unrelated wheel invariants but no covering wheel-majority count. Keyword and implication checks cannot rule out an unindexed equivalent.

## Value

**PASS.** Adding one universal hub to a cycle changes the deterministic majority network from a topology allowing many nonconsensus fixed states to one with exactly two fixed points, yet retains an explicitly countable, exponentially large family of genuine oscillating attractors. The exact coefficient formula counts *all* periodic states for a natural 3-connected, high-degree-heterogeneous social graph using polynomially many arithmetic operations, rather than an exponential state sweep. The parity-dependent constant-hub subfamily and the independent hub-switching class give structural explanations beyond a raw enumeration.

## Verification and limits

The extracted `verify.py` has 27 polynomial-versus-transfer checks, 13 complete-state comparisons over \(3\le n\le15\), and exact integer audits through \(n=60\). No basin-size or stabilization-time claim is made. Unindexed prior art and the absence of independent expert validation remain limitations.

Self-review: passed. Independent audit: not yet performed.
