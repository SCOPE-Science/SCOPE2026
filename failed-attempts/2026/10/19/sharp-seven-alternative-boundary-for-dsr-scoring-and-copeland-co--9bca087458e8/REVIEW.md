# Independent mathematical audit

## correctness

PASS

Hou's strict-tournament specialization is exact: the domination case implies gamma eligibility; gamma tests the universal nonempty intersections because the pivot always beats the bottom block; beta tests a full intersection for an upper vertex. The empty-bottom branch contributes one point to each incoming neighbor. Set-valued score ties are retained. The independently written NumPy Boolean-adjacency census partitions the label-mask ranges into disjoint chunks, checks all 2, 8, 64, 1024, 32768 and 2097152 cases, and obtains 0, 0, 0, 0, 0 and 5040 failures. It verifies exact equality of the failing-mask set and the witness relabeling set, with all 7! masks distinct, and winner sizes (Copeland, DSR, intersection)=(1,2,1) throughout. Replay: python3 /workspace/reviews/evidence/dsr_census.py; output reviews/evidence/dsr_census.txt. Neither the original code nor a sample is relied on. The claim says nothing for n>=8.

## originality

FAIL

A distinct indexed Resultary result covers the same exact rule, boundary, labeled count, witness score vectors and all-failure orbit. Common winners and the incidence fraction are direct consequences. The comparison is evidence of duplicate scientific coverage in the current corpus, not of earlier authorship: the matched record path is dated November 2 and the assigned path October 19. Inaccessible journal papers are not the basis for failure.

## value

PASS

The sharp first counterexample and complete obstructing class answer a natural boundary question for a specific social choice rule. A single witness would not supply the universal lower-order guarantee, the frequency or the fact that the unique Copeland winner is always retained at the boundary. This is a useful exact comparison independently of the duplicate coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
