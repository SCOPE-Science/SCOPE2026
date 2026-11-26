# Independent mathematical audit

## correctness

PASS

The two extreme 2-labels give weight 4. For n>=3, a feasible function of weight at most 4 must have a zero on each shore: if a whole shore is positive, at most one unit remains on the other, so the whole opposite shore must also be positive, which is too heavy. The two zero constraints therefore force both shore weights to be 2. If an A-positive index is at least 2, b_1 is positive (otherwise its guarding sum is below 2), then every a_i with i>=2 is positive. This is impossible for n>=4. For n=3 it forces x_2=x_3=1 and x_1=0; the two short B-prefixes force y_1=y_2=1 and y_3=0. In the other case a_1 carries both units and the zero a_n forces b_n=2. This fills the omitted shore-zero justification at weight 4 and the abbreviated n=3 argument in RESULT.md. An independent support/edge-list enumeration (branches/independent_small_replays.py half) reproduced 123949 bounded candidates for n=2..14, including (3,2) and (4,2) for n=2 and 3 (minimum, multiplicity), and the unique displayed optimum at each n=4..14. The proof, not the finite test, covers all n.

## originality

FAIL

The distinct indexed quasi-total result covers the entire frozen classification by an elementary low-weight implication, not just by a coincident numerical value. The ordinary Italian chain-graph enumerator independently covers the optimum multiplicities once one observes that each shore has weight 2 at any ordinary optimum of weight 4, so the ordinary >=2 inequalities become exact.

## value

FAIL

The exact rigidity threshold is natural, but the recorded statement adds no independently useful unknown classification to the available quasi-total theorem: only the short low-weight containment and the filtering of two listed boundary cases are needed. No distinct substantive remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
