# Independent mathematical audit

## correctness

PASS

The stationary promoter covariance is p(1−p)e^(−s|t|). Conditional on its path, the stationary count is driven by a Poisson immigration process with survival e^(−δu); the conditional mean is the stable exponential convolution of kG. At two times the covariance is the mean shared-survivor term nbar e^(−δ|t|) plus the covariance of those conditional means. This yields the stated positive continuous spectrum and V=nbar+c/δ; solving γ′=−δγ+c e^(−st) for t≥0 gives the stated two-exponential or confluent lag. Sampling aliases a strictly positive spectrum, and independent observation noise adds a constant. The periodized covariance is its evaluation at the Fourier grid, so both the circulant and the original finite Toeplitz block are strictly positive even when an exponential coefficient is negative and σ=0. The geometric wrap gives the explicit two-column correction for each exponential. Four distinct bases give independent columns by the first four Vandermonde rows; at resonance differentiation adds the two polynomial times exponential columns and the first four confluent rows are independent. The two exchange blocks in the distinct case are invertible unless A=0 (B never vanishes); in the resonant case the cross-block determinant is −K² before scaling, so the four-column form is nonsingular. A=0 requires δ>s and k=(δ²−s²)/(s(1−p)), in particular the stated example. With full column rank, UHUᵀ has exactly the rank of H. The real Gaussian determinant/solve formulas apply to the covariance-matched surrogate and cost O(m log m); they do not give the true count likelihood or treat conjugate Fourier bins as independent circular Gaussians. Independent reproduction: python3 /workspace/checks/2.py (SymPy), output /workspace/checks/2.out. Exact entrywise periodization and ranks 4,2,4 were checked at m=4,5,8, including distinct and exceptional examples at actual model rates and a rational confluent kernel. Geometric phase summation by signed lag independently gives the illustrative relative cross-bin covariance 0.0053053655796. The frozen checker was inspected, not executed.

## originality

PASS

Restricted to the explicit exact modally resolved covariance correction for the stationary telegraph model at all the stated rates: the exact rank and positive periodized baseline, with cancellation and the confluent equal-rate case. Neither Fourier/Whittle correction, the one-mode boundary identity, nor exact or fast Gaussian surrogate likelihood in itself is original. Exact prior finite-window Whittle identities and exact ranks for pure autoregressions are substantial overlap; their rank theorem does not cover this entire covariance family, including arbitrary additive noise. The general exact identity does not state a sharp rank or an explicit finite correction for the two-exponential/confluent mixture. In the inspected model and Fourier references there was no stronger rank theorem mechanically providing the full classification. This assessment is bounded, not a priority guarantee.

## value

PASS

The motivating procedure uses a diagonal covariance on a Fourier grid. The exact finite-window correction identifies a concrete off-diagonal effect that persists at the equal relaxation rates used in the numerical example, quantifies its dimension independent of sample count, and specifies when one lag mode and only its corresponding rank pair disappear. That exact finite-frequency information is useful in its own right; evaluating a Gaussian surrogate by an FFT and a small solve is a use of the structure, not a claim of a speed record against Kalman filtering or improved inference for the non-Gaussian transcription data. The result does not address transient initialization or numerical stability arbitrarily near resonance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
