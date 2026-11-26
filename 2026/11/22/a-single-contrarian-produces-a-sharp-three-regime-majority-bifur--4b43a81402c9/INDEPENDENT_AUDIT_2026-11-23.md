# Independent mathematical audit

## correctness

PASS

The final repaired finding preserves all census formulas. At a=1 the opposite shore is uniform after one update and the two surviving bits obey (c,d)→(1−d,c), giving one four-cycle. At a=2 the opposite shore freezes whenever S=1; an initially unanimous first shore instead forces its sign on the opposite shore at step one. Splitting the fixed points by strict nonunanimous, unanimous, and tied opposite-shore patterns gives the three basin sizes; the step-two count is twice (2^b+H_b)/2. At a≥3, the two canonical first-shore patterns have strict signs, so two strict signs swap and two tied shores are fixed. The frozen proof reversed which pattern updates in the exactly-one-tie case: the tied shore becomes canonical and the strict shore holds. The repair makes this explicit; it implies the strict shore needs a second step exactly when noncanonical, producing the stated N2. No ties can return once lost, so doubly tied states have no distinct predecessors. Complementation gives the polar basin counts. The ordinary rule has the same strict-sign swap and single-tie resolution, giving configuration-wise invariance. Independent direct labeled replay: python3 /workspace/branches/review_checks.py (15,876 states, both sizes 1–6; checks entrance and individual basin counts and ordinary membership). Supplied scripts inspected but not executed; docs corrected to Python 3.10+ for int.bit_count. The proof, not finite tests, establishes the unbounded result. No formal verification. Corrected complete affected files: /workspace/repairs/3/RESULT.md and VERIFICATION.md.

## originality

PASS

The retained contribution is the exact all-size labeled census and oscillation-basin invariance for a one-vertex rule change. General period restrictions and the known undeleted criterion are not new. The strongest inspected comparisons do not give the census; this is a best-of-current-evidence judgment, not priority certification.

## value

PASS

A single contrary rule on a natural symmetric graph changes the realized primitive period sharply at shore sizes 1 and 2, but at 3 and above preserves the precise set of oscillating initial configurations. Exact basin and time-to-attractor formulas quantify those statements for every finite size and tie parity; they are more informative than a period upper bound or a small census. Scope is deterministic, synchronous and tie-retaining, not arbitrary local faults.

The dated certificate retains the supplied scientific assessment, sources and limitations.
