# Scientific assessment: trajectory budget for quadratic-value identification

## Correctness — PASS

The observation map in modal coordinates has basis columns \(\big((\lambda_i\lambda_j)^t z_i^{(k)}z_j^{(k)}\big)_{k,t}\); its time grouping gives the universal upper rank bound. The explicitly constructed starts \(z_i^{(k)}=(2^{2^{i-1}})^k\) make the within-product blocks ordinary Vandermonde matrices on pairwise distinct nodes. Distinct product classes separate by the temporal Vandermonde matrix once the observation horizon is at least their count. Rank and minimum trajectory count follow without a genericity assumption. Genericity follows from a nonzero maximal minor; positive-definite ambiguity follows by a small symmetric kernel perturbation. The stable-geometric example follows by an exhaustive symbolic pair-count argument. The packaged script independently checks 643 finite-field ranks but is not an infinite proof.

## Originality — PASS, with residual risk

Baltussen et al. (2026) explicitly require full rank for the quadratic-value least-squares regression and suggest extra initial conditions; they do not calculate the minimum. Zhou (2016) gives the largest-eigenspace-multiplicity output-count result for **unrestricted** linear sensors on a lifted system, which captures the necessity, but does not establish sufficiency when every output is the symmetric rank-one tensor of an actual trajectory start. The simultaneous structured Vandermonde construction and exact rank at every trajectory count distinguish the claim. Van Waarde et al. (2020) treat input-driven collective excitation, not this restricted autonomous quadratic regression. Gosea and Gugercin (2022) treat frequency-domain quadratic-output model interpolation, Berkane et al. (2023) state observation with known quadratic-output matrices, and Tu and Recht (2018) include stochastic excitation. A generic lifted observability theorem combined with an unindexed structured-sensor construction could subsume this result and remains a literature risk; no independence is claimed.

## Value — PASS

The recent terminal-value fitting proposal requires a full quadratic-regression matrix but leaves the required initial-condition budget unspecified. This result provides an exact finite experiment-design invariant (product-multiplicity), identifies a distinct-eigenvalue class where arbitrarily long single trajectories provably fail, and gives an explicit constructive way to remove that failure. Such a classification affects how deterministic data collection is planned rather than merely improving a constant in a generic rank bound.

## Scope and risks

The theorem assumes a known fixed real-diagonalizable transition and exact quadratic measurements, at least as many time samples per trajectory as distinct spectral products, and unrestricted start states. Explicit starts may be very ill-conditioned; constraints on starts or shorter horizons are not classified. No claim is made about numerical precision, statistical robustness, or full nonlinear MPC performance. The lower-bound connection to unrestricted lifted observability is prior art; structural sufficiency is the assessed contribution. An unknown unindexed equivalence is possible.

Self-review: passed. Independent audit: not yet performed.
