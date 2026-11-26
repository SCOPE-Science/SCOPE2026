# Independent mathematical audit

## correctness

FAIL

The target in RESULT.md line 5 is J=integral_0^1 X(t) dt, whereas lines 36–40 use the Itô kernel for X(1)=integral_0^1 B(t) dt. Stochastic Fubini gives J=integral_0^1 (1-u)^2/2 dB(u), variance 1/20, and covariances with (X(z),B(z)) equal to (z^2(6-4z+z^2)/24, z(3-3z+z^2)/6). The observation covariance K is as given, but the target covariance is not. Thus both the risk and the optimizing design fail, not merely a normalization of the displayed risk. For P=10 the claimed optimal risk 1/14 exceeds the risk 1/20 of ignoring all data. For an exact design counterexample at that budget, both designs use z=1, where the true c=(1/8,1/6). The proposed (p,q)=(8,2) yields reduction c^T(K+diag(1/8,1/2))^(-1)c=53/1512, whereas (p,q)=(10,0) yields (1/8)^2/(1/3+1/10)=15/416, an improvement of 79/78624. Separately, even noiseless observations leave residual risk at least z^5/720+(1-z)^5/20: the quadratic part on [0,z] cannot be represented by an affine function, and the tail is unobserved. The minimum of this bound on [0,1] is positive, unlike the claimed limit. The source checker fixes the wrong c at line 13 and integrates f=1-xx at lines 54–60, so its reported PASS in VERIFICATION.md does not address this discrepancy. Inspected but did not run check.py. No repaired theorem for the stated target is claimed.

## originality

PASS

This is a statement-level coverage judgment, not validation of the asserted switch. The exact one-site independently noisy X and B design with shared precision for J=integral X is distinct from the inspected single-channel law for that J, from a two-channel Matérn case, and from Brownian-value designs for integral B. No dominating result for the full model and law was found in the bounded checks; the target confusion is a correctness failure, not evidence that the claimed law is known.

## value

FAIL

The measurement-budget question is worthwhile, but the delivered result supplies no sharp law for that question: its central risk formula and optimal allocation are false for the advertised integrated-Wiener functional. The surviving fixed-design Gaussian reduction after correcting c and the coefficient-to-precision Cauchy–Schwarz rule are standard. A switch theorem for X(1) would instead concern prediction of a terminal path value (equivalently the integral of B), and substituting that different target is not an established result about integration of X. No separate repaired finding is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
