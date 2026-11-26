# Independent mathematical audit

## correctness

PASS

Apart from the null set of endpoint itineraries, outer cells map by translation to the next lower index on the same side; central cells have slope m and split uniformly across the opposite side. Thus the balance relation is pi_k=pi_(k+1)+pi_0/m with pi_m=0, giving the stated normalized density. For uniqueness, length-n itinerary cylinders map affinely onto whole final cells and have mesh at most m^(-floor(n/m)); each m-step itinerary expands once. The cellwise-constant subspace is closed in L1. Averaging any invariant density on these cylinders and pushing it forward n steps gives a cellwise-constant approximant converging in L1 to that density by transfer contraction. The irreducible finite chain then fixes its unique normalized cell masses. At time zero just after a flip the landing index is uniform, and each specified excursion maps its coordinate affinely onto the next whole central cell, giving iid uniform inter-flip durations. With q_n the expectation relative to that post-flip sign, the renewal recurrence gives q_n=2(1-1/m)^n-1 for n<=m. The stationary first wait is r with probability 2(m-r+1)/(m(m+1)); conditioning on this wait and summing gives the claimed C_m(n). The first difference gives the minimizing lag and only the m=2 tie. Negativity for all m follows already at n=m: (1-1/m)^m<=exp(-1-1/(2m)), and using exp(-u)<=1-u+u^2/2 with 8/e<3 gives 8m(1-1/m)^m<3m-1. The floor error and convergence of m log(1-1/m) to -1 give the uniform limit and its unique minimum at log 2. One-step flips have probability 2/(m+1), as claimed.

## originality

PASS

The map family, fixed-point-free setting and alternating-renewal methods are known. The supported distinct result is the exact invariant density and lattice sign-correlation law at its specified neutral boundary, with a macroscopic negative trough despite vanishing one-step flip probability. The consulted exact sign and renewal results match the methods or observable, but not the conjunction of dynamics and finite-lag law. Full-text coverage of two older family sources could not be verified.

## value

PASS

The exactly solvable neutral boundary explains why rare one-step sign flips do not prevent negative sign memory at lags proportional to m. The stationary density, discrete correlation and sharp limiting trough quantify that distinction in a natural existing map family; they are not general claims about finite-precision realizations or security.

The dated certificate retains the supplied scientific assessment, sources and limitations.
