# Independent mathematical audit

## correctness

PASS

The exact finite-tree recursion has initial ratios λ (free) and 0 (empty), and p=r/(1+r). At r_c=1/(b−1) the single-step derivative is −1. For the centered two-step map and δ=λ/λ_c−1, the multiplier is 1+a_bδ+O(δ²) and the cubic at δ=0 is −C_b with C_b=(b+1)(b−1)^3/(6b²). Critical entry follows from the single fixed point of the square; independently, the single-step Schwarzian is −(b²−1)/(2(1+r)^2), so the square has negative Schwarzian and ((F²)')^(−1/2) is strictly convex. A nontrivial two-cycle would straddle r_c and give two more points with (F²)'=1 by Rolle, contradicting strict convexity. After fixed-time entry, a small centered interval is forward invariant by the sign of the cubic at its endpoints. In the inverse-square recursion the term (1/n)√w is at most a fixed constant times w/n locally. The remaining small radial error is absorbed in the positive source term, giving w_j comparable to j+1 up to n/2, uniformly for t in compact sets. The geometric sum has limit C_b(1−e^(−a_bt))/(a_bt) after division by n, with continuous value C_b at zero; the cumulative remainder is O(√n) before division. The odd update flips the sign, and multiplying the separation by σ'(r_c)=(b−1)^2/b² gives the stated amplitude. Independent bounded checks gave 8 exact finite-tree comparisons, 9 rational arity coefficient checks and 48 crossover cases with worst relative error 0.00122794. The reproduction was bounded_check.py, not a run of the frozen verify.py.

## originality

FAIL

The critical-window profile, including its nonzero critical amplitude once the two derivatives of the tree map are inserted, is the cubic discrete scaling law already given by Corral. The hard-core calculation is correct, and supplies explicit compact-uniform error control for the specialized iteration, but does not establish a distinct profile or a substantive new normal-form mechanism. The comparison is a reduction to an inspected prior equation, not a claim that Corral tabulated the tree observable.

## value

FAIL

Critical boundary sensitivity is a natural observable, and the specialization is a correct worked example. Its sharp scale, crossover and branching-number amplitude are obtained by evaluating the known cubic law and the elementary single-step observable. Compact-uniform control is useful justification for that application, but is supplied by the same local inverse-square recurrence and a bounded-window comparison, not a new independently useful estimate or invariant. No substantive distinct repaired claim is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
