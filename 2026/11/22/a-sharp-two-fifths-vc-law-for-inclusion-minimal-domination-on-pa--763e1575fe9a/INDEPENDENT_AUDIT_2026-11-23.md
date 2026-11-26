# Independent mathematical audit

## correctness

PASS

For a dominating set, deleting a selected vertex destroys domination exactly if some genuine vertex is dominated uniquely by it; this gives the five-bit criterion around each selected center. The boundaries must exclude nonexistent private-neighbor candidates: for length zero there is no test, for length one both boundary exclusions apply to its sole center, and thereafter the leftmost and rightmost genuine centers get the appropriate exclusions. Appending support marks maintains one nonempty set of possible states per assignment class, universally over labels and existentially over the unset bits. Merging equal sets preserves future viability, and accepting requires each set to contain a terminal-valid state. Weighted path counting therefore gives the claimed formal series. An independent tuple-based regeneration using direct tests for the final two centers reproduced 206 reachable families, 140 terminal families, 79 rejected edges and graph SHA-256 745e40a73b2b4c98aa3dee965bd42ffe216cefd75c1ccb361d3d905f7650bd1d. It reproduced the dimensions through 20 and all 206 coordinates of w_(n+5)=w_n+2 at n=16,…,20, including the 78 minus-infinity coordinates at n=16. The fixed transition operation commutes with addition of 2 to a whole vector, so equality at lengths 16 and 21 guarantees it at the next pair and inductively at every later pair. The accepted maximum agrees with the stated floor on the base lengths and grows by 2 per five steps. Independent literal enumeration of dominating sets and selected-vertex deletion also matched every face count through length 13, including the displayed polynomials; this is corroboration, not the all-length step.

## originality

PASS

The closest same-family connected-path calculation covers only n≤11, and the closest all-length shattering result concerns a strict subfamily. Neither determines the unrestricted all-length VC law or its shattered-support enumerator.

## value

PASS

The path is a natural model where local feasibility and all simultaneous membership assignments can both be studied. The exact all-length law settles an open range of the connected-path computation and has a different growth rate from the maximal independent subclass. The weighted transfer also determines every shattered-support coefficient, not just the degree or an asymptotic estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
