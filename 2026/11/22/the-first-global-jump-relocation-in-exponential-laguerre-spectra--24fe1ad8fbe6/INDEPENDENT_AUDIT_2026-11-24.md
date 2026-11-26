# Independent mathematical audit

## correctness

PASS

For ordinary variation on the open half-line understood as |Df| mass, a bounded representative equals a constant plus the signed Stieltjes integral of right-tail steps almost everywhere. The projection residual annihilates constants; the triangle inequality bounds it by the integral of the step norms against |Df|. A maximizing step attains the bound, and equality forces concentration of |Df| on the maximizing locations, so a unique location gives exactly the claimed nonconstant extremizers. Orthonormality, the integral of e^(-x)L_k(x) over [t,infinity), and subtraction of the first n+1 squared coefficients give R_n(t)=e^(-t)-e^(-2t)B_n(t). It is positive inside since a step cannot agree with a polynomial almost everywhere, and tends to zero at both ends. Differentiating gives R_n'=e^(-t)(2e^(-t)Q_n-1). The independent replay constructs B_n,Q_n over rationals, isolates and exhausts the positive roots of Q_n'-Q_n by Sturm sequences, and uses exact exponential intervals to count the stationary roots between them and compare their residuals. Counts are (1,1,1,3,3,3); the unique winners are root 1 through degree 4 and root 3 at degree 5, whose squared margin over root 1 exceeds 0.0000521944. Distinct successive maximizing locations and the pointwise nesting inequality also give strict decrease of the sharp norms over these degrees. Replay: python3 /workspace/branches/844146e3-8c0c-49b0-9eef-00e14b2d01d7/audit_laguerre_independent.py; see audit-run.txt there. The frozen script was not executed. No higher-degree, other-weight, or complex-valued classification is checked.

## originality

PASS

Best-of-knowledge pass for the sharp continuous projection-residual classification and first branch relocation through degree five. The variation-to-step argument, classical Laguerre identities and sharp single-coefficient analysis are not claimed as new. The closest indexed coefficient record was compared by formula and objective.

## value

PASS

The exact norm for continuous polynomial projection of variation-bounded data is a natural approximation invariant, and the optimizer geometry matters independently of the size of the norm. The degree-five switch disproves selecting the first stationary jump even within a short natural nested family, and certifies why a close numerical comparison has a strictly different winner. Proving the first switch and identifying all extremizers through it is useful finite structural information, not significance inferred from a tiny improvement in error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
