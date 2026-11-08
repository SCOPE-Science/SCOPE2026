# Scientific review: priced antipodal shortcuts on even cycles

## Correctness — PASS

The proof identifies a spectral-gap upper bound for *every* independent conductance allocation by averaging two real Fourier Rayleigh quotients at each of frequencies one and two. A uniform allocation attains both supporting bounds where they are active, and a two-line scalar maximization gives the exact threshold and allocation segment. Equality in the first-frequency positive-semidefinite inequality implies two genuine eigenvector equations; their imaginary and real parts force, respectively, all cycle conductances and all antipodal conductances to agree. This directly proves the claimed classification of all optimizers. Exact formulas imply the stated large-size limits. The executable verifier reproduces 641 finite checks, which supplement but do not replace the universal proof.

## Originality — PASS on inspected evidence, with residual risk

Sun–Boyd–Xiao–Diaconis (2006, DOI 10.1137/S0036144504443821) prove the general continuous-time priced-edge optimization framework and treat cycles without antipodal chords. Boyd–Diaconis–Parrilo–Xiao (2009, DOI 10.1137/070689413) analyze discrete-time stochastic fastest mixing by symmetry; the inspected cycle, wheel and multipartite sections do not imply the present priced continuous-time formulas. Shakeri et al. (arXiv:1510.06785) hold layer Laplacians fixed and allocate only interlayer links, a different feasible problem. The known six-vertex priced-matching classification on \(K_{3,3}\) is not claimed as new; the present theorem starts at \(m=4\). Related priced-wheel and exceptional-single-cycle-edge results have different graph families and constraints.

The fixed-price, vanishing-shortcut-budget fourfold improvement is not supplied by the inspected published statements. This is best-knowledge originality, not a proof of absolute publication priority; an undiscovered equivalent circulant-graph optimization may exist.

## Value — PASS

The graph is a natural sparse ring augmented by maximally long localizable shortcuts. Deciding whether such shortcuts merit funding is directly motivated by diffusion and spectral network design. The theorem supplies the entire unconstrained optimizer locus, a sharp support and nonuniqueness transition, a price threshold growing quadratically with network size, and the counterintuitive fourfold mixing-rate gain achievable with a diminishing \(O(m^{-2})\) budget fraction. The result is a meaningful graph-family classification rather than a single-case numerical table or a straightforward substitution into a fixed-weight spectrum.

## Limits and closest comparisons

The proof does not cover heterogeneous edge prices within each orbit, arbitrary shortcut placements, or discrete-time stochastic normalization. The special six-vertex case is excluded. The 2006 and 2009 primary PDFs and the full-text 2015 arXiv representation were inspected in the relevant sections, with explicit search terms for the closest graph aliases; unindexed equivalent literature remains the main residual novelty risk. Independent audit has not been undertaken.

Self-review: passed. Independent audit: not yet performed.
