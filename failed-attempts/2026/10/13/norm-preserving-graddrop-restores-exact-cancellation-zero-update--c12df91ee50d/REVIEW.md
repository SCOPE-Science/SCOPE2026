# Independent mathematical audit

## correctness

PASS

The public Lingvo documentation's live _Gradient source rendering agrees with the frozen formula: it returns transformed_grad * original_grad_norm / (transformed_grad_norm + p.epsilon), with keep_gradnorm_constant=True and epsilon=1e-7 by default. Writing r=||g|| and d=||tilde g||, the norm is rd/(d+epsilon)≤r in exact arithmetic; the update vanishes iff r=0 or d=0. Under the stated same-task aggregate assumption, exact cancellation forces r=0 for every mask and the bound gives vanishing escape amplitude near cancellation. In the scalar zero-leak, identity-activation example, equal positive and negative mass gives P=1/2 and the raw result is ±a almost surely, stronger than the positive probability of a nonzero update needed by the pure Proposition 1. This is not a theorem about optimizer states or all Lingvo versions: the historical cbceb3a source quoted in issue #254 divides the other way; that formula has norm d²/(r+epsilon) and need not vanish at r=0. The paper's prose supports the intended norm-preserving operation, not the exact regularizer or any assertion about historical builds. The frozen verify.py was inspected, not run; it checks a transcription of the intended formula, not package revision history.

## originality

FAIL

The exact regularized ratio in the frozen finding was publicly specified before this record in Lingvo issue #254, 2021-02-12. Under the frozen same-aggregate hypothesis the claimed all-dimensional norm bound, exact cancellation, and vanishing near-cancellation are immediate special cases of that exact formula. The paper already supplies both pure masking and the stated norm-preservation goal. The specific application to a conflicting scalar mask is an explanatory example of the known composition, not a distinct mathematical finding under the prior-implication standard.

## value

PASS

As an implementation diagnostic, the exact cancelling pair separates a pure sign-mask guarantee from the default rescaled update and gives a concrete unit test for a consequential distinction. The near-cancellation bound explains what kind of stochastic escape cannot survive a small aggregate norm. This is useful even though the outcomes are already implied by public material and do not meet originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
