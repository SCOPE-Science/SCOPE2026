# Independent mathematical audit

## correctness

PASS

Any scalar-linear extension is given at the new point by real weights summing to one. The exact equilateral Kantorovich–Rubinstein norm of delta_i-sum w_j delta_j is phi_i=(|1-w_i|+sum_{j≠i}|w_j|)/2, so ||E||=max(1,max_i phi_i/r_i). If w has negative coefficients with total negative mass t, the renormalized nonnegative vector w_i^+/(1+t) strictly decreases every phi_i; hence the new-point minimax is attained only nonnegatively. For probability weights phi_i=1-w_i. The feasibility function F(z)=sum_i(1-z r_i)_+ is strictly decreasing through one and the sorted-prefix constraints give z=max_{k>=2}(k-1)/sum_{i<=k}r_(i). At root F(z)=1, lower bounds saturate uniquely; z>=1 thereby gives one global optimal weight even at equality z=1. For z<1 strict optimality slack creates a relative open neighborhood in the coefficient-sum hyperplane; the full optimal polytope is exactly phi_i<=r_i for all i and is bounded. A negative entry w_j<0 forces r_j>1, while r_j>1 permits perturbation from a strictly feasible zero-j weight to negative after distributing F(1)<1 slack. Independently checked rational examples 4/3,1,5/6 and valid signed witness; finite LP/checker is corroboration only.

## originality

PASS

Best-of-knowledge originality: Water-filling and signed optimizer transitions for equilateral one-point Lipschitz extensions. THE PREVIOUS OCTOBER 25 THEOREM ALREADY COVERS THE EXACT NORM FORMULA; acceptance here rests solely on the new signed equality/optimizer phase, not on that prior result. Novelty limitations and primary material not obtained in full are retained below.

## value

PASS

The previously known sharp extension factor does NOT itself count as a new contribution. The surviving mathematical problem—classifying every optimal linear extension, distinguishing critical uniqueness from a full-dimensional phase, and characterizing exactly when negative weights are permitted—is a motivated natural equality-case classification relevant to Lipschitz random projections. It requires strict signed geometry beyond simply solving the scalar norm bound and has independent use for operator selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
