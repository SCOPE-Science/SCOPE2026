# Independent mathematical audit

## correctness

PASS

For each of the k accepted words choose a length-two accepting path. Two chosen paths cannot share the middle state, since splicing them would accept an off-diagonal word. A middle state cannot be initial or final, since then a word of length one is accepted. Three such middle states with the same final force two distinct four-cycles sharing an edge at the initial state. Thus at least ceil(k/2) distinct finals are needed. Pairing the paths at their finals realizes this bound with four-cycles meeting only at the start and a pendant path for an odd singleton. A shared final attains the unrestricted bound k+2, including k=1,2 where the overhead is zero. The proof counts states, not transitions, and covers nonunambiguous NFAs.

## originality

FAIL

The exact finding is covered in the same model by a distinct indexed diagonal-language result, which also gives rigidity. Independently, the arbitrary-relation theorem in assigned record 3 implies all of the finding. Demonstrated coverage is decisive; this is not a claim about discovery order.

## value

FAIL

A sharp linear cactus overhead is a useful illustrative example, but the record contains only the already covered diagonal minima and their difference. It supplies neither a new exact invariant nor additional structure of minimizers beyond the indexed stronger diagonal result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
