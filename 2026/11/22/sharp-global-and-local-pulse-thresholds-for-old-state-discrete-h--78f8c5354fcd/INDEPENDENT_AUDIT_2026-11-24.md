# Independent mathematical audit

## correctness

PASS

The effort cap is redundant on the nonnegative simplex because U_max >= E. In x_i=tau*q*u^i the normalized difference from any vertex is R-cQ, Q=sum_{j<i}x_j*x_i, R=sum_i x_i*(1-1/P_i), P_i=prod_{j<i}(1+x_j). For a positive current amount with positive preceding sum s_i, P_i>=1+s_i and s_i<S, so 1-1/P_i>=s_i/(1+s_i)>s_i/(1+S). This proves strict global exclusion of every split even at c=1/(1+S). The exact ordered two-entry split difference t*(S-t)*[1/(1+S-t)-c] proves necessity and eliminates every earlier pulse locally above the threshold. At the final pulse with preceding total t, the difference is at least (S-t)*t*[1/(1+t)-c]-c*t^2/2, uniformly in the split; its ratio to t tends to S*(1-c). At c>=1 a lone earlier t produces a strictly negative exact difference with denominator 1+t, including at c=1. For successive positive entries a,b after prefix product P, the reward difference on swapping equals ab(a-b)/(P*(1+a)*(1+b)); later products and the cost term are unchanged. This proves strict improvement to sorted order from any inversion, not a claim about arbitrary nonadjacent transpositions. The all-parameter judgment is analytic; the frozen rational checks are finite, inspected and not rerun.

## originality

PASS

Best of current knowledge: the arbitrary-horizon necessary and sufficient global pulse boundary and complete local pulse classification are distinct from the strongest located coverage. Prior work contains this objective, its two-step comparisons and a local example, not the all-horizon boundary, endpoint inclusion and ordering theorem.

## value

PASS

This resolves a motivated fixed-budget optimization question raised by a known quadrature artifact. A sharp horizon-independent classification identifies when complete concentration is optimal, separates that from a regime of nonglobal strict local trapping, and gives a useful ordering rule without solving an interior critical-point system. The old-state, pure-removal and feasible-pulse restrictions are essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
