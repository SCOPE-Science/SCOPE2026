# Independent mathematical audit

## correctness

PASS

The directed de Bruijn edge counts forget endpoints but retain multiplicities. In a balanced feasible graph every active vertex is a possible start, giving distinct words unless there is only one active vertex, when the two constant sequences contribute 2z/(1-z). Unbalanced vectors determine endpoints. Last exits from the nonterminal vertices form a rooted in-tree; conversely a rooted last-exit tree and ordered outgoing lists yield a trail: degree balance permits stopping only at the terminal, and unused edges would then force unused last exits along a tree path into that terminal. For each branch the number of local orders is one exactly when its marked last-exit type has multiplicity one; the terminal may have at most one type. Independently reproduced the exact OGF with python3 /workspace/checks/trigram_certificate.py. The reproduction uses a directed matrix-tree determinant for edge types and deletes forbidden last exits in a second determinant. It checks exact coefficients through window count 48, with a degree-41 numerator bound over (1-z)^3(1-z^2)(1-z^3)(1-z^4) obtained by summing the affine multiplicity ranges; hence this is an all-length certificate, not interpolation or a short-length test alone. Counts match the listed values. Dividing the numerator by the three regular factors at 1 gives value 1 and derivative -29/2; the other poles are simple roots of unity. This gives the stated n^2/2+14n+O(1) after shifting t=n-2. The determination does not cover cyclic words, supplied endpoints, or longer reads.

## originality

FAIL

A distinct Resultary finding gives the same unanchored singleton counts for every n>=3 and the same asymptotic, in an exactly equivalent quasipolynomial presentation. This is full mathematical coverage, not a conclusion about historical priority or independent provenance from the later date label.

## value

FAIL

The singleton-fiber census is a natural exact reconstruction invariant, but the distinct indexed law already fixes every coefficient and both stated leading terms. Re-expressing that complete count by a rational OGF is not a remaining independent scientific contribution, and no additional structural result is the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
