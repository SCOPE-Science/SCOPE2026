# Independent mathematical audit

## correctness

PASS

Independently reconstructed the Lévy and regression assertions in RESULT.md lines 74–146. Under the basic Thorin conditions the gamma ray (v/λ,v/λ²) has integrable (1∧‖jump‖²) and (1∧y): for |λ|≥1 the bounds are constants times λ^−2 after integrating v, and for small |λ| splitting at v=λ² and 1 gives O(1+|log |λ||). An equivalent direct construction is to leave Poisson jumps at |λ|≤1 uncompensated, compensate the first-coordinate sum at |λ|>1 in L², and add the integrable deterministic large-rate correction (1/λ−λ/(1+λ²)) against U. The second-coordinate sum is finite almost surely and uncompensated; the Gaussian part is (N(0,σ²),σ²) with covariance diag(σ²,0). Frullani's integral then gives the joint exponent of the frozen transform; principal logs agree because the two gamma factors have opposite-signed arguments and their product has positive real part. The transform fixes the HBB law. The inverse ray coordinates are (λ,v)=(z/y,z²/y); a fixed v-shell recovers U even for infinite measure, the Jacobian times v^−1 is y^−2, and the thresholds are the displayed maxima. For regression the extra inverse-rate integrability gives finite first moments, and tilted expectations yield ∫λ/(λ²+q)dU and ∫1/(λ²+q)dU. Their vanishing as q→∞ fixes the shifted intercept d. The remaining Stieltjes transform is that of the pushforward of (λ−b)U, understood as a locally finite signed density with integrable total variation against (1+t)^−1. Writing the Stieltjes kernel as a Laplace integral gives injectivity by two Laplace uniqueness steps (the exponentially tilted measures are finite); the finite signed conditional-mean measure then vanishes by one more Laplace uniqueness step. Radon–Nikodym weights give all balances and one-sided single-magnitude rigidity, with arbitrary slope only in the zero-spectrum case. Nonzero U puts mass off both axes, precluding independence of the ID coordinates. For one sign, bounded Borel association can be justified by conditioning on increasing finite-intensity windows of the Poisson configuration, and on the independent Gaussian variable: conditional expectations of bounded increasing observables increase with added jumps in each window, because the remaining increment and the deterministic compensations do not depend on that window's points. Poisson association and martingale convergence prove the inequality without any moments. The first-moment tilted ratios were also checked at three rational Laplace arguments for balanced and unbalanced two-magnitude examples (replay `OPENBLAS_NUM_THREADS=1 python /tmp/opencode/frozen-review-diagnostics.py`, check 1). The frozen checker was inspected but not executed; neither checker establishes the arbitrary-measure claims on its own.

## originality

PASS

The canonical law, single signed gamma coupling, unsigned marginal and mixed-cumulant formula are directly prior. The joint gamma-ray geometry is a natural extension within the prior multivariate Thorin framework and should not be described as a general representation advance. The exact necessary-and-sufficient ratewise balance under absolute first-moment integrability, with converse, one-sided rigidity and genuinely asymmetric continuous examples, is the supported distinct claim. In particular the inspected cumulant and polar-representation theorems do not give that conditional-mean equivalence.

## value

PASS

Affine prediction of the signed coordinate from the canonical latent scale is a natural classification question. A mere marginal transform or a few cumulants do not tell whether it holds under first-moment assumptions; an exact necessary-and-sufficient condition yields the contrast between one-sided single-rate rigidity and asymmetric continuous two-sided freedom. The jump map also gives a precise account of where the sign information discarded by the marginal is retained.

The dated certificate retains the supplied scientific assessment, sources and limitations.
