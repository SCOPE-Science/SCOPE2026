# Independent mathematical audit

## correctness

PASS

For each compact fully invariant K, complete two-sided orbits exist by smoothness and compactness. If X_i=max_K x_i>0, at a point maximizing x_i its time derivative is zero and the exact prey equation yields (growth_i-s_i X_i)/(1+k_i y) >= q_iE_i>=0; hence X_i <= M_i=max(growth_i-q_iE_i,0)/s_i, with X_i=0 if growth_i<=q_iE_i. Thus the exact predator logarithmic rate is <=Gamma<0 for every point of K. Along any y>0 complete orbit this forces y(t)>=y(0)exp[-Gamma(0-t)] for t<0, contradicting boundedness as t->-infinity. Therefore K lies in y=0. There, x1dot=x1(R1-s1*x1-A3*x2) and x2dot=x2(R2-B3*x1-s2*x2), and the Dulac divergence of B=(x1*x2)^-1 is -s1/x2-s2/x1<0 in the positive quadrant. Together with one-dimensional axis flows and planar Poincare–Bendixson recurrence, all recurrent points are equilibria. A compactly supported invariant probability measure is concentrated on recurrent points by Poincare recurrence. The universal claim concerns compact fully invariant sets, not merely forward-invariant trapping boxes.

## originality

FAIL

The audited theorem is a parameter substitution and direct dynamical corollary of Hou–Baigent 2015, Theorem 3.1, coupled only with classical planar Bendixson–Dulac and Poincare recurrence. This pre-existing Kolmogorov-system theorem supplies finite-time entry into any strictly inward coordinate rectangle when species are ordered appropriately. For arbitrary small epsilon>0, choose prey upper bounds M_i+epsilon and predator upper bound epsilon. First place all prey with q_iE_i>0 OR m_i<1; each has a uniformly negative per-capita rate at x_i>=M_i+epsilon independently of the unordered variables. Next place predator y: all remaining prey have m_i=1 and q_iE_i=0, so their predator conversion coefficients vanish, and its per-capita rate is at most Gamma+epsilon*sum_i C_i(1-m_i)<0. Place the exceptional prey last: when y<=epsilon and x_i>=M_i+epsilon, their per-capita growth is at most -(A_2/K_1 or B_2/K_2)*epsilon/(1+k_i*epsilon). Theorem 3.1 therefore gives absorbing rectangles with arbitrarily small predator cap; its strict uniform bounds make entry uniform over an arbitrary compact invariant set, forcing y=0 by invariance. On that plane, standard 2D competitive Lotka–Volterra Dulac and Poincare recurrence arguments put invariant measures on equilibria. The target Cao–Wang–Liu article itself states only local predator-free stability (4.8), which alone is insufficient; the decisive broader prior is Hou–Baigent Theorem 3.1. This is a statement-and-implication rejection, not a failed keyword search or inaccessible-paper inference.

## value

FAIL

The biological question is motivated, since the exact source paper studies Hopf bifurcation and chaos, and an explicit predator-exclusion parameter region can be useful for interpretation. Mathematically, however, the bound is a routine textbook comparison of carrying capacities with the predator per-capita growth rate, already supplied as a direct application of the published ordered Kolmogorov absorbing-box theorem. The invariant-measure corollary then uses the standard Dulac and Poincare recurrence theorems. No new sharp boundary, structural lemma, nontrivial classification, or new dynamical phenomenon is established; the sufficient condition is intentionally conservative. This is not rejection merely because the proof is short or because the subject is applied, but because the complete mathematical content is a textbook-level substitution into a covering prior result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
