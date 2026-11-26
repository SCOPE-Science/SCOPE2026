# Independent mathematical audit

## correctness

PASS

The fair creation bits can be recovered by ordering the uniform weights by increasing distance to 1/2; the sign of the newest weight relative to 1/2 dominates all sums with earlier weights, and each sign is fair conditional on the distances. Ross's maximum tail excess is exactly the maximum of the reversed sign walk including time 0; for even n the matching deficiency differs from that maximum by at most one. Centering the weighted bit sum for the edges gives exactly minus one half the sum of the same walk's partial sums. Donsker and the sup/integral continuous mapping give the joint limit with the stated centering and sign. The normalized fourth moments are bounded by Doob and the independent weighted-sign moment formula, giving uniform integrability through second moments. Independently, let h(t)=t-t²/2. Then B−3hA is independent of A (joint Gaussian with zero cross-covariance and Var(A)=1/3); one-dimensional Gaussian integration by parts conditional on this residual identifies Cov(M,A) as E[h(T)]. The supremum derivative is h(T) by a.s. uniqueness of the argmax and is bounded; arcsine moments give 5/16. This gives -5/32 after the edge factor, and division by the two nonzero limiting variances in standard-deviation form gives the stated correlation. Conditional monotonicity in each bit gives nonpositive covariance with each bit; changing the last bit when all earlier bits are 1 gives strictly negative covariance even at n=2. VERIFICATION.md and verify.py were inspected, not executed. The finite graph enumeration does not certify the limit or its moments.

## originality

PASS

Pass for the unconditional joint limit for maximum-matching deficiency and the centred edge count in the same graph draw, and the resulting exact asymptotic covariance and correlation. The individual graph representations, matching formula and marginal limits are prior or standard; no standalone priority is assigned to Brownian maximum/area identities as such.

## value

PASS

Edge count and unmatched-vertex count are natural graph invariants measured on the same sample. The exact asymptotic dependence is substantial (correlation near -0.898) despite the very different limiting marginal shapes. The common-walk representation explains the effect at the appropriate two scales and the strict finite-order sign connects it to the original model, not just to an abstract Brownian moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
