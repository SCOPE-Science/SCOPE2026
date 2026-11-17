# Independent mathematical audit

## correctness

PASS

PASS. The source proves the exact one-edge availability probability e^{-t} u_i(1-e^{-t})u_{n-i}(1-e^{-t}), with u_k(v)=sum_{j=0}^{k-1}(-v)^j/j!. Uniform Taylor remainders give mean available-edge count e^{-2-x} at t=log n+x. Influence of distant first-attempt clocks requires a strictly decreasing consecutive priority chain, probability <=2/R!, and R=ceil(3 log n) produces a finite-range dependent approximation. Distinct-index factorial moments converge to those of Poisson(e^{-2-x}); saturation is exactly the absence of available edges. The compensator of the superposed (n-1)-rate Poisson trial process makes T_n/n-tau_n tend to zero. The earlier 2026-10-18 full mathematical proof gives stronger spatial late-success Poisson count and same Gumbel limit. The sources distinguish first attempted edge clocks from successful arrivals. The all-order result is analytic, not inferred from the finite checker.

## originality

FAIL

Older published work gives the stronger *spatial* Poisson limit of late accepted dimers on the same finite open path, with quantitative O(log n/n) total-variation control for late success counts and the identical Gumbel terminal-time limit; it explicitly traces scalar Gumbel to 2002. At t=log n+x, the count A_n(t) of currently available edges equals the count W_n(t) of edges that will succeed after t with probability 1-O(1/n): any currently available edge later blocked without succeeding needs a neighboring edge with an independent first-attempt time >t; union bound O(n)e^{-2t}. Thus the earlier W_n Poisson theorem implies the A_n Poisson theorem. Converting continuous last-success time to trial count with a rate-(n-1) superposed Poisson clock is a routine martingale LLN and gives the submitted normalized Gumbel trial count. No independently valuable unaddressed final claim remains.

## value

FAIL

Jamming time and late-edge fluctuations are motivated natural invariants, but the submitted Poisson and Gumbel limits are already consequences of a strictly stronger published open-path spatial point-process theorem, including quantitative TV approximation. De-Poissonizing the terminal clock is a routine short additional step. Correctness and independent finite verification cannot transform this known result into independently valuable new science.

The dated certificate retains the supplied scientific assessment, sources and limitations.
