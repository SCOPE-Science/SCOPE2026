# Independent mathematical audit

## correctness

PASS

Frozen mathematics: for an outsider in a clique the closed trace consists of all codewords in that clique and its selected mate, if any. For ordinary location, two empty columns are forbidden; with at most one empty column, the same-clique traces are distinct, and cross-clique equality would require both cliques to have at most one codeword, impossible for n≥4. An empty column requires both cliques to be represented. The solid condition allows precisely the exceptional single-empty, all-other-double configurations, or fully occupied columns except the 2n singleton transversals with one selected vertex on one side. The single-deletion tests for these two families and their all-set counts check out. `python /workspace/reproductions/check_discrete_claims.py 3` compared all six original formulas against literal neighborhoods for n=4,5,6. Repaired mathematics: self-location forbids an empty column, whose trace contains only vertices from one clique and whose identifying intersection would contain that entire clique. An outsider with its selected mate needs at least two selected vertices in its own clique: zero gives only the mate's neighborhood, one leaves an additional vertex on the other side, and two distinct own-side neighbors eliminate all extra vertices. Thus count fully occupied columns and remove disjoint low-shore counts (n+1)z^n+nz^(n+1) for each shore. A double column allows a deletion on the shore with at least three selected vertices (total at least n+1≥5); all feasible singleton transversals are minimal, giving (2^n−2n−2)z^n. Self-location implies outsider antichain. Crown self-location forces a full shore or one doubly omitted column; in the latter case the prism condition fails. The shared sets consist of a full shore and at least two selected vertices on the other shore. Inclusion–exclusion over the full shores proves the shared polynomial. Ran `python /workspace/repairs/3/verify.py`: literal checks of all 5376 subsets in each graph for n=4,5,6 agree with the repaired enumerators and the solid family identity. The exact proofs cover all n≥4; the finite checks do not.

## originality

PASS

The frozen package cannot pass as a new three-family classification: the earlier crown solid-code classification determines the prism solid family exactly, not merely the same polynomial. The replacement at /workspace/repairs/3 narrows the new claim to the full and inclusion-minimal self-location enumerators in the prism and the count of sets self-locating in both graphs. It credits the known solid family as context, claims no novelty for known minima, and does not advance a new ordinary-location census. No prior coverage of the narrowed claim was established in the sources compared below.

## value

PASS

The surviving complete invariant distinguishes two effects of graph complementation under natural locating criteria: the solid code families are identical, while self-location has different minimal patterns in the two graphs. The exact prism polynomial, minimal-support classification, and shared-code polynomial identify the size and structure of the self-locating families with more information than the already-known minimum n. Value attaches to that structural remainder, not re-enumeration of the inherited solid family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
