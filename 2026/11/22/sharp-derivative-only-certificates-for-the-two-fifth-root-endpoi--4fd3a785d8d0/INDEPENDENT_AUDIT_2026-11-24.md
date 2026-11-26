# Independent mathematical audit

## correctness

PASS

Normalize by x=a+ht; normalized sixth derivatives contribute h^6 and the integral contributes h, giving h^7. Both reflected rules are exact on degrees 0–5, checked by substitution and independently in exact symbolic arithmetic. Using Taylor's integral remainder starting at 0, the order-six kernels are the corresponding error functionals on (x-s)_+^5/120. Substitution of the right endpoint jets yields K±=z²(±3√5/2−3−z)/720 with z=s(1−s). Their difference is √5 z²/240 and is strictly positive inside. The normalized error is a weighted average of 1/2−1/√5−z/(3√5). For any continuous nonzero nonnegative sixth derivative the ratio is strictly between the two endpoints; the closed interval stated in the proof is the closure of attainable ratios (as the proof and limitations specify elsewhere), not nonzero equality cases. Smooth derivative bumps recover the endpoints as limits, including one approaching an edge from inside, so the unique fixed-affine minimax choice is the midpoint with half-width 1/(24√5). The sign reversal and summation over a partition preserve the inequalities. Independent high-precision checks reproduce all stated exp(x) values and probe concentration at midpoint and edge using polynomial sixth derivatives: python3 /workspace/reproductions/check_frozen_math.py 2. These diagnostic runs do not replace the all-function kernel proof. Uploaded checker inspected but not executed.

## originality

PASS

The supported distinct claim is the exact relative-gap enclosure and fixed affine minimax estimator for these two specific endpoint rules, not the fifth-root rules or the Peano kernel representation. The closest located methods and competing certificates use different rules; no identified prior theorem supplied this signed kernel ratio or its range. The Wang primary passage could not be verified, so the comparison with its exact remainder discussion remains limited.

## value

PASS

For two existing rules sharing endpoint jets, the computable gap now gives a rigorous sign-constrained error certificate without estimating a global sixth-derivative norm or evaluating interior values. The sharp interval is about 3.73% of the raw gap; the exact constants allow optimal fixed blending rather than merely proving opposite signs. This is a useful property of the fixed pair, not a claim to outperform all endpoint rules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
