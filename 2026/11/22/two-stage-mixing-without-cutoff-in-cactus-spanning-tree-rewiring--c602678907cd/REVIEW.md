# Scientific review: two-stage cactus spanning-tree exchange mixing

## Correctness — PASS

Every spanning tree of a cactus is specified by one omitted edge per cycle. In the specified cut-first chain, the only possible nontrivial change is to swap the omitted and deleted edges of the same cycle; direct cut enumeration yields probability \(1/(2q_L)\) for each such coordinate change. Product-space diagonalization gives the exact finite spectral multiplicities. Independent continuous-time coordinate refreshes lead, at the explicitly centered time, to a Gaussian log-likelihood for the long cycles and an independent three-symbol likelihood. A spectral \(L^2\) estimate transfers the profile to discrete time. A separating statistic (the number of long coordinates retaining their original symbols) proves the macroscopic pre-transition total-variation lower bound. The remaining triangle gives the second exponential relaxation and the two mixing-time regimes. All inequalities, boundary restrictions, and quantifiers appear in `RESULT.md`. The standalone enumerator and lumped-chain checks pass 1,818 assertions; numerical checks are supporting evidence, not proof of limits.

## Originality — PASS, with historical-priority uncertainty

The dated foundational exchange enumeration of Mohamed (2014) describes an edge-promotion and minimal-partition algorithm, not the uniform cut-first walk. Russo–Teixeira–Francisco (2018) explicitly choose a host edge **first** and then delete an edge from the formed cycle, and their cactus results are mixing bounds for that other transition. Hora (1997) treats homogeneous Hamming graph walk profiles; the case of a simultaneously surviving three-symbol slow factor with an exponentially large growing-alphabet fast block is different. Chen–Kumagai (2017) develops general heterogeneous product-chain cutoff criteria, which establish background rather than the particular total-variation Gaussian–categorical profile and exact two-stage mixing constants here. Comparison with available relevant prior mathematical records did not identify the same statement or a stronger statement directly implying this full profile. Two additional published mathematical results were examined in full result statements: one gives independent minimum-spanning-tree weight-refresh changes on cacti, and the other optimizes fastest symmetric one-step mixing on heterogeneous clique products; neither analyzes the prescribed cut-first chain or its exact two-stage finite-time profile. An undiscovered stronger product-chain theorem could affect priority. The full PDF of Mohamed (2014) could not be obtained; the abstract and method description, not the full work, were compared. Independent priority audit has not occurred.

## Value — PASS

The phenomenon distinguishes collective equilibration of an exponentially large set of cycle choices from equilibration of a single slow local cycle. In a natural local rewiring algorithm for spanning trees, many fast degrees of freedom can give the visual appearance of a classical sharp cutoff while the actual total-variation distance settles at a nonzero plateau. The exact Gaussian–categorical crossover determines error tolerances for which the fast and slow mechanisms control the mixing time, a structural diagnostic for heterogeneous state-space exploration rather than an arbitrary finite computation.

## Closest literature and limitations

- A. Hora (1997), DOI: 10.2977/prims/1195145152 — exact homogeneous Hamming cutoff profiles, not this mixed law.
- G.-Y. Chen and T. Kumagai (2017), arXiv:1701.06665 — heterogeneous product-chain general criteria, including noncutoff examples; explicit formula not identified in the inspected material.
- L. M. S. Russo, A. S. Teixeira, A. P. Francisco (2018), DOI: 10.3390/a11040053 — insert-first spanning-tree chain and cactus-related coupling bounds.
- N. Mohamed (2014), arXiv:1407.0699, first posted July 2 — edge-exchange enumeration; accessible abstract only.

The precise graph family and exponential balance are required; no conclusion is asserted for all cactus graph sequences or all exchange chains. The singular mixing-tolerance boundary is intentionally left unresolved. No independent mathematical validation or publication-priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
