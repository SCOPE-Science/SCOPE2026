# Independent mathematical audit

## correctness

PASS

Walsh characters of weight k have Laplacian eigenvalue 2k and their products across a j-distance pair give the coefficients of (1-t)^j(1+t)^(d-j), including the factor 2^(-d) in the entry. An independent exact rational reconstruction reproduced all thirteen positive scaled entries at d=12,h=1/3, with gcd 2786059680768 and minimum 48478650/2410225524765331; the multiplicity-weighted sum is one. For d=13, clearing the positive denominator and dividing out h^j gives degrees 18,12,24 for j=7,13,1 respectively. A separate exact calculation reproduced both the negative test signs and the Sturm variations: 7 at both ends of (0,1/32]; 1 at both ends of [1/32,1/3]; and 11 at 1/3 and +∞ on the last interval. The negative evaluation covers both finite boundaries where needed; Sturm exclusion controls the entire union for real h>0, not just samples. Coordinate projection intertwines the Laplacians and the rational map, so summing the larger kernel over a nonempty fiber returns the smaller kernel. This propagates strict positivity downwards and nonnegativity impossibility upwards. Finally F has Taylor coefficients -1/144, 0, 1/1728 at degrees 5–7. Distances 1–5 use the positive shortest-path leading term; at distance 6 the vanishing sixth coefficient leaves exactly one diagonal stay among seven factors, giving +(35d/12)h^7. Distance 7 uses seven off-diagonal moves and gives -(35/12)h^7. Diagonal entries approach one; this proves the local threshold separately. Replay: frozen RESULT.md equations in §§1–3 (to reproduce, generate coefficients of (1-t)^j(1+t)^(d-j) over Z, sum the rational eigenvalues, and form the sequence M,M', then negative remainders over Q), coordinate projection and shortest paths in §§4–5. The supplied checker was inspected, not run. The analytic and exact-arithmetic checks concern a completed end-step, not stages or floating-point implementations.

## originality

PASS

The surviving central claim is existence of some strictly positive step precisely through dimension twelve and impossibility of any nonnegative positive step from thirteen onward. Prior all-step and large-step results on the same cubes, the order-seven Padé sign, and general Krawtchouk machinery are credited as antecedents, not as new findings. The inspected results do not give the intermediate-step feasibility boundary or imply it by changing variables or quantifiers.

## value

PASS

The graph family and entrywise condition are natural for stochastic diffusion. The separation of local and global feasibility cutoffs shows that small-step positivity failure need not prohibit every useful step; above a second exact dimension it does. The common rational witness, finite exact all-step obstruction, and marginal relation together give a complete classification of the existence question without claiming a full interval census below the boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
