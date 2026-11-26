# Independent mathematical audit

## correctness

PASS

For the frozen finite birth–death chain, positive birth rates on nonterminal states and positive downward rates off zero give irreducibility. Detailed balance gives the stationary adjacent ratios. The ratios at edges 0 and 1 are strictly below one; for every edge i>=2 the ratio crosses one exactly at G_i, which is positive. Put a=N*epsilon/mu. On clearing the positive denominators of the normalized successive threshold difference, the numerator is affine in a. At a=0 it is P_0=2i^2+5i+1-N(i+3); at a=1 its sign is that of (2i-N)(N+1)(i+1). For i<=floor(N/2), P_0<=1-i<0 and the other endpoint is nonpositive, so the strict sign survives for 0<a<1. For i>=floor(N/2)+1, P_0>=4 and the other endpoint is positive. Thus the unique minimum is at m+1; at N=3 this is simply the only candidate. Below it all ratios are below one; at it the unique tie is a nonmodal descending shoulder. Above it the increasing edges are one nonempty consecutive block starting at i>=2. A tie on the left boundary is a flat valley; a tie on the right yields a two-point upper mode. The endpoint N can be an upper mode, with no right neighbor required. The strict threshold valley excludes a third mode or an upper plateau of length three. With vanishing importation, substitution gives both parities the same F(m)=4+2(m-2)/(m(m+1)) in units of mu, with successive difference 2(4-m)/(m(m+1)(m+2)). The tied maximum is at m=4,5, and the separate N=3 limit is 3mu. This limit concerns thresholds, not the absorbing stationary law at zero importation. The exact-rational source checker was inspected, not executed; it tests bounded cases, while the sign and edge arguments establish the universal conclusion.

## originality

PASS

The stationary product formula and the general qualitative cap on strict mode counts overlap prior work. The distinct result is the exact optimizer for this normalized quadratic rate, its plateau-aware threshold classification, and the parity-paired nonmonotone limiting law. The strongest broader theorem inspected does not supply these quantities.

## value

PASS

For a natural finite irreducible birth–death model, the result identifies where a second local stationary peak first exists and distinguishes it from a shoulder at equality. The exact nonmonotone size dependence of the vanishing-seed threshold, with four maximizing sizes, adds information not contained in either a general mode bound or an infinite-size limit. The law of local modes does not describe relative mode weights, transition times, or a thermodynamic transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
