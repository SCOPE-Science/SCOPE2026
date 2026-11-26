# Independent mathematical audit

## correctness

PASS

Connectivity makes the direction space 1⊥, and the support-function difference sums |u_i−u_j| once per edge. Writing a normal as a positive sum of distinct centered nested level indicators makes graph variation additive over these cuts and its Euclidean norm subadditive. The Euclidean triangle inequality is strict for more than one of these nonpositively-collinear indicators, so all minimizing directions are two-level; the squared norm of a centered cut indicator is |S|(N−|S|)/N. An independent way to check the cut classification: if the hub-excluding side is disconnected, its cut sizes add over its components and its centered indicator is their sum, with strict Euclidean triangle inequality. Its ratio is then strictly worse than the best component ratio. A connected side avoiding the hub is exactly one leaf or one nonhub path interval; hub exclusion also picks a unique representative up to reversal of the normal. The leaf gives N/(N−1); maximizing s(N−s) over 1≤s≤m−1 gives h and, just when N is odd and the cap allows it, h+1. The ratio h(N−h)/(N−1) is strictly increasing: the balanced values at 2j and 2j+1 are j²/(2j−1) and (j+1)/2, and the cap branch (m−1)[1−(m−2)/(N−1)] joins at N=2(m−1). The ratio is less than m−1 if m≤5, equals 4 at t=15 and 9 for m=6 and 7 respectively by the cap formula, and equals 4 at N=15 for m=8,…,14 by balance. For m≥15 it is already greater than 4 at t=1 by the balanced branch and its N=16 bound. This covers all strict and tie cases. The frozen checker and its reported 63 exact cut enumerations and larger phase sweep were inspected, not rerun or used to extrapolate.

## originality

PASS

The distinct result is the evaluated bunched-cycle Euclidean width, exact leaf/arc switches and exhaustive minimizing directions. The graph form and general inradius/cut identity are prior, not claimed here as new.

## value

PASS

A cycle plus bunched pendants is a natural structured unicyclic family; the exact result distinguishes the bridge bottleneck from Euclidean balance. It shows precisely when a two-edge cycle cut beats every bridge cut, including three regimes of exact ties with distinct optimal directions and parity-dependent arc sizes. This is an all-parameter benchmark for the general variational problem, not a numerical table or the cut formula alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
