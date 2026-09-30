# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The derivation was checked from the multivariate folded-normal density rather than inferred from moment inequalities. The likelihood ratio relative to the independent half-normal product is the uniform sign average of Gaussian likelihood ratios. Expanding its \(L^2\) norm reduces the problem to Gaussian cross-integrals. The cross-integral matrix is
\[
R^{-1}+D_sR^{-1}D_s-I,
\]
and the all-positive sign term is finite exactly when \(2R^{-1}-I\succ0\), equivalently \(\lambda_{\max}(R)<2\). That condition also makes every sign-conjugate cross-integral finite because each of the first two precision terms is then strictly larger than \(I/2\).

The determinant formula was checked against the bivariate reduction
\[
D_2=-\log(1-\rho^4),
\]
against direct numerical integration by Gaussian expectation for nonsymmetric three-dimensional examples, and against the explicit trivariate equicorrelation simplification. The data-processing lower bound and the comparison with the signed Gaussian follow from standard Rényi data processing and conditional Jensen, respectively.

Potential failure modes examined included a missing factor from folding to the positive orthant, counting of ordered sign pairs, the singular boundary \(\lambda_{\max}(R)=2\), and the possibility that mixed-sign cross terms remain finite outside the stated spectral region. The all-positive cross term rules out the last possibility, and singularity at equality makes its Lebesgue integral divergent.

## Originality

The immediate literature target is Ouimet and Greaves (2026), whose Corollary 4.11 gives a lower certificate for the same order-2 Rényi total correlation of Gaussian magnitudes using product moments; the paper explicitly notes that this avoids direct evaluation of the joint density ratio. The present result evaluates that ratio's \(L^2\) norm exactly and extracts a spectral finiteness boundary.

The multivariate folded-normal density itself is established prior art. Chakraborty and Chatterjee (2013), Liu et al. (2023), and Benko, Hübnerová and Witkovský (2025) were inspected for the density and distributional context. The latter two sources also document corrections and later developments in folded-normal theory. Searches for folded/absolute Gaussian Rényi divergence, Pearson or chi-square divergence, total correlation, determinant formulas, and equicorrelation thresholds did not locate the multivariate formula or the spectral phase transition stated here.

The bivariate identity is deliberately not claimed as a standalone discovery. Squaring the magnitudes converts the pair to a classical bivariate gamma/chi-square law, and Lancaster's canonical-expansion theory together with Griffiths' bivariate-gamma canonical correlations provides an older route to the same \(L^2\) quantity. The general Gaussian likelihood-ratio integral and Rényi data processing are also standard ingredients.

Residual originality risk remains in older multivariate Lancaster expansions and in work on Gaussian sign mixtures or folded multivariate distributions that may encode the same determinant average under different terminology. No inspected source states the exact \(2^n\)-term formula, the equivalence \(D_2<\infty\iff\lambda_{\max}(R)<2\), or the equicorrelated phenomenon in which all pairwise magnitude divergences stay finite while the joint order-2 total correlation is infinite. The originality assessment is therefore to the best of our knowledge.

## Value

The result resolves a concrete quantity that a very recent Gaussian-product paper could only lower-bound, and it identifies a qualitative phenomenon invisible to pairwise dependence: an interior high-dimensional \(L^2\) blow-up despite finite bivariate magnitude dependence. The exact determinant representation also separates what is lost by discarding Gaussian signs from what is retained: folding strictly lowers finite Rényi-2 dependence unless the coordinates are independent, yet it leaves the spectral finiteness boundary unchanged.

## Limitations

The result concerns centered, standardized, nonsingular Gaussian vectors and Rényi order 2. The determinant sum has exponential sign complexity. It does not supply an efficient approximation scheme in large dimension, and it does not address nonzero means, singular laws, arbitrary Rényi order, or general elliptical families. The external literature check cannot certify absence of an equivalent older formulation.
