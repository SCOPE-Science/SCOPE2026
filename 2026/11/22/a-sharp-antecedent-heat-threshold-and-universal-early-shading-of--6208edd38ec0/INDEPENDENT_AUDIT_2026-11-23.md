# Independent mathematical audit

## correctness

PASS

An independent derivation uses the causal response K(u)=(1−e^{−u}) for u≥0 and 0 otherwise: the unshaded solution is reduced by ρ[K(t−s)−K(t−s−d)]. Continuity at the switches eliminates moving-boundary contributions. With k=m−1, q=e^{−s}, r=C/q, integrating 2x_s∂_s x_s gives Q'=ρ(1−b)[kq+2r+(bkq−ρ(1−b))r²], exactly ρ(1−b)P(q)/q². At q=C, the bracket in P(C)/C² is ≥(1+b)(1−C)>0; P(1)=(1+bC²)(m−mcrit). For m≥1 P>0 on [C,1]. For m<1, P(0)<0, P(C)>0, P tends to −∞, and strict concavity on q>0 gives one root below C and one above. Only the latter can be interior, precisely for m<mcrit; reversing q with s proves the strict decrease-then-increase pattern. Equality at mcrit leaves Q'(s)>0 for every positive feasible s. At q=√C, the given factorization has the strictly positive term (1−√C)(1+b√C), so the optimum precedes the midpoint of [0,H−d]. The larger root has P_q<0, P_m>0, P_ρ<0, giving the stated opposite signs for the optimizer's two dependencies. For fixed m<1, d and ρ, writing ε=√C and q=εz gives k z³+(2+bkε²)z−ρ(1−b)ε=0; its positive root at ε=0 has derivative −4 in z and continues to a physical root q∈(C,1). Taking −log proves the offset and the claimed error. Separate bisection and integration of the squared trajectory reproduce s*=1.18468780635247 and costs 1.29629488655589 and 1.59833476064739. The frozen verify.py was inspected but not executed; the finite diagnostics are not the proof, and its self-comparison of cubic(1,...) is not an endpoint test.

## originality

PASS

Empirical timed-shading studies motivate the model, and first-order pulse placement and greenhouse control are relevant comparisons. The retrieved evidence does not yield the exact one-block quadratic optimizer, threshold and asymptotic shift. This is a bounded priority assessment, with the closest unavailable methods and older control literature expressly unresolved.

## value

PASS

A fixed-duration, fixed-depth window has identical removed forcing at each placement, so the objective isolates thermal memory in a natural baseline model. The exact threshold predicts the qualitative policy switch with antecedent heat; the two interior parameter effects and the shade-independent leading long-day advance are useful checks on numerical or richer models. The criterion is cumulative squared normalized heat under constant forcing, not yield, crop adaptation, variable irradiance or unrestricted optimal control.

The dated certificate retains the supplied scientific assessment, sources and limitations.
