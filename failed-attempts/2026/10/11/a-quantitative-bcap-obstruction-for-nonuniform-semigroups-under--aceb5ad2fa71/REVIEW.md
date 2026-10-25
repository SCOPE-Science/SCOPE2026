# Independent mathematical audit

## correctness

PASS

For L=limsup_{t↓0}||T(t)||, strong continuity and uniform boundedness give 1<=L<infinity. For every c>L one can choose delta with ||T(t)||<=c for 0<=t<=delta and use t=n delta+r to obtain ||T(t)||<=c exp((log c)t/delta). An unbounded generator A has dense proper domain D(A); each right resolvent is injective with this dense nonclosed range, hence not Fredholm. Atkinson plus fixed uniform Calkin exponent m implies compactness of J_lambda^m, J_lambda=lambda R(lambda,A). These operators converge strongly to I, hence uniformly on compact subsets when their norms are uniformly bounded. The package estimates ||J_lambda||<=c lambda/(lambda-omega), yielding beta_K(X)<=c^m as lambda→∞ and then <=L^m. The norm-jump inequalities follow from ||T(t)-I||>=||T(t)||-1. No use of numerical experiments or unjustified extrapolation. Crucially, the same hypotheses admit a stronger standard estimate ||J_lambda^m||<=c(lambda/(lambda-omega))^m via m-fold Laplace convolution; this does not invalidate the weaker asserted bound but defeats originality/value.

## originality

FAIL

The claimed inequality is a directly dominated consequence of the focal Calkin/Yosida compact-power argument plus the classical Hille–Yosida estimate for *powers* of the resolvent. In fact, for any c>L and ||T(t)||<=c exp(omega t), the Gamma convolution identity gives ||J_lambda^m||<=c[lambda/(lambda-omega)]^m, not merely ||J_lambda||^m<=c^m[lambda/(lambda-omega)]^m. Thus beta_K(X)<=L, which implies the submitted beta_K(X)<=L^m for L>=1. The same standard arguments yield the stronger norm jump L-1>=beta_K(X)-1. Retaining the weaker factor c^m is not an original independent obstruction, whether or not the stronger conclusion was displayed in exactly this notation in the focal paper. The focal arXiv main body was not independently accessible in this run, so no fabricated assertion is made about every sentence of its full text.

## value

FAIL

The BCAP coefficient and initial semigroup norm are natural Banach-space invariants, so a genuinely informative sharp comparison could be valuable. This specific exponent-m bound is, however, an avoidably weaker one-line corollary: under exactly the same hypotheses the classical resolvent-power estimate immediately gives beta_K(X)<=L, independent of m, and hence a stronger norm jump beta_K(X)-1. No boundary attainment, independent sharp m-exponent phenomenon, or model application motivates retaining the poorer m-dependent estimate. The submitted quantitative gain is a routine, dominated norm-accounting variant of the focal proof rather than a mathematically needed separate obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
