# Independent mathematical audit

## correctness

PASS

For an invariant compactly supported history measure and any \(C^1\) cylinder \(H(X_0)\), differentiating invariance gives \(\mathbb E[H'(X_0)(-\gamma X_0+\beta f(X_{-\tau}))]=0\). Since \(H'\) may be any continuous test function on the compact one-time range, this is exactly the displayed conditional regression. Time-shift invariance equates the delayed and current marginals. Writing \(V=\beta f(X_{-\tau})-\gamma X_0\), the regression gives \(\mathbb E[V\mid X_0]=0\), so the cross term vanishes and yields the variance-defect identity. If the defect is zero, invariance plus continuity forces trajectories in the support to be constant. The Lipschitz variance bound \(\operatorname{Var}(f(X))\le L^2\operatorname{Var}(X)\) then gives \(\beta L>\gamma\) for any non-equilibrium stationary state. Fresh root solving reproduces \(0.7356331448588915\), \(0.8457944676553084\), and \(1.3248837608752875\).

## originality

FAIL

The load-bearing regression is a direct specialization of the standard invariant-measure generator identity: invariance of a semiflow gives \(\int L\Phi\,d\mu=0\) for every differentiable observable in the generator domain. Applying it to the one-dimensional cylinder \(H(X_0)\) immediately yields the conditional zero-drift statement for any scalar deterministic delay equation, not specifically Mackey–Glass. Equal delayed/current marginals are likewise immediate from shift invariance. The variance identity and support-slope obstruction then follow by elementary orthogonality and the standard Lipschitz variance inequality. The model-specific primary literature confirms the same continuous-history semiflow, so no nonstandard Mackey–Glass mechanism is needed.

## value

FAIL

The stationary identities are interpretable and the numerical slope windows are correct, but the entire mechanism is a routine cylinder-observable application of invariance followed by elementary variance algebra and a Lipschitz bound. The model specialization does not add a new structural lemma or difficult boundary beyond that generic theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
