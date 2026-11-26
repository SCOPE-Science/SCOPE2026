# Independent mathematical audit

## correctness

PASS

The row sums of T_j are mixtures of p0,p1 with nonnegative weights that sum to one, so all survival tails are at most p_*^k and the differences of consecutive tails give a probability law. Direct subtraction of the two rows and differentiation in j give the stated R(v) identities. On the appropriate cone R(v) has the strict sign of Delta whenever the free coordinate is positive; that coordinate stays positive under all product steps since the free-free entry is positive. The recurrence V_{k+1}(j)=T_j V_k(j+1) and entrywise nonnegativity then propagate the monotone shift, with a strict first-coordinate inequality at every k>=1. This argument includes n=0 and u1=0. Equal ratios instead give constant row sum p1 and hence exactly geometric tails. The infinity norm of T_j-T_infinity is attained by the free row and equals (U1+b)(u0+p1 U0)/D_j. Telescoping yields the stated bound on each tail; half the sum of the absolute mass differences is bounded by the sum over positive-index tail errors since the mass errors are consecutive tail differences and the index-zero tail error is zero. The exact first-tail error is -Delta(U1+b)/(U1 D_n), so the event K>=1 witnesses the lower bound, also when the target is a point mass at u1=0. The theorem proves order-sharpness, not a sharp upper constant, and concerns the reduced count law only. RESULT.md §§1–5, VERIFICATION.md and CHECK.py were inspected; the supplied code was not executed.

## originality

PASS

Jia supplies the exact kernel and qualitative large-n geometric behavior. Credit that model, the equal-ratio geometric mechanism and the first-tail information already directly available from the kernel. The supported distinct contribution is strict stochastic order of every positive-threshold tail for every initial count and quantified sharp-order total variation for the same kernel. I found no verified equivalent or stronger statement covering this contribution in the compared sources.

## value

PASS

Strict ordering for the entire law is stronger than a mean trend and applies uniformly in the threshold, even at the complete repression boundary. Explicit TV control answers when a simpler law is quantitatively justified for all count events, and the lower bound proves that replacing the rate by o(1/n) is impossible when the ratios differ. These are meaningful extensions of the qualitative approximation, not just verification of a known burst formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
