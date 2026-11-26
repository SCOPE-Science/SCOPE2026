# Independent mathematical audit

## correctness

PASS

The displayed mathematical claims are true. Rearrangement gives convexity of the rank penalty and the order of the minimizer; strict convexity gives uniqueness, and transfer from a positive coordinate to a zero coordinate has KL derivative -infinity, so the solution is positive. For u=z-ta and v=P_C(u), set p=softmax(v). The ordered entropy objective has gradient at p equal to v-u plus a constant vector. Since u-v belongs to N_C(v)=N_C(p) and the constant pairs to zero with simplex displacements, p satisfies the global first-order inequality. The last explanatory clause in frozen RESULT.md line 47 is incorrect: log(p_i)-u_i need not be constant within a pooled block (take u=(0,2)); the normal cone equality, not constancy of this residual, justifies the formula. For the semigroup, a tied input block in P_C(u) gives an ascending adjacent pair on subtracting s a. A strictly descending projected pair there could be replaced by its average, which remains feasible and strictly lowers squared error. Thus the first set of active normals remains active in the second fit, and adding the two normal-cone residuals yields P_C(P_C(u)-sa)=P_C(u-sa). Translations by a constant cancel under softmax; original order and ties are preserved. The constant projection criterion is the mean-zero polar cone, the nonpositive centered-prefix inequalities. For each proper prefix the mean of descending nonconstant a is strictly above the complementary suffix mean, proving positive denominators and the stated first hitting time, including uniform input. The exact example has prefix ratios log(12)/3 and log(18)/3 and first pooling at log(2). Inspected the supplied checker and verification notes, without executing uploaded code.

## originality

FAIL

The failure is established mathematical implication, not limited access and not that the identical sentence was found. The initially plausible distinction from older sticky-particle projection is the specific simplex-KL-to-isotonic formula. That remaining link is itself a direct exponential-loss case of the classical isotonic Bregman-loss theorem, followed by the simplex normalization. In those coordinates both time composition and full coalescence specialize the Lagrangian theorem and polar criterion of Natile–Savaré. No separate new finding remains in the frozen claim after crediting those implications.

## value

FAIL

The explicit simplex description is potentially useful as exposition or implementation guidance, but the claimed result adds no independent structural fact once the older Bregman isotonic optimum, sticky restart, and polar criterion are specialized. The normalized exponential coordinate change and the prefix ratio solve those established conditions directly. No further independently useful new invariant or regime survives in the submitted theorem to justify a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
