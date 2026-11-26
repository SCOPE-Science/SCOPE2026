# Independent mathematical audit

## correctness

PASS

Length-one overlap exclusion makes the first- and last-symbol sets disjoint. Over three symbols, reversal and relabeling can therefore always place a nonempty code among the 48 unbordered length-five words with starts in {0,2} and end 1. A checked conflict clique can meet a legal code at most once. The 28 weighted groups cover every eligible word with numerator at least 16, and their total numerator is 98, so 16|C|≤98 and |C|≤6. Independently rebuilt compatibility graphs and an exact coloring-bounded clique census confirmed the six-word witness, checked all 954 within-group pairs of the frozen certificate, and found (T_n,E_n)=(1,6),(2,18),(3,60),(6,72) at n=2,3,4,5. Comparing complete sets of codebooks under common alphabet relabeling and global reversal verified all seven listed orbit representatives and sizes 12,12,12,6,12,12,6, not just their total. A separate run without the deletion conflict confirmed 17. At length one the sole deletion descendant of every word is empty, so the first blocklength with at least four messages is indeed five. Deletion may occur at any coordinate of the identified word.

## originality

PASS

The exact uncorrected maximum 17 is established prior coverage, not the contribution. The inspected primary table and the closest indexed deletion and substitution results do not give the joint single-deletion/non-overlap maxima, labeled counts, or symmetry classes.

## value

PASS

The finite cutoff has a concrete coding interpretation: length five is the smallest ternary blocklength carrying four messages with both framing and single-deletion correction. The sharp comparison 17 versus 6 isolates the cost of the added constraint at that length. The upper certificate and complete equality classification identify all optimal designs up to the natural symmetries, rather than reporting a single feasible code or recomputing the known uncorrected table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
