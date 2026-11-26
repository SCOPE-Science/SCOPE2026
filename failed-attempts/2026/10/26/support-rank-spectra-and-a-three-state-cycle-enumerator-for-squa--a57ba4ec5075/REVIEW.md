# Independent mathematical audit

## correctness

PASS

In RESULT.md:44–64, the row for edge uv of the multiplication matrix is the equation a_u b_v+a_v b_u=0. Coordinates outside N[S] are free; each coordinate in N[S]\S is forced to vanish by an incident supported endpoint. Dividing b_v by a_v on S reduces the internal equations to y_u=−y_v. Along a connected component one value propagates with parity of path length; an odd cycle kills it except in characteristic two, where every component allows one constant. This gives exactly (1) including isolated and empty supports, and counting coefficients gives (2). On a proper nonempty cycle support, each zero run of length l contributes min(l,2) vertices to N[S] and corresponds to one supported component, giving |S| plus one per zero run of length at least two. The three states are the preceding zero suffix length truncated at two; their cyclic path is unique for each labelled support, including the all-zero loop at the two-zero state and the all-one loop at the one-symbol state. The latter needs exactly the correction based on parity and characteristic. The determinant of lambda I−T is lambda³−(1+wz)lambda²+wz(1−z), proving (4) also at j=0 by Cayley–Hamilton. Both C5 examples agree by counting supports of each size. Static inspection of verify.py:151–191 and VERIFICATION.md:19–23 confirms modular and F4 rank comparisons in 15 cycle/field cases and two all-four-vertex-graphs suites. These are finite diagnostics, not used for the proof.

## originality

FAIL

The distinct earlier October 12 Resultary finding proves the identical graph-support rank and identical cycle polynomial in nullity notation. Its four-state transfer also already implies the three-dimensional recurrence without a new enumerative argument: after converting nullity to rank two columns are equal, so the transfer descends by an explicit one-dimensional zero summand in the trace. The smaller matrix is an alternate presentation of this elementary reduction, not a materially distinct enumeration or recurrence.

## value

FAIL

The complete finite-field rank spectrum has mathematical use, but it and its constant-size computation are already available. The remaining improvement is a different three-state description of a matrix whose redundant dimension can be removed directly, with no new asymptotic efficiency, classification, or mathematical obstacle resolved. The explicit reduction shows why this is a small presentation change rather than an independent result warranting a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
