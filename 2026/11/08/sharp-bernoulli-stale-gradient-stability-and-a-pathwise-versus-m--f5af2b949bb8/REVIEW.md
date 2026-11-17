# Scientific review — corrected scope

## Correctness — PASS
For the fixed independent Bernoulli delay law with probability 1/4 and normalized stepsize 3/2, the two augmented-state matrices have induced norms 1/2 and 4 in the weighted maximum norm. Their law-of-large-numbers average log norm is -log(2)/4, establishing simultaneous almost-sure exponential decay for any deterministic starting pair. The independent exact covariance recurrence gives a rational second-moment generating function whose dominant positive pole corresponds to an eigenvalue in (1,9/8); the coefficient is nonzero and positive for initial pair (0,1). The two conclusions refer to the same sampled process and hence prove a genuine pathwise-versus-mean-square separation.

## Originality — PASS for corrected witness only; original broader claim covered
The original review included the sharp entire Bernoulli stale-gradient mean-square stability frontier as a new conclusion. A published November 2, 2026 result, *Exact quadratic energy and the sharp mean-square frontier for Bernoulli stale-gradient descent*, already proves the identical frontier and substantially strengthens it with an exact Lyapunov energy and noise floor. The frontier is no longer claimed as new. The retained theorem is the explicit almost-sure exponential contraction despite exponentially growing second moment. Earlier first-moment-versus-second-moment examples are not equivalent to almost-sure convergence. Standard general random-matrix Lyapunov/moment theory is acknowledged, and older specialized priority remains a risk.

## Scientific value — PASS
The corrected fixed numerical witness is a reusable, rigorously quantified counterexample to the potentially misleading inference that samplewise convergence guarantees control of expected quadratic optimization loss in a natural randomly stale-gradient numerical method. The contrast between almost-sure and moment stability motivates the precise invariant, rather than merely collecting another instance of the previously known mean-square frontier.

## Limitations and provenance
This is a substantive narrowing of the original submitted research claim. Prior source files and original assessment remain recoverable from their fixed Git blobs; they are not represented as newly verified original results. The all-parameter almost-sure stability frontier is not determined. Finite symbolic and rational checks supplement the proof. Independent expert/Lean verification is not asserted. See `RESULT.md` for exact mathematics and published references.
