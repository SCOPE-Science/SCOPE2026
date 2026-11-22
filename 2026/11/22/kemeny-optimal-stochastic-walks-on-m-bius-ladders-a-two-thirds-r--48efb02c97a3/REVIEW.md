# Scientific review: Kemeny-optimal stochastic walks on Möbius ladders

## Correctness — PASS
The precisely defined zero-target Kemeny constant equals the trace inverse on the constant-vector complement. The full objective is strictly convex in the independent symmetric edge variables; rotation averaging, followed by removal of holding, reduces the *unrestricted* optimization to one scalar, not just a heuristic invariant family. An explicit Fourier calculation and Poisson-kernel identity give the exact objective. The derivative at zero is negative, the upper boundary diverges, and the second derivative is strictly positive, giving one positive rung root. Exact derivative inequalities locate the two small complete/complete-bipartite cases and the larger-size regime. Uniform asymptotic derivative convergence and monotone root bracketing establish the exponent and constant. The independently constructed exact rational matrix traces and the previously published unweighted table agree; 417 standalone assertions passed. Finite checks cannot by themselves prove the infinite theorem.

## Originality — PASS on the inspected record, qualified
The closest material is the general convex Kemeny framework of Patel–Agharkar–Bullo and the 2026 structure-preserving reversible perturbation study, the general graph-symmetry and fastest-mixing framework of Boyd and coauthors, the unweighted Möbius-ladder Kirchhoff index of Baigonakova–Mednykh, and two publicly available fastest-SLEM Möbius-ladder classifications. The published Kirchhoff index corresponds to a **fixed** unit-edge walk, not an optimization over independent probabilities; fastest SLEM minimizes a spectral maximum, rather than Kemeny's reciprocal spectral sum, and its edge allocation has different scaling. Explicit comparison of implications leaves the optimizing root, unrestricted uniqueness, and the sharp two-thirds law uncovered by those inspected claims. Unindexed weighted-circulant or Kemeny-specific sources remain priority risks; absence from search is not itself proof of novelty.

## Value — PASS
This is a natural complete classification on an infinite, highly symmetric network family, with a structurally surprising contrast between mixing-rate and mean-target-passage objectives. The exact rung law and the persistent 50% loss of the equal-edge walk are nontrivial parameter-design consequences. The result is not an arbitrary finite table or a reformulation of an existing unweighted invariant.

## Scope and independence
The theorem excludes directed chains, nonuniform stationary distributions and mixing-time prefactors. Self-review does not substitute for independent audit.

Self-review: passed. Independent audit: not yet performed.
