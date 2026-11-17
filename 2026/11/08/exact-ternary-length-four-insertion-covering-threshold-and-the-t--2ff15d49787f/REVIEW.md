# Independent mathematical audit

## correctness

PASS

PASS: Every 5-word target has at most five 4-word deletion parents. The explicit 31-word code covers all 243 targets and the explicit 33-word code also covers all targets while avoiding both deletion words 012 and 102. For a putative insertion cover failing deletion coverage, every forbidden three-word using <=2 distinct letters forces a 5-word all of whose four-word deletions contain it; only three-distinct-letter omissions remain, and all are alphabet permutations of 012. The exhaustive 81-center/243-target set-cover decision can therefore restrict to centers avoiding 012. The actual supplied C++17 checker implements complete branching on all eligible parents of an uncovered target, sound volume/packing pruning, memoization by covered-target bitmap at minimal selected count, and forced centers. Independently compiled and executed an equivalent exact-integer checker: C31/C33 witnesses valid, no cover <=30 (7,615,421 branch nodes), no 012-avoiding cover <=32 (23,213 nodes), CERTIFICATE_OK. The finite search is exhaustive with justified pruning, not sampling or mere timed-out infeasibility.

## originality

PASS

Best of knowledge: previous published exact alphabet-symmetric ternary four-word insertion covering gives minimum 39 and exhibits an unrestricted 31-word witness, explicitly leaves unrestricted optimum unknown; another general paper establishes covering non-equivalence without the sharp small ternary length-four threshold. The new independently certified LOWER bound 31 and exact 33-word first separation survive.

## value

PASS

PASS: These exact small finite covering numbers quantify a natural tight boundary between insertion and deletion covering. The 31 optimum is not a mere known-table recomputation: a complete 81-by-243 set-cover impossibility argument closes an explicit prior open lower-bound gap. The 33 separation measures the minimal cardinality cost of non-equivalence, a motivated structural invariant even without general asymptotic consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
