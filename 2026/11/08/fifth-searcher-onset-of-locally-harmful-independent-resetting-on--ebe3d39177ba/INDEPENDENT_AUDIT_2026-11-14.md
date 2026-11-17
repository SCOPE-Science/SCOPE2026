# Independent mathematical audit

## correctness

PASS

For N=1,...,5, killed population-count chain on four transient vertex types has exactly (N+3 choose 3) states and A=-Q0 with diagonals N, 1->0 killing rate c1/2, ordinary off-diagonal rates c_i p_ij. Independent resets from positions 1,3,4 to 2 give generator B; differentiating u_r=(A-rB)^(-1)1 yields Au=1, Av=Bu and M_N'(0+)=v(N,0,0,0). All transient states can hit target and A is nonsingular. The exact table gives derivative -10, -44679/18496, -5826055874237962/9473890663107363, -98437587236766524607457/4857833711937191749095424, and +117715636350470400400957554016380716796973103498302122/602188558121296962986525429886983883962244425767981445. Independent separate numerical matrix reconstruction reproduced all five derivative signs and means; source verify.py supplies exact rational elimination and all-equation residual checks, including labeled-state N<=3. Finite exact certification suffices for precisely N<=5; there is no claim for all N or global reset rates.

## originality

PASS

Against full submitted theorem and inspected sources: Natural specific formula distinct from checked prior claims, with clear residual priority risks. A genuinely motivated first sign reversal in a finite network under independent-per-walker reset clocks, located sharply at five searchers. This quantifies a distinct discrete-network threshold and a policy-sensitive dif

## value

PASS

A genuinely motivated first sign reversal in a finite network under independent-per-walker reset clocks, located sharply at five searchers. This quantifies a distinct discrete-network threshold and a policy-sensitive difference from the common-clock critical four-searcher case; it is a natural exact finite classification, not an arbitrary instance. No extrapolation to higher populations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
