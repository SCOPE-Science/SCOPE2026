# Independent mathematical audit

## correctness

PASS

Each mutual-edge indicator has mean 1/d², overlapping edge-events are incompatible, and disjoint event families factor; hence E z^X=sum_r M_r((z-1)/d²)^r. The line graph has m=nd/2 vertices, h=m(d-1) edges and n*C(d,3)+t triangles. Inclusion-exclusion gives M1,M2,M3; conversion of the factorial moments produces mu=n/(2d), variance=n(d-1)²/(2d³), kappa3=n(d-1)²(d-2)²/(2d^5)-6t/d^6. Independently substituted the M1/2/3 formulas into SymPy and factored every difference with claimed moments to identically zero; boundary d=1,2,3 and t≤n*C(d,2)/3 establish the sign conditions. The variance/mean ratio ((d-1)/d)² uniquely determines positive integer d, then mu yields n and kappa3 yields t. Exhaustive 16-graph verifier source read, not substituted for universal algebra.

## originality

PASS

A natural matching-polynomial reformulation supplies the combinatorics, but the exact inverse identification of graph parameters from reciprocal-neighbor population cumulants and degree/triangle sign boundaries is distinct from known matching extremal inequalities.

## value

PASS

The first three observable cumulants of a simple natural local-interaction experiment recover three intrinsic graph parameters, with a complete sharp sign stratification. This is useful as an exact model-identifiability/motif statistic; the matching-polynomial reduction is classical but the inverse and signs for this model are independently motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
