# Independent mathematical audit

## correctness

PASS

The three-component Ricker map admits one-step xi<=e and persistent positive total S from S_next>=S exp(2-S). Exact logarithmic-gap update w_next=[1-(1-c)L(xi,xj)]w uses the logarithmic mean; since (1-c)e<2 on the stated open c interval, all gap multipliers have absolute value <1, and the positive S floor plus bounded initial log diameter yields a uniform q<1 along each trajectory. Consequently gaps decay geometrically, all xi become close, and t_n=(1+2c)S_n/3 obeys a scalar Ricker recurrence te^{2-t} times 1+O(q^{2n}). The scalar r=2 map has globally attractive positive fixed point 2 (no nontrivial two-cycle plus the one-dimensional convergence principle), and uniform finite-step perturbation argument transfers that to t_n. Thus all xi->2/(1+2c), with exact nonzero-gap exponent log((4c-1)/(1+2c)) by Cesaro. On the diagonal z_next=z+2-2e^z, direct symbolic composition gave f²(z)=z-(4/3)z³-(2/3)z⁴+O(z⁵); reciprocal-square differences give n z_n²->3/4 for small nonzero z. The source verifier was inspected, independent symbolic cubic and Jacobian checks made; finite checks do not establish all-seed convergence.

## originality

PASS

The 2017 Luís–Rodrigues three-dimensional Ricker analysis gives local fixed-point stability and states global-attraction questions, not all-positive convergence on the r=2 flip boundary. Gyllenberg–Jiang–Niu 2019 global stability theorem has a strict intensity condition not met by current intrinsic r=2; planar critical Ricker logarithmic asymptotics are genuinely two-dimensional, not covering a three-species global flow or pairwise asymptotic exponent. Therefore the conjunction of global three-species convergence at neutral flip and the two distinct rates appears new on inspected literature.

## value

PASS

Global convergence precisely at a neutral flip eigenvalue -1 in an actual three-species competition map, with exponential pairwise synchronization and algebraic common-mode relaxation, fills a natural boundary of the stability theory. The condition 1-2/e<c<1 has a structural source in logarithmic-mean contraction and is not a chosen arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
