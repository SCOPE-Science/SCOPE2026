# Independent mathematical audit

## correctness

PASS

Checked the exact stable domain and inspected the proof, verification note and rational Lyapunov checker without executing the uploaded code. In each orthogonal mode the AR polynomial z^2-az+b has a=(1+eta)t, b=eta t; 1-b>0, 1-a+b=1-t>0 and 1+a+b=1+(1+2eta)t>0 ensure Schur stability. As an independent variance calculation, let y_n be the causal stationary unit-white-noise AR(2) with the same a,b. By commuting linear time-invariant filters, x_n=sigma(c0 y_n+c1 y_(n-1)); its causal limit is independent of deterministic initialization. The white-process Yule–Walker equations give gamma1=a gamma0/(1+b) and gamma0=(1+b)/[(1-b)((1+b)^2-a^2)]. Thus Var(x_n)=sigma^2 gamma0 (c0^2+c1^2+2a c0 c1/(1+b)), reproducing the normalized formula, including its noise cross term. Independent modal innovations imply a joint centered Gaussian whose covariance suffices for the exact position law, not for exact time-lag statistics. Calibration equates an affine numerator to the strictly concave D_eta at two points; its line has K,G as stated. Real taps require K>0 and -1<=G/K<=1+2eta. K+G>2(1-eta^2)>0 follows from t_-+t_+-t_-t_+<1, and (1+2eta)K-G is eta times the product of the two stated positive linear factors. Both inequalities are strict; sum/difference square roots realize the desired taps, and overall sign reversal preserves them. For one mode one can instead take c1=0 and c0^2=alpha D_eta(t)/(sigma^2(1+eta t)). The residual is exactly q(t-t_-)(t-t_+)/D_eta(t); the affine-in-t numerator cannot agree with a nonzero quadratic at three distinct t values. The zero-momentum case is checked directly and excluded from the new claim. The rational example has normalized midpoint variance 826/851, as stated. The finite verification is supplemental, not a stability or arbitrary-dimension proof.

## originality

PASS

Pass the positive-momentum noise-only calibration theorem for the fixed recurrence: uniform feasibility for arbitrary two modes with a real common tap pair, sharp obstruction at three and signed position-variance bias. The white-noise modal variance for this same Nesterov recurrence is prior art, as are two-tap colored noise at zero momentum, general ARMA moment algebra and exact harmonic samplers in other method classes. These provide tools and boundary cases, not the specific simultaneous attainability classification with the common-tap constraints.

## value

PASS

For an inexpensive unadjusted quadratic sampler that keeps the deterministic extrapolation rule and uses one fresh Gaussian per step, it matters whether noise alone can remove stationary bias. The theorem gives a guaranteed realizable two-curvature design, a sharp obstruction even with arbitrary real common taps at a third curvature, and the exact sign of what goes wrong between and beyond calibrated modes. This is a meaningful design boundary, not just a stationary variance calculation or a claim of general superiority to exact harmonic integrators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
