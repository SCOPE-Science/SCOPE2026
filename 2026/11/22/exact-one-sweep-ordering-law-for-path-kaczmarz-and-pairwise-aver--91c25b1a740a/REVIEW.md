# Independent mathematical audit

## correctness

PASS

Independently reconstruct the sweep by letting U have columns equal to the chronologically ordered unit contact differences, and G=UᵀU=I+D+Dᵀ with D strictly lower triangular. The successive scalar residuals z obey (I+D)z=Uᵀx. Each projection loses exactly its squared scalar residual. Summing over a basis gives total squared Frobenius loss tr(BGBᵀ)=tr(B+Bᵀ−BBᵀ)=2m−||B||_F², with B=(I+D)^−1 and m=n−1. The constant vector is fixed, hence E=||B||_F²−m. In the finite expansion B=I−D+D²−⋯, off-diagonal entries correspond to directed paths in the oriented line of edge contacts. Distinct contacts at distance k on this line have a unique such route when all k intervening bits agree, and the coefficient is 2^−k; otherwise it is zero. Thus a run of length ℓ contributes sum over k=1,…,ℓ of (ℓ−k+1)4^−k, exactly the frozen run sum. Singleton runs minimize since S₁=1/4 and S_k>S₁ for k>1. The run cost is strictly superadditive since S_k is strictly increasing, so one constant run maximizes. All orientations are feasible (the line has no directed cycle); every alternating word is the matching red–black precedence class, whose linear extensions are linked by swaps of disjoint projections, whereas the constant words force literal monotone orders. Geometric summation recovers both extrema and the limit 4/3. At n=2 the loss is zero and at n=3 both orders give 1/4. Independent replay: python3 /workspace/evidence/path_sweeps.py tests every permutation for 2≤n≤8 with dyadic integer matrices against directed path counts, including both extrema. Normalization: the claimed expectation is for the stated mean-zero covariance I−J; E sums squared losses over a unit orthonormal basis of disagreement. A literal arithmetic average over those unscaled basis vectors would be E/(n−1), not E. The explicitly defined objective and extrema are unchanged by this clarification of loose basis-average wording.

## originality

PASS

The supported distinct claim is the exact all-permutation, all-path-length run law with sharp errors, including the worst case and equality classes. Related deterministic contact operations and the separately mentioned equal-strength optimum are not counted as independent originality. No read comparison contains a complete equivalent or dominating law; the optimizer announcement and inaccessible projection-ordering papers leave qualified priority risk.

## value

PASS

The exact error can be obtained from path precedences without matrix products and gives complete schedule comparisons under a natural, fixed one-contact budget and isotropic initial error. It identifies precisely which monotone runs worsen loss and quantifies the sharp asymptotic 4/3 squared-error penalty. This is not a claim about worst-direction error, nonpath graphs, or repeated sweeps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
