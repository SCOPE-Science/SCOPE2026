# Independent mathematical audit

## correctness

PASS

Choose smooth even compact cutoff χ=1 on [-2,2], 0 outside [-3,3], c(x)=∫0^xχ(u)du, f0=0,f1=2∫0^xc(u)du. Gradients g0=0,g1=2c are globally bounded, all derivatives bounded, and sample losses globally Lipschitz C∞. For shared-sample two-stage stochastic Heun starting X0=1 with h=1/n, all predictors/states remain [0,1], where c=x. Sample0 update multiplier 1, sample1 multiplier 1−2h+2h², so E X_n=(1−h+h²)^n=e^-1(1+1/(2n)+O(n^-2)). The authors' noise-only target dZ=−c(Z)dt+√h|c(Z)|dW, started at 1, matches geometric Brownian dG=−Gdt+√hGdW unless an exponentially rare escape above 2; exponential reflection bound and uniform second moments prove E Z_1=e^-1+O(exp(−C/h)). Hence lim n(E X_n−E Z_1)=1/(2e). General one-step mean mismatch is h²/2 Cov(g_gamma'(x),g_gamma(x)), nonzero at x=1; ordinary local weak error O(h²) yields global order 1 against the asserted target, not claimed alternative modified equations. Independently evaluated exact multipliers and scaled errors at increasing n, tending to 1/(2e). Source original equations (5), (6) and Theorem1 were read in accessible complete HTML version and checked for same-stage sampling.

## originality

PASS

The original 2020 Ayadi–Turinici theorem asserts weak order two relative to its uncorrected stochastic modified SDE and is the target of a mathematically explicit counterexample, not a prior refutation. Earlier stochastic modified equation frameworks (Li–Tai–E) and other Runge–Kutta methods do not state the globally smooth, globally Lipschitz shared-sample two-point example or its exact 1/(2e) global first-order bias. Resultary semantic queries did not find equivalent preexisting rebuttal. This is a best-of-knowledge originality PASS with literature risk.

## value

PASS

A precise failure of an explicit published weak-order-two guarantee under the method's own same-sample protocol is a motivated negative correctness boundary. The smooth globally Lipschitz data remove a possible regularity loophole; exact positive global bias identifies the missing covariance correction and matters to researchers choosing an appropriate stochastic modified equation. It does not overclaim convergence failures for unrelated adaptive optimizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
