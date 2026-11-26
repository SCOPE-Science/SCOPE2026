# Independent mathematical audit

## correctness

PASS

In a length-three simple path, positive end edges force the middle edge positive. In a bipartite graph absence of such paths makes each nontrivial component a star. For a left star with h>0 positives, its center and exactly the h specified leaves must be selected; for h=0 the disjoint choices are omit the center with any leaf subset or select the center with no leaves. These give the claimed inventory factors, with exchanged sorts on right stars. Components and unused vertices have disjoint coordinates, so coefficient multiplication counts completions for the exact quotas; permuting leaves reduces the labels to their h vector. In the padded region, the all-positive label tests the incident quotas. For any other label choose the positive endpoints (a negative edge has a degree-one endpoint not selected this way), then fill from unused coordinates. The labeled exponential formula counts the two star orientations with isolated edges included once. A nonempty forest has ell+t−number_of_components edges; the one-star and two-or-more-star bounds, and explicit stars attaining them, give the VC formula. For r,s≥3 the maximal edge count forces two nontrivial stars of opposite center sorts on all r+s available incident slots; choosing the two centers gives rs configurations on each active vertex set. Empty supports and quota one are included. My separate trace-fiber replay (`/tmp/opencode/frozen-review-repro.py rectangles`) reproduced the complete polynomials of the (4,6;2,3), (6,6;3,3) and (5,5;3,3) cases and checked aggregate face counts on the 3×3 grid for all nine positive quota pairs. Source code and recorded runs were inspected, not executed. No extrapolation from finite checks or assertion of necessary padding is used.

## originality

PASS

The non-induced-path obstruction, unrestricted star-forest classification and its species method are prior; the (2,2) dimensions are prior. The distinct all-grid exact-quota feasibility criterion, and the exact-quota stable enumeration and extremal consequences in their stated ranges, survive the source comparison. The stable count reuses the prior species argument rather than introducing a new unrestricted enumerator.

## value

PASS

Exact quotas are a natural restriction, not a numerical slice: padding fails on small grids even for some star forests whose incident vertices fit. The local inventories solve that obstruction for every support, while the stable polynomial and extremal description separate support-level structure from a scalar VC dimension. The result does not claim a sharp padding boundary or a polynomial-time test in the number of queried cells.

The dated certificate retains the supplied scientific assessment, sources and limitations.
