# Independent mathematical audit

## correctness

PASS

Diagonalizing SPD A reduces original constant-step true-L FISTA to independent normalized scalar modes q=lambda/L. Direct recurrence gives p3=(1−q)^2(1−aq), p4=(1−q)^3(1−cq). The fourth-step squared difference factors as (1−q)^4 q[a+cq−c−1][cq²−(a+c+1)q+2], positive only for 0.7109896908853<q<0.8467139159008. The first three comparisons decrease for every mode; universal monotonicity through step4 holds iff 1/kappa≥q_+, and any larger kappa has a diagonal witness (including kappa=4/3, q=3/4 and spike ratio 5.9852687). Symbolic/decimal independent verification reproduced boundaries and factors. Covers every finite-dimensional SPD A, not later steps or nonsmooth FISTA.

## originality

FAIL

The previously published 2026-10-04 Resultary theorem derives exactly the same fourth-step scalar spectral violation window for the same classical true-L FISTA recurrence embedded in an SPD quadratic. The advertised universal condition-number threshold is the immediate spectral-interval containment corollary of that theorem; a reparameterization and easy diagonal embedding do not establish a new scientific result. The coverage is direct, not a failed-search guess.

## value

FAIL

The scientific problem of earliest objective spikes and a sharp conditioning boundary is motivated, but the specific asserted advance is a direct corollary of a previously published sharp same-algorithm q-window. The kappa conversion, diagonal embedding, and kappa=4/3 numerical example are routine consequences; no independently useful new unknown fact survives the decisive prior coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
