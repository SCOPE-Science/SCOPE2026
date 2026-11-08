# Scientific review

## Correctness — PASS

The objective is the second eigenvalue of an unnormalized weighted graph Laplacian with linear per-edge price. Its Rayleigh characterization proves concavity, so averaging over core automorphisms gives an actual unrestricted optimum with two uniform rates. Every spectral mode of the resulting block Laplacian is solved explicitly. A sharp AM–GM lower bound on the rate budget for a prescribed gap yields the closed-form optimum with unique equality conditions. For a sunlet, the two first Fourier eigenvectors are forced into the kernel of every optimizer's shifted Laplacian by an average-of-PSD-matrices argument. Their pendant equations force every spoke weight, while the imaginary part of their combined cycle equation forces every rim weight. The proof covers all real positive costs and all integer cycle orders at least three. Exact symbolic and finite numerical checks in `verify.py` passed; they do not establish the universal theorem independently.

## Originality — PASS on inspected evidence

The 2006 continuous-time fastest-mixing paper sets up the general SDP and solves the bare cycle, but the inspected examples omit priced one-leaf coronas. The 2007 Barik–Pati–Sarma source supplies unweighted corona eigenvalue transfer without an edge-investment optimum. The 2007 symmetry paper is explicitly about minimizing discrete-time SLEM, not maximizing a continuous-time weighted Laplacian gap subject to the same linear cost. The new full-cycle optimizer uniqueness is also not a consequence of merely averaging by automorphisms. Remaining risk: unindexed equivalent continuous-time corona formulas or an independently derived eigenvalue-budget duality may already exist.

## Value — PASS

A family-wide analytic budget law replaces a potentially high-dimensional semidefinite optimization with three core parameters and yields unique *unrestricted* conductances on sunlets. The formula supplies a quantitative resource-allocation principle: a vanishing \(\pi\sqrt c/m\) fraction of budget suffices for indispensable pendant connectivity while preserving the optimal leading diffusion scale. This is a structural control/optimization statement, not a numerical case or a new notation for an existing spectral formula.

## Closest literature and scope

Sun–Boyd–Xiao–Diaconis, SIAM Review 48 (2006), sections 1 and 5; Barik–Pati–Sarma, SIAM Journal on Discrete Mathematics 21 (2007), theorem 3.2 and corollary 3.5; Boyd–Diaconis–Parrilo–Xiao, arXiv:0709.0955, sections 1–3. The claim applies to continuous-time algebraic connectivity with priced individual rates; it does not assert an explicit description of all optimizers for arbitrary transitive cores, and it does not characterize discrete-time SLEM.

Self-review: passed. Independent audit: not yet performed.
