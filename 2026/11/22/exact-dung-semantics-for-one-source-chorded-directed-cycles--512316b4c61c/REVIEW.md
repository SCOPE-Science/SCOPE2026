# Independent mathematical audit

## correctness

PASS

Use the complete three-valued labeling: IN iff all attackers are OUT, OUT iff an attacker is IN, and UNDEC otherwise. This is equivalent to a conflict-free defense fixed point with OUT exactly the attacked vertices. Propagate along 1,…,n−1 after assigning vertex 0. If 0 is UNDEC, the compulsory predecessor and any chord attacker are UNDEC at every step, so all are UNDEC. If 0 is OUT, each optional attack from 0 is neutral in the propagation; the bits alternate with the odds IN and closure at 0 requires n even. If 0 is IN, all targets in {1}∪K are OUT and the others alternate; along the suffix after h, n−1 is OUT iff n−1−h is even, exactly the closure condition at 0. Both nonempty cases are two-valued and stable. Preferred extensions are complete by maximal admissibility, so these nonempty cases give exactly the preferred extensions unless all-UNDEC is alone; empty is always grounded. For max K=k there are 2^(k−2) lower-target subsets and empty K contributes h=1. Summation over the required parity gives both stated formulas, including n=4,5 and K=∅; division by 2^(n−3) gives the two limits 1/3. Independent direct powerset enumeration confirmed 1,022 frameworks for n=4…12 and exact chord census through n=24. Replay: /workspace/branches/ef9810e0-36f7-4e77-88be-f9ce5b9a5dbc/independent_check.py with check_n12.log and census_n24.log. The supplied script was inspected, not run. Enumeration is finite corroboration, not the all-n proof.

## originality

PASS

The classical chordless boundary and generic kernel characterization overlap, but neither specifies which arbitrary sets of one-source chords admit the additional extension or the census over those sets. Reviewed related results do not imply the full three-valued classification.

## value

PASS

For an exponentially large perturbation family of the classical stable-existence obstruction, a single rightmost shortcut decides the additional stable alternative; the other shortcuts determine its vertices but not its existence. The rule also excludes any partially undecided nonempty complete extension. This yields an exact, finite-n labeled census and a sharp frequency, rather than recomputation of the classical chordless case or an application of a cycle-existence condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
