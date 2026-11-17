# Independent mathematical audit

## correctness

PASS

The source fixes heterogeneous h_j>0 scalar quadratic losses, independent geometrically decaying two-channel Laplace releases, exact full public transcript and affine one-agent adjacency. Conditioning on the same public history cancels all W-mixed releases; the affected coordinate has the signed two-step matrix S=[[t,1-t],[t(1-t),-t(1-t)]], initialized (X,Z)=(1,1-t). For 0<t<1 the cone X>=Z>=0 is invariant, the strictly positive Perron coefficient rules out cancellation, and sum_{m>=0}r^-m S^m converges iff r>lambda_+(t). Exact Laplace tail likelihood ratios attain finite-prefix suprema; monotone cylinder extension yields the full transcript bound, while divergence of prefix losses refutes every finite epsilon. t>=1 gives nondecaying/growing primal shifts. The exact resolvent returns epsilon=delta*(step*r*(r+1-t)/dx+r²*(1-t)/dy)/(r²-r*t²+t²-t). Independent symbolic characteristic polynomial and resolvent checks reproduce the h=1, step=1/2, r=4/5, dx=dy=delta=1 certificate 84/19. No convergence claim for optimization iterates.

## originality

PASS

Best-of-knowledge originality survives compared sources and all four direct implications.

## value

PASS

The exact all-network scalar-quadratic pure privacy feasibility threshold and minimal Laplace budget are naturally important for designing noisy gradient-tracking schedules. The signed invariant-cone sensitivity recurrence is nontrivial, and a provably feasible regime beyond the published sufficient comparison bound is quantitatively useful, without claiming optimization convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
