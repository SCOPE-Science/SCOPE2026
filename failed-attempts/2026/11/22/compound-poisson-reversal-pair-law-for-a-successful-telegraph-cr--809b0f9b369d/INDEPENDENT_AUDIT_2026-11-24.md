# Independent mathematical audit

## correctness

PASS

Success at the right endpoint requires positive final velocity and hence even parity from the inward positive start. In rate-scaled length, first-flight conditioning gives the marked backward equations; eliminating the minus component yields f_+''=(1−z²)f_+, f_+'(0)=f_+(0), f_+(c)=1. Thus the marked boundary value is 1/F_c(1−z²), in particular 1/(1+c) at z=1. Absorption occurs almost surely because at each flight the chance of an exit without another reversal is at least e^(−c). The entire function F_c(s) is the value at c of the scalar solution with u(0)=u'(0)=1; at a zero, integration by parts gives −s=(∫|u'|²+|u(0)|²)/∫|u|²>0. With ξ=c√(−s) the root equation is tan ξ=−ξ/c, one simple root in each stated half-period, none at zero. Growth at most exp(O(√|s|)) and ∑ξ_n^(−2)<∞ justify the normalized genus-zero product, with no exponential linear factor. Its ratios give the stated geometrics; the sum of their means is finite. The absolutely convergent log series gives the positive Lévy masses and rate −log H_c(0); F_c(1)=e^c. Independently expanding the two coefficients at s=0 gives Var(M)=A+A²−2B for A=F_c'(0)/F_c(0), B=F_c''(0)/(2F_c(0)); the factored expression and mean and variance scaling were checked by exact algebra. The supplied checker checks simulated success, mean and mass at zero, not simulated variance. At s>0 the Laplace limit follows by substituting q=e^(−s/c²), and at s=0 the transforms equal one. Euler's product and the convergent inverse squares and fourth powers give the independent-exponential law and its moments. These checks establish correctness without asserting physical-time or path convergence.

## originality

FAIL

A distinct indexed statement, 13632ddb5c13, gives the full marked right-exit transform for arbitrary interior launch position, with exactly the same outgoing boundary conditions and rate convention. At its continuous inward boundary value it gives the frozen PGF exactly. The remaining frozen formulas are routine consequences of that explicit transform, not merely information that is implicitly encoded in an arbitrary PGF: its displayed denominator is directly the scalar constant-coefficient Robin–Dirichlet characteristic function, with the usual order-below-one canonical product. Normalizing and substituting 1−q makes each linear factor a geometric PGF; taking its log immediately yields the compound-Poisson formula. Differentiation, evaluation at zero and substitution q=e^(−s/c²) give the moments, intensity and scaling limit. No new statement of the Robin representation was found verbatim in the other record; the failure is on mechanical implication of the entire frozen claim by the inspected broader transform plus standard identities, not an allegation of historical priority, nor based on failure to retrieve older literature.

## value

FAIL

The stopping model is natural and the geometric representation is a useful interpretation, but the submission does not establish a further worthwhile mathematical gap after the already available explicit full exit-count transform. The boundary specialization, constant-coefficient Robin characteristic product and elementary logarithmic expansion supply the exact candidate invariant without an additional structural or analytical step beyond standard tools. The other exact moments and limiting transform likewise follow directly; the frozen claim does not give a pathwise decomposition, new estimate, or different boundary model that would survive as a distinct motivated result under the narrow-invariant standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
