# Independent mathematical audit

## correctness

PASS

Because self-weight is zero, each fixed-action opinion optimization is a strictly concave quadratic with solution y_i=qz_i+(1-q)x_i in [0,1]. Completing the square gives the optimized action incentive beta*lambda/(beta+lambda) times z_i-theta, so joint deviations are accounted for. Within each community two distinct players differ only in which focal opinion is excluded. Thus z_i-z_j is the negative within-edge weight times y_i-y_j, while the equilibrium opinion difference has the same sign as x_i-x_j. Opposite actions would require the cooperator's z at least theta and the defector's z at most theta, a contradiction. For the two uniform block actions, the row-stochastic block matrix gives a unique opinion vector since q<1. Subtraction gives the opinion difference (1-q)/Delta in the A-only profile; then z_B=(1-p_B)/Delta and z_A=[q(1-p_B)+(1-q)p_A]/Delta. The B-only profile swaps roles. The consensus means are 0 and 1, and the excluded equalities guarantee strictness of every pure equilibrium. Width and translation follow by subtraction. A singleton forces p_A+p_B<1, and the only non-singleton case below five agents is balanced 2+2, so one-sided polarization is impossible there. For the 3+2 example the incentives put 5/8 strictly within the A interval and above the B interval. An exact fixed-point iteration with sup-norm error at most 2^(-18) independently resolves every player's action condition in all 32 profiles; the three surviving action vectors agree with the claim.

## originality

PASS

The existing balanced census and its within-community homogeneity reduction are material prior coverage and are not credited as new. The distinct contribution is the exact unequal-size interval split, the resulting one-sided pure polarization, and its sharp 3+2 minimum within the common-weight family. The inspected balanced theorem gives paired polarization only. The inspected opening of Davidson et al. concerns consensus and does not state an unequal-community census; the remaining primary text was not assessed.

## value

PASS

The interval split identifies what changes when the sizes, but not the edge parameters or behavior, are made asymmetric. It explains an odd three-equilibrium census that balanced polarization cannot realize. The exact minimum and strict witness make this more than an isolated finite enumeration; the witness is stable to sufficiently small parameter shifts within the family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
