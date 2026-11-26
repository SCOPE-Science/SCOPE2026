# Independent mathematical audit

## correctness

PASS

The identity fgf=f is equivalent to an equivariant right inverse on f(X), extended by the identity on its invariant complement. On each image orbit such a section must map onto a whole source orbit, and be injective there, so the witness is exactly a same-type source isomorphism. Conversely the inverses of independent such isomorphisms define the section. For a selected target support, each type-i source has b_i choices by evaluation at a stabilizer representative; hitting every selected type-i target with a type-i source is both necessary for regularity and sufficient to realize exactly the chosen support. Removing u selected same-type targets eliminates exactly u a_ii choices per type-i source. Inclusion–exclusion, independence by type and labelling of target orbits give the stated polynomial with point-cardinality exponent; the empty support contributes zero for nonempty X. For the monoid criterion, any image without a same-type preimage must have a strict incoming arrow. If its type is a singleton with no strict outgoing arrow, its sole source must hit itself, a contradiction. In the converse, send one strict-lower orbit to the offending target and send every same-type source either to a single different same-type orbit or, for a singleton type with an outgoing arrow, to another type. Extend by the identity; this is nonregular. All strict type changes strictly increase subgroup order, even for nonnormal H_i. Independent bounded point-map search testing all possible commuting maps and inner inverses (`python /workspace/branches/frozen_replay.py 3`) gives 14/16 and 36/48 in the two stated examples and 19/21 for a three-type C4 chain; these confirm specializations only. The frozen checker was inspected, not executed.

## originality

PASS

Pass for the table-of-marks image-cardinality census and the all-elements criterion on arbitrary finite G-sets, not for the section test in isolation or the finite cyclic and full-shift special cases. Konieczny (2003) explicitly has the same total-map all-regularity criterion in cycle language for cyclic actions, a stronger overlap than the 1999 partial-map analogy. Castillo-Ramirez–Gadouleau explicitly give the section criterion for finite full shifts. Those antecedents should be cited when describing the scope of originality. Neither inspected theorem supplies the rank census, and the cycle condition cannot distinguish incomparable stabilizers of the same sizes in general.

## value

PASS

Determining the point-rank distribution of regular elements from aggregate orbit data makes a semigroup invariant accessible without enumerating inner inverses. The criterion explains precisely how comparable stabilizer types and duplicate targets can obstruct a whole monoid's regularity, including cases not distinguished by the list of orbit sizes. The table-of-marks census provides value beyond a restatement of the section criterion or the known permutation centralizer test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
