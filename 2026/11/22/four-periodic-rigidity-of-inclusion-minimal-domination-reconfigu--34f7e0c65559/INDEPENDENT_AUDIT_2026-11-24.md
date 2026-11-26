# Independent mathematical audit

## correctness

PASS

A cyclic dominating word has no zero run of length >=3; minimality forbids a one run of length >=3 and requires two zeros on each side of every 11 for private witnesses. These conditions are sufficient: a singleton uses itself and each endpoint of 11 uses its exterior adjacent zero. For a mixed word the slide 11001→10101 leaves the exterior gaps unchanged. For all singletons, unequal adjacent gaps can be swapped by a slide; for constant gaps two one can split a token into its two vacant neighbours, and for constant gaps one one can merge a 101, yielding independent dominating words in both cases for n>=6. All-double words are the four 1100 shifts; the only candidate moves are slides, which for n>=8 deprive a distinct intact 11 of its adjacent private witness. C3 singletons and C4 pairs are all mobile; the two alternating C4 pairs each have an adjacent consecutive pair. This proves the full classification, not connectivity beyond the isolated-state obstruction. Independently ran checks/1.py (Python 3 standard library): private-witness/explicit set-move enumeration for 3<=n<=14 and 11-bit-window automaton by source/sink peeling, leaving exactly the periodic directed four-cycle for the n>=11 check. For the automaton, changes occur only within distance one of the move centre and the private-witness predicate reads radius two, so centre offsets -3..3 contain all affected tests. The run proof stands independently of computation.

## originality

PASS

The distinct claim is the all-cycle classification of isolated inclusion-minimal dominating states under the exact expansion/contraction rule. Beaton supplies the move model and other graph-family results, but the checked statements do not yield the classification. Two four-periodic analogues use different feasibility or transitions. The conclusion is bounded by checked sources, not a priority certificate.

## value

PASS

This gives a complete structural classification under a move model that allows changing the number of selected vertices, not just a disconnection example. It provides exact periodic obstructions for a natural connected 2-regular family, explains why C4 is exceptional, and gives an explicit move certificate for the complement of the frozen states. It makes no claim about the component structure of those mobile states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
