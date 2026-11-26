# Independent mathematical audit

## correctness

PASS

Independent attempts with completion allowed on ties give the ratio of expectations, a b-weighted mean of the deterministic ratios. For R<=cx S the positive stop-loss differences c_i vanish at i=1 and tend to zero by integrability and equal means. The mass difference is their discrete second difference. Finite summation by parts followed by the limit is legitimate: h=a,b are bounded, c_i tends to zero, and the second differences of h are absolutely summable. Subtracting Q(R) times the denominator increment gives the stated signed identity. Endpoint signs suffice by affinity. Necessity follows by placing a small mass at i and spreading that mass equally to i-1 and i+1, keeping positive admissible mass at any chosen j with b_j>0 (including j=i). Letting the small mass go to zero tests u_j and hence both possibly unattained extrema. For an interior start z<m, k=2m-z is the first far exit; both exits have fixed parity, so k-2 and k-1 have positive near-exit mass only, while k and k+1 have the same cumulative probabilities and include positive far-exit mass. The two spread comparisons then have opposite signs by the b-weighted mean rule. Reflection handles z>m; at z=m reflected paths have weight ratio ((1-p)/p)^m at every length. The phrase 'only site' is read within the positive-completion-time assumptions, so starts already at an absorbing boundary (T=0) are excluded. An independent exact-Fraction replay corroborated the identity and 189 walk cases (m=2..8, three biases, all interior starts); this is not the universal proof. Replay: python3 /workspace/branches/13fc8e70-3903-483e-82d9-65aa01518dfa/independent_check.py. The frozen checker.py was inspected, not executed.

## originality

PASS

Credit the known renewal ratio, midpoint neutrality, other clock orders and standard convex-order tools. The supported distinct claims are the exact necessary-and-sufficient curvature inequalities for the named discrete convex-order problem and the constructive strict failure of both directions at each off-midpoint interior site. The closest paper expressly poses the convex-order dual as open; possible earlier equivalent fractional-expectation criteria remain a limitation.

## value

PASS

The criterion resolves a specifically posed order-comparison question for a ratio of expectations, using just two curvature tests per time instead of quantifying over pairs of clock laws. The elementary opposite-direction witnesses show why the order gives no universal comparative prediction at any off-midpoint interior site despite known monotonicity results for other orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
