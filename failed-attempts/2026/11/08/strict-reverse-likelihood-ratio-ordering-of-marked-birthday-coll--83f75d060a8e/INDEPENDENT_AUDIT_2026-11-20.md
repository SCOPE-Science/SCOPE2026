# Independent mathematical audit

## correctness

PASS

For iid draws on m>=2 strictly positive categories, the first t-1 distinct labels in {C=i,T=t} comprise i plus t-2 others, giving K_{i,t}=(t-1)! p_i^2 e_{t-2}(p_{-i}) on the exact support 2<=t<=m+1. For p_i=p>p_j=q and E_k=e_k(p_{-{i,j}}), adjacent ratios K_{i,k+2}/K_{j,k+2} decrease because the cross-product difference (p-q)(E_k^2-E_{k-1}E_{k+1}) is positive, by strict Newton log-concavity and E_{-1}=E_{m-1}=0. The empty remaining-vector m=2 case gives the same strict endpoint comparison. Positive denominators cover the final time, and transitivity gives all t<u minors. Row normalization preserves likelihood-ratio ordering, implying strict conditional CDF and mean ordering. The direct identity K_{i,t}-K_{j,t}=(t-1)!(p-q)[(p+q)E_k+pq E_{k-1}]>0 covers both endpoint indices; uniform p gives independence by symmetry, and nonconstant p violates independence by strict odds variation. I independently checked 346 rational probability vectors with m=2..6, including 82 exhaustive first-repeat sequence enumerations at m<=4, and separately reconstructed the 7-entry Git tree SHA. These finite checks corroborate rather than prove the all-real theorem.

## originality

FAIL

A 2026-10-18 published Resultary theorem already asserts the identical all-m, all-positive-p, all-times marked joint mass K_{i,t}=(t-1)!p_i^2 e_{t-2}(p_{-i}) and for p_i<p_j strictly INCREASING posterior odds P(C=i|T=t)/P(C=j|T=t) as t increases. Multiplying by the positive time normalization and swapping i,j gives EXACTLY the November 8 strict reverse likelihood-ratio minor K_{j,t}K_{i,u}>K_{j,u}K_{i,t} for t<u. Consequently the time-given-mark strict likelihood-ratio order is a Bayes/2x2-minor reformulation, not a new result. The CDF and mean consequences follow from standard strict likelihood-ratio order; nonindependence for unequal p follows from the previously proved strict posterior odds, while full uniformity gives independence by symmetry. The joint mass row comparison follows by a one-line subtraction from the same published K formula. Therefore the candidate entire theorem is a restatement plus immediate consequences of an earlier full-text publication; this is decisive theorem-level prior coverage, not mere title similarity.

## value

FAIL

The conditional repeated-label/time likelihood-ratio property is a natural and potentially useful invariant of heterogeneous occupancy sampling; the strict stochastic-order and independence conclusions are substantive interpretations. But here they are algebraic reorientations or immediate standard consequences of the October 18 complete theorem for precisely the same K_{i,t} table. The extra row-dominance identity is a one-line difference of an already published probability formula, with no new motivated boundary, parameter or classification. Independent exact-rational verification, a more detailed presentation and the practical relevance do not establish an independently valuable new mathematical contribution after full prior implication is accounted for.

The dated certificate retains the supplied scientific assessment, sources and limitations.
