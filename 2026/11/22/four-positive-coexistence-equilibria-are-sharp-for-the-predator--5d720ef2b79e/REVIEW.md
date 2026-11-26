# Independent mathematical audit

## correctness

PASS

For 0<x<1 all entries of the capture matrix are positive, so delta>0. Equilibrium uniquely forces P=1/delta and Y=(r-1/(K delta))/delta. With those definitions Q=K delta²(hY-g), so Q(x)=0 is exactly the remaining equation; a candidate root must also satisfy Y>0. No division by h is needed, and no root gives more than one coexistence state. The average-rate identities r=u_B+xg and delta=v_B+xh cancel the xgh term in rh-delta g, leaving u_B h-v_B g of degree at most two. Thus degree Q<=4 and Q not identically zero gives the upper bound for distinct states. Independent exact checks/5.py (Python 3 and SymPy) reconstructs the quartic directly from the original payoff averages, confirms the five coefficients, gcd(Q,Q')=1, and exact real-root counts in the four supplied brackets. The signs of Q at the pairs of endpoints are (+,-),(-,+),(+,-),(-,+). The affine g,h are both negative throughout each of the first three brackets and positive throughout the last; hence Y=g/h>0 at all four roots. With positive parameters all these strict endpoint signs persist on a neighbourhood, furnishing four distinct admissible roots and ruling out Q identically zero there. The four states are isolated and independent of beta>0. This is a statement about equilibrium counts, not dynamical stability or Q identically zero.

## originality

PASS

The supported distinct result is sharpness in the full nondegenerate positive-payoff family: exactly four positive states are achievable for strictly positive rational data, robustly, and four is the global nondegenerate maximum. The model, feasibility conditions and rational equilibrium relation for h nonzero are known; clearing that denominator is not credited as new. The same-model primary text calls the elimination fifth degree and gives an example with three, not a sharp count of four. The exact cancellation supplies a sharper bound, but it is the positive, robust saturation of that bound together with the uniform proof that distinguishes the finding. Related catalogue statements do not cover the theorem. The origin paper was not retrievable by the attempted lawful routes, so this is not a universal priority claim.

## value

PASS

The maximum number of positive coexistence states is a natural structural feature of this model. Reducing the exact root degree constrains the whole nondegenerate family, while the rational witness shows the bound can be met on an open set under strict positivity, not just by counting formal roots or on a finely tuned slice. This settles a meaningful equilibrium-count question without asserting stability, generic ecological prevalence, or a classification of the degenerate family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
