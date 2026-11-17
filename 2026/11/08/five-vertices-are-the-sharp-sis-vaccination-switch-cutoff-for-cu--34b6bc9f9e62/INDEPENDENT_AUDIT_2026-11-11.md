# Independent mathematical audit

## correctness

PASS

The SIS generator Poisson equations on each nonempty infected subset have off-diagonal infection rate lambda*d_S(v), recovery rate1, and reward |S|; the absorbing empty state gives a unique positive finite expectation. Coupling with shared recovery/infection clocks proves burden strictly increases on adding an edge for uniformly seeded infections. Deleting any vertex from n<=4 leaves <=3 vertices, for which each possible residual edge count corresponds to a nested graph isomorphism type, hence maximum-degree vaccination is optimal uniformly in lambda. For the n=5 graph edges {01,02,04,12,13,23}, deletion 0 gives K3+K1, deletion 1/2 gives P4, and other deletions have strictly larger burden. Independent exact 15-state rational Poisson solves reproduce B_K3+K1=(3lambda²+3lambda+2)/2 and the displayed degree-eight rational B_P4. Their signed difference has numerator lambda²(lambda+1)(48lambda^5+136lambda^4+99lambda^3-78lambda²-156lambda-72), with positive denominator. Descartes sign variation and endpoint signs prove exactly one positive root, bracketed numerically at 1.0282979668; optimum switches {1,2} to {0} with tie {0,1,2}. This proves the claim for all positive rates, not just tested samples.

## originality

PASS

Earlier graph vaccination switches in Reed–Frost bond-percolation/SIR models concern final outbreak size, while SIS survival studies typically concern extinction time or initial infected-set rankings. The finite-graph intervention objective here is integrated infected person-time, including reinfections. No inspected earlier theorem yields the present all-rate cutoff and unique algebraic crossover.

## value

PASS

Exact order-four universality and the first order-five rate-dependent vaccination reversal establish a sharp decision-theoretic boundary on a natural stochastic network model. The crossover compares a connected corridor with a dense core plus isolate under time-integrated prevalence, a quantity not interchangeable with SIR final size or SIS extinction time. Unique algebraic threshold and complete optimizer sets are independently useful finite structural facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
