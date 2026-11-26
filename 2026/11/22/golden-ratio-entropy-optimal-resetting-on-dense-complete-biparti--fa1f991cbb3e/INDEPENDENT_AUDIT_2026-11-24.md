# Independent mathematical audit

## correctness

PASS

Part mass balance gives π(A)=1/(1+q) and π(B)=q/(1+q). A-origin destinations are disjoint between reset and hop, whereas a B-origin hop to the root adds to reset at that destination. The row entropies are H₂(r)+q log b and log a−K_a(r), so their stationary mixture gives (2), including r=0 and r=1 by continuity and the corresponding stationary laws. Differentiating the continuous size extension gives ∂ₓKₓ=(xr−q log(1+xr/q))/x²>0 for 0<r<1. The resulting strict ordering covers all unequal positive integer parts, including singleton parts. For fixed a,b, K_a=O(r²) at zero, so the r log(1/r) term gives a positive gain and excludes both endpoints for every global maximizer. Nonnegativity of KL and −q log q≤r even sharpen the stated cutoff to N/r≤1−log(r√(ab)), hence r√(ab)<e at any global optimum. This is enough to put every nr in a common compact set when both ratios converge to positive constants. With c=nr the log n terms in nH₂−c log √(ab) cancel; nK_a tends uniformly on compacts to −c+(c+1/α)log(1+αc), including c=0. The resulting gain function has derivative −½ log(c√(αβ)(1+αc)) and a strict unique interior maximum. The compactness argument compares maximal values against each fixed c (feasible eventually), so every maximizing sequence converges without finite-size uniqueness; substituting the root equation yields the positive claimed gain and the balanced inverse-golden-ratio case. I inspected, not ran, frozen verify.py; a separate direct construction checked exact stationarity and weighted-row entropy comparisons at 64 small-graph/parameter pairs, not the all-size or limit proof.

## originality

PASS

The general stationary reset kernel and entropy method are prior, and the strict ordering on the star slice is established in a separate record. The supported distinct claims are the ordering across arbitrary bicliques and the positive-ratio, all-global-optimizer asymptotic with explicit gain. The actual compared results do not cover those assertions.

## value

PASS

The observed entropy measures trajectory uncertainty, rather than the artificial uncertainty of an observed reset flag. Arbitrary-part root choice and the scale and gain of all optima are exact answers to a natural control problem in the prototypical dense bipartite family. The inverse golden ratio identifies the optimum in the natural balanced case and the cutoff excludes competing reset scales; the value is not merely the appearance of a named constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
