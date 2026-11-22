# Independent mathematical audit

## correctness

PASS

For each petal sharing hub colour h, only mixed type {h-1,h} can change, irreversibly freezing to {h,h}; if hub stalls, its successor-neighbour count cannot rise, so all motion freezes. At hub initial colour zero four explicit inequalities on petal type counts determine permanent rotation: B+2D+E>=2, E+2F>=2, A+C>=1, B+D>=1. They imply T^6=T^3 and sharp transient bounds and period-three onset at k>=3. Inclusion-exclusion of precisely the four inequalities with petal weights (1,2,2,1,2,1) produces B_k=3*6^k+2*k*6^(k-1)+2*k*4^(k-1)-(3+2*k)*3^k-2*k (k>=2), and B_1=9. Exact time-zero counts follow by monochromatic census. Inspected RESULT and code/verify_labelled.py; independently enumerated every labelled state k=1..4 (27,243,2187,19683 states), checked T^6=T^3 and basin numbers including rotating totals 0,0,54,3996; finite checks corroborate the all-k petal proof.

## originality

PASS

PASS best-of-knowledge: exact threshold-two friendship-graph hub/petal dynamics and complete basin formula differ from published threshold-two biclique formulas and from the threshold-one arbitrary-graph criterion.

## value

PASS

The friendship/windmill graphs are a natural sparse shared-hub family with arbitrarily many triangles. An exact all-size basin census, sharp transient and almost-sure oscillation limit distinguish local motif from global cycle dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
