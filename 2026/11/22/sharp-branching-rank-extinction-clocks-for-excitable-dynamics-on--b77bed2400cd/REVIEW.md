# Independent mathematical audit

## correctness

PASS

An excitation at time t>0 requires theta distinct predecessor excitations at t-1. Immediate spatial reversal would force the same vertex to be excited two updates apart, impossible for kappa>=3. Each causal walk is therefore a simple path, and unique paths from the root in a forest force injectivity of the entire selected witness, not just of each branch. No excitation is possible past H; all last excitations clear kappa-1 updates later and initially refractory states cannot delay extinction beyond this. To attain the bound, excite only the deepest leaves of a maximum witness. Inductively the only new excitations are its next shallower level, which is still at rest; an outside component has at most one attachment to the witness, and a vertex in the witness other than a parent gets at most one active neighbor. The root is nonzero at H+kappa-2, so absorbing rest is first reached at H+kappa-1. The argument includes H=0, isolated vertices, and disconnected forests. Counting witness vertices yields the displayed floor logarithm; pendant padding realizes every n, including n=1. The directed recurrence selects the theta-th largest independent branch height by truncating taller branches. Inspected both frozen scripts and their recorded output; did not rerun uploaded code. A distinct bounded script passed 1356 labelled-forest/parameter checks, including disconnected forests through order five and all initial states therein. This enumeration only tests ranks zero and one; higher ranks are established by the proof, not by those cases.

## originality

PASS

The same-day complete-tree witness and the earlier logarithmic degree-bound and density-budget results are material coverage of ideas or restricted conclusions. Credit these explicitly; the surviving claim is the exact all-forest shape invariant and attainment, across the stated thresholds and refractory lengths, with the sharp all-size integer law. Inspected statements do not supply that theorem. The same-day date does not settle order.

## value

PASS

The theorem resolves the sharp feasible excitation time on each fixed forest, distinguishing shapes with the same order or even large depth. The embedded complete branch witness is necessary and sufficient for worst-case delay and yields a computable invariant, plus a sharp logarithmic maximum attained at each size without a maximum-degree assumption.

The dated certificate retains the supplied scientific assessment, sources and limitations.
